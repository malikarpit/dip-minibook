---
id: "C12"
title: "Fourier Transform and the Frequency Domain"
layer: "MAIN"
part: "II — Improving the Image"
unit: "II"
version: "1.0"
status: "REFERENCE BUILD"
syllabus_scope:
  - "Fourier transform"
  - "Frequency-domain representation"
  - "Spatial frequency"
tags:
  - "CORE"
  - "EXAM"
  - "MATH"
  - "DEEP DIVE"
  - "LAB"
  - "FREQUENCY"
  - "FOURIER"
prerequisites:
  - "C03"
  - "C08"
  - "C09"
  - "C10"
  - "C11"
related:
  - "C07"
  - "C13"
  - "C14"
  - "C21"
  - "C23"
  - "C24"
math:
  - "M09"
  - "M10"
  - "M11"
  - "M12"
lab:
  - "LAB-U2-03"
  - "LAB-U2-05"
exam:
  - "EXAM-U2"
practice:
  - "P-C12"
assets:
  - "D-C12-01"
  - "D-C12-02"
  - "D-C12-03"
---

# Chapter 12 — Fourier Transform and the Frequency Domain

> **Chapter thesis**  
> The spatial domain describes image values by location. The frequency domain describes how rapidly those values vary across space. The Fourier transform provides a mathematical change of representation that makes periodic structure, low/high spatial frequencies and many filtering operations easier to analyze.

**Part II — Improving the Image**

> **Syllabus anchor:** Unit II explicitly includes Fourier analysis/frequency-domain processing and low-, high- and band-pass filtering. fileciteturn4file0L36-L40

---

# 12.0 Why Leave the Spatial Domain?

Suppose an image contains:

```text
smooth background
+
fine texture
+
periodic interference
```

In the spatial domain these may overlap visually.

The frequency domain provides another viewpoint:

```text
slow spatial variation
→ low frequencies

rapid spatial variation
→ high frequencies

repeating patterns
→ structured spectral components
```

This creates a powerful analysis pipeline:

```text
IMAGE
  ↓
FOURIER TRANSFORM
  ↓
FREQUENCY SPECTRUM
  ↓
ANALYZE / FILTER
  ↓
INVERSE FOURIER TRANSFORM
  ↓
IMAGE
```

---

# 12.1 Spatial Frequency Revisited

From C03:

```text
low spatial frequency
→ slow variation

high spatial frequency
→ rapid variation
```

Examples:

### Low frequency

```text
████████
████████
▓▓▓▓▓▓▓▓
░░░░░░░░
```

### High frequency

```text
█░█░█░█░
░█░█░█░█
█░█░█░█░
```

A real image contains a mixture of spatial frequencies.

The Fourier transform decomposes that mixture into frequency components.

---

# 12.2 The 1-D Fourier Transform

For a continuous 1-D signal:

\[
F(u)
=
\int_{-\infty}^{\infty}
f(x)e^{-i2\pi ux}\,dx
\]

where:

- \(f(x)\) = spatial-domain signal,
- \(u\) = frequency variable,
- \(i=\sqrt{-1}\).

The inverse transform is:

\[
f(x)
=
\int_{-\infty}^{\infty}
F(u)e^{i2\pi ux}\,du
\]

The transform is therefore a change of representation, not necessarily a loss of information.

---

# 12.3 Why Complex Numbers Appear

Fourier analysis uses:

\[
e^{i\theta}
=
\cos\theta+i\sin\theta
\]

via Euler's formula.

So Fourier coefficients are generally complex.

A coefficient contains:

```text
magnitude
+
phase
```

These two parts encode different information.

---

# 12.4 Magnitude and Phase

For a complex spectrum:

\[
F(u)=A(u)+iB(u)
\]

the magnitude is:

\[
|F(u)|
=
\sqrt{A(u)^2+B(u)^2}
\]

The phase is:

\[
\phi(u)
=
\operatorname{atan2}(B(u),A(u))
\]

Therefore:

```text
Fourier coefficient
→ magnitude
→ phase
```

