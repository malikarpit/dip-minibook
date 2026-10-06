---
id: "C14"
title: "Image Restoration and Deblurring"
layer: "MAIN"
part: "II — Improving the Image"
unit: "II"
version: "1.0"
status: "REFERENCE BUILD"
syllabus_scope:
  - "Image restoration"
  - "Noise reduction"
  - "Blur/degradation"
tags:
  - "CORE"
  - "EXAM"
  - "MATH"
  - "DEEP DIVE"
  - "RESTORATION"
  - "DEBLURRING"
  - "INVERSE PROBLEM"
prerequisites:
  - "C09"
  - "C10"
  - "C12"
  - "C13"
related:
  - "C08"
  - "C11"
  - "C21"
  - "C31"
math:
  - "M09"
  - "M10"
  - "M11"
  - "M12"
lab:
  - "LAB-U2-04"
  - "LAB-U2-05"
exam:
  - "EXAM-U2"
practice:
  - "P-C14"
assets:
  - "D-C14-01"
  - "D-C14-02"
  - "D-C14-03"
---

# Chapter 14 — Image Restoration and Deblurring

> **Chapter thesis**  
> Restoration treats an observed image as the output of a degradation process and attempts to estimate the unknown original. The central model is an inverse problem: blur, noise and sampling have transformed the underlying image, and restoration asks what original image is most consistent with the observed data and an assumed degradation model.

**Part II — Improving the Image**

> **Scope note:** The university Unit II scope explicitly includes noise reduction/restoration within the image-processing sequence. This chapter expands that foundation into classical degradation and restoration models so the student can understand the difference between enhancement and model-based recovery. fileciteturn4file0L36-L40

---

# 14.0 Enhancement vs Restoration

This distinction is one of the most important in the entire MiniBook.

### Enhancement

```text
observed image
     ↓
choose useful transformation
     ↓
more useful appearance/representation
```

### Restoration

```text
observed degraded image
     ↓
estimate degradation model
     ↓
invert / estimate degradation
     ↓
restored image
```

Enhancement may be subjective or task-driven.

Restoration is generally model-driven.

---

# 14.1 The Degradation Model

A classical degradation model is:

\[
g(x,y)=h(x,y)*f(x,y)+\eta(x,y)
\]

where:

- \(f(x,y)\) = original image,
- \(h(x,y)\) = degradation/blur function,
- \(*\) = convolution,
- \(\eta(x,y)\) = noise,
- \(g(x,y)\) = observed degraded image.

Conceptual pipeline:

```text
ORIGINAL IMAGE f
      ↓
  blur h
      ↓
add noise η
      ↓
OBSERVED IMAGE g
```

This model is not universal, but it is foundational.

---

# 14.2 Why Deblurring Is Hard

If:

\[
g=h*f+\eta
\]

we would like:

\[
f\approx ?
\]

The difficulty is that:

```text
blur
→ mixes neighbouring pixels

noise
→ introduces uncertainty

some frequency components
→ may be strongly attenuated
```

So simply “undoing the blur” can amplify noise enormously.

---

# 14.3 Frequency-Domain Degradation Model

Taking Fourier transforms:

\[
G(u,v)=H(u,v)F(u,v)+N(u,v)
\]

This is a powerful simplification.

Instead of spatial convolution:

\[
h*f
\]

we have multiplication:

\[
HF
\]

The restoration problem becomes:

```text
G
=
HF + N
```

and we want to estimate:

\[
F
\]

---

# 14.4 Ideal Inverse Filtering

Ignoring noise for a moment:

\[
G=HF
\]

Therefore:

\[
F=\frac{G}{H}
\]

This suggests the inverse filter:

\[
\hat F=
\frac{G}{H}
\]

where \(H\ne0\).

This seems perfect mathematically.

It is not robust in practice.

---

# 14.5 Why Inverse Filtering Can Explode

Suppose:

\[
|H|=0.1
\]

