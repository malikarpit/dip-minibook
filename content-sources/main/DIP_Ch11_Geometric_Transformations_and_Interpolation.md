---
id: "C11"
title: "Geometric Transformations and Interpolation"
layer: "MAIN"
part: "II — Improving the Image"
unit: "II"
version: "1.0"
status: "REFERENCE BUILD"
syllabus_scope:
  - "Geometric transformations"
  - "Spatial coordinate transformations"
  - "Interpolation"
tags:
  - "CORE"
  - "EXAM"
  - "MATH"
  - "DEEP DIVE"
  - "LAB"
  - "GEOMETRY"
  - "RESAMPLING"
prerequisites:
  - "C03"
  - "C04"
  - "C08"
related:
  - "C06"
  - "C12"
  - "C15"
  - "C19"
  - "C30"
math:
  - "M06"
  - "M07"
  - "M08"
lab:
  - "LAB-U2-05"
  - "LAB-U4-05"
exam:
  - "EXAM-U2"
practice:
  - "P-C11"
assets:
  - "D-C11-01"
  - "D-C11-02"
  - "D-C11-03"
---

# Chapter 11 — Geometric Transformations and Interpolation

> **Chapter thesis**  
> A geometric transformation changes where image samples are located in the image plane. The transformation is defined mathematically in coordinates, but a transformed grid usually asks for values at locations that did not exist in the original image. **Interpolation is therefore part of the resampling problem, not an optional visual afterthought.**

**Part II — Improving the Image**

> **Scope note:** The university Unit II scope centers on image enhancement/filtering; this chapter is included in the MiniBook architecture as a necessary engineering bridge between spatial processing and later frequency-domain/resampling work. fileciteturn4file0L36-L40

---

# 11.0 Why Geometry Appears in DIP

So far, most operations changed values while largely preserving the existing spatial grid.

Examples:

```text
C06
pixel value → new pixel value

C07
intensity distribution → new intensity mapping

C08–C10
local neighbourhood → new response
```

Geometric transformations ask a different question:

> **Where should each image sample appear?**

Conceptually:

```text
ORIGINAL IMAGE
      ↓
coordinate transformation
      ↓
NEW IMAGE GRID
      ↓
interpolation / resampling
      ↓
TRANSFORMED IMAGE
```

This is used in:

- resizing,
- rotation,
- translation,
- correction of geometric distortion,
- image registration,
- alignment,
- perspective transformation,
- mosaicing,
- vision pipelines.

---

# 11.1 Coordinate Transformation

Let an input point be:

\[
\mathbf{p}
=
\begin{bmatrix}
x\\y
\end{bmatrix}
\]

A geometric transformation produces:

\[
\mathbf{p}'
=
T(\mathbf{p})
\]

or:

\[
\begin{bmatrix}
x'\\y'
\end{bmatrix}
=
T
\left(
\begin{bmatrix}
x\\y
\end{bmatrix}
\right)
\]

The transformation acts on coordinates.

The image values then have to be sampled at the appropriate positions.

---

# 11.2 Translation

A translation shifts an image without changing its shape.

\[
x'=x+t_x
\]

\[
y'=y+t_y
\]

where:

- \(t_x\) = horizontal shift,
- \(t_y\) = vertical shift.

Matrix form:

\[
\begin{bmatrix}
x'\\y'
\end{bmatrix}
=
\begin{bmatrix}
x\\y
\end{bmatrix}
+
\begin{bmatrix}
t_x\\t_y
\end{bmatrix}
\]

---

# 11.3 Worked Translation Example

Suppose:

\[
(x,y)=(40,25)
\]

and:

\[
t_x=10,\qquad t_y=-5
\]

Then:

\[
x'=40+10=50
\]

\[
y'=25-5=20
\]

So:

\[
\boxed{(40,25)\rightarrow(50,20)}
\]

The point moves right and upward under the stated coordinate convention.

---

# 11.4 Why Translation Creates Empty Pixels

Suppose a square image is shifted right.

```text
ORIGINAL

████████
████████
████████

TRANSLATED

   ██████
   ██████
   ██████
```

