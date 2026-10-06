---
id: "C09"
title: "Smoothing and Noise Reduction"
layer: "MAIN"
part: "II — Improving the Image"
unit: "II"
version: "1.0"
status: "REFERENCE BUILD"
syllabus_scope:
  - "Smoothing"
  - "Noise reduction"
  - "Image degradation preview"
tags:
  - "CORE"
  - "EXAM"
  - "MATH"
  - "DEEP DIVE"
  - "LAB"
  - "NOISE"
  - "FILTERING"
prerequisites:
  - "C03"
  - "C08"
related:
  - "C10"
  - "C12"
  - "C13"
  - "C14"
  - "C21"
math:
  - "M05"
  - "M06"
  - "M08"
lab:
  - "LAB-U2-03"
  - "LAB-U2-04"
exam:
  - "EXAM-U2"
practice:
  - "P-C09"
assets:
  - "D-C09-01"
  - "D-C09-02"
  - "D-C09-03"
---

# Chapter 09 — Smoothing and Noise Reduction

> **Chapter thesis**  
> Noise reduction is not simply “make the image smoother.” A good denoising method is a deliberate compromise between suppressing unwanted variation and preserving edges, textures and other information that the task needs.

**Part II — Improving the Image**  
**Syllabus anchor:** Unit II includes smoothing and noise reduction within spatial-domain enhancement. fileciteturn4file0L36-L40

---

# 09.0 Why This Chapter Is Separate from C08

Chapter 08 established the general spatial-filtering machinery:

```text
image
+
neighbourhood
+
kernel
→
filtered response
```

This chapter asks a more specific question:

> **What kind of variation is unwanted, what kind of noise produced it, and which filter suppresses it while preserving useful information?**

That changes the learning direction from:

```text
HOW a filter works
```

to:

```text
WHY this denoising filter is appropriate
```

---

# 09.1 What Is Image Noise?

Image noise is unwanted variation introduced into an image during:

- acquisition,
- transmission,
- sensing,
- digitisation,
- storage,
- processing.

A simple additive model is:

\[
g(x,y)=f(x,y)+\eta(x,y)
\]

where:

- \(f\) = ideal/original image,
- \(\eta\) = noise,
- \(g\) = observed noisy image.

This is a useful model, but not every physical noise source is purely additive.

---

# 09.2 Why Noise Matters

Noise can:

- obscure low-contrast detail,
- create false edges,
- disturb segmentation,
- corrupt measurements,
- reduce feature quality,
- degrade compression efficiency,
- confuse machine-learning models.

A good denoising method therefore has to balance:

```text
noise suppression
        ↕
detail preservation
```

---

# 09.3 Three Different Meanings of “Clean Image”

In engineering work, “cleaner” can mean different things.

### Visually cleaner

Fewer visible speckles or fluctuations.

### Numerically closer

Lower error relative to a known reference.

### More useful for the task

Better segmentation/classification/detection performance.

These are not guaranteed to agree.

A strongly blurred image may look smooth but be worse for edge detection.

---

# 09.4 Noise Sources

Typical sources include:

```text
sensor electronics
thermal effects
photon statistics
readout circuitry
transmission errors
quantization
compression/processing
```

The exact statistical model depends on the imaging system.

For engineering analysis, we often begin by identifying the **observed noise pattern** and then choose a useful model.

---

# 09.5 Gaussian Noise

A common simplified model assumes noise values follow a Gaussian distribution.

Its probability density function is:

\[
p(\eta)=
\frac{1}{\sqrt{2\pi\sigma^2}}
e^{-\frac{(\eta-\mu)^2}{2\sigma^2}}
\]

where:

- \(\mu\) = mean,
- \(\sigma^2\) = variance.

For zero-mean Gaussian noise:

\[
\mu=0
\]

and:

\[
p(\eta)=
\frac{1}{\sqrt{2\pi\sigma^2}}
e^{-\frac{\eta^2}{2\sigma^2}}
\]

---

# 09.6 Gaussian Noise Intuition

For zero-mean Gaussian noise:

```text
small disturbances
→ common

large disturbances
→ less common
```

A histogram of noise values tends to look approximately bell-shaped under the model.

In a real image, the observed histogram combines:

```text
image signal
+
noise
```

so the image histogram itself is not automatically a Gaussian noise histogram.

---

# 09.7 Salt-and-Pepper Noise