Then:

\[
\frac1{|H|}=10
\]

A noise component of magnitude:

\[
0.02
\]

can become:

\[
0.02\times10=0.2
\]

after inversion.

If:

\[
|H|=0.001
\]

then:

\[
\frac1{|H|}=1000
\]

and even tiny noise can become enormous.

Therefore:

> **Inverse filtering is extremely sensitive to frequencies where the degradation transfer function is small.**

---

# 14.6 Worked Inverse-Filter Example

Suppose one frequency component has:

\[
G=0.52
\]

and:

\[
H=0.8
\]

Ignoring noise:

\[
\hat F=
\frac{0.52}{0.8}
\]

\[
\boxed{\hat F=0.65}
\]

Now suppose:

\[
H=0.02
\]

with the same observed value:

\[
\hat F=\frac{0.52}{0.02}=26
\]

The estimate becomes extremely large.

This is the instability problem.

---

# 14.7 Frequencies Where \(H=0\)

If:

\[
H(u,v)=0
\]

then:

\[
\frac{1}{H}
\]

is undefined.

That means the degradation has completely removed that frequency in the model.

No inverse filter can recover information that is mathematically absent from the observed signal without additional prior information.

This is a core inverse-problem insight.

---

# 14.8 Ill-Posedness

A restoration problem can be ill-conditioned or ill-posed because:

```text
different originals
→ can produce similar observations

small observation error
→ can create large restoration changes
```

Noise makes the problem especially unstable.

This is why regularization matters.

---

# 14.9 Point-Spread Function (PSF)

The blur function:

\[
h(x,y)
\]

is often called the **point-spread function (PSF)**.

Conceptually:

```text
ideal point object
      ↓
imaging system
      ↓
spread-out point
```

The PSF describes how a point-like input is distributed by the system.

A sharp system produces a concentrated PSF.

A blurry system produces a wider PSF.

---

# 14.10 Line-Spread Function

> **EXTENSION**

A line-spread function can characterize the response to an ideal line feature.

It is related to the PSF through integration along an appropriate direction.

The PSF is generally the more fundamental 2-D concept for image restoration.

---

# 14.11 Motion Blur

Camera or object motion can produce directional blur.

A simplified PSF may look like:

```text
████████
```

rather than a compact point.

In the frequency domain, this produces direction-dependent attenuation.

Restoration requires a model of:

```text
motion direction
+
motion length
+
possible exposure behaviour
```

The exact physical model can be more complex than a simple uniform line spread.

---

# 14.12 Defocus Blur

Defocus can spread a point into a disk-like region in a simplified model.

Conceptually:

```text
point
 ↓
  ●
blurred point
 ↓
 ◉
```

This produces a characteristic PSF.

Again:

> Real optical blur can be more complicated than the idealized textbook PSF.

---

# 14.13 Atmospheric / System Blur

> **EXTENSION**

Imaging through turbulence, scattering or other propagation effects can introduce blur and contrast loss.

Restoration then requires a model of the propagation/degradation process.

This illustrates a general rule:

> The quality of a restoration result depends strongly on how well the degradation model matches reality.

---

# 14.14 Wiener Filtering

A classical approach balances inversion against noise amplification.

The Wiener filter minimizes mean-square estimation error under the assumptions of the model.

A common frequency-domain form is:

\[
\hat F(u,v)
=
\frac{H^*(u,v)}
{|H(u,v)|^2+K(u,v)}
G(u,v)
\]

A commonly taught simplified form uses a constant:

\[
\hat F(u,v)
=
\frac{H^*(u,v)}
{|H(u,v)|^2+K}
G(u,v)
\]

where:

- \(H^*\) = complex conjugate of \(H\),
- \(K\) is related to the noise-to-signal power ratio under the chosen formulation.

---

# 14.15 Why Wiener Is More Stable

Compare:

### Inverse

\[
\frac{1}{H}
\]

### Wiener-like

