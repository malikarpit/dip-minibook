---
id: "C04"
title: "Image Representation: Pixels, Matrices, Tensors and Resolution"
layer: "MAIN"
part: "I — The Image"
unit: "I"
version: "1.0"
status: "REFERENCE BUILD"
syllabus_scope:
  - "Types of images: grayscale, RGB, multispectral"
  - "Image representation: pixels, bit depth, resolution"
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
  - "C03"
related:
  - "C05"
  - "C06"
  - "C08"
  - "C19"
  - "C25"
  - "C26"
math:
  - "M04"
  - "M05"
  - "M06"
  - "M07"
lab:
  - "LAB-U1-01"
  - "LAB-U1-03"
exam:
  - "EXAM-U1"
practice:
  - "P-C04"
assets:
  - "D-C04-01"
  - "D-C04-02"
  - "D-C04-03"
---

# Chapter 04 — Image Representation: Pixels, Matrices, Tensors and Resolution

> **Chapter thesis**  
> A digital image is not defined only by width and height. Its meaning depends on spatial organization, channels, numerical representation, intensity range, bit depth, colour model, datatype and the way the image is stored.

**Part I — The Image**  
**Syllabus anchor:** Unit I includes grayscale, RGB and multispectral images, plus pixels, bit depth and resolution. fileciteturn4file0L32-L35

---

# 04.0 Why This Chapter Exists

After sampling and quantization, we have a finite collection of numerical values.

Now we need to organize those values.

A real image-processing program needs to know:

```text
How many rows?
How many columns?
How many channels?
What datatype?
What intensity range?
What colour representation?
What does one value mean?
```

A statement such as:

```text
512 × 512
```

is useful, but incomplete.

A more informative description is:

```text
512 × 512
grayscale
uint8
0–255
```

For a colour image:

```text
1920 × 1080
RGB
uint8
3 channels
0–255 per stored channel sample
```

This chapter builds the vocabulary required to interpret such descriptions correctly.

---

# 04.1 What Is a Pixel?

## CORE — Working definition

A **pixel** is a discrete image sample/value associated with a particular spatial location in a digital image.

For a grayscale image, one pixel commonly corresponds to one intensity value.

For a colour or multispectral image, one spatial location may be associated with multiple channel values.

Conceptually:

```text
            columns →
        0    1    2    3

row 0   p    p    p    p
row 1   p    p    p    p
row 2   p    p    p    p
row 3   p    p    p    p
  ↓
 rows
```

A pixel therefore carries two linked ideas:

```text
WHERE
+
WHAT VALUE
```

---

# 04.2 Pixel Coordinates

Let a grayscale image be:

\[
I[m,n]
\]

where \(m\) and \(n\) are discrete spatial indices.

The exact starting index depends on notation and software.

A mathematical description may use:

\[
m,n\in\{0,\ldots,M-1\}
\]

while some software environments use one-based indexing.

> **WARNING:** Do not mix mathematical zero-based indexing with a programming language's indexing convention without explicitly translating it.

---

# 04.3 A Grayscale Image as a Matrix

Consider:

\[
I=
\begin{bmatrix}
10&12&13&15\\
11&18&21&16\\
12&25&30&17\\
10&15&20&14
\end{bmatrix}
\]

This is a:

\[
4\times4
\]

grayscale image.

It contains:

\[
4\times4=16
\]

spatial samples.

Each number represents one grayscale sample under the stated intensity convention.

---

# 04.4 Reading a Matrix as an Image

Suppose:

\[
I=
\begin{bmatrix}
10&10&10&10\\
10&80&80&10\\
10&80&120&10\\
10&10&10&10
\end{bmatrix}
\]

We can describe it conceptually as:

```text
dark background
+
bright rectangular region
+
very bright centre
```

The matrix contains spatial relationships.

For example, the value 120 matters not only because it is large, but because it appears next to values such as 80 and 10.

This is why image processing can detect:

- edges,
- regions,
- texture,
- shapes.

---

# 04.5 Neighbourhoods

A pixel is often processed together with nearby pixels.

For a 3×3 neighbourhood around a centre sample:

\[
\begin{bmatrix}
a&b&c\\
d&e&f\\
g&h&i
\end{bmatrix}
\]

the centre is:

\[
e
\]

and the surrounding values form its local neighbourhood.

This becomes fundamental for:

