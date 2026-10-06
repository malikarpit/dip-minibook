---
id: "C10"
title: "Sharpening and Edge Detection"
layer: "MAIN"
part: "II — Improving the Image"
unit: "II"
version: "1.0"
status: "REFERENCE BUILD"
syllabus_scope:
  - "Sharpening"
  - "Edge detection"
tags:
  - "CORE"
  - "EXAM"
  - "MATH"
  - "DEEP DIVE"
  - "LAB"
  - "EDGES"
  - "DERIVATIVES"
prerequisites:
  - "C08"
  - "C09"
related:
  - "C11"
  - "C15"
  - "C16"
  - "C19"
  - "C20"
  - "C30"
math:
  - "M05"
  - "M06"
  - "M07"
  - "M08"
lab:
  - "LAB-U2-04"
  - "LAB-U2-06"
  - "LAB-U4-05"
exam:
  - "EXAM-U2"
practice:
  - "P-C10"
assets:
  - "D-C10-01"
  - "D-C10-02"
  - "D-C10-03"
---

# Chapter 10 — Sharpening and Edge Detection

> **Chapter thesis**  
> Edges are locations of strong spatial change. Sharpening emphasizes such changes to improve apparent detail, while edge detection converts derivative evidence into an explicit representation of boundaries. Both tasks are powerful—and both are highly sensitive to noise.

**Part II — Improving the Image**  
**Syllabus anchor:** Unit II includes sharpening and edge detection; the practical sequence also includes frequency filtering later in the same unit. fileciteturn4file0L36-L40

---

# 10.0 Why Sharpening and Edge Detection Belong Together

C09 reduced unwanted variation.

Now consider:

```text
smooth region
→ little local change

object boundary
→ strong local change
```

Differentiation exposes that change.

Therefore:

```text
image
 ↓
optional denoising
 ↓
derivative
 ↓
edge evidence
```

Sharpening uses related high-frequency information differently:

```text
image
 ↓
estimate detail
 ↓
add detail back
 ↓
sharper appearance
```

So:

```text
EDGE DETECTION
→ represent boundaries

SHARPENING
→ enhance detail/boundary appearance
```

They are related but are not the same operation.

---

# 10.1 What Is an Edge?

An edge is a local region where image intensity changes substantially over a relatively small spatial distance.

Idealized 1-D example:

```text
100 100 100 200 200 200
          ↑
        transition
```

A derivative response becomes large near the transition.

Real edges may be:

- noisy,
- blurred,
- gradual,
- textured,
- multiple pixels wide.

Therefore an edge is better understood as a structural intensity transition than as one specific pixel.

---

# 10.2 Step, Ramp and Roof Edges

> **DEEP DIVE**

### Step edge

Abrupt transition:

```text
████████|░░░░░░
```

### Ramp edge

Gradual transition:

```text
███████▓▒░░░░░░
```

### Roof/ridge structure

Intensity rises and then falls:

```text
░░▒▓██▓▒░░
```

These idealized models help explain why derivatives respond differently to boundaries and thin structures.

---

# 10.3 First Derivative

For a 1-D signal \(f(x)\):

\[
\frac{df}{dx}
\]

measures the rate of intensity change.

Interpretation:

```text
flat area
→ derivative ≈ 0

strong transition
→ large derivative magnitude
```

This is the foundation of gradient-based edge detection.

---

# 10.4 Second Derivative

The second derivative is:

\[
\frac{d^2f}{dx^2}
\]

It is sensitive to changes in the first derivative.

It is useful for:

- fine detail,
- sharpening,
- locating zero crossings in some edge methods.

The Laplacian extends this idea to two dimensions.

---

# 10.5 Image Gradient

For a 2-D image:

\[
\nabla f=
\begin{bmatrix}
\frac{\partial f}{\partial x}\\
\frac{\partial f}{\partial y}
\end{bmatrix}
\]

Define:

\[
G_x=\frac{\partial f}{\partial x}
\]

\[
G_y=\frac{\partial f}{\partial y}
\]

Then:

\[
|\nabla f|
=
\sqrt{G_x^2+G_y^2}
\]

and:

\[
\theta=
\operatorname{atan2}(G_y,G_x)
\]

These equations form the mathematical core of many edge detectors.

---

# 10.6 What Does Gradient Direction Mean?

The gradient points toward the direction of maximum local increase in intensity.

