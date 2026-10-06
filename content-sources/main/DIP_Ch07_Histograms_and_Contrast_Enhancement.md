---
id: "C07"
title: "Histograms and Contrast Enhancement"
layer: "MAIN"
part: "II — Improving the Image"
unit: "II"
version: "1.0"
status: "REFERENCE BUILD"
syllabus_scope:
  - "Histogram processing"
  - "Histogram equalization"
  - "Contrast enhancement"
tags:
  - "CORE"
  - "EXAM"
  - "MATH"
  - "DEEP DIVE"
  - "LAB"
  - "VISUAL"
prerequisites:
  - "C04"
  - "C06"
related:
  - "C08"
  - "C09"
  - "C10"
  - "C15"
  - "C16"
  - "C31"
math:
  - "M05"
  - "M06"
  - "M08"
lab:
  - "LAB-U2-02"
  - "LAB-U2-03"
exam:
  - "EXAM-U2"
practice:
  - "P-C07"
assets:
  - "D-C07-01"
  - "D-C07-02"
  - "D-C07-03"
---

# Chapter 07 — Histograms and Contrast Enhancement

> **Chapter thesis**  
> A histogram converts a two-dimensional image into an intensity-distribution view. By studying how frequently intensity values occur, we can diagnose low contrast, identify saturation, design contrast transformations, and understand histogram equalization as a cumulative-distribution mapping rather than as a mysterious “automatic contrast” button.

**Part II — Improving the Image**  
**Syllabus anchor:** Unit II explicitly includes histogram equalization and spatial-domain enhancement. fileciteturn4file0L36-L40

---

# 07.0 Why Histograms Matter

A pixel matrix tells us:

```text
WHERE each value occurs
```

A histogram tells us:

```text
HOW OFTEN each value occurs
```

That change in viewpoint is powerful.

Consider two images:

```text
Image A
most values concentrated near 40–70

Image B
values spread across 0–255
```

Even before inspecting the images, the histograms tell us that Image A likely has a narrower effective intensity range.

This creates a useful diagnostic loop:

```text
IMAGE
  ↓
HISTOGRAM
  ↓
UNDERSTAND INTENSITY DISTRIBUTION
  ↓
CHOOSE ENHANCEMENT
  ↓
OUTPUT IMAGE
  ↓
RECHECK HISTOGRAM + VISUAL/TASK RESULT
```

---

# 07.1 Definition of an Image Histogram

For a discrete grayscale image with \(L\) possible intensity levels:

\[
r_0,r_1,\ldots,r_{L-1}
\]

the histogram is:

\[
h(r_k)=n_k
\]

where:

- \(r_k\) = the \(k\)-th intensity level,
- \(n_k\) = number of pixels having intensity \(r_k\).

The total number of pixels is:

\[
MN=\sum_{k=0}^{L-1}n_k
\]

for an \(M\times N\) image.

---

# 07.2 Normalized Histogram

A normalized histogram estimates the relative frequency:

\[
p(r_k)=\frac{n_k}{MN}
\]

Therefore:

\[
\sum_{k=0}^{L-1}p(r_k)=1
\]

This turns counts into proportions.

### Example

If an image has:

\[
MN=1000
\]

and 120 pixels have intensity 80, then:

\[
p(80)=\frac{120}{1000}=0.12
\]

So 12% of the pixels have that intensity.

---

# 07.3 Histogram Is Not a Spatial Representation

Two very different images can have the same histogram.

For example:

```text
Image A

██
██


Image B

  █
█ █
  █
```

Their spatial arrangements differ, but if they contain the same number of pixels at each intensity, their grayscale histograms are identical.

Therefore:

> A histogram describes intensity distribution, not spatial arrangement.

This limitation is crucial.

---

# 07.4 Matrix Example — Building a Histogram

Consider the image:

\[
I=
\begin{bmatrix}
0&1&1&2\\
2&2&3&3\\
3&3&3&2\\
1&1&2&0
\end{bmatrix}
\]

There are:

\[
4\times4=16
\]

pixels.

Count each level:

| Intensity | Count |
|---:|---:|
| 0 | 2 |
| 1 | 4 |
| 2 | 5 |
| 3 | 5 |

Check:

\[
2+4+5+5=16
\]

The normalized histogram is:

| Intensity | Count \(n_k\) | Probability \(p(r_k)\) |
|---:|---:|---:|
| 0 | 2 | 0.125 |
| 1 | 4 | 0.250 |
| 2 | 5 | 0.3125 |
| 3 | 5 | 0.3125 |

