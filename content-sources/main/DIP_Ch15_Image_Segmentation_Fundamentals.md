---
id: "C15"
title: "Image Segmentation Fundamentals"
layer: "MAIN"
part: "III — Understanding Image Content"
unit: "III"
version: "1.0"
status: "REFERENCE BUILD"
syllabus_scope:
  - "Image segmentation"
  - "Segmentation fundamentals"
  - "Object/region separation"
tags:
  - "CORE"
  - "EXAM"
  - "MATH"
  - "DEEP DIVE"
  - "LAB"
  - "VISION"
  - "SEGMENTATION"
prerequisites:
  - "C07"
  - "C09"
  - "C10"
  - "C14"
related:
  - "C16"
  - "C17"
  - "C18"
  - "C19"
  - "C20"
  - "C25"
  - "C28"
math:
  - "M05"
  - "M06"
  - "M08"
lab:
  - "LAB-U3-01"
  - "LAB-U3-02"
exam:
  - "EXAM-U3"
practice:
  - "P-C15"
assets:
  - "D-C15-01"
  - "D-C15-02"
  - "D-C15-03"
---

# Chapter 15 — Image Segmentation Fundamentals

> **Chapter thesis**  
> Segmentation turns an image from a single field of pixels into a collection of meaningful regions, candidate objects, or semantic areas. It is the bridge between low-level image processing and higher-level image understanding. The central design problem is not simply “split the image,” but **choose a representation and criterion that separates the structures required by the task while controlling false splits and false merges.**

**Part III — Understanding Image Content**  
**Syllabus anchor:** Unit III explicitly includes image segmentation, with thresholding, region-based segmentation and related feature/morphology methods developed in the same unit. fileciteturn4file0L41-L45

---

# 15.0 Why Segmentation Is a Major Change in the Pipeline

Part II focused primarily on:

```text
improve / transform image
```

Part III changes the question:

```text
what regions or objects are present?
```

A simplified pipeline becomes:

```text
raw / processed image
        ↓
segmentation
        ↓
regions / masks / candidate objects
        ↓
features
        ↓
classification / detection / analysis
```

Segmentation is therefore a structural transition.

---

# 15.1 What Is Image Segmentation?

**Image segmentation** is the process of partitioning an image into regions or assigning pixels to groups according to some criterion.

Possible goals include:

```text
foreground vs background
object A vs object B
tissue vs background
road vs non-road
land-cover classes
regions of similar intensity
```

The word **region** is deliberately broad.

Segmentation does not always produce object identities.

---

# 15.2 Segmentation vs Classification vs Detection

These terms are related but not interchangeable.

### Classification

Answers:

> What class does the image, crop or sample belong to?

### Object detection

Answers:

> Which objects are present, what classes are they, and where are they approximately located?

### Segmentation

Answers:

> Which pixels belong to which region/object/class?

Conceptually:

```text
classification
→ one/few labels

detection
→ objects + locations

segmentation
→ pixel-level regions
```

Later chapters revisit these distinctions.

---

# 15.3 Binary Segmentation

The simplest segmentation has two groups:

```text
foreground
background
```

A binary mask can be written:

\[
M(x,y)\in\{0,1\}
\]

For example:

\[
M(x,y)=
\begin{cases}
1,&\text{foreground}\\
0,&\text{background}
\end{cases}
\]

The mask is not necessarily the final image.

It is a representation of a selected region.

---

# 15.4 Multi-Class Segmentation

A multi-class segmentation may assign:

\[
M(x,y)\in\{0,1,\ldots,K-1\}
\]

where each label corresponds to a class or region.

Example:

```text
0 → background
1 → road
2 → vehicle
3 → building
```

This is more expressive than a binary mask.

---

# 15.5 Semantic vs Instance Segmentation

> **EXTENSION**

### Semantic segmentation

Every pixel receives a semantic class:

```text
all cars → class "car"
```

### Instance segmentation

Different objects of the same class receive different identities:

```text
car 1
car 2
car 3
```

So:

```text
semantic
→ what category?

instance
→ which object instance?
```

The classical threshold/region methods in this part can generate regions, but modern semantic/instance segmentation typically uses learned models.

---

# 15.6 What Information Can Segmentation Use?

A segmentation criterion can be based on:

### Intensity

```text
bright vs dark
```

### Colour

```text
red vs green
```

### Texture

```text
smooth vs patterned
```

### Edges

```text
strong boundaries
```

### Spatial connectivity

```text
nearby similar pixels
```

