---
id: "C06"
title: "Point Processing and Intensity Transformations"
layer: "MAIN"
part: "II — Improving the Image"
unit: "II"
version: "1.0"
status: "REFERENCE BUILD"
syllabus_scope:
  - "Spatial-domain enhancement"
  - "Intensity transformations"
  - "Point processing"
tags:
  - "CORE"
  - "EXAM"
  - "MATH"
  - "DEEP DIVE"
  - "LAB"
  - "ENHANCEMENT"
prerequisites:
  - "C04"
  - "C05"
related:
  - "C07"
  - "C08"
  - "C09"
  - "C10"
  - "C14"
math:
  - "M05"
  - "M06"
  - "M08"
lab:
  - "LAB-U2-01"
  - "LAB-U2-02"
exam:
  - "EXAM-U2"
practice:
  - "P-C06"
assets:
  - "D-C06-01"
  - "D-C06-02"
  - "D-C06-03"
---

# Chapter 06 — Point Processing and Intensity Transformations

> **Chapter thesis**  
> The simplest image-enhancement operation changes each pixel according to a transformation that depends only on that pixel's current value. By choosing the transformation carefully, we can brighten, darken, invert, expand contrast, compress dynamic range or emphasize selected intensity intervals.

**Part II — Improving the Image**  
**Syllabus anchor:** Unit II includes spatial-domain enhancement and the associated enhancement operations developed through filtering and histogram methods. fileciteturn4file0L36-L40

---

# 06.0 Why Start with Point Processing?

Before filtering neighbourhoods, Fourier transforms or segmentation, we should master the simplest possible image transformation.

For every pixel:

\[
r\rightarrow s
\]

where:

- \(r\) = input intensity,
- \(s\) = output intensity.

More formally:

\[
s=T(r)
\]

The output of one pixel depends only on its own input value.

```text
INPUT PIXEL
     │
     ▼
 TRANSFORM T
     │
     ▼
OUTPUT PIXEL
```

There is no neighbourhood yet.

That is what makes point processing such a powerful foundation.

---

# 06.1 Point Processing vs Neighbourhood Processing

### Point processing

```text
output at (x,y)
depends on
input at (x,y)
```

Mathematically:

\[
g(x,y)=T(f(x,y))
\]

### Neighbourhood processing

```text
output at (x,y)
depends on
a local set of neighbouring pixels
```

For example:

\[
g(x,y)=
\sum_{s,t}
w(s,t)f(x-s,y-t)
\]

The second category leads to convolution and spatial filtering in Chapter 08.

---

# 06.2 The Intensity Transformation Function

The function:

\[
s=T(r)
\]

maps input intensity values to output intensity values.

An intensity-transform curve is therefore a compact way of describing an image operation.

Conceptually:

```text
output s
  ↑
  │         /
  │       /
  │     /
  │   /
  │ /
  └────────────→ input r
```

Different curves create different visual effects.

---

# 06.3 What Is Enhancement?

Image enhancement modifies an image so that selected features become more useful for:

- human viewing,
- measurement,
- subsequent processing,
- segmentation,
- feature extraction.

Enhancement is task-dependent.

An operation that improves one property may damage another.

For example:

```text
strong sharpening
→ clearer edges
→ also stronger noise
```

Therefore enhancement is an engineering tradeoff, not an objective universal “quality increase.”

---

# 06.4 Identity Transformation

The simplest transformation is:

\[
s=r
\]

Every input intensity stays unchanged.

```text
input
  ↓
identity
  ↓
same image
```

This is useful as a baseline.

Whenever implementing an enhancement method, it is helpful to compare the result against the identity case.

---

# 06.5 Negative Transformation

For an image with:

\[
L
\]

possible intensity levels, the standard image-negative transformation is:

\[
s=(L-1)-r
\]

For an 8-bit image:

\[
L=256
\]

so:

\[
s=255-r
\]

---

