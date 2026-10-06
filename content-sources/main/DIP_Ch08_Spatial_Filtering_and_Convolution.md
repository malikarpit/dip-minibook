---
id: "C08"
title: "Spatial Filtering and Convolution"
layer: "MAIN"
part: "II — Improving the Image"
unit: "II"
version: "1.0"
status: "REFERENCE BUILD"
syllabus_scope:
  - "Spatial-domain enhancement"
  - "Smoothing"
  - "Sharpening"
  - "Filtering"
tags:
  - "CORE"
  - "EXAM"
  - "MATH"
  - "DEEP DIVE"
  - "LAB"
  - "CONVOLUTION"
  - "MATRICES"
prerequisites:
  - "C04"
  - "C06"
  - "C07"
related:
  - "C09"
  - "C10"
  - "C11"
  - "C12"
  - "C13"
  - "C14"
math:
  - "M05"
  - "M06"
  - "M07"
  - "M08"
lab:
  - "LAB-U2-02"
  - "LAB-U2-03"
  - "LAB-U2-04"
exam:
  - "EXAM-U2"
practice:
  - "P-C08"
assets:
  - "D-C08-01"
  - "D-C08-02"
  - "D-C08-03"
---

# Chapter 08 — Spatial Filtering and Convolution

> **Chapter thesis**  
> Point processing looks at one pixel at a time. Spatial filtering adds neighbourhood context. A filter kernel moves across the image, combines nearby values according to weights, and produces a new image that can suppress noise, blur detail, enhance structure or expose edges.

**Part II — Improving the Image**  
**Syllabus anchor:** Unit II includes spatial-domain enhancement with smoothing, sharpening and edge-detection operations. fileciteturn4file0L36-L40

---

# 08.0 Why Spatial Filtering Matters

A pixel's meaning often depends on its neighbours.

For example:

```text
flat region:
100 100 100
100 100 100
100 100 100
```

contains little local change.

But:

```text
100 100 200
100 100 200
100 100 200
```

contains a strong transition.

A spatial filter can detect or modify such local structure.

The conceptual progression is:

```text
C06
one pixel
   ↓
C07
whole-image intensity distribution
   ↓
C08
pixel + neighbourhood
```

---

# 08.1 What Is Spatial Filtering?

A spatial filter computes an output value using image samples around a target location.

General form:

\[
g(x,y)=\mathcal{F}\left\{f(x,y)\right\}
\]

More specifically, for a linear filter:

\[
g(x,y)=
\sum_s\sum_t
w(s,t)f(x-s,y-t)
\]

where:

- \(f\) = input image,
- \(w\) = filter/kernel coefficients,
- \(g\) = output,
- \(s,t\) = neighbourhood offsets.

The exact indexing convention may vary between correlation and convolution notation.

---

# 08.2 The Kernel / Mask

A spatial filter is often represented by a small matrix called a:

- kernel,
- mask,
- filter.

For example:

\[
H=
\frac{1}{9}
\begin{bmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{bmatrix}
\]

This is a 3×3 averaging kernel.

The kernel slides over the image.

---

# 08.3 The Sliding-Window Mental Model

Imagine:

```text
IMAGE

a b c d e
f g h i j
k l m n o
p q r s t
u v w x y

        ↓
     ┌─────┐
     │g h i│
     │l m n│
     │q r s│
     └─────┘
       KERNEL
```

The filter computes a new output value for the centre location.

Then it moves:

```text
→ one column
→ one column
→ next row
```

until the image has been processed.

---

# 08.4 Weighted Sum

For a 3×3 kernel:

\[
H=
\begin{bmatrix}
h_{11}&h_{12}&h_{13}\\
h_{21}&h_{22}&h_{23}\\
h_{31}&h_{32}&h_{33}
\end{bmatrix}
\]

and neighbourhood:

\[
P=
\begin{bmatrix}
p_{11}&p_{12}&p_{13}\\
p_{21}&p_{22}&p_{23}\\
p_{31}&p_{32}&p_{33}
\end{bmatrix}
\]

a basic filtering calculation is a weighted sum:

\[
g=
\sum_{i=1}^{3}\sum_{j=1}^{3}
h_{ij}p_{ij}
\]

for a correlation-style alignment.

---

# 08.5 Worked Example — 3×3 Mean Filter

Suppose the neighbourhood is:

\[
P=
\begin{bmatrix}
10&20&30\\
20&30&40\\
30&40&50
\end{bmatrix}
\]

and:

\[
H=
\frac19
\begin{bmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{bmatrix}
\]

Then:

\[
g=
\frac{10+20+30+20+30+40+30+40+50}{9}
\]

Sum:

\[
270
\]

Therefore:

\[
g=30
\]

So the centre output becomes:

\[
\boxed{30}
\]

This is local averaging.

---

# 08.6 Why Averaging Smooths

Suppose neighbouring values are:

```text
10 10 10
10 200 10
10 10 10
```

The centre value is a sharp isolated spike.

A 3×3 mean filter produces:

\[
\frac{280}{9}\approx31.11
\]

The 200 is pulled much closer to its neighbours.

This reduces isolated fluctuations.

However:

> useful small details can also be smoothed.

---

# 08.7 Smoothing vs Blurring

These terms are related but should not be treated as perfectly interchangeable.

### Smoothing

Emphasizes local averaging and suppresses rapid intensity variation.

### Blurring

Describes the resulting loss of fine spatial detail.

A filter intentionally designed to reduce noise may therefore create blur as a tradeoff.

---

# 08.8 Smoothing Filters

Common smoothing filters include:

- mean/box filter,
- weighted averaging filter,
- Gaussian filter,
- median filter.

The first three are based on different forms of weighted/local averaging.

Median filtering is nonlinear and behaves differently.

---

# 08.9 Mean Filter

A \(3\times3\) mean kernel is:

\[
H=
\frac19
\begin{bmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{bmatrix}
\]

For a \(5\times5\) mean filter:

\[
H=
\frac1{25}
\begin{bmatrix}
1&1&1&1&1\\
1&1&1&1&1\\
1&1&1&1&1\\
1&1&1&1&1\\
1&1&1&1&1
\end{bmatrix}
\]

As the kernel gets larger, the smoothing neighbourhood increases.

---

# 08.10 Kernel Size Tradeoff

Generally:

```text
small kernel
→ weaker smoothing
→ better detail retention

large kernel
→ stronger smoothing
→ more detail loss
```

This is a task-dependent tradeoff.

A very large kernel can remove meaningful structures along with noise.

---

# 08.11 Gaussian Filter

A Gaussian kernel assigns larger weights near the centre and smaller weights farther away.

A continuous 2-D Gaussian is:

\[
G(x,y)=
\frac{1}{2\pi\sigma^2}
e^{-\frac{x^2+y^2}{2\sigma^2}}
\]

where:

\[
\sigma
\]

controls the spread.

A discrete kernel is obtained by sampling/discretizing the Gaussian and normalizing it as appropriate.

---

# 08.12 Why Gaussian Smoothing Is Useful

Compared with an equal-weight box filter, a Gaussian filter gives greater influence to nearby pixels.

Conceptually:

```text
farther pixel
     ↓
small weight

nearby pixel
     ↓
larger weight

centre pixel
     ↓
largest weight
```

This often produces smoother and more natural spatial filtering behaviour.

---

# 08.13 Example Gaussian Kernel

A commonly used conceptual 3×3 Gaussian-like kernel is:

\[
H=
\frac1{16}
\begin{bmatrix}
1&2&1\\
2&4&2\\
1&2&1
\end{bmatrix}
\]

Check the normalization:

\[
1+2+1+2+4+2+1+2+1=16
\]

So the coefficients sum to:

\[
1
\]

A unit DC response is therefore obtained.

---

# 08.14 Worked Gaussian Calculation

Using:

\[
P=
\begin{bmatrix}
10&20&30\\
20&30&40\\
30&40&50
\end{bmatrix}
\]

and:

\[
H=
\frac1{16}
\begin{bmatrix}
1&2&1\\
2&4&2\\
1&2&1
\end{bmatrix}
\]

weighted sum:

\[
10(1)+20(2)+30(1)+20(2)+30(4)+40(2)+30(1)+40(2)+50(1)
\]

\[
=10+40+30+40+120+80+30+80+50
\]

\[
=480
\]

Thus:

\[
g=\frac{480}{16}=30
\]

Again:

\[
\boxed{30}
\]

The same neighbourhood happens to produce the same centre value as the mean filter in this particular example.

That is not generally true.

---

# 08.15 Smoothing and High Frequencies

A smoothing filter generally suppresses rapid local changes.

Therefore, from a frequency-domain perspective:

```text
high spatial frequencies
→ reduced

low spatial frequencies
→ relatively preserved
```

This creates a bridge to Chapter 12 and Chapter 13:

```text
spatial smoothing
↔
frequency-domain low-pass filtering
```

The mathematical descriptions differ, but the underlying effect can be closely related.

---

# 08.16 Median Filter

The median filter is nonlinear.

For:

\[
[10,10,10,10,200]
\]

the median is:

\[
10
\]

So a large isolated outlier is removed without averaging the values toward it.

This makes median filtering especially useful for impulse-like “salt-and-pepper” noise.

---

# 08.17 Worked Median Example

Sort the values:

\[
[10,10,10,10,200]
\]

The middle value is:

\[
\boxed{10}
\]

A mean would be:

\[
\frac{10+10+10+10+200}{5}=48
\]

So the mean is strongly influenced by the outlier while the median is not.

This illustrates why nonlinear filters can outperform linear averaging for certain noise types.

---

# 08.18 Correlation vs Convolution

This is one of the most important technical distinctions in spatial filtering.

### Correlation

The kernel is applied in its given orientation.

### Convolution

The kernel is flipped before the weighted sum.

For a 2-D kernel:

\[
h(m,n)
\]

convolution uses:

\[
h(-m,-n)
\]

conceptually.

---

# 08.19 Why the Difference Sometimes Doesn't Matter

If a kernel is symmetric:

\[
h(m,n)=h(-m,-n)
\]

then flipping it produces the same kernel.

Examples include many:

- mean filters,
- Gaussian filters.

Thus correlation and convolution give the same output for symmetric kernels under the same boundary conventions.

---

# 08.20 Why the Difference Matters for Edge Kernels

Consider a directional kernel such as:

\[
H=
\begin{bmatrix}
-1&0&1
\end{bmatrix}
\]

Flipping it gives:

\[
\begin{bmatrix}
1&0&-1
\end{bmatrix}
\]

The sign changes.

Therefore correlation and convolution can produce opposite signs.

The magnitude may remain informative, but the direction/orientation interpretation can differ.

---

# 08.21 Convolution Equation

A discrete 2-D convolution can be written:

\[
g[m,n]
=
\sum_{k}\sum_{\ell}
f[k,\ell]\,
h[m-k,n-\ell]
\]

Alternative equivalent indexing conventions exist.

The key conceptual feature is:

> the kernel is reversed relative to correlation.

---

# 08.22 Boundary Problem

What happens when the kernel reaches the image edge?

Suppose:

```text
┌───────────┐
│ image     │
│           │
│       ┌───┼── kernel
│       │
```

Part of the kernel falls outside the available image.

The algorithm needs a boundary rule.

Common options include:

- zero padding,
- replicate padding,
- reflect padding,
- circular/wrap padding,
- valid-only processing.

---

# 08.23 Zero Padding

Outside the image, assume:

\[
f=0
\]

Conceptually:

```text
0 0 0 0 0 0
0 a b c d 0
0 e f g h 0
0 i j k l 0
0 0 0 0 0 0
```

This is simple but can create artificial dark borders.

---

# 08.24 Replicate Padding

Extend the nearest edge values.

Conceptually:

```text
aaaaa
abbba
abbba
abbba
aaaaa
```

This often avoids the strong artificial dark edge caused by zero padding.

---

# 08.25 Reflect Padding

Mirror values across the boundary.

This can provide smoother edge behaviour for many filters.

The exact implementation details differ between libraries.

> **Engineering rule:** Boundary behaviour is part of the algorithm, not a cosmetic afterthought.

---

# 08.26 Output Size and Padding

For an input dimension \(N\), kernel dimension \(K\), stride \(S\), and padding \(P\), a common output-size expression is:

\[
N_{\text{out}}
=
\left\lfloor
\frac{N+2P-K}{S}
\right\rfloor+1
\]

For the same formula applied separately to height and width.

This expression is widely used in convolutional computational pipelines.

---

# 08.27 Worked Output-Size Example

Suppose:

\[
N=7
\]

\[
K=3
\]

\[
S=1
\]

\[
P=0
\]

Then:

\[
N_{\text{out}}
=
\left\lfloor
\frac{7-3}{1}
\right\rfloor+1
\]

\[
=4+1
\]

\[
\boxed{5}
\]

So a 7×7 input with a 3×3 kernel, stride 1 and no padding gives 5×5 output in this standard valid-convolution geometry.

---

# 08.28 “Same” vs “Valid”

### Valid

No padding:

```text
output smaller
```

### Same

Padding is selected so the output spatial dimensions can be preserved for suitable stride/settings.

For odd-sized kernels and stride 1, symmetric padding is commonly used.

Do not treat “same” as a universal literal padding amount independent of kernel size and framework.

---

# 08.29 Sharpening — The Opposite Goal

Smoothing reduces rapid variation.

Sharpening emphasizes rapid variation.

Conceptually:

```text
smooth background
→ remain relatively stable

edge
→ become more pronounced
```

One common conceptual approach is:

```text
original
    ↓
blurred version
    ↓
difference
    ↓
add scaled detail back
    ↓
sharpened image
```

This leads naturally to unsharp masking.

---

# 08.30 Unsharp Masking

Let:

\[
f
\]

be the original image.

Let a low-pass filter produce:

\[
f_{\text{blur}}
\]

Then the detail mask is:

\[
m=f-f_{\text{blur}}
\]

A sharpened image can be:

\[
g=f+k\,m
\]

where:

\[
k>0
\]

controls the sharpening strength.

This is called unsharp masking even though it uses a blurred image to construct the “mask.”

---

# 08.31 Equivalent Unsharp Formula

Substitute:

\[
m=f-f_{\text{blur}}
\]

into:

\[
g=f+km
\]

to get:

\[
g=f+k(f-f_{\text{blur}})
\]

\[
g=(1+k)f-kf_{\text{blur}}
\]

This makes the operation's linear-combination structure explicit.

---

# 08.32 Worked Unsharp Example

Suppose at one pixel:

\[
f=120
\]

and the blurred value is:

\[
f_{\text{blur}}=100
\]

Then:

\[
m=120-100=20
\]

For:

\[
k=1
\]

we get:

\[
g=120+20=140
\]

So the local detail is emphasized.

If instead:

\[
k=0.5
\]

then:

\[
g=120+0.5(20)=130
\]

Thus \(k\) controls the strength.

---

# 08.33 High-Boost Filtering

A stronger generalization is:

\[
g=A f-f_{\text{blur}}
\]

with:

\[
A>1
\]

When \(A=1+k\), this can be related directly to the unsharp expression.

High-boost filtering can increase fine detail more aggressively, but it can also amplify noise.

---

# 08.34 Laplacian Filtering

The Laplacian is a second-derivative operator.

In continuous form:

\[
\nabla^2f
=
\frac{\partial^2f}{\partial x^2}
+
\frac{\partial^2f}{\partial y^2}
\]

A common discrete approximation is:

\[
H=
\begin{bmatrix}
0&1&0\\
1&-4&1\\
0&1&0
\end{bmatrix}
\]

or a sign-reversed version depending on convention.

Different textbooks use different signs.

The important thing is to keep the kernel and the sharpening formula consistent.

---

# 08.35 Why the Laplacian Detects Rapid Change

The second derivative is sensitive to rapid changes in intensity.

A simplified conceptual interpretation:

```text
flat region
→ little second-order change

edge / fine structure
→ strong second-order response
```

This makes the Laplacian useful for:

- sharpening,
- detecting fine structure,
- constructing detail-enhancement operators.

---

# 08.36 Sharpening with the Laplacian

Depending on sign convention:

\[
g=f-\nabla^2f
\]

or:

\[
g=f+\nabla^2f
\]

may be used.

The correct version depends on the chosen Laplacian kernel sign.

> **EXAM TRAP:** Do not memorize the sharpening sign independently from the Laplacian definition.

---

# 08.37 Edge Detection as Spatial Differentiation

An edge is approximately a location where intensity changes rapidly.

The first derivative therefore provides a natural edge measure.

For a 1-D signal:

```text
100 100 100 200 200 200
          ↑
        edge
```

The derivative is approximately:

```text
0 0 0 +large 0 0
```

This is the core mathematical idea behind gradient-based edge detection.

---

# 08.38 Image Gradient

For a continuous image:

\[
\nabla f=
\begin{bmatrix}
\frac{\partial f}{\partial x}\\[4pt]
\frac{\partial f}{\partial y}
\end{bmatrix}
\]

The gradient magnitude is:

\[
|\nabla f|
=
\sqrt{
\left(\frac{\partial f}{\partial x}\right)^2
+
\left(\frac{\partial f}{\partial y}\right)^2
}
\]

The gradient direction is:

\[
\theta
=
\operatorname{atan2}
\left(
\frac{\partial f}{\partial y},
\frac{\partial f}{\partial x}
\right)
\]

These concepts are central to edge detection.

---

# 08.39 Simple Difference Kernels

A very simple horizontal derivative approximation is:

\[
H_x=
\begin{bmatrix}
-1&1
\end{bmatrix}
\]

A vertical version is:

\[
H_y=
\begin{bmatrix}
-1\\
1
\end{bmatrix}
\]

These approximate directional change.

They are simple but highly noise-sensitive.

---

# 08.40 Sobel Operator

The Sobel operator combines differentiation with some smoothing.

A common pair is:

\[
G_x=
\begin{bmatrix}
-1&0&1\\
-2&0&2\\
-1&0&1
\end{bmatrix}
\]

\[
G_y=
\begin{bmatrix}
-1&-2&-1\\
0&0&0\\
1&2&1
\end{bmatrix}
\]

Different sign conventions also exist.

The resulting responses estimate horizontal and vertical intensity derivatives.

---

# 08.41 Gradient Magnitude Approximation

After computing:

\[
G_x,\quad G_y
\]

the exact magnitude is:

\[
G=
\sqrt{G_x^2+G_y^2}
\]

A cheaper approximation sometimes used is:

\[
G\approx|G_x|+|G_y|
\]

The latter is computationally simpler but is not identical to the Euclidean magnitude.

---

# 08.42 Worked Sobel Interpretation

Suppose a strong vertical edge exists:

```text
dark | bright
```

The intensity changes strongly from left to right.

Therefore:

\[
|G_x|
\]

will tend to be large.

The corresponding:

\[
|G_y|
\]

may be smaller.

This tells us not only:

```text
there is an edge
```

but also gives information about its orientation.

---

# 08.43 Edge Orientation

The gradient direction points in the direction of strongest intensity increase.

The visual edge itself is approximately perpendicular to the gradient direction.

This is a frequent conceptual exam point:

```text
gradient direction
⊥
edge orientation
```

under the local idealized edge model.

---

# 08.44 Prewitt Operator

A common Prewitt pair is:

\[
G_x=
\begin{bmatrix}
-1&0&1\\
-1&0&1\\
-1&0&1
\end{bmatrix}
\]

\[
G_y=
\begin{bmatrix}
-1&-1&-1\\
0&0&0\\
1&1&1
\end{bmatrix}
\]

Compared with Sobel, the weighting differs.

Both are gradient-based edge operators.

---

# 08.45 Sobel vs Prewitt

| Property | Sobel | Prewitt |
|---|---|---|
| derivative basis | yes | yes |
| smoothing component | stronger central weighting | simpler equal weighting |
| complexity | low | low |
| typical use | general edge estimation | general edge estimation |
| key difference | coefficients | coefficients |

Neither is universally superior.

---

# 08.46 Noise and Differentiation

Differentiation is sensitive to rapid variations.

Noise often contains strong high-frequency components.

Therefore:

```text
noise
  ↓
derivative filter
  ↓
may become amplified
```

This explains why practical edge detection often includes smoothing first:

```text
image
 ↓
noise suppression / Gaussian smoothing
 ↓
gradient
 ↓
edge decision
```

This is an important bridge to C09 and C10.

---

# 08.47 Filter Classification

Spatial filters can be classified in several ways.

### By linearity

```text
linear
→ weighted sums

nonlinear
→ median, morphological operations, etc.
```

### By frequency effect

```text
low-pass
→ suppress high frequencies

high-pass
→ emphasize high frequencies

band-pass
→ retain selected frequency ranges
```

### By objective

```text
smoothing
sharpening
edge detection
```

The categories overlap.

---

# 08.48 Separable Filters

> **EXTENSION**

Some 2-D kernels can be expressed as an outer product of two 1-D kernels.

For the Gaussian-like kernel:

\[
\begin{bmatrix}
1\\2\\1
\end{bmatrix}
\begin{bmatrix}
1&2&1
\end{bmatrix}
=
\begin{bmatrix}
1&2&1\\
2&4&2\\
1&2&1
\end{bmatrix}
\]

Therefore a 2-D filtering operation can sometimes be implemented as:

```text
horizontal 1-D filter
        ↓
vertical 1-D filter
```

instead of a full 2-D kernel.

This can reduce computation.

---

# 08.49 Complexity Intuition

For an image with \(MN\) pixels and a \(K\times K\) kernel, direct filtering is roughly proportional to:

\[
MNK^2
\]

multiply/add operations, ignoring implementation-specific optimizations.

For a separable kernel, the work can be closer to:

\[
2MNK
\]

in the simple direct model.

This is why separability matters in performance-sensitive image pipelines.

---

# 08.50 Integer Kernels and Scaling

Many practical derivative kernels have integer coefficients.

For example:

\[
G_x=
\begin{bmatrix}
-1&0&1\\
-2&0&2\\
-1&0&1
\end{bmatrix}
\]

The output is not automatically in:

\[
0\ldots255
\]

It may contain:

- negative values,
- values greater than 255,
- a dynamic range different from the input.

Therefore a pipeline may need:

```text
filter
→ working datatype
→ magnitude / normalization
→ display conversion
```

rather than blindly casting to uint8.

---

# 08.51 Why “Apply Kernel and Save as uint8” Can Fail

Suppose a derivative response is:

\[
-120
\]

A direct unsigned conversion can produce unexpected behaviour depending on the conversion mechanism.

The intended scientific quantity is not:

```text
negative edge
→ random-looking byte
```

It is a signed response.

A correct workflow keeps the response in an appropriate signed or floating representation until interpretation is complete.

---

# 08.52 Worked Edge Matrix Example

Consider:

\[
I=
\begin{bmatrix}
10&10&100\\
10&10&100\\
10&10&100
\end{bmatrix}
\]

Apply a simple horizontal derivative:

\[
H=
\begin{bmatrix}
-1&0&1
\end{bmatrix}
\]

At the centre row:

\[
(-1)(10)+(0)(10)+(1)(100)
\]

\[
=-10+100
\]

\[
\boxed{90}
\]

A strong positive response indicates a strong increase from left to right under this kernel convention.

---

# 08.53 Filter Response as Local Evidence

A filter output should be interpreted as evidence about a local property.

Examples:

```text
mean filter
→ local average

Gaussian
→ weighted local average

Laplacian
→ second-order variation

Sobel Gx
→ x-direction intensity change

Sobel Gy
→ y-direction intensity change
```

The filter is therefore not “detecting objects” automatically.

It extracts a mathematical signal from the image.

---

# 08.54 Choosing a Filter

| Goal | Candidate |
|---|---|
| simple smoothing | mean |
| smoother weighted blur | Gaussian |
| impulse-noise suppression | median |
| second-order detail response | Laplacian |
| directional gradient | Sobel / Prewitt |
| controlled sharpening | unsharp masking |
| stronger detail enhancement | high-boost |

The image, noise, task and acceptable artifacts determine the final choice.

---

# 08.55 Practical Pipeline — Noise Reduction

```text
noisy image
    ↓
inspect noise type
    ↓
choose filter
    ├── Gaussian-like noise
    │     → Gaussian smoothing
    │
    └── impulse noise
          → median
    ↓
evaluate
    ↓
edge/detail retention check
```

This is only a starting decision tree.

---

# 08.56 Practical Pipeline — Edge Detection

```text
input image
   ↓
grayscale / suitable intensity representation
   ↓
optional smoothing
   ↓
compute Gx, Gy
   ↓
magnitude
   ↓
threshold / edge decision
   ↓
edge map
```

The final thresholding stage is a decision step rather than merely a derivative calculation.

---

# 08.57 Border Effects as a Diagnostic

A filtered image may show unexpected border behaviour.

Before blaming the kernel, inspect:

```text
padding mode
kernel anchor
output size
datatype
```

For many enhancement operations, border artifacts are implementation issues rather than properties of the intended filter.

---

# 08.58 Common Traps

## Trap 1 — “Convolution and correlation are always the same.”

False.

They coincide for symmetric kernels under identical boundary handling.

## Trap 2 — “Any blur removes only noise.”

False.

It can remove useful fine detail too.

## Trap 3 — “Sobel directly gives an edge map.”

Not necessarily.

It gives directional gradient responses. Thresholding and additional processing may be needed to form a binary edge map.

## Trap 4 — “Derivative filters are safe on noisy images.”

False.

Differentiation can amplify high-frequency noise.

## Trap 5 — “Kernel coefficients must sum to 1.”

Not always.

Averaging/low-pass kernels often do; derivative and sharpening kernels generally do not.

## Trap 6 — “A negative filter response is an invalid result.”

False.

Derivative filters naturally produce signed responses.

## Trap 7 — “A larger kernel is always better.”

False.

It increases smoothing or support but may destroy important structure.

---

# 08.59 Exam Formula Sheet

### Linear spatial filter

\[
\boxed{
g(x,y)=
\sum_s\sum_t
w(s,t)f(x-s,y-t)
}
\]

### 2-D convolution

\[
\boxed{
g[m,n]
=
\sum_k\sum_\ell
f[k,\ell]h[m-k,n-\ell]
}
\]

### Gradient

\[
\boxed{
\nabla f=
\left[
f_x,\ f_y
\right]^T
}
\]

### Gradient magnitude

\[
\boxed{
|\nabla f|=
\sqrt{f_x^2+f_y^2}
}
\]

### Gradient direction

\[
\boxed{
\theta=\operatorname{atan2}(f_y,f_x)
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
g=f+k\,m
}
\]

### High-boost

\[
\boxed{
g=Af-f_{\text{blur}},\quad A>1
}
\]

### Output dimension

\[
\boxed{
N_{\text{out}}
=
\left\lfloor
\frac{N+2P-K}{S}
\right\rfloor+1
}
\]

---

# 08.60 Exam-Style Problem — Mean Filter

Given:

\[
P=
\begin{bmatrix}
2&4&6\\
4&8&10\\
6&10&12
\end{bmatrix}
\]

and:

\[
H=
\frac19
\begin{bmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{bmatrix}
\]

calculate the filtered centre value.

### Solution

\[
2+4+6+4+8+10+6+10+12
=
62
\]

Therefore:

\[
g=\frac{62}{9}
\]

\[
\boxed{g\approx6.89}
\]

The output may then need rounding or floating-point preservation depending on the pipeline.

---

# 08.61 Exam-Style Problem — Gradient

Suppose:

\[
G_x=6
\]

and:

\[
G_y=8
\]

Then:

\[
|\nabla f|
=
\sqrt{6^2+8^2}
\]

\[
=\sqrt{36+64}
\]

\[
=\sqrt{100}
\]

\[
\boxed{10}
\]

Gradient direction:

\[
\theta=
\operatorname{atan2}(8,6)
\approx53.13^\circ
\]

The edge orientation is approximately perpendicular to the gradient direction under the idealized local-edge interpretation.

---

# 08.62 Worked Matrix — Laplacian Response

Take:

\[
P=
\begin{bmatrix}
10&10&10\\
10&50&10\\
10&10&10
\end{bmatrix}
\]

and:

\[
H=
\begin{bmatrix}
0&1&0\\
1&-4&1\\
0&1&0
\end{bmatrix}
\]

Then:

\[
g=
10+10-4(50)+10+10
\]

\[
=40-200
\]

\[
\boxed{-160}
\]

The strong signed response reflects strong second-order local variation.

If this is used for sharpening, the sign convention must be combined correctly with the sharpening equation.

---

# 08.63 Engineering Insight — Always Inspect the Intermediate

For an edge pipeline, do not inspect only the final image.

Keep:

```text
input
↓
smoothed image
↓
Gx
↓
Gy
↓
magnitude
↓
thresholded edge map
```

Each stage answers a different debugging question.

For example:

```text
Gx looks correct
Gy looks correct
magnitude wrong
→ magnitude calculation problem

magnitude correct
edge map wrong
→ threshold / post-processing problem
```

This is how mathematical understanding turns into reliable implementation.

---

# 08.64 Cross-Book Bridges

> **C07 BRIDGE**  
> Spatial filtering changes local values; histograms reveal the resulting global intensity distribution.

> **C09 BRIDGE**  
> Noise type determines whether mean, Gaussian, median or other smoothing is appropriate.

> **C10 BRIDGE**  
> Gradient/Laplacian foundations here become the formal edge-detection chapter.

> **C12–C13 BRIDGE**  
> Spatial convolution and frequency-domain multiplication are two views of related linear filtering operations under appropriate assumptions.

> **C14 BRIDGE**  
> Restoration treats blur/noise as a degradation model rather than simply applying a generic enhancement filter.

> **LAB BRIDGE**  
> Implement mean, Gaussian, median, Laplacian and Sobel filtering; record intermediate arrays and output statistics.

> **PRACTICE BRIDGE**  
> Solve kernel arithmetic, convolution/correlation orientation, padding, output-size and gradient problems.

> **EXAM BRIDGE**  
> Be able to write filter equations, calculate a centre output, explain correlation vs convolution, derive gradient magnitude and discuss smoothing/sharpening tradeoffs.

---

# 08.65 Quick Recall

```text
POINT
→ one pixel

SPATIAL FILTER
→ neighbourhood

LOW-PASS
→ smooth / reduce rapid variation

HIGH-PASS
→ emphasize rapid variation

GRADIENT
→ first-order change

LAPLACIAN
→ second-order change

UNSHARP
→ original + scaled detail
```

The essential engineering rule:

> **Keep the working data in a representation that preserves the quantity you are trying to measure.**

---

# 08.66 Chapter Checkpoint

1. Define spatial filtering.
2. What is a kernel?
3. Write the general linear filtering equation.
4. Explain the sliding-window process.
5. Calculate a 3×3 mean-filter output.
6. Why does smoothing reduce high-frequency variation?
7. Compare mean, Gaussian and median filters.
8. Define convolution and correlation.
9. When do convolution and correlation give the same result?
10. Why are boundary conditions necessary?
11. What is the difference between zero, replicate and reflect padding?
12. Derive the standard convolution output-size expression.
13. Explain unsharp masking.
14. Define the image gradient.
15. Calculate gradient magnitude and direction.
16. Why can derivative filters amplify noise?
17. What is the Laplacian?
18. Why must signed filter responses not be blindly converted to uint8?
19. Compare Sobel and Prewitt.
20. Why should intermediate filter outputs be inspected during implementation?

---

# 08.67 Connection Forward

We now have the basic spatial-filter toolkit:

```text
AVERAGE
→ smooth

GAUSSIAN
→ weighted smooth

MEDIAN
→ nonlinear outlier suppression

LAPLACIAN
→ second-order structure

SOBEL / PREWITT
→ directional gradient

UNSHARP / HIGH-BOOST
→ sharpening
```

The next chapters specialize these operations.

```text
C09
SMOOTHING + NOISE REDUCTION

        ↓

C10
SHARPENING + EDGE DETECTION

        ↓

C11
GEOMETRIC TRANSFORMATIONS

        ↓

C12
FOURIER TRANSFORM
```

The conceptual progression remains:

```text
local averaging
→ local derivatives
→ geometric coordinate changes
→ global frequency representation
```
