---
id: "M02"
title: "Functions, Coordinates and Discrete Images"
layer: "MATH"
part: "03 — Mathematics Companion"
unit_links:
  - "Unit I"
  - "Unit II"
  - "Unit IV"
version: "1.0"
status: "PRODUCTION"
syllabus_scope: "Image formation, sampling, quantization, image representation, pixels, resolution, video and tensor foundations"
tags:
  - digital-image-processing
  - mathematics
  - functions
  - coordinates
  - discrete-images
  - sampling
  - quantization
  - resolution
  - pixels
prerequisites:
  - "M01 — Mathematical Notation for Digital Image Processing"
related_main:
  - "C02 — Image Formation and Acquisition"
  - "C03 — Sampling and Quantization"
  - "C04 — Image Representation"
  - "C30 — Video Processing and Motion Analysis"
related_lab:
  - "LAB-01 — Image Input/Output and Colour Spaces"
  - "LAB-10 — Motion Tracking in Video"
related_code:
  - "CODE-01 — Image I/O and Representation"
  - "CODE-10 — Optical Flow and Tracking"
---

# M02 — Functions, Coordinates and Discrete Images

> **Purpose:** Build the mathematical bridge from a physical image modeled continuously over space to the finite numerical array stored and processed by a computer.

---

# 1. Why This Chapter Exists

A digital image is easiest to understand when you see the entire transformation:

```text
physical scene
      ↓
continuous image formation
      ↓
spatial sampling
      ↓
intensity quantization
      ↓
finite numerical array
      ↓
pixel operations
```

This chapter formalizes that transition.

The University syllabus explicitly requires:

- image formation;
- sampling;
- quantization;
- grayscale/RGB/multispectral images;
- pixels, bit depth and resolution. fileciteturn4file0L32-L35

The mathematics here supports those topics without turning the chapter into a signal-processing textbook.

---

# 2. Learning Contract

After this chapter, you should be able to:

- distinguish continuous and discrete image models;
- interpret \(f(x,y)\);
- interpret \(f[m,n]\);
- explain the spatial domain;
- explain image coordinates and indexing;
- determine the number of samples from image dimensions;
- connect sampling density to resolution;
- distinguish spatial sampling from intensity quantization;
- calculate the number of quantization levels from bit depth;
- calculate raw storage from dimensions and bit depth;
- reason about aliasing conceptually;
- distinguish pixel spacing from image dimensions;
- represent grayscale, RGB and multispectral images mathematically;
- extend the representation to video.

---

# 3. The Continuous Image Model

A real-world imaging system observes a scene and produces an image signal.

A common mathematical model is:

\[
f(x,y).
\]

Here:

- \(x\) = horizontal spatial coordinate;
- \(y\) = vertical spatial coordinate;
- \(f(x,y)\) = image intensity or radiometric measurement.

The coordinates are continuous in the mathematical model:

\[
x,y\in\mathbb R.
\]

The function therefore describes an idealized continuous spatial image.

---

# 4. What Does \(f(x,y)\) Mean Physically?

Suppose:

\[
f(10.2,7.4)=0.62.
\]

Conceptually, this says:

> At spatial location \((10.2,7.4)\), the image formation model assigns intensity/value 0.62 under the chosen scale.

This is a mathematical description, not necessarily a literal claim that a physical sensor has measured infinitely precise coordinates.

Real acquisition has optics, sensors and finite sampling.

---

# 5. From Continuous to Digital

A computer cannot store infinitely many values over a continuous plane.

We therefore discretize the image.

Two distinct operations are involved:

```text
spatial sampling
→ choose locations

intensity quantization
→ choose representable values
```

Thus:

\[
\boxed{
\text{digital image}
=
\text{sampled spatial coordinates}
+
\text{quantized values}
}
\]

This distinction is fundamental.

---

# 6. Spatial Sampling

Suppose we select equally spaced spatial coordinates:

\[
x=m\Delta_x
\]

and:

\[
y=n\Delta_y.
\]

Then the sampled image is:

\[
f[m,n]
=
f(m\Delta_x,n\Delta_y).
\]

Here:

- \(m,n\) are integer indices;
- \(\Delta_x,\Delta_y\) are spatial sampling intervals.

