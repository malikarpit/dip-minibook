---
id: "C23"
title: "Transform Coding and the Discrete Cosine Transform (DCT)"
layer: "MAIN"
part: "IV — Compressing Images"
unit: "Unit III"
version: "1.0"
status: "PRODUCTION"
syllabus_scope: "Supporting foundation for JPEG compression; transform coding and DCT are required to understand the JPEG compression steps and implementation"
tags:
  - digital-image-processing
  - transform-coding
  - dct
  - jpeg
  - frequency-domain
  - quantization
prerequisites:
  - "C08 — Spatial Filtering and Convolution"
  - "C12 — Fourier Transform and the Frequency Domain"
  - "C21 — Image Compression Fundamentals"
  - "C22 — Entropy, RLE and Huffman Coding"
related_math:
  - "Cosine functions"
  - "Linear transforms"
  - "Matrix multiplication"
  - "Orthogonality"
related_lab:
  - "LAB-07 — Image Compression"
related_code:
  - "CODE-07 — DCT and JPEG Components"
related_exam:
  - "EXAM-DCT"
related_practice:
  - "PRACTICE-DCT-and-Transform-Coding"
---

# C23 — Transform Coding and the Discrete Cosine Transform

> **Chapter thesis:** Transform coding changes the representation of image data so that energy is concentrated into a smaller number of coefficients, making efficient quantization and entropy coding possible.

---

# 1. Why This Chapter Exists

C21 introduced the purpose of compression.

C22 showed how statistical structure can be encoded efficiently.

But photographs contain another useful kind of structure:

> **Neighbouring pixels tend to be correlated, so representing every pixel independently is often inefficient.**

Transform coding attacks that problem by changing representation.

Instead of storing:

```text
pixel values
```

we can represent a block using:

```text
transform coefficients
```

The transform itself does not necessarily compress the data. It creates a representation that is easier to compress.

The core chain is:

```text
correlated pixels
      ↓
transform
      ↓
decorrelated / energy-concentrated coefficients
      ↓
quantization
      ↓
many small or zero coefficients
      ↓
efficient coding
```

This distinction is essential:

> **A transform is primarily a representation change; compression emerges when that representation is combined with quantization and coding.**

---

# 2. Learning Contract

After this chapter, you should be able to:

- explain transform coding;
- explain why correlation between neighbouring pixels is useful for compression;
- distinguish spatial-domain samples from transform-domain coefficients;
- explain the DCT conceptually;
- identify low-frequency and high-frequency components;
- explain the DC and AC coefficient idea;
- write the 1-D and 2-D DCT equations;
- calculate a small DCT example;
- explain why cosine basis functions are useful;
- explain the role of quantization after the DCT;
- explain why quantization creates zeros;
- describe the JPEG block-level compression pipeline;
- connect DCT to zig-zag scanning, run-length coding, and entropy coding.

---

# 3. Transform Coding: The Big Idea

Suppose an image block is:

```text
52  52  53  54
52  53  54  55
53  54  55  55
54  55  55  56
```

The values are highly related.

Storing all sixteen values separately does not explicitly expose that structure.

A transform represents the same block as weighted combinations of basis patterns.

Conceptually:

```text
spatial image block
        ↓
    transform
        ↓
frequency-like coefficient block
```

The coefficients tell us how strongly different basis patterns contribute to the original image.

---

# 4. Transformation Is Not Automatically Lossy

This is a common misconception.

A transform can be invertible.

If:

\[
Y=T(X)
\]

and:

\[
X=T^{-1}(Y),
\]

then no information has necessarily been discarded.

For an ideal exact transform:

```text
X
 ↓
Transform
 ↓
Y
 ↓
Inverse transform
 ↓
X exactly
```

The lossy step usually comes later:

```text
Y
 ↓
Quantization
 ↓
Y'
 ↓
Inverse transform
 ↓
X'
```

where:

\[
X'\neq X
\]

