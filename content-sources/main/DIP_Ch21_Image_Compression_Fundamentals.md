---
id: "C21"
title: "Image Compression Fundamentals"
layer: "MAIN"
part: "IV — Compressing Images"
unit: "Unit III"
version: "1.0"
status: "PRODUCTION"
syllabus_scope: "Image Compression; Lossless vs. Lossy Compression"
tags:
  - digital-image-processing
  - image-compression
  - redundancy
  - lossless
  - lossy
  - compression-ratio
prerequisites:
  - "C04 — Image Representation: Pixels, Matrices, Tensors and Resolution"
  - "C05 — Colour Models and Image File Formats"
  - "C08 — Spatial Filtering and Convolution"
related_math:
  - "Entropy"
  - "Probability"
related_lab:
  - "LAB-07 — Image Compression"
related_code:
  - "CODE-07 — Compression Implementations"
related_exam:
  - "EXAM-Compression-Fundamentals"
related_practice:
  - "PRACTICE-Compression-Core"
---

# C21 — Image Compression Fundamentals

> **Chapter thesis:** Image compression reduces the number of bits needed to represent image information by exploiting redundancy or information that can be removed with an acceptable loss of quality.

---

## 1. Why This Chapter Exists

A digital image is fundamentally a numerical dataset.

A grayscale image with width \(W\), height \(H\), and \(k\) bits per pixel requires, before any storage format or coding overhead,

\[
N_{\text{raw}} = W H k
\]

bits.

For a colour image with three 8-bit channels,

\[
N_{\text{raw}} = W H \times 3 \times 8.
\]

That representation is simple, but often wasteful.

Neighbouring pixels can be similar. Repeated values can occur frequently. Some visual information may be less important to human perception than other information. Compression asks a precise engineering question:

> **What information can be represented with fewer bits, and what information—if any—can be removed?**

This chapter builds the vocabulary and reasoning needed before studying entropy coding, DCT, and JPEG.

---

# 2. Learning Contract

After this chapter, you should be able to:

- explain why image compression is necessary;
- calculate raw image storage requirements;
- distinguish coding, spatial, and perceptual redundancy;
- distinguish lossless and lossy compression;
- calculate compression ratio and related measures;
- explain the trade-off between compression, quality, storage, and transmission;
- identify when a compression method is reversible;
- explain why a compressed file size cannot be predicted from image dimensions alone;
- choose a suitable compression strategy for a stated engineering requirement.

You should also be able to connect:

```text
raw image
→ redundancy
→ representation/coding
→ compressed representation
→ storage / transmission
→ reconstruction
```

---

# 3. The Compression Problem

Consider an image matrix:

\[
f(x,y).
\]

A file stores some representation of that image. The goal of compression is to construct a shorter representation without violating the task's quality requirements.

A generic system is:

```text
Original image
      │
      ▼
Analysis / representation
      │
      ▼
Compression
      │
      ▼
Compressed bitstream
      │
      ├──────────► Storage
      │
      └──────────► Transmission
                         │
                         ▼
                    Decompression
                         │
                         ▼
                 Reconstructed image
```

For a lossless method:

```text
Original
  │
  ▼
Encoder
  │
  ▼
Compressed representation
  │
  ▼
Decoder
  │
  ▼
Exactly the same image data
```

For a lossy method:

```text
Original
  │
  ▼
Encoder
  │
  ▼
Compressed representation
  │
  ▼
Decoder
  │
  ▼
Approximate reconstruction
```

The difference between these two cases is one of the most important facts in the entire compression unit.

---

# 4. Why Images Contain So Much Redundancy

Compression works because many images contain predictable structure.

A completely random image is difficult to compress because little can be predicted or represented more compactly.

A natural photograph, however, commonly contains:

- neighbouring pixels with related values;
- repeated colours or textures;
- smooth intensity regions;
- edges where useful information is concentrated;
- colour channels with related information;
- patterns that occur more often than others.

The key idea is:

> **Compression does not primarily “make the image smaller.” It changes the representation so that fewer bits are required.**

---

# 5. Four Useful Redundancy Categories

This chapter uses four categories because they help explain the logic behind different compression families.

## 5.1 Coding Redundancy

Suppose a source contains symbols with very unequal probabilities.

Example:

```text
A A A A A A A B A A C A A A A
```

Using the same number of bits for every symbol may be inefficient.

If one value occurs much more often than another, a variable-length code can assign:

```text
frequent symbol   → shorter code
rare symbol       → longer code
```

This is the basic idea behind entropy coding and Huffman coding.

### Key intuition

> **Coding redundancy comes from representing symbols inefficiently relative to their probabilities.**

---

## 5.2 Spatial Redundancy

Neighbouring image samples are often correlated.

Example:

\[
100,\ 101,\ 100,\ 102,\ 103,\ 102,\ 104
\]

Storing every value independently ignores the predictability between neighbours.

A compressor can exploit this relationship through prediction, transforms, run-length coding, differential representation, or related techniques.

### Key intuition

> **Spatial redundancy comes from local similarity or correlation within an image.**

---

## 5.3 Interchannel / Spectral Redundancy

Colour images contain multiple channels.

For RGB:

\[
I(x,y)=
\begin{bmatrix}
R(x,y) & G(x,y) & B(x,y)
\end{bmatrix}.
\]

The channels are not necessarily independent. Natural scenes often contain related information across channels.

This means a colour image may contain redundant information if each channel is treated as completely unrelated.

This is one reason colour transforms and chroma subsampling can help in practical codecs such as JPEG.

---

## 5.4 Perceptual Redundancy

Human vision does not respond equally to every possible change in an image.

Some fine-grained information may be less visually important than:

- strong edges;
- large structures;
- luminance changes;
- important spatial features.

Lossy compression can exploit perceptual characteristics by retaining more important information while discarding or coarsening information that has lower perceptual impact.

### Important caution

Perceptual redundancy does **not** mean that lost information is “irrelevant” for every application.

A change that is visually small can be scientifically, legally, medically, or forensically important.

Therefore:

> **A compression decision must be tied to the application, not only to visual appearance.**

---

# 6. Raw Storage: The Baseline

Before comparing compression methods, calculate the uncompressed size.

## 6.1 Grayscale Image

For:

- width = \(W\)
- height = \(H\)
- bit depth = \(k\)

the raw size is:

\[
N_{\text{bits}} = W H k
\]

and

\[
N_{\text{bytes}} = \frac{W H k}{8}.
\]

### Worked Example 1

A grayscale image is:

\[
1024\times768
\]

with 8 bits per pixel.

Then:

\[
N_{\text{bits}}=1024\times768\times8.
\]

Since one pixel requires one byte:

\[
N_{\text{bytes}}=1024\times768=786{,}432
\]

bytes.

Using decimal units:

\[
\approx0.786\text{ MB}.
\]

Using binary units:

\[
\frac{786{,}432}{1024^2}\approx0.75\text{ MiB}.
\]

### Engineering note

Do not casually use “MB” and “MiB” as if they were identical. For exam calculations, follow the convention used by the question.

---

# 7. Colour Image Storage

For three channels each using \(k\) bits:

\[
N_{\text{bits}}=WH(3k).
\]

For a standard 8-bit-per-channel RGB image:

\[
N_{\text{bits}}=WH\times24.
\]

### Worked Example 2

For a \(1920\times1080\) RGB image with 8 bits per channel:

\[
N_{\text{bytes}}
=
1920\times1080\times3.
\]

\[
=6{,}220{,}800\text{ bytes}
\]

or approximately:

\[
6.22\text{ MB}.
\]

This is the raw pixel payload, not necessarily the exact size of a real BMP, PNG, TIFF, or JPEG file.

---

# 8. Compression Ratio

A common measure is the **compression ratio**:

\[
CR=
\frac{\text{original size}}{\text{compressed size}}.
\]

A larger \(CR\) means stronger size reduction.

### Example

Suppose:

- original = 8 MB
- compressed = 2 MB

Then:

\[
CR=\frac{8}{2}=4.
\]

So the compression ratio is:

\[
\boxed{4:1}
\]

The compressed representation uses one quarter of the original storage.

---

# 9. Percentage Size Reduction

Another useful quantity is:

\[
\text{Reduction \%}
=
\left(
1-\frac{S_c}{S_o}
\right)\times100
\]

where:

- \(S_o\) = original size
- \(S_c\) = compressed size.

For 8 MB → 2 MB:

\[
\left(1-\frac{2}{8}\right)100=75\%.
\]

So the size is reduced by:

\[
\boxed{75\%}.
\]

Do not confuse this with the compression ratio.

```text
Compression ratio: 4:1
Size reduction:    75%
```

They describe related but different quantities.

---

# 10. Bits Per Pixel

For an image containing \(N\) pixels and a compressed payload containing \(B\) bits:

\[
bpp=\frac{B}{N}.
\]

This measure is especially useful when comparing compression across images of different dimensions.

### Example

A compressed grayscale image contains:

\[
300\,000
\]

bits and has:

\[
100\,000
\]

pixels.

Then:

\[
bpp=\frac{300\,000}{100\,000}=3.
\]

The compressed representation uses:

\[
\boxed{3\text{ bits/pixel}}.
\]

The original might have used 8 bits/pixel.

---

# 11. Compression Ratio vs Bits Per Pixel

These measures can be connected.

For an 8-bit grayscale source:

\[
CR=\frac{8}{bpp}
\]

when comparing raw pixels to an idealized compressed payload without side information or format overhead.

For example, if:

\[
bpp=2
\]

then:

\[
CR=\frac{8}{2}=4:1.
\]

In real files, headers, metadata, tables, padding, and other overhead mean the measured ratio may differ from this idealized calculation.

---

# 12. Lossless Compression

A compression method is **lossless** when decompression reproduces the exact original image data.

Mathematically, if encoder \(E\) and decoder \(D\) are applied:

\[
D(E(I))=I.
\]

No pixel value is changed.

### Typical use cases

Lossless compression is particularly appropriate when exact values matter, such as:

- archival masters;
- scientific images;
- medical workflows where exact pixel values matter;
- images used for further numerical analysis;
- diagrams, text-heavy graphics, and some synthetic images.

### Strength and limitation

Strength:

> Exact recovery.

Limitation:

> Compression may be substantially weaker than lossy compression for many natural photographs.

---

# 13. Lossy Compression

A lossy method permits information to be discarded or approximated.

\[
D(E(I))\approx I.
\]

The reconstructed image is not necessarily identical to the original.

The goal is controlled information loss in exchange for significantly lower size.

### Typical use cases

Lossy compression is commonly appropriate when:

- storage/transmission efficiency is important;
- small visual differences are acceptable;
- the image is a photograph or natural scene;
- application requirements specify an acceptable quality threshold.

### Important distinction

Lossy does **not** automatically mean poor quality.

A lossy codec can produce a reconstruction that is visually very close to the original at moderate compression.

---

# 14. Lossless vs. Lossy — Core Comparison

| Property | Lossless | Lossy |
|---|---|---|
| Exact original recovery | Yes | No |
| Information discarded | No | Potentially yes |
| Typical compression strength | Lower | Higher |
| Repeated decoding | Reversible | Does not recover original by re-encoding/decoding |
| Best for exact numerical preservation | Yes | Often unsuitable |
| Visual quality can be excellent | Yes | Yes, depending on settings |
| Typical photographic use | Possible | Very common |
| Typical analytical/archive use | Strong candidate | Must be evaluated carefully |

The most important exam sentence is:

> **Lossless compression reduces representation redundancy while preserving all information; lossy compression sacrifices some information to achieve greater compression.**

---

# 15. Why Photographs and Text Graphics Behave Differently

Compression efficiency depends strongly on the source image.

### Photograph

A natural photograph may contain:

- many colours;
- gradual variations;
- texture;
- noise;
- broad spatial correlation.

A lossy transform-based codec may compress it effectively.

### Screenshot / text / line art

Sharp boundaries and small symbols can be sensitive to compression artifacts.

For some graphics, lossless compression may preserve the visual structure much better.

Therefore:

```text
Best compression method
≠
same method for every image
```

Instead:

```text
image characteristics
+
application requirement
+
quality tolerance
+
storage/transmission constraints
→
compression choice
```

---

# 16. Redundancy-to-Compression Map

| Redundancy | What it means | Methods that may exploit it |
|---|---|---|
| Coding | Unequal symbol probabilities | Huffman, arithmetic-style entropy coding |
| Spatial | Similar neighbouring samples | Prediction, RLE, transforms |
| Interchannel | Related colour channels | Colour transforms, chroma subsampling |
| Perceptual | Unequal visual importance | Quantization / perceptual coding |

