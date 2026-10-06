---
id: "MAIN-00"
title: "Digital Image Processing — Master Table of Contents & Learning Map"
layer: "MAIN"
system: "Engineering Minibooks · Digital Image Processing"
version: "1.0"
status: "ARCHITECTURE LOCK"
---

# MAIN-00 — Digital Image Processing Master Table of Contents & Learning Map

> **Role:** The navigation and learning map for the canonical DIP Main Book.

The Main Book is the primary teaching hub. It contains the canonical conceptual explanation of the subject. Mathematics, practical work, code, exams, practice and resources connect to it rather than replacing it.

---

# 1. The DIP Journey

The Main Book follows the natural transformation of an image:

```text
REAL WORLD
    ↓
IMAGE FORMATION
    ↓
SAMPLING
    ↓
QUANTIZATION
    ↓
DIGITAL REPRESENTATION
    ↓
ENHANCEMENT
    ↓
RESTORATION
    ↓
TRANSFORMATION
    ↓
SEGMENTATION
    ↓
FEATURES
    ↓
COMPRESSION
    ↓
CLASSIFICATION
    ↓
DETECTION
    ↓
VIDEO / MOTION
```

The flow is conceptual rather than a claim that every practical system must execute every stage.

---

# 2. Part Map

| Part | Theme | Chapters |
|---|---|---|
| I | The Image | C01–C05 |
| II | Improving the Image | C06–C14 |
| III | Understanding Image Content | C15–C20 |
| IV | Compressing Images | C21–C24 |
| V | From DIP to Intelligent Vision | C25–C31 |

---

# 3. Part I — The Image

## C01 — Digital Image Processing: The Big Picture

### Purpose

Establish what DIP is, why images need computational processing, and how an end-to-end DIP system is organized.

### Major concepts

- Definition and scope of DIP
- Digital image vs physical image
- Image processing vs image analysis vs computer vision
- Major application areas
- Generic image-processing pipeline
- Human visual perception as context
- Input–process–output thinking
- Course roadmap

### Core visual assets

```text
physical scene → acquisition → digital image → processing → result
master DIP pipeline
DIP vs image analysis vs computer vision relationship
application map
```

### Core mathematical ideas

- \(f(x,y)\) as image representation
- digital image as sampled/quantized data

---

## C02 — Image Formation and Acquisition

### Purpose

Explain how a real-world scene becomes measurable image data.

### Major concepts

- Scene
- Illumination
- Reflectance
- Imaging system
- Sensor
- Sampling plane
- Acquisition chain
- Digital sensor output

### Core visual assets

```text
scene → optics → sensor → electrical signal → digitization → image
```

### Deep Dive

- radiometric intuition
- sensor limitations
- acquisition noise
- geometric considerations

---

## C03 — Sampling and Quantization

### Purpose

Explain the two fundamental discretization processes.

### Major concepts

- Continuous image
- spatial sampling
- discrete coordinates
- sampling density
- aliasing intuition
- intensity quantization
- quantization levels
- bit depth
- quantization error

### Core formulas

\[
L=2^k
\]

where \(k\) is bits per intensity sample.

### Core visual assets

```text
continuous → sampled grid
continuous intensity → quantized levels
undersampling / aliasing illustration
bit-depth comparison
```

---

## C04 — Image Representation: Pixels, Matrices, Tensors and Resolution

### Major concepts

- Pixel
- coordinate conventions
- grayscale matrix
- RGB channel structure
- image dimensions
- bit depth
- datatype
- dynamic range
- spatial resolution
- radiometric resolution
- memory requirements
- tensor representation

### Core representations

```text
grayscale:
H × W

RGB:
H × W × 3

multispectral:
H × W × C
```

### Deep Dive

- channel-first vs channel-last representations
- datatype/range interactions
- storage vs display representation

---

## C05 — Colour Models and Image File Formats

### Colour

- RGB
- HSV
- CMY
- YUV
- purpose of colour spaces
- conversion intuition
- channel interpretation

### File formats

- BMP
- PNG
- JPEG
- TIFF
- lossless/lossy distinction
- metadata
- compression relationships

### Core visual assets

```text
RGB decomposition
HSV components
colour-space comparison
format/compression comparison
```

---

# 4. Part II — Improving the Image

## C06 — Point Processing and Intensity Transformations

### Major concepts

