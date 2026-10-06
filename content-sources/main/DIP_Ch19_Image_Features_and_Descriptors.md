---
id: "C19"
title: "Image Features and Descriptors"
layer: "MAIN"
part: "III — Understanding Image Content"
unit: "III"
version: "1.0"
status: "REFERENCE BUILD"
syllabus_scope:
  - "Image features"
  - "Feature representation"
  - "Descriptors"
tags:
  - "CORE"
  - "EXAM"
  - "MATH"
  - "DEEP DIVE"
  - "LAB"
  - "FEATURES"
  - "DESCRIPTORS"
  - "COMPUTER VISION"
prerequisites:
  - "C10"
  - "C15"
  - "C17"
  - "C18"
related:
  - "C20"
  - "C25"
  - "C28"
  - "C30"
math:
  - "M05"
  - "M06"
  - "M08"
  - "M09"
lab:
  - "LAB-U3-05"
  - "LAB-U3-06"
  - "LAB-U4-02"
exam:
  - "EXAM-U3"
practice:
  - "P-C19"
assets:
  - "D-C19-01"
  - "D-C19-02"
  - "D-C19-03"
---

# Chapter 19 — Image Features and Descriptors

> **Chapter thesis**  
> A raw image contains enormous amounts of numerical information, but many computer-vision tasks need a more compact representation of useful structure. A **feature** is a measurable property of an image or region; a **descriptor** is a structured numerical representation intended to characterize that feature so it can be compared, matched or used for later analysis.

**Part III — Understanding Image Content**  
**Syllabus anchor:** Unit III places feature-detection methods such as SIFT, SURF and HOG after segmentation and morphology. fileciteturn4file0L41-L45

---

# 19.0 Why Features?

A 1920×1080 RGB image contains millions of channel samples.

A vision system may not need all of them for every task.

Instead, it can extract information such as:

```text
edges
corners
blobs
texture
shape
colour statistics
gradient orientation
keypoints
```

The pipeline becomes:

```text
IMAGE
  ↓
candidate structure
  ↓
FEATURE DETECTION
  ↓
FEATURE DESCRIPTION
  ↓
feature vectors
  ↓
matching / classification / recognition
```

This is a major transition from pixel processing to compact representation.

---

# 19.1 Feature vs Descriptor vs Keypoint

These terms are often mixed together.

### Feature

A measurable property or structure.

Examples:

```text
edge strength
corner response
texture statistic
shape
colour distribution
```

### Keypoint

A detected image location considered distinctive or important.

Example:

```text
corner at (x,y)
```

### Descriptor

A numerical representation associated with a feature/keypoint.

Example:

```text
vector of local gradient statistics
```

The distinction can be summarized:

```text
keypoint
→ WHERE

feature
→ WHAT structure/property

descriptor
→ HOW that structure is numerically represented
```

The exact terminology varies across computer-vision literature.

---

# 19.2 What Makes a Good Feature?

A useful feature often aims for some combination of:

```text
distinctiveness
repeatability
localization
robustness
compactness
computational efficiency
```

A feature should ideally remain recognizable when the image undergoes expected changes.

For example:

```text
small illumination change
→ feature remains useful
```

or:

```text
moderate rotation
→ descriptor remains matchable
```

No classical feature is invariant to every possible transformation.

---

# 19.3 Feature Types

Features can be categorized by the image property they represent.

### Intensity features

```text
mean
variance
histogram
local contrast
```

### Edge features

```text
gradient
edge orientation
edge density
```

### Corner/keypoint features

```text
corner location
local patch structure
```

### Texture features

```text
local variation
co-occurrence statistics
frequency patterns
```

### Shape features

```text
area
perimeter
eccentricity
curvature
contour
```

### Colour features

```text
channel means
histograms
colour moments
```

---

# 19.4 Global vs Local Features

### Global feature

Describes the whole image or large region.

Example:

```text
global colour histogram
```

### Local feature

Describes a small neighbourhood.

Example:

```text
descriptor around a keypoint
```

Local features are powerful when:

```text
objects move
background changes
image contains multiple objects
partial visibility occurs
```

because they can represent small distinctive structures.

---

# 19.5 Why Local Features Matter

Suppose the same object appears:

```text
Image A
object at left

Image B
object at right
```

A global representation can change significantly.

A local descriptor around an object corner can remain similar.

This supports:

```text
matching
registration
object recognition
tracking
```

---

# 19.6 Feature Detection vs Feature Description

These are separate stages.

```text
DETECTION
→ find interesting locations

DESCRIPTION
→ encode the local appearance
```

For example:

```text
image
 ↓
detect keypoints
 ↓
300 keypoints
 ↓
descriptor for each
 ↓
300 feature vectors
```

This is the conceptual structure behind SIFT and ORB.

---

# 19.7 Feature Matching

Given descriptors:

\[
\mathbf d_i^A
\]

from image A and:

\[
\mathbf d_j^B
\]

from image B, compute a distance:

\[
d(\mathbf d_i^A,\mathbf d_j^B)
\]

and seek compatible pairs.

For normalized Euclidean descriptors:

\[
d_E(\mathbf a,\mathbf b)
=
\sqrt{
\sum_k(a_k-b_k)^2
}
\]

For binary descriptors, Hamming distance is usually more appropriate.

---

# 19.8 Worked Descriptor Distance

Suppose:

\[
\mathbf a=(1,2,3)
\]

\[
\mathbf b=(2,2,5)
\]

Then:

\[
d_E=
\sqrt{
(1-2)^2+
(2-2)^2+
(3-5)^2
}
\]

\[
=
\sqrt{1+0+4}
\]

\[
\boxed{\sqrt5\approx2.236}
\]

A smaller distance generally indicates greater similarity under this descriptor metric, assuming the descriptor is designed for Euclidean comparison.

---

# 19.9 Why Descriptor Distance Is Not Universal

Different descriptors use different structures.

Examples:

```text
SIFT
→ floating-point descriptor
→ often Euclidean/L2-type comparison

ORB
→ binary descriptor
→ Hamming distance
```

Therefore:

> The distance metric should match the descriptor representation.

---

# 19.10 Hamming Distance

For binary vectors:

\[
\mathbf a=101100
\]

\[
\mathbf b=100110
\]

Compare bit by bit:

```text
1 = same
0 = same
1 ≠ 0
1 = 1
0 ≠ 1
0 = 0
```

There are two differing positions.

Thus:

\[
\boxed{d_H=2}
\]

Hamming distance is the number of differing bits.

---

# 19.11 What Is Invariance?

A feature is **invariant** to a transformation when its representation remains sufficiently stable under that transformation.

Examples:

```text
rotation invariance
→ orientation changes, descriptor remains comparable

scale invariance
→ object size changes, descriptor remains comparable

illumination robustness
→ brightness changes, descriptor remains useful
```

In practice, invariance is approximate and parameter-dependent.

---

# 19.12 What Is Equivariance?

> **EXTENSION**

A representation is equivariant when a transformation of the input causes a predictable transformation of the output.

For example:

```text
translate image
→ keypoint locations translate correspondingly
```

This is different from invariance.

```text
INVARIANT
→ representation stays approximately the same

EQUIVARIANT
→ representation changes predictably
```

This distinction becomes increasingly important in modern deep learning.

---

# 19.13 Corners

A corner is a location where intensity changes significantly in more than one direction.

Compare:

### Flat region

```text
100 100 100
100 100 100
100 100 100
```

### Edge

```text
100 100 200
100 100 200
100 100 200
```

Strong change in one direction.

### Corner

```text
100 100 200
100 100 200
200 200 200
```

Changes in multiple directions.

Corners are useful because they are often more distinctive than points on a uniform edge.

---

# 19.14 Harris Corner Intuition

The Harris detector examines local intensity change under small shifts.

A common formulation uses the structure tensor / second-moment matrix:

\[
M=
\sum_{(x,y)\in W}
w(x,y)
\begin{bmatrix}
I_x^2 & I_xI_y\\
I_xI_y & I_y^2
\end{bmatrix}
\]

where:

- \(I_x,I_y\) are image gradients,
- \(w\) weights the local neighbourhood.

The eigenvalues:

\[
\lambda_1,\lambda_2
\]

describe intensity variation in two principal directions.

---

# 19.15 Harris Interpretation

### Flat region

\[
\lambda_1\approx0,\quad\lambda_2\approx0
\]

### Edge

One large, one small:

\[
\lambda_1\gg\lambda_2
\]

### Corner

Both large:

\[
\lambda_1\approx\lambda_2\gg0
\]

This is a beautiful example of how linear algebra becomes geometric image understanding.

---

# 19.16 Harris Response

A common Harris response is:

\[
R=
\det(M)-k[\operatorname{trace}(M)]^2
\]

where:

\[
\det(M)=\lambda_1\lambda_2
\]

and:

\[
\operatorname{trace}(M)=\lambda_1+\lambda_2
\]

The parameter \(k\) controls the response behaviour.

---

# 19.17 Worked Harris-Style Interpretation

Suppose:

\[
\lambda_1=100
\]

and:

\[
\lambda_2=80
\]

Then:

\[
\det(M)=8000
\]

\[
\operatorname{trace}(M)=180
\]

For:

\[
k=0.04
\]

\[
R=8000-0.04(180)^2
\]

\[
=8000-0.04(32400)
\]

\[
=8000-1296
\]

\[
\boxed{6704}
\]

A strong positive response is consistent with corner-like structure under the Harris formulation.

---

# 19.18 Why Corners Are Useful

A local corner is often:

```text
more distinctive
than
a point along a long uniform edge
```

because there is significant variation in multiple directions.

This makes corners useful for:

- image registration,
- panorama stitching,
- tracking,
- object recognition.

---

# 19.19 Blobs

A blob is a region-like structure that differs from its surroundings.

Examples:

```text
bright spot on dark background
dark spot on bright background
```

Blob detectors often use scale-space methods.

Conceptually:

```text
small scale
→ small structures

large scale
→ larger structures
```

This leads to multi-scale feature detection.

---

# 19.20 Scale Space

> **EXTENSION**

A Gaussian scale space can be written:

\[
L(x,y,\sigma)
=
G(x,y,\sigma)*I(x,y)
\]

where \(\sigma\) controls scale.

As:

\[
\sigma\uparrow
\]

fine structures are increasingly smoothed.

Features can then be detected across multiple scales.

This concept is central to SIFT.

---

# 19.21 Difference of Gaussians

SIFT uses a Difference-of-Gaussians (DoG) scale-space approximation.

\[
D(x,y,\sigma)
=
L(x,y,k\sigma)-L(x,y,\sigma)
\]

This approximates a scaled Laplacian-of-Gaussian response under appropriate conditions.

It is efficient for detecting scale-space extrema.

---

# 19.22 Feature Descriptor Goals

A descriptor should ideally encode enough local information to distinguish one feature from another while remaining compact enough for efficient matching.

Potential properties:

```text
distinctive
repeatable
robust
compact
matchable
```

This creates a tradeoff:

```text
more information
↔
larger computation/storage
```

---

# 19.23 Hand-Crafted vs Learned Features

### Hand-crafted

Designed by mathematical/algorithmic rules.

Examples:

```text
SIFT
SURF
HOG
ORB
```

### Learned

Learned from data.

Examples:

```text
CNN embeddings
deep local features
transformer embeddings
```

This chapter focuses on classical descriptors required by the course, while Part V returns to learned representations.

---

# 19.24 SIFT — Big Picture

**Scale-Invariant Feature Transform (SIFT)** is a classical feature-detection and description method designed for strong robustness to scale and rotation changes, with additional resilience to moderate illumination and viewpoint changes.

A simplified SIFT pipeline is:

```text
image
 ↓
scale-space construction
 ↓
Difference of Gaussians
 ↓
keypoint localization
 ↓
remove unstable/low-contrast points
 ↓
assign dominant orientation
 ↓
build local gradient descriptor
 ↓
descriptor vector
```

---

# 19.25 SIFT Scale-Space Construction

A Gaussian pyramid uses multiple scales:

\[
L(x,y,\sigma)
=
G(x,y,\sigma)*I(x,y)
\]

SIFT examines differences between nearby scales:

\[
D(x,y,\sigma)
=
L(x,y,k\sigma)-L(x,y,\sigma)
\]

This helps identify structures that persist around particular scales.

---

# 19.26 SIFT Keypoint Localization

Candidate extrema are detected by comparing a point with neighbours in:

```text
space
+
scale
```

Conceptually:

```text
3×3 spatial neighbours
+
previous scale
+
next scale
```

A candidate is retained if it is a local maximum/minimum under the DoG representation.

---

# 19.27 SIFT Keypoint Refinement

Not every candidate is useful.

Unstable points can be rejected because of:

```text
low contrast
+
edge-like instability
```

This improves descriptor repeatability.

The exact mathematical localization/refinement uses a local Taylor approximation in the original method.

---

# 19.28 SIFT Orientation Assignment

Around the keypoint, gradient magnitude and orientation are computed.

A common gradient representation is:

\[
m(x,y)
=
\sqrt{
[L(x+1,y)-L(x-1,y)]^2
+
[L(x,y+1)-L(x,y-1)]^2
}
\]

and:

\[
\theta(x,y)
=
\operatorname{atan2}
(
L(x,y+1)-L(x,y-1),
L(x+1,y)-L(x-1,y)
)
\]

The dominant local orientation is used to normalize the descriptor orientation.

---

# 19.29 Why Orientation Assignment Helps

Suppose:

```text
feature in Image A
→ rotated 30°
```

Without orientation normalization:

```text
descriptor changes strongly
```

With orientation normalization:

```text
local coordinate frame rotates with feature
→ descriptor remains more comparable
```

This is the core idea behind rotation robustness.

---

# 19.30 SIFT Descriptor Construction

A common SIFT descriptor uses:

```text
4 × 4 spatial cells
×
8 orientation bins
```

giving:

\[
4\times4\times8
=
\boxed{128}
\]

descriptor dimensions.

The descriptor is a floating-point vector.

---

# 19.31 What the 128 Dimensions Represent

They summarize local gradient orientation distributions.

Conceptually:

```text
keypoint neighbourhood
      ↓
4×4 cells
      ↓
8 orientation bins/cell
      ↓
histograms
      ↓
128 values
```

The vector is normalized to reduce sensitivity to some illumination changes.

---

# 19.32 SIFT Descriptor Normalization

A common pipeline includes vector normalization.

Let:

\[
\mathbf d
\]

be the descriptor.

A basic L2 normalization is:

\[
\mathbf d'=
\frac{\mathbf d}
{\|\mathbf d\|_2}
\]

where:

\[
\|\mathbf d\|_2
=
\sqrt{\sum_i d_i^2}
\]

Further clipping/renormalization is used in the classic SIFT construction.

---

# 19.33 Worked Normalization Example

Suppose:

\[
\mathbf d=(3,4)
\]

Then:

\[
\|\mathbf d\|_2
=
\sqrt{3^2+4^2}
=
5
\]

Normalized:

\[
\mathbf d'
=
(0.6,0.8)
\]

and:

\[
\|\mathbf d'\|_2=1
\]