This table is a mental bridge to Chapters 22–24.

---

# 17. Generic Compression Pipeline

A codec can often be understood as several conceptual stages:

```text
Input image
    ↓
Representation transform
    ↓
Redundancy reduction
    ↓
Quantization
    ↓
Entropy coding
    ↓
Compressed bitstream
```

Not every codec contains all stages in exactly this order.

For a **lossless** system, quantization in the lossy sense is absent because exact recovery is required.

For a **lossy transform codec** such as JPEG, the conceptual path is closer to:

```text
image
→ colour transform
→ block transform
→ quantization
→ coefficient ordering
→ entropy coding
→ file/bitstream
```

The detailed JPEG implementation appears in C24.

---

# 18. Where Does Compression Actually Happen?

This question is useful because “compression” is not a single operation.

Consider a transform codec.

### Stage A — Transform

The data is represented differently.

```text
spatial samples
→ transform coefficients
```

The number of samples may not yet have decreased.

### Stage B — Quantization

Some coefficient precision is reduced or removed.

This is a major lossy step.

### Stage C — Symbol representation

Remaining values are encoded efficiently.

This reduces coding redundancy.

Therefore:

> **A codec can combine representation change, information reduction, and efficient coding.**

---

# 19. Rate–Quality Trade-off

Lossy compression is an engineering optimization.

Let:

- \(R\) = rate, often bits per pixel or file size;
- \(Q\) = quality measure.

The exact relationship depends on the codec and source.

A general conceptual curve is:

```text
Quality
  ^
  |                         ______
  |                     ___/
  |                 ___/
  |             ___/
  |___________/______________________> bitrate
```

At low bitrates, visual quality can deteriorate substantially.

At higher bitrates, additional bits may provide progressively smaller visible improvements.

This is why a single statement such as “JPEG is 10:1 compressed” is incomplete without specifying the actual image and quality settings.

---

# 20. Rate–Distortion Thinking

Lossy compression can be viewed as minimizing distortion subject to a rate constraint:

\[
\min D
\quad
\text{subject to}
\quad
R\le R_{\max}
\]

or alternatively:

\[
\min (D+\lambda R)
\]

for a suitable trade-off parameter \(\lambda\).

Here:

- \(D\) = distortion;
- \(R\) = bitrate;
- \(\lambda\) = relative cost assigned to rate.

You do not need a full rate–distortion-theory treatment for the syllabus, but this formulation captures the engineering problem:

> **How much quality should be sacrificed to save how many bits?**

---

# 21. Measuring Reconstruction Quality

Compression quality should not be judged only by file size.

## Mean Squared Error

For original \(I\) and reconstructed image \(\hat I\):

\[
MSE=
\frac{1}{MN}
\sum_{x=1}^{M}
\sum_{y=1}^{N}
\left[I(x,y)-\hat I(x,y)\right]^2.
\]

Lower MSE means smaller average squared error.

## Peak Signal-to-Noise Ratio

For peak value \(MAX_I\):

\[
PSNR=
10\log_{10}
\left(
\frac{MAX_I^2}{MSE}
\right).
\]

For an 8-bit image:

\[
MAX_I=255.
\]

Higher PSNR generally means lower MSE.

### Important caveat

PSNR is not a perfect perceptual-quality metric. Two images with similar PSNR can look different to a human observer.

Therefore:

```text
file size
+
numerical distortion
+
visual inspection
+
task-specific requirements
```

should be considered together.

---

# 22. Worked Numerical Example — Compression Metrics

An original image occupies:

\[
12\text{ MB}
\]

and the compressed representation occupies:

\[
3\text{ MB}.
\]

### Compression ratio

\[
CR=\frac{12}{3}=4.
\]

So:

\[
\boxed{4:1}
\]

### Percentage reduction

\[
\text{Reduction}
=
\left(1-\frac34\right)100
=75\%.
\]

### Space saved

\[
12-3=9\text{ MB}.
\]

So the method saves:

\[
\boxed{9\text{ MB}}
\]

for this file.

---

# 23. Why File Size Is Not Determined by Resolution Alone

Suppose two images are both:

\[
1920\times1080.
\]