- point operation
- intensity mapping
- negative transformation
- thresholding as a point transformation
- contrast stretching
- logarithmic transformation
- power-law/gamma transformation
- clipping and dynamic range

### Core formulation

\[
s=T(r)
\]

Interpretation:

> Output intensity is determined from the corresponding input intensity.

---

## C07 — Histograms and Contrast Enhancement

### Major concepts

- histogram
- normalized histogram
- cumulative distribution function
- contrast
- dynamic range
- histogram stretching
- histogram equalization
- histogram specification / matching
- limitations

### Core formulas

\[
p(r_k)=\frac{n_k}{MN}
\]

and the appropriate cumulative transformation.

### Required worked examples

- small histogram
- probability table
- CDF
- mapping
- transformed intensities
- before/after histogram interpretation

---

## C08 — Spatial Filtering and Convolution

### Major concepts

- neighbourhood
- kernel/filter mask
- correlation
- convolution
- local operator
- linear filtering
- border handling
- kernel normalization

### Core mathematical example

Show actual matrix multiplication/summation on a small neighbourhood.

### Core visual assets

```text
kernel sliding across image
active neighbourhood
input → kernel → output
```

---

## C09 — Smoothing and Noise Reduction

### Major concepts

- mean filtering
- weighted averaging
- Gaussian filtering
- median filtering
- smoothing vs detail
- impulse noise
- trade-offs

### Comparison

```text
Mean
Gaussian
Median
```

with:

- operation
- strength
- noise suitability
- edge effect
- computational characteristics

---

## C10 — Sharpening and Edge Detection

### Major concepts

- intensity transition
- first derivative
- gradient
- second derivative
- Laplacian
- Sobel
- Prewitt
- Canny
- gradient magnitude
- edge orientation

### Core formulas

\[
\nabla f=
\begin{bmatrix}
\partial f/\partial x\\
\partial f/\partial y
\end{bmatrix}
\]

\[
|\nabla f|=\sqrt{G_x^2+G_y^2}
\]

### Worked matrix examples

- Sobel response
- gradient magnitude
- edge interpretation

---

## C11 — Geometric Transformations and Interpolation

### Major concepts

- translation
- scaling
- rotation
- affine intuition
- coordinate mapping
- nearest-neighbour interpolation
- bilinear interpolation
- trade-offs

### Core visual assets

```text
original grid
→ transformed coordinate grid
→ interpolation
→ output
```

---

## C12 — Fourier Transform and the Frequency Domain

### Major concepts

- spatial variation
- frequency
- low/high spatial frequencies
- Fourier representation
- complex values
- magnitude spectrum
- phase
- DFT
- 2-D image transform
- FFT as efficient computation of DFT

### Core conceptual pipeline

```text
spatial image
→ Fourier transform
→ frequency representation
→ manipulate
→ inverse transform
→ image
```

---

## C13 — Frequency-Domain Filtering

### Major concepts

- frequency masks
- low-pass filter
- high-pass filter
- band-pass filter
- band-stop intuition
- ideal filters
- smoother filters
- ringing/artifacts
- frequency vs spatial trade-offs

### Core visual assets

```text
spectrum
→ filter mask
→ filtered spectrum
→ spatial result
```

---

## C14 — Image Restoration and Deblurring

### Major concepts

- degradation model
- blur
- noise
- inverse problem
- restoration vs enhancement
- denoising
- deblurring
- restoration limitations

### Core model

\[
g(x,y)=h(x,y)*f(x,y)+\eta(x,y)
\]

where:

- \(f\) = original image
- \(h\) = degradation function
- \(g\) = observed image
- \(\eta\) = noise

---

# 5. Part III — Understanding Image Content

## C15 — Image Segmentation Fundamentals

### Major concepts

- purpose of segmentation
- foreground/background
- regions
- boundaries
- semantic motivation
- segmentation as a bridge to analysis

### Pipeline

```text
image
→ preprocessing
→ segmentation
→ regions/mask
→ measurement/feature extraction
```

---

## C16 — Thresholding

### Major concepts

- global threshold
- binary segmentation
- threshold selection
- adaptive thresholding
- local neighbourhood
- uneven illumination
- failure modes

### Core expression

\[
g(x,y)=
\begin{cases}
1 & f(x,y)\ge T\\
0 & f(x,y)<T
\end{cases}
\]