This equation provides the clean mathematical bridge from continuous coordinates to a discrete image.

---

# 7. Sample Spacing and Sampling Density

If:

\[
\Delta_x
\]

is small, samples are close together.

Therefore sampling density is high.

If:

\[
\Delta_x
\]

is large, samples are farther apart.

Therefore sampling density is lower.

Conceptually:

```text
small Δ
████████████████
many samples

large Δ
█   █   █   █
fewer samples
```

---

# 8. Sampling Frequency

In one spatial direction, a sampling frequency can be expressed conceptually as:

\[
f_s=\frac{1}{\Delta}
\]

when spatial units and reciprocal units are defined consistently.

This is analogous to temporal sampling in signals.

For example, if sample spacing is:

\[
\Delta=0.5\text{ mm},
\]

then:

\[
f_s=\frac{1}{0.5}
=
2\text{ samples/mm}.
\]

The exact unit depends on the physical spatial unit.

---

# 9. Pixel Grid

After sampling, the image becomes a finite grid.

For:

\[
M\times N
\]

samples:

```text
N columns
M rows
```

under the common matrix convention.

The image contains:

\[
MN
\]

sample locations.

### Example

For:

\[
512\times512,
\]

the number of samples is:

\[
512\times512
=
262{,}144.
\]

---

# 10. Pixel as a Mathematical Object

A pixel can be treated as:

```text
location
+
stored value(s)
```

For grayscale:

\[
p_{m,n}=f[m,n].
\]

For RGB:

\[
\mathbf p_{m,n}
=
\begin{bmatrix}
R_{m,n}\\
G_{m,n}\\
B_{m,n}
\end{bmatrix}.
\]

For multispectral imagery:

\[
\mathbf p_{m,n}
\in\mathbb R^C
\]

where \(C\) is the number of spectral bands.

Thus “pixel” does not always mean one scalar.

---

# 11. Grayscale Image as a Function

A grayscale digital image can be written:

\[
f[m,n].
\]

The sample values might satisfy:

\[
f[m,n]\in\{0,\ldots,255\}
\]

for a conventional 8-bit representation.

Or, after normalization:

\[
f[m,n]\in[0,1].
\]

These are different numeric representations of image values.

---

# 12. Matrix Representation

A finite grayscale image can be written:

\[
F=
\begin{bmatrix}
f[0,0] & f[0,1] & \cdots & f[0,N-1]\\
f[1,0] & f[1,1] & \cdots & f[1,N-1]\\
\vdots & \vdots & \ddots & \vdots\\
f[M-1,0] & f[M-1,1] & \cdots & f[M-1,N-1]
\end{bmatrix}.
\]

This is why image processing and matrix operations are so closely connected.

---

# 13. Coordinate-to-Array Mapping

Mathematical notation:

\[
f(x,y)
\]

is conceptually spatial.

A programming array may use:

```text
image[row, column]
```

which often corresponds to:

```text
image[y, x]
```

if:

\[
x=\text{column},
\quad
y=\text{row}.
\]

This mapping must be explicitly defined.

---

# 14. Why Coordinate Conventions Matter

Suppose you intend to access:

\[
(x,y)=(10,20).
\]

Under a row-column array convention, you may need:

```python
image[20, 10]
```

not:

```python
image[10, 20]
```

Swapping them may produce a valid pixel but the wrong location.

This kind of mistake can silently corrupt geometric transformations, optical-flow calculations and visual overlays.

---

# 15. Origin

A coordinate system needs an origin.

For many image-processing conventions:

```text
top-left
```

is treated as:

\[
(0,0).
\]

But mathematical coordinate systems often place the origin differently.

Therefore:

> **The image coordinate system is a convention, not a universal law.**

---

# 16. Vertical Direction

In many graphics/image arrays:

```text
x increases → right
y increases → down
```

while in a conventional Cartesian graph:

```text
x increases → right
y increases → up
```

This difference matters for:

- angles;
- geometric transforms;
- optical flow;
- plotted axes.

Always document it.

---

# 17. Resolution

“Resolution” can refer to several related concepts.

For a digital image:

```text
spatial dimensions
→ number of samples

physical resolution
→ spatial detail represented per physical unit

display resolution
→ device pixel structure
```