Salt-and-pepper noise is characterized by isolated extreme-valued pixels.

Conceptually:

```text
normal image
████████████████

with impulse noise

███████•████████
████████████•███
██•█████████████
```

Depending on the representation:

```text
pepper → dark impulses
salt   → bright impulses
```

This noise is called **impulse noise**.

It is especially useful for understanding why the median filter can outperform simple averaging.

---

# 09.8 Why Mean Filtering Struggles with Impulse Noise

Consider:

\[
[10,10,10,10,250]
\]

Mean:

\[
\frac{10+10+10+10+250}{5}
=
58
\]

Median:

\[
10
\]

The single extreme outlier moves the mean substantially.

The median is much more resistant to that outlier.

Therefore:

```text
impulse noise
→ median is often a strong candidate
```

This is not a guarantee for every image or parameter setting.

---

# 09.9 Uniform Noise

A simplified uniform-noise model assumes equal probability within a finite interval.

For:

\[
a\le\eta\le b
\]

the probability density is:

\[
p(\eta)=
\begin{cases}
\frac{1}{b-a},&a\le\eta\le b\\
0,&\text{otherwise}
\end{cases}
\]

Uniform noise may be useful in simulation and analysis even when it is not a perfect physical model.

---

# 09.10 Periodic Noise

Periodic or sinusoidal interference may appear as repeating patterns.

For example:

```text
//// //// //// ////
```

or:

```text
dark-light-dark-light
```

in structured directions.

A useful model can be:

\[
\eta(x,y)=A\sin(2\pi(u_0x+v_0y)+\phi)
\]

where:

- \(A\) = amplitude,
- \(u_0,v_0\) = spatial frequencies,
- \(\phi\) = phase.

Periodic noise is especially important because it often becomes easy to identify in the frequency domain.

This will connect directly to C12–C13.

---

# 09.11 Speckle and Multiplicative Noise

Some imaging systems are better described using a multiplicative model:

\[
g(x,y)=f(x,y)n(x,y)
\]

where \(n\) is a multiplicative noise factor.

This occurs in settings such as coherent imaging.

A common extension is the logarithmic transformation:

\[
\ln g=\ln f+\ln n
\]

which turns multiplication into addition, making additive-noise tools potentially more applicable after suitable handling.

> **EXTENSION:** This transformation requires positive-valued data and careful range/zero handling.

---

# 09.12 Quantization Noise vs Acquisition Noise

C03 introduced quantization.

Quantization error is not automatically the same thing as sensor noise.

```text
quantization
→ finite numerical representation

sensor/acquisition noise
→ unwanted physical/electronic variation
```

Both may affect the final image, but their causes and mathematical models differ.

---

# 09.13 Noise Model Comparison

| Noise type | Typical appearance | Simplified model | Common candidate |
|---|---|---|---|
| Gaussian | small random fluctuations | additive Gaussian | Gaussian/linear smoothing |
| Salt-and-pepper | isolated dark/bright impulses | impulse noise | median |
| Uniform | bounded random variation | uniform PDF | averaging/adaptive methods |
| Periodic | repeating structure | sinusoidal components | frequency-domain filtering |
| Speckle-like | granular/multiplicative | \(g=fn\) | model-dependent |

The “candidate” column is a starting point, not a universal prescription.

---

# 09.14 Signal-to-Noise Ratio

A useful quality concept is the signal-to-noise ratio:

\[
\mathrm{SNR}
=
\frac{P_{\text{signal}}}
{P_{\text{noise}}}
\]

where \(P\) denotes an appropriate power measure.

In decibels:

\[
\mathrm{SNR}_{dB}
=
10\log_{10}
\left(
\frac{P_{\text{signal}}}
{P_{\text{noise}}}
\right)
\]

A higher SNR generally indicates a stronger signal relative to noise under the chosen measurement definition.

---

# 09.15 Amplitude-Ratio Form

When RMS amplitudes rather than powers are used:

\[
\mathrm{SNR}_{dB}
=
20\log_{10}
\left(
\frac{A_{\text{signal}}}
{A_{\text{noise}}}
\right)
\]

This is mathematically consistent with the power form when power is proportional to squared amplitude.

> **Exam trap:** Use 10 log for a power ratio and 20 log for an amplitude ratio.

---

# 09.16 PSNR

For image restoration tasks, **Peak Signal-to-Noise Ratio (PSNR)** is often used.

