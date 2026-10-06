---
id: "C13"
title: "Frequency-Domain Filtering"
layer: "MAIN"
part: "II — Improving the Image"
unit: "II"
version: "1.0"
status: "REFERENCE BUILD"
syllabus_scope:
  - "Frequency-domain filtering"
  - "Low-pass filters"
  - "High-pass filters"
  - "Band-pass filtering"
  - "Frequency-domain enhancement"
tags:
  - "CORE"
  - "EXAM"
  - "MATH"
  - "DEEP DIVE"
  - "LAB"
  - "FOURIER"
  - "FILTER DESIGN"
prerequisites:
  - "C08"
  - "C09"
  - "C10"
  - "C12"
related:
  - "C07"
  - "C11"
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
  - "P-C13"
assets:
  - "D-C13-01"
  - "D-C13-02"
  - "D-C13-03"
---

# Chapter 13 — Frequency-Domain Filtering

> **Chapter thesis**  
> Once an image has been represented in the frequency domain, filtering becomes the design and application of a frequency response \(H(u,v)\). Low-pass filtering suppresses rapid variation, high-pass filtering emphasizes it, and band/notch designs allow more selective control. The difficult part is not multiplying two arrays—it is choosing a response that improves the task without creating unacceptable spatial artifacts.

**Part II — Improving the Image**  
**Syllabus anchor:** Unit II explicitly includes Fourier/frequency-domain processing and low-pass, high-pass and band-pass filtering. fileciteturn4file0L36-L40

---

# 13.0 From Fourier Analysis to Filtering

C12 answered:

> What frequencies are present?

C13 asks:

> Which frequencies should remain?

The core equation is:

\[
G(u,v)=H(u,v)F(u,v)
\]

where:

- \(F(u,v)\) = input spectrum,
- \(H(u,v)\) = filter/transfer function,
- \(G(u,v)\) = filtered spectrum.

Then:

\[
g(x,y)=\mathcal{F}^{-1}\{G(u,v)\}
\]

So the full operation is:

```text
input image
     ↓
DFT / FFT
     ↓
frequency spectrum F
     ↓
design H(u,v)
     ↓
multiply F × H
     ↓
inverse DFT / FFT
     ↓
output image
```

This is the frequency-domain counterpart of spatial filtering.

---

# 13.1 What Is a Frequency-Domain Filter?

A frequency-domain filter assigns a response to each frequency location.

Conceptually:

```text
frequency
    ↓
H(u,v)
    ↓
how much of that frequency to keep
```

Examples:

```text
H = 1
→ preserve

H = 0
→ reject

0 < H < 1
→ attenuate
```

A filter therefore does not need to be binary.

---

# 13.2 Transfer Function

The function:

\[
H(u,v)
\]

is called a frequency response or transfer function in this context.

It describes the filter's gain at each frequency coordinate.

For a real symmetric low-pass filter:

```text
centre
→ high response

farther from centre
→ lower response
```

For a high-pass filter:

```text
centre
→ low response

farther from centre
→ high response
```

The exact filter shape determines how gradually or sharply the transition occurs.

---

# 13.3 Frequency Coordinates and the Origin

Before frequency centering, the zero-frequency component is at the DFT origin:

\[
(0,0)
\]

For visualization and many filter constructions, we shift it to the centre:

```text
corners / raw indexing
        ↓
FFT shift
        ↓
DC at centre
```

Let the centered frequency origin be:

\[
(u_0,v_0)
\]

Then a radial distance can be defined as:

\[
D(u,v)
=
\sqrt{(u-u_0)^2+(v-v_0)^2}
\]

This single quantity is used to construct many radially symmetric filters.

---

# 13.4 Why Distance from the Origin Matters

For a radially symmetric filter:

```text
same distance from DC
→ same response
```

So the filter depends only on:

\[
D
\]

rather than independently on \(u\) and \(v\).

Conceptually:

```text
          high f
             ↑
             │
       ──────┼──────
             │
             ↓
          low f
```