\[
\frac{H^*}{|H|^2+K}
\]

When:

\[
|H|\rightarrow0
\]

the inverse filter becomes unstable.

But if:

\[
K>0
\]

the denominator remains nonzero.

So the Wiener approach prevents unlimited amplification of weak spectral regions.

---

# 14.16 Worked Wiener-Style Example

Suppose:

\[
H=0.1
\]

and:

\[
K=0.01
\]

Assume real \(H\) for simplicity.

Then:

\[
H^*=0.1
\]

\[
|H|^2=0.01
\]

Therefore the filter gain is:

\[
\frac{0.1}{0.01+0.01}
\]

\[
=\frac{0.1}{0.02}
\]

\[
\boxed{5}
\]

The direct inverse gain would be:

\[
\frac1{0.1}=10
\]

Thus the Wiener-style regularization reduces the amplification in this example.

---

# 14.17 Wiener Interpretation

The denominator:

\[
|H|^2+K
\]

creates a compromise:

```text
strongly transmitted frequency
→ permit more recovery

weakly transmitted / noisy frequency
→ avoid excessive amplification
```

It is therefore a model-based tradeoff.

---

# 14.18 Regularization

More generally, restoration can be viewed as:

\[
\text{data fidelity}
+
\lambda\cdot\text{prior/regularization}
\]

The first term says:

> stay consistent with the observed image.

The second says:

> prefer a plausible or stable solution.

This is the broader mathematical view of inverse problems.

---

# 14.19 Tikhonov-Style Regularization

> **EXTENSION**

A common formulation is:

\[
\hat f
=
\arg\min_f
\left[
\|Hf-g\|_2^2
+
\lambda\|Lf\|_2^2
\right]
\]

where:

- \(Hf\) models degradation,
- \(g\) is observed data,
- \(L\) is a regularization operator,
- \(\lambda\) controls the tradeoff.

This says:

```text
fit observed image
+
avoid implausibly unstable solution
```

The exact solution depends on the chosen \(L\), boundary conditions and optimization formulation.

---

# 14.20 Why Regularization Is Necessary

Without regularization:

```text
fit data exactly
→ may fit noise
→ may explode at weak frequencies
```

With too much regularization:

```text
stable solution
→ but useful detail may be suppressed
```

Therefore:

\[
\text{regularization strength}
\]

is itself a model-selection parameter.

---

# 14.21 Noise-Free vs Noisy Restoration

### Noise-free

If:

\[
\eta=0
\]

the inverse problem is simpler.

### Noisy

If:

\[
\eta\ne0
\]

then direct inversion can amplify noise.

This is why restoration methods must explicitly account for noise assumptions.

---

# 14.22 Blur and Noise Are Different Degradations

### Blur

```text
mixes spatial information
```

### Noise

```text
adds uncertainty/variation
```

A good restoration model may need both:

\[
g=h*f+\eta
\]

Ignoring one component can lead to poor recovery.

---

# 14.23 Restoration vs Denoising

Denoising:

```text
focus on noise
```

Deblurring:

```text
focus on blur
```

Restoration:

```text
estimate degradation process
+
recover original
```

Real systems may require both simultaneously.

---

# 14.24 Estimating the Degradation Function

Sometimes \(H\) is known or calibrated.

Examples:

```text
known optical system
known motion direction
known blur kernel
```

Other times it must be estimated.

This is called **blind deconvolution** when both the original image and degradation are unknown or only partially known.

---

# 14.25 Blind Deconvolution

Conceptually:

```text
observed image
      ↓
estimate blur
      ↓
estimate original
      ↕
refine blur
      ↕
refine original
```

This is difficult because many combinations of:

```text
image
+
blur kernel
```

can explain the observations.

Therefore strong priors and good initialization can matter.

---

# 14.26 Why Wrong PSF Can Be Worse Than No Restoration

Suppose the true blur is directional but the restoration algorithm assumes isotropic Gaussian blur.

