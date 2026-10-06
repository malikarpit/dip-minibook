---
id: "C24"
title: "JPEG Compression End to End"
layer: "MAIN"
part: "IV — Compressing Images"
unit: "Unit III"
version: "1.0"
status: "PRODUCTION"
syllabus_scope: "JPEG Compression Steps and Implementation"
tags:
  - digital-image-processing
  - jpeg
  - image-compression
  - dct
  - chroma-subsampling
  - quantization
  - zig-zag
  - entropy-coding
prerequisites:
  - "C05 — Colour Models and Image File Formats"
  - "C21 — Image Compression Fundamentals"
  - "C22 — Entropy, RLE and Huffman Coding"
  - "C23 — Transform Coding and DCT"
related_math:
  - "DCT"
  - "Quantization"
  - "Compression ratio"
  - "Entropy"
related_lab:
  - "LAB-07 — Image Compression"
related_code:
  - "CODE-07 — Manual JPEG Components"
related_exam:
  - "EXAM-JPEG"
related_practice:
  - "PRACTICE-JPEG-Pipeline"
---

# C24 — JPEG Compression End to End

> **Chapter thesis:** JPEG compresses photographic images by changing colour representation, exploiting spatial correlation with block DCT, discarding selected information through quantization, rearranging coefficients to expose zero runs, and then applying efficient entropy coding.

---

# 1. Why This Chapter Exists

The University syllabus explicitly requires:

> **JPEG Compression Steps and Implementation.** fileciteturn4file0L41-L45

The practical syllabus goes further by requiring students to **implement JPEG compression steps manually** using Python/NumPy/PIL or MATLAB. fileciteturn4file0L68-L74

Therefore this chapter is not just a JPEG overview.

You should finish it able to trace the data from:

```text
RGB image
    ↓
colour representation
    ↓
chroma handling
    ↓
8×8 blocks
    ↓
level shift
    ↓
DCT
    ↓
quantization
    ↓
zig-zag
    ↓
DC/AC coding
    ↓
entropy coding
    ↓
JPEG bitstream
```

and the reverse process during decoding.

---

# 2. Learning Contract

After this chapter, you should be able to:

- explain what JPEG is designed for;
- state why JPEG is usually considered lossy in its baseline photographic form;
- explain the full encoding and decoding pipelines;
- explain RGB-to-YCbCr-style colour conversion at a conceptual level;
- explain luminance and chrominance;
- explain chroma subsampling;
- explain 8×8 block processing;
- explain level shifting;
- apply the DCT stage conceptually;
- apply quantization to a small matrix;
- explain zig-zag ordering;
- explain DC and AC coefficient coding;
- explain zero-run coding;
- explain Huffman entropy coding;
- identify where information is discarded;
- calculate simplified compression metrics;
- implement the teaching pipeline in Python or MATLAB;
- diagnose common JPEG artifacts.

---

# 3. What JPEG Is

JPEG originally refers to a family of image coding standards associated with the Joint Photographic Experts Group.

In everyday usage, “JPEG” often refers to files using the `.jpg` or `.jpeg` extension.

For this course, the important focus is the baseline lossy photographic compression process.

Do not treat every feature associated with the broader JPEG family as identical to baseline JPEG.

This chapter teaches the **conceptual baseline JPEG pipeline** needed for the university course and practical.

---

# 4. Why JPEG Became Important

Photographs are large numerical datasets.

A raw 24-bit RGB image requires approximately:

\[
24\text{ bits/pixel}.
\]

For large images, that becomes expensive in:

- storage;
- transmission;
- web delivery;
- camera systems;
- multimedia systems.

JPEG exploits characteristics of natural photographs to reduce this cost while maintaining acceptable visual quality over a useful range of settings.

---

# 5. Master JPEG Encoding Pipeline

The most useful diagram to memorize is:

```text
RGB IMAGE
   │
   ▼
Colour conversion
   │
   ▼
Luminance + chrominance representation
   │
   ▼
Optional chroma subsampling
   │
   ▼
8×8 block partitioning
   │
   ▼
Level shift
   │
   ▼
2-D DCT
   │
   ▼
Quantization
   │
   ▼
Zig-zag scan
   │
   ├────► DC coding
   │
   └────► AC run/size coding
             │
             ▼
      Entropy coding
             │
             ▼
        JPEG bitstream
```

This pipeline should become the backbone of your practical and exam answer.

---

# 6. The First Major Idea: Colour Conversion

JPEG commonly operates on a luminance/chrominance representation rather than directly compressing RGB independently.

Conceptually:

```text
RGB
 ↓
Y   = luminance-like component
Cb  = blue-difference chroma component
Cr  = red-difference chroma component
```

The exact equations and coding conventions can vary, but the underlying engineering idea is:

> **Brightness information and colour-difference information can be represented separately.**