in general.

Thus:

\[
\boxed{\text{Transform} \neq \text{information loss}}
\]

and:

\[
\boxed{\text{Quantization can introduce the loss}}
\]

---

# 5. Why Work on Small Blocks?

JPEG uses small image blocks rather than applying one giant transform to the entire image.

For baseline JPEG, the spatial image is processed using:

\[
8\times8
\]

blocks.

Why is block processing attractive?

### Local structure

A small region can often be approximated effectively by a limited set of basis patterns.

### Computational practicality

Transforming many small blocks is manageable.

### Adaptation

Different regions of an image can receive different coefficient patterns and quantization effects.

### Important limitation

Block processing can produce visible block artifacts at strong compression.

This becomes obvious in C24.

---

# 6. Frequency Intuition

The word “frequency” can be intimidating because an image is not an audio waveform.

Here, frequency refers to how rapidly intensity changes across spatial position.

### Low spatial frequency

Slow intensity variation:

```text
dark → slightly brighter → slightly brighter → bright
```

### High spatial frequency

Rapid changes:

```text
dark → bright → dark → bright
```

Strong edges contain high-frequency components.

Broad smooth regions contain more low-frequency content.

So a transform can separate:

```text
slow variation
from
rapid variation
```

---

# 7. Basis Functions

A transform represents a signal using basis functions.

For DCT, these basis functions are cosine patterns with different spatial frequencies.

Conceptually:

```text
DC basis:
████████
████████
████████
████████

low frequency:
░░▒▒▓▓██
░░▒▒▓▓██
░░▒▒▓▓██
░░▒▒▓▓██

higher frequency:
█░█░█░█░
█░█░█░█░
█░█░█░█░
█░█░█░█░
```

These are conceptual illustrations, not exact DCT basis matrices.

The transform asks:

> **How much of each basis pattern is present in this image block?**

---

# 8. The DC Coefficient

The coefficient at the top-left of the DCT coefficient matrix is conventionally called the **DC coefficient**.

It represents the average or overall brightness component of the block, subject to transform normalization conventions.

The remaining coefficients are commonly called **AC coefficients**.

A useful mental map is:

```text
DCT coefficient matrix

[ DC | low horizontal frequencies ... ]
[ low vertical ...                 ... ]
[ ...                    high ...  ... ]
[ ...                         high ...]
```

The distance from the top-left generally increases with spatial frequency in the horizontal and vertical directions.

---

# 9. 1-D DCT

For an input sequence \(f(x)\) of length \(N\), one common orthonormal DCT-II form is:

\[
F(u)=
\alpha(u)
\sum_{x=0}^{N-1}
f(x)
\cos
\left[
\frac{\pi(2x+1)u}{2N}
\right]
\]

where:

\[
\alpha(u)=
\begin{cases}
\sqrt{\frac{1}{N}}, & u=0,\\[4pt]
\sqrt{\frac{2}{N}}, & u>0.
\end{cases}
\]

Different books and implementations may use equivalent scaling conventions.

That changes coefficient magnitudes but not the fundamental concept.

> **Always check the normalization convention before comparing hand calculations with a software library.**

---

# 10. 2-D DCT

For an \(N\times N\) image block:

\[
F(u,v)=
\alpha(u)\alpha(v)
\sum_{x=0}^{N-1}
\sum_{y=0}^{N-1}
f(x,y)
\cos
\left[
\frac{\pi(2x+1)u}{2N}
\right]
\cos
\left[
\frac{\pi(2y+1)v}{2N}
\right].
\]

For the JPEG block:

\[
N=8.
\]

Thus:

\[
F(u,v)
=
\alpha(u)\alpha(v)
\sum_{x=0}^{7}
\sum_{y=0}^{7}
f(x,y)
\cos
\left[
\frac{\pi(2x+1)u}{16}
\right]
\cos
\left[
\frac{\pi(2y+1)v}{16}
\right].
\]

