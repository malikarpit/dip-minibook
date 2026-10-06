---
id: "C03"
title: "Sampling and Quantization"
layer: "MAIN"
part: "I — The Image"
unit: "I"
version: "1.0"
status: "REFERENCE BUILD"
syllabus_scope:
  - "Sampling"
  - "Quantization"
  - "Bit depth / intensity levels"
tags:
  - "CORE"
  - "EXAM"
  - "MATH"
  - "DEEP DIVE"
  - "LAB"
  - "EXTENSION"
prerequisites:
  - "C01"
  - "C02"
related:
  - "C04"
  - "C11"
  - "C12"
  - "C14"
math:
  - "M02"
  - "M03"
  - "M05"
  - "M08"
lab:
  - "LAB-U1-01"
  - "LAB-U1-03"
exam:
  - "EXAM-U1"
practice:
  - "P-C03"
assets:
  - "D-C03-01"
  - "D-C03-02"
  - "D-C03-03"
---

# Chapter 03 — Sampling and Quantization

> **Chapter thesis**  
> A physical image is effectively continuous in space and signal values, but a digital computer needs a finite set of spatial samples and a finite set of numerical intensity values. **Sampling discretizes where we measure; quantization discretizes what value we store.**

**Part I — The Image**  
**Syllabus anchor:** Unit I explicitly includes sampling and quantization. fileciteturn4file0L32-L35

---

# 03.0 Why This Chapter Matters

The previous chapters established:

```text
real scene
→ image formation
→ measurable image signal
```

But the computer does not work with a perfectly continuous image.

It needs something like:

```text
a finite grid
+
finite numerical values
```

That creates two fundamental operations:

```text
SAMPLING
→ discretize spatial position

QUANTIZATION
→ discretize intensity/amplitude
```

These two ideas explain why a digital image has a fixed width, height, number of pixels, and finite intensity precision.

They also explain several practical problems:

- aliasing,
- loss of fine detail,
- staircase-like patterns,
- banding,
- quantization error,
- limited dynamic precision.

---

# 03.1 Continuous vs Digital Representation

A simplified continuous image can be written as:

\[
f(x,y)
\]

where \(x\) and \(y\) are continuous spatial coordinates.

A digital image can be represented using discrete indices:

\[
f[m,n]
\]

The conceptual transition is:

```text
continuous spatial coordinates
          ↓
        SAMPLING
          ↓
discrete spatial coordinates

continuous intensity
          ↓
      QUANTIZATION
          ↓
finite intensity values
```

These operations are related but not interchangeable.

---

# 03.2 Sampling: What Is It?

## CORE — Definition

**Sampling is the process of measuring a continuous image at discrete spatial locations.**

Imagine a continuous image surface:

```text
────────────────────────────
 continuous image content
────────────────────────────
```

Now place a grid over it:

```text
•   •   •   •   •
•   •   •   •   •
•   •   •   •   •
•   •   •   •   •
```

The dots indicate spatial sampling locations.

After sampling, we no longer have an intensity value at every possible real-valued coordinate. We have values at selected coordinates.

---

# 03.3 Sampling as a Coordinate Operation

Suppose the sampling spacing is:

\[
\Delta x,\quad \Delta y
\]

Then one possible discrete representation is:

\[
x=m\Delta x,\qquad y=n\Delta y
\]

and therefore:

\[
f[m,n]=f(m\Delta x,n\Delta y)
\]

where \(m,n\) are integer indices.

This is one of the most useful mathematical bridges in DIP.

It says:

> the digital image samples the continuous image on a discrete spatial lattice.

---

# 03.4 What Does “Higher Sampling” Actually Mean?

If we reduce the spacing:

\[
\Delta x,\Delta y \downarrow
\]

then the sampling grid becomes denser.

Equivalently:

\[
f_{s,x}=\frac{1}{\Delta x},
\qquad
f_{s,y}=\frac{1}{\Delta y}
\]

where the sampling frequencies describe how many samples are acquired per unit distance.

So:

```text
larger spacing
→ fewer samples
→ lower spatial sampling density

smaller spacing
→ more samples
→ higher spatial sampling density
```

### Important distinction

More samples do not automatically guarantee more useful detail.

The captured detail is also limited by:

- optics,
- sensor response,
- blur,
- scene content,
- noise,
- focus.

---

# 03.5 Sampling and Image Resolution

If an image contains:

\[
M\times N
\]

samples, then \(M\) and \(N\) describe its digital spatial dimensions.

For example:

```text
640 × 480
```

means:

```text
640 samples along one image dimension
480 samples along the other
```