### Motion

```text
moving vs static regions
```

### Learned features

```text
CNN/transformer representations
```

Therefore segmentation is a **family of problems**, not one algorithm.

---

# 15.7 Main Classical Segmentation Families

This MiniBook organizes classical segmentation as:

```text
EDGE-BASED
     ↓
THRESHOLD-BASED
     ↓
REGION-BASED
     ↓
MORPHOLOGY-AIDED
     ↓
FEATURE / CLUSTER-BASED
```

The syllabus specifically gives thresholding and region-based methods their own coverage, while morphology and feature methods follow them. fileciteturn4file0L41-L45

---

# 15.8 Segmentation as a Decision Rule

For a simple intensity segmentation:

\[
M(x,y)=
\begin{cases}
1,&f(x,y)\ge T\\
0,&f(x,y)<T
\end{cases}
\]

This is a classifier operating at the pixel level.

For a richer segmentation:

\[
M(x,y)=g(
f(x,y),
\mathcal N(x,y),
\text{colour},
\text{texture},
\text{context}
)
\]

where \(\mathcal N\) denotes neighbourhood information.

The complexity of \(g\) determines how much context the segmentation uses.

---

# 15.9 The Central Segmentation Tradeoff

Two major failure modes are:

```text
UNDER-SEGMENTATION
→ distinct regions are merged

OVER-SEGMENTATION
→ one meaningful region is split unnecessarily
```

Conceptually:

```text
true objects:
A | B | C

under-seg:
A+B | C

over-seg:
A1 | A2 | B1 | B2 | C
```

A good algorithm balances both.

---

# 15.10 Region Homogeneity

A region often should be internally consistent according to some criterion.

For example:

```text
similar intensity
similar colour
similar texture
```

A generic homogeneity measure can be represented as:

\[
H(R)
\]

where low or high values indicate suitability depending on the chosen metric.

There is no universal homogeneity function.

The engineering task is to choose one appropriate to the image and objective.

---

# 15.11 Region Adjacency

Segmentation is spatial.

Two pixels with similar values may belong to different objects if they are disconnected.

Example:

```text
bright object A      bright object B

   ███                  ███
```

A pure histogram cannot distinguish them.

Spatial connectivity supplies that missing information.

This connects segmentation to matrices, neighbourhoods and connected components.

---

# 15.12 Connected Components

After a binary segmentation, connected-component analysis can group connected foreground pixels.

Conceptually:

```text
binary mask
   ↓
connectivity rule
   ↓
components
   ↓
object candidates
```

Common connectivity choices include:

### 4-connectivity

Neighbours:

```text
  N
W P E
  S
```

### 8-connectivity

Adds diagonals:

```text
NW N NE
 W P E
SW S SE
```

The selected connectivity can change the number of components.

---

# 15.13 4- vs 8-Connectivity Example

Consider:

```text
1 0
0 1
```

Under:

```text
4-connectivity
```

the two pixels are disconnected.

Under:

```text
8-connectivity
```

they are connected diagonally.

Therefore connectivity is part of the segmentation definition.

---

# 15.14 Segmentation Output Types

A segmentation system can output:

### Binary mask

\[
M\in\{0,1\}
\]

### Label image

```text
0,1,2,...,K
```

### Probability map

\[
P_k(x,y)
\]

### Contours

```text
boundary curves
```

### Region list

```text
region ID
area
bounding box
features
```

The correct output depends on what later stages need.

---

# 15.15 Hard vs Soft Segmentation

### Hard

Each pixel gets one definite label.

\[
M(x,y)=k
\]

### Soft

A pixel can have class probabilities:

\[
P(k\mid x,y)
\]

For example:

```text
background = 0.15
object     = 0.85
```

Soft outputs are especially common in modern machine learning.

---

# 15.16 Segmentation and Preprocessing

Segmentation often improves after appropriate preprocessing:

```text
raw image
 ↓
denoise
 ↓
contrast correction
 ↓
colour-space conversion
 ↓
segmentation
```

But preprocessing can also remove the very boundaries needed for segmentation.

Therefore:

> Every preprocessing step should be judged by its effect on the downstream segmentation task.

---

# 15.17 Example — Why Denoising Can Help Segmentation

Suppose:

```text
foreground = bright
background = dark
```

but the foreground contains random noise.

Thresholding may produce:

```text
foreground
+ isolated false pixels
```

A small smoothing operation may make the object more coherent.

But too much smoothing can blur object boundaries.

This is the C09 → C15 connection.

---