---

# 11. What \(u\) and \(v\) Mean

In:

\[
F(u,v)
\]

- \(u\) indexes one spatial frequency direction;
- \(v\) indexes the other spatial frequency direction.

The pair \((u,v)\) identifies a particular 2-D cosine basis.

The DC component is:

\[
F(0,0).
\]

Large \(u\), \(v\) values correspond to higher-frequency variations along those directions.

---

# 12. Matrix Form of the DCT

A compact way to express a 2-D DCT is:

\[
F=CXC^T
\]

where:

- \(X\) = spatial-domain block;
- \(C\) = DCT transform matrix;
- \(F\) = coefficient matrix.

The inverse is:

\[
X=C^TFC
\]

for the orthonormal convention.

This form is extremely useful because it makes the connection to linear algebra explicit.

```text
X
 ↓ left multiply by C
C X
 ↓ right multiply by Cᵀ
C X Cᵀ
 ↓
F
```

---

# 13. A Small 2×2 DCT Example

To make the mathematics manageable, consider:

\[
X=
\begin{bmatrix}
10 & 10\\
10 & 10
\end{bmatrix}.
\]

This block is constant.

Therefore, intuitively:

```text
average brightness → present
variation           → absent
```

So the DC coefficient is nonzero, while AC coefficients are zero under an orthonormal DCT.

Using:

\[
C=
\frac{1}{\sqrt2}
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix},
\]

we have:

\[
F=CXC^T.
\]

First:

\[
CX
=
\frac{1}{\sqrt2}
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
\begin{bmatrix}
10&10\\
10&10
\end{bmatrix}
\]

\[
=
\frac{1}{\sqrt2}
\begin{bmatrix}
20&20\\
0&0
\end{bmatrix}.
\]

Then:

\[
F=
\frac{1}{\sqrt2}
\begin{bmatrix}
20&20\\
0&0
\end{bmatrix}
\frac{1}{\sqrt2}
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
\]

which gives:

\[
\boxed{
F=
\begin{bmatrix}
20&0\\
0&0
\end{bmatrix}
}
\]

This is an ideal demonstration of energy concentration:

> A constant image block needs only the DC component.

---

# 14. Another 2×2 Example — A Horizontal Change

Consider:

\[
X=
\begin{bmatrix}
10&20\\
10&20
\end{bmatrix}.
\]

There is:

- an average brightness;
- a horizontal intensity change;
- no vertical change.

The DCT therefore places energy primarily in:

```text
DC
+
horizontal-frequency component
```

while the coefficient corresponding to pure vertical variation is zero.

The important insight is:

> **DCT coefficients describe patterns of variation, not simply individual pixel locations.**

---

# 15. Why DCT Is Useful for Natural Images

Natural image blocks often vary smoothly.

For smooth content:

```text
low-frequency coefficients
→ relatively important

high-frequency coefficients
→ often smaller
```

This creates an opportunity.

If many high-frequency coefficients are small, quantization can reduce them to zero or coarser values.

After that:

```text
many zeros
+
repeated/small coefficient patterns
→
RLE + entropy coding
```

This is the main compression chain.

---

# 16. Energy Compaction

A major reason for using DCT is **energy compaction**.

Suppose a block's total signal energy is represented by coefficients.

A transform with good energy compaction places a large portion of useful signal energy into a small subset of coefficients.

Conceptually:

```text
Before transform

information spread across many pixels
████ ████ ████ ████ ████ ████

After DCT

large energy concentrated near DC/low frequencies
████████████
██
█
.
.
.
```

This is not a guarantee that every image or every block concentrates perfectly.

It is a statistical property exploited by the codec.

---

# 17. Transform Coefficients Are Not “Pixels”

A common beginner mistake is to interpret:

\[
F(u,v)
\]

as though it were another image with ordinary pixel values.

It is not.

A coefficient represents the strength of a particular basis function.

Thus:

```text
pixel matrix
→ actual spatial samples

DCT matrix
→ strengths of spatial-frequency components
```

The coefficient image can be visualized, but its values have a different interpretation.

---

# 18. Coefficient Sign

DCT coefficients may be:

- positive;
- negative;
- zero.

The sign describes the phase/polarity contribution of the corresponding cosine basis pattern under the chosen convention.

The magnitude indicates how strongly that component contributes.

---

# 19. Quantization After the DCT

Suppose the DCT produces:

```text
120  11   4   2
  8   4   1   1
  3   1   0   0
  1   0   0   0
```

We can divide coefficients by a quantization table and round.

Conceptually:

\[
\hat F(u,v)
=
\operatorname{round}
\left(
\frac{F(u,v)}{Q(u,v)}
\right).
\]

Then reconstruction uses:

\[
F'(u,v)
=
\hat F(u,v)Q(u,v).
\]

Because rounding is not generally reversible, this stage can lose information.

---

# 20. Why Quantization Creates Zeros

Suppose:

\[
F=7
\]

and:

\[
Q=10.
\]

Then:

\[
\operatorname{round}(7/10)=1.
\]

Suppose:

\[
F=2,\quad Q=10.
\]

Then:

\[
\operatorname{round}(2/10)=0.
\]

Small coefficients can therefore disappear.

This is enormously useful for compression because a coefficient matrix containing many zeros is easier to encode efficiently.

---

# 21. Worked Quantization Example

Suppose a coefficient block is:

\[
F=
\begin{bmatrix}
80 & 17 & 5\\
11 & 3 & 2\\
4 & 2 & 1
\end{bmatrix}
\]

and a simplified quantization matrix is:

\[
Q=
\begin{bmatrix}
8 & 10 & 16\\
10 & 16 & 20\\
16 & 20 & 24
\end{bmatrix}.
\]

Then:

\[
\hat F=
\operatorname{round}(F/Q).
\]

Element-wise:

\[
80/8=10
\]

\[
17/10=1.7\rightarrow2
\]

\[
5/16=0.3125\rightarrow0
\]

and so on.

A possible result is:

\[
\boxed{
\hat F=
\begin{bmatrix}
10&2&0\\
1&0&0\\
0&0&0
\end{bmatrix}
}
\]

Many coefficients have become zero.

This illustrates the mechanism without reproducing the full JPEG standard quantization tables.

---

# 22. Why Quantization Is Frequency-Dependent

In JPEG-style compression, quantization is typically stronger for higher spatial frequencies.

Why?

Because many natural images can tolerate some loss of fine detail more than loss of broad intensity structure.

Conceptually:

```text
DC / low frequency
→ finer preservation

higher frequency
→ stronger quantization
```

This is a perceptual engineering choice, not a mathematical law that all images must obey.

---

# 23. Compression Pipeline at the Block Level

The basic JPEG-inspired block pipeline is:

```text
8×8 image block
      ↓
level / range preparation
      ↓
2-D DCT
      ↓
64 coefficients
      ↓
quantization
      ↓
many small / zero coefficients
      ↓
zig-zag ordering
      ↓
run-length representation
      ↓
entropy coding
```

C24 will expand the JPEG-specific implementation details.

---

# 24. Why Zig-Zag Ordering Helps

After quantization, low-frequency coefficients tend to be near the top-left, while high-frequency coefficients tend to lie farther away.

A zig-zag scan orders the 8×8 coefficients approximately from lower to higher spatial frequency.

Conceptually:

```text
 0  1  5  6 ...
 2  4  7 ...
 3  8 ...
...
```

The exact standard ordering is fixed and should be treated as a lookup pattern, not guessed.

The benefit is practical:

```text
important nonzero coefficients
→ early

many zero coefficients
→ later
```

This creates long runs of zeros.

That is precisely what enables run-based coding to become effective.

---

# 25. Worked Zig-Zag Example