For maximum possible sample value \(MAX_I\) and mean squared error \(MSE\):

\[
\mathrm{PSNR}
=
10\log_{10}
\left(
\frac{MAX_I^2}{MSE}
\right)
\]

If the image is an 8-bit representation with maximum value 255:

\[
MAX_I=255
\]

Then:

\[
\mathrm{PSNR}
=
10\log_{10}
\left(
\frac{255^2}{MSE}
\right)
\]

---

# 09.17 MSE

For two images \(I\) and \(K\):

\[
MSE=
\frac{1}{MN}
\sum_{x=0}^{M-1}
\sum_{y=0}^{N-1}
[I(x,y)-K(x,y)]^2
\]

For colour images, the averaging convention must be stated because channels may be incorporated differently.

---

# 09.18 Worked MSE Example

Suppose the reference and output values for four pixels are:

```text
Reference:  10 20 30 40
Output:     12 18 29 43
```

Errors:

\[
2,-2,-1,3
\]

Squared errors:

\[
4,4,1,9
\]

Therefore:

\[
MSE=\frac{4+4+1+9}{4}
\]

\[
=\frac{18}{4}
\]

\[
\boxed{4.5}
\]

For an 8-bit image:

\[
PSNR=
10\log_{10}
\left(
\frac{255^2}{4.5}
\right)
\]

which is approximately:

\[
\boxed{41.6\text{ dB}}
\]

---

# 09.19 PSNR Limitations

PSNR is useful, but it is not a complete measure of perceptual quality.

Two images can have:

```text
similar PSNR
```

but substantially different visual quality or task performance.

Likewise:

```text
higher PSNR
```

does not automatically mean better edge preservation.

Use metrics according to the task.

---

# 09.20 Mean / Box Smoothing

The \(K\times K\) mean filter computes:

\[
g(x,y)
=
\frac{1}{K^2}
\sum_{s,t}f(x-s,y-t)
\]

under the chosen boundary convention.

Its main effect is:

```text
local averaging
→ reduced random variation
→ reduced high-frequency detail
```

---

# 09.21 Gaussian Smoothing

A Gaussian filter uses distance-dependent weights.

Continuous Gaussian:

\[
G(x,y)
=
\frac{1}{2\pi\sigma^2}
e^{-\frac{x^2+y^2}{2\sigma^2}}
\]

Higher \(\sigma\) gives a wider kernel.

Conceptually:

```text
small σ
→ narrow smoothing

large σ
→ broader smoothing
```

---

# 09.22 Effect of Gaussian Sigma

Imagine:

```text
σ small
→ preserve more local detail
→ less smoothing

σ large
→ stronger blur
→ more noise suppression
→ more detail loss
```

There is no universally correct sigma.

It should be selected from:

- noise strength,
- object scale,
- desired edge preservation,
- downstream task.

---

# 09.23 Mean vs Gaussian

| Property | Mean | Gaussian |
|---|---|---|
| weighting | equal | centre-weighted |
| mathematical shape | box | Gaussian |
| implementation | very simple | still efficient |
| smoothing | uniform neighbourhood | distance-weighted |
| common use | simple baseline | general-purpose smoothing |

Gaussian filtering is often preferred when a smoother spatial response is desired.

---

# 09.24 Median Filtering

For an odd-sized neighbourhood, arrange the values in sorted order and select the middle value.

For:

\[
[12,11,13,10,120]
\]

sorted:

\[
[10,11,12,13,120]
\]

median:

\[
\boxed{12}
\]

The extreme outlier has much less effect than it would under averaging.

---

# 09.25 Why Median Preserves Edges Better in Some Cases

An isolated impulse can be removed without averaging a dark/bright boundary into intermediate values.

For example:

```text
left region      right region

10 10 | 200 200
```

An averaging filter near the boundary can produce intermediate values.

A median filter may preserve the dominant local levels more effectively.

However, median filtering can also remove thin structures if the kernel is too large.

---

# 09.26 Kernel Size for Median Filtering

A common choice is:

\[
3\times3
\]

for mild impulse noise.

Larger kernels:

```text
5×5
7×7
...
```

can remove stronger noise but increase the risk of:

- edge loss,
- thin-line removal,
- small-object removal,
- texture destruction.

---

# 09.27 Order-Statistics Filters

The median belongs to a broader family.

For values in a neighbourhood:

### Minimum filter

\[
g=\min\{f_i\}
\]