The exact geometry is determined by the frequency coordinate convention.

---

# 13.5 Ideal Low-Pass Filter

The simplest low-pass filter is the ideal low-pass.

\[
H(u,v)=
\begin{cases}
1,&D(u,v)\le D_0\\
0,&D(u,v)>D_0
\end{cases}
\]

where \(D_0\) is the cutoff frequency.

Graphically:

```text
response

1 ─────────┐
           │
0          └────────────→ D
           D0
```

It has a perfectly sharp cutoff.

---

# 13.6 What an Ideal Low-Pass Does

It preserves:

```text
low frequencies
→ broad structures
```

and rejects:

```text
high frequencies
→ fine detail / edges / some noise
```

The spatial result tends to be smoother.

But the perfectly sharp cutoff creates a major problem.

---

# 13.7 Ringing from Sharp Frequency Cutoffs

A very abrupt frequency-domain transition corresponds to an extended oscillatory spatial response.

The result can include:

```text
edge
→ overshoot
→ undershoot
→ ringing
```

This is a classic spatial artifact.

The central engineering lesson is:

> **A sharper frequency cutoff does not necessarily mean a better image.**

---

# 13.8 Butterworth Low-Pass Filter

A common Butterworth low-pass form is:

\[
H(u,v)
=
\frac{1}
{1+\left(\frac{D(u,v)}{D_0}\right)^{2n}}
\]

where:

- \(D_0\) = cutoff parameter,
- \(n\) = order.

The response is smoother than the ideal filter.

---

# 13.9 Effect of Butterworth Order

For low order:

```text
gentler transition
```

For higher order:

```text
sharper transition
```

Conceptually:

```text
response
1 |───────
  |       \
  |        \
  |         \

higher order

1 |────────
  |        \
  |         \
  |          |
  └────────────→ D
           D0
```

As the order increases, ringing can become more pronounced because the transition becomes sharper.

---

# 13.10 Gaussian Low-Pass Filter

A common Gaussian low-pass response is:

\[
H(u,v)
=
e^{-\frac{D(u,v)^2}{2D_0^2}}
\]

This gives a smooth, monotonic response.

There is no abrupt cutoff.

---

# 13.11 Ideal vs Butterworth vs Gaussian

| Property | Ideal LPF | Butterworth LPF | Gaussian LPF |
|---|---|---|---|
| cutoff | abrupt | smooth but controllable | very smooth |
| parameter | \(D_0\) | \(D_0,n\) | \(D_0\) or equivalent scale |
| ringing tendency | strongest | depends on order | low |
| selectivity | very sharp | adjustable | smooth |
| spatial appearance | may show ringing | compromise | smooth blur |

---

# 13.12 Worked Gaussian Filter Example

Suppose:

\[
D_0=10
\]

and:

\[
D=5
\]

Then:

\[
H=e^{-25/(2\cdot100)}
\]

\[
=e^{-0.125}
\]

\[
\approx0.882
\]

So this frequency is attenuated only modestly.

For:

\[
D=20
\]

\[
H=e^{-400/200}
=e^{-2}
\approx0.135
\]

The farther frequency is strongly attenuated.

---

# 13.13 High-Pass Filtering

A high-pass filter suppresses the low-frequency region and preserves higher frequencies.

One simple complement is:

\[
H_{HP}(u,v)=1-H_{LP}(u,v)
\]

for a matching low-pass filter.

Conceptually:

```text
low frequency
→ reject

high frequency
→ keep
```

Spatially, this often emphasizes:

- edges,
- fine detail,
- texture,
- noise.

---

# 13.14 Ideal High-Pass Filter

\[
H(u,v)=
\begin{cases}
0,&D(u,v)\le D_0\\
1,&D(u,v)>D_0
\end{cases}
\]

This is the complement of the ideal low-pass.

The same sharp-cutoff issue remains:

```text
sharp frequency boundary
→ possible ringing
```

---

