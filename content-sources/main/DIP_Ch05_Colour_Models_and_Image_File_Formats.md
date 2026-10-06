---
id: "C05"
title: "Colour Models and Image File Formats"
layer: "MAIN"
part: "I — The Image"
unit: "I"
version: "1.0"
status: "REFERENCE BUILD"
syllabus_scope:
  - "RGB"
  - "HSV"
  - "CMY"
  - "YUV"
  - "BMP"
  - "JPEG"
  - "PNG"
  - "TIFF"
tags:
  - "CORE"
  - "EXAM"
  - "COLOUR"
  - "FORMATS"
  - "LAB"
  - "DEEP DIVE"
prerequisites:
  - "C03"
  - "C04"
related:
  - "C06"
  - "C07"
  - "C15"
  - "C16"
  - "C21"
  - "C23"
  - "C24"
  - "C26"
math:
  - "M05"
  - "M06"
  - "M08"
lab:
  - "LAB-U1-01"
  - "LAB-U1-07"
exam:
  - "EXAM-U1"
practice:
  - "P-C05"
assets:
  - "D-C05-01"
  - "D-C05-02"
  - "D-C05-03"
---

# Chapter 05 — Colour Models and Image File Formats

> **Chapter thesis**  
> Colour is not a single number. A colour image is a structured representation of measurements, and the best representation depends on the task. File formats then determine how those numerical data are organized, stored, compressed and exchanged.

**Part I — The Image**  
**Syllabus anchor:** Unit I explicitly includes RGB, HSV, CMY and YUV colour models, together with BMP, JPEG, PNG and TIFF image formats. fileciteturn4file0L32-L35

---

# 05.0 Why This Chapter Matters

By now we can describe an image as:

```text
spatial samples
+
channel values
+
bit depth
+
datatype
```

But a colour image adds another question:

> How should the channels be interpreted?

The same visual scene can be represented as:

```text
RGB
HSV
CMY
YUV
```

These are not merely different names for the same three numbers.

They organize colour information differently.

A second engineering question is:

> How do we store that representation in a file?

That leads to:

```text
BMP
JPEG
PNG
TIFF
```

Understanding the difference between **colour representation** and **file format** prevents many common mistakes.

---

# 05.1 Colour Is a Representation Problem

A digital colour image usually associates multiple channel values with one spatial location.

Conceptually:

\[
I(x,y)=(c_1,c_2,\ldots,c_K)
\]

For ordinary RGB imagery:

\[
I(x,y)=(R,G,B)
\]

The three values together define a colour under the specified colour-space conventions.

This immediately gives an important rule:

> Never interpret a colour triplet without knowing what the channels mean.

For example, the triplet:

\[
(255,0,0)
\]

means saturated red under a conventional 8-bit RGB interpretation.

But a three-number vector in another colour model can mean something entirely different.

---

# 05.2 Additive vs Subtractive Colour

Two major ideas help organize the colour models in this chapter.

### Additive colour

Light components are combined.

```text
RED + GREEN + BLUE
        ↓
      WHITE
```

This is associated with displays and emitted light.

### Subtractive colour

Components conceptually remove portions of reflected/transmitted light.

```text
CYAN + MAGENTA + YELLOW
             ↓
     reduced reflected light
```

This is associated with printing processes.

This distinction explains why RGB and CMY use different conceptual structures.

---

# 05.3 RGB — The Familiar Digital Colour Model

RGB stands for:

```text
R = Red
G = Green
B = Blue
```

A pixel is represented as:

\[
(R,G,B)
\]

Under a common 8-bit-per-channel representation:

\[
0\le R,G,B\le255
\]

Examples:

| RGB triplet | Conceptual result |
|---|---|
| (0,0,0) | black |
| (255,255,255) | white |
| (255,0,0) | red |
| (0,255,0) | green |
| (0,0,255) | blue |
| (255,255,0) | yellow |
| (0,255,255) | cyan |
| (255,0,255) | magenta |

These examples assume the conventional normalized/8-bit interpretation.

---

# 05.4 RGB as a Cube

A useful mental model is an RGB cube.

```text
                 B
                 ↑
                 │
                 ●────────────●
                /│           /│
               / │          / │
              ●────────────●  │
              │  │         │  │
              │  ●─────────│──●
              │ /          │ /
              │/           │/
              ●────────────●────→ R
             /
            G
```

Each colour is a point in a 3-D coordinate space:

\[
(R,G,B)
\]

This geometric interpretation is useful for understanding:

- colour distance,
- colour clustering,
- segmentation,
- channel manipulation.

---