Then:

```text
model mismatch
→ incorrect inversion
→ artifacts
→ ringing/noise
```

Thus:

> **Restoration is only as good as the degradation model and assumptions behind it.**

---

# 14.27 Motion Deblurring Example

Suppose:

```text
horizontal motion
→ blur horizontally
```

A correct PSF might represent motion along the x-axis.

A Gaussian isotropic blur assumption would not capture the directionality.

The resulting restoration can fail even if the algorithm itself is implemented correctly.

---

# 14.28 Restoration Pipeline

A disciplined restoration pipeline is:

```text
observed image g
      ↓
diagnose degradation
      ↓
choose/model h
      ↓
estimate noise statistics
      ↓
choose restoration method
      ↓
restore
      ↓
range / datatype handling
      ↓
evaluate against reference or task
```

This is more principled than:

```text
try random sharpening
```

---

# 14.29 Restoration Quality Evaluation

When a clean reference exists:

### MSE

\[
MSE=
\frac1{MN}\sum(I-\hat I)^2
\]

### PSNR

\[
PSNR=
10\log_{10}
\left(
\frac{MAX_I^2}{MSE}
\right)
\]

But also inspect:

```text
edge preservation
texture
ringing
noise
```

If no reference exists, evaluation becomes harder and may rely on:

- no-reference metrics,
- task accuracy,
- visual inspection,
- consistency with known system constraints.

---

# 14.30 Worked Restoration Example

Suppose one frequency satisfies:

\[
G=0.42
\]

and:

\[
H=0.7
\]

Ignoring noise:

\[
\hat F=\frac{0.42}{0.7}
\]

\[
\boxed{\hat F=0.6}
\]

Now assume:

\[
K=0.04
\]

in a simplified Wiener expression.

Then:

\[
\hat F_W=
\frac{0.7}
{0.7^2+0.04}
(0.42)
\]

\[
=
\frac{0.7}{0.49+0.04}\times0.42
\]

\[
=
\frac{0.7}{0.53}\times0.42
\]

\[
\approx0.555
\]

The regularized estimate is smaller than the direct inverse estimate.

This is the intended stabilizing behaviour.

---

# 14.31 Interpreting Restoration as an Inverse Problem

The forward process is:

\[
f
\xrightarrow{h}
h*f
\xrightarrow{+\eta}
g
\]

Restoration reverses this:

\[
g
\xrightarrow{\text{model}}
\hat f
\]

But the reverse is not exact because:

```text
noise
+
information attenuation
+
unknown parameters
```

make the inverse uncertain.

This is why a restored image is an **estimate**, not proof of the exact original.

---

# 14.32 Information Loss and Irrecoverability

Suppose a degradation completely suppresses a frequency:

\[
H(u,v)=0
\]

Then:

\[
G(u,v)=N(u,v)
\]

at that location.

The original signal component cannot be recovered from the data alone.

Any estimate must come from:

- priors,
- neighbouring frequencies,
- spatial assumptions,
- statistical structure.

This is the central difference between:

```text
reconstruction
```

and:

```text
guessing with priors
```

A restoration algorithm combines evidence and assumptions.

---

# 14.33 Prior Knowledge

Useful priors can include assumptions such as:

```text
images are usually smooth except at edges
noise is statistically structured
blur kernel has known shape
natural images contain spatial redundancy
```

Different algorithms encode different priors.

This becomes a bridge to modern machine-learning restoration.

---

# 14.34 Classical vs Learned Restoration

### Classical

```text
explicit degradation model
+
explicit regularizer/statistics
```

### Learned

```text
data
+
model/training
→
learned mapping/prior
```

Modern deep-learning restoration can learn powerful priors, but it can also hallucinate structures when evidence is insufficient.

This is particularly important in high-stakes imaging.

---

# 14.35 Responsible Restoration

A restored image should not be presented as:

> “the true original”

unless the claim is actually supported.

Better language:

```text
restored estimate
model-based reconstruction
deblurred estimate
```

Record:

```text
original input
restoration method
degradation assumptions
parameters
reference/ground truth if available
```

This preserves scientific traceability.

---

# 14.36 Restoration Artifacts

Possible artifacts include:

```text
ringing
oversharpening
noise amplification
haloing
texture distortion
false structures
edge oscillations
```

These are not random annoyances.

They often reveal:

```text
model mismatch
+
unstable inversion
+
over-aggressive regularization choices
```

---

# 14.37 Why Deblurring Can Create Ringing

If the inverse filter aggressively boosts frequencies that were attenuated by blur, it can create oscillations near edges.

Conceptually:

```text
blurred edge
██████▓▓▒░░░

inverse
███████│░│░│
```

This is a classic inverse-filtering artifact.

Regularized filters attempt to control it.

---

# 14.38 Noise-Restoration Tradeoff

Suppose the degradation suppresses high frequencies.

An inverse method tries to restore them:

```text
missing/attenuated detail
→ boost
```

But:

```text
noise at same frequencies
→ also boosted
```

Therefore restoration is fundamentally a tradeoff:

\[
\text{sharpness}
\leftrightarrow
\text{noise amplification}
\]

---

# 14.39 Restoration Parameter Selection

Relevant parameters can include:

```text
PSF size
PSF orientation
noise variance
Wiener K
regularization λ
stopping condition
boundary model
```

Parameter selection should ideally use:

- calibration,
- reference validation,
- cross-validation,
- known imaging physics,
- downstream task evaluation.

---

# 14.40 Boundary Conditions

As with filtering:

```text
image boundaries
→ affect convolution
→ affect frequency model
→ affect restoration
```

Possible assumptions include:

- periodic,
- zero,
- reflective,
- other model-specific boundaries.

A restoration result can change substantially if boundary assumptions change.

---

# 14.41 Practical Deblurring Experiment

A strong lab experiment can create controlled blur:

```text
clean image
    ↓
known Gaussian PSF
    ↓
blurred image
    ↓
optional Gaussian noise
    ↓
inverse filtering
    ↓
Wiener restoration
    ↓
compare to clean image
```

Record:

```text
PSF size
noise level
inverse method
Wiener parameter
MSE
PSNR
visual artifacts
edge sharpness
```

This turns an abstract restoration problem into an experimentally verifiable pipeline.

---

# 14.42 Controlled Motion-Blur Experiment

```text
clean image
   ↓
synthetic motion PSF
   ↓
blurred image
   ↓
add noise
   ↓
estimate/use known PSF
   ↓
restore
   ↓
compare
```

Now compare:

```text
no restoration
inverse filter
Wiener
```

The experiment makes instability visible.

---

# 14.43 Why Inverse Filter Can Win in a Noise-Free Toy Case

Suppose:

```text
PSF perfectly known
noise = 0
H never near zero
```

Then direct inversion may recover the original extremely well.

This is useful educationally.

But once:

```text
noise > 0
or
PSF uncertain
```

the situation changes.

This is why classroom formulas should never be transferred blindly into production imaging systems.

---

# 14.44 Frequency-Domain Restoration Pipeline

```text
g(x,y)
  ↓
FFT
  ↓
G(u,v)

estimate H(u,v)
estimate noise model
  ↓
choose:
  inverse
  Wiener
  regularized method
  ↓
construct restoration transfer function
  ↓
multiply
  ↓
inverse FFT
  ↓
real output
  ↓
range handling
  ↓
evaluation
```

---

# 14.45 Common Traps

## Trap 1 — “Restoration is just stronger enhancement.”

False.

Restoration is model-based estimation.

## Trap 2 — “Divide by the blur spectrum and everything is recovered.”

False.

Small \(H\) values amplify noise and zeros make inversion undefined.

## Trap 3 — “Wiener filter always produces a perfect result.”

False.