Suppose a quantized block becomes conceptually:

```text
10  2  0  0
 1  0  0  0
 0  0  0  0
 0  0  0  0
```

A zig-zag-like ordering groups the nonzero low-frequency values near the beginning:

```text
10, 2, 1, 0, 0, 0, 0, ...
```

The later part contains a long sequence of zeros.

An RLE representation can then record:

```text
number of zeros before next nonzero
+
nonzero coefficient
```

This is one of the important connections between:

```text
DCT
→ quantization
→ zig-zag
→ RLE
```

---

# 26. Why Not Just Quantize Pixels Directly?

Direct pixel quantization can discard information, but it does not exploit the spatial structure as effectively.

Transform coding first separates different spatial variation patterns.

That allows the compressor to treat:

```text
smooth/large-scale content
and
fine/high-frequency content
```

differently.

This provides more control over the rate–distortion trade-off.

---

# 27. DCT vs. Fourier Transform

Both describe spatial frequency information, but they are not identical.

| Aspect | DCT | DFT |
|---|---|---|
| Basis | Cosine | Complex exponential / sine + cosine |
| Typical coefficients | Real-valued | Generally complex-valued |
| Symmetry assumptions | Even-symmetry relationship | Periodic representation |
| Common JPEG role | Core block transform | Not the baseline JPEG transform |
| Compression use | Strong energy compaction for typical image blocks | More general frequency analysis |

The DCT is especially convenient for image compression because of its real coefficients and favourable energy-compaction behaviour for correlated image blocks.

---

# 28. Relation to C12

C12 introduced the frequency-domain viewpoint.

C23 applies that viewpoint to compression:

```text
C12
Fourier / frequency thinking
        ↓
C23
DCT representation
        ↓
energy compaction
        ↓
quantization
        ↓
compression
```

Do not think of DCT as unrelated to the Fourier transform family.

It belongs to the broader family of transform-domain signal representations.

---

# 29. Complexity and Implementation

A direct 2-D DCT is computationally expensive if evaluated literally from the double summation for every coefficient.

Practical libraries use optimized algorithms.

Possible implementation strategies include:

- separability;
- precomputed transform matrices;
- fast DCT algorithms;
- vectorized numerical operations;
- optimized native libraries.

### Separability

A 2-D DCT can be computed as:

```text
rows → 1-D DCT
columns → 1-D DCT
```

instead of directly evaluating every 2-D basis expression independently.

This is a general computational insight:

> **Exploit mathematical structure before optimizing code.**

---

# 30. MATLAB — Block DCT Demonstration

MATLAB provides an implementation of the 2-D DCT through `dct2`.

```matlab
img = imread('sample.png');

if ndims(img) == 3
    img = rgb2gray(img);
end

img = double(img);

F = dct2(img);

figure;
imagesc(log(abs(F) + 1));
axis image;
colormap gray;
title('Log-Magnitude DCT Coefficients');
```

The logarithm is used only for visualization so that a wide range of coefficient magnitudes can be displayed.

It does not mean JPEG stores `log(abs(F)+1)`.

That is a frequent implementation misconception.

---

# 31. Python — DCT Concept

A typical Python implementation may use SciPy for the transform.

```python
from __future__ import annotations

import cv2
import numpy as np
from scipy.fft import dct


def dct2(block: np.ndarray) -> np.ndarray:
    if block.ndim != 2:
        raise ValueError("Expected a 2-D grayscale block.")

    x = np.asarray(block, dtype=np.float64)

    # Apply an orthonormal 1-D DCT to rows,
    # then to columns.
    tmp = dct(x, axis=0, norm="ortho")
    return dct(tmp, axis=1, norm="ortho")


img = cv2.imread("sample.png", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError("Could not read sample.png")

coeff = dct2(img)

visual = np.log1p(np.abs(coeff))

print("Image shape:", img.shape)
print("DCT shape:", coeff.shape)
```