# 05.5 Worked Example — RGB Combination

Take:

\[
R=200,\quad G=120,\quad B=40
\]

Then the pixel is:

\[
(200,120,40)
\]

Relative comparison:

```text
R = strong
G = moderate
B = low
```

So the pixel is warm and reddish/yellowish in ordinary RGB visualization.

The exact perceptual appearance depends on the display and colour-management pipeline.

---

# 05.6 RGB Strengths and Limitations

### Strengths

- natural representation for many cameras/displays,
- straightforward channel-wise storage,
- directly supported by common image libraries,
- convenient for many machine-learning pipelines.

### Limitations

RGB is not always the most convenient space for a particular task.

For example:

- similar colours can differ in several channels,
- brightness and chromatic information are mixed,
- simple channel thresholds may not correspond to perceptual similarity.

This motivates alternative colour models.

---

# 05.7 HSV — Hue, Saturation, Value

HSV represents colour using:

```text
H = Hue
S = Saturation
V = Value
```

It is often useful because it separates a colour-like attribute from two magnitude-related attributes more explicitly than raw RGB coordinates do.

### Hue

Describes the dominant colour family.

Conceptually:

```text
red → yellow → green → cyan → blue → magenta → red
```

### Saturation

Describes how strongly coloured the value is relative to a neutral/gray axis in the model.

### Value

Represents the model's brightness-like magnitude coordinate.

> **WARNING:** “Value” in HSV is not identical to physical luminance, radiometric intensity, or perceptual brightness.

---

# 05.8 Why HSV Is Popular in Segmentation

Consider detecting a coloured object.

In RGB:

```text
object colour
→ may vary strongly in R, G and B
```

In HSV:

```text
object colour
→ often easier to describe with a hue interval
```

Conceptual pipeline:

```text
RGB image
    ↓
HSV conversion
    ↓
select Hue/Saturation range
    ↓
binary mask
    ↓
morphological cleanup
```

This can be useful for controlled colour-based segmentation.

---

# 05.9 HSV Circularity of Hue

Hue has a special property.

Red lies near both ends of the hue cycle:

```text
          RED
      /         \
 MAGENTA         YELLOW
   |               |
 BLUE             GREEN
      \         /
          CYAN
```

Therefore a condition such as:

```text
H > 350°
or
H < 10°
```

may represent one contiguous red interval.

This is different from a normal linear numerical variable.

> **Engineering trap:** Treating hue as an ordinary straight-line scalar can create incorrect threshold logic around the wrap-around boundary.

---

# 05.10 RGB to HSV — Conceptual Route

For normalized RGB:

\[
r,g,b\in[0,1]
\]

define:

\[
C_{\max}=\max(r,g,b)
\]

\[
C_{\min}=\min(r,g,b)
\]

\[
\Delta=C_{\max}-C_{\min}
\]

Then the HSV values are derived according to which channel is maximal.

For example, when \(C_{\max}=r\):

\[
H'=60^\circ
\left(
\frac{g-b}{\Delta}
\right)
\]

with appropriate wrap-around adjustment.

Then:

\[
S=
\begin{cases}
0,&C_{\max}=0\\[4pt]
\frac{\Delta}{C_{\max}},&C_{\max}\ne0
\end{cases}
\]

and:

\[
V=C_{\max}
\]

> **EXAM NOTE:** The exact hue formula has separate cases for max-\(R\), max-\(G\), max-\(B\). Do not memorize only one branch as the complete conversion.

---

# 05.11 Worked HSV Example

Take normalized RGB:

\[
(r,g,b)=(1,0,0)
\]

Then:

\[
C_{\max}=1
\]

\[
C_{\min}=0
\]

\[
\Delta=1
\]

Since \(R\) is maximum:

\[
H'= \frac{0-0}{1}=0
\]

so:

\[
H=0^\circ
\]

and:

\[
S=\frac{1}{1}=1
\]

\[
V=1
\]

Therefore:

\[
(R,G,B)=(1,0,0)
\rightarrow
(H,S,V)=(0^\circ,1,1)
\]

---

# 05.12 CMY — A Subtractive Model

CMY stands for:

```text
C = Cyan
M = Magenta
Y = Yellow
```

For normalized components under the basic complement relationship:

\[
C=1-R
\]

\[
M=1-G
\]

\[
Y=1-B
\]

This describes the conceptual inverse relation between normalized RGB and CMY.

---

# 05.13 Worked RGB → CMY

Take:

\[
(R,G,B)=(1,0.4,0.2)
\]

Then:

\[
C=1-1=0
\]

\[
M=1-0.4=0.6
\]