---

# 19.34 SIFT Matching

Given two descriptors:

\[
d_A,\ d_B
\]

a common similarity measure is Euclidean distance:

\[
d=
\|d_A-d_B\|_2
\]

Nearest-neighbour matching selects the closest descriptor candidate.

But nearest distance alone can produce ambiguous matches.

---

# 19.35 Lowe-Style Ratio Test

A commonly used test compares:

```text
nearest distance
vs
second-nearest distance
```

Let:

\[
d_1=\text{best match distance}
\]

\[
d_2=\text{second-best distance}
\]

Accept when:

\[
\frac{d_1}{d_2}<r
\]

for a selected ratio \(r\).

A lower ratio indicates that the best match is substantially better than the next candidate.

---

# 19.36 Worked Ratio Example

Suppose:

\[
d_1=0.30
\]

\[
d_2=0.90
\]

Then:

\[
\frac{d_1}{d_2}
=
\frac{0.30}{0.90}
=
0.333
\]

If:

\[
r=0.75
\]

then:

\[
0.333<0.75
\]

so the match passes the ratio criterion.

---

# 19.37 Why Matching Still Needs Geometric Validation

Even a good descriptor match can be false.

If many matches are available, a geometric model can reject inconsistent pairs.

For example:

```text
feature matches
 ↓
estimate transformation
 ↓
remove outliers
 ↓
use inlier matches
```

RANSAC is commonly used for this purpose.

This bridges C19/C20 to C11 registration.

---

# 19.38 SURF — Big Picture

**Speeded-Up Robust Features (SURF)** is another classical local-feature method designed to provide robust keypoints/descriptors with efficient computation.

SURF uses approximations to scale-space operations and relies heavily on:

```text
integral images
+
box filters
+
Hessian-based responses
```

to speed computation.

---

# 19.39 SURF Detector Intuition

A Hessian matrix for an image can be written:

\[
H(x,y)=
\begin{bmatrix}
I_{xx}&I_{xy}\\
I_{xy}&I_{yy}
\end{bmatrix}
\]

Its determinant:

\[
\det(H)
=
I_{xx}I_{yy}-I_{xy}^2
\]

can identify blob-like structures.

SURF approximates second-order derivatives using box filters.

---

# 19.40 Integral Image

An integral image allows fast rectangular-sum computation.

For image \(I\):

\[
S(x,y)
=
\sum_{i\le x}
\sum_{j\le y}
I(i,j)
\]

A rectangle sum can then be obtained using a small number of array accesses.

Conceptually:

```text
large rectangular sum
→ four corner values
```

This is one reason SURF can evaluate box filters efficiently.

---

# 19.41 SURF Descriptor

SURF describes local neighbourhoods using Haar-wavelet-like responses.

A simplified structure is:

```text
keypoint
 ↓
orientation
 ↓
local square region
 ↓
4×4 subregions
 ↓
wavelet response statistics
 ↓
descriptor
```

The descriptor dimension depends on the variant/configuration.

This is one reason it is safer to describe SURF conceptually rather than assume one universal vector size.

---

# 19.42 SIFT vs SURF

| Property | SIFT | SURF |
|---|---|---|
| key idea | DoG scale space + gradients | Hessian + efficient approximations |
| scale handling | yes | yes |
| orientation | yes | yes |
| descriptor | gradient histograms | Haar-wavelet response statistics |
| computation | comparatively heavier | designed for faster computation |
| descriptor comparison | typically Euclidean | typically Euclidean |
| course role | major classical feature | comparative classical feature |

---

# 19.43 ORB — Big Picture

**Oriented FAST and Rotated BRIEF (ORB)** combines:

```text
FAST keypoint detection
+
orientation estimation
+
rotated BRIEF binary descriptor
```

It is designed to be computationally efficient.

---

# 19.44 FAST Detector

FAST identifies corners by examining pixels on a circle around a candidate.

A candidate is considered corner-like if a sufficient contiguous sequence of circle pixels is significantly brighter or darker than the centre according to the detector's threshold.

Conceptually:

```text
       o o o
    o         o
   o     P     o
    o         o
       o o o
```

The circular test is much cheaper than some more elaborate corner detectors.

---

# 19.45 ORB Orientation

ORB estimates an orientation for the FAST keypoint using local intensity moments.

Then the BRIEF sampling pattern is rotated according to that orientation.

This gives a degree of rotation robustness.

---

# 19.46 BRIEF Descriptor

BRIEF uses intensity comparisons between selected point pairs.

For two sampled intensities:

\[
I(p)
\]

and:

\[
I(q)
\]

define:

\[
\tau(p,q)=
\begin{cases}
1,&I(p)<I(q)\\
0,&I(p)\ge I(q)
\end{cases}
\]

Many such binary tests are concatenated:

```text
1 0 1 1 0 0 1 ...
```

The result is a binary descriptor.

---

# 19.47 Why ORB Is Fast

ORB benefits from:

```text
FAST detector
+
binary descriptor
+
Hamming distance
```

Binary descriptors are compact and can be matched efficiently using bit operations.

---

# 19.48 Worked Hamming Example

Descriptor A:

\[
10101100
\]