---

# 7. Why Separate Brightness and Colour?

Human vision is generally more sensitive to spatial detail in luminance than to equally fine chrominance detail.

This means a codec can often preserve luminance relatively carefully while reducing chrominance sampling or precision more aggressively.

That motivates chroma subsampling.

### Important warning

This does not mean chroma information is unimportant.

It means the system can exploit a perceptual trade-off.

---

# 8. Conceptual RGB → YCbCr-Style Transformation

A commonly encountered full-range conversion is conceptually represented by equations such as:

\[
Y=
0.299R+0.587G+0.114B
\]

\[
Cb=
-0.168736R-0.331264G+0.5B+128
\]

\[
Cr=
0.5R-0.418688G-0.081312B+128.
\]

These equations are useful for understanding the separation of brightness and chroma.

### Caveat

JPEG implementation details can involve specific range, offset, and sampling conventions. Different APIs may expose normalized or differently scaled variants.

Therefore:

> **Do not assume that every RGB↔YCbCr function uses identical equations and ranges.**

---

# 9. Worked Colour Example

For a pure white pixel:

\[
R=G=B=255.
\]

Using the common full-range conceptual equations:

\[
Y=255.
\]

The chroma channels are approximately centered near their neutral value.

This is intuitively sensible:

```text
white
→ maximum brightness
→ little colour difference
```

For a grey pixel where:

\[
R=G=B,
\]

the chrominance difference is similarly near neutral.

---

# 10. Chroma Subsampling

Once luminance and chrominance are separated, chroma may be sampled at lower spatial resolution.

Common notation includes:

```text
4:4:4
4:2:2
4:2:0
```

These describe relative sampling of luma and chroma components.

### Conceptual comparison

| Scheme | Chroma resolution | General effect |
|---|---|---|
| 4:4:4 | Full | Highest chroma detail |
| 4:2:2 | Reduced horizontally | Lower data |
| 4:2:0 | Reduced horizontally and vertically | Greater data reduction |

The exact sample arrangement is standardized and should be treated carefully when implementing a real encoder.

---

# 11. Why Chroma Subsampling Helps

Suppose a system can reduce chroma samples while keeping luminance detail relatively high.

Then:

```text
less chroma data
+
mostly preserved luma detail
→
lower total rate
```

This is a form of controlled information reduction.

It is one reason a JPEG representation can use significantly fewer bits than raw RGB.

---

# 12. 8×8 Block Partitioning

Each component is divided into small blocks.

For baseline JPEG, the standard block size is:

\[
8\times8.
\]

Thus each block has:

\[
64
\]

samples.

The transform is then applied block by block.

Conceptually:

```text
large image
┌─────────────────────────┐
│ 8×8 │ 8×8 │ 8×8 │ ...  │
├─────┼─────┼─────┼───────┤
│ 8×8 │ 8×8 │ 8×8 │ ...  │
├─────┼─────┼─────┼───────┤
│ ...                         │
└─────────────────────────┘
```

---

# 13. Why Blocks Are Useful

A local block is:

- small enough for efficient processing;
- large enough to capture meaningful local spatial variation;
- suitable for DCT basis representation.

But blocking creates a known side effect.

At high compression, adjacent blocks can reconstruct differently.

This can produce:

```text
| block | block |
| edges | edges |
```

and visible square boundaries.

This is the **blocking artifact**.

---

# 14. Boundary Handling

Image dimensions are not always multiples of 8.

Suppose:

\[
W=1017,\qquad H=769.
\]

Both dimensions require handling before forming complete 8×8 blocks.

A teaching implementation may use padding.

Possible policies include:

- zero padding;
- edge replication;
- reflection.

A real codec has standardized implementation rules and signaling details.

The learning point is:

> **Always define what happens at the image boundary.**

Otherwise a manual implementation may silently produce shape or quality errors.

---

# 15. Level Shift

For a typical 8-bit sample:

\[
0\le f\le255.
\]

The JPEG-style transform preparation centers the values:

\[
f'=f-128.
\]

Therefore:

```text
0   → -128
64  → -64
128 → 0
192 → 64
255 → 127
```

This shifts the block around zero before the DCT.

---

# 16. Why Level Shift Helps

The DCT naturally works with positive and negative variations around a baseline.

Centering the samples makes the numerical representation more convenient.

Remember:

> **Level shifting is a preprocessing step; it is not the compression loss.**

---

# 17. Apply the 2-D DCT

For each 8×8 block:

\[
F(u,v)
=
\alpha(u)\alpha(v)
\sum_{x=0}^{7}
\sum_{y=0}^{7}
f'(x,y)
\cos
\left[
\frac{(2x+1)u\pi}{16}
\right]
\cos
\left[
\frac{(2y+1)v\pi}{16}
\right].
\]