Their compressed sizes can differ greatly because of:

- image content;
- colour distribution;
- texture;
- noise;
- repeated patterns;
- codec settings;
- metadata;
- quantization;
- entropy of the source.

Therefore:

\[
\boxed{\text{same dimensions} \not\Rightarrow \text{same compressed size}}
\]

This is a common conceptual trap.

---

# 24. Lossless Compression and Information Entropy

Before studying C22, one idea is essential:

> A source with more predictable symbols can often be encoded using fewer average bits per symbol.

For a discrete random variable \(X\), entropy is:

\[
H(X)=
-\sum_i p_i\log_2 p_i.
\]

Entropy represents a lower-bound notion of average information content under ideal coding assumptions.

We develop this properly in C22.

---

# 25. A Tiny Intuition Example

Suppose four symbols occur with equal probability:

\[
P(A)=P(B)=P(C)=P(D)=0.25.
\]

All four symbols are equally likely.

A fixed-length binary representation needs:

\[
\log_2 4=2
\]

bits per symbol.

Now suppose:

\[
P(A)=0.875,\qquad
P(B)=P(C)=P(D)=0.041667.
\]

The source is much more predictable.

A good variable-length code can give the common symbol a short representation and rarer symbols longer representations.

The exact coding construction belongs to C22, but the compression principle is already visible:

```text
predictability
→ lower average code length
→ fewer bits
```

---

# 26. Compression Does Not Always Help Equally

Some inputs are already highly compact or statistically difficult to compress.

Examples include:

- encrypted image data;
- pseudo-random data;
- heavily noisy data;
- data that has already been compressed effectively.

Trying another lossless compression stage may provide little or no benefit.

In some cases, the compressed output can even become slightly larger because of headers and metadata.

So:

> **Compression is data-dependent.**

---

# 27. Lossy Compression Is Not Appropriate Everywhere

Consider a medical image where a tiny intensity difference has diagnostic significance.

A visually imperceptible modification could still alter the numerical evidence needed for analysis.

Likewise, in scientific measurements:

```text
visual similarity
≠
scientific equivalence
```

For these systems, the compression policy must be determined by domain requirements.

---

# 28. Engineering Decision Example

### Scenario A — Web photograph

Requirements:

- low bandwidth;
- reasonable visual quality;
- fast loading.

A lossy codec may be attractive.

### Scenario B — Line-art diagram for repeated editing

Requirements:

- preserve sharp boundaries;
- preserve exact colours;
- repeated editing.

Lossless compression may be preferable.

### Scenario C — Quantitative scientific image

Requirements:

- preserve numerical data.

Lossless compression should be strongly considered unless the application explicitly validates a lossy method.

### Decision rule

```text
What is the image used for?
        ↓
Can information be discarded?
        ↓
How much storage/bandwidth is saved?
        ↓
What distortion is acceptable?
        ↓
Select codec + operating point
```

---

# 29. Common Traps

### Trap 1 — “Lossless means no compression.”

False.

Lossless compression can significantly reduce file size while still allowing exact reconstruction.

### Trap 2 — “Lossy always looks bad.”

False.

Lossy compression can provide excellent visual quality at appropriate settings.

### Trap 3 — Compression ratio and percentage reduction are the same.

False.

For \(4:1\):

\[
\text{Reduction}=75\%.
\]

### Trap 4 — Every image can be compressed to an arbitrarily tiny lossless file.

False.

Information content limits how much lossless compression is possible.

### Trap 5 — A smaller file automatically means a better compression method.

False.

The correct method depends on:

- distortion;
- task;
- speed;
- memory;
- compatibility;
- decoding requirements.

---

# 30. Compression Vocabulary

| Term | Meaning |
|---|---|
| Compression | Reducing representation size |
| Encoder | Converts input into compressed representation |
| Decoder | Reconstructs an image from compressed representation |
| Bitstream | Encoded sequence of bits |
| Redundancy | Information that can be represented more efficiently |
| Lossless | Exact reconstruction |
| Lossy | Approximate reconstruction permitted |
| Compression ratio | Original size / compressed size |
| Bitrate | Number of bits used per unit of data |
| bpp | Bits per pixel |
| Distortion | Difference introduced by approximation |
| Quantization | Mapping values to a reduced set of representation levels |