# 13.15 Butterworth High-Pass

A common Butterworth high-pass can be written:

\[
H(u,v)
=
\frac{1}
{1+\left(\frac{D_0}{D(u,v)}\right)^{2n}}
\]

for \(D(u,v)\ne0\), with the DC point handled appropriately.

This is mathematically complementary to the corresponding Butterworth low-pass form.

---

# 13.16 Gaussian High-Pass

A common Gaussian high-pass is:

\[
H_{HP}(u,v)
=
1-e^{-D^2/(2D_0^2)}
\]

At:

\[
D=0
\]

the response is:

\[
H_{HP}=0
\]

and as \(D\) increases:

\[
H_{HP}\rightarrow1
\]

---

# 13.17 Why High-Pass Filtering Looks Like Edge Enhancement

An edge contains rapid spatial change.

Rapid spatial change corresponds to higher spatial frequencies.

Therefore:

```text
high-pass
→ emphasizes high-frequency content
→ edges become more prominent
```

However:

```text
noise
→ also often contains high-frequency components
```

So high-pass filtering can amplify noise.

---

# 13.18 High-Pass Output Is Not Automatically a Sharpened Image

A pure high-pass filter may produce a detail/edge component centered around zero rather than a visually natural image.

For example:

```text
high-pass result
→ dark/bright signed detail
```

To make a sharpened image:

```text
original + scaled high-pass detail
```

This creates a direct bridge to unsharp masking and high-boost filtering.

---

# 13.19 High-Frequency Emphasis

A general high-frequency emphasis filter can be written conceptually as:

\[
H_{HFE}(u,v)
=
a+bH_{HP}(u,v)
\]

where parameters determine how much original/low-frequency content remains.

A related high-boost interpretation is:

\[
g=Af-f_{\text{blur}}
\]

This can be expressed in frequency-domain form as a suitable transfer function.

---

# 13.20 Band-Pass Filtering

A band-pass filter keeps an interval:

```text
low frequencies
→ reject

middle frequencies
→ keep

high frequencies
→ reject
```

A simple ideal annular band-pass can be written:

\[
H(u,v)=
\begin{cases}
1,&D_1\le D(u,v)\le D_2\\
0,&\text{otherwise}
\end{cases}
\]

where:

\[
D_1<D_2
\]

---

# 13.21 Why Band-Pass Filters Matter

Some structures occur at characteristic spatial scales.

For example:

```text
very broad illumination
→ low frequency

medium-scale pattern
→ middle frequency

fine noise
→ high frequency
```

A band-pass filter can isolate the middle range.

This becomes useful for:

- texture analysis,
- feature enhancement,
- scale-specific detection.

---

# 13.22 Band-Reject / Band-Stop

The complement of a band-pass can reject a frequency band.

Conceptually:

```text
low
→ keep

middle
→ reject

high
→ keep
```

This is often useful for suppressing narrow-band interference.

---

# 13.23 Notch Filtering

> **EXTENSION**

A notch filter rejects localized frequency regions rather than a complete circular band.

This is particularly useful for periodic noise.

Suppose the spectrum contains two symmetric interference peaks:

```text
        •
         \
          ○ DC
         /
        •
```

A pair of notch-reject regions can suppress those specific frequencies.

---

# 13.24 Why Periodic Noise Is a Good Notch-Filter Problem

From C12:

```text
periodic spatial pattern
→ concentrated spectral energy
```

So:

```text
periodic noise
→ spectral peaks
→ notch filter
→ inverse transform
```

This can be much more targeted than broad blurring.

---

# 13.25 Notch Reject Concept

If desired spectral locations are:

\[
(u_k,v_k)
\]

and symmetric counterparts:

\[
(-u_k,-v_k)
\]

we can construct local rejection regions around them.

The exact transfer function can be:

- ideal,
- Butterworth,
- Gaussian-shaped.

The choice controls transition smoothness and residual artifacts.

---

# 13.26 Worked Notch Concept