The transform's exact numerical scaling depends on the selected normalization convention.

---

# 32. Manual 8×8 Block Processing

A JPEG-like teaching implementation can process an image block by block.

```text
image
 ↓
pad to dimensions divisible by 8
 ↓
extract 8×8 block
 ↓
apply DCT
 ↓
quantize
 ↓
store coefficient block
 ↓
next 8×8 block
```

A production codec must also handle:

- image dimensions;
- data ranges;
- colour channels;
- quantization tables;
- entropy coding;
- headers and metadata.

---

# 33. Range Preparation / Level Shift

JPEG encoding commonly shifts 8-bit sample values before the DCT so that an unsigned range centered around 128 becomes approximately symmetric around zero.

For an 8-bit sample \(f\):

\[
f_{\text{shifted}}=f-128.
\]

Thus:

```text
0     → -128
128   → 0
255   → 127
```

This centers the block values for the transform.

### Important nuance

The DCT itself is not “subtract 128.” The level shift is a JPEG implementation step associated with preparing 8-bit samples for the baseline encoding process.

---

# 34. DCT and Visual Information

The transform does not identify “important pixels.”

Instead, it identifies components such as:

```text
average brightness
horizontal change
vertical change
diagonal change
fine texture
```

This allows compression to preserve major structure while coarsening selected detail.

That is why the DCT is better understood as a **representation of patterns**.

---

# 35. Engineering Failure Modes

### Failure 1 — Wrong normalization

Two DCT libraries may return different numerical values because of scaling conventions.

### Failure 2 — Forgetting level shift

A manual JPEG-like encoder may produce incorrect coefficient behaviour if the expected preprocessing convention is not followed.

### Failure 3 — Quantizing before transform

That changes the algorithm and loses the main transform-coding advantage.

### Failure 4 — Treating coefficient magnitude as an image intensity

Coefficient values have transform-domain meaning.

### Failure 5 — Assuming all energy is always in low frequencies

Natural images often exhibit concentration there, but not every image block does.

### Failure 6 — Skipping inverse testing

A transform implementation should be tested through:

```text
input
→ DCT
→ inverse DCT
→ reconstruction
→ compare with input
```

before adding quantization.

---

# 36. Verification Experiment

For a lossless transform test:

```text
original block
      ↓
DCT
      ↓
inverse DCT
      ↓
reconstructed block
```

With floating-point arithmetic, expect very small numerical differences due to finite precision.

Define:

\[
e=\max |X-\hat X|.
\]

If \(e\) is close to numerical tolerance, the transform implementation is behaving as expected.

After quantization:

\[
e
\]

will generally become nonzero by design.

---

# 37. Worked End-to-End Micro Example

Suppose an 8×8 block has:

```text
smooth intensity pattern
```

### Step 1 — DCT

Produces:

```text
large DC
several low-frequency coefficients
many smaller high-frequency coefficients
```

### Step 2 — Quantization

Small coefficients become zero:

```text
large values → retained
small values → coarse / zero
```

### Step 3 — Zig-zag

Coefficients become:

```text
large/important terms first
→
longer zero region later
```

### Step 4 — RLE

Zero runs become compact:

```text
(run length, coefficient)
```

### Step 5 — Entropy coding

The resulting symbols receive efficient variable-length codes.

Thus:

\[
\boxed{
\text{DCT enables a representation that later stages can compress efficiently}
}
\]

---

# 38. Lossy Information Flow

For a JPEG-style pipeline:

```text
Original pixels
     │
     ▼
DCT
     │
     ▼
Coefficients
     │
     ▼
Quantization
     │
     ├── information may be discarded
     ▼
Quantized coefficients
     │
     ▼
Zig-zag / RLE / entropy coding
     │
     ▼
Compressed bitstream
```

During decoding:

```text
bitstream
→ entropy decode
→ inverse run representation
→ inverse zig-zag
→ dequantization
→ inverse DCT
→ reconstructed image
```