- smoothing,
- sharpening,
- edge detection,
- convolution,
- morphology,
- texture analysis.

---

# 04.6 Image Dimensions

If an image has:

\[
M\text{ rows}\times N\text{ columns}
\]

then it contains:

\[
MN
\]

spatial positions for a single-channel representation.

### Example

For:

\[
1920\times1080
\]

the number of spatial samples is:

\[
1920\times1080=2{,}073{,}600
\]

For RGB with three stored channels:

\[
2{,}073{,}600\times3
=
6{,}220{,}800
\]

channel samples.

---

# 04.7 Grayscale Images

A grayscale image normally uses one channel representing intensity-related information.

A common conceptual structure is:

\[
H\times W
\]

For example:

```text
256 × 256 grayscale
```

contains:

\[
256^2=65{,}536
\]

spatial samples.

### Why one channel?

Because the representation has one scalar value per spatial location.

This is often sufficient for operations based on intensity structure.

---

# 04.8 RGB Images

RGB represents colour using three components:

```text
Red
Green
Blue
```

Conceptually:

\[
I[m,n,c]
\]

with:

\[
c\in\{R,G,B\}
\]

The array shape may be represented as:

\[
H\times W\times3
\]

in one common convention.

A pixel may therefore be written conceptually as:

\[
(R,G,B)
\]

For example:

\[
(255,0,0)
\]

represents a saturated red under the conventional 8-bit RGB interpretation.

---

# 04.9 RGB as Three Matrices

Instead of thinking only in terms of one 3-D array, we can visualize RGB as three 2-D planes:

```text
RGB IMAGE

        ┌───────────────┐
        │ R CHANNEL     │
        │ H × W         │
        └───────────────┘

        ┌───────────────┐
        │ G CHANNEL     │
        │ H × W         │
        └───────────────┘

        ┌───────────────┐
        │ B CHANNEL     │
        │ H × W         │
        └───────────────┘
```

The final colour image is interpreted using all three channels together.

---

# 04.10 Worked Example — RGB Pixel

Suppose one pixel is:

\[
(R,G,B)=(30,140,220)
\]

Under an 8-bit RGB convention:

```text
R = 30
G = 140
B = 220
```

The blue component is strongest.

The displayed colour therefore appears bluish rather than neutral.

### Important

The exact visual colour depends on the colour space, transfer characteristics, display and implementation context.

A raw triplet should not be treated as a universal perceptual colour measurement independent of context.

---

# 04.11 Multispectral Images

A multispectral image contains multiple image channels corresponding to selected spectral bands.

Conceptually:

\[
H\times W\times C
\]

where \(C\) is the number of bands/channels.

For example:

```text
Band 1
Band 2
Band 3
Band 4
...
Band C
```

Each band may reveal different information about the scene.

This is useful in areas such as:

- remote sensing,
- environmental monitoring,
- agriculture,
- scientific imaging.

> **Extension:** More channels do not automatically mean “better colour.” Multispectral data may represent information outside ordinary visible RGB perception.

---

# 04.12 Grayscale vs RGB vs Multispectral

| Property | Grayscale | RGB | Multispectral |
|---|---|---|---|
| Typical channels | 1 | 3 | >3 in many systems |
| Main content | intensity | colour components | selected spectral bands |
| Common shape | \(H\times W\) | \(H\times W\times3\) | \(H\times W\times C\) |
| Typical use | structure/intensity processing | ordinary colour imaging | spectral analysis |
| Example task | edge detection | colour segmentation | land-cover analysis |

The table describes common representations, not mandatory definitions for every imaging system.

---

# 04.13 Bit Depth

Bit depth describes how many bits are used to encode a sample under a particular representation.

If:

\[
k=\text{bits/sample}
\]

then:

\[
L=2^k
\]

possible binary codes exist.

Examples:

```text
8-bit  → 256 codes
10-bit → 1024 codes
12-bit → 4096 codes
16-bit → 65536 codes
```

### Important distinction

Bit depth is not the same thing as:

- number of pixels,
- number of channels,
- file size,
- display resolution.

---

# 04.14 Worked Example — Total Raw Storage

Suppose an image is:

```text
1920 × 1080
RGB
8-bit per stored channel sample
```

Then:

\[
1920\times1080\times3
=
6{,}220{,}800
\]

channel samples.