Useful for emphasizing dark regions / suppressing bright impulses in some contexts.

### Maximum filter

\[
g=\max\{f_i\}
\]

Useful for emphasizing bright regions / suppressing dark impulses in some contexts.

### Midpoint filter

\[
g=
\frac{\min+\max}{2}
\]

Can be useful for certain noise types but is sensitive to extremes.

---

# 09.28 Arithmetic Mean Filter

The arithmetic mean is:

\[
g=
\frac{1}{N}\sum_{i=1}^{N}x_i
\]

It reduces random variation by averaging.

But every sample participates equally.

Thus extreme outliers can strongly influence the result.

---

# 09.29 Geometric Mean Filter

A geometric mean is:

\[
g=
\left(
\prod_{i=1}^{N}x_i
\right)^{1/N}
\]

This requires careful treatment when values are zero or negative.

For typical nonnegative image data, it can behave differently from arithmetic averaging and can sometimes preserve detail better.

> **Extension:** The practical value of a geometric mean filter is task- and data-dependent.

---

# 09.30 Harmonic Mean Filter

The harmonic mean can be written:

\[
g=
\frac{N}{
\sum_{i=1}^{N}\frac{1}{x_i}
}
\]

It also requires nonzero values.

It is particularly sensitive to small values.

Its use is more specialized than the mean or median.

---

# 09.31 Contraharmonic Mean Filter

A contraharmonic mean filter is:

\[
g=
\frac{
\sum x_i^{Q+1}
}{
\sum x_i^Q
}
\]

where \(Q\) is the filter parameter.

A commonly taught property is:

```text
Q > 0
→ tends to suppress pepper-like dark impulses

Q < 0
→ tends to suppress salt-like bright impulses
```

The denominator must be handled carefully, especially near zero.

---

# 09.32 Why Parameter Sign Matters

Suppose the neighbourhood contains:

```text
10 10 10 250
```

The desired direction of suppression depends on whether the problematic impulse is:

```text
dark
```

or:

```text
bright
```

The contraharmonic parameter \(Q\) controls which side receives stronger influence.

This is a classic exam concept, but practical use requires parameter validation and zero handling.

---

# 09.33 Adaptive Local Noise Reduction

> **EXTENSION**

A fixed filter treats every neighbourhood similarly.

An adaptive filter attempts to use local statistics:

\[
\mu_L,\qquad \sigma_L^2
\]

to decide how strongly to smooth.

One common form is:

\[
\hat f(x,y)
=
g(x,y)
-
\frac{\sigma_\eta^2}
{\sigma_L^2}
\left[
g(x,y)-\mu_L
\right]
\]

when the local variance is treated as informative and under the assumptions of the particular model.

Interpretation:

```text
local variance ≈ noise variance
→ stronger smoothing

local variance >> noise variance
→ preserve more local structure
```

The exact adaptive filter and assumptions must be stated.

---

# 09.34 Why Adaptive Filtering Is Attractive

A uniform background does not need the same treatment as a textured edge region.

```text
smooth background
→ can tolerate stronger smoothing

edge / texture
→ requires more preservation
```

Adaptive filters attempt to exploit that difference.

---

# 09.35 Noise Reduction vs Edge Preservation

Imagine:

```text
noise strength
↑
│\
│ \
│  \
│   \
└────────→ smoothing strength

              ↑
       too much smoothing
       destroys useful detail
```

This is not a fixed universal curve; it represents the general tradeoff.

A good denoising method should be evaluated at the task level.

---

# 09.36 Noise and Edge Detection

Suppose:

```text
original edge
████████|░░░░░░
```

Noise can introduce false transitions:

```text
███░████|░█░░██
```

A derivative filter may interpret these as edges.

Therefore a practical edge-detection pipeline often begins with:

```text
denoise / smooth
        ↓
derivative
        ↓
edge decision
```

This links C09 to C10.

---

# 09.37 Over-Smoothing Failure

A common mistake is:

```text
noise visible
→ increase kernel size
→ increase again
→ image becomes very smooth
```

The result may have:

- weak edges,
- lost texture,
- merged small structures,
- poorer segmentation.

Therefore:

> Do not optimize only for minimum visible noise.

---

# 09.38 Denoising Evaluation Matrix