# 15.18 Example — Why Contrast Enhancement Can Help

Suppose foreground intensity is:

\[
120\text{–}130
\]

and background intensity is:

\[
100\text{–}105
\]

The classes overlap little but are close numerically.

Contrast enhancement may increase separation.

However, a transformation can also change the noise distribution.

Thus preprocessing and thresholding should be treated as one pipeline.

---

# 15.19 Segmentation by Edges

Another strategy is:

```text
image
 ↓
edge detector
 ↓
closed/connected boundaries
 ↓
regions
```

This works well when object boundaries are strong.

It struggles when:

- edges are weak,
- boundaries are broken,
- texture creates many internal edges,
- illumination creates false edges.

This is why edge detection alone does not solve segmentation.

---

# 15.20 Region-Based Segmentation

Region methods group connected pixels according to a homogeneity rule.

Two important strategies are:

```text
region growing
region splitting/merging
```

These are treated more deeply in Chapter 17.

The core concept introduced here is:

> Segmentation can be driven by region consistency instead of only by isolated pixel thresholds or edges.

---

# 15.21 Region Growing — Concept

Start with one or more seed pixels.

Then:

```text
seed
 ↓
inspect neighbours
 ↓
accept similar neighbours
 ↓
expand region
 ↓
repeat
```

The similarity rule may depend on:

\[
|f(x,y)-\mu_R|<\tau
\]

where:

- \(\mu_R\) = current region mean,
- \(\tau\) = tolerance.

This specific rule is only one possible choice.

---

# 15.22 Worked Region-Growing Example

Consider:

\[
I=
\begin{bmatrix}
10&11&12&90\\
10&12&13&92\\
11&12&14&91\\
80&82&84&90
\end{bmatrix}
\]

Suppose the seed is the top-left 10.

A tolerance of:

\[
\tau=5
\]

could grow through:

```text
10, 11, 12, 13, 14
```

while values around:

```text
80–92
```

would be rejected.

This demonstrates the basic idea of local homogeneity.

---

# 15.23 Why Seed Selection Matters

The same image can produce different regions from different seeds.

```text
good seed
→ stable target region

bad seed
→ wrong growth

multiple seeds
→ broader coverage
```

Therefore seed selection is an algorithmic parameter.

Automatic seed selection can use:

- extrema,
- prior knowledge,
- connected components,
- edge information,
- learned proposals.

---

# 15.24 Segmentation Boundaries and Gradients

An edge can serve as a boundary cue.

For example:

\[
|\nabla f|
\]

can be used to discourage region growth across strong boundaries.

A region-growing criterion might therefore combine:

```text
intensity similarity
+
edge strength
+
connectivity
```

This is a more realistic segmentation strategy than one number alone.

---

# 15.25 Colour Segmentation

For colour images:

\[
I(x,y)=(R,G,B)
\]

or another colour representation can be used.

A segmentation criterion can operate on:

\[
\mathbf c(x,y)
\]

rather than a scalar intensity.

For example:

\[
\|\mathbf c-\mathbf c_0\|<\tau
\]

can represent distance from a target colour.

The choice of colour-space affects the usefulness of that distance.

---

# 15.26 Example — RGB Colour Distance

Suppose target colour:

\[
\mathbf c_0=(200,50,30)
\]

and pixel:

\[
\mathbf c=(190,55,40)
\]

Euclidean RGB distance:

\[
d=
\sqrt{
(190-200)^2
+
(55-50)^2
+
(40-30)^2
}
\]

\[
=
\sqrt{100+25+100}
\]

\[
=\sqrt{225}
\]

\[
\boxed{15}
\]

A threshold such as:

\[
d<20
\]

would accept this pixel under the stated criterion.

---

# 15.27 Why Colour Distance Is Not Universal

Euclidean distance in RGB treats channel differences geometrically in the storage coordinates.

It is not automatically equal to perceptual colour difference.

Therefore:

```text
RGB distance
≠ universal human-perception distance
```

For some tasks, another colour representation or perceptual colour metric may be more suitable.

---

# 15.28 Texture-Based Segmentation

Two regions can have similar average intensity but different texture.

Example:

```text
Region A
smooth gray

Region B
gray with repeated pattern
```

A histogram or mean may not separate them well.

Texture features can provide additional evidence.

This is an extension beyond basic thresholding/region growth.

---

# 15.29 Segmentation as Feature Selection

A powerful general formulation is:

```text
pixel/neighbourhood
        ↓
features
        ↓
decision rule
        ↓
label
```