Suppose the Fourier spectrum shows:

```text
one strong peak at
(+20,+5)

and the conjugate peak near
(-20,-5)
```

A notch-reject filter can attenuate those locations while retaining most other frequencies.

The key is:

```text
targeted rejection
→ preserve unrelated image frequencies
```

---

# 13.27 Low-Pass Cutoff Selection

Choosing:

\[
D_0
\]

is a design problem.

Small cutoff:

```text
strong smoothing
→ more detail loss
```

Large cutoff:

```text
weaker smoothing
→ more detail retained
```

The best cutoff depends on:

- object scale,
- noise level,
- sampling,
- task objective.

There is no universal “correct” cutoff.

---

# 13.28 Filter Transition Width

A hard cutoff:

```text
pass → reject
```

can cause ringing.

A smooth transition:

```text
pass → attenuate gradually → reject
```

often reduces ringing at the cost of a less selective frequency response.

This gives one of the core engineering tradeoffs:

```text
selectivity
↔
spatial artifacts
```

---

# 13.29 Frequency-Domain Filtering Is a Global Operation

A spatial kernel is local.

A frequency-domain filter often modifies the spectrum globally.

This means one frequency coefficient can represent information distributed across the image.

Therefore frequency-domain filtering is not naturally local in spatial coordinates.

This distinction is important when choosing between spatial and frequency approaches.

---

# 13.30 Spatial Filter vs Frequency Filter

| Spatial domain | Frequency domain |
|---|---|
| kernel operates locally | transfer function operates spectrally |
| output depends on neighbourhood | output depends on spectral components |
| convolution direct | multiplication in transform domain |
| intuitive spatial structure | intuitive scale/frequency structure |
| often efficient for small kernels | useful for large/global filters |

Under suitable conditions, the two can represent equivalent linear filtering behaviour.

---

# 13.31 Convolution Theorem Revisited

If:

\[
g=f*h
\]

then:

\[
G=FH
\]

under the corresponding transform convention.

This means frequency-domain filtering is not a completely separate world.

It is another implementation/analysis view of convolution.

---

# 13.32 Large-Kernel Filtering

Suppose a filter has a huge spatial support.

Direct convolution can become expensive.

A frequency-domain approach may be advantageous:

```text
image
→ FFT
filter transfer function
→ multiply
→ inverse FFT
```

The practical crossover depends on:

- image size,
- kernel size,
- implementation,
- hardware,
- repeated filtering.

---

# 13.33 FFT-Based Filtering Workflow

A typical linear-convolution-oriented workflow:

```text
image f
   ↓
pad image
   ↓
construct filter h
   ↓
pad h to compatible size
   ↓
FFT(f)
FFT(h)
   ↓
multiply
   ↓
inverse FFT
   ↓
crop intended region
```

Padding and alignment must be handled correctly.

---

# 13.34 Filter Alignment

The origin of a spatial kernel must correspond correctly to the frequency representation.

A misplaced kernel can introduce a phase shift.

Therefore:

```text
spatial kernel position
→ affects phase
→ affects spatial alignment
```

This is a frequent FFT-filtering implementation pitfall.

---

# 13.35 Why Kernel Shifts Cause Phase Effects

A spatial translation theorem states that shifting a function in space changes its Fourier phase.

Therefore an improperly centered kernel may have:

```text
correct-looking magnitude
+
wrong phase
```

and produce a shifted or otherwise misaligned spatial result.

---

# 13.36 Ideal vs Smooth Filters

Consider a sharp edge.

An ideal frequency filter can create:

```text
edge
→ ringing
```

A Gaussian-type filter:

```text
edge
→ smoother transition
```

A Butterworth filter provides a tunable middle ground.

This is why filter family choice matters.

---

# 13.37 Filter Design by Objective

| Objective | Candidate |
|---|---|
| strong sharp cutoff | ideal |
| tunable transition | Butterworth |
| smooth response / low ringing | Gaussian |
| isolate frequency interval | band-pass |
| suppress narrow periodic interference | notch |
| edge/detail enhancement | high-pass/high-frequency emphasis |