The resulting block still contains 64 coefficients.

The number of values has not magically fallen.

What has changed is the **representation**.

---

# 18. Interpreting an 8×8 DCT Matrix

Conceptually:

```text
┌───────────────────────────┐
│ DC | low frequencies      │
│────┼──────────────────────│
│ low frequencies           │
│                            │
│      progressively         │
│      higher frequencies    │
└───────────────────────────┘
```

The top-left coefficient:

\[
F(0,0)
\]

is the DC component.

The remaining 63 are AC coefficients.

---

# 19. Quantization — The Main Lossy Stage

Now apply a quantization matrix \(Q\):

\[
\hat F(u,v)
=
\operatorname{round}
\left(
\frac{F(u,v)}{Q(u,v)}
\right).
\]

During decoding:

\[
F_{\text{recon}}(u,v)
=
\hat F(u,v)Q(u,v).
\]

Because of rounding:

\[
F_{\text{recon}}\neq F
\]

in general.

This is why the usual baseline JPEG process is lossy.

---

# 20. Simplified Quantization Example

Suppose:

\[
F=
\begin{bmatrix}
400&40&12&5\\
32&10&4&2\\
15&5&2&1\\
4&2&1&0
\end{bmatrix}
\]

and for teaching we use:

\[
Q=
\begin{bmatrix}
10&10&16&20\\
10&16&20&24\\
16&20&24&28\\
20&24&28&32
\end{bmatrix}.
\]

Then:

\[
\hat F=
\operatorname{round}(F/Q).
\]

Examples:

\[
400/10=40
\]

\[
40/10=4
\]

\[
12/16=0.75\rightarrow1
\]

\[
5/20=0.25\rightarrow0.
\]

Several small coefficients become zero.

The exact JPEG tables are standardized examples of this broader idea.

---

# 21. Why Quantization Produces Compression Opportunity

Before quantization:

```text
many different coefficient values
```

After quantization:

```text
fewer levels
+
many zeros
+
repeated small integer values
```

This makes later coding much more efficient.

Therefore:

```text
DCT
→ exposes frequency structure

Quantization
→ reduces precision

Zig-zag + RLE
→ exposes zero runs

Entropy coding
→ exploits statistical frequency
```

---

# 22. Where Information Is Discarded

The most important exam and viva question is:

> **Where does JPEG lose information?**

For the conventional lossy pipeline, the major intentional loss comes from:

\[
\boxed{\text{quantization}}
\]

There can also be information reduction from chroma subsampling when used.

The following stages are primarily representational/coding operations:

```text
DCT             → transform
zig-zag         → ordering
RLE             → lossless representation
Huffman coding  → lossless coding
```

This distinction should be explicitly remembered.

---

# 23. Quantization Strength and Quality

Stronger quantization generally means:

```text
larger Q values
→
coarser coefficient representation
→
more information discarded
→
higher compression
→
potentially lower quality
```

Weaker quantization generally means:

```text
smaller Q values
→
finer coefficient representation
→
less loss
→
larger compressed size
→
higher quality
```

Thus:

\[
\boxed{
\text{compression}
\leftrightarrow
\text{quality}
}
\]

is not a fixed relationship; it is controlled by operating choices.

---

# 24. Quality Factor — Conceptual View

Image software often exposes a “quality” parameter.

Do not interpret:

```text
quality = 80
```

as though it were universally:

\[
80\% \text{ of original image quality}.
\]

The parameter usually influences quantization tables or related encoder settings.

Different encoders can map the same numerical quality setting differently.

Therefore:

> **A quality number is an encoder parameter, not a universal perceptual measurement.**

---

# 25. Zig-Zag Scan

After quantization, the coefficients are traversed in a standardized zig-zag order.

Conceptually:

```text
 0 → 1 → 5 → 6 → 14 → ...
 ↓
 2 → 4 → 7 → 13 → ...
 ↓
 3 → 8 → 12 → ...
```

The exact JPEG zig-zag order should be implemented from a fixed table.

The purpose is:

```text
low-frequency coefficients
→ early positions

high-frequency coefficients
→ later positions
```

Since many high-frequency coefficients have become zero, long zero runs appear toward the end.

---

# 26. DC Coding

The DC coefficient represents the block's average-like component.

Neighbouring image blocks often have similar DC values.

Instead of independently coding every DC coefficient, JPEG can code differences between successive DC values.

Conceptually:

\[
\Delta DC_i=DC_i-DC_{i-1}.
\]

Example:

```text
DC values:
100, 102, 105, 104

differences:
100, +2, +3, -1
```

The differences are often smaller and therefore easier to encode efficiently.

This exploits inter-block correlation.

---

# 27. AC Coding

The 63 remaining values are AC coefficients.

After zig-zag scanning, there may be:

```text
12
3
0
0
0
-2
0
0
0
0
...
```

