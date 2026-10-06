---
id: "C20"
title: "SIFT, SURF, ORB and HOG"
layer: "MAIN"
part: "III — Understanding Image Content"
unit: "III"
version: "1.0"
status: "REFERENCE BUILD"
syllabus_scope:
  - "SIFT"
  - "SURF"
  - "HOG"
  - "Classical feature detection and description"
tags:
  - "CORE"
  - "EXAM"
  - "MATH"
  - "DEEP DIVE"
  - "LAB"
  - "FEATURES"
  - "DESCRIPTORS"
  - "SIFT"
  - "SURF"
  - "ORB"
  - "HOG"
prerequisites:
  - "C10"
  - "C19"
related:
  - "C11"
  - "C17"
  - "C18"
  - "C25"
  - "C28"
  - "C30"
math:
  - "M06"
  - "M08"
  - "M09"
  - "M10"
lab:
  - "LAB-U3-06"
  - "LAB-U4-02"
exam:
  - "EXAM-U3"
practice:
  - "P-C20"
assets:
  - "D-C20-01"
  - "D-C20-02"
  - "D-C20-03"
---

# Chapter 20 — SIFT, SURF, ORB and HOG

> **Chapter thesis**  
> Classical feature methods solve different versions of the same representation problem: **find useful local or dense image structure, encode it compactly, and make the resulting representation useful for matching or recognition**. SIFT emphasizes robust scale-space local descriptors, SURF emphasizes efficient Hessian-based approximations, ORB emphasizes fast binary matching, and HOG emphasizes dense gradient-based shape information.

**Part III — Understanding Image Content**  
**Syllabus anchor:** Unit III explicitly names SIFT, SURF and HOG, while ORB is included as a modern practical extension of the classical local-feature family. fileciteturn4file0L41-L45

---

# 20.0 Why a Dedicated Method Chapter?

C19 established:

```text
feature
keypoint
descriptor
matching
```

Now we need to understand the actual algorithms.

The most useful comparison is:

```text
SIFT
→ robust local feature

SURF
→ efficient classical local feature

ORB
→ fast binary local feature

HOG
→ dense gradient/shape descriptor
```

They should not be judged using one single metric.

---

# 20.1 Four Different Design Philosophies

| Method | Main design idea |
|---|---|
| SIFT | robustness through scale-space + orientation-normalized gradient descriptor |
| SURF | speed through Hessian approximation + integral images |
| ORB | speed/compactness through FAST + binary BRIEF |
| HOG | shape representation through dense local gradient histograms |

This is the first comparison to remember.

---

# 20.2 SIFT Pipeline

```text
INPUT IMAGE
     ↓
Gaussian scale space
     ↓
Difference of Gaussians
     ↓
scale-space extrema
     ↓
keypoint localization/refinement
     ↓
low-contrast / unstable-point filtering
     ↓
orientation assignment
     ↓
local gradient histograms
     ↓
descriptor normalization
     ↓
128-D descriptor
```

The power of SIFT comes from the fact that detection and description are designed as one coherent representation system.

---

# 20.3 SIFT Scale Space

The Gaussian-smoothed image at scale \(\sigma\):

\[
L(x,y,\sigma)
=
G(x,y,\sigma)*I(x,y)
\]

with:

\[
G(x,y,\sigma)
=
\frac{1}{2\pi\sigma^2}
e^{-\frac{x^2+y^2}{2\sigma^2}}
\]

As \(\sigma\) increases:

```text
fine detail disappears
→ larger-scale structures dominate
```

---

# 20.4 Why Use Difference of Gaussians?

SIFT forms:

\[
D(x,y,\sigma)
=
L(x,y,k\sigma)-L(x,y,\sigma)
\]

This approximates scale-normalized Laplacian behaviour and allows efficient detection of extrema across space and scale.

The important conceptual role is:

```text
compare neighbouring scales
→ identify structures distinctive at a particular scale
```

---

# 20.5 SIFT Keypoint Candidate Detection

Each point is compared with neighbouring points in:

```text
current scale
previous scale
next scale
```

A local maximum/minimum becomes a candidate.

This produces:

```text
position
+
scale
```

for each candidate.

---

# 20.6 Why Scale Matters

Suppose a logo is:

```text
large in Image A
small in Image B
```

A single fixed-size detector may fail.

SIFT searches across multiple scales.

Therefore the same physical structure can potentially produce corresponding keypoints at different image sizes.