---

# 13.38 Worked Design Example — Gaussian Blur

Suppose:

\[
D_0=15
\]

and two frequency points are:

\[
D=5,\quad D=30
\]

Using:

\[
H=e^{-D^2/(2D_0^2)}
\]

For \(D=5\):

\[
H=e^{-25/450}
\approx e^{-0.0556}
\approx0.946
\]

For \(D=30\):

\[
H=e^{-900/450}=e^{-2}\approx0.135
\]

So the lower frequency passes almost unchanged while the higher frequency is strongly attenuated.

---

# 13.39 Worked Design Example — Butterworth

Let:

\[
D_0=10,\qquad n=2
\]

At:

\[
D=5
\]

\[
H=
\frac{1}
{1+(5/10)^4}
\]

\[
=
\frac{1}{1+0.0625}
\]

\[
\approx0.941
\]

At:

\[
D=20
\]

\[
H=
\frac{1}
{1+(2)^4}
\]

\[
=
\frac1{17}
\]

\[
\approx0.0588
\]

The filter strongly attenuates the higher frequency.

---

# 13.40 Comparing the Same Cutoff

Using:

\[
D_0=10
\]

different families produce different responses at the same \(D\).

Therefore:

```text
D0
does not fully define filter behaviour
```

The family matters.

For Butterworth, order matters.

For other designs, other parameters matter.

---

# 13.41 Frequency-Domain Sharpening

A high-pass component can be added to the original spectrum.

Conceptually:

\[
G=(1+kH_{HP})F
\]

so:

\[
g=
\mathcal{F}^{-1}
\left\{
(1+kH_{HP})F
\right\}
\]

This produces frequency-selective detail enhancement.

It can be more controlled than using a crude ideal high-pass.

---

# 13.42 Relation to Unsharp Masking

Suppose:

\[
H_{LP}
\]

is a low-pass filter.

Then:

\[
H_{HP}=1-H_{LP}
\]

An unsharp/high-boost style filter can therefore be expressed as:

\[
H_{sharp}
=
1+kH_{HP}
\]

or:

\[
H_{sharp}
=
1+k(1-H_{LP})
\]

\[
=(1+k)-kH_{LP}
\]

This mirrors the spatial-domain formula:

\[
g=(1+k)f-kf_{\text{blur}}
\]

The duality is now explicit.

---

# 13.43 Frequency-Domain Noise Reduction

For approximately white high-frequency noise:

```text
low-pass
→ can reduce noise
```

But if noise occupies the same frequency range as important detail:

```text
filter
→ cannot cleanly separate them
```

This is a fundamental limitation.

Frequency filtering works best when desired and undesired components are separable enough in the chosen representation.

---

# 13.44 Frequency-Domain Filtering and SNR

If filtering suppresses more noise than useful signal, the effective signal-to-noise ratio can improve.

But filtering can also:

```text
reduce noise
+
reduce signal detail
```

Therefore SNR alone is not always sufficient.

Task-specific fidelity still matters.

---

# 13.45 Frequency-Domain Filtering for Periodic Noise

A good engineering workflow:

```text
noisy image
     ↓
FFT
     ↓
inspect magnitude spectrum
     ↓
identify isolated interference peaks
     ↓
design notch filter
     ↓
multiply
     ↓
inverse FFT
     ↓
inspect residual noise + ringing
```

This is one of the strongest classical examples of domain selection.

---

# 13.46 Frequency-Domain Filtering and Edges

Edges are high-frequency structures.

Therefore low-pass filtering reduces edge sharpness.

High-pass filtering emphasizes edge response.

A well-designed sharpening filter can increase apparent edge contrast without preserving all high frequencies equally.

This lets us trade:

```text
sharpness
↔
noise/artifacts
```

---

# 13.47 Boundary Effects