\[
Y=1-0.2=0.8
\]

Therefore:

\[
(C,M,Y)=(0,0.6,0.8)
\]

This is useful for understanding the relationship between additive RGB and subtractive CMY.

---

# 05.14 Why CMYK Exists

Printing commonly introduces a fourth component:

```text
C
M
Y
K = Black
```

The syllabus names CMY rather than CMYK, so CMYK is treated here as an extension.

Why add black?

Conceptually, a separate black ink can:

- improve deep dark tones,
- reduce the need to combine large amounts of coloured inks,
- improve practical printing control.

Real printer colour management is more complex than simply applying the idealized complement equations.

---

# 05.15 YUV — Separating Luma-Related and Chrominance Information

YUV is commonly discussed in the context of separating brightness-related information from colour-difference components.

Conceptually:

```text
Y
→ luma-related component

U, V
→ chrominance / colour-difference components
```

This structure is particularly useful when designing systems in which human visual sensitivity to spatial detail differs between brightness-related and colour information.

> **Terminology note:** In digital video, related systems such as YCbCr are extremely common. Do not automatically treat “YUV” and every YCbCr encoding as mathematically identical.

---

# 05.16 Why Separate Brightness and Colour?

A simplified conceptual idea is:

```text
fine spatial detail
→ important in brightness/luma

colour detail
→ can sometimes be represented at lower spatial resolution
```

This helps explain chroma subsampling.

---

# 05.17 Chroma Subsampling

> **EXTENSION**

Some image/video systems store colour-difference information at lower spatial resolution than luma.

Common notation includes:

```text
4:4:4
4:2:2
4:2:0
```

The exact sampling structure depends on the standard and should be learned from the relevant specification.

Conceptually:

```text
4:4:4
→ full chroma sampling

4:2:2
→ reduced horizontal chroma sampling

4:2:0
→ reduced chroma sampling in both dimensions
```

This can reduce data volume with relatively modest perceptual impact in many viewing conditions.

---

# 05.18 Colour Model Comparison

| Model | Main idea | Typical usefulness |
|---|---|---|
| RGB | additive channel representation | cameras, displays, general image data |
| HSV | hue/saturation/value coordinates | colour selection and some segmentation workflows |
| CMY | subtractive colour components | printing concepts |
| YUV | luma/chroma-oriented representation | video/compression-related systems |

No model is universally “best.”

The appropriate representation depends on:

- sensor,
- display,
- task,
- computation,
- storage,
- communication system.

---

# 05.19 Colour Conversion Is a Transformation

A common pipeline is:

```text
camera/image file
      ↓
RGB
      ↓
HSV
      ↓
segmentation
```

Or:

```text
RGB
 ↓
grayscale
 ↓
edge detection
```

Or:

```text
RGB / source colour representation
      ↓
luma/chroma representation
      ↓
compression/storage
```

Each conversion changes the numerical representation.

It can also introduce:

- rounding,
- range changes,
- clipping,
- precision loss,
- convention mismatches.

---

# 05.20 Common Colour-Processing Errors

### Error 1 — RGB vs BGR confusion

Some software APIs use channel order such as:

```text
B, G, R
```

even though the image is conventionally described as RGB.

Always inspect the API documentation and test with a known colour.

### Error 2 — HSV range confusion

Different libraries may use different numeric ranges for \(H,S,V\).

Never assume a hue range from one library applies unchanged to another.

### Error 3 — Limited vs full ranges

Video-oriented encodings can use conventions that differ from a simple full-range 0–255 representation.

### Error 4 — “HSV is perceptually uniform”

It is not.

HSV is convenient, not a universal model of human colour perception.

---

# 05.21 What Is an Image File Format?

A file format defines how image data are structured and stored.

It may specify:

```text
metadata
+
pixel/channel data
+
colour interpretation
+
compression
+
file organization
```

Therefore:

> A colour model and a file format are different concepts.

For example:

```text
RGB
```

is a colour representation.

```text
JPEG
```

is a file format.

A JPEG file can contain colour information represented using structures designed around its compression pipeline.

---

# 05.22 BMP

BMP is a bitmap-oriented image format historically associated with relatively direct pixel storage.

Conceptually:

```text
BMP file
├── file information
├── image information
├── pixel storage
└── optional additional structures
```

BMP can be useful for teaching because the relationship between stored pixels and image data can be relatively straightforward for simple cases.

### Strength

Simple conceptual relationship to bitmap storage.

### Limitation

For many practical workflows, it is less storage-efficient than compressed formats.

---

# 05.23 PNG

PNG is designed for **lossless** image compression.