---

# 31. Compression Decision Matrix

| Requirement | Preferred direction |
|---|---|
| Exact numerical recovery | Lossless |
| Maximum size reduction | Lossy may be appropriate |
| Photographic web content | Often lossy |
| Archival exactness | Lossless |
| Repeated numerical analysis | Lossless |
| Bandwidth-constrained delivery | Higher compression, subject to quality |
| Text/line-art preservation | Often lossless |
| Unknown downstream use | Preserve original / use lossless |

This is a decision aid, not a universal codec rule.

---

# 32. Bridge to C22

Compression fundamentals establish **why** compression works.

C22 now asks a more precise question:

> **How can symbols be encoded using as few bits as possible?**

The progression is:

```text
C21
Why compress?
     ↓
Redundancy
     ↓
Lossless vs lossy
     ↓
Compression metrics
     ↓
C22
Entropy + RLE + Huffman
     ↓
C23
Transform coding + DCT
     ↓
C24
JPEG end to end
```

---

# 33. Exam Lens

## 2-mark questions

**What is image compression?**  
Reduction in the number of bits required to represent image information.

**What is lossless compression?**  
Compression in which decompression reproduces the exact original image data.

**What is lossy compression?**  
Compression that permits controlled information loss to obtain greater size reduction.

**Define compression ratio.**

\[
CR=\frac{S_o}{S_c}.
\]

---

## 5-mark question

### Explain different forms of image redundancy.

A strong answer should name and explain:

1. coding redundancy;
2. spatial redundancy;
3. interchannel/spectral redundancy;
4. perceptual redundancy.

Then connect each to a compression strategy.

---

## 10-mark question

### Compare lossless and lossy image compression.

Structure:

```text
definition
→ reconstruction property
→ information loss
→ compression strength
→ examples/use cases
→ advantages
→ limitations
→ engineering choice
```

---

# 34. Chapter Checkpoint

### Concept

Why can a highly structured image compress better than a random image?

### Numerical

A 10 MB file is compressed to 2.5 MB. Find:

1. compression ratio;
2. percentage size reduction.

### Reasoning

Why is lossless compression usually safer for quantitative image analysis?

### Engineering

A web service must transmit photographs over limited bandwidth. The application tolerates small visible differences but not severe artifacts. Which broad compression family is likely suitable, and why?

### Forward connection

Which idea from C21 explains why Huffman coding can reduce the average number of bits per symbol?

---

# 35. One-Page Recall Sheet

```text
IMAGE COMPRESSION
│
├── Goal
│   └── fewer bits
│
├── Why possible?
│   ├── coding redundancy
│   ├── spatial redundancy
│   ├── interchannel redundancy
│   └── perceptual redundancy
│
├── Lossless
│   └── exact reconstruction
│
├── Lossy
│   └── approximate reconstruction
│
├── Metrics
│   ├── CR = original / compressed
│   ├── reduction% = (1 - Sc/So) × 100
│   └── bpp = bits / pixels
│
└── Core engineering trade-off
    └── size ↔ quality ↔ complexity
```

---

# 36. Cross-Book Links

| Layer | Connection |
|---|---|
| MAIN | C21 complete conceptual foundation |
| MATH | Entropy and probability become important in C22 |
| LAB | LAB-07 uses manual JPEG compression workflow |
| CODE | Raw-size, ratio, entropy, and codec experiments |
| EXAM | Lossless/lossy, redundancy, numerical metrics |
| PRACTICE | Compression calculations and method selection |
| RESOURCE | Gonzalez & Woods; Szeliski; course references |
| ASSETS | Redundancy diagrams, rate–quality sketches, codec pipeline |
| MASTER | Coverage and dependency tracking |

---

# 37. Final Chapter Summary

The central mental model is:

> **Compression is a representation problem.**

Images contain redundancy because their values are structured and statistically non-random. Compression exploits that structure through more efficient coding, representation changes, and—when allowed—controlled removal of information.

The most important distinction is:

\[
\boxed{\text{Lossless: exact recovery}}
\]

versus

\[
\boxed{\text{Lossy: approximate recovery}}
\]

Everything that follows in this part of the MiniBook builds on that distinction.

---

**Next chapter:** C22 — Entropy, Run-Length Encoding and Huffman Coding
