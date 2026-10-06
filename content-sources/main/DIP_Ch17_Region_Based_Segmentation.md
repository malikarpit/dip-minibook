---
id: "C17"
title: "Region-Based Segmentation"
layer: "MAIN"
part: "III — Understanding Image Content"
unit: "III"
version: "1.0"
status: "REFERENCE BUILD"
syllabus_scope:
  - "Region-based segmentation"
  - "Region growing"
  - "Region splitting and merging"
tags:
  - "CORE"
  - "EXAM"
  - "MATH"
  - "DEEP DIVE"
  - "LAB"
  - "SEGMENTATION"
  - "REGIONS"
prerequisites:
  - "C10"
  - "C15"
  - "C16"
related:
  - "C18"
  - "C19"
  - "C20"
  - "C25"
math:
  - "M05"
  - "M06"
  - "M08"
lab:
  - "LAB-U3-03"
  - "LAB-U3-04"
exam:
  - "EXAM-U3"
practice:
  - "P-C17"
assets:
  - "D-C17-01"
  - "D-C17-02"
  - "D-C17-03"
---

# Chapter 17 — Region-Based Segmentation

> **Chapter thesis**  
> Thresholding makes a decision mainly from pixel values. Region-based segmentation adds spatial context by asking which neighbouring pixels belong together. The central idea is **homogeneity + connectivity**: a good region should be internally consistent according to a chosen criterion and spatially coherent according to a chosen connectivity rule.

**Part III — Understanding Image Content**  
**Syllabus anchor:** Unit III explicitly includes region-based segmentation after global/adaptive thresholding. fileciteturn4file0L41-L45

---

# 17.0 Why Region-Based Segmentation?

C16 showed that a threshold can classify pixels:

```text
pixel
 ↓
compare with T
 ↓
label
```

But consider:

```text
same intensity
+
different spatial locations
```

A threshold cannot tell whether two equal-valued pixels belong to the same physical object.

Region methods add:

```text
pixel value
+
neighbours
+
connectivity
+
region statistics
```

The conceptual shift is:

```text
PIXEL DECISION
       ↓
NEIGHBOUR-AWARE DECISION
       ↓
REGION
```

---

# 17.1 What Is a Region?

A region \(R\) is a connected set of image pixels that satisfies a chosen homogeneity or membership criterion.

A useful conceptual definition is:

\[
P(R)=\text{true}
\]

where \(P\) is the predicate that determines whether \(R\) is sufficiently homogeneous.

A region should typically be:

```text
connected
+
internally homogeneous
+
meaningful for the task
```

These are design conditions, not universal mathematical requirements for every segmentation framework.

---

# 17.2 Region Segmentation Components

A region-based method usually needs:

```text
1. feature / value representation
2. connectivity definition
3. homogeneity predicate
4. initialization
5. growth or partition strategy
6. stopping criterion
7. post-processing
```

Therefore the algorithm is more than:

> “compare neighbouring pixels.”

---

# 17.3 Homogeneity Criteria

A region can be considered homogeneous using:

### Intensity difference

\[
|f(x,y)-\mu_R|<\tau
\]

### Range

\[
\max(R)-\min(R)<\tau
\]

### Variance

\[
\sigma_R^2<\tau
\]

### Colour distance

\[
\|\mathbf c-\boldsymbol\mu_R\|<\tau
\]

### Texture similarity

A task-specific texture descriptor can be used.

The criterion should match the problem.

---

# 17.4 Region Growing

Region growing starts with one or more seed points and expands a region by adding neighbouring pixels that satisfy the membership rule.

Conceptually:

```text
seed
 ↓
inspect neighbours
 ↓
test homogeneity
 ↓
accept valid pixels
 ↓
new boundary
 ↓
repeat
```

It is naturally spatial and can therefore outperform purely histogram-based methods when connected structure matters.

---

# 17.5 Basic Region-Growing Algorithm

```text
Input:
    image I
    seed S
    tolerance τ

Initialize region R = {S}

repeat:
    inspect neighbours of R
    for each candidate pixel p:
        if p satisfies membership criterion:
            add p to R
until no more pixels are added

return R
```

This is a conceptual algorithm.

Production implementations need explicit handling of:

- visited pixels,
- queues/stacks,
- boundary conditions,
- update strategy for region statistics.

---