This describes the digital sampling grid.

It does **not**, by itself, tell us every detail about the physical resolving power of the imaging system.

That distinction becomes important when discussing resolution in Chapter 04.

---

# 03.6 Worked Example — Spatial Sampling

Suppose a continuous image region is 10 mm wide.

### Case A

We sample every:

\[
\Delta x=1\text{ mm}
\]

Then the sampling density is:

\[
f_s=\frac{1}{1}=1
\]

sample/mm.

### Case B

We sample every:

\[
\Delta x=0.25\text{ mm}
\]

Then:

\[
f_s=\frac{1}{0.25}=4
\]

samples/mm.

So the second grid samples the spatial signal four times more densely.

### Interpretation

```text
1 sample/mm
→ coarse spatial representation

4 samples/mm
→ denser spatial representation
```

This does not guarantee perfect recovery of every scene detail; that depends on the highest spatial frequencies present in the signal and the acquisition system.

---

# 03.7 What Is Spatial Frequency?

Before discussing aliasing, we need one idea.

**Spatial frequency** describes how rapidly image intensity changes as we move through space.

### Low spatial frequency

Slow variation:

```text
dark → dark gray → gray → light gray
```

### High spatial frequency

Rapid variation:

```text
dark → light → dark → light → dark
```

A simple pattern illustrates this:

```text
LOW FREQUENCY

██████████
██████████
░░░░░░░░░░
░░░░░░░░░░


HIGH FREQUENCY

██░░██░░██
░░██░░██░░
██░░██░░██
```

Fine texture and abrupt transitions generally contain stronger high-frequency content than broad smooth regions.

---

# 03.8 The Sampling Problem

Suppose an image contains spatial detail that changes faster than the sampling grid can capture.

Then:

```text
continuous detail
        ↓
insufficient sampling
        ↓
incorrect digital appearance
```

This phenomenon is called:

> **aliasing**

Aliasing means that different high-frequency patterns can produce the same or misleading sampled representation.

---

# 03.9 Nyquist–Shannon Sampling Idea

## CORE / DEEP DIVE

For a band-limited signal with maximum frequency \(f_{\max}\), ideal reconstruction requires the sampling frequency to satisfy:

\[
f_s>2f_{\max}
\]

The boundary:

\[
2f_{\max}
\]

is commonly called the Nyquist rate.

This is a theoretical condition for a suitably band-limited signal and ideal sampling/reconstruction assumptions.

It is not a guarantee that an arbitrary camera image will be perfectly reconstructed just because a specification says “twice the frequency.”

---

# 03.10 Worked Example — Nyquist Requirement

Suppose the highest relevant spatial frequency is:

\[
f_{\max}=6\text{ cycles/mm}
\]

Then the theoretical Nyquist rate is:

\[
2f_{\max}
=
12\text{ samples/mm}
\]

Therefore an ideal sampling system would require:

\[
f_s>12\text{ samples/mm}
\]

under the stated assumptions.

If:

\[
f_s=20\text{ samples/mm}
\]

then the sampling density is above the theoretical requirement.

If:

\[
f_s=8\text{ samples/mm}
\]

then it is below the Nyquist rate and aliasing can occur.

---

# 03.11 Aliasing: What It Looks Like

A classic conceptual example is a fine stripe pattern.

```text
ORIGINAL HIGH-FREQUENCY PATTERN

||||||||||||||||||||||||||||||

        ↓ sample too coarsely

DIGITAL OBSERVATION

||  |   ||    |  ||    |
```

The sampled image may appear to contain a different, slower pattern.

This is why fine repetitive structures can produce:

- false patterns,
- apparent motion,
- moiré-like effects,
- incorrect orientations,
- misleading textures.

---

# 03.12 Why Cameras Can Produce Moiré

> **EXTENSION**

When a scene contains repetitive detail close to the sensor's sampling limit, such as:

- fine fabric,
- roof tiles,
- screen pixels,
- dense line patterns,

the sampled image may contain interference-like false patterns.

The cause is not necessarily a problem in the scene.

It can result from the interaction between:

```text
scene spatial frequency
+
optical response
+
sensor sampling pattern
```

This is a practical manifestation of aliasing.

---

# 03.13 Anti-Aliasing

If a high-frequency component cannot be represented safely by the target sampling rate, one strategy is to reduce that component **before downsampling**.

Conceptually:

```text
high-resolution image
        ↓
low-pass / anti-alias filtering
        ↓
downsampling
        ↓
lower-resolution image
```

This is an important engineering pattern.

### Why filter first?