Descriptor B:

\[
10011110
\]

Compare:

```text
1 0 1 0 1 1 0 0
1 0 0 1 1 1 1 0
```

Differences occur at positions:

```text
3
4
7
```

Therefore:

\[
\boxed{d_H=3}
\]

---

# 19.49 SIFT vs ORB

| Property | SIFT | ORB |
|---|---|---|
| descriptor type | floating-point | binary |
| typical distance | L2 | Hamming |
| scale robustness | strong | more limited depending on implementation |
| rotation handling | yes | yes |
| speed | generally slower | generally faster |
| memory | larger | compact |
| practical use | robust matching | efficient real-time matching |

The comparison is qualitative; actual speed depends on implementation and hardware.

---

# 19.50 HOG — Histogram of Oriented Gradients

**Histogram of Oriented Gradients (HOG)** describes object appearance through local gradient orientation distributions.

Unlike SIFT/ORB, which are typically keypoint-centric, HOG is commonly built over a dense grid of cells.

Conceptual pipeline:

```text
image
 ↓
gradient
 ↓
orientation + magnitude
 ↓
cells
 ↓
orientation histograms
 ↓
blocks
 ↓
normalization
 ↓
feature vector
```

---

# 19.51 HOG Cell

A cell contains a small image region.

For each pixel:

\[
G_x,\quad G_y
\]

are computed.

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

Then votes are accumulated into orientation bins.

---

# 19.52 HOG Orientation Histogram

Suppose a cell uses 9 bins.

Each pixel contributes:

```text
orientation bin
+
weighted magnitude
```

A conceptual histogram:

```text
frequency
   ↑
   │       █
   │   █   ███
   │ ███   █
   └────────────→ orientation
```

This describes the local distribution of edge directions.

---

# 19.53 Why HOG Works for Shape

Object silhouettes and local contours create characteristic gradient orientations.

Therefore:

```text
gradient orientation
→ local shape cue
→ HOG descriptor
```

HOG became particularly influential in classical object detection.

---

# 19.54 HOG Block Normalization

Local histograms are grouped into blocks and normalized to reduce sensitivity to illumination/contrast changes.

For descriptor vector \(v\):

### L2 normalization

\[
v'=
\frac{v}
{\sqrt{\|v\|_2^2+\epsilon^2}}
\]

where \(\epsilon\) avoids division by zero.

Other normalization variants exist.

---

# 19.55 Worked HOG Normalization

Suppose:

\[
v=(3,4)
\]

Then:

\[
\|v\|_2=5
\]

with small \(\epsilon\) ignored for illustration:

\[
v'=(0.6,0.8)
\]

Again:

\[
\|v'\|_2=1
\]

---

# 19.56 HOG vs SIFT

| Property | HOG | SIFT |
|---|---|---|
| sampling | commonly dense grid | keypoint-centred |
| main signal | gradient orientations | local gradient structure |
| scale handling | depends on window/design | explicit scale-space |
| rotation handling | limited unless designed for it | explicit orientation assignment |
| typical role | shape/object appearance | local matching/recognition |
| descriptor | grid/cell/block histogram | local 128-D-style gradient descriptor |

---

# 19.57 HOG vs ORB

| Property | HOG | ORB |
|---|---|---|
| feature style | dense region descriptor | local keypoint descriptor |
| values | real-valued | binary |
| typical distance | Euclidean | Hamming |
| strength | contour/shape appearance | fast local matching |
| scale invariance | not inherent | limited compared with SIFT |
| speed | practical | highly efficient for matching |

---

# 19.58 Descriptor Comparison Overview

| Method | Detector | Descriptor | Main strength | Typical distance |
|---|---|---|---|---|
| SIFT | scale-space DoG | gradient histogram | robust local matching | L2 |
| SURF | Hessian-based | wavelet responses | efficient robust features | L2 |
| ORB | FAST | rotated BRIEF | fast binary matching | Hamming |
| HOG | dense gradient grid | orientation histograms | shape/appearance | L2-like |

---

# 19.59 Choosing a Feature Method

```text
Need robust local matching across scale/rotation?
→ SIFT

Need efficient classical Hessian-style features?
→ SURF

Need fast binary local matching?
→ ORB

Need dense shape/gradient representation?
→ HOG
```

This is a practical starting point, not a universal benchmark.

---

# 19.60 Matching Pipeline

A classical local-feature matching system:

```text
image A
  ↓
detect
  ↓
describe
  ↓
descriptors A

image B
  ↓
detect
  ↓
describe
  ↓
descriptors B

A ↔ B matching
  ↓
ratio/filter test
  ↓
geometric verification
  ↓
inliers
```

This is directly useful for registration and image alignment.

---

# 19.61 RANSAC for Geometric Verification

> **EXTENSION**

Suppose feature matches suggest a transformation:

\[
\mathbf p'_i\approx H\mathbf p_i
\]

Some matches may be wrong.

RANSAC repeatedly:

```text
select minimal sample
→ estimate model
→ count inliers
→ repeat
→ choose strong consensus model
```

The result separates:

```text
geometrically consistent matches
```

from:

```text
outliers
```

---