And:

\[
0.125+0.25+0.3125+0.3125=1
\]

---

# 07.5 Visual Interpretation of Histogram Shapes

Histograms can provide useful qualitative clues.

### Narrow histogram

```text
frequency
  ↑
  │       █████
  │       █████
  │       █████
  └────────────────→ intensity
            small range
```

Possible interpretation:

- low effective contrast,
- scene naturally occupies a small intensity range,
- underexposure or overexposure may be present.

### Broad histogram

```text
frequency
  ↑
  │   █ ███ ███ █ █
  │ ███████████████
  └────────────────→ intensity
          broad range
```

Possible interpretation:

- larger effective contrast range.

But a broad histogram is not automatically a “good” histogram.

---

# 07.6 Dark and Bright Images

A simple heuristic:

### Dark image

Most histogram mass appears toward the lower intensity end.

```text
frequency
  ↑
  │ ███████
  │ █████████
  │ █████
  └────────────────→
   dark          bright
```

### Bright image

Mass shifts toward the upper end.

```text
frequency
  ↑
  │                 ███████
  │             ███████████
  │              █████
  └────────────────→
   dark          bright
```

These are diagnostics, not rigorous exposure metrics.

---

# 07.7 Clipped Histograms

A pile-up near the boundary can indicate clipping.

For example:

```text
█████████
████
█
└────────────────────→
0                   255
```

Large counts at 0 may indicate dark clipping.

Large counts at 255 may indicate bright clipping.

Clipping is important because once values have been clipped during acquisition or processing, the original out-of-range differences may not be recoverable.

---

# 07.8 Contrast

A useful practical interpretation of contrast is the degree to which intensity differences are expressed in the image.

A low-contrast image may have values concentrated in a narrow region:

\[
r_{\min}\ll r_{\max}
\]

relative to the available range.

Contrast enhancement aims to make useful differences more distinguishable.

This connects directly to C06:

```text
C06
point transformation
     ↓
C07
histogram / distribution-guided enhancement
```

---

# 07.9 Histogram Stretching vs Histogram Equalization

These are related but not identical.

### Contrast stretching

Usually uses a deliberately selected mapping such as:

\[
[r_{\min},r_{\max}]
\rightarrow
[s_{\min},s_{\max}]
\]

It is often approximately linear or piecewise linear.

### Histogram equalization

Uses the cumulative distribution of intensities to construct a nonlinear mapping.

A useful summary:

```text
stretching
→ explicitly expand a range

equalization
→ use the histogram/CDF to redistribute intensities
```

---

# 07.10 Cumulative Distribution Function

The normalized histogram probabilities are:

\[
p(r_k)
\]

The cumulative distribution is:

\[
C(r_k)
=
\sum_{j=0}^{k}p(r_j)
\]

This gives the fraction of pixels with intensity less than or equal to \(r_k\).

The CDF is the mathematical engine behind classical histogram equalization.

---

# 07.11 Histogram Equalization

For an \(L\)-level grayscale image, a common discrete mapping is:

\[
s_k
=
(L-1)
\sum_{j=0}^{k}
p(r_j)
\]

or equivalently:

\[
s_k=(L-1)C(r_k)
\]

followed by the required integer conversion.

The exact rounding/flooring convention can vary between textbook presentations and implementations. This MiniBook states the convention whenever a numerical example depends on it.

---

# 07.12 Why Equalization Can Spread Intensities

Suppose many pixels occupy a small input range.

The CDF rises rapidly over that region.

Mapping the CDF to:

\[
0\ldots L-1
\]

therefore expands frequently occupied intensity regions.

Conversely, intensity ranges containing few or no pixels receive less output range.

Conceptually:

```text
input intensity
     ↓
histogram
     ↓
CDF
     ↓
nonlinear mapping
     ↓
output intensity
```

---

# 07.13 Worked Histogram-Equalization Example

Use the earlier 4×4 image:

\[
I=
\begin{bmatrix}
0&1&1&2\\
2&2&3&3\\
3&3&3&2\\
1&1&2&0
\end{bmatrix}
\]

The counts were:

| \(r_k\) | \(n_k\) |
|---:|---:|
| 0 | 2 |
| 1 | 4 |
| 2 | 5 |
| 3 | 5 |

Total:

\[
MN=16
\]

So:

\[
p(r_0)=0.125
\]

\[
p(r_1)=0.25
\]

\[
p(r_2)=0.3125
\]