DFT-based filtering implicitly works with periodic extension of the finite array under the standard interpretation.

If the image boundaries do not match smoothly, artificial discontinuities can introduce strong spectral components.

These can produce unexpected filtering artifacts.

Padding and windowing can sometimes reduce such problems, depending on the task.

---

# 13.48 Why Zero Padding Alone Does Not “Fix Everything”

Zero padding can help with convolution geometry and circular wrap-around.

But:

```text
zero padding
≠
automatic removal of boundary discontinuities
```

It changes the transform size and spatial support.

A careful implementation considers:

- padding amount,
- boundary model,
- kernel alignment,
- crop region.

---

# 13.49 Windowing

> **EXTENSION**

A window function can taper the signal/image near the boundaries before spectral analysis.

This reduces abrupt discontinuities but also modifies the data.

Thus:

```text
less spectral leakage
↔
possible amplitude/resolution tradeoff
```

Windowing is more common in spectral analysis than in every standard image-filtering workflow.

---

# 13.50 Ringing vs Blurring

This is a major filter-design tradeoff.

### Very sharp frequency response

```text
good frequency selectivity
+
more spatial ringing
```

### Very smooth response

```text
less ringing
+
less sharp frequency selectivity
+
more gradual attenuation
```

There is no free lunch.

---

# 13.51 Practical Image Example — Removing Periodic Stripe Noise

Suppose:

```text
input image
+ periodic vertical stripes
```

Pipeline:

```text
1. compute FFT
2. center spectrum
3. inspect magnitude
4. find symmetric stripe-frequency peaks
5. construct notch-reject masks
6. multiply spectrum by mask
7. inverse FFT
8. compare image and spectrum
```

If the notch is too broad:

```text
noise removed
+
useful texture removed
```

If too narrow:

```text
residual periodic noise
```

---

# 13.52 Practical Image Example — Frequency Sharpening

Pipeline:

```text
image
 ↓
FFT
 ↓
Gaussian/BW low-pass
 ↓
construct HP = 1 − LP
 ↓
Hsharp = 1 + k·HP
 ↓
multiply spectrum
 ↓
inverse FFT
 ↓
clip/visualize carefully
```

Then inspect:

```text
edges
texture
noise
halos
```

---

# 13.53 Frequency Filter Parameter Log

A reproducible experiment should record:

```text
transform size
centering method
padding
filter family
cutoff
order
notch locations
notch width
gain
output scaling
```

Without this information, two “same filter” experiments may produce different outputs.

---

# 13.54 Implementation Safety

Keep the spectrum complex:

\[
F(u,v)\in\mathbb{C}
\]

Do not discard phase by using only:

\[
|F|
\]

for filtering.

The correct operation is:

\[
G=HF
\]

using the complex spectrum.

Magnitude is primarily for inspection.

---

# 13.55 A Common Implementation Bug

Incorrect:

```text
FFT
→ take abs()
→ multiply filter
→ inverse FFT
```

This throws away phase.

Correct conceptual path:

```text
FFT
→ keep complex F
→ inspect |F| separately
→ multiply complex F by H
→ inverse FFT
```

This distinction is extremely important.

---

# 13.56 Another Common Bug — Filtering the Log Magnitude

The visualization:

\[
\log(1+|F|)
\]

is not the spectrum used directly for inverse reconstruction.

Do not confuse:

```text
display spectrum
```

with:

```text
complex transform data
```

---

# 13.57 Output Range Handling

Inverse filtering can produce:

- small numerical imaginary residuals,
- negative values,
- values greater than the source range.

A careful pipeline:

```text
inverse FFT
 ↓
take real part when justified
 ↓
inspect min/max
 ↓
choose normalization/clipping policy
 ↓
convert for display/storage
```

Do not silently destroy quantitative output through an inappropriate cast.

---

# 13.58 Frequency-Domain Debugging Checklist