A magnitude-only display is not the complete Fourier transform.

---

# 12.5 2-D Fourier Transform

A continuous 2-D Fourier transform can be written:

\[
F(u,v)
=
\int\int
f(x,y)
e^{-i2\pi(ux+vy)}
\,dx\,dy
\]

The inverse is:

\[
f(x,y)
=
\int\int
F(u,v)
e^{i2\pi(ux+vy)}
\,du\,dv
\]

For digital images, we use the discrete version.

---

# 12.6 2-D Discrete Fourier Transform

For an \(M\times N\) image:

\[
F(u,v)
=
\sum_{x=0}^{M-1}
\sum_{y=0}^{N-1}
f(x,y)
e^{-i2\pi
\left(
\frac{ux}{M}
+
\frac{vy}{N}
\right)}
\]

for:

\[
u=0,\ldots,M-1
\]

\[
v=0,\ldots,N-1
\]

This is the **2-D Discrete Fourier Transform (DFT)**.

---

# 12.7 Inverse 2-D DFT

The inverse is:

\[
f(x,y)
=
\frac{1}{MN}
\sum_{u=0}^{M-1}
\sum_{v=0}^{N-1}
F(u,v)
e^{i2\pi
\left(
\frac{ux}{M}
+
\frac{vy}{N}
\right)}
\]

The factor:

\[
\frac1{MN}
\]

appears in this common convention.

> **Convention note:** Some software/discussions distribute normalization factors differently between forward and inverse transforms. Always follow the chosen convention consistently.

---

# 12.8 What Does Each Frequency Mean?

The pair:

\[
(u,v)
\]

describes a spatial-frequency component.

Conceptually:

```text
small |u|, |v|
→ broad / slowly varying patterns

large |u|, |v|
→ fine / rapidly varying patterns
```

The orientation in the frequency plane also contains information about the orientation of the corresponding spatial pattern.

---

# 12.9 Frequency Domain Visualization

A raw spectrum often has very large values near the origin.

A common visualization uses:

\[
D(u,v)=\log\left(1+|F(u,v)|\right)
\]

This compresses the dynamic range of spectral magnitudes for display.

It is a visualization transformation.

It does not mean that the Fourier spectrum itself has been logarithmically altered in the filtering algorithm.

---

# 12.10 DC Component

The zero-frequency component is:

\[
F(0,0)
\]

It represents the image's average/constant component under the chosen DFT convention.

For an image:

\[
F(0,0)
=
\sum_x\sum_y f(x,y)
\]

Therefore:

\[
\frac{F(0,0)}{MN}
\]

is the mean image value under this convention.

---

# 12.11 Worked DC Example

Consider:

\[
I=
\begin{bmatrix}
10&20\\
30&40
\end{bmatrix}
\]

Then:

\[
F(0,0)
=
10+20+30+40
=
100
\]

Image mean:

\[
\mu=\frac{100}{4}=25
\]

Therefore:

\[
\boxed{
\frac{F(0,0)}{4}=25
}
\]

---

# 12.12 Frequency Spectrum and Constant Images

Suppose:

\[
f(x,y)=C
\]

for every pixel.

This image contains only a DC/zero-frequency component in the ideal discrete periodic representation.

Conceptually:

```text
constant image
→ no spatial variation
→ only zero-frequency energy
```

This is one of the most useful sanity checks for understanding Fourier transforms.

---

# 12.13 What Does a Smooth Image Look Like?

A smooth image has predominantly low-frequency content.

Conceptually:

```text
spatial image
████████
▓▓▓▓▓▓▓▓
░░░░░░░░

spectrum
      *
    ***
   *****
```

Most energy is concentrated relatively near the low-frequency region.

---

# 12.14 What Does a Fine Texture Look Like?

Rapid repeated changes produce higher-frequency components.

```text
image:
█░█░█░█░█░█

spectrum:
     •     •
   •   • •   •
```

The exact spectrum depends on frequency, phase, orientation and boundary effects.

---

# 12.15 Orientation in the Fourier Domain