It depends on model assumptions and parameterization.

## Trap 4 — “A wrong PSF is a small issue.”

False.

Model mismatch can dominate the result.

## Trap 5 — “If the image looks sharper, restoration succeeded.”

Not necessarily.

Sharpness may come from noise, ringing or false detail.

## Trap 6 — “Blur and noise are the same.”

False.

Blur mixes/attenuates spatial information; noise introduces uncertainty.

## Trap 7 — “A restored image is the original image.”

False.

It is generally an estimate conditioned on a model and data.

## Trap 8 — “No reference image means restoration quality can be judged by eye alone.”

False.

No-reference situations are harder and require appropriate domain/task evaluation.

---

# 14.46 Exam Formula Sheet

### Degradation model

\[
\boxed{
g=h*f+\eta
}
\]

### Frequency-domain degradation

\[
\boxed{
G=HF+N
}
\]

### Inverse filter

\[
\boxed{
\hat F=\frac{G}{H}
}
\]

when \(H\ne0\) and the model permits it.

### Wiener-style filter

\[
\boxed{
\hat F=
\frac{H^*}{|H|^2+K}G
}
\]

for the simplified common formulation.

### MSE

\[
\boxed{
MSE=
\frac1{MN}
\sum(I-\hat I)^2
}
\]

### PSNR

\[
\boxed{
PSNR=
10\log_{10}
\frac{MAX_I^2}{MSE}
}
\]

### Regularized inverse-problem form

\[
\boxed{
\hat f=
\arg\min_f
\left[
\|Hf-g\|_2^2+
\lambda\|Lf\|_2^2
\right]
}
\]

---

# 14.47 Exam-Style Problem — Inverse Filtering

Given:

\[
G=0.8,\qquad H=0.4
\]

Ignoring noise:

\[
\hat F=\frac{0.8}{0.4}
\]

\[
\boxed{\hat F=2}
\]

The value can exceed the observed magnitude because the system attenuation is being inverted.

---

# 14.48 Exam-Style Problem — Inverse Instability

Suppose:

\[
H=0.01
\]

and noise magnitude is:

\[
N=0.03
\]

The inverse gain is:

\[
\frac1H=100
\]

Therefore the noise contribution after inversion can be approximately:

\[
0.03\times100=3
\]

The noise becomes much larger.

This demonstrates why direct inverse filtering can be unstable.

---

# 14.49 Exam-Style Problem — Wiener Gain

Given:

\[
H=0.5,\qquad K=0.1
\]

Assume \(H\) is real.

Then:

\[
\frac{H^*}{|H|^2+K}
=
\frac{0.5}{0.25+0.1}
\]

\[
=
\frac{0.5}{0.35}
\]

\[
\boxed{\approx1.429}
\]

The corresponding direct inverse gain would be:

\[
2
\]

so the Wiener form is less aggressive under this parameter choice.

---

# 14.50 Restoration Decision Tree

```text
OBSERVED DEGRADATION
        │
        ├── mainly random noise?
        │       ↓
        │   denoising candidate
        │
        ├── known blur + low noise?
        │       ↓
        │   inverse/deconvolution candidate
        │
        ├── known blur + significant noise?
        │       ↓
        │   Wiener / regularized restoration
        │
        ├── unknown blur?
        │       ↓
        │   estimate PSF / blind deconvolution
        │
        └── uncertain degradation?
                ↓
        diagnose/model first
```

---

# 14.51 Enhancement → Filtering → Restoration

The end of Part II now forms a coherent progression:

```text
C06
INTENSITY TRANSFORMATION
        ↓
C07
HISTOGRAM
        ↓
C08
SPATIAL FILTER
        ↓
C09
NOISE REDUCTION
        ↓
C10
SHARPENING / EDGE
        ↓
C11
GEOMETRIC RESAMPLING
        ↓
C12
FOURIER REPRESENTATION
        ↓
C13
FREQUENCY FILTERING
        ↓
C14
RESTORATION
```