Because simply throwing samples away does not remove frequency components that can alias into the lower-frequency range.

---

# 03.14 Sampling Is Not the Same as Resizing

A software command that changes an image from:

```text
1000 × 1000
```

to:

```text
250 × 250
```

is not conceptually just:

> “Make it smaller.”

It involves a resampling process.

A responsible resampling pipeline may involve:

```text
original image
→ anti-alias filtering
→ choose new sample locations
→ interpolation/resampling
→ output image
```

The exact pipeline depends on the operation and library.

---

# 03.15 Quantization: What Is It?

Sampling determines **where** we measure.

Quantization determines **which numerical level** represents the measured value.

## CORE — Definition

**Quantization maps a continuous-valued measurement to one value from a finite set of allowed intensity or amplitude levels.**

Conceptually:

```text
continuous intensity

0 ──────── 0.18 ───────── 0.37 ───────── 0.91 ─── 1
                       ↓
                  quantization
                       ↓
finite levels
0   0.25   0.50   0.75   1.00
```

The exact mapping depends on the quantizer design and convention.

---

# 03.16 Number of Quantization Levels

If a sample is represented with \(k\) bits, then the number of distinct binary codes is:

\[
L=2^k
\]

Examples:

| Bit depth | Levels |
|---:|---:|
| 1 bit | 2 |
| 2 bits | 4 |
| 3 bits | 8 |
| 4 bits | 16 |
| 8 bits | 256 |
| 10 bits | 1024 |
| 12 bits | 4096 |
| 16 bits | 65536 |

This is a representation-level statement.

The physical sensor may have different effective characteristics, and a file may use different storage conventions.

---

# 03.17 Worked Example — Bit Depth

Suppose a grayscale sample is stored with:

\[
k=3
\]

bits.

Then:

\[
L=2^3=8
\]

possible coded levels are available.

Conceptually, the image can distinguish eight discrete intensity codes rather than the 256 codes available in an 8-bit representation.

This can produce visibly stronger quantization steps in smooth gradients.

---

# 03.18 Quantization Error

If the original continuous-valued measurement is \(r\) and the quantized value is \(q(r)\), then the quantization error can be written:

\[
e_q=r-q(r)
\]

For a uniform quantizer using nearest-level rounding with step size \(\Delta\), the maximum absolute error is commonly bounded by approximately:

\[
|e_q|\leq\frac{\Delta}{2}
\]

under the stated quantizer convention.

### Worked example

Suppose:

\[
\Delta=0.1
\]

and a measurement is rounded to the nearest available level.

Then the maximum idealized absolute error is:

\[
\frac{0.1}{2}=0.05
\]

So:

\[
|e_q|\leq0.05
\]

again under the stated rounding model.

---

# 03.19 Quantization Noise Intuition

Quantization error behaves like a small numerical perturbation of the original value.

Conceptually:

```text
true signal
     │
     ├── exact value
     │
     ↓
quantizer
     │
     ↓
stored level
     │
     ↕
 quantization error
```

Under common assumptions for a uniform quantizer and sufficiently non-pathological input, quantization error can be modelled statistically.

A frequently used approximation is:

\[
\sigma_q^2\approx\frac{\Delta^2}{12}
\]

where \(\sigma_q^2\) is the quantization-noise variance.

> **DEEP DIVE:** This is an approximate model, not a universal identity for every image or quantizer.

---

# 03.20 Quantization and Bit Depth

Increasing bit depth generally reduces the spacing between representable intensity levels for a fixed input range.

Conceptually:

```text
2-bit

|    |    |    |

        vs

8-bit

|||||||||||||||||||||||||||||||||||||||||||||
```

The 8-bit representation provides many more possible values.

However:

> higher bit depth does not automatically mean a better image if the acquisition system, noise, optics, display and task do not benefit from that additional precision.

---

# 03.21 Sampling vs Quantization — The Critical Difference

| Property | Sampling | Quantization |
|---|---|---|
| Discretizes | spatial position | intensity/amplitude |
| Main question | Where do we measure? | Which numeric level do we store? |
| Controls | number/density of spatial samples | number of intensity levels |
| Too little | spatial detail loss / aliasing | intensity precision loss / banding |
| Related term | spatial resolution | radiometric resolution / intensity precision |
| Mathematical idea | discrete coordinates | finite output levels |

### Memory sentence

> **Sampling discretizes space. Quantization discretizes value.**

---

# 03.22 A Full Digitisation Pipeline

The concepts now fit together:

```text
CONTINUOUS IMAGE
      │
      ├────────────── spatial information
      │
      ▼
   SAMPLING
      │
      ▼
DISCRETE SPATIAL GRID
      │
      ├────────────── intensity information
      │
      ▼
 QUANTIZATION
      │
      ▼
FINITE NUMERICAL IMAGE
```

The digital image is therefore discrete in **both** spatial coordinates and represented intensity values.

---

# 03.23 Worked Matrix Example — Sampling

Consider this toy grayscale matrix:

\[
I=
\begin{bmatrix}
10&20&30&40&50&60\\
15&25&35&45&55&65\\
20&30&40&50&60&70\\
25&35&45&55&65&75\\
30&40&50&60&70&80\\
35&45&55&65&75&85
\end{bmatrix}
\]

Suppose we keep every second row and every second column.

Selecting rows:

\[
1,3,5
\]

and columns:

\[
1,3,5
\]

produces:

\[
I_s=
\begin{bmatrix}
10&30&50\\
20&40&60\\
30&50&70
\end{bmatrix}
\]

### What happened?

The representation changed from:

\[
6\times6
\]

to:

\[
3\times3
\]

The spatial sample density has been reduced.

### Important warning

This example performs simple decimation for illustration.

A production-quality reduction should consider anti-alias filtering when the source contains frequencies that could alias at the new sampling rate.

---

# 03.24 Worked Quantization Example

Suppose normalized intensity values are:

\[
[0.10,\ 0.26,\ 0.51,\ 0.74,\ 0.95]
\]

and, for a simple illustrative quantizer, we use four equally spaced reconstruction values:

\[
\{0,\ 0.33,\ 0.67,\ 1\}
\]

Mapping to the nearest level gives approximately:

```text
0.10 → 0
0.26 → 0.33
0.51 → 0.67
0.74 → 0.67
0.95 → 1
```

Therefore the quantized sequence becomes:

\[
[0,\ 0.33,\ 0.67,\ 0.67,\ 1]
\]

### Why did 0.51 become 0.67?

Because:

\[
|0.51-0.67|=0.16
\]

while:

\[
|0.51-0.33|=0.18
\]

so 0.67 is the closer reconstruction level under this particular convention.

> **Convention note:** Real quantizers may use different level definitions and interval boundaries. The MiniBook will always specify the convention when a numerical result depends on it.

---

# 03.25 Bit Depth vs Number of Pixels

These are independent dimensions of representation.

Consider:

```text
Image A
512 × 512
8-bit grayscale
```

and:

```text
Image B
512 × 512
12-bit grayscale
```

They contain the same number of spatial samples:

\[
512\times512
\]

but Image B can represent more intensity levels per sample.

Conversely:

```text
Image C
1024 × 1024
8-bit grayscale
```

has four times as many spatial samples as the 512×512 image but the same 8-bit intensity-code count per sample.

This gives us two independent ideas:

```text
SPATIAL DETAIL
→ how densely space is sampled

INTENSITY PRECISION
→ how finely values are quantized
```

---

# 03.26 A Useful Four-Quadrant Mental Model

Think about two axes:

```text
                HIGH INTENSITY PRECISION
                         ↑
                         │
        many levels      │     many levels
        but coarse       │     + dense spatial
        spatial sampling │     sampling
                         │
 LOW SPATIAL ────────────┼──────────── HIGH SPATIAL
                         │
        few levels       │     dense spatial
        + coarse         │     but limited
        spatial sampling │     intensity precision
                         │
                         ↓
                LOW INTENSITY PRECISION
```

The ideal setting depends on the application.

---

# 03.27 Common Quantization Artifact — Banding

Suppose a smooth gradient should look like:

```text
black → dark gray → gray → light gray → white
```

With very few quantization levels it may become:

```text
████
░░░░
▒▒▒▒
▓▓▓▓
```

with visible steps instead of a smooth transition.

This is called **banding** or contouring-like quantization artifact in suitable contexts.

It becomes more obvious when:

- the gradient is smooth,
- few intensity levels are available,
- processing amplifies the differences,
- display conditions make the steps visible.

---

# 03.28 Common Sampling Artifact — Stair-Stepping

Edges that are smooth in continuous space can appear jagged in a low-resolution digital representation.

Conceptually:

```text
ideal edge

       /
      /
     /

sampled representation

       ██
      █
      ██
    ██
```

The visual artifact is related to finite spatial sampling and display/resampling.

---

# 03.29 Why Resampling and Interpolation Appear Later

When an image must be displayed or transformed at different dimensions, we need new pixel locations.

For example:

```text
100 × 100
     ↓ scaling
250 × 250
```

The target grid may require values that were not directly present in the source grid.