### Worked examples

- simple numeric threshold
- global vs adaptive visual example

---

## C17 — Region-Based Segmentation

### Major concepts

- region homogeneity
- region growing
- seed selection
- region merging/splitting concepts
- connectivity

### Visual assets

```text
seed
→ neighbourhood test
→ region growth
→ final region
```

---

## C18 — Mathematical Morphology

### Major concepts

- binary image as set
- structuring element
- erosion
- dilation
- opening
- closing
- shape effects

### Core visual method

Use binary matrices and explicit structuring elements.

### Required comparison

```text
Erosion
Dilation
Opening
Closing
```

---

## C19 — Image Features and Descriptors

### Major concepts

- feature definition
- local vs global features
- intensity
- edge
- corner
- texture
- shape
- descriptor
- invariance intuition

### Pipeline

```text
image
→ feature detection
→ descriptor construction
→ feature vector
→ matching/classification
```

---

## C20 — SIFT, SURF, ORB and HOG

### Major concepts

- SIFT
- SURF
- ORB
- HOG
- detector vs descriptor distinction
- local features
- gradient-based description
- scale/rotation robustness concepts
- computational trade-offs

### Comparison table

Compare:

- representation
- main purpose
- robustness
- computational considerations
- typical use

The syllabus specifically names SIFT, SURF and HOG; ORB is an explicit extension and should be labelled accordingly.

---

# 6. Part IV — Compressing Images

## C21 — Image Compression Fundamentals

### Major concepts

- need for compression
- redundancy
- spatial redundancy
- coding redundancy
- statistical redundancy
- perceptual redundancy
- compression ratio
- lossless vs lossy

---

## C22 — Entropy, Run-Length Encoding and Huffman Coding

### Major concepts

- information intuition
- entropy
- symbol probabilities
- RLE
- Huffman coding
- prefix codes
- coding efficiency

### Core formula

\[
H(X)=-\sum_i p_i\log_2p_i
\]

### Worked examples

- entropy of a tiny distribution
- RLE encoding
- Huffman tree and encoded symbols

---

## C23 — Transform Coding and DCT

### Major concepts

- transform coding
- spatial redundancy
- DCT intuition
- basis functions
- coefficient representation
- energy concentration
- quantization

### Core visual assets

```text
image block
→ transform coefficients
→ important coefficients
→ quantization
```

---

## C24 — JPEG Compression End to End

### Master pipeline

```text
RGB image
→ colour conversion
→ chroma subsampling
→ 8×8 blocks
→ DCT
→ quantization
→ zig-zag scan
→ DC/AC coding
→ entropy coding
→ JPEG bitstream
```

### Critical teaching point

Explicitly identify:

> **Where information is discarded and where the coding/compression occurs.**

### Quality

Discuss:

- compression ratio
- visual artifacts
- block effects
- quantization strength
- quality trade-off

---

# 7. Part V — From DIP to Intelligent Vision

## C25 — Image Classification

### Major concepts

- classification task
- label
- feature representation
- training/inference
- classical vs learned features
- image-level decision

### Task distinction

```text
Classification → what?
Detection      → what + where?
Segmentation   → which pixels?
```

---

## C26 — Convolutional Neural Networks

### Major concepts

- image tensor
- convolution
- learned filters
- feature maps
- activation
- pooling
- multilayer feature hierarchy
- training/inference

### Main bridge

```text
Classical DIP:
human-designed kernel

CNN:
learned kernel
```

This should explicitly connect CNN convolution to earlier DIP filtering.

---

## C27 — VGG and ResNet

### Major concepts

- deeper networks
- feature hierarchy
- VGG-style stacking
- residual learning
- skip/residual connections
- why deeper networks become difficult
- architecture comparison

---

## C28 — Object Detection and YOLO

### Major concepts

- detection problem
- bounding boxes
- confidence
- class prediction
- IoU
- real-time inference
- YOLO concept
- model/version awareness

Do not describe YOLO as one immutable algorithm; distinguish the general family from the concrete implementation used in practical work.

---

## C29 — Image Denoising with Autoencoders

### Major concepts

- encoder
- latent representation
- decoder
- reconstruction
- denoising objective
- training pairs
- limitations

### Pipeline

```text
noisy image
→ encoder
→ latent representation
→ decoder
→ reconstructed image
```

---