# 06.6 Worked Example — Image Negative

Suppose:

\[
r=80
\]

Then:

\[
s=255-80
\]

\[
\boxed{s=175}
\]

For several pixels:

| Input \(r\) | Output \(s=255-r\) |
|---:|---:|
| 0 | 255 |
| 50 | 205 |
| 100 | 155 |
| 150 | 105 |
| 200 | 55 |
| 255 | 0 |

Dark values become bright and bright values become dark.

---

# 06.7 Why Use an Image Negative?

Negative transformation can be useful when details of interest are more visible in the inverted intensity relationship.

A classic conceptual application is displaying structures whose visual interpretation benefits from reversing bright/dark relationships.

The important idea is not:

> “Negative is always better.”

It is:

> “Negative changes the intensity ordering in a controlled way.”

---

# 06.8 Logarithmic Transformation

A common form is:

\[
s=c\log(1+r)
\]

where \(c\) controls scaling.

The log function expands lower input values relative to higher values.

Conceptually:

```text
small r
→ relatively large output change

large r
→ compressed output change
```

This is useful when the input dynamic range is very large and weaker components need greater visibility.

---

# 06.9 Why the \(1+r\)?

If:

\[
r=0
\]

then:

\[
\log(1+r)=\log(1)=0
\]

This avoids the mathematical problem of attempting:

\[
\log(0)
\]

at the zero-intensity point.

---

# 06.10 Worked Log Example

Suppose:

\[
r=9
\]

and:

\[
c=1
\]

Then:

\[
s=\log(1+9)=\log(10)
\]

Using natural logarithm:

\[
s\approx2.303
\]

The numerical value is not yet in an 8-bit display range.

Therefore a practical pipeline often requires normalization/scaling before storing or displaying the result.

> **Engineering trap:** A mathematically valid transformation is not automatically a valid 8-bit image without range handling.

---

# 06.11 Inverse Log / Exponential-Like Transform

An exponential-type transformation has the opposite qualitative behaviour:

```text
small input region
→ compressed

large input region
→ expanded
```

The exact formula depends on the chosen transformation and parameterization.

The important conceptual comparison is:

```text
log transform
→ expands low range, compresses high range

inverse/exponential-type transform
→ can emphasize higher intensities
```

---

# 06.12 Power-Law (Gamma) Transformation

A widely used family is:

\[
s=cr^\gamma
\]

where:

- \(c\) = scaling constant,
- \(\gamma\) = exponent.

This is also called a gamma or power-law transformation in many DIP contexts.

---

# 06.13 Shape of the Power-Law Transform

For normalized:

\[
r\in[0,1]
\]

and \(c=1\):

### If \(0<\gamma<1\)

The curve lies above the identity line:

```text
s
↑
│       ╭────
│     ╭─
│   ╭─
│ ╭─
└────────────→ r
```

Low and mid intensities are expanded.

### If \(\gamma>1\)

The curve lies below the identity line:

```text
s
↑
│        ───╮
│           ╰╮
│            ╰╮
│              ╰
└────────────→ r
```

Low and mid intensities are compressed.

---

# 06.14 Worked Gamma Example

Let:

\[
r=0.25
\]

and:

\[
\gamma=0.5
\]

Then:

\[
s=(0.25)^{0.5}
\]

\[
s=0.5
\]

So a normalized input of 0.25 becomes 0.5.

That is an example of low-range expansion.

---

# 06.15 Scaling a Normalized Result to 8-bit

Suppose:

\[
s=0.5
\]

and we want an 8-bit display value:

\[
s_{8}=255s
\]

Then:

\[
s_8=127.5
\]

Depending on the conversion convention, this may be rounded to:

\[
128
\]

This illustrates why numerical pipelines must specify:

- normalization range,
- output datatype,
- rounding,
- clipping.

---

# 06.16 Contrast Stretching

Suppose the useful input range is:

\[
[r_{\min},r_{\max}]
\]