That motivates:

- nearest-neighbour interpolation,
- bilinear interpolation,
- other resampling methods.

These are the focus of Chapter 11.

---

# 03.30 Image Acquisition and Anti-Aliasing

The practical acquisition chain can therefore be viewed as:

```text
scene
  ↓
optics
  ↓
analog image signal
  ↓
anti-alias / optical response
  ↓
sampling
  ↓
quantization
  ↓
digital image
```

The exact physical implementation depends on the imaging system.

The important principle is that **good digitisation manages information before it becomes irreversible digital representation error**.

---

# 03.31 Engineering Decision Example

Suppose you need to reduce a 4000×3000 image to 1000×750.

A weak approach is:

```text
throw away 75% of rows/columns
```

A more principled conceptual approach is:

```text
high-resolution image
→ suppress frequencies that cannot survive
→ resample onto the lower-resolution grid
→ inspect result
```

This reduces the risk of aliasing.

If the image contains high-frequency text or fine texture, the choice of resampling filter matters greatly.

---

# 03.32 Common Traps

## Trap 1 — “Sampling and quantization are the same.”

False.

Sampling is primarily about **where** values are measured.

Quantization is primarily about **which numerical levels** represent those values.

## Trap 2 — “More pixels means more intensity precision.”

False.

Pixel count concerns spatial sampling. Bit depth concerns the number of representable levels per sample.

## Trap 3 — “8-bit means 8 pixels.”

False.

8-bit describes the number of bits used to encode a sample under the stated representation.

## Trap 4 — “Nyquist means sample at exactly twice the highest frequency.”

Too simplistic.

Ideal band-limited reconstruction requires a rate greater than the relevant highest frequency twice, under appropriate assumptions, and real imaging systems have additional limitations.

## Trap 5 — “Downsampling is just deleting pixels.”

Incomplete.

Good resampling often includes filtering and interpolation/weighted estimation.

## Trap 6 — “Higher bit depth always guarantees better visual quality.”

False.

The extra precision is useful only when the acquisition, processing, display and task can benefit from it.

---

# 03.33 Engineering Insight — Information Can Be Lost Twice

Digitisation can discard information in two fundamentally different ways:

```text
SAMPLING
→ loses / aliases spatial information

QUANTIZATION
→ reduces intensity precision
```

Later, additional operations may discard information again:

```text
blurring
thresholding
lossy compression
downsampling
clipping
```

This is why the sequence of operations matters.

---

# 03.34 Cross-Book Bridges

> **MATH BRIDGE — M02 / M03 / M05**  
> Review discrete coordinates, summation and matrix representation.

> **LAB BRIDGE — LAB-U1-01 / LAB-U1-03**  
> Inspect image dimensions and compare resampled/quantized representations.

> **PRACTICE BRIDGE**  
> Identify whether a described problem is primarily spatial-sampling or intensity-quantization related.

> **EXAM BRIDGE**  
> Be ready to define sampling and quantization, derive \(L=2^k\), explain aliasing, state the Nyquist condition, and compare sampling with quantization.

> **RESOURCE BRIDGE**  
> Classical DIP references provide deeper treatments of sampling, quantization and image digitisation.

---

# 03.35 Quick Recall

```text
SAMPLING
→ where / how often

QUANTIZATION
→ which level / how precisely

Sampling frequency
\[
f_s=\frac{1}{\Delta}
\]

Number of levels
\[
L=2^k
\]

Ideal band-limited sampling condition
\[
f_s>2f_{\max}
\]

Approximate uniform-quantizer variance
\[
\sigma_q^2\approx\frac{\Delta^2}{12}
\]
```

---

# 03.36 Chapter Checkpoint

1. What is sampling?
2. What is quantization?
3. Why are they conceptually different?
4. What does a smaller sampling interval mean?
5. What is spatial frequency?
6. What is aliasing?
7. State the Nyquist condition under ideal band-limited assumptions.
8. Why is anti-alias filtering useful before downsampling?
9. How many levels does a \(k\)-bit representation provide?
10. What is quantization error?
11. What happens when bit depth is reduced?
12. How can a digital image lose information during digitisation?

---

# 03.37 Connection Forward

Sampling and quantization tell us how the continuous image becomes discrete.

We now know:

```text
how many spatial samples
+
how many intensity levels
```

But a digital image still needs a richer description:

> What exactly is a pixel?  
> How are rows and columns organized?  
> How are colour channels represented?  
> What do “resolution,” “bit depth,” “dynamic range,” and “datatype” actually mean?

Those questions are the focus of Chapter 04.