```text
[ ] Is the FFT centered only for display/filter construction?
[ ] Is the actual complex spectrum retained?
[ ] Is H aligned with the spectrum?
[ ] Is padding adequate?
[ ] Is the filter symmetric when expected?
[ ] Is the inverse transform normalized correctly?
[ ] Is the result real within numerical tolerance?
[ ] Were min/max inspected before uint8 conversion?
[ ] Was the intended crop applied?
```

---

# 13.59 Common Traps

## Trap 1 — “Low-pass keeps low pixel values.”

False.

Low-pass concerns low **spatial frequencies**, not low intensity values.

## Trap 2 — “High-pass means make the image brighter.”

False.

It emphasizes high-frequency variation.

## Trap 3 — “FFT magnitude is enough for filtering.”

False.

Phase is part of the transform.

## Trap 4 — “Ideal filters are best because the cutoff is sharp.”

Not necessarily.

Sharp cutoffs can create ringing.

## Trap 5 — “Band-pass means keep only a certain intensity range.”

False.

It keeps a certain spatial-frequency range.

## Trap 6 — “Zero padding removes all frequency artifacts.”

False.

It mainly addresses transform size/convolution geometry and changes boundary representation.

## Trap 7 — “Notch filtering removes all periodic noise automatically.”

False.

The frequency locations and bandwidth must be identified correctly.

## Trap 8 — “Same cutoff means same filter.”

False.

Filter family and parameters also determine the response.

---

# 13.60 Exam Formula Sheet

### Frequency-domain filtering

\[
\boxed{G(u,v)=H(u,v)F(u,v)}
\]

### Radial frequency distance

\[
\boxed{
D(u,v)=
\sqrt{(u-u_0)^2+(v-v_0)^2}
}
\]

### Ideal LPF

\[
\boxed{
H=
\begin{cases}
1,&D\le D_0\\
0,&D>D_0
\end{cases}
}
\]

### Butterworth LPF

\[
\boxed{
H=
\frac1{1+(D/D_0)^{2n}}
}
\]

### Gaussian LPF

\[
\boxed{
H=e^{-D^2/(2D_0^2)}
}
\]

### Ideal HPF

\[
\boxed{
H=
\begin{cases}
0,&D\le D_0\\
1,&D>D_0
\end{cases}
}
\]

### Gaussian HPF

\[
\boxed{
H_{HP}=1-e^{-D^2/(2D_0^2)}
}
\]

### Ideal band-pass

\[
\boxed{
H=
\begin{cases}
1,&D_1\le D\le D_2\\
0,&\text{otherwise}
\end{cases}
}
\]

### High-frequency emphasis

\[
\boxed{
H_{HFE}=1+kH_{HP}
}
\]

for one common conceptual form.

---

# 13.61 Exam-Style Problem — Ideal LPF

A frequency point has:

\[
D=12
\]

and:

\[
D_0=10
\]

For an ideal low-pass:

\[
D>D_0
\]

therefore:

\[
\boxed{H=0}
\]

The frequency is rejected.

---

# 13.62 Exam-Style Problem — Butterworth LPF

Given:

\[
D_0=20,\quad n=2,\quad D=10
\]

\[
H=
\frac1{1+(10/20)^4}
\]

\[
=
\frac1{1+1/16}
\]

\[
=
\frac{16}{17}
\]

\[
\boxed{H\approx0.9412}
\]

So roughly 94.1% of the amplitude is retained at that frequency under this transfer-function interpretation.

---

# 13.63 Exam-Style Problem — Gaussian LPF

Given:

\[
D_0=10,\quad D=10
\]

\[
H=e^{-100/200}
=e^{-0.5}
\]

\[
\boxed{H\approx0.6065}
\]

At \(D=D_0\), the Gaussian response is about 0.6065 for this parameterization.

---

# 13.64 Exam-Style Problem — High-Pass Complement

Suppose:

\[
H_{LP}=0.8
\]

Using:

\[
H_{HP}=1-H_{LP}
\]

we get:

\[
H_{HP}=1-0.8
\]