\[
p(r_3)=0.3125
\]

### CDF

\[
C(0)=0.125
\]

\[
C(1)=0.125+0.25=0.375
\]

\[
C(2)=0.6875
\]

\[
C(3)=1.0
\]

Since:

\[
L=4
\]

we have:

\[
L-1=3
\]

Therefore:

\[
s_0=3(0.125)=0.375
\]

\[
s_1=3(0.375)=1.125
\]

\[
s_2=3(0.6875)=2.0625
\]

\[
s_3=3(1)=3
\]

If we use nearest-integer rounding:

\[
0.375\rightarrow0
\]

\[
1.125\rightarrow1
\]

\[
2.0625\rightarrow2
\]

\[
3\rightarrow3
\]

In this toy example, the mapping happens to preserve the same four codes.

This is an excellent reminder:

> Histogram equalization does not guarantee that every example produces dramatic visible expansion.

The image content and discrete mapping determine the result.

---

# 07.14 A Second Equalization Example

Consider a 4-level image with:

| Intensity | Count |
|---:|---:|
| 0 | 8 |
| 1 | 4 |
| 2 | 2 |
| 3 | 2 |

Total:

\[
16
\]

Probabilities:

\[
0.5,\ 0.25,\ 0.125,\ 0.125
\]

CDF:

\[
0.5,\ 0.75,\ 0.875,\ 1
\]

Mapping with \(L-1=3\):

\[
1.5,\ 2.25,\ 2.625,\ 3
\]

Nearest-integer mapping gives approximately:

\[
2,\ 2,\ 3,\ 3
\]

So the original lower levels become more compressed into a different output arrangement.

Again:

> “Equalization” does not mean “every histogram becomes perfectly flat.”

---

# 07.15 Why the Textbook Histogram Is Not Usually Perfectly Uniform

The continuous theory describes a transformation based on a CDF.

But real digital images have:

- finite pixels,
- discrete levels,
- repeated values,
- integer outputs.

Therefore discrete histogram equalization may produce:

```text
approximately redistributed
```

rather than:

```text
exactly equal count at every level
```

This is an important exam and implementation point.

---

# 07.16 Histogram Equalization Is Global

Classical histogram equalization uses the histogram of the entire image.

Therefore a bright region affects the mapping of a dark region.

That can be useful for global contrast enhancement, but it can also be suboptimal when lighting varies strongly across the image.

This motivates adaptive/local methods.

---

# 07.17 Adaptive Histogram Equalization

> **EXTENSION**

Adaptive histogram equalization divides the image into local regions or tiles and computes local mappings.

Conceptually:

```text
whole image
┌────────┬────────┐
│ tile 1 │ tile 2 │
├────────┼────────┤
│ tile 3 │ tile 4 │
└────────┴────────┘

each region
→ local histogram
→ local mapping
```

This can improve local contrast but may amplify noise.

---

# 07.18 CLAHE

**Contrast Limited Adaptive Histogram Equalization (CLAHE)** adds a mechanism to limit excessive local histogram amplification.

Conceptual pipeline:

```text
image
 ↓
local tiles
 ↓
local histograms
 ↓
clip histogram bins
 ↓
redistribute excess
 ↓
compute local mappings
 ↓
interpolate tile boundaries
 ↓
enhanced image
```

CLAHE is widely used as a practical local-contrast enhancement technique.

> **Course-scope note:** The university syllabus explicitly names histogram equalization, while adaptive methods are an extension for engineering depth. fileciteturn4file0L36-L40

---

# 07.19 Global vs Local Enhancement

| Method | Information used | Strength | Risk |
|---|---|---|---|
| contrast stretch | selected global range | predictable | depends on range choice |
| global histogram equalization | global histogram/CDF | automatic global redistribution | may distort local contrast |
| adaptive equalization | local histograms | improves local structure | can amplify noise |
| CLAHE | local histograms with limiting | stronger control | more parameters/complexity |

---

# 07.20 Histogram Specification / Matching

> **EXTENSION**

Sometimes the target is not simply:

> “spread the histogram.”

Instead, we may want the output to approximate a desired histogram.

This is called histogram specification or matching.

Conceptually:

```text
input histogram
      ↓
input CDF
      ↓
mapping
      ↓
target distribution
```

This is useful when a desired statistical appearance must be approximated.

---

# 07.21 Histogram Statistics

A histogram can support simple numerical descriptors.

### Mean intensity

\[
\mu=\sum_{k=0}^{L-1}r_kp(r_k)
\]