and we want to map it to:

\[
[s_{\min},s_{\max}]
\]

A linear contrast-stretching transformation is:

\[
s
=
s_{\min}
+
\frac{(r-r_{\min})(s_{\max}-s_{\min})}
{r_{\max}-r_{\min}}
\]

for:

\[
r_{\max}\ne r_{\min}
\]

This expands a narrow intensity range into a wider output range.

---

# 06.17 Worked Contrast-Stretch Example

Suppose an image effectively uses only:

\[
r_{\min}=50
\]

to:

\[
r_{\max}=180
\]

and we want:

\[
s_{\min}=0,\qquad s_{\max}=255
\]

For:

\[
r=100
\]

we get:

\[
s=
\frac{(100-50)(255)}
{180-50}
\]

\[
=
\frac{50\times255}{130}
\]

\[
\approx98.08
\]

After integer conversion, this is approximately:

\[
\boxed{98}
\]

The same input value becomes more separated from the dark end of the output range than in the original narrow range.

---

# 06.18 Why Contrast Stretching Helps

Suppose a dark image occupies only:

```text
50 ........................ 100
```

of a possible 0–255 display range.

The output may look compressed:

```text
████████████████████
```

After stretching:

```text
0 ......................... 255
```

differences can become more visible.

This is especially useful when the recorded image has a narrow effective intensity distribution.

---

# 06.19 Piecewise-Linear Transformation

Not every enhancement should use one straight line.

A piecewise transformation can define different behaviour in different intensity ranges:

```text
output
  ↑
  │             /
  │           /
  │     _____/
  │   /
  │__/
  └──────────────→ input
```

This allows us to:

- suppress one range,
- expand another,
- preserve selected intensities.

---

# 06.20 Example — Highlighting a Target Range

Suppose the useful feature occurs in:

\[
[100,150]
\]

A piecewise mapping could:

```text
0–99
→ keep dark

100–150
→ expand strongly

151–255
→ compress
```

Conceptually:

```text
input range
────────┬────────────┬────────
        100         150
         ↑ target ↑
```

This is useful for selective enhancement.

---

# 06.21 Thresholding as an Extreme Point Transform

A binary threshold can be written:

\[
s=
\begin{cases}
0,&r<T\\
255,&r\ge T
\end{cases}
\]

for a conventional binary 8-bit output.

This is technically a point transformation because the output depends only on the individual pixel value.

However, in this MiniBook it is treated fully in the segmentation section because the **goal and interpretation** are different.

That distinction prevents overlap:

```text
C06
→ transformation mechanics

C16
→ segmentation meaning and threshold selection
```

---

# 06.22 Clipping

Suppose transformed values fall outside the valid output range.

For an 8-bit unsigned image:

\[
0\le s\le255
\]

A simple clipping operation is:

\[
s_{\text{clip}}=
\min(255,\max(0,s))
\]

### Example

If:

\[
s=-10
\]

then:

\[
s_{\text{clip}}=0
\]

If:

\[
s=280
\]

then:

\[
s_{\text{clip}}=255
\]

---

# 06.23 Clipping Is Not the Same as Rescaling

Suppose:

```text
values = [-20, 50, 300]
```

### Clipping

```text
[-20, 50, 300]
      ↓
[0, 50, 255]
```

### Rescaling

The values are mapped relatively into a chosen output interval.

These operations have different effects.

> **Engineering trap:** Blind clipping can destroy relative information outside the valid range.

---

# 06.24 Point Processing as a Lookup Table

For discrete intensity values, a transformation can be implemented as a lookup table.

For an 8-bit image:

```text
input:
0 ... 255

LUT:
T(0) ... T(255)
```

Then every pixel is replaced using:

\[
s=T(r)
\]

This is computationally efficient.

Conceptually:

```text
pixel value
    ↓
lookup index
    ↓
transformed value
```