\[
\boxed{0.2}
\]

So the high-pass counterpart attenuates this low-frequency location strongly.

---

# 13.65 Engineering Insight — Filter Design Is a Task Problem

Do not begin with:

> “Which filter is famous?”

Begin with:

```text
What do I want to remove?
What do I want to preserve?
Where does that information live in frequency?
How sharp can the transition be?
What artifacts can I tolerate?
```

Then choose:

```text
family
+
cutoff
+
transition
+
gain
```

This is the engineering version of frequency-domain filtering.

---

# 13.66 Cross-Book Bridges

> **C08 BRIDGE**  
> Spatial convolution and frequency multiplication are related through the convolution theorem.

> **C09 BRIDGE**  
> Low-pass filtering provides a frequency-domain view of smoothing and noise reduction.

> **C10 BRIDGE**  
> High-pass filtering and frequency emphasis explain why sharpening enhances edges and can amplify noise.

> **C12 BRIDGE**  
> Fourier representation, magnitude/phase and FFT operations are prerequisites for every filter in this chapter.

> **C14 BRIDGE**  
> Restoration uses the frequency response of the degradation model rather than simply applying a generic filter.

> **C21–C24 BRIDGE**  
> Transform-domain thinking reappears in JPEG/DCT compression, with different mathematical objectives.

> **LAB BRIDGE**  
> Build ideal, Butterworth and Gaussian LPF/HPF experiments and a notch-filter experiment for periodic noise.

> **PRACTICE BRIDGE**  
> Calculate transfer-function values, classify frequencies, choose cutoff/order parameters and diagnose FFT filtering bugs.

> **EXAM BRIDGE**  
> Know ideal/Butterworth/Gaussian LPF and HPF equations, band-pass concepts, notch filtering, convolution theorem and filter-design tradeoffs.

---

# 13.67 Quick Recall

```text
F
→ input spectrum

H
→ frequency response

G = H·F
→ filtered spectrum

LOW-PASS
→ suppress high frequency

HIGH-PASS
→ suppress low frequency

BAND-PASS
→ keep middle band

NOTCH
→ reject selected frequency locations

IDEAL
→ sharp cutoff

BUTTERWORTH
→ tunable transition

GAUSSIAN
→ smooth transition
```

Core rule:

> **Filter the complex spectrum; use magnitude primarily to inspect it.**

---

# 13.68 Chapter Checkpoint

1. Define a frequency-domain filter.
2. Explain \(H(u,v)\).
3. Derive radial frequency distance \(D(u,v)\).
4. Write the ideal low-pass filter.
5. Explain ringing in ideal filtering.
6. Write the Butterworth low-pass equation.
7. Explain the role of filter order \(n\).
8. Write the Gaussian low-pass equation.
9. Compare ideal, Butterworth and Gaussian filters.
10. Explain high-pass filtering.
11. Derive a high-pass complement from a low-pass filter.
12. Define band-pass and band-reject filtering.
13. What is a notch filter?
14. Why is notch filtering suitable for periodic noise?
15. Explain high-frequency emphasis.
16. Why is phase required during inverse filtering?
17. Why is the displayed log-magnitude spectrum not the data used for inverse reconstruction?
18. Explain linear vs circular convolution in FFT-based filtering.
19. Why can sharp frequency cutoffs create ringing?
20. How should a filter cutoff be selected in an engineering application?

---

# 13.69 Unit II Final Chapter Preview

The frequency-domain core is now:

```text
C12
FOURIER REPRESENTATION
      ↓
C13
FREQUENCY-DOMAIN FILTER DESIGN
      ↓
C14
IMAGE RESTORATION
```

The difference is fundamental:

```text
ENHANCEMENT
→ choose a transformation that makes the image more useful

RESTORATION
→ model the degradation and estimate the underlying image
```

Chapter 14 therefore moves from:

```text
generic filtering
```

to:

```text
degradation model
+
inverse problem
+
reconstruction
```