| Evaluation | What it asks |
|---|---|
| visual | Does the image look cleaner? |
| MSE | How close is it to a reference? |
| PSNR | How strong is signal relative to reconstruction error? |
| edge preservation | Are important boundaries retained? |
| texture preservation | Is meaningful high-frequency information retained? |
| downstream accuracy | Did the actual task improve? |

---

# 09.39 Before/After Experiment Design

A strong lab experiment should store:

```text
original clean/reference
       ↓
synthetic noisy image
       ↓
mean filter
Gaussian filter
median filter
       ↓
compare
```

Record:

```text
kernel size
sigma
noise type
noise parameter
MSE
PSNR
visual observations
edge observations
```

This turns “try filters” into a reproducible engineering experiment.

---

# 09.40 Synthetic Noise as a Learning Tool

When a clean image is available, generate controlled noise:

```text
clean image
    ↓
known noise model
    ↓
noisy image
    ↓
denoising method
    ↓
compare against known original
```

Advantages:

- ground truth is known,
- parameters are controlled,
- methods can be compared fairly.

Limitations:

> Synthetic noise may not reproduce all real acquisition-system behaviour.

---

# 09.41 Practical Decision Tree

```text
OBSERVED NOISE
      │
      ├── isolated black/white impulses
      │       ↓
      │      median
      │
      ├── approximately random Gaussian-like fluctuations
      │       ↓
      │      Gaussian / linear smoothing
      │
      ├── repeating interference
      │       ↓
      │      frequency-domain analysis
      │
      └── multiplicative/granular pattern
              ↓
          identify imaging model
              ↓
          model-aware method
```

The first job is diagnosis, not filter selection.

---

# 09.42 Worked Example — Choosing a Filter

Suppose a 256×256 image shows:

```text
isolated white dots
+
isolated black dots
```

A reasonable first candidate is a median filter.

Why?

```text
noise
→ impulsive extremes

median
→ robust to isolated extreme values
```

A large Gaussian blur may reduce the dots, but it may also smear edges and texture.

Therefore median is a more targeted first experiment.

---

# 09.43 Worked Example — Gaussian Noise

Suppose an image is corrupted by small random fluctuations with approximately zero mean.

A Gaussian filter can be tested.

Workflow:

```text
estimate noise strength
      ↓
choose sigma
      ↓
apply Gaussian
      ↓
measure MSE/PSNR if reference exists
      ↓
inspect edges
```

A larger sigma does not automatically give a better result.

---

# 09.44 Why Noise Reduction Is Partly a Statistical Problem

Noise has properties such as:

- mean,
- variance,
- distribution,
- spatial correlation,
- temporal behaviour.

Therefore, good denoising uses statistical assumptions.

This creates a bridge:

```text
image processing
+
probability/statistics
```

That mathematical connection becomes deeper in restoration and machine learning.

---

# 09.45 Colour Images and Denoising

Denoising can be applied:

### Independently per channel

Simple, but channel relationships can be disturbed.

### On a luminance-like component

May better preserve colour relationships.

### In a colour space designed to separate brightness and chroma

Can allow different smoothing strengths.

The correct method depends on:

- noise source,
- colour representation,
- application.

---

# 09.46 Border Handling During Denoising

A filter near an image boundary sees fewer real neighbours.

The algorithm must choose a border policy.

Common options:

```text
zero
replicate
reflect
wrap
```

The choice can affect:

- edge appearance,
- boundary statistics,
- measured error.

A reproducible experiment must record it.

---

# 09.47 Computational Considerations

For a direct \(K\times K\) linear filter:

\[
O(MNK^2)
\]

is a useful simple complexity estimate.

A separable Gaussian can reduce the direct work substantially.

Median filtering has different computational behaviour because sorting/order statistics are involved.

Modern implementations may use optimized algorithms, vectorization or specialized hardware.

---

# 09.48 Practical Pseudocode

```text
INPUT:
    image
    noise model
    filter parameters

inspect:
    shape
    channels
    dtype
    min/max

if required:
    convert to working representation

estimate or specify noise characteristics

select candidate filter

apply filter

restore intended output range/dtype

evaluate:
    visual quality
    edge preservation
    numerical metrics
    downstream task
```

---

# 09.49 Common Traps

## Trap 1 — “Noise reduction always improves an image.”

False.

It can remove meaningful detail.

## Trap 2 — “Gaussian filter is best for all noise.”

False.

It is a general smoothing method, not a universal denoiser.

## Trap 3 — “Median filter works by averaging.”

False.

It selects an order statistic.