This technique is useful for real-time and repeated transformations.

---

# 06.25 Matrix Example — Point Transformation

Consider:

\[
I=
\begin{bmatrix}
10&20&30\\
40&50&60\\
70&80&90
\end{bmatrix}
\]

Apply:

\[
s=100-r
\]

Then:

\[
O=
\begin{bmatrix}
90&80&70\\
60&50&40\\
30&20&10
\end{bmatrix}
\]

Notice:

> each output pixel was computed independently.

No neighbourhood was needed.

---

# 06.26 Matrix Example — Threshold

For:

\[
T=50
\]

using:

\[
s=
\begin{cases}
0,&r<50\\
255,&r\ge50
\end{cases}
\]

the same matrix becomes:

\[
O=
\begin{bmatrix}
0&0&0\\
0&255&255\\
255&255&255
\end{bmatrix}
\]

The spatial pattern remains, but the intensity representation has been drastically simplified.

---

# 06.27 Point Processing and Histograms

Point transformations change the intensity values and therefore change the image histogram.

For example:

```text
contrast stretching
→ spreads histogram

negative
→ reverses intensity ordering

threshold
→ collapses values into a few levels
```

This is why histogram analysis is the natural next chapter.

---

# 06.28 Enhancement Function Selection

A useful decision table:

| Problem | Candidate transformation | Main effect |
|---|---|---|
| image too dark | gamma with \(\gamma<1\), suitable scaling | expand lower intensities |
| image too bright | gamma with \(\gamma>1\), suitable scaling | suppress lower/mid intensities |
| narrow intensity range | contrast stretch | expand useful range |
| need inversion | negative | reverse intensity ordering |
| very wide dynamic range | log-type transform | compress high values, expand low values |
| isolate intensity class | threshold / piecewise mapping | separate target range |

These are starting points, not automatic prescriptions.

---

# 06.29 Worked Comparison

Suppose two pixels have:

\[
r_1=50,\qquad r_2=100
\]

Under a negative transformation:

\[
s_1=255-50=205
\]

\[
s_2=255-100=155
\]

Under contrast stretching, their outputs depend on the image's global \(r_{\min},r_{\max}\).

Under a gamma transformation, their outputs depend on:

\[
c,\gamma
\]

Therefore an enhancement cannot be selected from the pixel value alone.

The function and its parameters define the behaviour.

---

# 06.30 Colour Images and Point Processing

A point transformation can be applied:

### Per channel

\[
R'=T(R),\quad
G'=T(G),\quad
B'=T(B)
\]

But this can alter colour relationships.

For example, applying a strong nonlinear function independently to each RGB channel can change saturation and hue.

### On a luminance/luma-like component

An alternative is to transform a brightness-related component while preserving chromatic information more directly.

This depends on the colour representation and application.

> **Engineering Insight:** Point processing on RGB is not automatically colour-safe.

---

# 06.31 Example — Why Independent RGB Enhancement Can Change Colour

Suppose:

\[
(R,G,B)=(100,100,200)
\]

The blue component is stronger than red and green.

Now imagine applying different channel transforms:

\[
R'=0.8R
\]

\[
G'=1.2G
\]

\[
B'=0.9B
\]

Then:

\[
(R',G',B')=(80,120,180)
\]

The relative channel balance changed.

Therefore the perceived colour can change even though the operation was intended as “brightness enhancement.”

This is one reason colour processing often requires deliberate colour-space selection.

---

# 06.32 Dynamic Range Compression vs Contrast Enhancement

These ideas can appear contradictory.

### Contrast enhancement

```text
spread selected intensity differences
→ make differences more visible
```

### Dynamic-range compression

```text
fit very large values into a smaller range
→ prevent extreme values from dominating
```

A logarithmic transform can compress a huge range while simultaneously making weaker signals more visible.

Thus:

> “Enhancement” is about task usefulness, not simply increasing every numerical difference.

---

# 06.33 Noise Interaction

Point transformations also modify noise.

Suppose:

\[
g=f+\eta
\]

and we apply:

\[
s=T(g)
\]

For nonlinear \(T\), the noise is generally transformed nonlinearly as well.

Therefore:

```text
enhancement
→ can make desired details clearer
→ can also make noise more visible
```

This motivates more careful smoothing/restoration methods later.

---

# 06.34 Quantization Interaction

Remember C03.

A transformation may produce floating-point values that are then mapped back to finite levels.

For example:

```text
float result
   ↓
normalize
   ↓
clip
   ↓
round
   ↓
uint8
```

Each step can introduce additional numerical effects.

A correct algorithm therefore specifies the entire value pipeline.

---

# 06.35 Implementation Pattern

A robust point-processing implementation conceptually looks like:

```text
load image
     ↓
inspect datatype/range
     ↓
convert to a safe working representation
     ↓
apply T(r)
     ↓
handle range
     ↓
clip/normalize as required
     ↓
convert to destination datatype
     ↓
visualize and evaluate
```

Never assume the library will make the scientifically intended choice automatically.

---

# 06.36 Pseudocode

```text
INPUT image I

inspect:
    shape
    channels
    datatype
    min/max

convert to working representation

for each pixel value r:
    s = T(r)

apply intended range handling

convert to output representation

return output
```

For a lookup-table implementation:

```text
construct LUT[k] = T(k)

for each pixel r:
    output = LUT[r]
```

when the source domain is a suitable discrete integer range.

---

# 06.37 Engineering Example — Improving a Dark Image

Suppose an image has values concentrated around:

\[
20\le r\le90
\]

Possible first choices:

```text
contrast stretching
or
gamma < 1
```

A good workflow is:

```text
inspect histogram
       ↓
identify useful range
       ↓
choose transformation
       ↓
apply
       ↓
compare before/after
       ↓
check noise and clipping
```

Do not apply a transformation only because it is famous.

---

# 06.38 Evaluation: How Do We Know It Helped?

Possible checks:

### Visual

- Is the target structure more visible?
- Did colours change unexpectedly?
- Was noise amplified?

### Numerical

- Did dynamic range increase?
- Did saturation/clipping increase?
- How did the histogram change?

### Downstream

- Did segmentation improve?
- Did feature extraction improve?
- Did a classifier perform better?

The correct evaluation depends on the task.

---

# 06.39 Common Traps

## Trap 1 — “Enhancement always improves the image.”

False.

Enhancement is task-dependent.

## Trap 2 — “Log transformation simply brightens the image.”

Incomplete.

It compresses high intensities and expands lower intensities relative to the input scale.

## Trap 3 — “Gamma less than 1 always gives a brighter image.”

Only under a suitable normalized positive-domain formulation and output scaling.

The exact implementation matters.

## Trap 4 — “Contrast stretching cannot lose information.”

False.

It can involve clipping or datatype conversion, and extreme values may be affected depending on implementation.

## Trap 5 — “Point processing uses neighbouring pixels.”

False.

By definition, each output depends only on the corresponding input value for a pure point transform.

## Trap 6 — “Applying the same formula independently to RGB preserves colour.”

Not necessarily.

Relative channel relationships can change.

## Trap 7 — “Mathematically computed values can always be stored directly.”

False.

The output datatype and range may require scaling, clipping or conversion.

---

# 06.40 Exam Formula Sheet

### General point transformation

\[
\boxed{s=T(r)}
\]

### Negative

\[
\boxed{s=(L-1)-r}
\]

### Log

\[
\boxed{s=c\log(1+r)}
\]

### Power-law

\[
\boxed{s=cr^\gamma}
\]

### Linear contrast stretch

\[
\boxed{
s=
s_{\min}
+
\frac{(r-r_{\min})(s_{\max}-s_{\min})}
{r_{\max}-r_{\min}}
}
\]

### 8-bit clipping

\[
\boxed{
s_{\text{clip}}=\min(255,\max(0,s))
}
\]

---

# 06.41 Worked Exam-Style Problem

### Problem

An 8-bit grayscale image has useful intensity values between 40 and 160. Map this range linearly to 0–255. Find the output for input intensity 100.

### Given

\[
r_{\min}=40
\]

\[
r_{\max}=160
\]

\[
s_{\min}=0
\]

\[
s_{\max}=255
\]

\[
r=100
\]

### Formula

\[
s=
0+
\frac{(100-40)(255)}
{160-40}
\]

\[
=
\frac{60\times255}{120}
\]

\[
=127.5
\]

After a specified integer conversion, approximately:

\[
\boxed{128}
\]

### Interpretation

The midpoint of the original useful range maps to the midpoint of the target range.

---

# 06.42 Deep Concept — Transformations as Functions on a Histogram

A point transformation does not use spatial relationships.

Therefore it can be studied partly through the intensity distribution.

Conceptually:

```text
input histogram
      ↓
mapping T(r)
      ↓
output histogram
```

This gives an important connection:

```text
C06
point transformations

        ↓

C07
histogram-based enhancement
```

The next chapter therefore moves from:

```text
pixel-by-pixel mapping
```

to:

```text
distribution-aware enhancement
```

---

# 06.43 Cross-Book Bridges

> **C03 BRIDGE**  
> Quantization and datatype constraints determine how transformed values are stored.

> **C05 BRIDGE**  
> Colour-space choice determines whether the transformation acts directly on RGB channels or on another representation.

> **C07 BRIDGE**  
> Histograms provide a distribution-level view of intensity transformation.

> **C08 BRIDGE**  
> Spatial filters extend the idea from one-pixel functions to neighbourhood-dependent operations.

> **LAB BRIDGE**  
> Implement negative, log, gamma and contrast-stretch transformations and compare their histograms.

> **PRACTICE BRIDGE**  
> Solve transformation calculations and diagnose enhancement failures.

> **EXAM BRIDGE**  
> Memorize formulas, but also understand when each transformation is useful and what information it can distort.

---

# 06.44 Quick Recall

```text
Point processing:
g(x,y)=T(f(x,y))

Negative:
s=(L-1)-r

Log:
s=c log(1+r)

Gamma:
s=c r^γ

Contrast stretch:
map [rmin,rmax] → [smin,smax]
```

Core questions:

```text
What does T(r) do?
Why was it chosen?
What happens to the histogram?
What happens to noise?
What happens to datatype/range?
Does it actually improve the task?
```

---

# 06.45 Chapter Checkpoint

1. Define point processing.
2. Write the general point-processing equation.
3. Differentiate point processing from neighbourhood processing.
4. Derive the negative transformation for an \(L\)-level image.
5. Apply a log transform to a specified value.
6. Explain the effect of \(0<\gamma<1\) versus \(\gamma>1\).
7. Derive and apply a linear contrast-stretch formula.
8. Why might clipping be necessary?
9. Why is clipping different from rescaling?
10. What is a lookup table and why is it useful?
11. Why can independent RGB enhancement alter colour?
12. Explain why an enhancement method should be evaluated against the downstream task.

---

# 06.46 Part II Opening Map

```text
C06
POINT PROCESSING
      ↓
C07
HISTOGRAMS + CONTRAST
      ↓
C08
SPATIAL FILTERING + CONVOLUTION
      ↓
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
      ↓
C13
FREQUENCY-DOMAIN FILTERING
      ↓
C14
RESTORATION + DEBLURRING
```

The central progression is:

```text
ONE PIXEL
→
NEIGHBOURHOOD
→
WHOLE IMAGE DISTRIBUTION
→
FREQUENCY CONTENT
→
DEGRADED-IMAGE MODEL
```

That progression is one of the core intellectual structures of Digital Image Processing.