A sinusoidal pattern in one spatial direction produces spectral energy along a related direction in frequency space.

The spectrum provides information about:

- dominant spatial frequency,
- orientation,
- periodicity.

This is why periodic noise can be easier to isolate in frequency space.

---

# 12.16 Separable 2-D DFT

A 2-D DFT can be computed using successive 1-D transforms.

Conceptually:

```text
rows
 ↓
1-D DFT
 ↓
columns
 ↓
1-D DFT
 ↓
2-D DFT
```

This separability is important computationally.

---

# 12.17 DFT vs FFT

### DFT

The mathematical transform:

\[
F(u,v)
\]

### FFT

A family of algorithms for computing the DFT efficiently.

Therefore:

> FFT is not a different transform from the DFT; it is an efficient computation strategy for the DFT under applicable conditions.

---

# 12.18 Complexity

A direct 1-D DFT is roughly:

\[
O(N^2)
\]

for \(N\) samples.

A typical FFT algorithm can reduce this to approximately:

\[
O(N\log N)
\]

under its applicable structure.

For 2-D images, separability plus efficient 1-D FFTs makes large transforms practical.

This is why frequency-domain image processing is computationally feasible.

---

# 12.19 Worked 1-D DFT Example

Consider:

\[
f=[1,0,1,0]
\]

For the 4-point DFT:

\[
F(k)=\sum_{n=0}^{3}f[n]e^{-i2\pi kn/4}
\]

### \(k=0\)

\[
F(0)=1+0+1+0=2
\]

### \(k=1\)

\[
F(1)
=
1+1e^{-i\pi}
\]

because the other terms are multiplied by zero.

Since:

\[
e^{-i\pi}=-1
\]

we get:

\[
F(1)=1-1=0
\]

### \(k=2\)

\[
F(2)
=
1+1e^{-i2\pi}
\]

and:

\[
e^{-i2\pi}=1
\]

so:

\[
F(2)=2
\]

### \(k=3\)

Similarly:

\[
F(3)=0
\]

Therefore:

\[
\boxed{F=[2,0,2,0]}
\]

This makes sense because the original sequence contains a strong alternating pattern.

---

# 12.20 Why Fourier Coefficients Can Be Complex

The image is real-valued, but the basis functions contain:

\[
e^{-i\theta}
\]

Therefore the transform is generally complex.

For real images, the DFT exhibits conjugate symmetry:

\[
F(u,v)
=
F^*((-u)\bmod M,(-v)\bmod N)
\]

under the standard DFT indexing convention.

This means positive/negative frequency components are not independent in the same way they are for arbitrary complex-valued signals.

---

# 12.21 Centered Spectrum

Many visualizations shift the zero-frequency component to the centre.

Conceptually:

```text
raw FFT display

DC
*


centered display

      *
      ↑
     DC
```

A common operation is called **FFT shift** or spectrum centering.

This changes display/index arrangement, not the underlying transform content.

---

# 12.22 Radial Distance from the Frequency Origin

A radial frequency measure can be written:

\[
D(u,v)
=
\sqrt{
(u-u_0)^2+(v-v_0)^2
}
\]

where \((u_0,v_0)\) is the chosen spectral centre.

This is useful for defining circular filters:

```text
small D
→ low frequency

large D
→ high frequency
```

---

# 12.23 Low-Pass Filtering in Frequency Domain

A frequency-domain filter is represented by a transfer function:

\[
H(u,v)
\]

The filtered spectrum is:

\[
G(u,v)=H(u,v)F(u,v)
\]

A low-pass filter preserves low frequencies and suppresses high frequencies.

Conceptually:

```text
FREQUENCY SPECTRUM
      ↓
   H(u,v)
      ↓
low frequencies kept
high frequencies reduced
```

This generally produces smoothing in the spatial domain.

---

# 12.24 High-Pass Filtering

A high-pass filter suppresses low frequencies and preserves/emphasizes higher-frequency components.

Conceptually:

```text
low frequencies
→ suppressed

high frequencies
→ preserved/emphasized
```

