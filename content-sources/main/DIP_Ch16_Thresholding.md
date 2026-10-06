---
id: "C16"
title: "Thresholding"
layer: "MAIN"
part: "III — Understanding Image Content"
unit: "III"
version: "1.0"
status: "REFERENCE BUILD"
syllabus_scope:
  - "Global thresholding"
  - "Adaptive thresholding"
tags:
  - "CORE"
  - "EXAM"
  - "MATH"
  - "DEEP DIVE"
  - "LAB"
  - "SEGMENTATION"
  - "OTSU"
  - "ADAPTIVE"
prerequisites:
  - "C06"
  - "C07"
  - "C15"
related:
  - "C17"
  - "C18"
  - "C19"
  - "C25"
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
  - "P-C16"
assets:
  - "D-C16-01"
  - "D-C16-02"
  - "D-C16-03"
---

# Chapter 16 — Thresholding

> **Chapter thesis**  
> Thresholding is a segmentation strategy that converts image values into labels by comparing them with one or more thresholds. Its apparent simplicity hides an important design problem: **choosing a threshold that separates the desired populations under the image's illumination, noise, contrast and class-overlap conditions.**

**Part III — Understanding Image Content**  
**Syllabus anchor:** Unit III explicitly includes global thresholding and adaptive thresholding. fileciteturn4file0L41-L45

---

# 16.0 Why Thresholding Matters

Thresholding is one of the most important classical segmentation tools because it is:

```text
simple
fast
interpretable
easy to implement
```

The core operation is:

\[
f(x,y)\xrightarrow{\text{threshold}}\text{label}
\]

For a binary mask:

\[
M(x,y)=
\begin{cases}
1,&f(x,y)\ge T\\
0,&f(x,y)<T
\end{cases}
\]

But the hard problem is:

\[
\boxed{\text{How do we choose }T?}
\]

---

# 16.1 Global Thresholding

A **global threshold** uses one value \(T\) for the entire image.

```text
all pixels
    ↓
same T
    ↓
foreground / background
```

This works best when:

- illumination is reasonably uniform,
- foreground/background intensities are separated,
- the histogram is informative.

---

# 16.2 Worked Global Threshold

Given:

\[
I=
\begin{bmatrix}
20&30&40\\
100&120&150\\
180&200&220
\end{bmatrix}
\]

Use:

\[
T=100
\]

with foreground defined as:

\[
I\ge100
\]

Then:

\[
M=
\begin{bmatrix}
0&0&0\\
1&1&1\\
1&1&1
\end{bmatrix}
\]

Foreground area:

\[
6
\]

pixels.

This is a direct pixel-level decision.

---

# 16.3 Threshold Direction Matters

The segmentation can instead be:

\[
M(x,y)=
\begin{cases}
1,&f(x,y)<T\\
0,&f(x,y)\ge T
\end{cases}
\]

This is useful when the foreground is darker than the background.

Therefore:

```text
THRESHOLD VALUE
+
THRESHOLD POLARITY
```

both matter.

---

# 16.4 Binary, Multi-Level and Range Thresholding

### Binary threshold

One threshold:

\[
T
\]

### Multi-level thresholding

Multiple thresholds:

\[
T_1<T_2<\cdots<T_K
\]

### Range threshold

Accept values within:

\[
T_{\min}\le f<T_{\max}
\]

Range thresholding is especially useful when the desired class occupies a middle intensity band.

---

# 16.5 Worked Range Threshold

Suppose:

\[
40\le f<80
\]

is the target range.

For:

\[
I=
\begin{bmatrix}
20&50&90\\
45&70&100\\
30&60&85
\end{bmatrix}
\]

the mask is:

\[
M=
\begin{bmatrix}
0&1&0\\
1&1&0\\
0&1&0
\end{bmatrix}
\]

This selects a middle intensity band rather than everything above a single threshold.

---

# 16.6 Histogram-Guided Threshold Selection

A histogram can reveal whether two populations are approximately separable.

A common ideal pattern is bimodal:

```text
frequency
  ↑
  │    /\             /\
  │   /  \           /  \
  │__/    \_________/    \__
  └────────────────────────→ intensity
              ↑
           possible T
```

The valley between the modes can be a candidate threshold.

But this heuristic can fail with:

- overlapping distributions,
- uneven illumination,
- skewed classes,
- noise,
- shadows.

---

# 16.7 Why Histogram Shape Alone Is Not Enough

Suppose foreground occupies only 5% of pixels.

Its histogram peak may be small.

A simple valley heuristic can therefore choose an inappropriate threshold.

Likewise, two spatially distinct objects can have overlapping intensity distributions.

The histogram does not know where the pixels are.

---

# 16.8 Manual Threshold Selection

The simplest method is:

```text
inspect image
→ inspect histogram
→ choose T
→ evaluate mask
→ adjust T
```

Advantages:

- easy,
- interpretable,
- useful for controlled laboratory images.

Disadvantages:

- subjective,
- difficult to scale,
- sensitive to image changes.

---

# 16.9 Iterative Threshold Selection

> **EXTENSION**

One classical approach starts with an initial threshold and repeatedly updates it.

Conceptually:

```text
initial T
 ↓
split image into two groups
 ↓
compute group means
 ↓
update T
 ↓
repeat until stable
```

A common update is:

\[
T_{\text{new}}
=
\frac{\mu_1+\mu_2}{2}
\]

where \(\mu_1,\mu_2\) are the means of the two classes induced by the current threshold.

---

# 16.10 Worked Iterative Threshold Example

Suppose current threshold produces two groups with means:

\[
\mu_1=50
\]

and:

\[
\mu_2=150
\]

Then:

\[
T_{\text{new}}
=
\frac{50+150}{2}
=
\boxed{100}
\]

Reapply at \(T=100\), recompute the class means and continue until the threshold stabilizes.

This is one form of iterative thresholding.

---

# 16.11 Otsu's Method

Otsu's method chooses a threshold by maximizing the separation between two classes in terms of between-class variance.

For a threshold \(t\), define:

\[
w_0(t),\quad w_1(t)
\]

as class probabilities.

Class means:

\[
\mu_0(t),\quad\mu_1(t)
\]

Overall mean:

\[
\mu_T
\]

The between-class variance is:

\[
\sigma_B^2(t)
=
w_0(t)w_1(t)
[\mu_0(t)-\mu_1(t)]^2
\]

Otsu selects:

\[
\boxed{
t^*=
\arg\max_t
\sigma_B^2(t)
}
\]

---

# 16.12 Why Otsu Works Intuitively

A good threshold should create two groups with:

```text
high within-group similarity
+
large separation between group means
```

Otsu formalizes this using between-class variance.

A visually useful mental model is:

```text
good split
→ compact classes
→ far-separated means
```

---

# 16.13 Otsu's Method Step-by-Step

For each candidate threshold \(t\):

```text
1. split histogram into class 0 and class 1
2. compute class probabilities
3. compute class means
4. calculate between-class variance
5. store score
```

Choose the threshold with the maximum score.

This can be done efficiently using cumulative histogram statistics.

---

# 16.14 Otsu Worked Example

Consider four intensity levels:

| \(r\) | probability |
|---:|---:|
| 0 | 0.25 |
| 1 | 0.25 |
| 2 | 0.25 |
| 3 | 0.25 |

Evaluate threshold after level 1:

Class 0:

```text
0,1
```

\[
w_0=0.5
\]

\[
\mu_0=\frac{0(0.25)+1(0.25)}{0.5}=0.5
\]

Class 1:

```text
2,3
```

\[
w_1=0.5
\]

\[
\mu_1=\frac{2(0.25)+3(0.25)}{0.5}=2.5
\]

Then:

\[
\sigma_B^2
=
(0.5)(0.5)(0.5-2.5)^2
\]

\[
=
0.25(4)
\]

\[
\boxed{1}
\]

This is a candidate score. Other thresholds can be evaluated and compared.

---

# 16.15 Otsu Limitations

Otsu often works well for approximately bimodal histograms.

It can struggle when:

- class sizes are extremely unequal,
- illumination varies spatially,
- classes overlap strongly,
- more than two classes exist,
- noise distorts the histogram.

Therefore:

> Otsu is a statistical threshold selector, not a universal segmentation algorithm.

---

# 16.16 Multi-Level Otsu

> **EXTENSION**

Otsu's idea can be extended to multiple classes using multiple thresholds.