New locations exist where no original sample was previously present.

The output must decide what values to use in those locations.

Possible approaches include:

- constant background,
- zero,
- replication,
- interpolation only where source data exist.

---

# 11.5 Rotation

For a 2-D rotation about the origin:

\[
x'=x\cos\theta-y\sin\theta
\]

\[
y'=x\sin\theta+y\cos\theta
\]

Matrix form:

\[
\begin{bmatrix}
x'\\y'
\end{bmatrix}
=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}
\begin{bmatrix}
x\\y
\end{bmatrix}
\]

This is one of the most important transformation matrices in image geometry.

---

# 11.6 Worked Rotation Example

Take:

\[
(x,y)=(1,0)
\]

and:

\[
\theta=90^\circ
\]

Since:

\[
\cos90^\circ=0
\]

\[
\sin90^\circ=1
\]

we get:

\[
x'=1(0)-0(1)=0
\]

\[
y'=1(1)+0(0)=1
\]

Therefore:

\[
\boxed{(1,0)\rightarrow(0,1)}
\]

under the standard Cartesian rotation convention.

---

# 11.7 Rotation About the Image Centre

Real image rotation is usually intended around a centre, not the coordinate origin.

A conceptual pipeline is:

```text
translate centre to origin
        ↓
rotate
        ↓
translate back
```

Mathematically:

\[
\mathbf{p}'=
T(\mathbf{c})
R(\theta)
T(-\mathbf{c})
\mathbf{p}
\]

where \(T\) denotes translation and \(R\) denotes rotation.

The multiplication order is important.

---

# 11.8 Why Order Matters

Consider:

```text
translate → rotate
```

versus:

```text
rotate → translate
```

They generally produce different results.

Geometric transformations are not generally commutative:

\[
AB\ne BA
\]

This is an important engineering and exam concept.

---

# 11.9 Scaling

Scaling changes spatial dimensions.

\[
x'=s_xx
\]

\[
y'=s_yy
\]

where:

- \(s_x\) = horizontal scale,
- \(s_y\) = vertical scale.

If:

\[
s_x=s_y
\]

the scaling is isotropic/uniform.

If:

\[
s_x\ne s_y
\]

the image is stretched differently in the two directions.

---

# 11.10 Worked Scaling Example

Suppose:

\[
(x,y)=(20,30)
\]

and:

\[
s_x=2,\qquad s_y=0.5
\]

Then:

\[
x'=2(20)=40
\]

\[
y'=0.5(30)=15
\]

Therefore:

\[
\boxed{(20,30)\rightarrow(40,15)}
\]

The object is stretched horizontally and compressed vertically.

---

# 11.11 Reflection

Reflection reverses one coordinate.

Horizontal-axis-style reflection:

\[
x'=x,\qquad y'=-y
\]

Vertical-axis-style reflection:

\[
x'=-x,\qquad y'=y
\]

The exact visual effect depends on the coordinate convention.

Because image arrays frequently use downward-increasing row indices, direct matrix indexing and Cartesian diagrams must not be mixed carelessly.

---

# 11.12 Shearing

Horizontal shear:

\[
x'=x+sy
\]

\[
y'=y
\]

Vertical shear:

\[
x'=x
\]

\[
y'=y+sx
\]

Shearing changes angles and shape while preserving one axis direction in the basic transformation.

---

# 11.13 Affine Transformation

A general affine transformation can combine:

- translation,
- rotation,
- scaling,
- reflection,
- shear.

One common form:

\[
x'=a_{11}x+a_{12}y+t_x
\]

\[
y'=a_{21}x+a_{22}y+t_y
\]

or in homogeneous coordinates:

\[
\begin{bmatrix}
x'\\
y'\\
1
\end{bmatrix}
=
\begin{bmatrix}
a_{11}&a_{12}&t_x\\
a_{21}&a_{22}&t_y\\
0&0&1
\end{bmatrix}
\begin{bmatrix}
x\\
y\\
1
\end{bmatrix}
\]

---

# 11.14 Why Homogeneous Coordinates Matter