This tends to highlight:

- edges,
- fine detail,
- rapid intensity changes.

This connects directly to C10.

---

# 12.25 Band-Pass Filtering

A band-pass filter retains a selected frequency band.

Conceptually:

```text
low frequencies
→ reject

middle band
→ keep

high frequencies
→ reject
```

This can be useful for detecting structures associated with a particular spatial scale.

---

# 12.26 Frequency-Domain Pipeline

```text
input image
    ↓
optional preprocessing
    ↓
DFT / FFT
    ↓
spectrum
    ↓
design H(u,v)
    ↓
multiply:
G=HF
    ↓
inverse DFT / FFT
    ↓
real-valued output handling
    ↓
display / evaluation
```

C13 develops the filter designs in detail.

---

# 12.27 Multiplication in Frequency Domain

The central operation is:

\[
G(u,v)=H(u,v)F(u,v)
\]

This is powerful because:

```text
spatial convolution
↔
frequency multiplication
```

under the appropriate Fourier/convolution convention.

Thus a potentially expensive convolution operation can sometimes be analyzed or implemented through the frequency domain.

---

# 12.28 Convolution Theorem

The convolution theorem states, under standard transform conventions:

\[
f*h
\quad\Longleftrightarrow\quad
FH
\]

That is:

```text
convolution in spatial domain
↔
multiplication in frequency domain
```

and:

```text
multiplication in spatial domain
↔
convolution in frequency domain
```

This is one of the most important bridges in image processing.

---

# 12.29 Linear vs Circular Convolution

A DFT naturally corresponds to circular convolution when multiplication is performed directly in the transform domain.

For linear convolution via FFT, suitable zero-padding is generally required.

This distinction is critical.

```text
DFT multiplication
→ circular convolution relationship

linear convolution desired
→ appropriate padding / size handling
```

---

# 12.30 Why Zero Padding Matters

Suppose an image and filter have finite sizes.

If the FFT transform size is too small, circular wrap-around can contaminate the result.

Proper zero-padding can make the circular convolution correspond to the desired linear convolution over the relevant output region.

The required size depends on the image and kernel dimensions and the implementation convention.

---

# 12.31 Frequency-Domain View of Gaussian Smoothing

A Gaussian in the spatial domain transforms to a Gaussian-like function in the frequency domain.

Conceptually:

```text
spatial Gaussian blur
↔
smooth low-pass spectrum
```

This explains why Gaussian smoothing suppresses high frequencies.

---

# 12.32 Frequency-Domain View of Derivatives

Differentiation has a simple Fourier-domain relationship.

For a 1-D signal:

\[
\mathcal{F}
\left\{
\frac{df}{dx}
\right\}
=
i2\pi uF(u)
\]

under the continuous Fourier-transform convention used here.

Therefore:

```text
derivative
→ multiply spectrum by frequency
```

Higher frequencies receive stronger weighting.

This mathematically explains why differentiation is noise-sensitive.

---

# 12.33 Worked Derivative Frequency Intuition

Suppose two spectral components have frequencies:

\[
u_1=1
\]

and:

\[
u_2=10
\]

Derivative magnitude weighting is proportional to:

\[
|u|
\]

Therefore the second component receives approximately:

\[
\frac{10}{1}=10
\]

times the derivative weighting of the first component, all else equal.

This explains why high-frequency noise can become prominent after differentiation.

---

# 12.34 Frequency-Domain View of Integration / Smoothing

Conversely, a low-pass-like operation reduces high-frequency components.

So the duality becomes:

```text
differentiation
→ high-frequency emphasis

smoothing
→ high-frequency suppression
```

This ties C09 and C10 directly to the frequency domain.

---

# 12.35 Periodic Noise in Frequency Domain

Suppose an image contains sinusoidal interference.

In the spatial domain:

```text
repeating stripes
```

In the frequency domain:

```text
distinct spectral peaks
```

This is valuable because the noise can become spatially separated from much of the natural image spectrum.

A targeted notch filter can then suppress those peaks.