Do not collapse all of these into one number.

For a stored image:

\[
W\times H
\]

is the pixel dimension.

That does not by itself specify physical scene resolution.

---

# 18. Pixel Dimensions vs Physical Sampling

Suppose:

\[
W=2000,\quad H=1000.
\]

This tells us:

\[
2{,}000\times1{,}000
\]

samples.

But without knowing physical field of view or pixel spacing, we cannot determine:

```text
mm per pixel
```

or:

```text
metres per pixel.
```

Thus:

\[
\boxed{
\text{pixel count}\neq\text{complete physical resolution specification}
}
\]

---

# 19. Aspect Ratio

Aspect ratio can be expressed as:

\[
\text{AR}=\frac{W}{H}.
\]

For:

\[
W=1920,\quad H=1080,
\]

\[
AR=\frac{1920}{1080}
=
\frac{16}{9}.
\]

Aspect ratio describes shape of the image frame.

It is not the same as image resolution.

---

# 20. Sampling and Aliasing

If an image contains details that vary more rapidly than the sampling grid can represent, incorrect patterns can appear.

This is aliasing.

Conceptually:

```text
fine pattern
   ↓
insufficient samples
   ↓
different apparent pattern
```

The digitized image can therefore contain a pattern that was not truly present at that spatial frequency.

---

# 21. Intuitive Example of Aliasing

Imagine alternating stripes:

```text
█░█░█░█░█░
```

If sampling points align unfavourably with the pattern, the samples may appear:

```text
██████████
```

or:

```text
░░░░░░░░░░
```

or another incorrect lower-frequency pattern.

This is the spatial analogue of aliasing in sampled time signals.

---

# 22. Nyquist-Style Intuition

For a band-limited 1-D signal with highest frequency:

\[
f_{\max},
\]

a basic sampling theorem condition is:

\[
f_s>2f_{\max}
\]

for ideal reconstruction under its stated assumptions.

The image version applies the same idea spatially.

The full theorem contains important assumptions; do not interpret \(2f_{\max}\) as a universal guarantee for arbitrary real images.

---

# 23. Why Anti-Aliasing Is Used

Before downsampling, systems may suppress frequencies that cannot be represented at the lower sampling rate.

Conceptually:

```text
high-resolution image
      ↓
low-pass / anti-alias filtering
      ↓
downsampling
```

This reduces aliasing risk.

This connects image resampling to the frequency-domain material from C12–C13.

---

# 24. Downsampling

Suppose an image changes from:

\[
2000\times2000
\]

to:

\[
1000\times1000.
\]

The number of pixel samples becomes:

\[
1{,}000{,}000
\]

instead of:

\[
4{,}000{,}000.
\]

So the sample count is reduced by a factor of:

\[
4.
\]

Spatial dimensions are each halved.

---

# 25. Upsampling

Upsampling increases the number of samples.

For example:

\[
1000\times1000
\rightarrow
2000\times2000.
\]

The additional samples must be estimated.

That is why interpolation is necessary.

Upsampling does **not** recover true missing detail automatically.

---

# 26. Continuous Model vs Interpolation

Suppose only:

\[
f[0],f[1]
\]

are known.

An interpolator may estimate a value halfway between them.

For linear interpolation:

\[
f(0.5)
\approx
\frac{f[0]+f[1]}{2}.
\]

This creates a plausible intermediate value.

But unless additional information exists, it is still an estimate.

---

# 27. Quantization

Sampling chooses:

```text
where to measure
```

Quantization chooses:

```text
which representable value to store
```

Suppose the continuous intensity is:

\[
127.8.
\]

For integer storage:

\[
127.8
\rightarrow
128
\]

under a simple rounding rule.

This creates quantization error.

---

# 28. Quantization Levels

If each sample uses:

\[
k
\]

bits, the number of representable levels is:

\[
\boxed{L=2^k}.
\]

Examples:

\[
k=1\Rightarrow L=2
\]

\[
k=8\Rightarrow L=256
\]

\[
k=10\Rightarrow L=1024
\]

\[
k=12\Rightarrow L=4096
\]

\[
k=16\Rightarrow L=65536.
\]

---

# 29. Quantization Step Size