# 17.6 Membership Rule

A simple rule is:

\[
|f(p)-\mu_R|<\tau
\]

where:

- \(f(p)\) = candidate pixel value,
- \(\mu_R\) = current region mean,
- \(\tau\) = tolerance.

This is adaptive during growth because \(\mu_R\) can change as the region expands.

---

# 17.7 Worked Region-Growing Example

Consider:

\[
I=
\begin{bmatrix}
10&11&12&90\\
10&12&13&92\\
11&13&14&91\\
80&82&84&90
\end{bmatrix}
\]

Seed:

\[
S=(1,1)
\]

assuming one-based matrix coordinates for this example.

Initial region:

\[
R=\{10\}
\]

Take:

\[
\tau=5
\]

Early neighbours:

```text
10
11
12
10
12
13
...
```

are close to the seed/region mean.

Values around:

```text
80–92
```

are much farther away.

The region therefore tends to remain around the upper-left low-intensity structure.

---

# 17.8 Why the Current Mean Matters

Suppose the region contains:

\[
10,11,12,13
\]

Then:

\[
\mu_R=
\frac{10+11+12+13}{4}
=
11.5
\]

For candidate:

\[
15
\]

the difference is:

\[
|15-11.5|=3.5
\]

If:

\[
\tau=5
\]

it passes.

For:

\[
20
\]

we have:

\[
|20-11.5|=8.5
\]

so it fails.

The membership boundary therefore moves with the region statistics.

---

# 17.9 Seed Selection

Seed selection is critical.

A good seed should be:

```text
inside the desired region
+
representative of it
+
away from strong boundaries when possible
```

A bad seed can:

```text
grow into the wrong region
```

or fail to grow enough.

---

# 17.10 Manual vs Automatic Seeds

### Manual

User chooses:

```text
click point
```

Useful for:

- interactive segmentation,
- demonstrations,
- difficult images.

### Automatic

Seeds can be generated from:

- local extrema,
- threshold masks,
- connected components,
- feature detectors,
- prior models.

Automatic seed generation makes the method scalable.

---

# 17.11 Multiple Seeds

For multiple regions:

```text
seed A
seed B
seed C
```

all can grow.

A common conceptual strategy is:

```text
unassigned pixel
→ evaluate nearby region candidates
→ assign according to criterion
```

This can produce a partition of the image.

---

# 17.12 Region Growing and Connectivity

A candidate must usually satisfy:

```text
homogeneity
+
connectivity
```

A pixel with matching intensity but no path of valid neighbours should not automatically join the region.

This is one of the strongest differences between:

```text
histogram-based classification
```

and:

```text
region-based segmentation
```

---

# 17.13 4-Connectivity

For pixel \(P\):

```text
  N
W P E
  S
```

Neighbours are:

\[
N,S,E,W
\]

This avoids diagonal-only connections.

---

# 17.14 8-Connectivity

Adds diagonal neighbours:

```text
NW N NE
 W P E
SW S SE
```

This creates more connected structures.

The choice should be deliberate.

---

# 17.15 Connectivity and Region Shape

Consider:

```text
1 0
0 1
```

With 4-connectivity:

```text
two regions
```

With 8-connectivity:

```text
one region
```

Therefore connectivity changes topology.

That is an important practical and exam observation.

---

# 17.16 Stopping Criteria

Region growth can stop when:

```text
no valid neighbours remain
```

or when:

```text
region reaches desired size
```

or:

```text
region statistics stop satisfying constraints
```

or:

```text
boundary condition is encountered
```

The stopping rule is part of the segmentation design.

---

# 17.17 Region Growing Failure — Leakage

A major failure is **region leakage**.

Suppose an object has a gradual intensity gradient:

```text
100 → 105 → 110 → 115 → 120
```

and tolerance is too generous.

The region may continue into background.

Conceptually:

```text
target object
████████████
          █
          █
          █████ background
```

This is a common reason to combine intensity similarity with edge or boundary constraints.

---

# 17.18 Region Growing Failure — Fragmentation

If tolerance is too small:

```text
one object
→ several small regions
```

This is over-segmentation.

Therefore:

```text
small τ
→ fragmentation risk

large τ
→ leakage risk
```

---

# 17.19 Combining Homogeneity and Edge Evidence

A stronger rule can use:

\[
|f(p)-\mu_R|<\tau
\]

and:

\[
|\nabla f(p)|<\gamma
\]

for growth across relatively smooth areas.

This says:

```text
candidate is similar
+
boundary crossing is not too strong
```

The exact combined criterion depends on the application.

---

# 17.20 Region Splitting

Region splitting starts with a large region, often the full image, and tests whether it is homogeneous.

If not:

```text
split
```

The image is recursively partitioned.

A conceptual quadtree split is:

```text
┌─────────────┐
│             │
│             │
│             │
│             │
└─────────────┘

        ↓

┌──────┬──────┐
│      │      │
├──────┼──────┤
│      │      │
└──────┴──────┘
```

Each region is tested again.

---

# 17.21 Region Splitting Predicate

Suppose:

\[
P(R)=
\begin{cases}
\text{true},&\sigma_R^2<\tau\\
\text{false},&\sigma_R^2\ge\tau
\end{cases}
\]

Then:

```text
variance low
→ region acceptable

variance high
→ split region
```

This is a simple statistical predicate.

---

# 17.22 Region Merging

After splitting, neighbouring regions with compatible statistics can be merged.

Conceptually:

```text
split too much
     ↓
compare neighbouring regions
     ↓
merge compatible regions
     ↓
final segmentation
```

This gives the classical:

```text
SPLIT + MERGE
```

framework.

---

# 17.23 Split-and-Merge Workflow

```text
whole image
    ↓
test homogeneity
    ↓
split non-homogeneous regions
    ↓
obtain small regions
    ↓
test adjacent pairs
    ↓
merge compatible regions
    ↓
final region partition
```

This method balances:

```text
under-segmentation
↔
over-segmentation
```

through complementary operations.

---

# 17.24 Quadtree Representation

For square images, recursive four-way splitting naturally forms a quadtree.

Conceptually:

```text
ROOT
├── Q1
│   ├── ...
│   └── ...
├── Q2
├── Q3
└── Q4
```

The hierarchy stores:

```text
large homogeneous regions
+
smaller subdivisions where needed
```

This is useful for adaptive image representations.

---

# 17.25 Region Merging Criterion

Two regions \(R_1,R_2\) can be merged if their combined statistics satisfy a homogeneity predicate.

For example:

\[
|\mu_{R_1}-\mu_{R_2}|<\tau
\]

This checks mean similarity.

A more robust criterion can consider:

- variance,
- colour,
- texture,
- boundary strength,
- region size.

---

# 17.26 Worked Merge Example

Suppose:

\[
\mu_{R_1}=100
\]

\[
\mu_{R_2}=103
\]

and:

\[
\tau=5
\]

Then:

\[
|100-103|=3<5
\]

so the mean-similarity criterion allows a merge.

If:

\[
\mu_{R_2}=110
\]

then:

\[
|100-110|=10
\]

and the regions remain separate under this criterion.

---

# 17.27 Region Splitting vs Region Growing

| Method | Starting point | Main action | Main parameter |
|---|---|---|---|
| region growing | seed(s) | expand | similarity/tolerance |
| region splitting | large regions | divide | homogeneity threshold |
| merging | small/adjacent regions | combine | compatibility threshold |
| split-and-merge | full image | divide then combine | both |

---

# 17.28 Region-Based vs Thresholding

| Property | Thresholding | Region-based |
|---|---|---|
| core evidence | value | value + spatial context |
| connectivity | optional/post-process | fundamental |
| initialization | threshold | seed or initial partition |
| illumination sensitivity | high for global methods | can be better with local criteria |
| parameterization | \(T\) | seed, tolerance, homogeneity |
| complexity | low | higher |

---

# 17.29 Region-Based vs Edge-Based Segmentation

### Edge-based

```text
find boundaries
→ infer regions
```

### Region-based

```text
find coherent regions
→ infer boundaries
```

They are almost complementary strategies.

A strong system can combine both.

---

# 17.30 Region Adjacency Graph

> **EXTENSION**

Once the image is partitioned into regions, create a graph:

```text
node = region
edge = adjacency
```

Conceptually:

```text
R1 ── R2
│     │
R3 ── R4
```

Each node can store:

```text
mean
variance
area
colour
texture
```

Merging then becomes a graph operation.

This creates a bridge between classical segmentation and graph-based image analysis.