## C30 — Video Processing and Motion Analysis

### Major concepts

- video as image sequence
- frame
- temporal dimension
- frame differencing
- background change
- motion detection
- optical flow
- motion vectors
- tracking intuition

### Practical connection

The syllabus includes motion tracking using optical flow.

---

## C31 — DIP Applications, Engineering Context and Responsible Use

### Major concepts

- healthcare imaging
- surveillance
- industrial inspection
- document processing
- remote sensing
- entertainment/media
- limitations
- dataset dependence
- privacy
- bias and reliability
- human oversight

The chapter should connect the technical pipeline to real engineering systems without turning into a generic AI ethics chapter.

---

# 8. Syllabus Coverage Matrix

| Syllabus requirement | Main chapters |
|---|---|
| Fundamentals of DIP | C01 |
| Image formation | C02 |
| Sampling | C03 |
| Quantization | C03 |
| Grayscale | C04 |
| RGB | C04–C05 |
| Multispectral | C04 |
| Pixels | C04 |
| Bit depth | C03–C04 |
| Resolution | C04 |
| RGB | C05 |
| HSV | C05 |
| CMY | C05 |
| YUV | C05 |
| BMP | C05 |
| JPEG | C05, C24 |
| PNG | C05 |
| TIFF | C05 |
| Spatial enhancement | C06–C10 |
| Histogram equalization | C07 |
| Smoothing | C09 |
| Sharpening | C10 |
| Edge detection | C10 |
| Fourier transform | C12 |
| Frequency filters | C13 |
| Noise reduction | C09, C14 |
| Image restoration | C14 |
| Segmentation | C15–C17 |
| Global thresholding | C16 |
| Adaptive thresholding | C16 |
| Region-based segmentation | C17 |
| Erosion | C18 |
| Dilation | C18 |
| Opening | C18 |
| Closing | C18 |
| Features/descriptors | C19–C20 |
| SIFT | C20 |
| SURF | C20 |
| HOG | C20 |
| Lossless compression | C21–C22 |
| Lossy compression | C21–C24 |
| JPEG compression | C24 |
| Classification | C25 |
| Object detection | C28 |
| CNNs | C26 |
| VGG | C27 |
| ResNet | C27 |
| YOLO | C28 |
| Autoencoder denoising | C29 |
| Healthcare | C31 |
| Surveillance | C31 |
| Video processing | C30 |
| Motion analysis | C30 |

---

# 9. Lab Mapping

| Practical | Primary Main chapters |
|---|---|
| Image input/output + colour conversion | C04–C05 |
| Image enhancement | C06–C10 |
| Frequency-domain filtering | C12–C13 |
| Noise removal | C09, C14 |
| Image segmentation | C15–C18 |
| Feature detection | C19–C20 |
| JPEG compression | C21–C24 |
| CNN classification | C25–C26 |
| Object detection using YOLO | C28 |
| Motion tracking / optical flow | C30 |

---

# 10. Cross-Layer Map

Every major Main chapter should eventually expose connections.

Example:

```text
C07 Histogram Enhancement

MAIN
→ complete concept

MATH
→ histogram probability + CDF

LAB
→ histogram experiment

CODE
→ histogram/equalization implementation

EXAM
→ definition + numerical + comparison

PRACTICE
→ numerical + visual interpretation

RESOURCE
→ textbook/official references

ASSET
→ histogram figures

MASTER
→ dependency/status
```

---

# 11. Part-Level Learning Outcomes

## Part I

You should be able to represent an image correctly as digital data and explain how it became digital.

## Part II

You should be able to choose and reason about enhancement, filtering and restoration techniques.

## Part III

You should be able to isolate useful structures and represent image features.

## Part IV

You should be able to explain why and how image data can be compressed.

## Part V

You should understand how classical image processing connects to modern vision systems.

---

# 12. Final Main Book Principle

The reader should be able to move through the subject as a coherent story:

```text
What is the image?
        ↓
How did we obtain it?
        ↓
How is it represented?
        ↓
How can we improve it?
        ↓
How can we restore it?
        ↓
How can we isolate meaningful regions?
        ↓
How can we describe what is inside it?
        ↓
How can we store it efficiently?
        ↓
How can a machine classify or detect content?
        ↓
How does this extend to video and real systems?
```

That narrative is the primary organizing principle of the Main Book.