Since 8 bits = 1 byte:

\[
6{,}220{,}800\text{ bytes}
\]

This is approximately:

\[
\frac{6{,}220{,}800}{1024^2}
\approx5.93\text{ MiB}
\]

### Interpretation

This is an estimate for the raw channel array.

It is **not** a guarantee that the corresponding JPEG/PNG/TIFF file will occupy 5.93 MiB.

---

# 04.15 File Size vs Raw Image Size

This distinction is critical.

```text
RAW IMAGE REPRESENTATION
→ dimensions × channels × bytes/sample

FILE ON DISK
→ raw data
  + metadata
  + possible compression
  + format-specific structures
```

A JPEG may be much smaller than the raw RGB array because it uses lossy compression.

A PNG can also be substantially smaller due to lossless compression and image redundancy.

The actual file size depends on image content and format settings.

---

# 04.16 Datatype

An image-processing program must also know the numeric datatype.

Common examples include:

```text
uint8
uint16
float32
float64
```

These are not interchangeable.

For example:

```text
uint8
→ often represents integer values such as 0–255

float
→ can represent fractional values
```

But the actual valid range depends on how the application defines the representation.

---

# 04.17 Why Datatype Matters

Suppose an operation produces:

\[
280
\]

If the destination representation is an 8-bit unsigned integer with the conventional 0–255 range, 280 cannot be represented directly.

A pipeline may therefore:

- clip,
- rescale,
- wrap,
- convert differently,

depending on the implementation.

> **WARNING:** Numerical behaviour after datatype conversion must never be assumed.

This is one reason the Coding Companion requires explicit range/datatype declarations.

---

# 04.18 Dynamic Range

Dynamic range describes the span between low and high representable or measurable signal levels, depending on context.

For a simple 8-bit grayscale representation:

```text
low
0
↓
127
↓
255
high
```

A wider dynamic range can allow more separation between weak and strong signals, but dynamic range and bit depth are not identical concepts.

### Important distinction

```text
Bit depth
→ number of representable codes

Dynamic range
→ span of signal levels that can be represented/measured
```

A system can have high bit depth without having arbitrarily large physical dynamic range.

---

# 04.19 Resolution — The Word That Causes Confusion

The word **resolution** is used in multiple ways.

For this MiniBook, avoid saying simply:

> “Resolution means number of pixels.”

That is incomplete.

Useful distinctions include:

### Spatial resolution

How finely spatial detail is represented or, depending on context, the system's ability to distinguish nearby spatial structures.

### Image dimensions

The number of stored pixels/samples:

\[
H\times W
\]

### Radiometric resolution

Ability to distinguish intensity/signal differences.

### Temporal resolution

How frequently measurements are acquired over time, especially for video.

The present course mainly needs spatial and intensity/bit-depth distinctions, while the broader terminology becomes useful later.

---

# 04.20 Image Dimensions vs Spatial Resolution

Two images can both have:

\[
1920\times1080
\]

yet have different effective image quality because their acquisition systems may differ in:

- optical sharpness,
- sensor quality,
- focus,
- noise,
- sampling response,
- compression,
- processing.

Therefore:

> **Stored pixel dimensions are not a complete description of spatial resolving power.**

---

# 04.21 Worked Example — Two Images, Same Dimensions

Consider:

```text
Image A
1920 × 1080
good focus
low blur

Image B
1920 × 1080
strong defocus blur
```

Both contain the same number of stored pixels.

But Image B may show substantially less useful fine detail.

This demonstrates:

```text
pixel count ≠ complete image quality
```

---

# 04.22 Tensor Representation

> **DEEP DIVE / EXTENSION**

In modern computer vision, an image is often represented as a tensor.

Examples:

### Grayscale

\[
H\times W
\]

### RGB

\[
H\times W\times3
\]

### Batch of RGB images

\[
B\times H\times W\times3
\]

where:

- \(B\) = batch size,
- \(H\) = height,
- \(W\) = width.

Some frameworks use channel-first layout:

\[
B\times3\times H\times W
\]

The numerical information may be the same, but the memory/processing layout differs.

---

# 04.23 Channel-First vs Channel-Last

These are representation conventions.

### Channel-last

\[
H\times W\times C
\]

### Channel-first

\[
C\times H\times W
\]

For a batch:

```text
channel-last:
B × H × W × C

channel-first:
B × C × H × W
```