---

# 17.31 Region Statistics

For region \(R\):

### Area

\[
A_R=|R|
\]

### Mean

\[
\mu_R=
\frac1{|R|}
\sum_{p\in R}f(p)
\]

### Variance

\[
\sigma_R^2=
\frac1{|R|}
\sum_{p\in R}
[f(p)-\mu_R]^2
\]

These statistics can drive segmentation decisions.

---

# 17.32 Worked Region Statistics

Suppose region values are:

\[
[10,12,11,13]
\]

Mean:

\[
\mu_R=
\frac{46}{4}
=
11.5
\]

Variance:

\[
\sigma_R^2=
\frac{
(10-11.5)^2+
(12-11.5)^2+
(11-11.5)^2+
(13-11.5)^2
}{4}
\]

\[
=
\frac{2.25+0.25+0.25+2.25}{4}
\]

\[
=
\frac5{4}
\]

\[
\boxed{1.25}
\]

The region is relatively homogeneous under this simple intensity criterion.

---

# 17.33 Region Growing with Colour

For RGB:

\[
\mathbf c(p)=
[R(p),G(p),B(p)]^T
\]

A simple criterion is:

\[
\|\mathbf c(p)-\boldsymbol\mu_R\|_2<\tau
\]

where \(\boldsymbol\mu_R\) is the region's mean colour vector.

This incorporates multiple channels.

---

# 17.34 Why Colour Space Matters

If the RGB representation mixes brightness and chromatic changes unfavourably, a region criterion may become unstable under lighting variation.

A different colour representation may improve separability.

Therefore:

```text
region-growing rule
depends on
feature representation
```

This links C05 to C17.

---

# 17.35 Region Growing with Texture

A candidate pixel or local patch can be represented by:

```text
local mean
local variance
gradient statistics
texture descriptor
```

Then the membership condition can operate on that feature vector.

Conceptually:

\[
\|\mathbf z(p)-\boldsymbol\mu_R\|<\tau
\]

where \(\mathbf z\) is a chosen feature vector.

This is a bridge toward feature-based segmentation.

---

# 17.36 Seeded vs Unseeded Segmentation

### Seeded

Starts from known seed points.

Advantages:

```text
strong user/control
specific target
```

### Unseeded

Automatically determines regions.

Advantages:

```text
scalable
less manual intervention
```

The complexity shifts into:

```text
automatic initialization
```

---

# 17.37 Practical Example — Medical-Style Region

Suppose a target structure has approximately homogeneous intensity but is surrounded by a gradual intensity transition.

A global threshold may fragment it.

Region growing can use:

```text
seed inside target
+
local similarity
+
edge-aware stopping
```

This may produce a more connected structure.

But the exact performance depends on the image modality and noise.

---

# 17.38 Practical Example — Natural Scene

Suppose:

```text
sky
trees
buildings
```

have overlapping intensities but different spatial structure.

A region-growing criterion could exploit:

```text
intensity
+
colour
+
gradient
```

However, complex natural scenes frequently violate simple homogeneity assumptions.

Learned segmentation may then be preferable.

---

# 17.39 Region-Based Segmentation and Morphology

After region segmentation:

```text
small holes
small islands
gaps
```

may remain.

Morphological operations can refine the result.

This connection becomes central in C18.

---

# 17.40 Computational Cost

A region-growing algorithm can approach:

\[
O(MN)
\]

for simple single-pass visitation, although practical cost depends on:

- neighbourhood size,
- data structures,
- feature computation,
- repeated statistics,
- multiple seeds.

Split-and-merge can involve hierarchical recursion and graph operations.

The complexity depends strongly on implementation.

---

# 17.41 Queue-Based Region Growing

A robust implementation commonly maintains:

```text
queue
visited mask
region mask
region statistics
```

Conceptually:

```text
seed
 ↓
enqueue
 ↓
pop pixel
 ↓
inspect neighbours
 ↓
accept → enqueue
 ↓
repeat
```

The visited structure prevents infinite revisiting.

---

# 17.42 Pseudocode — Queue Version

```text
initialize queue with seed
initialize visited
initialize region

while queue not empty:

    p = pop(queue)

    for q in neighbours(p):

        if q is already visited:
            continue

        mark q visited

        if q satisfies membership criterion:
            add q to region
            push q into queue

return region
```