For:

\[
T_1<T_2
\]

we can create:

```text
class 0: f < T1
class 1: T1 ≤ f < T2
class 2: f ≥ T2
```

The optimization becomes more expensive as the number of thresholds grows.

---

# 16.17 Adaptive Thresholding

A global threshold assumes:

```text
one T works everywhere
```

Adaptive thresholding instead computes a local threshold:

\[
T(x,y)
\]

The decision becomes:

\[
M(x,y)=
\begin{cases}
1,&f(x,y)\ge T(x,y)\\
0,&f(x,y)<T(x,y)
\end{cases}
\]

This is useful when illumination varies across the image.

---

# 16.18 Local Mean Threshold

A simple adaptive method computes a local mean:

\[
\mu_L(x,y)
\]

and defines:

\[
T(x,y)=\mu_L(x,y)-C
\]

where \(C\) is an offset.

The exact sign and formula vary by implementation.

The key idea is:

```text
threshold follows local brightness
```

---

# 16.19 Worked Adaptive Threshold Example

Suppose a local 3×3 neighbourhood has mean:

\[
\mu_L=120
\]

and:

\[
C=10
\]

Then:

\[
T=120-10=110
\]

For a pixel with:

\[
f=115
\]

the pixel is classified as foreground under:

\[
f\ge T
\]

because:

\[
115\ge110
\]

---

# 16.20 Adaptive Gaussian Threshold

Instead of an equally weighted local mean, we can use a Gaussian-weighted average:

\[
\mu_G(x,y)
=
\sum_{s,t}w_G(s,t)f(x-s,y-t)
\]

with:

\[
\sum_{s,t}w_G(s,t)=1
\]

Then:

\[
T(x,y)=\mu_G(x,y)-C
\]

This gives nearby pixels greater influence.

---

# 16.21 Global vs Adaptive Thresholding

| Property | Global | Adaptive |
|---|---|---|
| threshold | one \(T\) | \(T(x,y)\) |
| assumption | roughly uniform illumination | local variation allowed |
| complexity | lower | higher |
| strength | simple, interpretable | handles uneven lighting better |
| risk | failure under illumination gradients | parameter sensitivity/noise amplification |

---

# 16.22 Adaptive Threshold Failure

Adaptive thresholding is not automatically superior.

It can produce:

```text
local false positives
fragmented objects
noise-driven regions
halo-like boundaries
```

when the window is:

- too small,
- too large,
- too sensitive.

Parameter selection remains important.

---

# 16.23 Window Size Matters

A local threshold uses a neighbourhood/window.

### Small window

```text
high local sensitivity
+
noise sensitivity
```

### Large window

```text
more stable
+
less responsive to local illumination
```

This creates a scale tradeoff.

---

# 16.24 Worked Window-Size Thought Experiment

Consider a page with slowly varying illumination.

A:

```text
3×3
```

window may respond strongly to individual letters and noise.

A:

```text
51×51
```

window can estimate broader background illumination more smoothly.

The appropriate size should relate to:

```text
object stroke scale
+
illumination variation scale
+
noise scale
```

---

# 16.25 Sauvola-Style Thresholding

> **EXTENSION**

Document binarization often uses local mean and local standard deviation.

A representative formula is:

\[
T(x,y)
=
m(x,y)
\left[
1+k
\left(
\frac{s(x,y)}{R}-1
\right)
\right]
\]

where:

- \(m\) = local mean,
- \(s\) = local standard deviation,
- \(R\) = dynamic-range/reference constant,
- \(k\) = parameter.

This is a more statistics-aware local threshold.

It is especially useful for difficult document backgrounds.

---

# 16.26 Why Variance Helps

A region with:

```text
low mean
+
low variance
```

may represent a blank background.

A region with:

```text
similar mean
+
high local variance
```

may contain text or texture.

Thus local variance can provide information that the mean alone misses.

---

# 16.27 Thresholding and Colour

Thresholding is not restricted to grayscale.

You can threshold:

```text
R
G
B
H
S
V
luma
colour distance
```

The representation matters.

For coloured objects, a threshold in HSV may be much easier to tune than one on a grayscale image.

---

# 16.28 Example — Hue Range Threshold

Suppose a target object has hue around:

\[
H\in[350^\circ,10^\circ]
\]

because hue wraps around.

A correct red mask needs two intervals:

\[
H\ge350^\circ
\]

or:

\[
H\le10^\circ
\]

This is a classic thresholding edge case.

---

# 16.29 Thresholding and Noise

Noise near the threshold can flip labels:

```text
value just below T
→ background

value just above T
→ foreground
```

A small perturbation can therefore change a pixel's class.

This is why:

```text
denoise
+
threshold
```

can often outperform:

```text
threshold
```

alone.

But denoising should preserve relevant boundaries.

---

# 16.30 Hysteresis Thresholding

Canny uses two thresholds:

\[
T_L<T_H
\]

Pixels are categorized as:

```text
strong
weak
non-edge
```

and weak pixels connected to strong ones can be retained.

Although designed for edge detection, this provides a useful general lesson:

> Multiple thresholds plus connectivity can be more robust than one independent cutoff.

---

# 16.31 Double Thresholding Beyond Canny

> **EXTENSION**

The same conceptual pattern can be used for segmentation where:

```text
high-confidence foreground
+
possible foreground
```

are differentiated.

Connectivity then determines whether uncertain pixels belong to a confident region.

This idea is useful in interactive and seeded segmentation methods.

---

# 16.32 Multi-Level Thresholding

For:

\[
T_1<T_2
\]

define:

\[
M(x,y)=
\begin{cases}
0,&f<T_1\\
1,&T_1\le f<T_2\\
2,&f\ge T_2
\end{cases}
\]

This partitions an image into three intensity classes.

Applications include:

- multi-material images,
- grayscale scientific data,
- document/foreground/background separation.

---

# 16.33 Thresholding with Class Imbalance

Suppose:

```text
background = 95%
foreground = 5%
```

A method optimized for total pixel agreement may prefer labeling everything background.

Therefore:

```text
high pixel accuracy
```

does not necessarily mean:

```text
good object segmentation
```

Use IoU, Dice, precision/recall or task-specific measures when the foreground is small.

---

# 16.34 Threshold Selection as an Optimization Problem

A general thresholding formulation is:

\[
T^*=
\arg\max_T
J(T)
\]

where:

\[
J(T)
\]

is a separation criterion.

Examples:

```text
between-class variance
entropy-based score
classification accuracy
IoU on validation data
```

This is a powerful abstraction.

It turns thresholding from:

```text
pick a number
```

into:

```text
optimize a criterion
```

---

# 16.35 Entropy-Based Thresholding

> **EXTENSION**

Some methods choose thresholds using information/entropy criteria.

A simplified idea is:

```text
choose threshold
→ maximize useful information separation
```

The exact formulas vary by method.

The important conceptual extension is that threshold selection does not have to rely solely on mean/variance separation.

---

# 16.36 Thresholding and Morphology

After thresholding:

```text
mask
```

may contain defects:

```text
holes
specks
broken strokes
small islands
```

Morphology can be applied:

```text
threshold
 ↓
opening/closing
 ↓
clean mask
```

This relationship is central to C18.

---

# 16.37 Example — Document Binarization

Typical pipeline:

```text
document image
 ↓
grayscale
 ↓
optional denoise
 ↓
adaptive threshold
 ↓
morphological cleanup
 ↓
connected components
 ↓
OCR
```

Potential failure causes:

- shadows,
- page texture,
- bleed-through,
- small font,
- uneven illumination.

The threshold method should match the document conditions.

---

# 16.38 Example — Industrial Object Segmentation

Suppose a dark component sits on a bright conveyor.

A global threshold may work extremely well if:

```text
lighting is controlled
background is stable
object intensity is distinct
```

This is why simple algorithms remain valuable in industrial environments.

A more complex learned model is not automatically better if the simple rule is reliable and easier to validate.

---

# 16.39 Example — Unevenly Lit Surface

Suppose:

```text
left background = 50
right background = 120
```

with the object only slightly darker than its local background.

A global threshold may fail because one threshold cannot follow both background levels.

Adaptive thresholding can model:

```text
local background
```

and therefore become more effective.

---

# 16.40 Thresholding and Illumination Correction

An alternative to adaptive thresholding is:

```text
estimate illumination
       ↓
correct image
       ↓
global threshold
```