The visual edge is approximately perpendicular to the gradient direction for an ideal local boundary.

Example:

```text
dark | bright
      →
 gradient direction

edge:
────────────
```

The edge orientation and gradient direction are therefore related by approximately:

\[
90^\circ
\]

under the idealized model.

---

# 10.7 Simple Finite Differences

A basic horizontal derivative can be approximated by:

\[
G_x(i,j)=f(i,j+1)-f(i,j)
\]

Similarly:

\[
G_y(i,j)=f(i+1,j)-f(i,j)
\]

These are simple forward differences.

Central differences use values on both sides:

\[
G_x(i,j)
\approx
\frac{
f(i,j+1)-f(i,j-1)
}{2}
\]

This can provide a more symmetric approximation.

---

# 10.8 Roberts Cross Operator

A simple 2×2 derivative-based operator uses diagonal differences.

One common convention is:

\[
R_x=
\begin{bmatrix}
1&0\\
0&-1
\end{bmatrix}
\]

\[
R_y=
\begin{bmatrix}
0&1\\
-1&0
\end{bmatrix}
\]

Sign conventions vary.

Roberts is computationally simple but uses a very small neighbourhood and can be sensitive to noise.

---

# 10.9 Prewitt Operator

A common Prewitt pair is:

\[
P_x=
\begin{bmatrix}
-1&0&1\\
-1&0&1\\
-1&0&1
\end{bmatrix}
\]

\[
P_y=
\begin{bmatrix}
-1&-1&-1\\
0&0&0\\
1&1&1
\end{bmatrix}
\]

These estimate directional gradients while providing some local averaging.

---

# 10.10 Sobel Operator

A common Sobel pair is:

\[
S_x=
\begin{bmatrix}
-1&0&1\\
-2&0&2\\
-1&0&1
\end{bmatrix}
\]

\[
S_y=
\begin{bmatrix}
-1&-2&-1\\
0&0&0\\
1&2&1
\end{bmatrix}
\]

Compared with Prewitt, Sobel gives stronger weight to the central row/column.

This provides additional smoothing while computing the directional derivative.

---

# 10.11 Worked Sobel Example

Consider:

\[
I=
\begin{bmatrix}
10&10&100\\
10&10&100\\
10&10&100
\end{bmatrix}
\]

For the centre:

### \(S_x\)

\[
(-1)(10)+(0)(10)+(1)(100)
\]

\[
+(-2)(10)+(0)(10)+(2)(100)
\]

\[
+(-1)(10)+(0)(10)+(1)(100)
\]

\[
=-10+100-20+200-10+100
\]

\[
=360
\]

### \(S_y\)

Because the image is constant vertically:

\[
S_y=0
\]

Therefore:

\[
|\nabla f|
=
\sqrt{360^2+0^2}
=
360
\]

There is a strong left-to-right transition.

---

# 10.12 Gradient Magnitude Scaling

Derivative responses can exceed the image storage range.

For the previous example:

\[
G=360
\]

This cannot be directly represented by ordinary 8-bit intensity without scaling or clipping.

A visualization pipeline might:

\[
G_{\text{norm}}
=
255\frac{G-G_{\min}}
{G_{\max}-G_{\min}}
\]

when appropriate.

For true quantitative processing, preserve the original response in a suitable signed/floating representation rather than replacing it permanently with a display-scaled image.

---

# 10.13 Edge Map vs Gradient Image

A gradient-magnitude image is:

```text
continuous-valued edge evidence
```

An edge map is often:

```text
binary or thin boundary representation
```

Conceptually:

```text
gradient magnitude
→ threshold / post-process
→ edge map
```

Therefore:

> Sobel output and an edge map are not necessarily the same thing.

---

# 10.14 Thresholding the Gradient

Let:

\[
G(x,y)=|\nabla f(x,y)|
\]

Define:

\[
E(x,y)=
\begin{cases}
1,&G(x,y)\ge T\\
0,&G(x,y)<T
\end{cases}
\]

This converts gradient evidence into a binary edge decision.

The threshold \(T\) determines sensitivity.

---

# 10.15 Low vs High Edge Threshold

### Too low

```text
many true edges
+
many noise responses
```

### Too high

```text
noise suppressed
+
weak real edges lost
```

Therefore threshold selection is a detection tradeoff.

---

# 10.16 Why Smoothing Often Comes First

From C09:

```text
noise
→ high-frequency variation
```

From this chapter:

```text
derivative
→ emphasizes local variation
```

Therefore:

```text
noise
  ↓
derivative
  ↓
false strong responses
```

A common strategy is:

```text
image
 ↓
Gaussian smoothing
 ↓
gradient
 ↓
edge detection
```

The smoothing scale controls the smallest structures that remain strongly detectable.

---

# 10.17 Canny Edge Detector

> **EXTENSION**

Canny is a multi-stage edge detector designed around goals such as:

- good detection,
- good localization,
- limited multiple responses to a single edge.

A simplified pipeline is:

```text
image
 ↓
Gaussian smoothing
 ↓
gradient computation
 ↓
gradient magnitude + direction
 ↓
non-maximum suppression
 ↓
double threshold
 ↓
edge tracking by hysteresis
 ↓
final edge map
```

---

# 10.18 Non-Maximum Suppression

Gradient responses often form thick bands around edges.

Non-maximum suppression keeps a response only if it is locally maximal along the gradient direction.

Conceptually:

```text
THICK RESPONSE

████
████
████
 ↓
NMS
 ↓
THIN RESPONSE

  █
  █
  █
```

This is a key reason Canny edges are often thinner than raw Sobel thresholding.

---

# 10.19 Double Threshold

Canny commonly uses:

```text
high threshold
low threshold
```

Pixels are classified conceptually as:

```text
strong
weak
non-edge
```

Strong responses are accepted.

Weak responses may be kept if they are connected to strong edge evidence.

---

# 10.20 Hysteresis

Hysteresis prevents isolated weak responses from automatically becoming edges.

Conceptually:

```text
strong edge
   │
weak ── weak ── weak
   │
connected chain
   ↓
keep

isolated weak response
   ↓
discard
```

This is more robust than applying one threshold independently to every pixel.

---

# 10.21 Canny vs Sobel

| Property | Sobel | Canny |
|---|---|---|
| output | gradient response | refined edge map |
| smoothing | built into kernel | explicit Gaussian stage |
| thresholding | usually separate | integrated multi-stage process |
| thinning | no | non-maximum suppression |
| weak-edge linking | no | hysteresis |
| complexity | lower | higher |

Sobel is excellent for learning and simple gradient estimation.

Canny is a more complete classical edge-detection pipeline.

---

# 10.22 Second-Derivative Edge Detection

The Laplacian is:

\[
\nabla^2f
=
\frac{\partial^2 f}{\partial x^2}
+
\frac{\partial^2 f}{\partial y^2}
\]

A common discrete kernel is:

\[
H=
\begin{bmatrix}
0&1&0\\
1&-4&1\\
0&1&0
\end{bmatrix}
\]

A sign-reversed form is equally possible with a consistent interpretation.

---

# 10.23 Zero-Crossing Idea

Second derivatives can change sign around transitions.

Conceptually:

```text
positive response
     ↓
     0
     ↓
negative response
```

The zero crossing can provide an edge candidate.

Because second derivatives are highly noise-sensitive, smoothing is commonly paired with this approach.

---

# 10.24 Laplacian of Gaussian

A combined approach is:

```text
Gaussian smoothing
+
Laplacian
```

This produces the Laplacian of Gaussian (LoG) concept.

A further related detector is the Difference of Gaussians (DoG), which approximates a band-pass/LoG-like response under suitable conditions.

These are extensions beyond the minimum syllabus requirement.

---

# 10.25 Sharpening and High Frequencies

Edges and fine detail correspond to rapid spatial variation.

Therefore sharpening often increases high-frequency content.

Conceptually:

```text
original
 ↓
estimate low-frequency component
 ↓
detail = original − low-frequency
 ↓
add selected detail
```

This is the same structure introduced in C08, now analyzed as a sharpening strategy.

---

# 10.26 Unsharp Masking

Let:

\[
f_{\text{blur}}=LP\{f\}
\]

Then:

\[
m=f-f_{\text{blur}}
\]

and:

\[
g=f+k\,m
\]

where:

\[
k>0
\]

controls strength.

Equivalent form:

\[
g=(1+k)f-kf_{\text{blur}}
\]

---

# 10.27 Worked Unsharp Example

Suppose:

\[
f=150
\]

and:

\[
f_{\text{blur}}=120
\]

Then:

\[
m=150-120=30
\]

For:

\[
k=0.5
\]

we get:

\[
g=150+0.5(30)
\]