### Variance

\[
\sigma^2=
\sum_{k=0}^{L-1}
(r_k-\mu)^2p(r_k)
\]

These provide information about:

- average brightness,
- intensity spread.

But they do not fully describe spatial structure.

---

# 07.22 Worked Mean Example

Use:

| \(r_k\) | \(p(r_k)\) |
|---:|---:|
| 0 | 0.25 |
| 1 | 0.50 |
| 2 | 0.25 |

Then:

\[
\mu=
0(0.25)+1(0.50)+2(0.25)
\]

\[
=0+0.5+0.5
\]

\[
\boxed{\mu=1}
\]

So the mean intensity is 1.

---

# 07.23 Worked Variance Example

Using:

\[
\mu=1
\]

we calculate:

\[
\sigma^2
=
(0-1)^2(0.25)
+
(1-1)^2(0.5)
+
(2-1)^2(0.25)
\]

\[
=1(0.25)+0+1(0.25)
\]

\[
\boxed{\sigma^2=0.5}
\]

Standard deviation:

\[
\sigma=\sqrt{0.5}\approx0.707
\]

---

# 07.24 Histogram Interpretation Is Contextual

A histogram alone cannot tell you:

- whether an object is in the left or right side,
- whether an edge exists,
- whether a texture is periodic,
- whether two equal-intensity regions are connected.

Therefore:

```text
histogram
→ global intensity evidence

image matrix
→ spatial evidence
```

A strong DIP workflow uses both.

---

# 07.25 Histogram Enhancement of a Colour Image

There are several possible strategies.

### Option A — Equalize each RGB channel independently

Potential benefit:

```text
per-channel contrast changes
```

Potential problem:

```text
colour balance can shift
```

### Option B — transform a brightness/luma-related component

Potential benefit:

```text
preserve chromatic relationships more directly
```

The exact choice depends on the representation and objective.

> **Engineering rule:** Never assume independent RGB histogram equalization is colour-neutral.

---

# 07.26 Histogram and Clipping

Suppose a transform pushes many values above 255.

After clipping:

```text
260 → 255
270 → 255
300 → 255
```

The output histogram may develop a large spike at 255.

This tells us something important:

> The histogram can diagnose damage caused by range handling, not just describe the original image.

---

# 07.27 Histogram as a Debugging Tool

A robust enhancement experiment should record:

```text
before:
shape
dtype
min/max
mean
histogram

after:
shape
dtype
min/max
mean
histogram
```

This often reveals bugs such as:

- accidental clipping,
- wrong channel processing,
- incorrect normalization,
- integer overflow,
- unexpected conversion.

---

# 07.28 Implementation Logic

A conceptual histogram pipeline:

```text
load grayscale image
       ↓
determine valid intensity domain
       ↓
count occurrences
       ↓
normalize if required
       ↓
compute CDF
       ↓
construct transformation
       ↓
map pixels
       ↓
evaluate output
```

For global histogram equalization:

```text
histogram
→ normalized histogram
→ cumulative sum
→ scale by L−1
→ round/convert
→ lookup/mapping
```

---

# 07.29 Why Histogram Equalization Is Not “Free Detail”

Histogram equalization cannot create information that was never captured.

If the original image has:

```text
blur
+
sampling loss
+
clipping
```

equalization cannot reconstruct the missing details.

It only remaps existing intensity information.

This distinction is essential:

```text
enhancement
≠
information recovery
```

That leads later to restoration.

---

# 07.30 Enhancement vs Restoration

### Enhancement

Goal:

```text
make image more useful
```

Method may be subjective/task-driven.

### Restoration

Goal:

```text
estimate an image degraded by a known/assumed degradation process
```

Method is usually model-driven.

This distinction becomes central in C14.

---

# 07.31 Practical Example — Unevenly Lit Document

Suppose a scanned page has:

```text
bright center
dark corners
```

Global equalization may improve overall contrast, but it cannot fully solve spatially varying illumination.

A better pipeline might be:

```text
estimate background illumination
        ↓
correct illumination
        ↓
enhance contrast
        ↓
threshold/segment
```

The right solution depends on the actual degradation and objective.

---

# 07.32 Practical Example — Low-Contrast X-Ray-Like Image

For a medical-style grayscale image, enhancement may reveal useful structures, but:

> visual enhancement should not be confused with diagnostic validity.

The processing pipeline should preserve provenance and avoid implying that enhancement created clinically meaningful evidence that was not present.