# 19.62 Reprojection Error

Given an estimated transformation \(T\), a correspondence:

\[
p_i\rightarrow p_i'
\]

has reprojection error:

\[
e_i=
\|p_i'-T(p_i)\|
\]

Small:

\[
e_i
\]

suggests consistency with the model.

This is a useful bridge between feature matching and geometric registration.

---

# 19.63 Worked Reprojection Error

Suppose predicted point:

\[
\hat p=(102,49)
\]

and measured point:

\[
p'=(100,50)
\]

Then:

\[
e=
\sqrt{(100-102)^2+(50-49)^2}
\]

\[
=
\sqrt{4+1}
\]

\[
\boxed{\sqrt5\approx2.236}
\]

---

# 19.64 Feature Density

Not every image produces the same number of useful features.

Examples:

```text
textured scene
→ many keypoints

blank wall
→ few keypoints

motion blur
→ unstable features
```

Feature count alone is therefore not enough.

Quality and repeatability matter.

---

# 19.65 Repeated Patterns

A repeated texture can create many similar local features.

This creates ambiguity:

```text
many candidates
→ similar descriptor distances
→ uncertain matching
```

This is where ratio testing and geometric verification become important.

---

# 19.66 Illumination Effects

Feature detectors/descriptors can be affected by:

- shadows,
- saturation,
- strong exposure changes,
- colour shifts.

Descriptor normalization improves some robustness, but not unlimited.

The correct question is:

> Is the expected image variation within the feature method's robustness regime?

---

# 19.67 Blur Effects

Motion blur can:

```text
remove keypoint detail
→ reduce detection
→ alter descriptors
```

This links C14 restoration concepts to feature extraction.

Restoring blur can sometimes help, but restoration artifacts can also damage features.

---

# 19.68 Feature Extraction from Segmented Regions

Segmentation can provide an ROI:

```text
image
 ↓
segment object
 ↓
crop/mask ROI
 ↓
extract features
```

This can reduce background interference.

Conversely, local features can help initialize or guide segmentation.

The relationship can be bidirectional.

---

# 19.69 Shape Features from Masks

A segmented region can provide classical features:

\[
A=\text{area}
\]

\[
P=\text{perimeter}
\]

\[
AR=\frac{\text{width}}{\text{height}}
\]

and moments.

These are simpler than SIFT/ORB but highly useful when object geometry is known.

---

# 19.70 Moments

For a binary region, raw moments can be:

\[
m_{pq}
=
\sum_x\sum_y
x^py^qI(x,y)
\]

The zeroth moment:

\[
m_{00}
\]

corresponds to area for a binary region.

Centroid:

\[
\bar x=\frac{m_{10}}{m_{00}}
\]

\[
\bar y=\frac{m_{01}}{m_{00}}
\]

These connect segmentation directly to feature extraction.

---

# 19.71 Worked Moment Example

Suppose foreground pixels are:

\[
(1,1),(2,1),(1,2),(2,2)
\]

Then:

\[
m_{00}=4
\]

\[
m_{10}=1+2+1+2=6
\]

\[
m_{01}=1+1+2+2=6
\]

So:

\[
\bar x=\frac64=1.5
\]

\[
\bar y=\frac64=1.5
\]

This matches the centroid derived in C15.

---

# 19.72 Shape vs Local Descriptor

| Feature family | Example | Main information |
|---|---|---|
| region statistics | area, centroid | global object geometry |
| contour | perimeter, curvature | boundary shape |
| corner | Harris | local distinctive structure |
| local descriptor | SIFT/ORB | local appearance |
| dense descriptor | HOG | local/global shape pattern |
| texture | local statistics | surface structure |

A good system may combine several.

---

# 19.73 Feature Normalization

Features can have different numeric scales.

Example:

```text
area
→ thousands

aspect ratio
→ around 1

colour mean
→ 0–255
```

A machine-learning model may be dominated by large-scale features unless normalization is applied.

Possible transformations include:

\[
z=
\frac{x-\mu}{\sigma}
\]

or min-max scaling:

\[
x'=
\frac{x-x_{\min}}
{x_{\max}-x_{\min}}
\]

depending on the downstream model.

---

# 19.74 Feature Selection

Not every feature is useful.

A large feature vector can introduce:

```text
redundancy
noise
computation
overfitting risk
```

Feature selection asks:

> Which measured properties contribute useful information?

This is a bridge to classical machine learning.

---

# 19.75 Dimensionality Reduction

> **EXTENSION**

Techniques such as PCA can reduce feature dimensionality.

Given feature vectors collected into matrix:

\[
X
\]

PCA finds directions of large variance.

Conceptually:

```text
many dimensions
→ principal components
→ fewer dimensions
```

The goal is often compact representation while retaining important variation.

---

# 19.76 Feature Engineering Pipeline

A classical vision system can be:

```text
image
 ↓
preprocessing
 ↓
segmentation / ROI
 ↓
feature detection
 ↓
feature description
 ↓
feature selection
 ↓
classifier / matcher
```

This is the predecessor architecture to modern learned pipelines.

---

# 19.77 Classical Features vs CNN Features

### Classical