This is the origin of scale robustness.

---

# 20.7 Low-Contrast Point Rejection

A candidate with very weak response may be unstable.

Therefore SIFT rejects sufficiently low-contrast points.

Conceptually:

```text
strong distinct structure
→ keep

weak/noisy structure
→ reject
```

This improves descriptor reliability.

---

# 20.8 Edge-Like Point Rejection

A strong DoG response can come from an elongated edge.

But points on an edge are often poorly localized along the edge direction.

SIFT uses local curvature information to reject unstable edge-like candidates.

The exact test is derived from the Hessian of the local DoG approximation.

---

# 20.9 SIFT Orientation Assignment

For each keypoint, compute local gradients.

Magnitude:

\[
m=
\sqrt{G_x^2+G_y^2}
\]

Orientation:

\[
\theta=
\operatorname{atan2}(G_y,G_x)
\]

Nearby gradients vote into an orientation histogram.

The dominant orientation becomes the keypoint's local reference direction.

---

# 20.10 Rotation Robustness

The local descriptor is constructed relative to the assigned dominant orientation.

Therefore if:

```text
image rotates
```

the local coordinate frame rotates too.

This allows corresponding descriptors to remain comparable.

Rotation robustness is therefore built into the **coordinate normalization**, not merely into a later matching trick.

---

# 20.11 SIFT Descriptor Geometry

Around the keypoint:

```text
16 × 16-like local support
        ↓
4 × 4 cells
        ↓
8 orientation bins
```

So:

\[
4\times4\times8=128
\]

dimensions.

Each cell stores a histogram of gradient orientations weighted by gradient magnitude and spatial contribution.

---

# 20.12 Why Use Histograms Instead of Raw Pixels?

Raw pixel values are sensitive to:

```text
small translations
brightness changes
local noise
```

Gradient histograms summarize local shape structure more robustly.

Therefore:

```text
raw pixels
→ derivatives
→ orientation distribution
```

is a purposeful abstraction.

---

# 20.13 SIFT Descriptor Normalization

Let:

\[
d_i
\]

be descriptor components.

L2 normalization:

\[
\hat{\mathbf d}
=
\frac{\mathbf d}
{\sqrt{\sum_i d_i^2}}
\]

The original SIFT pipeline also clips unusually large values and renormalizes, reducing sensitivity to illumination-related changes.

---

# 20.14 SIFT Matching

Given:

\[
d_A,d_B
\]

use Euclidean distance:

\[
d_E=
\sqrt{\sum_i(d_{A,i}-d_{B,i})^2}
\]

The nearest neighbour is a candidate match.

Then use a ratio test:

\[
\frac{d_1}{d_2}<r
\]

to reject ambiguous matches.

---

# 20.15 SIFT Strengths

SIFT is valuable when:

```text
scale changes matter
rotation changes matter
local matching matters
moderate viewpoint changes exist
```

It produces relatively distinctive descriptors.

---

# 20.16 SIFT Limitations

Potential limitations include:

```text
computational cost
larger descriptor storage
sensitivity to extreme viewpoint/illumination changes
weak performance in textureless scenes
```

It is robust, not magic.

---

# 20.17 SURF Pipeline

A conceptual SURF pipeline is:

```text
INPUT
 ↓
integral image
 ↓
Hessian response across scales
 ↓
scale-space keypoints
 ↓
orientation estimation
 ↓
wavelet-response descriptor
 ↓
matching
```

SURF's central engineering idea is efficient approximation.

---

# 20.18 SURF Hessian Matrix

At point \((x,y)\):

\[
H(x,y,\sigma)=
\begin{bmatrix}
L_{xx}&L_{xy}\\
L_{xy}&L_{yy}
\end{bmatrix}
\]

The determinant:

\[
\det(H)
=
L_{xx}L_{yy}-L_{xy}^2
\]

is used as a blob-like interest response.

---

# 20.19 Why Hessian Determinant Detects Blobs

A blob-like structure has substantial second-order variation in multiple directions.

Thus:

```text
Lxx strong
Lyy strong
cross-term controlled
→ strong determinant
```

The detector can identify distinctive scale-dependent structures.

---

# 20.20 Box-Filter Approximation

SURF approximates derivatives with box filters.

The integral image then allows these rectangular sums to be calculated efficiently.

This is the computational trick:

```text
complex derivative convolution
→ box approximation
→ integral-image sum
→ faster response
```