Potential features:

```text
intensity
colour
gradient
local variance
texture
position
learned embedding
```

This connects segmentation directly to the feature-descriptor chapters.

---

# 15.30 Spatial Context

A pixel's own value may be ambiguous.

Example:

```text
pixel intensity = 100
```

Could be:

```text
background
or
object
```

Spatial context can resolve the ambiguity.

This is why segmentation methods frequently use:

```text
neighbourhood
+
connectivity
+
region statistics
```

instead of isolated pixels.

---

# 15.31 Segmentation and Morphology

After segmentation, the binary mask may contain:

```text
small holes
isolated noise
broken edges
thin protrusions
```

Morphological operations can clean or structure the mask.

Conceptual pipeline:

```text
segmentation
 ↓
morphology
 ↓
cleaner region mask
```

This is developed fully in C18.

---

# 15.32 Segmentation and Feature Extraction

Once a region is available, calculate:

```text
area
perimeter
bounding box
centroid
aspect ratio
shape descriptors
texture
colour statistics
```

Then:

```text
features
 ↓
classifier
```

This is a classical computer-vision pipeline.

---

# 15.33 Centroid of a Binary Region

For a binary region containing \(N\) foreground pixels with coordinates \((x_i,y_i)\):

\[
\bar x=\frac1N\sum_{i=1}^{N}x_i
\]

\[
\bar y=\frac1N\sum_{i=1}^{N}y_i
\]

The pair:

\[
(\bar x,\bar y)
\]

is the region centroid under the equal-weight pixel model.

---

# 15.34 Worked Centroid Example

Suppose foreground pixels are:

\[
(1,1),\ (2,1),\ (1,2),\ (2,2)
\]

Then:

\[
\bar x=\frac{1+2+1+2}{4}
=1.5
\]

\[
\bar y=\frac{1+1+2+2}{4}
=1.5
\]

Therefore:

\[
\boxed{(1.5,1.5)}
\]

This illustrates how segmentation converts pixels into geometric objects that can be measured.

---

# 15.35 Boundary Representation

A region can be represented by its:

```text
mask
or
boundary
```

The boundary is useful for:

- perimeter,
- contour shape,
- object matching,
- geometric measurements.

The mask is useful for:

- area,
- region statistics,
- pixel-level operations.

---

# 15.36 Segmentation Quality

If a reference segmentation is available, compare:

```text
predicted mask
vs
ground-truth mask
```

Common overlap measures include:

### Intersection over Union

\[
IoU=
\frac{|A\cap B|}
{|A\cup B|}
\]

### Dice coefficient

\[
Dice=
\frac{2|A\cap B|}
{|A|+|B|}
\]

These are highly useful metrics for segmentation.

---

# 15.37 Worked IoU Example

Suppose:

\[
|A\cap B|=80
\]

and:

\[
|A\cup B|=100
\]

Then:

\[
IoU=\frac{80}{100}
\]

\[
\boxed{0.8}
\]

or:

\[
80\%
\]

overlap.

---

# 15.38 Worked Dice Example

Suppose:

\[
|A|=90
\]

\[
|B|=100
\]

and:

\[
|A\cap B|=80
\]

Then:

\[
Dice=
\frac{2(80)}
{90+100}
\]

\[
=
\frac{160}{190}
\]

\[
\boxed{\approx0.8421}
\]

---

# 15.39 Pixel-Level Precision and Recall

Treat foreground detection as a binary classification.

Then:

\[
Precision=
\frac{TP}{TP+FP}
\]

\[
Recall=
\frac{TP}{TP+FN}
\]

This distinguishes:

```text
false foreground
```

from:

```text
missed foreground
```

A segmentation method can have high IoU but still exhibit particular precision/recall tradeoffs.

---

# 15.40 Under- vs Over-Segmentation Evaluation

A useful diagnostic is:

```text
too many regions
→ over-segmentation

too few regions
→ under-segmentation
```

Numerical metrics can help, but visual inspection of the mask and object-level errors remains important.

---

# 15.41 Segmentation Failure Case — Uneven Illumination

Suppose an object has:

```text
left side = 100
right side = 160
```

and background includes values:

```text
110–120
```

A single global threshold may fail.

Why?

```text
object intensity varies spatially
```

Potential solutions:

```text
illumination correction
adaptive threshold
region method
colour/features
```

This sets up Chapter 16.

---

# 15.42 Segmentation Failure Case — Overlapping Intensity Distributions

Suppose:

```text
object:
100–150

background:
120–170
```

Thresholding cannot create perfect separation because the intensity distributions overlap.

A richer representation may be required:

```text
colour
texture
edges
spatial context
learned features
```

The key engineering lesson:

> If the chosen feature does not separate the classes, changing the threshold alone cannot create separation that is absent from that feature.

---

# 15.43 Segmentation Failure Case — Texture

A threshold may segment a textured object into many disconnected pieces.

Possible pipeline:

```text
threshold
 ↓
fragmented mask
 ↓
morphological cleanup
 ↓
connected components
```

But if the fragments are semantically distinct, merging them blindly can be wrong.

Again, the task defines what “correct” means.

---

# 15.44 Segmentation and Scale

The correct segmentation depends on scale.

A texture at one scale may appear as:

```text
noise
```

at another.

A small object may disappear after aggressive smoothing.

Therefore segmentation is sensitive to:

```text
resolution
filter scale
kernel size
feature scale
```

This connects C09, C10 and C11 to C15–C20.

---

# 15.45 Segmentation as a Pipeline, Not a Single Algorithm

A realistic classical system may be:

```text
acquire
 ↓
denoise
 ↓
contrast/colour adjustment
 ↓
candidate segmentation
 ↓
morphological cleanup
 ↓
connected components
 ↓
feature extraction
 ↓
classification
```

Calling only the threshold step “the segmentation system” can hide many important decisions.

---

# 15.46 Reproducibility Requirements

Record:

```text
input image
preprocessing
colour space
threshold/criterion
connectivity
kernel/morphology settings
seed selection
post-processing
output representation
evaluation metric
```

Without these, segmentation experiments are difficult to reproduce.

---

# 15.47 Engineering Decision Tree

```text
Are intensities/colours well separated?
        │
       YES
        ↓
  threshold candidate
        │
       NO
        ↓
Is there strong boundary evidence?
        │
       YES
        ↓
 edge/region method
        │
       NO
        ↓
Do regions have local homogeneity?
        │
       YES
        ↓
 region-based method
        │
       NO
        ↓
use richer features / learned method
```

This is a conceptual starting point rather than a strict algorithm selector.

---

# 15.48 Practical Lab Experiment

A good segmentation lab can use one image and compare:

```text
1. global threshold
2. adaptive threshold
3. region growing
4. morphology-assisted cleanup
```

Record:

```text
parameters
mask area
number of connected components
IoU/Dice if ground truth exists
visual observations
```

The point is not merely to produce a mask.

It is to understand why the masks differ.

---

# 15.49 Common Traps

## Trap 1 — “Segmentation means object detection.”

False.

Segmentation produces regions/pixel labels; detection additionally identifies/localizes objects.

## Trap 2 — “A histogram can segment an image.”

Not by itself.

A histogram contains no spatial arrangement.

## Trap 3 — “Every segmentation result should be binary.”

False.

Multi-class and probabilistic segmentation are common.

## Trap 4 — “A threshold is an object detector.”

Not automatically.

It is a pixel-level decision rule.

## Trap 5 — “Edge detection solves segmentation.”

Not generally.

Edges may be broken, weak, or generated inside textured objects.

## Trap 6 — “More regions means better segmentation.”

False.

That may simply indicate over-segmentation.

## Trap 7 — “Preprocessing is separate from segmentation quality.”

False.

Preprocessing can strongly change separability.

## Trap 8 — “IoU alone explains all segmentation failures.”

False.

Object size, localization, false positives and topology can require additional analysis.

---

# 15.50 Exam Formula Sheet

### Binary segmentation

\[
\boxed{
M(x,y)=
\begin{cases}
1,&f(x,y)\ge T\\
0,&f(x,y)<T
\end{cases}
}
\]

### Region similarity example

\[
\boxed{
|f(x,y)-\mu_R|<\tau
}
\]

### Connectivity

```text
4-neighbour
8-neighbour
```

### Centroid