\[
=165
\]

The detail difference has been partially added back.

---

# 10.28 Over-Sharpening

Excessive sharpening can cause:

```text
haloing
ringing
noise amplification
unnatural edges
clipping
```

Therefore sharpening strength should be controlled.

A common failure pipeline is:

```text
noisy image
→ strong sharpening
→ amplified noise
→ even more sharpening
→ unstable appearance
```

Denoising and sharpening often need to be coordinated.

---

# 10.29 High-Boost Filtering

A high-boost form is:

\[
g=Af-f_{\text{blur}}
\]

where:

\[
A>1
\]

If:

\[
A=1+k
\]

it connects naturally to unsharp masking.

High-boost enhancement can retain more of the original while still emphasizing high-frequency detail.

---

# 10.30 Laplacian Sharpening

Depending on sign convention:

\[
g=f-\nabla^2f
\]

or:

\[
g=f+\nabla^2f
\]

can be used.

The sign must match the selected Laplacian kernel.

This produces a detail-enhancement operation based on second-order derivatives.

---

# 10.31 Worked Laplacian-Sharpening Example

Use:

\[
P=
\begin{bmatrix}
100&100&100\\
100&150&100\\
100&100&100
\end{bmatrix}
\]

with:

\[
H=
\begin{bmatrix}
0&1&0\\
1&-4&1\\
0&1&0
\end{bmatrix}
\]

Laplacian response at the centre:

\[
100+100-4(150)+100+100
\]

\[
=400-600
\]

\[
=-200
\]

If using:

\[
g=f-\nabla^2 f
\]

then:

\[
g=150-(-200)
\]

\[
\boxed{350}
\]

This exceeds the 8-bit display range.

So a real implementation must decide how to handle the result rather than blindly storing 350 in uint8.

---

# 10.32 Why the Example Matters

The calculation demonstrates three concepts simultaneously:

```text
1. second derivative detects local structure
2. sharpening can create values outside original range
3. output representation is part of the algorithm
```

This connects directly to C04's datatype/range concepts.

---

# 10.33 Edge Detection Pipeline

A disciplined edge workflow:

```text
RAW / INPUT IMAGE
       ↓
inspect datatype/range
       ↓
grayscale or suitable representation
       ↓
optional denoising
       ↓
gradient or second derivative
       ↓
magnitude / zero-crossing
       ↓
thresholding
       ↓
post-processing
       ↓
EDGE MAP
```

For Canny:

```text
image
 ↓
Gaussian
 ↓
gradient
 ↓
NMS
 ↓
double threshold
 ↓
hysteresis
 ↓
edges
```

---

# 10.34 Edge Detection Does Not Mean Object Detection

An edge map shows likely boundaries.

It does not automatically identify:

```text
car
person
tree
building
```

Object detection requires higher-level reasoning.

The progression is:

```text
edges
→ contours/features
→ regions
→ objects/classes
```

This becomes important in Part III and Part V.

---

# 10.35 Edges vs Texture

Texture can contain many rapid local changes.

A derivative-based detector may therefore produce responses inside a textured region.

So:

```text
strong gradient
≠ necessarily object boundary
```

Context and higher-level processing are required to distinguish structural boundaries from texture.

---

# 10.36 Edge Connectivity

A useful edge map is not just a set of independent bright pixels.

Real boundaries tend to form connected structures.

Post-processing can include:

- linking,
- morphological operations,
- contour extraction,
- connected components.

These connect this chapter to segmentation and morphology.

---

# 10.37 Multi-Scale Edge Detection

> **EXTENSION**

An edge's visibility depends on scale.

```text
small Gaussian σ
→ detects finer structures
→ more noise sensitivity

large Gaussian σ
→ suppresses fine structures
→ emphasizes broader boundaries
```

Therefore:

> “Is there an edge?” can be an incomplete question.

A better question is:

> “At what spatial scale is this boundary meaningful?”

This is a major idea in modern computer vision.

---

# 10.38 Orientation Information

Gradient-based operators provide directional information.

For:

\[
G_x,G_y
\]

orientation:

\[
\theta=\operatorname{atan2}(G_y,G_x)
\]

This can support:

- contour analysis,
- feature descriptors,
- texture analysis,
- local shape reasoning.

This prepares the ground for HOG and related descriptors in C19–C20.

---

# 10.39 Feature Descriptors Bridge

HOG, introduced later, uses gradient orientation information across cells.