Notch filtering is introduced fully in C13.

---

# 12.36 Frequency-Domain Filter Families

Classical families include:

### Ideal

Sharp cutoff.

### Butterworth

Smoother transition controlled by order.

### Gaussian

Very smooth frequency response.

They offer different tradeoffs between:

```text
selectivity
+
spatial ringing
```

C13 will treat these systematically.

---

# 12.37 Ideal Low-Pass Filter

A simple ideal low-pass transfer function is:

\[
H(u,v)=
\begin{cases}
1,&D(u,v)\le D_0\\
0,&D(u,v)>D_0
\end{cases}
\]

where:

\[
D_0
\]

is the cutoff frequency.

It preserves a circular region around the frequency origin.

---

# 12.38 Why Ideal Filters Can Ring

A sharp discontinuity in frequency response can create spatial oscillation artifacts.

This is related to the Fourier-transform duality between:

```text
sharp frequency cutoff
↔
extended/ringing spatial response
```

A classic consequence is Gibbs-like ringing behaviour around sharp intensity transitions.

This is one reason smoother filters such as Gaussian or Butterworth are often preferred in practical image processing.

---

# 12.39 Butterworth Low-Pass

A common form is:

\[
H(u,v)
=
\frac{1}{
1+\left(\frac{D(u,v)}{D_0}\right)^{2n}
}
\]

where:

- \(D_0\) = cutoff,
- \(n\) = filter order.

Higher \(n\) gives a sharper transition.

---

# 12.40 Gaussian Low-Pass

A common form is:

\[
H(u,v)
=
e^{-\frac{D(u,v)^2}{2D_0^2}}
\]

This provides a smooth frequency response.

It is closely related to Gaussian spatial smoothing.

---

# 12.41 High-Pass Construction

A simple high-pass complement is:

\[
H_{HP}(u,v)
=
1-H_{LP}(u,v)
\]

for the corresponding low-pass filter.

This is a conceptual construction.

For some applications, high-boost or other specialized filters are preferable.

---

# 12.42 Worked Low-Pass Filter Example

Suppose:

\[
D_0=10
\]

and a frequency location has:

\[
D=5
\]

For the ideal low-pass:

\[
D\le D_0
\]

so:

\[
H=1
\]

For another point:

\[
D=15
\]

then:

\[
H=0
\]

Thus the ideal filter makes an abrupt decision.

---

# 12.43 Frequency Spectrum Magnitude Does Not Equal Image Brightness

A common misunderstanding is:

> “A bright spot in the spectrum is a bright object in the image.”

False.

Spectrum brightness usually represents transformed frequency magnitude.

The spectrum describes:

```text
how strongly a spatial-frequency component is present
```

not where an object is located in the original image.

Spatial localization and frequency representation are different viewpoints.

---

# 12.44 Phase and Spatial Structure

Magnitude tells us how strong frequency components are.

Phase strongly influences where structures occur spatially.

This is why:

> discarding phase can destroy spatial localization information even if the magnitude spectrum remains unchanged.

Phase is therefore not a minor technical detail.

---

# 12.45 A Useful Mental Experiment

Consider two images with similar magnitude spectra but different phase.

They can have substantially different spatial appearances.

Therefore:

```text
magnitude
→ frequency strength

phase
→ spatial alignment/structure information
```

This is a conceptual rather than a complete reconstruction theorem, but it is an essential intuition.

---

# 12.46 Frequency-Domain Image Processing and Padding

FFT-based filtering often includes:

```text
image
→ pad
→ transform
→ shift/inspect
→ multiply by H
→ inverse transform
→ crop
```

Padding can:

- reduce circular wrap-around,
- create a desired output region,
- improve correspondence with linear convolution.

The correct padding depends on the objective.

---

# 12.47 Complex Numerical Output

Due to numerical floating-point effects, inverse FFT of a theoretically real image may contain tiny imaginary components:

\[
2\times10^{-15}i
\]

These can be safely treated as numerical residuals when appropriate.

But large imaginary components are a warning that something may be wrong with:

- spectrum modification,
- symmetry,
- transform convention,
- implementation.

---

# 12.48 Frequency-Domain Debugging

A good implementation should inspect:

```text
input
 ↓
FFT magnitude
 ↓
filter H
 ↓
filtered spectrum
 ↓
inverse FFT
 ↓
real output
```

Potential diagnostic clues:

```text
spectrum looks wrong
→ transform/centering issue

spectrum correct, output wrong
→ filter multiplication/inverse issue

output has large imaginary component
→ symmetry/convention problem
```

---

# 12.49 Spatial vs Frequency Domain

| Feature | Spatial domain | Frequency domain |
|---|---|---|
| representation | pixels by location | frequency components |
| natural operation | point/neighbourhood processing | spectral multiplication |
| edge visibility | explicit locally | high-frequency energy |
| periodic noise | may be visually mixed | often isolated peaks |
| convolution | direct local operation | multiplication |
| intuitive geometry | strong | weaker |
| useful analysis | local structure | scale/frequency structure |

The domains are complementary.

---

# 12.50 When Should You Use Which Domain?

### Spatial domain

Good when:

- neighbourhood is small,
- operation is local,
- geometric context matters,
- simple filtering is sufficient.

### Frequency domain

Good when:

- periodic interference exists,
- large convolution kernels are involved,
- frequency-selective filtering is desired,
- spectral structure is informative.

The best domain is task-dependent.

---

# 12.51 Worked Conceptual Example — Periodic Interference

Suppose an image contains:

```text
building image
+
horizontal repeating stripes
```

Spatial approach:

```text
try blur
→ stripes may weaken
→ building edges also weaken
```

Frequency approach:

```text
FFT
→ identify spectral peaks
→ notch those frequencies
→ inverse FFT
```

This can provide more targeted suppression.

---

# 12.52 Frequency Domain and Downsampling

C03 established:

```text
downsampling
→ risk of aliasing
```

Frequency domain explains why.

Before reducing sampling rate:

```text
high frequencies that exceed the new Nyquist limit
→ must be attenuated
```

Conceptually:

```text
source spectrum
      ↓
low-pass
      ↓
safe bandwidth
      ↓
downsample
```

This is a powerful connection across chapters.

---

# 12.53 Sampling Theorem Connection

For a band-limited continuous signal:

\[
f_s>2f_{\max}
\]

is the classical ideal sampling condition.

In the frequency domain, sampling creates spectral replicas separated by the sampling frequency.

Conceptually:

```text
original spectrum
      ↓
sampling
      ↓
repeated spectral copies
```

If the copies overlap:

```text
aliasing
```

occurs.

---

# 12.54 Spectral Replication Intuition

Imagine:

```text
        original
          ███
          ███

after sampling:

███       ███       ███
███       ███       ███
```

As sampling frequency decreases, the copies move closer.

Eventually they overlap.

That is the frequency-domain picture of aliasing.

---

# 12.55 Why Anti-Aliasing Works

An anti-alias filter removes frequencies that would overlap after sampling.

Conceptually:

```text
wide source spectrum
      ↓
low-pass
      ↓
narrow safe spectrum
      ↓
sampling
      ↓
separated replicas
```

This makes the C03 Nyquist discussion tangible.

---

# 12.56 DFT Resolution

For a 1-D sampled signal with \(N\) samples and sampling frequency \(f_s\), the frequency-bin spacing is:

\[
\Delta f=\frac{f_s}{N}
\]

under the standard DFT frequency-grid interpretation.

Therefore increasing \(N\), for a fixed \(f_s\), gives finer frequency-bin spacing.

---

# 12.57 Worked Frequency-Bin Example

Suppose:

\[
f_s=1000\text{ Hz}
\]

and:

\[
N=500
\]

Then:

\[
\Delta f=\frac{1000}{500}
\]

\[
\boxed{\Delta f=2\text{ Hz}}
\]

This means adjacent DFT frequency bins are separated by 2 Hz under the chosen interpretation.

---