Homogeneous coordinates allow:

```text
linear transformation
+
translation
```

to be represented in one matrix multiplication.

This is especially useful when composing multiple transformations.

For example:

```text
rotation
+
scale
+
translation
```

can be combined into one transformation matrix.

---

# 11.15 Matrix Composition

Suppose:

\[
\mathbf{p}_1=A\mathbf{p}
\]

and:

\[
\mathbf{p}_2=B\mathbf{p}_1
\]

Then:

\[
\mathbf{p}_2=BA\mathbf{p}
\]

Therefore:

```text
first A
then B

→
combined matrix BA
```

Read matrix multiplication from right to left when interpreting sequential transformations.

---

# 11.16 Worked Composition Example

Suppose:

\[
A=
\begin{bmatrix}
2&0\\
0&2
\end{bmatrix}
\]

is scaling by 2, and:

\[
B=
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}
\]

is a 90° rotation.

Then:

\[
BA
=
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}
\begin{bmatrix}
2&0\\
0&2
\end{bmatrix}
\]

\[
=
\begin{bmatrix}
0&-2\\
2&0
\end{bmatrix}
\]

So the combined operation is:

```text
scale by 2
→ rotate 90°
```

---

# 11.17 Inverse Mapping

A major implementation issue is deciding whether to map:

```text
source → destination
```

or:

```text
destination → source
```

The second approach is called **inverse mapping**.

For each output coordinate:

\[
(x',y')
\]

find where it came from:

\[
(x,y)=T^{-1}(x',y')
\]

Then sample the source image at \((x,y)\).

---

# 11.18 Why Inverse Mapping Is Usually Convenient

Forward mapping can produce:

```text
holes
overlaps
uneven coverage
```

because source pixels may map between output grid locations.

Inverse mapping instead asks:

```text
for every output pixel:
    where should I sample the source?
```

This naturally fills the output grid.

---

# 11.19 Forward vs Inverse

| Method | Core question | Common issue |
|---|---|---|
| forward mapping | where does this source point go? | holes/overlaps |
| inverse mapping | where did this output point come from? | requires inverse transform |

For many practical image-warp implementations, inverse mapping with interpolation is the standard conceptual pattern.

---

# 11.20 Why Interpolation Is Needed

Suppose inverse mapping asks for:

\[
f(12.4, 7.8)
\]

But the source image only contains samples at integer grid positions:

```text
(12,7)
(12,8)
(13,7)
(13,8)
```

There is no direct stored pixel at:

\[
(12.4,7.8)
\]

Therefore a resampling rule estimates the value.

This is interpolation.

---

# 11.21 Nearest-Neighbour Interpolation

Nearest-neighbour selects the closest source sample.

For:

\[
(x,y)=(12.4,7.8)
\]

the nearest integer location is approximately:

\[
(12,8)
\]

So:

\[
f(12.4,7.8)\approx f(12,8)
\]

### Strength

- very simple,
- fast,
- preserves discrete labels.

### Weakness

- blockiness,
- jagged edges,
- stair-step artifacts for natural images.

---

# 11.22 Bilinear Interpolation

Bilinear interpolation uses the four nearest neighbours:

```text
Q11 ───── Q21
│          │
│  P(x,y)  │
│          │
Q12 ───── Q22
```

Let the local fractional coordinates be:

\[
\alpha=x-x_0
\]

\[
\beta=y-y_0
\]

Then:

\[
f(x,y)
=
(1-\alpha)(1-\beta)Q_{11}
+
\alpha(1-\beta)Q_{21}
+
(1-\alpha)\beta Q_{12}
+
\alpha\beta Q_{22}
\]

This is a weighted average.

---

# 11.23 Worked Bilinear Example

Suppose the four neighbouring values are:

\[
Q_{11}=10,\quad
Q_{21}=20,\quad
Q_{12}=30,\quad
Q_{22}=40
\]

and:

\[
\alpha=0.25,\qquad\beta=0.5
\]

Then:

\[
f=
(0.75)(0.5)(10)
+
(0.25)(0.5)(20)
+
(0.75)(0.5)(30)
+
(0.25)(0.5)(40)
\]

\[
=3.75+2.5+11.25+5
\]

\[
\boxed{22.5}
\]

Depending on the destination representation, this may remain floating-point or be rounded.

---

# 11.24 Why Bilinear Is Smoother

Nearest-neighbour chooses one sample.

Bilinear uses four:

```text
one sample
vs
weighted local neighbourhood
```

Therefore bilinear generally reduces blockiness.

But interpolation cannot reconstruct details that were never sampled.

It creates a smooth estimate from available samples.

---

# 11.25 Bicubic Interpolation

> **EXTENSION**

Bicubic interpolation uses a larger neighbourhood, commonly based on 16 surrounding samples.

It can produce smoother results than bilinear for many natural-image resizing tasks, but it is more computationally expensive and can introduce ringing/overshoot depending on the kernel.

The exact mathematical kernel varies by implementation.

---

# 11.26 Interpolation Is Not Reconstruction from Nothing

A common misunderstanding is:

> “Bicubic creates new detail.”

Not in the information-theoretic sense.

Interpolation estimates values between known samples.

It cannot recover spatial information that was never captured.

This distinction connects back to C03:

```text
sampling loss
→ interpolation cannot fully undo it
```

---

# 11.27 Downsampling vs Upsampling

### Upsampling

```text
fewer samples
→ more output grid points
```

Interpolation is required to estimate many new samples.

### Downsampling

```text
many samples
→ fewer output samples
```

Anti-alias filtering may be required before decimation to prevent aliasing.

Therefore:

```text
UP
→ interpolation

DOWN
→ filtering + resampling
```

as a useful conceptual rule.

---

# 11.28 Resize Pipeline

A robust resize workflow:

### Upscaling

```text
source image
→ choose target grid
→ inverse map
→ interpolate
→ output
```

### Downscaling

```text
source image
→ low-pass / anti-alias filtering
→ inverse map / resampling
→ output
```

The actual library implementation can combine these operations internally.

---

# 11.29 Rotation and Interpolation

A rotated image usually requires interpolation because the rotated output coordinates do not align exactly with the original integer grid.

Conceptually:

```text
source grid
████████
████████
████████

rotate

output grid
╲██████╱
 ╲████╱
```

The values at the new positions must be estimated.

---

# 11.30 Geometric Distortion

Not every transformation is a simple rotation or scaling.

Lens and camera geometry can produce nonlinear distortions such as:

- barrel distortion,
- pincushion distortion.

A correction workflow can be:

```text
distorted image
      ↓
camera/distortion model
      ↓
inverse warp
      ↓
interpolation
      ↓
corrected image
```

> **Extension:** Real distortion correction often uses calibration data rather than an arbitrary visual warp.

---

# 11.31 Image Registration

Image registration aligns two or more images.

Example:

```text
image A
   +
image B
   ↓
find transformation
   ↓
warp one image
   ↓
aligned images
```

Applications include:

- medical imaging,
- satellite imagery,
- panorama creation,
- change detection,
- multi-sensor fusion.

Registration is a major bridge from geometric processing to higher-level image analysis.

---

# 11.32 Feature-Based Registration

A more advanced workflow is:

```text
image A
→ detect features

image B
→ detect features

match corresponding features
        ↓
estimate transformation
        ↓
warp image
        ↓
evaluate alignment
```

SIFT, ORB and related descriptors later in the MiniBook provide tools that can support this process.

---

# 11.33 Perspective Transformation

When a planar object is viewed from different viewpoints, an affine model may be insufficient.

A projective/perspective transformation can be represented using a homography:

\[
\lambda
\begin{bmatrix}
x'\\y'\\1
\end{bmatrix}
=
H
\begin{bmatrix}
x\\y\\1
\end{bmatrix}
\]

where \(H\) is a \(3\times3\) matrix and \(\lambda\) is a scale factor.

This is useful for:

- document rectification,
- planar scene alignment,
- perspective correction.

---

# 11.34 Perspective Example

A photographed document may appear as:

```text
   ______
  /     /
 /_____/
```

A homography can transform it toward:

```text
┌──────────┐
│          │
│ document │
│          │
└──────────┘
```

The image is warped to approximate a frontal view.

---

# 11.35 Geometric Transformation vs Intensity Transformation

| Property | Geometric transformation | Intensity transformation |
|---|---|---|
| main change | coordinates | values |
| example | rotation | negative |
| core equation | \(\mathbf p'=T(\mathbf p)\) | \(s=T(r)\) |
| interpolation | often required | generally not |
| spatial arrangement | changes | usually preserved |
| examples | rotate, scale, warp | log, gamma, contrast stretch |

This is an important conceptual distinction.

---

# 11.36 Coordinate Conventions — Major Trap

Image arrays often use:

```text
row ↑ downward
column → right
```

Cartesian geometry often uses:

```text
x → right
y ↑ upward
```

Therefore a mathematical rotation can appear visually reversed if directly applied to row/column indices without conversion.

Always define:

```text
x ↔ column
y ↔ row
```

and the sign convention before deriving the transformation.

---

# 11.37 Pixel-Centre Conventions

> **DEEP DIVE**

Different systems can interpret coordinates as referring to:

- pixel centres,
- pixel corners,
- continuous image coordinates.

This affects resizing and transformation alignment.

For example, scaling around pixel centres versus array corners can produce a small but systematic shift.

This is one reason seemingly identical resizing operations can differ across libraries.

---

# 11.38 Half-Pixel and Alignment Issues

Consider a 2× image enlargement.

A simplistic coordinate map may use:

\[
x'=2x
\]

Another system may map pixel centres using an offset such as:

\[
x'=2(x+0.5)-0.5
\]

The resulting sampling locations differ.

> **Engineering rule:** When reproducing results across libraries, document the coordinate convention and interpolation geometry, not just the scale factor.

---

# 11.39 Boundary Handling in Resampling

A transformed coordinate may fall outside the source image.

The implementation must decide:

```text
constant
replicate
reflect
wrap
transparent / invalid
crop
```

The correct policy depends on the application.

For document warping, a constant background may be appropriate.

For cyclic image domains, wrap-around can be appropriate.

There is no universal choice.

---

# 11.40 Interpolation and Image Type

For a continuous-tone photograph:

```text
bilinear / bicubic
```

are often reasonable candidates.

For categorical label images:

```text
nearest-neighbour
```

is usually preferred because interpolation between labels creates meaningless fractional classes.

Example:

```text
class 1
class 2
```

Bilinear interpolation might produce:

\[
1.5
\]

which is not a valid class label.

This is a critical practical distinction.

---

# 11.41 Interpolation and Edge Sharpness

Interpolation can soften boundaries.

Conceptually:

```text
nearest
→ blocky but sharper transitions

bilinear
→ smoother but somewhat softer

bicubic
→ smoother; may preserve apparent sharpness differently
```

The actual result depends on the image and implementation.

---

# 11.42 Geometric Transformation Pipeline

A robust pipeline can be expressed as:

```text
INPUT IMAGE
     ↓
define coordinate convention
     ↓
define transformation
     ↓
choose forward/inverse mapping
     ↓
choose output grid
     ↓
map destination coordinates
     ↓
sample source
     ↓
interpolate
     ↓
handle boundaries
     ↓
write output
     ↓
evaluate geometry + image quality
```

Every stage can affect the result.

---

# 11.43 Implementation Pseudocode

```text
for each output pixel (x', y'):

    source_coord = inverse_transform(x', y')

    if source_coord is inside source image:
        value = interpolate(source, source_coord)
    else:
        value = boundary_value

    output[x', y'] = value
```

This compactly describes a large family of image-warp operations.

---

# 11.44 Worked Rotation Pipeline

Suppose a grayscale image must be rotated by:

\[
30^\circ
\]

A conceptual implementation is:

```text
1. define centre
2. construct rotation matrix
3. for each output pixel
4. transform output coordinate back to source
5. bilinearly interpolate
6. handle out-of-bounds coordinates
7. store output
```

The rotation angle alone is therefore not the whole algorithm.

---

# 11.45 Evaluation of Geometric Transforms

A correct transformation should be evaluated for:

### Geometry

- expected position,
- expected orientation,
- expected scale.

### Image quality

- aliasing,
- blur,
- interpolation artifacts,
- holes,
- clipping.

### Registration/alignment

- landmark alignment,
- overlap,
- transformation residual error.

A visually plausible image can still be geometrically incorrect.

---

# 11.46 Common Traps

## Trap 1 — “Rotation only changes coordinates.”

Incomplete.

After coordinate transformation, the output grid requires resampling.

## Trap 2 — “Forward mapping always fills the output.”

False.

It can produce holes and uneven coverage.

## Trap 3 — “Interpolation restores lost detail.”

False.

It estimates values from known samples.

## Trap 4 — “Bilinear is always better than nearest neighbour.”

False.

Nearest neighbour is often the correct choice for categorical labels.

## Trap 5 — “Downsampling only needs interpolation.”

Incomplete.

Anti-alias filtering is important when high-frequency content could alias.

## Trap 6 — “Transformations can be reordered freely.”

False.

Matrix transformations generally do not commute.

## Trap 7 — “Image y-coordinate is always Cartesian y.”

False.

Array row indexing often increases downward.

## Trap 8 — “A resize factor fully specifies a resize operation.”

False.

Coordinate convention, interpolation, anti-aliasing, rounding and boundary handling can differ.

---

# 11.47 Exam Formula Sheet

### Translation

\[
\boxed{
x'=x+t_x,\quad y'=y+t_y
}
\]

### Scaling

\[
\boxed{
x'=s_xx,\quad y'=s_yy
}
\]

### Rotation

\[
\boxed{
x'=x\cos\theta-y\sin\theta
}
\]

\[
\boxed{
y'=x\sin\theta+y\cos\theta
}
\]

### Affine transformation

\[
\boxed{
\begin{bmatrix}
x'\\y'\\1
\end{bmatrix}
=
\begin{bmatrix}
a_{11}&a_{12}&t_x\\
a_{21}&a_{22}&t_y\\
0&0&1
\end{bmatrix}
\begin{bmatrix}
x\\y\\1
\end{bmatrix}
}
\]

### Bilinear interpolation

\[
\boxed{
f(x,y)
=
(1-\alpha)(1-\beta)Q_{11}
+
\alpha(1-\beta)Q_{21}
+
(1-\alpha)\beta Q_{12}
+
\alpha\beta Q_{22}
}
\]

### Homography

\[
\boxed{
\lambda\mathbf p'=H\mathbf p
}
\]

---

# 11.48 Exam-Style Problem — Translation

A pixel at:

\[
(25,40)
\]

is translated by:

\[
(10,-15)
\]

Find its new position.

\[
x'=25+10=35
\]

\[
y'=40-15=25
\]

Therefore:

\[
\boxed{(35,25)}
\]

---

# 11.49 Exam-Style Problem — Rotation

Rotate:

\[
(2,1)
\]

by:

\[
90^\circ
\]

Then:

\[
x'=2(0)-1(1)=-1
\]

\[
y'=2(1)+1(0)=2
\]

Therefore:

\[
\boxed{(-1,2)}
\]

under the standard Cartesian convention.

---

# 11.50 Exam-Style Problem — Bilinear Interpolation

Given:

\[
Q_{11}=10,\quad Q_{21}=30,\quad Q_{12}=20,\quad Q_{22}=40
\]

and:

\[
\alpha=\beta=0.5
\]

then:

\[
f=
0.25(10)+0.25(30)+0.25(20)+0.25(40)
\]

\[
=
\frac{10+30+20+40}{4}
\]

\[
\boxed{25}
\]

At the exact centre of the four samples, bilinear interpolation becomes their arithmetic mean.

---

# 11.51 Practical Design Example — Document Rectification

A photographed page may be skewed and viewed in perspective.

A typical engineering pipeline:

```text
photo
 ↓
detect document corners
 ↓
estimate homography
 ↓
inverse warp
 ↓
bilinear/bicubic interpolation
 ↓
crop/standardize
 ↓
OCR or document processing
```

The geometric correction is often as important as the later OCR model.

---

# 11.52 Practical Design Example — Image Registration

Suppose two satellite images of the same area are slightly shifted.

Pipeline:

```text
image A
image B
  ↓
detect/match features
  ↓
estimate transformation
  ↓
warp B
  ↓
compare aligned images
```

Errors may arise from:

- incorrect feature matches,
- inappropriate transformation model,
- interpolation,
- non-rigid scene changes.

---

# 11.53 Connection to Frequency Domain

Geometric transformation changes spatial coordinates.

Fourier analysis changes the representation from:

```text
spatial domain
```

to:

```text
frequency domain
```

This gives the next conceptual transition:

```text
C11
WHERE are samples?

        ↓

C12
HOW does the image vary across spatial frequencies?
```

This is the bridge into the frequency-domain half of Unit II.

---

# 11.54 Cross-Book Bridges

> **C03 BRIDGE**  
> Sampling explains why transformed coordinates usually require interpolation and why downsampling can alias.

> **C04 BRIDGE**  
> Image dimensions, datatype and channel layout determine how transformed images are stored.

> **C08 BRIDGE**  
> Spatial filtering is often used as anti-aliasing before downsampling.

> **C12–C13 BRIDGE**  
> Frequency-domain methods provide another way to understand spatial detail and filtering.

> **C19–C20 BRIDGE**  
> Feature descriptors can support registration and alignment.

> **C30 BRIDGE**  
> Video stabilization and frame alignment are geometric transformation problems.

> **LAB BRIDGE**  
> Implement translation, scaling, rotation and interpolation comparisons; inspect coordinate grids and boundary effects.

> **PRACTICE BRIDGE**  
> Solve transformation matrices, composition, inverse mapping and interpolation calculations.

> **EXAM BRIDGE**  
> Know translation/scaling/rotation equations, affine transformation, bilinear interpolation and the distinction between forward and inverse mapping.

---

# 11.55 Quick Recall

```text
GEOMETRY
→ changes WHERE samples belong

INTERPOLATION
→ estimates values between known samples

FORWARD MAP
→ source → destination

INVERSE MAP
→ destination → source

NEAREST
→ one closest sample

BILINEAR
→ four neighbours

AFFINE
→ rotation + scale + shear + translation

HOMOGRAPHY
→ projective/perspective mapping
```

Core rule:

> **A geometric transform is not complete until the new grid has been resampled.**

---

# 11.56 Chapter Checkpoint

1. Define geometric transformation.
2. Write translation equations.
3. Write scaling equations.
4. Derive the 2-D rotation matrix.
5. Why is rotation about an image centre implemented using translations plus rotation?
6. Why does transformation order matter?
7. Define an affine transformation.
8. Why are homogeneous coordinates useful?
9. Compare forward and inverse mapping.
10. Why is interpolation required after a geometric transformation?
11. Explain nearest-neighbour interpolation.
12. Derive/use the bilinear interpolation equation.
13. Compare nearest, bilinear and bicubic interpolation.
14. Why should categorical masks usually avoid bilinear interpolation?
15. Why is anti-alias filtering important before downsampling?
16. Explain the coordinate-convention problem in image arrays.
17. What is a homography?
18. Give one engineering application of image registration.

---

# 11.57 Unit II Transition

The spatial-domain processing sequence is now:

```text
C06
INTENSITY TRANSFORMATIONS
        ↓
C07
HISTOGRAMS
        ↓
C08
SPATIAL FILTERING
        ↓
C09
NOISE REDUCTION
        ↓
C10
SHARPENING + EDGES
        ↓
C11
GEOMETRIC TRANSFORMATIONS
```

We are now ready for the frequency-domain representation:

```text
SPATIAL DOMAIN
        ↓
Fourier Transform
        ↓
FREQUENCY DOMAIN
        ↓
frequency filtering
```

That is Chapter 12.