For example:

\[
f_{\text{corrected}}
=
\frac{f}{i}
\]

under a suitable multiplicative illumination model and with safe handling of zero/near-zero values.

Thus adaptive thresholding is not the only solution to uneven illumination.

---

# 16.41 Threshold Parameter Sensitivity

A useful experiment is to sweep:

\[
T-10,\quad T-5,\quad T,\quad T+5,\quad T+10
\]

and compare masks.

If a tiny threshold change produces huge object changes:

```text
class distributions overlap strongly
```

or the image is near a critical decision boundary.

This sensitivity is itself diagnostic information.

---

# 16.42 Stability Analysis

For adaptive thresholding, similarly vary:

```text
window size
C
Gaussian sigma
```

A robust method should not collapse under tiny parameter changes unless the task itself is highly sensitive.

This is a practical engineering test.

---

# 16.43 Thresholding Pipeline

A disciplined workflow:

```text
INPUT
 ↓
inspect histogram / image
 ↓
choose representation
 ↓
choose global or adaptive method
 ↓
choose polarity
 ↓
choose threshold parameters
 ↓
generate mask
 ↓
optional morphology
 ↓
connected components
 ↓
evaluate
```

This makes thresholding reproducible.

---

# 16.44 Implementation Pseudocode

### Global

```text
for each pixel:
    if value >= T:
        mask = 1
    else:
        mask = 0
```

### Adaptive

```text
for each pixel:
    compute local statistic
    compute T(x,y)
    compare pixel against local threshold
```

### Otsu-style

```text
compute histogram
for each candidate threshold:
    compute class statistics
    compute objective
choose threshold with best objective
```

---

# 16.45 Common Traps

## Trap 1 — “Otsu is always optimal.”

False.

It optimizes its statistical criterion under its assumptions, not every segmentation objective.

## Trap 2 — “Adaptive thresholding always beats global thresholding.”

False.

Controlled uniform illumination can favour a global rule.

## Trap 3 — “A threshold changes image quality.”

Its primary goal is label separation, not image enhancement.

## Trap 4 — “Histogram valley always gives the correct threshold.”

False.

Histograms can be skewed, noisy and class-imbalanced.

## Trap 5 — “Threshold 128 is universal for 8-bit images.”

False.

The correct threshold depends on image content and representation.

## Trap 6 — “More thresholds give better segmentation.”

Not necessarily.

Too many classes can produce over-segmentation.

## Trap 7 — “Thresholding is only for grayscale.”

False.

Colour and feature-space thresholding are common.

## Trap 8 — “Changing the threshold fixes feature overlap.”

False.

If the chosen feature distributions overlap substantially, no single threshold can produce perfect separation.

---

# 16.46 Exam Formula Sheet

### Global threshold

\[
\boxed{
M(x,y)=
\begin{cases}
1,&f(x,y)\ge T\\
0,&f(x,y)<T
\end{cases}
}
\]

### Range threshold

\[
\boxed{
M=
1
\quad\text{if}\quad
T_{\min}\le f<T_{\max}
}
\]

### Otsu between-class variance

\[
\boxed{
\sigma_B^2(t)
=
w_0(t)w_1(t)
[\mu_0(t)-\mu_1(t)]^2
}
\]

### Otsu threshold

\[
\boxed{
t^*=\arg\max_t\sigma_B^2(t)
}
\]

### Adaptive threshold

\[
\boxed{
M(x,y)=
\begin{cases}
1,&f(x,y)\ge T(x,y)\\
0,&f(x,y)<T(x,y)
\end{cases}
}
\]

### Local-mean form

\[
\boxed{
T(x,y)=\mu_L(x,y)-C
}
\]

---

# 16.47 Exam-Style Problem — Otsu Class Statistics

Suppose a threshold divides the image into:

\[
w_0=0.4,\qquad w_1=0.6
\]

with:

\[
\mu_0=40,\qquad\mu_1=160
\]

Then:

\[
\sigma_B^2
=
(0.4)(0.6)(40-160)^2
\]

\[
=
0.24(120^2)
\]

\[
=
0.24(14400)
\]

\[
\boxed{3456}
\]

This is the between-class variance score for that threshold.

---

# 16.48 Exam-Style Problem — Adaptive Threshold