```text
human-designed detector
+
human-designed descriptor
```

### CNN

```text
learned filters
+
learned intermediate representations
```

The CNN may learn features directly from data.

However, classical descriptors remain valuable because they are:

- interpretable,
- useful with limited data,
- often efficient,
- strong for matching tasks.

---

# 19.78 Feature Matching and Classification

Descriptors can be used in two broad ways.

### Matching

```text
descriptor A
↔
descriptor B
```

### Classification

```text
many feature vectors
→ classifier
→ class
```

HOG historically became strongly associated with classification pipelines such as linear classifiers for object detection.

SIFT/ORB are more naturally associated with matching and local correspondence.

---

# 19.79 Evaluation of Feature Detectors

Useful metrics include:

### Repeatability

Does the same physical point get detected again after transformation?

### Localization accuracy

How precisely is the feature located?

### Matching accuracy

How many correct correspondences are obtained?

### Robustness

How does performance change under:

```text
rotation
scale
blur
illumination
viewpoint
noise
```

---

# 19.80 Feature Matching Evaluation

Suppose:

```text
100 candidate matches
70 correct
30 incorrect
```

Then:

\[
Precision=
\frac{70}{100}=0.70
\]

If 80 correct correspondences actually exist in the images:

\[
Recall=
\frac{70}{80}=0.875
\]

So:

\[
\boxed{Precision=70\%,\ Recall=87.5\%}
\]

---

# 19.81 Descriptor Distance Distributions

A useful diagnostic is to inspect:

```text
correct-match distances
incorrect-match distances
```

A good descriptor should ideally produce:

```text
correct
→ low distances

incorrect
→ higher distances
```

If distributions overlap heavily, matching becomes difficult.

---

# 19.82 Practical Experiment — SIFT vs ORB

Use two images with:

```text
translation
rotation
scale change
```

Run:

```text
SIFT
ORB
```

Record:

```text
keypoint count
descriptor count
matching time
candidate matches
filtered matches
geometric inliers
```

This turns a comparison into measurable evidence.

---

# 19.83 Practical Experiment — HOG

Use two categories with visible shape differences.

Pipeline:

```text
image
 ↓
resize/normalize
 ↓
gradient
 ↓
HOG
 ↓
feature vector
 ↓
classifier
 ↓
accuracy
```

Vary:

```text
cell size
block size
orientation bins
```

and observe performance.

---

# 19.84 Common Traps

## Trap 1 — “Feature and descriptor are the same.”

Not necessarily.

Detection and description are related but distinct stages.

## Trap 2 — “More features always means better vision.”

False.

Many unstable or repetitive features can make matching worse.

## Trap 3 — “SIFT is a classifier.”

False.

SIFT primarily detects and describes local image structure.

## Trap 4 — “HOG detects objects by itself.”

False.

HOG provides a descriptor; a detector/classifier can be built on top of it.

## Trap 5 — “ORB and SIFT use the same distance metric.”

False.

ORB is binary and commonly uses Hamming distance; SIFT is floating-point and commonly uses Euclidean/L2 distance.

## Trap 6 — “A nearest descriptor match is always correct.”

False.

Ambiguity and repetitive patterns create false matches.

## Trap 7 — “Feature matching alone proves images are aligned.”

False.

Geometric verification is often required.

## Trap 8 — “Scale invariance means any scale change works perfectly.”

False.

Robustness is approximate and parameter-dependent.

## Trap 9 — “HOG is naturally rotation invariant.”

False.

Its orientation histogram is not equivalent to the explicit orientation normalization used by SIFT.

## Trap 10 — “Classical features are obsolete.”

False.

They remain valuable for matching, registration, low-data settings and interpretable engineered systems.

---

# 19.85 Exam Formula Sheet

### Euclidean descriptor distance

\[
\boxed{
d_E(\mathbf a,\mathbf b)
=
\sqrt{\sum_i(a_i-b_i)^2}
}
\]

### Hamming distance

\[
\boxed{
d_H=
\text{number of differing bits}
}
\]

### Harris matrix

\[
\boxed{
M=
\sum_W
w
\begin{bmatrix}
I_x^2&I_xI_y\\
I_xI_y&I_y^2
\end{bmatrix}
}
\]

### Harris response

\[
\boxed{
R=\det(M)-k[\operatorname{trace}(M)]^2
}
\]

### Scale-space Gaussian

\[
\boxed{
L(x,y,\sigma)=G(x,y,\sigma)*I(x,y)
}
\]

### Difference of Gaussians

\[
\boxed{
D(x,y,\sigma)
=
L(x,y,k\sigma)-L(x,y,\sigma)
}
\]

### Descriptor normalization

\[
\boxed{
\mathbf d'=
\frac{\mathbf d}
{\|\mathbf d\|_2}
}
\]

### Ratio test

\[
\boxed{
\frac{d_1}{d_2}<r
}
\]

### Reprojection error

\[
\boxed{
e_i=\|p_i'-T(p_i)\|
}
\]

### Region moments

\[
\boxed{
m_{pq}
=
\sum_x\sum_yx^py^qI(x,y)
}
\]

---

# 19.86 Exam-Style Problem — Descriptor Distance