### Engineering Insight

Shape errors are among the most common problems when moving images between libraries and machine-learning frameworks.

Always inspect the shape rather than assuming it.

---

# 04.24 Worked Example — Tensor Shape

Suppose you have:

```text
32 RGB images
224 × 224
```

Then channel-last batch shape is:

\[
32\times224\times224\times3
\]

Number of stored channel samples:

\[
32\times224\times224\times3
=
4{,}816{,}128
\]

If values are float32, each takes 4 bytes in the usual representation, so raw array storage is approximately:

\[
4{,}816{,}128\times4
=
19{,}264{,}512\text{ bytes}
\]

before additional framework overhead.

---

# 04.25 Normalized Image Values

Image-processing and machine-learning pipelines may convert integer images into floating-point representations.

For example:

```text
uint8:
0 → 255
```

may be mapped to:

\[
[0,1]
\]

using:

\[
x_{\text{norm}}=\frac{x}{255}
\]

under this specific convention.

Thus:

\[
128\rightarrow\frac{128}{255}\approx0.502
\]

### WARNING

Not every system uses \([0,1]\).

Some pipelines use:

\[
[-1,1]
\]

or standardized values.

Therefore normalization must always be declared.

---

# 04.26 Image Coordinate System vs Display Coordinate System

Mathematical diagrams, programming libraries and graphics systems do not always use identical conventions.

You may encounter:

```text
row increases downward
column increases to the right
```

in array/image processing.

But a conventional Cartesian plot often uses:

```text
x increases right
y increases upward
```

This can cause apparent vertical inversions when an image is plotted.

> **Engineering Insight:** Always state the coordinate convention when a derivation or geometric transformation depends on it.

---

# 04.27 Pixel Value Is Not Always “Brightness”

A stored pixel value represents the quantity defined by its encoding.

For example:

```text
RGB value
→ colour-channel code

thermal image value
→ may represent calibrated temperature-related data

multispectral band value
→ may represent a sensor measurement in a spectral band
```

Therefore the word **intensity** should be used carefully.

For a grayscale image it is often a useful description.

For scientific images, the stored values may have a more specific physical meaning.

---

# 04.28 Resolution, Bit Depth and Channels — Separate Them

| Property | Controls |
|---|---|
| Width / height | spatial sample count |
| Channel count | number of stored components/bands |
| Bit depth | number of codes per stored sample |
| Datatype | computational/storage representation |
| Dynamic range | signal span |
| Colour model | how colour information is parameterized |
| Compression | how storage redundancy is reduced |

These properties interact but are not interchangeable.

---

# 04.29 A Complete Image Description

Instead of saying:

> “This is a high-resolution image.”

provide a structured description:

```text
Dimensions:
1920 × 1080

Channels:
3

Representation:
RGB

Datatype:
uint8

Per-channel code levels:
256

Raw channel samples:
6,220,800

Approximate raw storage:
5.93 MiB

File format:
JPEG

Compression:
lossy
```

This is much more useful for engineering work.

---

# 04.30 Image Representation Pipeline

```text
PHYSICAL MEASUREMENT
        ↓
SPATIAL SAMPLES
        ↓
NUMERIC VALUES
        ↓
CHANNEL ORGANIZATION
        ↓
COLOUR / SIGNAL REPRESENTATION
        ↓
DATATYPE + RANGE
        ↓
FILE FORMAT
        ↓
OPTIONAL COMPRESSION
```

Each stage answers a different question.

---

# 04.31 Example — One Scene, Many Representations

A single photograph can exist as:

```text
RAW / SENSOR-RELATED DATA
        ↓
linear camera representation
        ↓
RGB image
        ↓
grayscale copy
        ↓
HSV representation
        ↓
normalized floating tensor
        ↓
JPEG file
```

These are not necessarily different scenes.

They are different representations of related image information.

---

# 04.32 Why Representation Choice Matters

Suppose you want to isolate objects based on colour.

### RGB

You can inspect three channels directly.

### HSV

Hue and saturation may provide a more convenient representation for some colour-based segmentation tasks.

Suppose you want edge detection.

### Grayscale

A single intensity-related channel may simplify the computation.

Suppose you want to feed an image into a CNN.

### Tensor

A shape such as:

\[
B\times H\times W\times C
\]

may be required.