Local mean:

\[
\mu_L=150
\]

and:

\[
C=20
\]

Then:

\[
T=150-20
\]

\[
\boxed{130}
\]

For pixel:

\[
f=140
\]

the pixel becomes foreground under:

\[
f\ge T
\]

because:

\[
140\ge130
\]

---

# 16.49 Exam-Style Problem — Multi-Level Threshold

Let:

\[
T_1=50,\qquad T_2=100
\]

For a pixel:

\[
f=75
\]

it belongs to:

\[
50\le f<100
\]

and therefore receives the middle class label.

---

# 16.50 Engineering Insight — Thresholding Is a Feature Problem

Suppose you are thresholding grayscale intensity.

You have chosen:

```text
feature = intensity
```

The threshold is only useful if intensity separates the desired classes.

A better workflow can be:

```text
change representation
→ choose better feature
→ then threshold
```

For example:

```text
RGB
→ HSV
→ hue threshold
```

can outperform:

```text
RGB
→ grayscale
→ intensity threshold
```

for a colour-defined object.

---

# 16.51 Cross-Book Bridges

> **C06 BRIDGE**  
> Thresholding can be understood as a piecewise point transformation.

> **C07 BRIDGE**  
> Histogram shape provides evidence for whether global thresholding may work.

> **C09 BRIDGE**  
> Noise near the threshold can produce label instability; preprocessing can help.

> **C10 BRIDGE**  
> Edge information can complement threshold-based region separation.

> **C15 BRIDGE**  
> Thresholding implements the general pixel-to-label idea introduced in segmentation fundamentals.

> **C17 BRIDGE**  
> When a single threshold fails, region-based methods incorporate spatial connectivity and homogeneity.

> **C18 BRIDGE**  
> Morphological operations clean masks generated by thresholding.

> **LAB BRIDGE**  
> Compare manual, iterative, Otsu and adaptive thresholding under controlled image conditions.

> **PRACTICE BRIDGE**  
> Solve binary/range/multi-level thresholds, Otsu calculations and adaptive-threshold problems.

> **EXAM BRIDGE**  
> Know global vs adaptive thresholding, Otsu's criterion, local threshold equations, histogram-based reasoning and failure cases.

---

# 16.52 Quick Recall

```text
GLOBAL
→ one T

ADAPTIVE
→ T(x,y)

OTSU
→ maximize between-class variance

RANGE
→ keep values inside interval

MULTI-LEVEL
→ several thresholds

KEY FAILURE
→ class distributions overlap
or
→ illumination varies
```

Core rule:

> **Do not ask only “What is the threshold?” Ask “Why should this threshold separate the intended classes?”**

---

# 16.53 Chapter Checkpoint

1. Define thresholding.
2. Differentiate global and adaptive thresholding.
3. Explain threshold polarity.
4. Calculate a binary mask from a threshold.
5. Explain range and multi-level thresholding.
6. How can a histogram guide threshold selection?
7. Why can histogram-valley thresholding fail?
8. Explain iterative threshold selection.
9. Derive the Otsu between-class variance.
10. Explain Otsu's intuition.
11. Why can Otsu fail under severe illumination variation?
12. Write the adaptive threshold formulation.
13. Explain how local mean thresholding works.
14. Why does window size matter?
15. Compare global and adaptive thresholding.
16. Explain thresholding in a colour space.
17. Why can preprocessing improve thresholding?
18. What happens when class distributions overlap strongly?
19. How can IoU/Dice evaluate a thresholded mask?
20. Design an experiment comparing global, Otsu and adaptive thresholding.

---

# 16.54 Part III Progression

The current knowledge chain is:

```text
C15
SEGMENTATION FUNDAMENTALS
        ↓
C16
THRESHOLDING
```

Next:

```text
C17
REGION-BASED SEGMENTATION
        ↓
C18
MATHEMATICAL MORPHOLOGY
        ↓
C19
IMAGE FEATURES + DESCRIPTORS
        ↓
C20
SIFT / SURF / ORB / HOG
```

The central progression is:

```text
pixel decision
→
adaptive pixel decision
→
connected regions
→
shape manipulation
→
measurable features
→
robust local descriptors
```

That moves the MiniBook from basic segmentation into classical computer vision.