## Trap 4 — “Salt-and-pepper noise is Gaussian noise.”

False.

Impulse noise has a different structure.

## Trap 5 — “PSNR tells complete visual quality.”

False.

It is a useful numerical metric, not a complete perceptual/task metric.

## Trap 6 — “More smoothing means less error.”

False.

Beyond an optimum, detail loss can increase error.

## Trap 7 — “Noise model always comes from the final image histogram.”

False.

The observed histogram mixes scene and noise statistics.

## Trap 8 — “Denoising before edge detection is optional.”

Not always.

It is often important because differentiation is sensitive to high-frequency variation.

---

# 09.50 Exam Formula Sheet

### Additive noise

\[
\boxed{g=f+\eta}
\]

### Gaussian PDF

\[
\boxed{
p(\eta)=
\frac{1}{\sqrt{2\pi\sigma^2}}
e^{-\frac{(\eta-\mu)^2}{2\sigma^2}}
}
\]

### Uniform PDF

\[
\boxed{
p(\eta)=\frac1{b-a},
\quad a\le\eta\le b
}
\]

### SNR

\[
\boxed{
SNR=\frac{P_s}{P_n}
}
\]

### SNR in dB

\[
\boxed{
SNR_{dB}
=
10\log_{10}\frac{P_s}{P_n}
}
\]

### PSNR

\[
\boxed{
PSNR
=
10\log_{10}
\frac{MAX_I^2}{MSE}
}
\]

### MSE

\[
\boxed{
MSE=
\frac1{MN}
\sum
(I-K)^2
}
\]

### Median

\[
\boxed{
g=\operatorname{median}\{f_i\}
}
\]

---

# 09.51 Exam-Style Comparison

| Noise | Why it is difficult | Candidate method |
|---|---|---|
| Gaussian | distributed over many pixels | Gaussian/mean/adaptive |
| salt-and-pepper | extreme impulses | median |
| periodic | structured interference | frequency-domain analysis |
| multiplicative | signal-dependent distortion | model-aware processing |

---

# 09.52 Cross-Book Bridges

> **C08 BRIDGE**  
> General spatial-filter mechanics are reused here with noise-specific decision logic.

> **C10 BRIDGE**  
> Noise suppression is often performed before derivative-based edge detection.

> **C12–C13 BRIDGE**  
> Periodic noise is especially informative in the frequency domain.

> **C14 BRIDGE**  
> Restoration treats blur/noise using an explicit degradation model and can use Wiener/model-based methods.

> **LAB BRIDGE**  
> Add controlled Gaussian and impulse noise, run candidate filters, and compare metrics.

> **PRACTICE BRIDGE**  
> Identify noise models, compute MSE/PSNR, select filters and analyze tradeoffs.

> **EXAM BRIDGE**  
> Prepare noise distributions, mean/median/contraharmonic filters, SNR/PSNR and filter-selection reasoning.

---

# 09.53 Quick Recall

```text
NOISE
→ unwanted variation

GAUSSIAN
→ random bell-shaped model

SALT + PEPPER
→ impulse extremes

MEAN / GAUSSIAN
→ linear smoothing

MEDIAN
→ nonlinear impulse suppression

PERIODIC NOISE
→ frequency-domain candidate

PSNR
→ reference-based numerical quality measure
```

Core rule:

> **Identify the noise before choosing the filter.**

---

# 09.54 Chapter Checkpoint

1. Define image noise.
2. Write the additive noise model.
3. Describe Gaussian noise.
4. Explain salt-and-pepper noise.
5. Why does median filtering work well for impulse noise?
6. Define periodic noise and explain why frequency-domain analysis can help.
7. Differentiate additive and multiplicative noise.
8. Define SNR and PSNR.
9. Calculate MSE for two short image sequences.
10. Compare mean, Gaussian and median filtering.
11. Explain contraharmonic mean filtering and the role of \(Q\).
12. Why can over-smoothing reduce task performance?
13. Why is PSNR insufficient as a complete image-quality measure?
14. How should a reproducible denoising experiment be designed?

---

# 09.55 Connection Forward

We now understand how to suppress unwanted variation.

But the next question is the opposite:

> **How do we deliberately emphasize boundaries, fine detail and intensity transitions?**

That is Chapter 10:

```text
noise reduction
      ↓
gradient / derivative
      ↓
edge response
      ↓
edge decision
      ↓
sharpened / structured image
```