This illustrates the broader engineering principle of responsible image processing.

---

# 07.33 Common Traps

## Trap 1 — “Histogram tells me where objects are.”

False.

It discards spatial arrangement.

## Trap 2 — “Equalization makes every histogram perfectly flat.”

False for discrete digital images.

## Trap 3 — “Histogram equalization creates detail.”

False.

It remaps existing intensity information.

## Trap 4 — “A wide histogram always means a better image.”

False.

Noise and saturation can also create broad distributions.

## Trap 5 — “Equalizing RGB channels is always safe.”

False.

It can alter colour relationships.

## Trap 6 — “CLAHE is just stronger histogram equalization.”

Incomplete.

It uses local tiles and contrast limiting, with additional processing considerations.

---

# 07.34 Exam Formula Sheet

### Histogram

\[
\boxed{h(r_k)=n_k}
\]

### Normalized histogram

\[
\boxed{p(r_k)=\frac{n_k}{MN}}
\]

### Probability sum

\[
\boxed{\sum_{k=0}^{L-1}p(r_k)=1}
\]

### CDF

\[
\boxed{
C(r_k)=\sum_{j=0}^{k}p(r_j)
}
\]

### Histogram equalization

\[
\boxed{
s_k=(L-1)C(r_k)
}
\]

under the stated classical discrete convention.

### Mean

\[
\boxed{
\mu=\sum_k r_kp(r_k)
}
\]

### Variance

\[
\boxed{
\sigma^2=\sum_k(r_k-\mu)^2p(r_k)
}
\]

---

# 07.35 Exam-Style Problem

### Problem

An image has \(256\) pixels and four intensity levels:

| Intensity | Count |
|---:|---:|
| 0 | 64 |
| 1 | 64 |
| 2 | 64 |
| 3 | 64 |

Find the normalized histogram and the equalization mapping under:

\[
s_k=3C(r_k)
\]

### Solution

Each probability is:

\[
\frac{64}{256}=0.25
\]

So:

\[
p=[0.25,0.25,0.25,0.25]
\]

CDF:

\[
C=[0.25,0.50,0.75,1]
\]

Therefore:

\[
s=[0.75,1.5,2.25,3]
\]

After the specified integer mapping convention, the output levels must be converted appropriately.

### Interpretation

The input is already uniformly distributed, so histogram equalization does not have a strong reason to redistribute it dramatically.

---

# 07.36 Cross-Book Bridges

> **C06 BRIDGE**  
> Point transformations provide the direct mapping viewpoint. Histogram methods provide a distribution-aware viewpoint.

> **C08 BRIDGE**  
> Filtering changes local values and therefore changes the histogram indirectly.

> **LAB BRIDGE**  
> Plot before/after histograms for negative, contrast stretching, global equalization and CLAHE.

> **PRACTICE BRIDGE**  
> Calculate histogram counts, probabilities, CDF, mean, variance and equalization mappings.

> **EXAM BRIDGE**  
> Histogram definition, normalized histogram, CDF, equalization algorithm and numerical mapping are core exam material.

---

# 07.37 Quick Recall

```text
Histogram
→ how often each intensity occurs

Normalized histogram
→ probability distribution

CDF
→ cumulative probability

Equalization
→ map CDF to output intensity range

Contrast stretching
→ expand selected intensity interval
```

Core warning:

> **A histogram is global intensity evidence, not spatial understanding.**

---

# 07.38 Chapter Checkpoint

1. Define an image histogram.
2. Differentiate histogram counts and normalized histogram.
3. Why can two different images have the same histogram?
4. How can a histogram indicate a dark image?
5. What can spikes at 0 or 255 suggest?
6. Define the cumulative distribution function.
7. Derive the classical histogram-equalization mapping.
8. Why may the equalized histogram not be perfectly uniform?
9. What is the difference between contrast stretching and histogram equalization?
10. Why can local histogram methods amplify noise?
11. Why can equalizing RGB channels alter colour?
12. Why can histogram equalization not restore information lost through clipping or blur?

---

# 07.39 Connection Forward

C06 gave us:

```text
ONE PIXEL
→
intensity transformation
```

C07 added:

```text
WHOLE IMAGE INTENSITY DISTRIBUTION
→
histogram-based mapping
```

Now we need to bring **neighbourhood information** into the operation.

That is Chapter 08:

```text
PIXEL
+
NEIGHBOURS
→
SPATIAL FILTERING
→
CONVOLUTION
→
SMOOTHING / SHARPENING
```