The intellectual progression is:

```text
modify values
→ understand distributions
→ use neighbourhoods
→ diagnose noise
→ emphasize structure
→ move coordinates
→ change mathematical representation
→ selectively filter frequencies
→ solve an inverse problem
```

This completes the classical enhancement/processing portion of the MiniBook.

---

# 14.52 Cross-Book Bridges

> **C09 BRIDGE**  
> Noise models and PSNR/MSE provide the quantitative basis for evaluating restoration.

> **C12 BRIDGE**  
> The frequency-domain degradation model is built directly on the DFT/FFT representation.

> **C13 BRIDGE**  
> Frequency filtering explains why inverse filtering works—and why it fails when \(H\) is small.

> **C08 BRIDGE**  
> Spatial convolution and the PSF form the forward degradation model.

> **C11 BRIDGE**  
> Geometric blur such as motion depends on coordinate motion and resampling concepts.

> **C21–C24 BRIDGE**  
> Transform-domain thinking later reappears in compression, where the objective is efficient representation rather than restoration.

> **C31 BRIDGE**  
> Responsible restoration requires provenance, uncertainty awareness and careful claims about reconstructed information.

> **LAB BRIDGE**  
> Generate controlled blur/noise, estimate/use a PSF, compare inverse and Wiener restoration quantitatively.

> **PRACTICE BRIDGE**  
> Solve degradation-model equations, inverse-filter stability questions, Wiener calculations and model-selection problems.

> **EXAM BRIDGE**  
> Know the degradation model, inverse filtering, instability at small \(H\), Wiener filtering, PSF, regularization and enhancement-vs-restoration distinction.

---

# 14.53 Quick Recall

```text
DEGRADATION
g = h*f + η

FREQUENCY MODEL
G = HF + N

INVERSE
F̂ = G/H

PROBLEM
small |H|
→ noise amplification

WIENER
H* / (|H|² + K)

CORE IDEA
restoration = model-based estimation
```

The most important sentence:

> **A restoration algorithm does not recover “the truth” automatically; it estimates an underlying image under assumptions about the degradation and the data.**

---

# 14.54 Chapter Checkpoint

1. Distinguish enhancement and restoration.
2. Write the degradation model.
3. Interpret each term in \(g=h*f+\eta\).
4. Derive the frequency-domain degradation model.
5. Explain inverse filtering.
6. Why does inverse filtering amplify noise when \(|H|\) is small?
7. What happens when \(H=0\)?
8. Define the point-spread function.
9. Give examples of motion and defocus blur.
10. Write the common simplified Wiener filter equation.
11. Explain the role of \(K\).
12. Compare inverse and Wiener filtering.
13. Define an ill-conditioned inverse problem.
14. Explain regularization.
15. What is blind deconvolution?
16. Why can a wrong PSF produce a poor restoration?
17. Why is a restored image an estimate rather than necessarily the original?
18. How should restoration be evaluated?
19. Design a controlled deblurring experiment.
20. Explain the tradeoff between sharpness and noise amplification.

---

# 14.55 Part II Completion Gate

Before moving to Part III, the student should be able to look at an image problem and classify it:

```text
Need simple intensity adjustment?
→ C06

Need distribution-based contrast control?
→ C07

Need local neighbourhood operation?
→ C08

Need noise suppression?
→ C09

Need stronger edges/detail?
→ C10

Need resize/rotate/warp?
→ C11

Need spectral analysis?
→ C12

Need frequency-selective filtering?
→ C13

Need model-based deblurring/restoration?
→ C14
```

This classification skill is more important than memorizing isolated algorithms.

---

# 14.56 Part III Preview

The next part changes the question.

Part II asked:

```text
How can we improve or reconstruct the image?
```

Part III asks:

```text
How can we understand what is inside the image?
```

The progression becomes:

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

This moves the MiniBook from **image processing** toward **image analysis and computer vision**.