# 12.58 Spatial-Frequency Units

In images, frequency may be expressed as:

- cycles/pixel,
- cycles/mm,
- line pairs/mm,
- normalized spatial frequency.

The unit matters.

A statement such as:

\[
0.2\text{ cycles/pixel}
\]

describes a digital spatial frequency.

Physical units require knowledge of the physical sampling scale.

---

# 12.59 Zero Frequency Is Relative to the Coordinate Convention

Whether the DC term is displayed at the corner or centre depends on the visualization/index arrangement.

The underlying zero-frequency component is still:

\[
F(0,0)
\]

before shifting.

This matters when writing code that constructs filters.

---

# 12.60 Common Traps

## Trap 1 — “FFT is a different transform from DFT.”

False.

FFT is an efficient algorithm for computing the DFT.

## Trap 2 — “Bright spectrum spot means bright object.”

False.

It indicates strong frequency magnitude.

## Trap 3 — “Magnitude spectrum contains all spatial information.”

Not generally.

Phase is important.

## Trap 4 — “Fourier transform only works on periodic images.”

False.

The DFT represents finite sampled signals; periodic extension is inherent in some mathematical interpretations of the DFT.

## Trap 5 — “Low frequencies mean dark pixels.”

False.

Low frequency means slow spatial variation.

## Trap 6 — “High-pass filtering only detects edges.”

Not exclusively.

It emphasizes high-frequency content, including texture and noise.

## Trap 7 — “DFT multiplication always gives linear convolution.”

False without appropriate padding/interpretation.

## Trap 8 — “The inverse FFT output should never contain a tiny imaginary term.”

Numerical floating-point effects can produce tiny residual imaginary values.

---

# 12.61 Exam Formula Sheet

### 2-D DFT

\[
\boxed{
F(u,v)
=
\sum_{x=0}^{M-1}
\sum_{y=0}^{N-1}
f(x,y)
e^{-i2\pi
\left(
\frac{ux}{M}
+
\frac{vy}{N}
\right)}
}
\]

### Inverse DFT

\[
\boxed{
f(x,y)
=
\frac1{MN}
\sum_u\sum_v
F(u,v)
e^{i2\pi
\left(
\frac{ux}{M}
+
\frac{vy}{N}
\right)}
}
\]

### Magnitude

\[
\boxed{
|F|=\sqrt{\Re(F)^2+\Im(F)^2}
}
\]

### Phase

\[
\boxed{
\phi=\operatorname{atan2}
(\Im F,\Re F)
}
\]

### Frequency-domain filtering

\[
\boxed{
G=HF
}
\]

### Ideal low-pass

\[
\boxed{
H=
\begin{cases}
1,&D\le D_0\\
0,&D>D_0
\end{cases}
}
\]

### Butterworth low-pass

\[
\boxed{
H=
\frac{1}{
1+(D/D_0)^{2n}
}
}
\]

### Gaussian low-pass

\[
\boxed{
H=e^{-D^2/(2D_0^2)}
}
\]

### Frequency-bin spacing

\[
\boxed{
\Delta f=\frac{f_s}{N}
}
\]

---

# 12.62 Exam-Style Problem — DC Value

Given:

\[
I=
\begin{bmatrix}
2&4\\
6&8
\end{bmatrix}
\]

find \(F(0,0)\) and the mean.

\[
F(0,0)=2+4+6+8=20
\]

Mean:

\[
\mu=\frac{20}{4}=5
\]

Therefore:

\[
\boxed{F(0,0)=20,\quad\mu=5}
\]

---

# 12.63 Exam-Style Problem — Ideal Low-Pass

Suppose:

\[
D_0=15
\]

For:

\[
D=8
\]

\[
H=1
\]

For:

\[
D=20
\]

\[
H=0
\]

Therefore the ideal filter passes the first frequency location and rejects the second.

---

# 12.64 Exam-Style Problem — Frequency Bin

A 1-D signal is sampled at:

\[
f_s=800\text{ Hz}
\]

with:

\[
N=400
\]

Then:

\[
\Delta f=\frac{800}{400}=2\text{ Hz}
\]

So:

\[
\boxed{2\text{ Hz}}
\]

---

# 12.65 Engineering Insight — Think in Representations

A useful DIP habit is to ask:

```text
What is difficult to see here?
```

Then choose the representation.

For:

```text
local blur
```

spatial filtering may be easiest.

For:

```text
periodic interference
```

frequency representation may be easier.

For:

```text
shape alignment
```

geometric coordinates may be easier.

This is one of the central engineering ideas of image processing:

> **Change representation when the next operation becomes easier in another domain.**

---

# 12.66 Cross-Book Bridges

> **C03 BRIDGE**  
> Sampling theory, aliasing and Nyquist become intuitive through spectral replication.

> **C08 BRIDGE**  
> Spatial convolution corresponds to frequency multiplication under the convolution theorem.

> **C09 BRIDGE**  
> Smoothing suppresses high-frequency variation.

> **C10 BRIDGE**  
> Derivatives emphasize high-frequency components, explaining noise amplification.

> **C13 BRIDGE**  
> Frequency-domain low-, high-, band- and notch-filter designs are developed fully next.

> **C14 BRIDGE**  
> Degradation models such as blur can be represented using frequency responses.

> **C21–C24 BRIDGE**  
> DCT-based compression is conceptually related to transform-domain representation but is not identical to the DFT.

> **LAB BRIDGE**  
> Compute FFT/DFT, visualize magnitude/phase, apply low/high-pass masks and reconstruct the image.

> **PRACTICE BRIDGE**  
> Solve DFT calculations, DC/mean relationships, frequency-bin problems and filter-response reasoning.

> **EXAM BRIDGE**  
> Know the 2-D DFT/IDFT equations, magnitude/phase, DC component, FFT vs DFT, convolution theorem, and frequency-domain filter concepts.

---

# 12.67 Quick Recall

```text
SPATIAL DOMAIN
→ where values occur

FREQUENCY DOMAIN
→ how rapidly values vary

DFT
→ discrete frequency representation

FFT
→ efficient DFT computation

MAGNITUDE
→ strength of frequency component

PHASE
→ spatial alignment/structure information

LOW-PASS
→ suppress high frequencies

HIGH-PASS
→ suppress low frequencies

G=HF
→ frequency-domain filtering
```

Core rule:

> **Frequency describes variation across space; it does not directly describe object location.**

---

# 12.68 Chapter Checkpoint

1. Why is a frequency-domain representation useful?
2. Define spatial frequency.
3. Write the 2-D DFT equation.
4. Write the inverse DFT equation.
5. What are magnitude and phase?
6. What does the DC component represent?
7. Calculate the DC component and mean for a small matrix.
8. Explain why the DFT is complex-valued.
9. Differentiate DFT and FFT.
10. What is spectrum centering?
11. Explain low-, high- and band-pass filtering.
12. State the convolution theorem.
13. Why is zero-padding important in FFT-based linear convolution?
14. Why can ideal frequency filters cause ringing?
15. Why are periodic noise patterns often easier to detect in the frequency domain?
16. Explain spectral replication and aliasing.
17. Calculate DFT frequency-bin spacing.
18. Why is phase important?
19. Why does differentiation emphasize high frequencies?
20. What is the difference between spatial-domain and frequency-domain processing?

---

# 12.69 Unit II Transition

The full conceptual flow is now:

```text
C06
INTENSITY
   ↓
C07
HISTOGRAM
   ↓
C08
NEIGHBOURHOOD
   ↓
C09
NOISE
   ↓
C10
DERIVATIVES / EDGES
   ↓
C11
GEOMETRY
   ↓
C12
FREQUENCY REPRESENTATION
```

Next:

```text
C13
FREQUENCY-DOMAIN FILTERING
   ↓
C14
IMAGE RESTORATION + DEBLURRING
```

The key shift is:

```text
C12
understand the spectrum

C13
design operations on the spectrum

C14
use a degradation model to recover a better estimate
```