If the representable output range has width:

\[
R
\]

and there are \(L\) uniformly spaced levels, a simple quantizer has a step related to:

\[
\Delta_q\approx\frac{R}{L}
\]

depending on the exact endpoint convention.

Do not assume one formula fits every quantizer design.

---

# 30. Quantization Error

For a rounded scalar quantizer with step size \(\Delta_q\), the quantization error is:

\[
e_q=x-\hat x.
\]

In an ideal uniform mid-rise/mid-tread setting, magnitude is typically bounded by approximately:

\[
|e_q|\le\frac{\Delta_q}{2}.
\]

Exact bounds depend on the quantizer design and endpoint conventions.

---

# 31. Worked Quantization Example

Suppose:

\[
0\le x\le255
\]

and we use:

\[
k=3
\]

bits.

Then:

\[
L=2^3=8.
\]

There are eight representable levels.

A coarse quantizer must map the original continuum/intensity range into those eight levels.

This produces much larger quantization error than 8-bit storage.

---

# 32. Sampling Error vs Quantization Error

These are different.

### Sampling error / aliasing

Caused by insufficient spatial sampling.

```text
wrong spatial information
```

### Quantization error

Caused by limited value precision.

```text
value rounding / level approximation
```

A digital image can therefore have:

```text
adequate sampling
+
poor quantization

or

poor sampling
+
high bit depth
```

Higher bit depth does not fix spatial aliasing.

---

# 33. Bit Depth

Bit depth is the number of bits used to represent a sample or channel.

For grayscale:

\[
k=8
\]

means:

\[
256
\]

possible levels.

For 16-bit grayscale:

\[
2^{16}=65{,}536
\]

possible levels.

---

# 34. RGB Bit Depth

If each RGB channel uses:

\[
8\text{ bits},
\]

then one RGB pixel contains:

\[
8+8+8=24
\]

bits.

Therefore:

\[
2^{24}
\]

possible RGB code combinations if all combinations are representable.

That equals:

\[
16{,}777{,}216.
\]

This is commonly described as 24-bit colour.

---

# 35. Multispectral Representation

If an image has \(C\) spectral bands:

\[
\mathbf f(x,y)
=
\begin{bmatrix}
f_1(x,y)\\
f_2(x,y)\\
\vdots\\
f_C(x,y)
\end{bmatrix}.
\]

Then each spatial location has a spectral vector.

This is fundamentally different from treating the image as only one grayscale value.

The syllabus explicitly includes multispectral images. fileciteturn4file0L32-L35

---

# 36. Tensor Representation

A colour image can be viewed as:

\[
H\times W\times C.
\]

A multispectral image can also be:

\[
H\times W\times C
\]

with larger \(C\).

A video may become:

\[
T\times H\times W\times C.
\]

A batch of videos can add another dimension:

\[
B\times T\times H\times W\times C.
\]

The tensor is simply a multidimensional numerical arrangement.

---

# 37. Samples vs Values

This distinction is worth memorizing.

```text
Sampling
→ number/locations of measurements

Quantization
→ precision of the measured values
```

Therefore:

```text
resolution problem
≠
bit-depth problem
```

although they interact in image quality.

---

# 38. Raw Storage Mathematics

For:

- width \(W\);
- height \(H\);
- channels \(C\);
- bits/channel \(k\);

raw payload bits are:

\[
N_{\text{bits}}=WHCk.
\]

Raw bytes:

\[
N_{\text{bytes}}
=
\frac{WHCk}{8}.
\]

---

# 39. Worked Raw-Storage Example

Image:

\[
1920\times1080
\]

RGB:

\[
C=3
\]

8 bits/channel:

\[
k=8.
\]

Then:

\[
N_{\text{bytes}}
=
\frac{1920\times1080\times3\times8}{8}.
\]

So:

\[
N_{\text{bytes}}
=
1920\times1080\times3
\]

\[
=
6{,}220{,}800.
\]

Approximately:

\[
6.22\text{ MB}
\]

in decimal units.

---

# 40. Spatial Resolution and Sampling Interval

Suppose an image covers:

\[
100\text{ mm}
\]

across its width and contains:

\[
1000
\]

samples.

A simple average spacing is approximately:

\[
\Delta_x=\frac{100}{1000}
=
0.1\text{ mm/sample}.
\]

Therefore:

\[
\boxed{0.1\text{ mm/pixel}}
\]

under this simplified geometry.

---

# 41. Resolution Is Context-Dependent

The phrase “higher resolution” can mean:

```text
more pixels
```

or:

```text
smaller physical sampling interval
```

or:

```text
better ability to resolve fine detail
```

These are related but not identical.

A 4000×3000 image can be:

- higher pixel count;
- lower physical resolution,

depending on the field of view.

---

# 42. Discrete Spatial Domain

Once sampled, coordinates become indices.

Write:

\[
m,n\in\mathbb Z.
\]

A finite image might use:

\[
m=0,\ldots,M-1
\]

\[
n=0,\ldots,N-1.
\]

Then:

\[
f[m,n]
\]

is a finite discrete data set.

---

# 43. Finite Support

An image has finite spatial extent.

We can think of:

\[
f[m,n]=0
\]

outside its defined finite region for some theoretical operations.

This is useful when discussing:

- convolution;
- padding;
- transforms;
- boundary handling.

The chosen extension outside the image is implementation-dependent.

---

# 44. Boundary Conditions

Suppose a filter wants:

\[
f[m-1,n].
\]

What happens at:

\[
m=0?
\]

That index is outside the stored image.

Possible policies:

```text
zero
replicate edge
reflect
wrap/circular
ignore incomplete neighbourhood
```

Therefore the mathematical operation alone may be incomplete without a boundary convention.

---

# 45. Continuous Image Formation vs Digital Representation

A useful layered model is:

```text
physical world
      ↓
scene radiance / reflected light
      ↓
continuous image field
      ↓
sensor sampling
      ↓
spatial samples
      ↓
ADC / quantization
      ↓
digital values
      ↓
array / tensor
```

This connects image formation from C02 to the representation ideas from C04.

---

# 46. Grayscale, RGB and Multispectral — Mathematical Comparison

| Representation | Mathematical form | Values per location |
|---|---|---:|
| Grayscale | \(f[m,n]\) | 1 |
| RGB | \(\mathbf f[m,n]\in\mathbb R^3\) | 3 |
| Multispectral | \(\mathbf f[m,n]\in\mathbb R^C\) | \(C\) |
| Video RGB | \(f[m,n,t,c]\) or tensor | 3 per frame location |

This is the mathematical basis of “types of images” in Unit I.

---

# 47. Colour Space Is Not Tensor Shape

An RGB image and a YCbCr image can both have:

\[
H\times W\times3.
\]

The tensor shape is the same.

The meaning of the three channels is different.

Thus:

\[
\boxed{
\text{shape}\neq\text{semantic representation}
}
\]

This distinction matters in code.

---

# 48. Normalized vs Integer Images

These can both represent the same conceptual grayscale image:

```text
uint8:
[0, 128, 255]

normalized float:
[0.0, 0.50196, 1.0]
```

The numeric values differ because the scale differs.

Many machine-learning pipelines prefer normalized floating-point inputs.

Classical image-writing APIs may prefer integer formats.

Always know the current range.

---

# 49. Sampling Grid and Image Geometry

Suppose sample points are:

\[
(x_m,y_n)
=
(m\Delta_x,n\Delta_y).
\]

Then image geometry is determined by:

- origin;
- sample spacing;
- number of samples;
- coordinate convention.

This is enough to reason about basic spatial transformations without immediately introducing homogeneous coordinates.

---

# 50. Translation

A translation by:

\[
(\Delta x,\Delta y)
\]

maps:

\[
x'=x+\Delta x
\]

\[
y'=y+\Delta y.
\]

This is a coordinate transformation.

It does not inherently change pixel values.

After the transformation, however, interpolation may be required because mapped coordinates may not fall exactly on the original grid.

---

# 51. Rotation

A rotation around the origin is:

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
\end{bmatrix}.
\]

This is a continuous coordinate transformation.

A digital implementation needs:

```text
coordinate mapping
+
interpolation
+
boundary policy
```

The equation alone does not produce a complete image algorithm.

---

# 52. Connection to Sampling

After geometric transformation, desired coordinates may be fractional:

\[
x'=12.3.
\]

The discrete image does not necessarily contain a sample exactly at 12.3.

Interpolation estimates the value.

Thus:

```text
geometry
→ fractional coordinates
→ interpolation
→ digital output
```

This is why sampling mathematics naturally connects to C11.

---

# 53. Video as a Discrete 3-D Signal

A grayscale video can be written:

\[
f[m,n,t].
\]

For RGB:

\[
f[m,n,t,c].
\]

Here the temporal coordinate is also discretized.

If a video has:

\[
30\text{ FPS},
\]

then frame \(t\) corresponds approximately to:

\[
t/30
\]

seconds from the first frame under a simplified indexing model beginning at zero.

---

# 54. Temporal Sampling and Motion

Suppose an object moves:

\[
u=6\text{ pixels/frame}.
\]

At:

\[
30\text{ FPS},
\]

a simple average image-space displacement rate is:

\[
6\times30
=
180\text{ pixels/s}.
\]

This is not physical velocity unless pixel-to-world calibration is available.

This connects M02 directly to optical flow in C30.

---

# 55. 2-D vs 3-D vs 4-D Terminology

A grayscale image can be considered:

```text
2-D spatial data
```

A grayscale video:

```text
3-D data
(x,y,t)
```

An RGB video:

```text
4-D data
(x,y,t,c)
```

A batched RGB video becomes:

```text
5-D tensor
(batch, time, height, width, channel)
```

Terminology can differ by field.

The dimensions themselves are what matter.

---

# 56. Worked Example — Image-to-Tensor

Suppose:

\[
H=128,\quad W=256,\quad C=3.
\]

The image tensor contains:

\[
128\times256\times3.
\]

Number of scalar channel values:

\[
128\times256\times3
=
98{,}304.
\]

For a batch of:

\[
B=16,
\]

the batch contains:

\[
16\times98{,}304
=
1{,}572{,}864
\]

scalar values.

This is a simple but useful tensor-size calculation.

---

# 57. Sampling vs Quantization Table

| Property | Sampling | Quantization |
|---|---|---|
| Acts on | spatial/time coordinates | value/intensity amplitude |
| Main question | where do we measure? | which value do we store? |
| Controlled by | sample spacing/rate | bit depth/levels |
| Main risk | aliasing | quantization error |
| Example | 512×512 vs 1024×1024 | 8-bit vs 16-bit |

---

# 58. Bit Depth vs Dynamic Range

Higher bit depth means more representable numerical levels.

It does not automatically guarantee a larger physical dynamic range.

A sensor can have:

```text
16-bit representation
```

while its effective physical dynamic range is limited by sensor noise/saturation.

Thus:

\[
\boxed{
\text{bit depth}\neq\text{complete sensor dynamic-range specification}
}
\]

This distinction becomes important in image acquisition.

---

# 59. Sampling and Compression

Sampling affects the amount of spatial data.

Compression can reduce the bits required to store that data.

Conceptually:

```text
higher sampling
→ more samples
→ more raw data

compression
→ fewer storage bits
```

These are different system levers.

A smaller compressed file does not mean the image was sampled at lower resolution.

---

# 60. A Unified Image Model

A powerful abstraction is:

\[
I=
\left\{
f[m,n,c]
\right\}.
\]

For video:

\[
V=
\left\{
f[m,n,t,c]
\right\}.
\]

Then nearly every later DIP operation can be understood as:

```text
select values
+
combine values
+
transform values
+
estimate values
```

This is the mathematical foundation of the entire subject.

---

# 61. Common Traps

### Trap 1 — Sampling and quantization are the same.

False.

Sampling discretizes coordinates; quantization discretizes values.

### Trap 2 — More pixels always mean better physical resolution.

False.

Physical field of view and sampling geometry matter.

### Trap 3 — 16-bit always means 16-bit sensor precision.

Not necessarily.

It may describe storage representation.

### Trap 4 — Higher bit depth fixes aliasing.

False.

Aliasing is primarily a sampling problem.

### Trap 5 — Interpolation recreates lost information exactly.

False.

It estimates values from available information and assumptions.

### Trap 6 — RGB is the tensor itself.

No.