\[
\boxed{
\bar x=\frac1N\sum_i x_i,\quad
\bar y=\frac1N\sum_i y_i
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

### Precision

\[
\boxed{
Precision=\frac{TP}{TP+FP}
}
\]

### Recall

\[
\boxed{
Recall=\frac{TP}{TP+FN}
}
\]

---

# 15.51 Exam-Style Problem — Binary Mask

Given:

\[
I=
\begin{bmatrix}
10&40&80\\
20&70&90\\
30&60&100
\end{bmatrix}
\]

Use:

\[
T=60
\]

with:

\[
M=1\quad\text{if }I\ge60
\]

Then:

\[
M=
\begin{bmatrix}
0&0&1\\
0&1&1\\
0&1&1
\end{bmatrix}
\]

Foreground area:

\[
\boxed{4\text{ pixels}}
\]

---

# 15.52 Exam-Style Problem — Connectivity

Consider:

```text
1 0 1
0 1 0
1 0 1
```

The centre pixel is diagonally connected to all four corner pixels.

Under:

```text
4-connectivity
```

the centre alone forms one component.

Under:

```text
8-connectivity
```

all five foreground pixels form one connected component.

Thus:

\[
\boxed{
\text{connectivity changes the segmentation interpretation}
}
\]

---

# 15.53 Exam-Style Problem — IoU

Prediction:

\[
|A|=90
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
|A\cup B|
=
90+100-80
=
110
\]

Therefore:

\[
IoU=
\frac{80}{110}
\]

\[
\boxed{\approx0.7273}
\]

---

# 15.54 Engineering Insight — Start by Asking What Must Be Separated

A segmentation problem should begin with:

```text
What are the regions?
What makes them different?
Which features separate them?
Where does the boundary come from?
What errors are acceptable?
```

Only then choose:

```text
threshold
region growth
edge method
morphology
feature method
learned segmentation
```

This avoids algorithm-first thinking.

---

# 15.55 Cross-Book Bridges

> **C07 BRIDGE**  
> Histograms help diagnose whether intensity distributions are separable enough for threshold-based segmentation.

> **C09 BRIDGE**  
> Denoising can reduce false segmented pixels but may also weaken boundaries.

> **C10 BRIDGE**  
> Gradients and edges provide boundary evidence.

> **C16 BRIDGE**  
> Thresholding develops the pixel-decision idea introduced here into global and adaptive methods.

> **C17 BRIDGE**  
> Region growing and splitting/merging use spatial connectivity and homogeneity directly.

> **C18 BRIDGE**  
> Morphological operations clean and structure segmentation masks.

> **C19–C20 BRIDGE**  
> Features and descriptors convert segmented regions into measurable representations.

> **C25 / C28 BRIDGE**  
> Classical segmentation provides a conceptual foundation for modern classification and object-detection pipelines.

> **LAB BRIDGE**  
> Implement binary segmentation, connected components, region criteria and overlap metrics.

> **PRACTICE BRIDGE**  
> Classify segmentation problems, choose suitable evidence, compute masks/metrics and diagnose over/under-segmentation.

> **EXAM BRIDGE**  
> Be able to define segmentation, compare threshold/edge/region approaches, explain connectivity, and calculate IoU/Dice/centroids.

---

# 15.56 Quick Recall

```text
SEGMENTATION
→ assign pixels to meaningful regions

BINARY
→ foreground/background

MULTI-CLASS
→ multiple labels

EDGE
→ boundary evidence

THRESHOLD
→ value-based decision

REGION
→ connected homogeneity

MORPHOLOGY
→ structure/cleanup

FEATURES
→ measurable region properties
```

Core rule:

> **A segmentation algorithm is correct only relative to the separation objective it is supposed to achieve.**

---

# 15.57 Chapter Checkpoint

1. Define image segmentation.
2. Differentiate segmentation, classification and detection.
3. What is a binary mask?
4. What is multi-class segmentation?
5. What is the difference between semantic and instance segmentation?
6. What kinds of features can drive segmentation?
7. Explain under-segmentation and over-segmentation.
8. Why is spatial connectivity important?
9. Compare 4-connectivity and 8-connectivity.
10. What is region growing?
11. Why does seed selection matter?
12. Why can preprocessing change segmentation quality?
13. Explain why edge detection does not automatically solve segmentation.
14. Calculate a binary segmentation mask from a threshold.
15. Calculate a region centroid.
16. Derive IoU and Dice.
17. What are precision and recall for pixel-level segmentation?
18. What is the difference between hard and soft segmentation?
19. Design a basic segmentation experiment.
20. Explain why feature choice can matter more than threshold tuning.

---

# 15.58 Connection Forward

Segmentation has introduced the central idea:

```text
pixel evidence
+
decision rule
+
spatial organization
→
region
```

The next chapter focuses on the simplest and most widely taught segmentation family:

```text
C16
THRESHOLDING

global threshold
→ adaptive threshold
→ Otsu
→ multi-level thresholding
→ threshold failure analysis
```

The central question becomes:

> **How should the threshold itself be selected?**