---

# 20.21 Integral Image Definition

For grayscale image \(I\):

\[
S(x,y)
=
\sum_{i=0}^{x}
\sum_{j=0}^{y}
I(i,j)
\]

For a rectangle:

```text
A ───── B
│       │
│ RECT  │
│       │
C ───── D
```

the sum can be computed from four integral-image values:

\[
S(D)-S(B)-S(C)+S(A)
\]

with coordinate indexing adjusted appropriately.

---

# 20.22 Why Integral Images Matter

A rectangle sum can then be computed in approximately constant time regardless of rectangle area.

This is extremely useful for repeated box-filter evaluation.

The broader algorithmic lesson is:

> Precompute cumulative information when many repeated structured queries are required.

---

# 20.23 SURF Orientation

SURF estimates local orientation using Haar-wavelet responses in a neighbourhood.

The dominant directional response defines the keypoint orientation.

The descriptor is then expressed relative to that orientation.

Thus SURF also seeks rotation robustness.

---

# 20.24 SURF Descriptor

A common SURF descriptor divides the local neighbourhood into subregions and summarizes:

```text
Haar x response
Haar y response
|Haar x|
|Haar y|
```

For each subregion, these statistics are aggregated.

A widely used standard SURF descriptor variant has 64 dimensions, with an extended 128-dimensional variant.

> **Important:** Descriptor length depends on the selected SURF variant.

---

# 20.25 SURF Matching

Because the descriptor is floating-point:

\[
L_2
\]

distance is a natural comparison metric.

The same general matching workflow can be used:

```text
nearest neighbour
→ ratio test
→ geometric verification
```

---

# 20.26 SURF Strengths

```text
efficient classical detector
good scale handling
orientation robustness
smaller common descriptor than classic SIFT
```

The exact speed advantage depends on implementation/hardware.

---

# 20.27 SURF Limitations

Potential limitations:

```text
less commonly available in some modern libraries
patent/history considerations affected practical use
not necessarily best under every transformation
```

For a university course, the important conceptual contribution is:

```text
Hessian
+
integral image
+
efficient local descriptor
```

---

# 20.28 ORB Pipeline

ORB means:

```text
Oriented FAST
+
Rotated BRIEF
```

Pipeline:

```text
image
 ↓
FAST keypoints
 ↓
orientation estimation
 ↓
rotate BRIEF sampling pattern
 ↓
binary descriptor
 ↓
Hamming matching
```

It is designed for speed and compact representation.

---

# 20.29 FAST Corner Detector

For candidate pixel \(p\), inspect pixels on a circle around it.

Classical FAST determines whether enough contiguous circle pixels are significantly:

```text
brighter than centre
or
darker than centre
```

Conceptually:

```text
ring of neighbours
+
centre
→
corner decision
```

This is efficient because it uses intensity comparisons rather than heavier matrix calculations.

---

# 20.30 FAST Is Not the Same as Harris

| Harris | FAST |
|---|---|
| structure tensor | circle intensity test |
| derivative-based | comparison-based |
| algebraically richer | very fast |
| corner response score | decision/test |
| different robustness/cost tradeoff | efficient real-time candidate detector |

Both are corner-detection approaches, but their design philosophies differ.

---

# 20.31 ORB Orientation

FAST gives location but does not by itself provide a robust orientation.

ORB estimates orientation from local intensity moments.

A centroid-like vector is used to determine the direction of the local patch.

The BRIEF sampling pattern is then rotated accordingly.

---

# 20.32 BRIEF Binary Test

For sampled points \(p,q\):

\[
\tau(p,q)=
\begin{cases}
1,&I(p)<I(q)\\
0,&I(p)\ge I(q)
\end{cases}
\]

Repeat for many pairs:

\[
\mathbf b=
[\tau_1,\tau_2,\ldots,\tau_N]
\]

The descriptor is:

\[
\boxed{\mathbf b\in\{0,1\}^N}
\]

---

# 20.33 Why Binary Descriptors Are Fast

A binary descriptor can be stored compactly.

Comparison can use bitwise operations and popcount:

```text
descriptor A
XOR
descriptor B
 ↓
count 1s
 ↓
Hamming distance
```

This can be extremely efficient.

---

# 20.34 Worked ORB Matching

A:

\[
10110010
\]

B:

\[
10011011
\]

XOR:

\[
00101001
\]