RGB is a colour representation; tensor shape describes organization of the numerical data.

---

# 62. Exam Lens

## 2-mark

**What is a digital image mathematically?**

A finite, discrete set of sampled and quantized image values, commonly represented as an array \(f[m,n]\).

**State the relation between bit depth and quantization levels.**

\[
L=2^k.
\]

---

## 5-mark

### Explain sampling and quantization.

Write:

```text
continuous image
→ spatial sampling
→ discrete coordinates

continuous intensity
→ quantization
→ discrete levels
```

Then explain aliasing and quantization error.

---

## 10-mark

### Explain how a continuous image becomes a digital image.

Recommended structure:

1. physical scene;
2. image formation;
3. continuous image model;
4. spatial sampling;
5. sampling interval/density;
6. aliasing;
7. anti-aliasing;
8. intensity quantization;
9. bit depth;
10. digital matrix/tensor;
11. RGB/multispectral extension;
12. storage implications.

---

# 63. Numerical Practice

### Problem 1

An 8-bit grayscale image has:

\[
1024\times768.
\]

Find raw bytes.

\[
1024\times768
=
786{,}432
\]

bytes.

### Problem 2

A colour image has:

\[
640\times480
\]

and 8 bits per channel for RGB.

Find raw bits:

\[
640\times480\times3\times8.
\]

### Problem 3

How many intensity levels are represented by 12 bits?

\[
2^{12}=4096.
\]

---

# 64. Chapter Checkpoint

### Q1

What is the mathematical difference between:

\[
f(x,y)
\]

and:

\[
f[m,n]?
\]

### Q2

Why does increasing bit depth not eliminate aliasing?

### Q3

How many quantization levels are available at 10 bits?

### Q4

Why does an RGB pixel usually contain three scalar values?

### Q5

What does \(f[m,n,t]\) represent?

### Q6

Why is interpolation required after some geometric transformations?

### Q7

What information is missing when someone tells you only that an image is “4000×3000”?

---

# 65. One-Page Recall Sheet

```text
CONTINUOUS IMAGE
f(x,y)
    ↓
SPATIAL SAMPLING
f[m,n]
    ↓
INTENSITY QUANTIZATION
finite levels
    ↓
DIGITAL IMAGE
matrix / tensor
```

Core formulas:

\[
f[m,n]=f(m\Delta_x,n\Delta_y)
\]

\[
L=2^k
\]

\[
N_{\text{bits}}=WHCk
\]

Sampling:

\[
f_s\approx\frac1\Delta
\]

Spatial video:

\[
f[m,n,t]
\]

RGB:

\[
\mathbf f[m,n]\in\mathbb R^3
\]

---

# 66. Cross-Book Links

| Layer | Connection |
|---|---|
| MAIN | C02, C03, C04, C11, C30 |
| MATH | Foundation for sampling, quantization, geometry and tensors |
| LAB | Image loading, resolution, datatype and video experiments |
| CODE | Array shape, indexing, datatype/range and coordinate conventions |
| EXAM | Sampling vs quantization, bit depth, resolution |
| PRACTICE | Matrix dimensions, storage calculations, aliasing reasoning |
| RESOURCE | Gonzalez & Woods / Szeliski mathematical foundations |
| ASSETS | Sampling grids, quantization ladders, tensor diagrams |
| MASTER | Mathematical dependency graph for Units I and later chapters |

---

# 67. Final Summary

The mathematical bridge is:

\[
\boxed{
\text{continuous spatial function}
\rightarrow
\text{sampled grid}
\rightarrow
\text{quantized values}
\rightarrow
\text{digital array}
}
\]

Sampling answers:

\[
\boxed{\text{Where do we measure?}}
\]

Quantization answers:

\[
\boxed{\text{Which value do we store?}}
\]

And the digital representation becomes:

\[
\boxed{
f[m,n]
}
\]

for grayscale,

\[
\boxed{
\mathbf f[m,n]\in\mathbb R^3
}
\]

for RGB,

and more generally:

\[
\boxed{
f[m,n,t,c]
}
\]

for video with channels.

This chapter therefore supplies the mathematical foundation for image formation, sampling, quantization, pixels, resolution, colour-channel representation and the later temporal/tensor view of DIP.
