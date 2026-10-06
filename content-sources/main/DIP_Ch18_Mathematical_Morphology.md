---
id: "C18"
title: "Mathematical Morphology"
layer: "MAIN"
part: "III — Understanding Image Content"
unit: "III"
version: "1.0"
status: "REFERENCE BUILD"
syllabus_scope:
  - "Mathematical morphology"
  - "Morphological image processing"
  - "Binary shape operations"
tags:
  - "CORE"
  - "EXAM"
  - "MATH"
  - "DEEP DIVE"
  - "LAB"
  - "MORPHOLOGY"
  - "SHAPE"
  - "MASKS"
prerequisites:
  - "C15"
  - "C16"
  - "C17"
related:
  - "C19"
  - "C20"
  - "C21"
  - "C31"
math:
  - "M06"
  - "M07"
  - "M08"
  - "M09"
lab:
  - "LAB-U3-04"
  - "LAB-U3-05"
exam:
  - "EXAM-U3"
practice:
  - "P-C18"
assets:
  - "D-C18-01"
  - "D-C18-02"
  - "D-C18-03"
---

# Chapter 18 — Mathematical Morphology

> **Chapter thesis**  
> Morphology treats image regions as geometric structures. Instead of primarily asking what intensity a pixel has, it asks how foreground and background relate to a chosen **structuring element**. Erosion, dilation, opening and closing can remove, connect, expand, shrink and characterize shapes in a controllable way.

**Part III — Understanding Image Content**  
**Syllabus anchor:** Unit III explicitly includes mathematical morphology after segmentation and region-based methods. fileciteturn4file0L41-L45

---

# 18.0 Why Morphology?

A segmentation mask can be technically correct but messy:

```text
█████████
███ ███ █
█████████
   •
```

Problems may include:

- tiny noise,
- holes,
- disconnected fragments,
- unwanted protrusions,
- broken structures.

Morphology provides shape-aware operations.

The key change is:

```text
INTENSITY
→
BINARY / REGION STRUCTURE
→
GEOMETRIC TRANSFORMATION
```

---

# 18.1 What Is Mathematical Morphology?

Mathematical morphology is a framework for analyzing and modifying structures in images using set-theoretic and geometric operations.

For binary images:

```text
foreground
→ set of image coordinates
```

A structuring element probes that set.

For grayscale images, analogous operations are defined using intensity extrema.

This chapter first develops the binary case because it makes the concepts easiest to see.

---

# 18.2 Binary Image as a Set

Let:

\[
A
\]

be the set of foreground pixel coordinates.

For example:

```text
0 1 1
0 1 0
1 1 0
```

corresponds to:

\[
A=
\{
(1,2),(1,3),
(2,2),
(3,1),(3,2)
\}
\]

assuming the stated coordinate convention.

Morphological operations transform this set.

---

# 18.3 Structuring Element

A **structuring element (SE)** is a small geometric pattern used to probe the image.

Example:

\[
B=
\begin{bmatrix}
0&1&0\\
1&1&1\\
0&1&0
\end{bmatrix}
\]

This is a cross-shaped structuring element.

Another common SE:

\[
B=
\begin{bmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{bmatrix}
\]

The SE's:

- shape,
- size,
- origin/anchor

affect the result.

---

# 18.4 Why the Structuring Element Matters

Think of the SE as a small geometric probe.

```text
SE shape
  ↓
what local structure counts as fitting?
```

A:

```text
line SE
```

can emphasize line-like structures.

A:

```text
disk SE
```

can be more natural for rounded structures.

A:

```text
square SE
```

treats horizontal/vertical neighbourhoods symmetrically in a grid-oriented way.

---

# 18.5 Dilation — Intuition

**Dilation expands the foreground according to the structuring element.**

Conceptually:

```text
input

   ██
   ██

dilation

  ████
  ████
  ████
```

Dilation can:

- enlarge objects,
- connect nearby components,
- fill small gaps,
- strengthen thin structures.

---

# 18.6 Binary Dilation Definition

For sets:

\[
A\oplus B
\]

is the dilation of \(A\) by \(B\).

A set-theoretic interpretation is:

\[
A\oplus B
=
\{z\mid
(B)_z\cap A\ne\varnothing
\}
\]

under the standard reflected/translated structuring-element convention.

Equivalent textbook forms may differ in how reflection and origin are defined.

---

# 18.7 Pixel-Rule Intuition for Dilation

For a binary SE:

```text
if any required SE foreground
overlaps foreground
→ output can become foreground
```

This is a useful implementation intuition, but the exact rule depends on the SE definition.

---

# 18.8 Worked Dilation Example

Input:

\[
A=
\begin{bmatrix}
0&0&0\\
0&1&0\\
0&0&0
\end{bmatrix}
\]

Use:

\[
B=
\begin{bmatrix}
0&1&0\\
1&1&1\\
0&1&0
\end{bmatrix}
\]

Then:

\[
A\oplus B
=
\begin{bmatrix}
0&1&0\\
1&1&1\\
0&1&0
\end{bmatrix}
\]

A single foreground point expands into the SE shape.

---

# 18.9 Erosion — Intuition

**Erosion shrinks the foreground.**

Conceptually:

```text
large object
██████
██████
██████

erosion
  ██
  ██
```

Erosion can:

- remove small components,
- break narrow connections,
- shrink object boundaries,
- eliminate structures too small for the SE.

---

# 18.10 Binary Erosion Definition

The erosion:

\[
A\ominus B
\]

can be defined as:

\[
A\ominus B
=
\{z\mid
(B)_z\subseteq A
\}
\]

under the standard convention.

Interpretation:

> Keep a location only if the translated structuring element fits entirely inside the foreground.

---

# 18.11 Worked Erosion Example

Consider:

\[
A=
\begin{bmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{bmatrix}
\]

with:

\[
B=
\begin{bmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{bmatrix}
\]

Using a centred SE and valid binary erosion, only the centre location can support the full 3×3 SE.

So the conceptual result is:

\[
\begin{bmatrix}
0&0&0\\
0&1&0\\
0&0&0
\end{bmatrix}
\]

Boundary convention can change the full output canvas representation, so the example focuses on the morphological support relationship.

---

# 18.12 Dilation vs Erosion

| Operation | Main effect | Typical use |
|---|---|---|
| dilation | expand foreground | connect gaps, strengthen structures |
| erosion | shrink foreground | remove small structures, break thin links |

Memory:

```text
DILATION
→ grow

EROSION
→ shrink
```

---

# 18.13 Opening

Opening is:

\[
A\circ B
=
(A\ominus B)\oplus B
\]

So:

```text
erosion
→ dilation
```

Opening tends to:

- remove small foreground objects,
- remove thin protrusions,
- smooth boundaries,
- preserve larger structures that can survive erosion.

---

# 18.14 Why Opening Removes Small Objects

Suppose:

```text
large object       tiny dot

██████████          •
██████████
```

Erosion can eliminate the tiny dot.

The later dilation cannot recreate it because it has already disappeared.

The large object can survive and then regrow approximately.

Therefore:

```text
opening
→ remove small foreground details
```

---

# 18.15 Worked Opening Example

Suppose a binary mask contains:

```text
large square
+
one isolated single pixel
```

Using an SE larger than the isolated pixel:

```text
erosion
→ isolated pixel disappears

dilation
→ large square regrows
→ isolated pixel stays absent
```

The final output is cleaner.

---

# 18.16 Closing

Closing is:

\[
A\bullet B
=
(A\oplus B)\ominus B
\]

So:

```text
dilation
→ erosion
```

Closing tends to:

- fill small holes,
- close narrow gaps,
- connect nearby components,
- smooth boundaries.

---

# 18.17 Why Closing Fills Small Holes

Conceptually:

```text
object with tiny hole

███████
██   ██
██   ██
███████
```

Dilation expands the surrounding foreground and can cover the hole.

The later erosion returns the main object toward its original size while preserving the filled structure when the hole is small enough for the SE.

---

# 18.18 Opening vs Closing

| Operation | Sequence | Typical effect |
|---|---|---|
| opening | erosion → dilation | remove small foreground structures |
| closing | dilation → erosion | fill small holes / close gaps |

Memory:

```text
OPENING
→ open/remove small protrusions

CLOSING
→ close gaps/holes
```

---

# 18.19 Morphological Idempotence

A powerful property:

\[
(A\circ B)\circ B=A\circ B
\]

for standard binary opening.

Similarly:

\[
(A\bullet B)\bullet B=A\bullet B
\]

for closing.

This means:

> Applying the same opening twice does not continue changing the image after the first completed opening, under the standard morphological definition.

This is a useful mathematical property and an excellent exam concept.

---

# 18.20 Increasing Property

For suitable sets:

\[
A\subseteq C
\]

implies:

\[
A\oplus B\subseteq C\oplus B
\]

and similarly for erosion/opening/closing under the corresponding standard morphology properties.

The intuition is:

```text
larger input set
→ does not produce a smaller corresponding dilation
```

This illustrates that morphology respects set inclusion.

---

# 18.21 Translation Invariance

Standard morphological dilation/erosion are translation invariant in the sense that translating the input translates the output correspondingly, given consistent coordinate conventions and no special boundary artefacts.

This makes morphology naturally geometric.

---

# 18.22 Morphological Boundary Extraction

A boundary can be obtained from:

\[
\beta(A)=A-(A\ominus B)
\]

where subtraction indicates set difference for binary morphology.

Conceptually:

```text
object
 ↓
erode
 ↓
remove eroded interior
 ↓
boundary
```

---

# 18.23 Worked Boundary Example

Suppose:

```text
object:

111
111
111
```

Eroding with a 3×3 SE gives:

```text
000
010
000
```

Subtracting:

```text
111   000
111 - 010
111   000
```

gives:

```text
111
101
111
```

which represents an outer boundary-like ring under this simple discrete setup.

---

# 18.24 Morphological Gradient

A common morphological gradient is:

\[
G_m=(A\oplus B)-(A\ominus B)
\]

This highlights transition regions around objects.

Conceptually:

```text
dilate
  ↓
expanded object
  -
eroded object
  ↓
boundary band
```

---

# 18.25 Hit-or-Miss Transform

> **EXTENSION**

The hit-or-miss transform detects specific binary configurations.

It uses:

```text
foreground pattern
+
background pattern
```

to identify a desired local shape.

Conceptually:

```text
target pattern
     ↓
scan image
     ↓
location matches
```

It is useful for shape detection.

---

# 18.26 Thinning and Skeletonization

> **EXTENSION**

Morphological thinning reduces a shape toward a skeletal representation while preserving important topology under suitable algorithms.

Skeletonization can represent:

```text
thick object
→ medial/structural line
```

Applications include:

- character analysis,
- road/network extraction,
- shape analysis.

Exact algorithms have their own topology-preservation rules.

---

# 18.27 Grayscale Morphology

Morphology is not limited to binary masks.

For a grayscale image \(f\) and flat structuring element \(B\):

### Grayscale dilation

Conceptually:

\[
(f\oplus B)(x)
=
\max_{b\in B} f(x-b)
\]

### Grayscale erosion

\[
(f\ominus B)(x)
=
\min_{b\in B} f(x+b)
\]

Exact indexing/sign convention depends on the chosen morphological definition.

The key idea is:

```text
dilation
→ local maximum-like operation

erosion
→ local minimum-like operation
```

---

# 18.28 Morphological Opening on Grayscale

\[
f\circ B=
(f\ominus B)\oplus B
\]

It can suppress bright structures smaller than the SE.

Conversely, closing can suppress/fill dark structures of suitable size.

This provides a powerful scale-based interpretation.

---

# 18.29 Morphological Top-Hat

White top-hat:

\[
T_W=f-(f\circ B)
\]

It emphasizes bright structures that are smaller than the structuring element's effective scale.

Conceptually:

```text
image
-
opened background-like version
→
bright details
```

---

# 18.30 Black-Hat

Black-hat:

\[
T_B=(f\bullet B)-f
\]

It emphasizes dark structures relative to a locally closed background.

These operations are useful for tasks such as:

- uneven illumination correction,
- text extraction,
- small-feature enhancement.

---

# 18.31 Worked Top-Hat Idea

Imagine:

```text
smooth background
+
small bright dots
```

Opening removes many small bright structures.

Then:

\[
f-(f\circ B)
\]

leaves those bright structures emphasized.

Thus white top-hat acts like a morphology-based small-bright-feature detector.

---

# 18.32 Structuring Element Size as a Scale Parameter

This is one of the most important morphology ideas.

Suppose target object width is:

\[
3\text{ pixels}
\]

and the SE is:

\[
11\times11
\]

A morphology operation may treat the 3-pixel object as small relative to the chosen scale.

Change the SE to:

\[
3\times3
\]

and the same object may survive.

Therefore morphology is inherently scale-sensitive.

---

# 18.33 Shape Matters, Not Just Size

A horizontal line SE behaves differently from a disk or square.

For example:

```text
horizontal SE
→ favours horizontal structures

vertical SE
→ favours vertical structures
```

Thus:

```text
SE size
+
SE shape
+
SE orientation
```

define the morphological prior.

---

# 18.34 Morphology for Mask Cleanup

A common segmentation pipeline is:

```text
threshold
 ↓
opening
 ↓
remove small foreground noise
 ↓
closing
 ↓
fill small gaps
 ↓
connected components
```

The order matters.

Changing:

```text
opening → closing
```

to:

```text
closing → opening
```

can produce different results.

---

# 18.35 Worked Cleanup Scenario

Suppose a thresholded object has:

```text
small isolated foreground dots
+
small holes
```

A reasonable experiment might be:

```text
opening
→ suppress isolated dots

closing
→ fill small holes
```

But the exact kernel should be chosen based on object scale.

---

# 18.36 Morphology and Connectivity

Morphological operations can alter connectivity.

### Dilation

Can connect nearby components.

### Erosion

Can break thin connections.

This is why morphology can change connected-component counts.

---

# 18.37 Example — Bridge Breaking

Consider:

```text
██████
   ██
██████
```

A narrow one-pixel bridge connects two larger areas.

An erosion with a suitable SE may break the bridge:

```text
█████

█████
```

This can be useful when separate objects are connected by a thin artifact.

---

# 18.38 Example — Gap Closing

Consider:

```text
████ ████
```

A suitable dilation followed by erosion can close a small gap.

This is especially useful for:

- broken character strokes,
- incomplete boundaries,
- segmented line structures.

---

# 18.39 Morphological Noise Removal vs Statistical Denoising

C09 used filters based on numeric neighbourhood statistics.

Morphology uses geometric structure.

### Statistical

```text
mean / median / Gaussian
→ value relationships
```

### Morphological

```text
erosion / dilation
→ set/shape relationships
```

This distinction helps choose the right tool.

---

# 18.40 Morphology and Edge Detection

Morphological boundaries can provide object contours.

Gradient-based edges:

```text
intensity derivatives
```

Morphological boundaries:

```text
shape/set difference
```

They can be combined.

---

# 18.41 Morphology and Connected Components

A practical mask-processing chain:

```text
segmentation
 ↓
morphology
 ↓
connected components
 ↓
region measurements
```

Morphology improves the topology before measurements are extracted.

---

# 18.42 Morphological Distance Intuition

Repeated erosion can remove outer layers.

The number of erosions required to eliminate a region provides information about its scale.

This connects morphology to:

```text
shape thickness
+
distance-like measures
```

Advanced algorithms use this idea for skeletons and distance transforms.

---

# 18.43 Distance Transform

> **EXTENSION**

A distance transform assigns each foreground pixel a distance to the nearest background pixel under a chosen metric.

For example:

\[
D(p)=\min_{q\in\text{background}}d(p,q)
\]

A large value indicates a pixel deep inside the object.

This can support:

- skeletonization,
- object-centre detection,
- separation of touching objects.

---

# 18.44 Morphological Reconstruction

> **EXTENSION**

Morphological reconstruction uses a **marker** image constrained by a **mask** image.

Conceptually:

```text
marker
 +
mask constraint
 ↓
connected reconstruction
```

It can preserve large connected structures while removing unwanted components more selectively than simple opening.

---

# 18.45 Why Reconstruction Is Useful

Simple opening removes structures according to the SE.

Reconstruction can instead preserve the connectivity of selected marker regions.

This is powerful for:

- extracting connected objects,
- removing small components without distorting surviving shapes,
- advanced segmentation cleanup.

---

# 18.46 Practical Experiment Design

For a binary mask, compare:

```text
original
opening with 3×3
opening with 5×5
closing with 3×3
closing with 5×5
opening + closing
closing + opening
```

Record:

```text
foreground area
component count
hole count
IoU/Dice
visual shape changes
```

This exposes the meaning of structuring-element scale.

---

# 18.47 Boundary Conditions

Morphological operators also need border behaviour.

Pixels outside the image may be treated according to library-specific rules.

Therefore:

```text
same SE
+
different border policy
→
possibly different result
```

Reproducibility requires recording the implementation convention.

---

# 18.48 Binary vs Grayscale Morphology

| Property | Binary | Grayscale |
|---|---|---|
| basic data | sets / 0–1 | intensity values |
| dilation | set expansion | local max-like operation |
| erosion | set shrinking | local min-like operation |
| opening/closing | shape filtering | intensity-structure filtering |
| common task | mask cleanup | feature/background manipulation |

---

# 18.49 Common Traps

## Trap 1 — “Dilation always makes objects look bigger in every possible sense.”

Usually it expands foreground support, but the exact result depends on SE shape and boundary convention.

## Trap 2 — “Erosion just deletes noise.”

It can also shrink objects and break useful connections.

## Trap 3 — “Opening = dilation then erosion.”

False.

Standard opening is:

\[
erosion\rightarrow dilation
\]

## Trap 4 — “Closing = erosion then dilation.”

False.

Standard closing is:

\[
dilation\rightarrow erosion
\]

## Trap 5 — “Bigger SE is always better.”

False.

It can eliminate genuine structures.

## Trap 6 — “Morphology is only for binary images.”

False.

Grayscale morphology is important.

## Trap 7 — “Morphology cannot change connectivity.”

False.

Dilation and erosion can connect or disconnect regions.

## Trap 8 — “Top-hat is just a brighter image.”

False.

It isolates structures relative to a morphological opening/closing.

---

# 18.50 Exam Formula Sheet

### Dilation

\[
\boxed{
A\oplus B
}
\]

### Erosion

\[
\boxed{
A\ominus B
}
\]

### Opening

\[
\boxed{
A\circ B=(A\ominus B)\oplus B
}
\]

### Closing

\[
\boxed{
A\bullet B=(A\oplus B)\ominus B
}
\]

### Boundary extraction

\[
\boxed{
\beta(A)=A-(A\ominus B)
}
\]

### Morphological gradient

\[
\boxed{
G_m=(A\oplus B)-(A\ominus B)
}
\]

### White top-hat

\[
\boxed{
T_W=f-(f\circ B)
}
\]

### Black-hat

\[
\boxed{
T_B=(f\bullet B)-f
}
\]

### Grayscale dilation, conceptual flat-SE form

\[
\boxed{
(f\oplus B)(x)=\max_{b\in B}f(x-b)
}
\]

### Grayscale erosion, conceptual flat-SE form

\[
\boxed{
(f\ominus B)(x)=\min_{b\in B}f(x+b)
}
\]

---

# 18.51 Exam-Style Problem — Opening

State the sequence for opening.

Answer:

\[
\boxed{
A\circ B=(A\ominus B)\oplus B
}
\]

Therefore:

```text
erosion
→ dilation
```

Primary purpose:

```text
remove small foreground structures
+
smooth certain boundary protrusions
```

---

# 18.52 Exam-Style Problem — Closing

State the sequence for closing.

\[
\boxed{
A\bullet B=(A\oplus B)\ominus B
}
\]

Therefore:

```text
dilation
→ erosion
```

Primary purpose:

```text
close small gaps
+
fill small holes
```

---

# 18.53 Exam-Style Problem — Boundary

Given:

\[
A=
\begin{bmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{bmatrix}
\]

and erosion result:

\[
A\ominus B=
\begin{bmatrix}
0&0&0\\
0&1&0\\
0&0&0
\end{bmatrix}
\]

Then:

\[
A-(A\ominus B)
\]

gives:

\[
\boxed{
\begin{bmatrix}
1&1&1\\
1&0&1\\
1&1&1
\end{bmatrix}
}
\]

This extracts a boundary-like structure under the example convention.

---

# 18.54 Engineering Insight — Morphology Is a Shape Prior

A structuring element encodes an assumption:

```text
what local shape matters?
```

Therefore selecting:

```text
3×3 square
```

versus:

```text
horizontal line
```

is not just a parameter change.

It is a change in the geometric prior.

This is one reason morphology is so effective in engineered vision systems where object geometry is known.

---

# 18.55 Practical Example — OCR Cleanup

A document may produce:

```text
broken strokes
small black noise
tiny holes
```

A morphology pipeline can be:

```text
grayscale
 ↓
threshold
 ↓
opening / closing
 ↓
connected components
 ↓
OCR
```

The exact order and SE depend on:

- font thickness,
- scan resolution,
- noise scale.

---

# 18.56 Practical Example — Industrial Components

Suppose a binary segmentation produces:

```text
components
+
small gaps
+
small isolated specks
```

Morphology can:

```text
remove specks
connect intended pieces
fill holes
```

Then:

```text
connected components
→ area filtering
→ measurement
```

This creates a classical industrial inspection pipeline.

---

# 18.57 Morphology and Object Scale

Suppose the smallest valid object diameter is:

\[
d=8
\]

pixels.

A 15×15 opening may remove that object.

Therefore:

> Morphological scale should be chosen from the geometry of meaningful objects, not merely from the amount of visible noise.

---

# 18.58 Morphology Evaluation

For ground-truth masks, compare:

```text
before morphology
vs
after morphology
vs
ground truth
```

Do not assume that a prettier mask is automatically more accurate.

Measure:

\[
IoU,\quad Dice
\]

and inspect:

```text
small objects
boundaries
holes
connectivity
```

---

# 18.59 Common Engineering Failure

A user notices tiny noise and selects:

```text
large opening
```

The noise disappears—but so do:

```text
small valid objects
```

This is the morphology version of over-smoothing.

The cure is the same engineering principle:

> Define what information must survive before choosing the filter scale.

---

# 18.60 Cross-Book Bridges

> **C16 BRIDGE**  
> Thresholding produces masks that frequently need morphological cleanup.

> **C17 BRIDGE**  
> Region-based segmentation creates connected regions; morphology refines their geometry.

> **C10 BRIDGE**  
> Morphological boundaries provide an alternative/complementary form of edge evidence.

> **C19–C20 BRIDGE**  
> Clean masks enable reliable shape and region feature extraction.

> **C21+ BRIDGE**  
> Morphology can preprocess regions before compression-independent feature analysis.

> **LAB BRIDGE**  
> Compare erosion, dilation, opening and closing using multiple SE shapes/sizes.

> **PRACTICE BRIDGE**  
> Trace binary morphology by hand, identify operation sequences and reason about connectivity/shape effects.

> **EXAM BRIDGE**  
> Know set definitions, erosion/dilation, opening/closing, boundary extraction and top-hat/black-hat concepts.

---

# 18.61 Quick Recall

```text
EROSION
→ shrink

DILATION
→ grow

OPENING
→ erosion → dilation
→ remove small foreground structures

CLOSING
→ dilation → erosion
→ close gaps / holes

BOUNDARY
→ A − erosion(A)

TOP-HAT
→ bright small structures

BLACK-HAT
→ dark small structures
```

Core rule:

> **The structuring element defines the geometric scale and shape that morphology considers important.**

---

# 18.62 Chapter Checkpoint

1. Define mathematical morphology.
2. What is a structuring element?
3. Explain binary morphology as set operations.
4. Define dilation.
5. Define erosion.
6. Compare dilation and erosion.
7. Define opening and give its sequence.
8. Define closing and give its sequence.
9. Explain why opening removes small foreground components.
10. Explain why closing fills small holes.
11. Define morphological boundary extraction.
12. Define morphological gradient.
13. What are top-hat and black-hat transforms?
14. Explain the effect of structuring-element size.
15. Explain the effect of structuring-element shape.
16. How can morphology change connectivity?
17. Compare binary and grayscale morphology.
18. What is morphological reconstruction?
19. How can morphology support OCR or industrial inspection?
20. Design a morphology pipeline for a noisy segmentation mask.

---

# 18.63 Part III Progress

The classical segmentation chain is now:

```text
C15
SEGMENTATION FUNDAMENTALS
      ↓
C16
THRESHOLDING
      ↓
C17
REGION-BASED SEGMENTATION
      ↓
C18
MATHEMATICAL MORPHOLOGY
```

Next:

```text
C19
IMAGE FEATURES AND DESCRIPTORS
      ↓
C20
SIFT / SURF / ORB / HOG
```

The conceptual transition is:

```text
pixels
→ labels
→ connected regions
→ shapes
→ measurable features
→ robust descriptors
```

That is the bridge from classical image processing into classical computer vision.