Rather than storing every zero explicitly, JPEG represents zero runs together with information about the next nonzero coefficient.

This is a more structured form of run-length coding than the simplest `(count, symbol)` example from C22.

---

# 28. AC Run-Length Intuition

Consider:

```text
5, 0, 0, 0, 0, -2, 0, 0, 0, 0...
```

Instead of:

```text
5,0,0,0,0,-2,0,0,0,0
```

the encoder can conceptually represent:

```text
5
→ zero-run = 4, value = -2
→ ...
```

The exact JPEG syntax uses categories/size information and special symbols such as **EOB** (End of Block). The teaching model is enough to understand why the representation becomes compact.

---

# 29. EOB — End of Block

When all remaining coefficients are zero, JPEG does not need to list every remaining zero.

It can indicate:

```text
no more nonzero AC coefficients
```

with an end-of-block representation.

Conceptually:

```text
nonzero
→ zero run + next value
→ zero run + next value
→ EOB
```

This can save many bits for smooth blocks.

---

# 30. Entropy Coding

After coefficient representation, symbols are entropy-coded.

Baseline JPEG uses Huffman coding as one of its standard entropy-coding options.

The information arriving here has already been transformed into a representation with favourable statistics.

Thus:

```text
DCT
→ transform correlation

quantization
→ many zeros / reduced precision

zig-zag
→ clusters zeros

RLE
→ compact zero-run symbols

Huffman
→ compact variable-length codes
```

This is the complete logic of the pipeline.

---

# 31. JPEG Encoding — Full Conceptual View

```text
                 ┌──────────────────────────────┐
                 │            RGB IMAGE         │
                 └──────────────┬───────────────┘
                                ↓
                    Colour conversion
                                ↓
                    Y / Cb / Cr-like data
                                ↓
                     Chroma subsampling
                                ↓
                       8×8 block split
                                ↓
                         Level shift
                                ↓
                           2-D DCT
                                ↓
                        64 coefficients
                                ↓
                         Quantization
                                ↓
                    mostly small/zero terms
                                ↓
                         Zig-zag order
                                ↓
                 ┌──────────────┴──────────────┐
                 ↓                             ↓
              DC coding                    AC coding
                 │                        run/size/EOB
                 └──────────────┬──────────────┘
                                ↓
                       Entropy coding
                                ↓
                        JPEG bitstream
```

---

# 32. JPEG Decoding — Reverse Direction

The decoder performs the reverse logical operations:

```text
JPEG bitstream
      ↓
entropy decoding
      ↓
recover coefficient symbols
      ↓
inverse zig-zag
      ↓
dequantization
      ↓
inverse DCT
      ↓
undo level shift
      ↓
upsample chroma where necessary
      ↓
colour conversion
      ↓
reconstructed image
```

The decoder does not recover information discarded during quantization.

Therefore:

\[
\boxed{\text{decompression} \neq \text{restoration of the original}}
\]

It reconstructs the best image represented by the stored compressed information.

---

# 33. Dequantization

If the quantized coefficient is:

\[
\hat F(u,v),
\]

the decoder estimates:

\[
F'(u,v)=
\hat F(u,v)Q(u,v).
\]

Example:

Encoder:

\[
F=17,\quad Q=10
\]

\[
\hat F=\operatorname{round}(1.7)=2.
\]

Decoder:

\[
F'=2(10)=20.
\]

Original:

\[
17.
\]

Reconstructed coefficient:

\[
20.
\]

The difference:

\[
20-17=3
\]

cannot be recovered from the compressed representation.

---

# 34. Inverse DCT

After dequantization, the inverse DCT reconstructs the block.

Conceptually:

\[
f'(x,y)=
\sum_{u=0}^{7}
\sum_{v=0}^{7}
\alpha(u)\alpha(v)
F'(u,v)
\cos
\left[
\frac{(2x+1)u\pi}{16}
\right]
\cos
\left[
\frac{(2y+1)v\pi}{16}
\right].
\]

After inverse transform, the level shift is undone:

\[
f(x,y)=f'(x,y)+128.
\]

The exact implementation includes the relevant rounding/clipping rules.

---

# 35. Clipping and Reconstruction

Numerical inverse operations can produce values outside the valid display range.

For 8-bit samples, values are typically clipped/rounded back into:

\[
[0,255].
\]

Conceptually:

```text
inverse transform
→ floating-point values
→ rounding
→ clipping
→ 8-bit samples
```

This is another reason a manual implementation must be explicit about numeric types.

---

# 36. JPEG Artifacts

At stronger compression, you may observe:

### Blocking

Square boundaries around 8×8 blocks.

Cause:

```text
independent block processing
+
strong coefficient quantization
```

### Ringing

Oscillatory patterns near strong edges.

Cause:

```text
loss of higher-frequency transform information
```

### Colour artifacts

Can become more visible when chroma is strongly subsampled or compressed.

### Loss of fine texture

Fine detail can disappear as higher-frequency coefficients are heavily quantized.

---

# 37. Quality–Size Trade-off

Consider three conceptual JPEG settings:

```text
High quality
→ large file
→ fewer artifacts

Medium quality
→ smaller file
→ moderate artifacts

Low quality
→ very small file
→ visible loss
```

This is not a guarantee that every image follows exactly the same visual progression, but it is the fundamental engineering trade-off.

---

# 38. Worked Compression Example

Suppose an uncompressed image occupies:

\[
8\text{ MB}
\]

and the JPEG is:

\[
1.6\text{ MB}.
\]

Compression ratio:

\[
CR=\frac{8}{1.6}=5.
\]

Therefore:

\[
\boxed{5:1}
\]

Percentage reduction:

\[
\left(1-\frac{1.6}{8}\right)100
\]

\[
=(1-0.2)100
\]

\[
=\boxed{80\%}.
\]

---

# 39. Why JPEG Works Especially Well for Photographs

The pipeline matches statistical properties of natural images:

```text
RGB correlation
     ↓
colour transform / chroma reduction

spatial correlation
     ↓
DCT

fine detail can be less important perceptually
     ↓
quantization

many small/zero coefficients
     ↓
zig-zag + RLE

unequal symbol frequencies
     ↓
Huffman coding
```

JPEG is therefore not “one compression trick.”

It is a **chain of complementary transformations**.

---

# 40. JPEG and PNG Are Not “Quality Levels”

A frequent mistake is:

> “JPEG = compressed image, PNG = higher-quality JPEG.”

This is incorrect.

JPEG and PNG use fundamentally different compression approaches.

At a high level:

| Property | JPEG | PNG |
|---|---|---|
| Typical photographic use | Strong | Possible but often larger |
| Typical compression | Lossy in common photographic workflow | Lossless |
| Uses DCT | Yes in baseline JPEG | No |
| Transparency support | Not the same as PNG | Yes |
| Exact pixel recovery | Not in lossy JPEG workflow | Yes |
| Strong for sharp line/text graphics | Can introduce artifacts | Often excellent |

The file format choice depends on image content and requirements.

---

# 41. JPEG vs. Lossless JPEG

Do not generalize:

```text
JPEG = always lossy
```

The broader JPEG family includes lossless-related modes and extensions.

For this university course, however, the practical “JPEG compression steps” usually refers to the familiar baseline photographic pipeline taught above.

When answering an exam question, state your scope clearly if needed.

---

# 42. JPEG Implementation Strategy

The practical syllabus asks for manual JPEG compression steps. fileciteturn4file0L68-L74

A good teaching implementation should **not** simply call:

```python
cv2.imwrite("out.jpg", image, [quality])
```

and claim that the JPEG algorithm has been implemented.

That tests library usage, not understanding.

Instead, build the conceptual components:

```text
input
→ convert colour
→ choose one component
→ split into 8×8 blocks
→ level shift
→ DCT
→ quantize
→ zig-zag
→ RLE-like coefficient representation
→ inspect output
```

A complete standards-compliant JPEG writer is a substantially larger engineering project because the JPEG file structure, tables, markers, entropy coding, sampling factors, restart intervals, and bit packing must also be handled.

For the course practical, a **manual component-level implementation** is an excellent learning target.

---

# 43. Python — Manual JPEG-Like Encoder Core

```python
from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np
from scipy.fft import dct


Q_LUMA = np.array(
    [
        [16, 11, 10, 16, 24, 40, 51, 61],
        [12, 12, 14, 19, 26, 58, 60, 55],
        [14, 13, 16, 24, 40, 57, 69, 56],
        [14, 17, 22, 29, 51, 87, 80, 62],
        [18, 22, 37, 56, 68, 109, 103, 77],
        [24, 35, 55, 64, 81, 104, 113, 92],
        [49, 64, 78, 87, 103, 121, 120, 101],
        [72, 92, 95, 98, 112, 100, 103, 99],
    ],
    dtype=np.float64,
)

ZIGZAG = [
    (0, 0),
    (0, 1), (1, 0),
    (2, 0), (1, 1), (0, 2),
    (0, 3), (1, 2), (2, 1), (3, 0),
    (4, 0), (3, 1), (2, 2), (1, 3), (0, 4),
    (0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0),
    (6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6),
    (0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0),
    (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7),
    (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2),
    (7, 3), (6, 4), (5, 5), (4, 6), (3, 7),
    (4, 7), (5, 6), (6, 5), (7, 4),
    (7, 5), (6, 6), (5, 7),
    (6, 7), (7, 6),
    (7, 7),
]


def dct2(block: np.ndarray) -> np.ndarray:
    tmp = dct(block, axis=0, norm="ortho")
    return dct(tmp, axis=1, norm="ortho")


def quantize(coeff: np.ndarray, qtable: np.ndarray) -> np.ndarray:
    return np.round(coeff / qtable).astype(np.int32)


def zigzag_scan(block: np.ndarray) -> list[int]:
    return [int(block[r, c]) for r, c in ZIGZAG]


def rle_zeros(values: list[int]) -> list[tuple[int, int]]:
    output: list[tuple[int, int]] = []
    run = 0

    for value in values:
        if value == 0:
            run += 1
        else:
            output.append((run, value))
            run = 0

    return output


image_path = Path("sample.png")
image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError(f"Could not read {image_path}")

block = image[:8, :8].astype(np.float64) - 128.0

coeff = dct2(block)
qcoeff = quantize(coeff, Q_LUMA)
sequence = zigzag_scan(qcoeff)

print("Input 8×8 block:")
print(block.astype(int))

print("\nQuantized coefficients:")
print(qcoeff)

print("\nZig-zag sequence:")
print(sequence)

print("\nNon-zero run/value pairs:")
print(rle_zeros(sequence))
```