The key loss location is:

\[
\boxed{\text{quantization}}
\]

for the usual lossy JPEG pipeline.

---

# 39. Exam Lens

## 2-mark questions

**What is transform coding?**  
A compression approach that transforms data into a representation in which redundancy can be exploited more effectively.

**What is DCT?**  
A transform that represents image samples using cosine basis functions with different spatial frequencies.

**What is the DC coefficient?**  
The coefficient representing the zero-frequency/average component of a block under the chosen DCT convention.

---

## 5-mark question

### Explain why DCT is used in image compression.

Structure:

```text
pixel correlation
→ transform
→ frequency components
→ energy compaction
→ quantization
→ zeros/small coefficients
→ RLE + entropy coding
```

---

## 10-mark question

### Explain the role of DCT in JPEG.

Include:

1. 8×8 blocking;
2. level shift where applicable;
3. 2-D DCT;
4. coefficient interpretation;
5. quantization;
6. zig-zag order;
7. run-length representation;
8. entropy coding;
9. lossy step;
10. reconstruction quality trade-off.

---

# 40. Numerical Practice Pattern

For exams, be prepared for small matrices.

A problem may provide:

\[
X=
\begin{bmatrix}
x_{00}&x_{01}\\
x_{10}&x_{11}
\end{bmatrix}
\]

and ask for a small DCT.

The safe procedure is:

```text
1. identify transform convention
2. construct C or use the equation
3. compute C X
4. compute C X Cᵀ
5. interpret DC / AC components
```

Do not silently switch normalization conventions.

---

# 41. Chapter Checkpoint

### Concept

Why does transforming an image help compression if the transform itself can be reversible?

### Mathematics

For:

\[
X=
\begin{bmatrix}
10&10\\
10&10
\end{bmatrix}
\]

under the orthonormal 2×2 DCT, determine the nonzero coefficient.

### Compression reasoning

Why does quantizing small high-frequency coefficients often create many zeros?

### Pipeline

Put the following in order:

```text
entropy coding
DCT
quantization
zig-zag
RLE
```

### Engineering

Why should a DCT implementation be tested with inverse DCT before quantization is introduced?

---

# 42. One-Page Recall Sheet

```text
TRANSFORM CODING
│
├── Goal
│   └── change representation
│
├── DCT
│   ├── cosine basis
│   ├── DC = average component
│   └── AC = variation components
│
├── Desired property
│   └── energy compaction
│
├── Quantization
│   ├── divide by Q
│   ├── round
│   └── may lose information
│
├── Then
│   ├── zig-zag
│   ├── RLE
│   └── entropy coding
│
└── JPEG bridge
    └── DCT + quantization + coding
```

---

# 43. Cross-Book Links

| Layer | Connection |
|---|---|
| MAIN | C23 explains transform coding and DCT |
| MATH | Matrix form, cosine basis, orthogonality |
| LAB | Manual JPEG / DCT experiment |
| CODE | DCT block implementation and inverse verification |
| EXAM | DCT equation, coefficient interpretation, JPEG role |
| PRACTICE | Small matrix DCT + pipeline reasoning |
| RESOURCE | Gonzalez & Woods; Szeliski |
| ASSETS | DCT basis illustrations, coefficient matrices, zig-zag diagram |
| MASTER | Direct dependency into C24 |

---

# 44. Final Chapter Summary

The core sequence is:

\[
\boxed{
\text{correlated pixels}
\rightarrow
\text{DCT}
\rightarrow
\text{energy concentration}
\rightarrow
\text{quantization}
\rightarrow
\text{zeros/sparse coefficients}
\rightarrow
\text{efficient coding}
}
\]

The most important conceptual distinction is:

> **DCT changes the representation; quantization is where controlled information loss enters the JPEG-style lossy pipeline.**

The next chapter puts the pieces together.

---

**Next chapter:** C24 — JPEG Compression End to End