Given:

\[
a=(2,4,6)
\]

\[
b=(1,4,3)
\]

Calculate Euclidean distance.

\[
d=
\sqrt{
(2-1)^2+
(4-4)^2+
(6-3)^2
}
\]

\[
=
\sqrt{1+0+9}
\]

\[
\boxed{\sqrt{10}\approx3.162}
\]

---

# 19.87 Exam-Style Problem — Harris Interpretation

Suppose a point has:

\[
\lambda_1=0,\quad\lambda_2=0
\]

Interpret it.

Answer:

```text
little intensity change in either direction
→ flat-region behaviour
→ weak corner response
```

Suppose:

\[
\lambda_1\gg0,\quad\lambda_2\approx0
\]

Then:

```text
strong change in one direction
→ edge-like
```

Suppose both are large:

```text
strong change in both directions
→ corner-like
```

---

# 19.88 Exam-Style Problem — SIFT Dimension

A simplified SIFT descriptor uses:

```text
4 × 4 spatial cells
8 orientation bins per cell
```

Dimension:

\[
4\times4\times8
\]

\[
\boxed{128}
\]

---

# 19.89 Exam-Style Problem — ORB Matching

Two 8-bit descriptors:

\[
A=10110100
\]

\[
B=11100110
\]

Differences:

```text
position 2
position 5
position 7
```

Therefore:

\[
\boxed{d_H=3}
\]

---

# 19.90 Exam-Style Problem — Ratio Test

Given:

\[
d_1=20
\]

\[
d_2=50
\]

and:

\[
r=0.5
\]

Then:

\[
\frac{20}{50}=0.4
\]

Since:

\[
0.4<0.5
\]

the match passes the ratio test.

---

# 19.91 Engineering Insight — Features Are a Compression of Meaning

A useful way to think about feature extraction is:

```text
millions of pixel values
        ↓
task-relevant structure
        ↓
hundreds/thousands of features
```

Good features preserve what the next task needs.

Bad features can discard exactly the information required for recognition.

Therefore feature engineering is another form of **representation design**.

---

# 19.92 Cross-Book Bridges

> **C10 BRIDGE**  
> Gradients and edge orientation provide the mathematical foundation for HOG and local descriptors.

> **C15–C18 BRIDGE**  
> Segmentation and morphology can define regions of interest before feature extraction.

> **C20 BRIDGE**  
> SIFT, SURF, ORB and HOG specialize the general feature/descriptor framework.

> **C11 BRIDGE**  
> Geometric verification and registration use matched features to estimate image transformations.

> **C25 BRIDGE**  
> Feature vectors can feed classical classifiers.

> **C28 BRIDGE**  
> Modern object detection replaces much hand-crafted feature engineering with learned representations.

> **C30 BRIDGE**  
> Feature points can be tracked through video for motion estimation.

> **LAB BRIDGE**  
> Detect features, compute descriptors, match images and evaluate geometric inliers.

> **PRACTICE BRIDGE**  
> Calculate descriptor distances, Harris statistics, HOG normalization, ratio tests and reprojection error.

> **EXAM BRIDGE**  
> Know feature/keypoint/descriptor distinctions, corner/gradient concepts, SIFT/SURF/ORB/HOG pipelines and matching principles.

---

# 19.93 Quick Recall

```text
FEATURE
→ measurable image property

KEYPOINT
→ distinctive location

DESCRIPTOR
→ numerical representation

SIFT
→ DoG + orientation + gradient descriptor

SURF
→ Hessian + integral-image efficiency

ORB
→ FAST + rotated BRIEF

HOG
→ gradient-orientation histograms

MATCHING
→ descriptor distance

VERIFICATION
→ geometric consistency
```

Core rule:

> **A feature detector finds where to look; a descriptor encodes what was found.**

---

# 19.94 Chapter Checkpoint

1. Define a feature.
2. Define a keypoint.
3. Define a descriptor.
4. Explain the difference between detection and description.
5. What makes a feature useful?
6. Compare global and local features.
7. Define invariance and equivariance.
8. Explain why corners are useful.
9. Describe Harris corner intuition using eigenvalues.
10. Define scale space.
11. Explain the Difference-of-Gaussians idea.
12. Outline the SIFT pipeline.
13. Why is SIFT commonly described as rotation/scale robust?
14. Why does the classic SIFT descriptor have 128 dimensions?
15. Explain SURF's Hessian/integral-image idea.
16. Describe ORB's FAST + BRIEF construction.
17. Why is Hamming distance appropriate for ORB?
18. Explain HOG's cell/block histogram structure.
19. Compare SIFT, SURF, ORB and HOG.
20. Why is geometric verification necessary after feature matching?

---

# 19.95 Connection Forward

This chapter created the general feature language.

Chapter 20 now turns that language into the four syllabus-named feature methods:

```text
SIFT
SURF
ORB
HOG
```

The next chapter will focus more tightly on:

```text
algorithm pipelines
+
descriptor construction
+
matching
+
parameter tradeoffs
+
practical implementation
+
comparison
```

This makes C20 the **classical feature-methods laboratory chapter**, while C19 remains the conceptual feature foundation.