This is a **JPEG-like educational core**, not a complete `.jpg` file writer.

---

# 44. MATLAB — Manual JPEG-Like Block

```matlab
img = imread('sample.png');

if ndims(img) == 3
    img = rgb2gray(img);
end

img = double(img);

% Select one 8x8 block for demonstration.
block = img(1:8, 1:8);

% JPEG-style level shift.
shifted = block - 128;

% DCT.
coeff = dct2(shifted);

% Simplified demonstration quantization table.
Q = [
    16 11 10 16 24 40 51 61;
    12 12 14 19 26 58 60 55;
    14 13 16 24 40 57 69 56;
    14 17 22 29 51 87 80 62;
    18 22 37 56 68 109 103 77;
    24 35 55 64 81 104 113 92;
    49 64 78 87 103 121 120 101;
    72 92 95 98 112 100 103 99
];

qcoeff = round(coeff ./ Q);

disp('Original block:');
disp(block);

disp('DCT coefficients:');
disp(coeff);

disp('Quantized coefficients:');
disp(qcoeff);
```

This allows the practical student to inspect:

```text
original block
→ DCT coefficients
→ quantized coefficients
```

before implementing the remaining scan/coding stages.

---

# 45. Manual Implementation Validation

A good implementation should produce evidence at each stage.

Save or display:

```text
1. original image
2. Y / luminance image
3. one 8×8 block
4. shifted block
5. DCT coefficient matrix
6. quantized coefficient matrix
7. zig-zag sequence
8. run/value sequence
9. reconstructed block
10. reconstructed image
11. difference image
12. final file-size comparison
```

This is much stronger than displaying only the final JPEG.

---

# 46. Difference Image

To inspect reconstruction error:

\[
D(x,y)=I(x,y)-\hat I(x,y).
\]

For visualization:

```python
difference = cv2.absdiff(original, reconstructed)
```

A heatmap or amplified display can show where compression changed the image.

Remember:

```text
difference image
≠
original image
```

It is a diagnostic representation.

---

# 47. Quality Evaluation

Useful measurements include:

\[
MSE=
\frac{1}{MN}
\sum_{x,y}
(I-\hat I)^2
\]

and:

\[
PSNR=
10\log_{10}
\left(
\frac{255^2}{MSE}
\right)
\]

for 8-bit images.

A stronger practical evaluation compares:

```text
file size
+
compression ratio
+
MSE
+
PSNR
+
visual artifact inspection
```

This connects directly to C21.

---

# 48. Practical 7 — Experiment Blueprint

The university practical states:

> Implement JPEG compression steps manually using Python (NumPy, PIL) or MATLAB. fileciteturn4file0L68-L74

### Objective

Understand and implement the principal stages of JPEG-style image compression.

### Suggested sequence

```text
1. Load image
2. Convert to suitable colour representation
3. Select luminance / colour components
4. Apply optional chroma sampling
5. Pad dimensions if needed
6. Divide into 8×8 blocks
7. Level shift
8. DCT
9. Quantization
10. Zig-zag scan
11. DC / AC representation
12. Run-length handling
13. Entropy coding concept
14. Decode
15. Reconstruct image
16. Compare size and quality
```

### Evidence

| Evidence | Why |
|---|---|
| Original image | Baseline |
| One raw block | Understand spatial data |
| DCT block | Understand transform |
| Quantized block | See information reduction |
| Zig-zag sequence | Understand coefficient ordering |
| RLE output | Understand zero-run coding |
| Reconstruction | Verify decoder |
| Difference | Localize distortion |
| MSE/PSNR | Numerical evaluation |
| File-size comparison | Compression measurement |