For a dynamic region-mean criterion, update the statistics when a pixel is accepted.

---

# 17.43 Boundary-Aware Region Growing

A stronger pipeline can be:

```text
candidate q
   ↓
similarity test
   ↓
edge-strength test
   ↓
inside image?
   ↓
not previously visited?
   ↓
accept/reject
```

This illustrates how several classical DIP chapters can be combined into one algorithm.

---

# 17.44 Parameter Sensitivity

Vary:

```text
seed
tolerance τ
connectivity
window/feature scale
edge constraint γ
```

Then inspect:

```text
region area
boundary
leakage
fragmentation
IoU/Dice
```

This shows whether the method is stable.

---

# 17.45 Common Failure Patterns

### Leakage

Tolerance too high.

### Fragmentation

Tolerance too low.

### Boundary stopping

Strong edge prevents desired growth.

### Wrong seed

Starts outside the target.

### Illumination drift

Region statistics change across the object.

### Texture

Within-object texture violates homogeneity.

---

# 17.46 Region Growing vs Adaptive Thresholding

Both use local information.

But:

```text
adaptive threshold
→ computes local decision threshold

region growing
→ explicitly builds connected regions
```

The latter has stronger spatial identity.

---

# 17.47 Region Merging and Object Meaning

Two adjacent regions can be numerically similar but semantically different.

Example:

```text
two adjacent materials
same mean intensity
```

A blind merge would be incorrect.

This is a reminder:

> Homogeneity is a numerical property; semantic identity is a task-level property.

---

# 17.48 Segmentation Quality Measures

Once regions are produced, evaluate:

\[
IoU=
\frac{|A\cap B|}{|A\cup B|}
\]

\[
Dice=
\frac{2|A\cap B|}
{|A|+|B|}
\]

and if appropriate:

```text
boundary accuracy
precision
recall
component count
area error
```

Different tasks require different metrics.

---

# 17.49 Worked Region IoU Example

Prediction area:

\[
|A|=120
\]

Ground truth:

\[
|B|=100
\]

Intersection:

\[
|A\cap B|=80
\]

Union:

\[
120+100-80=140
\]

Therefore:

\[
IoU=
\frac{80}{140}
\]

\[
\boxed{\approx0.5714}
\]

A reasonable overlap exists, but substantial segmentation error remains.

---

# 17.50 Engineering Decision Tree

```text
Do regions have reasonably homogeneous interiors?
        │
       YES
        ↓
Can useful seeds be identified?
        │
       YES
        ↓
Region growing
        │
       NO
        ↓
Can image be recursively partitioned?
        │
       YES
        ↓
Split / split-and-merge
        │
       NO
        ↓
Use richer features or learned segmentation
```

This is a conceptual selector, not a mandatory sequence.

---

# 17.51 Reproducible Experiment

Record:

```text
image
preprocessing
feature representation
connectivity
seed points
homogeneity criterion
tolerance
stopping rule
post-processing
evaluation metric
```

Without these, a region-growing result is difficult to reproduce.

---

# 17.52 Common Traps

## Trap 1 — “Region growing is just thresholding repeatedly.”

False.

Region growing explicitly uses connectivity and region evolution.

## Trap 2 — “A similar-valued pixel always belongs to the same region.”

False.

It must also satisfy the spatial/region membership logic.

## Trap 3 — “Large tolerance is safer.”

False.

It increases leakage.

## Trap 4 — “Small tolerance is safer.”

False.

It can fragment the target.

## Trap 5 — “Seed selection doesn't matter.”

False.

It can determine the entire growth path.

## Trap 6 — “Split-and-merge always produces optimal regions.”

False.

The result depends on the homogeneity and merging criteria.

## Trap 7 — “4- and 8-connectivity are interchangeable.”

False.

They can produce different component topology.

## Trap 8 — “Region similarity equals semantic similarity.”

False.

Two semantically different objects may be statistically similar.

---

# 17.53 Exam Formula Sheet

### Region mean

\[
\boxed{
\mu_R=
\frac1{|R|}
\sum_{p\in R}f(p)
}
\]

### Region variance

\[
\boxed{
\sigma_R^2=
\frac1{|R|}
\sum_{p\in R}
[f(p)-\mu_R]^2
}
\]

### Example homogeneity predicate