That means, after decoding:

\[
\text{decoded image data}
=
\text{original encoded image data}
\]

for the data covered by the compression process.

PNG is especially useful when exact pixel preservation matters, such as:

- diagrams,
- screenshots,
- graphics,
- images with sharp edges,
- transparency-supporting workflows.

---

# 05.24 JPEG

JPEG is commonly used for photographic images and typically uses **lossy** compression.

Conceptually:

```text
RGB/source image
      ↓
colour transformation
      ↓
block-based transform
      ↓
quantization
      ↓
entropy coding
      ↓
JPEG bitstream
```

The detailed JPEG pipeline is covered in depth later in C24.

### Key property

Lossy compression can reduce file size substantially, but decoding does not necessarily reproduce the original pixel values exactly.

---

# 05.25 Why JPEG Works Well for Photos

Natural photographs contain substantial spatial correlation.

Neighbouring pixels often have related values.

JPEG exploits image structure to represent information more compactly.

Its transform and quantization stages allow the encoder to remove information judged less important for the desired compression level.

At higher compression, visible artifacts can appear.

---

# 05.26 JPEG Artifacts

At aggressive compression settings, common artifacts can include:

- block boundaries,
- ringing-like effects,
- loss of fine texture,
- colour/detail degradation.

Conceptually:

```text
original
→ fine detail

high compression
→ simplified local structure
→ possible blocking / ringing / blur
```

These artifacts matter in:

- medical imaging,
- scientific analysis,
- machine vision,
- document processing,

where exact or subtle pixel information may be important.

---

# 05.27 TIFF

TIFF is a flexible image-file format widely used in professional, archival and scientific workflows.

A TIFF file can support different forms of image data and may be configured in ways that preserve high precision or use compression.

This makes TIFF less about one fixed visual appearance and more about a flexible container for image information.

> **Important:** “TIFF = lossless” is too simplistic. TIFF can support different compression choices and image configurations.

---

# 05.28 Format Comparison

| Format | Typical compression | Typical strength | Typical caution |
|---|---|---|---|
| BMP | often little/no compression in simple cases | straightforward bitmap storage | large files |
| PNG | lossless | exact pixel recovery, graphics, transparency | usually less effective than JPEG for photos |
| JPEG | lossy | efficient photographic compression | irreversible detail loss |
| TIFF | flexible; can be uncompressed or compressed | high-quality/professional/scientific workflows | larger/more complex files depending on configuration |

---

# 05.29 Lossless vs Lossy

This distinction becomes fundamental in C21–C24.

### Lossless

```text
encode
 ↓
decode
 ↓
original represented data recovered
```

### Lossy

```text
encode
 ↓
information deliberately discarded
 ↓
decode
 ↓
approximation of original
```

Use lossless approaches when exact data recovery matters.

Use lossy approaches when storage/communication efficiency is more important and some information loss is acceptable.

---

# 05.30 Worked Format Decision

Suppose you have:

### Case A — Laboratory graph/screenshot

Need:

```text
sharp edges
exact text
small file
```

PNG may be a suitable choice.

### Case B — Natural photograph for web delivery

Need:

```text
small file
acceptable visual quality
```

JPEG is often suitable.

### Case C — Scientific image requiring flexible high-precision storage

Need:

```text
metadata
high bit depth
controlled processing
```

A suitable TIFF configuration may be preferable.

> These are engineering examples, not universal rules.

---

# 05.31 File Extension Is Not Enough

A filename ending in:

```text
.jpg
```

does not by itself tell you all of the numerical properties of the decoded image.

You should inspect:

```text
dimensions
channels
datatype
colour interpretation
compression
metadata
```

Likewise, changing a filename extension does not convert an image format.

---

# 05.32 File Format vs Codec vs Container

These terms can overlap in casual discussion but are not identical.

A practical mental model is:

```text
FORMAT
→ defines file organization and rules

ENCODING / CODEC
→ defines how data are compressed/represented

CONTAINER
→ packages one or more streams and metadata
```

The exact relationship depends on the ecosystem.

For the university syllabus, the main distinction to retain is:

```text
colour model
≠
file format
```

---

# 05.33 A Complete Colour-Image Pipeline

```text
SCENE
  ↓
IMAGE ACQUISITION
  ↓
RAW / SENSOR-RELATED DATA
  ↓
COLOUR REPRESENTATION
  ↓
RGB
  ↓
OPTIONAL CONVERSION
  ├── HSV → segmentation
  ├── grayscale → intensity processing
  └── luma/chroma → coding/compression workflow
  ↓
FILE ENCODING
  ├── PNG
  ├── JPEG
  ├── TIFF
  └── BMP
  ↓
STORAGE / TRANSMISSION
  ↓
DECODING
  ↓
PROCESSING / DISPLAY
```