---

# 49. Full JPEG Reasoning Table

| Stage | Input | Output | Main purpose | Lossy? |
|---|---|---|---|---|
| Colour conversion | RGB | Y/Cb/Cr-like components | separate brightness/chroma | No by itself |
| Chroma subsampling | Full chroma | fewer chroma samples | reduce data | Can discard information |
| Blocking | image | 8×8 blocks | local processing | No |
| Level shift | samples | centered samples | prepare transform | No |
| DCT | pixels | coefficients | expose frequency structure | No |
| Quantization | coefficients | reduced-precision coefficients | compress/remove less-important detail | **Yes** |
| Zig-zag | coefficient matrix | ordered sequence | expose low→high frequency structure | No |
| RLE | sequence | run/value symbols | compress zero runs | No |
| Huffman | symbols | bitstream | efficient coding | No |

This is one of the most important tables in the chapter.

---

# 50. Common Traps

### Trap 1 — DCT itself is the lossy step.

Not necessarily.

DCT can be inverted.

### Trap 2 — JPEG stores transformed coefficients directly without quantization.

Baseline JPEG quantizes the DCT coefficients before entropy coding.

### Trap 3 — Huffman coding causes the visual loss.

No.

Huffman coding is lossless coding of the already-selected symbols.

### Trap 4 — Zig-zag compresses by itself.

No.

It rearranges coefficients so zero runs become easier to encode.

### Trap 5 — JPEG compression ratio is fixed.

No.

It depends on image content, chroma sampling, quantization, encoder settings, and overhead.

### Trap 6 — Quality 90 means 90% original quality.

No.

It is an encoder-specific setting.

### Trap 7 — All JPEG images have exactly the same internal tables.

No.

Quantization and Huffman tables can vary, and JPEG supports different sampling/configuration details.

### Trap 8 — A JPEG decoder can reconstruct discarded details.

No.

Information removed during lossy encoding cannot be recovered exactly.

---

# 51. Exam Lens

## 2-mark questions

**What is JPEG?**  
A widely used image coding standard/family whose common baseline photographic workflow combines colour representation, 8×8 DCT, quantization, coefficient coding, and entropy coding.

**What is the JPEG block size in baseline JPEG?**

\[
\boxed{8\times8}
\]

**Where does the primary lossy operation occur?**

\[
\boxed{\text{Quantization}}
\]

**What is zig-zag scanning used for?**  
To order DCT coefficients so that low-frequency coefficients appear earlier and zero runs are concentrated toward the end.

---

# 52. 5-Mark Answer Pattern

### Explain JPEG compression.

Write:

```text
RGB
→ colour conversion
→ chroma subsampling
→ 8×8 blocking
→ level shift
→ DCT
→ quantization
→ zig-zag
→ DC/AC run coding
→ Huffman coding
→ bitstream
```

Then state:

> Quantization is the principal lossy stage in the conventional baseline workflow.

---

# 53. 10-Mark Answer Pattern

### Explain JPEG compression and decompression in detail.

Use these sections:

1. Need for JPEG;
2. colour conversion;
3. chroma subsampling;
4. 8×8 blocking;
5. level shifting;
6. DCT;
7. quantization;
8. zig-zag scanning;
9. DC coding;
10. AC run-length coding;
11. Huffman entropy coding;
12. JPEG bitstream;
13. decoding reverse path;
14. where loss occurs;
15. quality/compression trade-off;
16. artifacts.

This structure gives an examiner a clear end-to-end answer.

---

# 54. Numerical Practice

Suppose one coefficient is:

\[
F=73
\]

and:

\[
Q=16.
\]

Quantized coefficient:

\[
\hat F=
\operatorname{round}
\left(
\frac{73}{16}
\right).
\]

\[
73/16=4.5625
\]

so:

\[
\boxed{\hat F=5}.
\]

Decoder estimate:

\[
F'=5\times16=80.
\]

Thus the coefficient error is:

\[
80-73=7.
\]

This tiny example captures the central mechanism of JPEG's lossy compression.

---

# 55. Advanced Engineering Insight — Why 8×8?

The 8×8 choice balances:

```text
local adaptation
+
transform efficiency
+
computational cost
+
artifact behaviour
```

Larger blocks can capture broader spatial structure but may have greater computational cost and different artifact characteristics.

Smaller blocks provide more locality but can be less efficient for broader correlations.

JPEG standardizes 8×8 DCT blocks in its baseline architecture rather than leaving block size arbitrary.

---

# 56. Advanced Engineering Insight — DCT vs. “Frequency Filtering”

C13 used frequency-domain filters to modify an image.

JPEG uses DCT coefficients differently.

```text
Frequency filtering:
→ intentionally retain/remove frequency regions
→ output a modified image

JPEG transform coding:
→ represent image using frequency coefficients
→ quantize selected coefficients
→ encode efficiently
```