\[
\boxed{
|f(p)-\mu_R|<\tau
}
\]

### Colour-vector predicate

\[
\boxed{
\|\mathbf c(p)-\boldsymbol\mu_R\|_2<\tau
}
\]

### IoU

\[
\boxed{
IoU=
\frac{|A\cap B|}
{|A\cup B|}
}
\]

### Dice

\[
\boxed{
Dice=
\frac{2|A\cap B|}
{|A|+|B|}
}
\]

---

# 17.54 Exam-Style Problem — Region Mean

Region values:

\[
[20,22,24,26]
\]

Mean:

\[
\mu_R=
\frac{20+22+24+26}{4}
\]

\[
=
\frac{92}{4}
\]

\[
\boxed{23}
\]

For candidate:

\[
p=27
\]

and:

\[
\tau=5
\]

difference:

\[
|27-23|=4<5
\]

so it is accepted under the stated criterion.

---

# 17.55 Exam-Style Problem — Region Variance

Values:

\[
[10,12,14]
\]

Mean:

\[
\mu=12
\]

Variance:

\[
\sigma^2=
\frac{
(10-12)^2+
(12-12)^2+
(14-12)^2
}{3}
\]

\[
=
\frac{4+0+4}{3}
\]

\[
\boxed{\frac83\approx2.667}
\]

---

# 17.56 Exam-Style Problem — Merge Criterion

Two neighbouring regions have:

\[
\mu_1=70,\qquad\mu_2=73
\]

If:

\[
\tau=5
\]

then:

\[
|\mu_1-\mu_2|=3<5
\]

so they can merge under the simple mean-similarity predicate.

---

# 17.57 Cross-Book Bridges

> **C15 BRIDGE**  
> Region-based methods implement the general segmentation idea using explicit connectivity and homogeneity.

> **C16 BRIDGE**  
> Thresholding provides candidate seeds and demonstrates the pixel-decision foundation.

> **C10 BRIDGE**  
> Gradient/edge strength can prevent region leakage across strong boundaries.

> **C18 BRIDGE**  
> Morphology cleans region masks and can connect/break structures according to shape.

> **C19–C20 BRIDGE**  
> Features can replace simple intensity as region-membership evidence.

> **LAB BRIDGE**  
> Implement seeded region growing, split-and-merge and compare 4/8-connectivity.

> **PRACTICE BRIDGE**  
> Calculate region statistics, trace region growth, analyze leakage/fragmentation and evaluate masks.

> **EXAM BRIDGE**  
> Explain region growing, seed selection, homogeneity predicates, region splitting/merging and connectivity.

---

# 17.58 Quick Recall

```text
REGION
→ connected + homogeneous

GROWING
→ seed → expand

SPLITTING
→ large region → smaller regions

MERGING
→ compatible neighbours → larger regions

KEY PARAMETERS
→ seed
→ connectivity
→ tolerance
→ homogeneity
```

Core rule:

> **Region segmentation adds spatial identity to numerical similarity.**

---

# 17.59 Chapter Checkpoint

1. Define a region.
2. Why does region-based segmentation add information beyond thresholding?
3. Define region growing.
4. Write a basic homogeneity predicate.
5. Explain why seed selection matters.
6. Compare 4- and 8-connectivity.
7. What causes region leakage?
8. What causes region fragmentation?
9. Explain region splitting.
10. Explain region merging.
11. Describe split-and-merge segmentation.
12. What is a region adjacency graph?
13. Calculate region mean and variance.
14. How can colour-vector similarity drive region growing?
15. How can gradient information constrain region growth?
16. Compare thresholding, edge-based and region-based segmentation.
17. Explain the effect of tolerance on leakage and fragmentation.
18. How should a region-growing experiment be evaluated?
19. Why is numerical homogeneity not the same as semantic identity?
20. Design a region-based segmentation pipeline for an image with uneven illumination.

---

# 17.60 Connection Forward

Region methods produce masks and connected regions, but those masks often contain:

```text
holes
small specks
broken boundaries
thin protrusions
```

The next chapter introduces a language for manipulating image shapes:

```text
C18
MATHEMATICAL MORPHOLOGY

structuring element
→ erosion
→ dilation
→ opening
→ closing
→ boundary extraction
→ connected shape reasoning
```

This is the bridge from **regions as data** to **shape as structure**.