Conceptually:

```text
edge detection
→ local gradient
→ orientation
→ aggregate orientations
→ descriptor
```

Thus edge detection is not an isolated topic.

It is one of the mathematical foundations of classical feature engineering.

---

# 10.40 Video Bridge

In video, edges can also help identify moving structures, but motion requires temporal comparison.

Conceptually:

```text
frame t
+
frame t+1
→
temporal change
```

This becomes C30.

---

# 10.41 Colour Edge Detection

A colour image has multiple channels.

A simplistic approach is:

```text
convert RGB → grayscale
→ detect edges
```

This is often useful but can discard chromatic transitions that have little grayscale contrast.

A more advanced approach can compute gradients across colour vectors or use a suitable colour representation.

> **Extension:** The “best edge” depends on whether the task cares about luminance boundaries, chromatic boundaries, or both.

---

# 10.42 Edge Evaluation

When a reference edge map is available, evaluate:

```text
true positives
false positives
false negatives
```

From these we can derive measures such as:

\[
\text{precision}
=
\frac{TP}{TP+FP}
\]

\[
\text{recall}
=
\frac{TP}{TP+FN}
\]

The suitable evaluation protocol should account for localization tolerance and application context.

---

# 10.43 Sharpening Evaluation

For sharpening, useful checks include:

### Visual

- improved apparent detail?
- halos?
- ringing?
- noise amplification?

### Numerical/reference-based

- MSE/PSNR,
- edge contrast,
- gradient statistics.

### Task-based

- better OCR?
- better segmentation?
- better feature matching?

Again:

> A higher edge strength is not automatically a better image.

---

# 10.44 Implementation Safety Checklist

Before applying an edge or sharpening operator:

```text
1. inspect image dtype
2. inspect value range
3. choose working datatype
4. choose padding
5. apply filter
6. inspect signed response
7. compute magnitude or sharpening result
8. normalize only for display if needed
9. preserve original quantitative result
```

This prevents many common bugs.

---

# 10.45 Common Traps

## Trap 1 — “Edges are always one-pixel-wide.”

False.

Real edges can be blurred or spread over multiple pixels.

## Trap 2 — “Sobel produces a binary edge image.”

False.

It produces derivative responses; thresholding is an additional step.

## Trap 3 — “Gradient direction equals edge direction.”

False.

Gradient direction is approximately perpendicular to the local edge orientation.

## Trap 4 — “Second derivative is always better than first derivative.”

False.

It is sensitive to noise and has different localization/response properties.

## Trap 5 — “Sharpening creates missing information.”

False.

It enhances existing spatial variation; it does not reconstruct genuinely missing detail.

## Trap 6 — “More sharpening means more detail.”

Not necessarily.

It can mainly amplify noise and produce artifacts.

## Trap 7 — “A strong gradient always means an object boundary.”

False.

Texture, noise and illumination changes can also produce strong gradients.

## Trap 8 — “Gradient magnitude can always be stored as uint8.”

False.

Derivative outputs can be signed and exceed 255.

---

# 10.46 Exam Formula Sheet

### Gradient

\[
\boxed{
\nabla f=
\begin{bmatrix}
f_x\\
f_y
\end{bmatrix}
}
\]

### Magnitude

\[
\boxed{
|\nabla f|=
\sqrt{f_x^2+f_y^2}
}
\]

### Direction

\[
\boxed{
\theta=\operatorname{atan2}(f_y,f_x)
}
\]

### Laplacian

\[
\boxed{
\nabla^2f=f_{xx}+f_{yy}
}
\]

### Unsharp mask

\[
\boxed{
m=f-f_{\text{blur}}
}
\]

\[
\boxed{
g=f+km
}
\]

### High-boost

\[
\boxed{
g=Af-f_{\text{blur}},\quad A>1
}
\]

### Binary gradient threshold

\[
\boxed{
E=
\begin{cases}
1,&|\nabla f|\ge T\\
0,&|\nabla f|<T
\end{cases}
}
\]

---

# 10.47 Exam-Style Problem — Sobel

Given:

\[
G_x=12,\qquad G_y=5
\]

Calculate gradient magnitude.

\[
G=
\sqrt{12^2+5^2}
\]

\[
=
\sqrt{144+25}
\]

\[
=
\sqrt{169}
\]

\[
\boxed{13}
\]

Direction:

\[
\theta=
\operatorname{atan2}(5,12)
\approx22.62^\circ
\]

The local edge orientation is approximately:

\[
22.62^\circ+90^\circ
=
112.62^\circ
\]

under the ideal perpendicular relationship.

---

# 10.48 Exam-Style Problem — Sharpening

At a pixel:

\[
f=100
\]

and:

\[
f_{\text{blur}}=90
\]

For:

\[
k=2
\]

detail mask:

\[
m=100-90=10
\]

output:

\[
g=100+2(10)
\]

\[
\boxed{120}
\]

Interpretation:

```text
local detail
→ amplified by factor controlled by k
```

---

# 10.49 Exam-Style Problem — Laplacian

Given:

\[
f=120,\qquad \nabla^2 f=-30
\]

and sharpening rule:

\[
g=f-\nabla^2f
\]

then:

\[
g=120-(-30)
\]

\[
\boxed{150}
\]

The sign convention must always match the chosen Laplacian definition.

---

# 10.50 Cross-Book Bridges

> **C09 BRIDGE**  
> Denoising controls the noise amplification problem that naturally appears in derivative-based edge detection.

> **C08 BRIDGE**  
> Kernel convolution, padding, signed responses and filtering geometry originate in the general spatial-filter chapter.

> **C15–C20 BRIDGE**  
> Edge maps become useful inputs for segmentation, morphology and feature extraction.

> **C19–C20 BRIDGE**  
> Gradient direction is foundational for HOG and classical local-feature reasoning.

> **C30 BRIDGE**  
> Spatial edges become temporal/motion evidence when frames are compared.

> **LAB BRIDGE**  
> Implement Sobel/Prewitt/Roberts, gradient magnitude, thresholding, Laplacian sharpening and a Canny-style pipeline.

> **PRACTICE BRIDGE**  
> Work derivative calculations, orientation reasoning, sharpening calculations and edge-threshold tradeoffs.

> **EXAM BRIDGE**  
> Be able to derive gradient magnitude, write Sobel/Prewitt/Laplacian kernels, explain edge orientation, unsharp masking, and the Canny pipeline.

---

# 10.51 Quick Recall

```text
EDGE
→ rapid spatial change

GRADIENT
→ first derivative

LAPLACIAN
→ second derivative

SOBEL / PREWITT / ROBERTS
→ gradient approximations

CANNY
→ multi-stage refined edge detection

UNSHARP
→ original + detail

HIGH-BOOST
→ stronger detail emphasis
```

Core rule:

> **Denoise before differentiation when noise would otherwise dominate the derivative response.**

---

# 10.52 Chapter Checkpoint

1. Define an image edge.
2. Explain step and ramp edges.
3. Define the first derivative and its edge-detection role.
4. Define the image gradient.
5. Derive gradient magnitude and direction.
6. Why is edge orientation approximately perpendicular to gradient direction?
7. Compare Roberts, Prewitt and Sobel.
8. Calculate a Sobel/gradient response for a small matrix.
9. Why can derivative filters amplify noise?
10. Explain why smoothing is often applied before edge detection.
11. What is the Laplacian?
12. Explain zero-crossing edge detection.
13. Define unsharp masking.
14. Compare unsharp and high-boost filtering.
15. What is non-maximum suppression?
16. Explain Canny's double-threshold and hysteresis idea.
17. Why does an edge map not equal object detection?
18. Why can aggressive sharpening introduce halos or ringing?
19. Why should derivative responses remain signed/floating until interpretation?
20. How can gradient orientation contribute to feature descriptors?

---

# 10.53 Unit II Progress

At this point the spatial-domain core has become:

```text
C06
INTENSITY TRANSFORMATIONS
        ↓
C07
HISTOGRAMS
        ↓
C08
SPATIAL FILTERS + CONVOLUTION
        ↓
C09
NOISE + SMOOTHING
        ↓
C10
SHARPENING + EDGES
```

The remaining Unit II progression is:

```text
C11
GEOMETRIC TRANSFORMATIONS
        ↓
C12
FOURIER TRANSFORM
        ↓
C13
FREQUENCY-DOMAIN FILTERING
        ↓
C14
RESTORATION + DEBLURRING
```

The conceptual progression is now:

```text
intensity
→ distribution
→ neighbourhood
→ noise
→ derivatives
→ geometry
→ frequency
→ degradation model
```

That is the central computational structure of the classical Digital Image Processing pipeline.