Number of ones:

\[
3
\]

Therefore:

\[
\boxed{d_H=3}
\]

This demonstrates the computational simplicity of binary matching.

---

# 20.35 ORB and Scale

ORB is rotation-aware, but it is not as fully scale-invariant as SIFT's explicit scale-space design.

An ORB pipeline can use image pyramids to improve scale robustness.

Still:

```text
SIFT
→ stronger explicit scale-space strategy

ORB
→ faster, more compact
```

This is the appropriate conceptual tradeoff.

---

# 20.36 ORB Strengths

```text
fast
compact
binary matching
good for real-time systems
easy to integrate into many practical pipelines
```

---

# 20.37 ORB Limitations

Potential weaknesses:

```text
less robust than SIFT under large scale/viewpoint changes
binary descriptors can be less distinctive in repetitive textures
performance depends on detector parameters
```

Again, benchmark results depend on the actual data.

---

# 20.38 HOG Pipeline

HOG is fundamentally different from the keypoint-centric methods.

```text
image
 ↓
optional normalization
 ↓
gradient calculation
 ↓
cell orientation histograms
 ↓
block grouping
 ↓
block normalization
 ↓
concatenate
 ↓
feature vector
```

It is typically computed over a dense image region rather than around sparse keypoints.

---

# 20.39 HOG Gradient Calculation

Given:

\[
G_x,\quad G_y
\]

compute:

\[
m=
\sqrt{G_x^2+G_y^2}
\]

and:

\[
\theta=
\operatorname{atan2}(G_y,G_x)
\]

The magnitude supplies the vote weight.

The orientation determines the histogram bin.

---

# 20.40 Orientation Binning

Suppose the descriptor uses:

\[
9
\]

orientation bins over a chosen angular range.

Each pixel contributes to nearby bins according to its orientation and magnitude.

Some implementations use interpolation between bins.

The exact binning convention should be documented.

---

# 20.41 Cells

The image is divided into small cells.

For example:

```text
8 × 8 pixels per cell
```

might be used in a common configuration.

Each cell produces an orientation histogram.

The exact cell size is a parameter, not a universal requirement.

---

# 20.42 Blocks

Cells are grouped into blocks.

For example:

```text
2 × 2 cells per block
```

A block concatenates its cell histograms and normalizes them.

Overlapping blocks improve local normalization.

---

# 20.43 HOG Normalization

For vector \(v\), an L2-type normalization can be:

\[
v'=
\frac{v}
{\sqrt{\|v\|_2^2+\epsilon^2}}
\]

This reduces sensitivity to local illumination/contrast changes.

Other normalization choices exist.

---

# 20.44 Why HOG Represents Shape

Consider a person's silhouette.

The silhouette contains:

```text
vertical boundaries
horizontal boundaries
diagonal boundaries
```

These create characteristic gradient orientation patterns.

HOG turns those patterns into a vector.

Therefore:

```text
shape
→ gradients
→ orientation statistics
→ descriptor
```

---

# 20.45 HOG Strengths

```text
strong shape representation
interpretable
dense
works well with simple classifiers
```

It was historically very important in classical object detection before deep neural networks became dominant.

---

# 20.46 HOG Limitations

```text
not inherently scale invariant
not inherently rotation invariant
can become high-dimensional
depends strongly on cell/block parameters
less effective for large viewpoint variation
```

It should be thought of as a shape/gradient descriptor, not a complete object-recognition system.

---

# 20.47 SIFT vs SURF vs ORB vs HOG — Core Table

| Aspect | SIFT | SURF | ORB | HOG |
|---|---|---|---|---|
| detector style | DoG scale-space | Hessian | FAST | dense gradient |
| keypoint-centric | yes | yes | yes | no |
| scale strategy | strong | strong | limited/pyramid-dependent | not inherent |
| orientation strategy | dominant gradient | wavelet response | intensity moments | histogram orientation |
| descriptor | gradient histogram | wavelet statistics | binary comparisons | gradient histograms |
| descriptor type | float | float | binary | float |
| common distance | L2 | L2 | Hamming | L2-like |
| main strength | robust local matching | efficient robust local features | speed | shape |
| typical computation | heavier | moderate | fast | moderate/high |
| matching style | local correspondence | local correspondence | local correspondence | typically feature+classifier |

---

# 20.48 Method Selection

### Use SIFT when:

```text
robust local matching
scale variation
rotation
moderate viewpoint changes
```