The same scene can therefore pass through several representations before a final output is obtained.

---

# 05.34 Engineering Scenario — Coloured Object Detection

Suppose the goal is to detect a red object.

A simple pipeline might be:

```text
image
 ↓
RGB
 ↓
HSV
 ↓
red hue mask
 ↓
morphological cleanup
 ↓
connected components / contour analysis
 ↓
object location
```

Potential failures:

- illumination changes,
- shadows,
- reflections,
- background colours,
- hue wrap-around,
- sensor noise.

This illustrates a major DIP principle:

> A representation can make a problem easier without making it solved.

---

# 05.35 Engineering Scenario — Why JPEG Can Be Dangerous

Suppose a model is trained on heavily compressed images.

Compression artifacts may become a shortcut signal.

For example:

```text
class A
→ consistently JPEG-compressed differently

class B
→ different JPEG processing
```

A model could partially learn the compression signature rather than the intended visual feature.

This is a machine-learning extension of a classical image-processing issue.

---

# 05.36 Common Traps

## Trap 1 — “RGB is a file format.”

False.

RGB is a colour representation.

## Trap 2 — “JPEG always means RGB.”

Not necessarily.

File encodings can transform or store colour information in different internal representations.

## Trap 3 — “PNG has no compression.”

False.

PNG uses lossless compression.

## Trap 4 — “TIFF is always lossless.”

False.

TIFF can support different compression approaches/configurations.

## Trap 5 — “HSV is better than RGB.”

Not universally.

It may be more convenient for some tasks.

## Trap 6 — “YUV and YCbCr are identical in every context.”

Unsafe assumption.

They are related, but exact conventions and equations can differ.

---

# 05.37 Exam-Ready Comparison

| Question | Core answer |
|---|---|
| RGB? | additive three-channel colour representation |
| HSV? | hue/saturation/value representation |
| CMY? | subtractive cyan/magenta/yellow representation |
| YUV? | luma/chroma-oriented representation |
| BMP? | bitmap-oriented image file format |
| PNG? | lossless compressed image format |
| JPEG? | usually lossy photographic compression format |
| TIFF? | flexible image file format supporting multiple configurations |

---

# 05.38 Cross-Book Bridges

> **MATH BRIDGE**  
> Review vector representation and transformation equations for colour conversion.

> **LAB BRIDGE — LAB-U1-01 / LAB-U1-07**  
> Load an image, inspect channel order, convert RGB↔HSV and compare format behaviour.

> **PRACTICE BRIDGE**  
> Choose an appropriate colour representation or file format for a stated engineering task.

> **EXAM BRIDGE**  
> Prepare definitions, comparisons, RGB/CMY equations, conceptual HSV conversion, and format distinctions.

> **COMPRESSION BRIDGE**  
> JPEG concepts introduced here are developed mathematically in C21–C24.

---

# 05.39 Quick Recall

```text
RGB
→ additive
→ display/camera-friendly

HSV
→ hue + saturation + value
→ often useful for colour selection

CMY
→ subtractive
→ printing concept

YUV
→ luma/chroma-oriented

PNG
→ lossless

JPEG
→ usually lossy

BMP
→ bitmap-oriented

TIFF
→ flexible image format
```

---

# 05.40 Chapter Checkpoint

1. What is a colour model?
2. Why is RGB called additive?
3. What are the three RGB components?
4. What are hue, saturation and value?
5. Why can HSV be useful for colour segmentation?
6. Write the normalized RGB→CMY complement equations.
7. What is the role of Y in a YUV-type representation?
8. Distinguish a colour model from a file format.
9. Compare BMP, PNG, JPEG and TIFF.
10. What is the difference between lossless and lossy compression?
11. Why should file format properties be inspected rather than inferred from a filename?
12. Give one example where HSV may be preferable to direct RGB thresholding.

---

# 05.41 Part I Completion Map

At the end of Part I, the representation chain is now:

```text
C01
BIG PICTURE
     ↓
C02
IMAGE FORMATION
     ↓
C03
SAMPLING + QUANTIZATION
     ↓
C04
PIXELS + MATRICES + TENSORS + RESOLUTION
     ↓
C05
COLOUR MODELS + FILE FORMATS
```

The result is a complete foundation for the next part:

```text
THE IMAGE
→
HOW TO IMPROVE THE IMAGE
```

That begins with point processing and intensity transformations in Chapter 06.