The mathematical language overlaps, but the engineering objective differs.

This is a useful bridge between the enhancement and compression parts of the MiniBook.

---

# 57. Advanced Engineering Insight — Quantization Tables

A quantization matrix controls how aggressively each coefficient is quantized.

Conceptually:

```text
small Q
→ finer precision
→ preserve more detail

large Q
→ coarser precision
→ stronger compression
```

The table can vary with:

- luminance/chroma;
- encoder quality settings;
- implementation;
- application needs.

This is why JPEG can operate at many rate–quality points.

---

# 58. Advanced Engineering Insight — What JPEG Is Good At

JPEG is particularly strong for:

- natural photographs;
- camera images;
- web photos;
- general-purpose photographic storage.

JPEG is less attractive when exact preservation of:

- hard edges;
- text;
- line drawings;
- transparency;
- pixel-level numerical values

is required.

The correct decision always depends on application constraints.

---

# 59. Chapter Checkpoint

### Q1 — Pipeline

Arrange:

```text
DCT
Huffman coding
quantization
zig-zag
colour conversion
8×8 blocking
```

### Q2 — Loss

Which operation primarily causes irreversible coefficient loss?

### Q3 — Reasoning

Why does zig-zag scanning make RLE more effective?

### Q4 — Practical

Why is merely calling a JPEG library function insufficient for the “manual JPEG compression steps” practical?

### Q5 — Numerical

If an 8 MB raw image becomes a 1 MB JPEG, calculate:

\[
CR
\]

and percentage reduction.

### Q6 — Interpretation

Why can a JPEG with a much smaller file size still look acceptable?

---

# 60. One-Page JPEG Recall Sheet

```text
JPEG
│
├── RGB
│   ↓
├── Y / Cb / Cr-style representation
│   ↓
├── Chroma subsampling
│   ↓
├── 8×8 blocks
│   ↓
├── Level shift
│   ↓
├── DCT
│   ↓
├── Quantization  ← PRIMARY LOSS
│   ↓
├── Zig-zag
│   ↓
├── DC / AC coding
│   ├── DC differences
│   └── AC zero runs + EOB
│   ↓
├── Huffman entropy coding
│   ↓
└── JPEG bitstream

DECODE
bitstream
→ entropy decode
→ inverse coefficient ordering
→ dequantize
→ inverse DCT
→ undo level shift
→ chroma upsample
→ colour conversion
→ image
```

---

# 61. Cross-Book Links

| Layer | Connection |
|---|---|
| MAIN | C24 is the complete JPEG teaching chapter |
| MATH | DCT, quantization, compression metrics |
| LAB | Practical 7 — manual JPEG compression |
| CODE | Python/NumPy/MATLAB component implementation |
| EXAM | Full pipeline, loss location, numerical compression |
| PRACTICE | Pipeline ordering, coefficient calculations, debugging |
| RESOURCE | Gonzalez & Woods; Szeliski; course practical requirements |
| ASSETS | JPEG pipeline, 8×8 blocks, DCT matrix, quantization, zig-zag |
| MASTER | Completes the Unit III compression branch |

---

# 62. Final Chapter Summary

JPEG is best understood as a **pipeline of cooperating operations**:

\[
\boxed{
\text{colour representation}
\rightarrow
\text{sampling}
\rightarrow
\text{DCT}
\rightarrow
\text{quantization}
\rightarrow
\text{coefficient coding}
\rightarrow
\text{entropy coding}
}
\]

The single most important fact is:

\[
\boxed{
\text{Quantization is where the principal intentional coefficient information loss occurs}
}
\]

The second most important fact is:

\[
\boxed{
\text{DCT does not itself reduce the number of coefficients; it creates a representation that is easier to compress}
}
\]

And the third is:

\[
\boxed{
\text{JPEG compression is not one algorithmic step—it is a pipeline}
}
\]

That pipeline connects everything learned in this part:

```text
C21
Compression fundamentals
      ↓
C22
Entropy + RLE + Huffman
      ↓
C23
DCT + transform coding
      ↓
C24
JPEG end to end
```

---

# 63. Course Practical Mapping

The syllabus's seventh practical is explicitly:

> **Image Compression — Implement JPEG compression steps manually.** fileciteturn4file0L68-L74

Therefore this chapter should be used together with:

```text
C21 → why compression
C22 → coding foundations
C23 → DCT mathematics
C24 → JPEG pipeline
LAB-07 → experiment execution
CODE-07 → reusable implementation
EXAM-UNIT-III → exam answer
PRACTICE-JPEG → problem solving
```

---

**Part IV core compression theory is now complete: C21 → C24.**

**Next set:** C25 + C26 — Image Classification and Convolutional Neural Networks.