are important.

### Use SURF when:

```text
classical Hessian-style features
+
efficient approximation
```

are desired.

### Use ORB when:

```text
speed
+
compact binary descriptors
+
real-time matching
```

matter.

### Use HOG when:

```text
object shape
+
dense gradient structure
```

are the main signal.

---

# 20.49 Feature Pipeline for Image Registration

A robust classical registration workflow:

```text
IMAGE A                      IMAGE B
   ↓                            ↓
detect keypoints              detect keypoints
   ↓                            ↓
compute descriptors           compute descriptors
   ↓                            ↓
          MATCH
             ↓
       ratio / distance test
             ↓
       geometric verification
             ↓
       estimate transform
             ↓
          warp image
             ↓
         aligned result
```

C11 supplies the transformation machinery.

---

# 20.50 Feature Pipeline for Object Recognition

A classical pipeline can be:

```text
training images
 ↓
feature extraction
 ↓
descriptor database
 ↓

query image
 ↓
feature extraction
 ↓
descriptor matching
 ↓
evidence aggregation
 ↓
object hypothesis
```

A classifier can replace or complement the matching stage.

---

# 20.51 HOG + Classifier Pipeline

Historically common structure:

```text
image
 ↓
resize
 ↓
HOG
 ↓
feature vector
 ↓
linear SVM / other classifier
 ↓
class / detection
```

The feature descriptor alone is not the final decision model.

---

# 20.52 Matching Thresholds

For descriptor matching, a threshold can be applied:

\[
d<\tau
\]

But a raw distance threshold is sensitive to:

- descriptor normalization,
- image content,
- descriptor family.

Ratio tests and geometric validation can be more robust.

---

# 20.53 RANSAC Integration

Suppose we have matches:

\[
(p_i,p_i')
\]

Estimate transformation \(T\).

RANSAC chooses:

```text
minimal sample
→ model
→ count inliers
→ repeat
```

A match is an inlier if:

\[
\|p_i'-T(p_i)\|<\epsilon
\]

under the chosen geometric model and error metric.

---

# 20.54 Worked Inlier Decision

Suppose:

\[
e_i=2.4
\]

and:

\[
\epsilon=3
\]

Then:

\[
2.4<3
\]

so:

\[
\boxed{\text{inlier}}
\]

If:

\[
e_i=7
\]

then:

\[
\boxed{\text{outlier}}
\]

under this criterion.

---

# 20.55 Descriptor Matching Complexity

Suppose:

```text
N descriptors in A
M descriptors in B
```

A naive all-pairs comparison requires approximately:

\[
O(NM)
\]

distance calculations.

This can become expensive.

Therefore practical systems use:

```text
k-d trees
FLANN-like approximate search
LSH / binary matching structures
specialized nearest-neighbour indexes
```

depending on descriptor type.

---

# 20.56 Binary vs Floating Descriptors

| Property | Floating | Binary |
|---|---|---|
| examples | SIFT, SURF, HOG | ORB |
| comparison | L2/cosine-like depending on design | Hamming |
| storage | larger | compact |
| matching | arithmetic-heavy | bit operations |
| discriminative structure | richer continuous values | binary pattern |

This is a systems-level tradeoff.

---

# 20.57 Descriptor Dimensionality

Higher dimension can mean:

```text
more representational capacity
```

but also:

```text
more memory
more computation
possible redundancy
```

So:

> Descriptor dimension is a design parameter, not a quality score.

---

# 20.58 Feature Detector Thresholds

Detector parameters influence:

```text
number of keypoints
stability
computation
matching quality
```

A low threshold:

```text
more features
+
more weak/noisy points
```

A high threshold:

```text
fewer features
+
potentially stronger points
```

This is a recurring detection tradeoff.

---

# 20.59 Feature Scale and Image Resolution

A feature method cannot recover structure that sampling or blur has destroyed.

For example:

```text
fine texture
→ downsample
→ feature disappears
```

This connects C03/C09/C14 directly to C19/C20.

Feature extraction is constrained by image formation and preprocessing.

---

# 20.60 Feature Robustness Test Matrix

A useful lab test changes one condition at a time:

| Condition | Example |
|---|---|
| translation | shift by 20 px |
| rotation | +30° |
| scale | 0.5× / 2× |
| blur | Gaussian blur |
| brightness | darker/brighter |
| noise | additive noise |
| compression | stronger JPEG |
| viewpoint | perspective change |

Measure:

```text
detected features
repeatable features
matches
correct matches
inliers
runtime
```

---

# 20.61 Practical SIFT vs ORB Experiment

Use:

```text
Image A
Image B = rotated + scaled version
```

Run both.

Record:

```text
SIFT:
keypoints
descriptor size
good matches
inliers
runtime

ORB:
same measurements
```

Then compare:

```text
robustness
speed
memory
matching precision
```

This produces engineering evidence instead of relying on “SIFT is better” claims.

---

# 20.62 Practical HOG Experiment

Take two visually distinguishable shape categories.

Vary:

```text
cell size
block size
orientation bins
```

Then train the same simple classifier.

Record:

```text
feature dimension
training time
validation accuracy
confusion matrix
```

This shows how descriptor geometry affects classification.

---

# 20.63 Common Traps

## Trap 1 — “SIFT, SURF, ORB and HOG are interchangeable.”

False.

They have different detector/descriptor philosophies.

## Trap 2 — “HOG detects keypoints.”

Not in the usual dense-grid formulation.

## Trap 3 — “ORB is simply a smaller SIFT.”

False.

It uses a fundamentally different binary descriptor and detector.

## Trap 4 — “SURF is exactly the same as SIFT but faster.”

False.

The detector and descriptor design differ.

## Trap 5 — “All descriptors should use Euclidean distance.”

False.

Binary descriptors such as ORB are naturally compared with Hamming distance.

## Trap 6 — “More keypoints always improve registration.”

False.

Incorrect or unstable matches can increase outliers.

## Trap 7 — “A descriptor match proves the object is present.”

False.

Matching should be validated geometrically and/or semantically.

## Trap 8 — “HOG is rotation invariant.”

False in its standard form.

## Trap 9 — “Scale-space guarantees perfect scale invariance.”

False.

Sampling, blur, parameter ranges and viewpoint limits still matter.

## Trap 10 — “A feature detector works equally well on every image.”

False.

Textureless, repetitive, blurred or saturated images can be difficult.

---

# 20.64 Exam Formula Sheet

### Gaussian scale space

\[
\boxed{
L(x,y,\sigma)=G(x,y,\sigma)*I(x,y)
}
\]

### DoG

\[
\boxed{
D(x,y,\sigma)=
L(x,y,k\sigma)-L(x,y,\sigma)
}
\]

### Gradient magnitude

\[
\boxed{
m=
\sqrt{G_x^2+G_y^2}
}
\]

### Gradient orientation

\[
\boxed{
\theta=
\operatorname{atan2}(G_y,G_x)
}
\]

### Hessian determinant

\[
\boxed{
\det(H)=L_{xx}L_{yy}-L_{xy}^2
}
\]

### Hamming distance

\[
\boxed{
d_H=
\sum_i
\mathbf1[a_i\ne b_i]
}
\]

### L2 distance

\[
\boxed{
d_2=
\sqrt{\sum_i(a_i-b_i)^2}
}
\]

### Ratio test

\[
\boxed{
d_1/d_2<r
}
\]

### Reprojection error

\[
\boxed{
e=\|p'-T(p)\|
}
\]

---

# 20.65 Exam-Style Problem — DoG

Suppose:

\[
L(x,y,\sigma)=40
\]

and:

\[
L(x,y,k\sigma)=55
\]

Then:

\[
D=55-40
\]

\[
\boxed{15}
\]

The positive DoG response indicates a stronger response at the larger scale under the chosen ordering.

---

# 20.66 Exam-Style Problem — Hessian Determinant

Given:

\[
L_{xx}=5
\]

\[
L_{yy}=4
\]

\[
L_{xy}=1
\]

Then:

\[
\det(H)
=
(5)(4)-(1)^2
\]

\[
=20-1
\]

\[
\boxed{19}
\]

---

# 20.67 Exam-Style Problem — Hamming

Descriptor A:

\[
10101010
\]

Descriptor B:

\[
11100011
\]

Compare bits.

Differences occur at positions:

```text
2
4
5
7
```

Therefore:

\[
\boxed{d_H=4}
\]

---

# 20.68 Exam-Style Problem — Descriptor Ratio

Best:

\[
d_1=12
\]

Second best:

\[
d_2=30
\]

Ratio threshold:

\[
r=0.5
\]

Then:

\[
\frac{12}{30}=0.4
\]

Since:

\[
0.4<0.5
\]

the match passes.

---

# 20.69 Engineering Insight — Match Quality Is a Pipeline Property

A poor matching result may come from:

```text
bad image quality
→ bad keypoints
→ bad descriptors
→ ambiguous nearest neighbours
→ insufficient geometric verification
```

Therefore debugging only the final matcher can miss the true problem.

Inspect:

```text
image
→ keypoints
→ descriptors
→ candidate matches
→ filtered matches
→ geometric inliers
```

This is the feature equivalent of inspecting intermediate filter outputs in C08–C14.

---

# 20.70 Cross-Book Bridges

> **C03 BRIDGE**  
> Sampling determines whether feature-scale information is actually available.

> **C09 BRIDGE**  
> Noise can create unstable keypoints and alter gradient descriptors.

> **C10 BRIDGE**  
> Gradient magnitude/orientation are the mathematical foundation of HOG and SIFT.

> **C11 BRIDGE**  
> Feature correspondences can estimate affine/homography transformations for registration.

> **C17–C18 BRIDGE**  
> Segmentation/morphology can define ROIs before feature extraction.

> **C25 BRIDGE**  
> Feature vectors can become inputs to classical image classifiers.

> **C28 BRIDGE**  
> Deep detectors learn feature representations automatically rather than using only hand-crafted descriptors.

> **C30 BRIDGE**  
> Stable keypoints can be tracked across video frames.

> **LAB BRIDGE**  
> Implement SIFT/ORB matching, HOG extraction and geometric verification; record runtime and inliers.

> **PRACTICE BRIDGE**  
> Solve DoG/Hessian/gradient/Hamming/L2/ratio-test calculations and compare algorithm design tradeoffs.

> **EXAM BRIDGE**  
> Be able to explain SIFT, SURF, ORB and HOG pipelines, descriptor types, matching metrics and strengths/limitations.

---

# 20.71 Quick Recall

```text
SIFT
→ DoG
→ scale
→ orientation
→ gradient descriptor
→ 128-D

SURF
→ Hessian
→ integral image
→ Haar responses

ORB
→ FAST
→ orientation
→ rotated BRIEF
→ binary
→ Hamming

HOG
→ gradient
→ cells
→ orientation histograms
→ block normalization
→ shape descriptor
```

Core comparison:

```text
SIFT
→ robustness

SURF
→ efficient classical robustness

ORB
→ speed + binary compactness

HOG
→ dense shape representation
```

---

# 20.72 Chapter Checkpoint

1. Outline the SIFT pipeline.
2. Why does SIFT use scale space?
3. Write the Gaussian scale-space equation.
4. Explain the Difference-of-Gaussians.
5. Why does SIFT assign a dominant orientation?
6. Why is the classic SIFT descriptor 128-dimensional?
7. Explain SIFT descriptor normalization.
8. Outline SURF.
9. What is the Hessian determinant?
10. Why do integral images speed rectangular filtering?
11. Explain FAST corner detection conceptually.
12. What does ORB add to FAST and BRIEF?
13. Why is Hamming distance suitable for ORB?
14. Describe the HOG pipeline.
15. Explain HOG cells and blocks.
16. Compare SIFT, SURF, ORB and HOG.
17. Why is geometric verification needed after descriptor matching?
18. Explain the ratio test.
19. Design an experiment comparing SIFT and ORB.
20. Design an experiment studying HOG parameter effects.

---

# 20.73 Part III Completion Gate

Part III now forms a complete progression:

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
        ↓
C19
FEATURES + DESCRIPTORS
        ↓
C20
SIFT / SURF / ORB / HOG
```

The intellectual movement is:

```text
pixel
→ label
→ connected region
→ shape
→ feature
→ descriptor
→ correspondence
```

That is the classical computer-vision bridge from image processing to recognition.

---

# 20.74 Transition to Part IV

Part III asks:

```text
How can we understand or represent image content?
```

Part IV changes the optimization objective:

```text
How can we represent image information using fewer bits?
```

The next sequence is:

```text
C21
IMAGE COMPRESSION FUNDAMENTALS
        ↓
C22
ENTROPY + RLE + HUFFMAN
        ↓
C23
TRANSFORM CODING + DCT
        ↓
C24
JPEG END TO END
```

The central transition is:

```text
understand image information
→
measure redundancy
→
encode efficiently
→
compress deliberately
```