The representation should therefore follow the task.

---

# 04.33 Common Traps

## Trap 1 — “A pixel is always one number.”

False.

That is common for grayscale images, but colour and multispectral images can associate multiple channel values with one spatial location.

## Trap 2 — “RGB is one matrix.”

Simplification.

It can be represented as one 3-D array or as three 2-D channel matrices, depending on the notation/layout.

## Trap 3 — “Higher resolution means more bit depth.”

False.

Spatial dimensions and intensity precision are distinct.

## Trap 4 — “1920×1080 tells me everything about image quality.”

False.

Optics, blur, noise, acquisition quality, compression and other factors matter.

## Trap 5 — “8-bit RGB means the file is 24 bits.”

Not necessarily.

An uncompressed 8-bit-per-channel RGB array contains 24 bits per pixel of raw channel data, but the final file may be compressed or stored in another format.

## Trap 6 — “All software uses RGB H×W×3.”

False.

Channel order, memory layout and batching conventions vary.

## Trap 7 — “Pixel value always means physical brightness.”

False.

Its meaning depends on the image modality and encoding.

---

# 04.34 Engineering Decision Example — Choosing a Representation

Imagine a segmentation task for a brightly coloured object against a differently coloured background.

Possible workflow:

```text
RGB image
→ inspect channels
→ transform to a suitable colour representation
→ threshold/segment
→ morphological cleanup
```

The choice of colour space should be justified by the separation it provides for the specific image/task.

There is no universal rule that one colour space is always best.

---

# 04.35 Cross-Book Bridges

> **MATH BRIDGE — M04–M08**  
> Vectors, matrices, tensor shapes and basic linear operations.

> **LAB BRIDGE — LAB-U1-01**  
> Load images and inspect shape, channel count, datatype and range.

> **CODE BRIDGE — CODE-00**  
> Pay special attention to RGB/BGR conventions, normalization and shape ordering.

> **PRACTICE BRIDGE**  
> Given an image description, calculate sample count, channel samples and raw storage.

> **EXAM BRIDGE**  
> Prepare definitions and comparisons for pixel, grayscale, RGB, multispectral image, bit depth, resolution, datatype and dynamic range.

---

# 04.36 Quick Recall

### Grayscale

\[
H\times W
\]

### RGB

\[
H\times W\times3
\]

### Multispectral

\[
H\times W\times C
\]

### Batch of RGB images — one common layout

\[
B\times H\times W\times3
\]

### Levels from \(k\) bits

\[
L=2^k
\]

### Raw storage estimate

\[
\text{bytes}
=
HWC\times
\frac{\text{bits/sample}}{8}
\]

for a simple uncompressed channel array.

---

# 04.37 Chapter Checkpoint

1. What is a pixel?
2. How is a grayscale image represented mathematically?
3. How can RGB be represented as three matrices?
4. What is a multispectral image?
5. How does bit depth relate to the number of levels?
6. What is the difference between dimensions and resolution?
7. What is the difference between bit depth and dynamic range?
8. Why does datatype matter?
9. What is the difference between channel-first and channel-last?
10. Calculate the raw storage of a 1024×1024 RGB image with 8-bit channels.
11. Why can two images with identical dimensions have different useful detail?
12. Why must colour-space and normalization conventions be declared?

---

# 04.38 Calculation Check — Raw Storage Example

For:

```text
1024 × 1024
RGB
8-bit/channel
```

spatial samples:

\[
1024\times1024=1{,}048{,}576
\]

channel samples:

\[
1{,}048{,}576\times3=3{,}145{,}728
\]

bytes:

\[
3{,}145{,}728
\]

Approximate MiB:

\[
\frac{3{,}145{,}728}{1024^2}=3.00\text{ MiB}
\]

So a raw 8-bit RGB array of this size requires approximately:

\[
\boxed{3.00\text{ MiB}}
\]

excluding extra metadata or program overhead.

---

# 04.39 Connection Forward

We now know what an image **is as data**:

```text
pixels
+
dimensions
+
channels
+
bit depth
+
datatype
+
range
+
representation
```

The next question is:

> **How do we represent and manipulate colour in a principled way, and how do image file formats preserve or compress that information?**

That leads to Chapter 05:

```text
RGB
→ HSV
→ CMY
→ YUV
→ BMP / PNG / JPEG / TIFF
```
