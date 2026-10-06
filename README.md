# 📷 DIP MiniBook — Arpit | DU B.Tech / B.Sc CSE (DSE-3)

> **Digital Image Processing** · University of Delhi · DSE-3
> A Visual, Mathematical, and Algorithmic Self-Teaching Interactive Textbook mapped directly to the University Syllabus across 4 Units and 31 Complete Chapters.

An interactive study companion and textbook for Digital Image Processing covering the complete university syllabus + modern computer vision foundations. Built for deep conceptual understanding, mathematical rigor, algorithmic intuition, and offline self-study.

## 🌐 Live Site

Hosted on GitHub Pages → [`malikarpit.github.io/dip-minibook`](https://malikarpit.github.io/dip-minibook/)

---

## 🎯 Dual-View & Interactive Syllabus Filter

The portal now features an interactive curriculum filter engine:
1. **📋 University Syllabus Order (4 Units)**: Re-arranges the entire book into the exact 4-Unit sequence prescribed by the University of Delhi syllabus. In Unit IV, topics are arranged in the precise syllabus order (Classification & Detection → CNNs → Pretrained VGG/ResNet/YOLO → Autoencoder Denoising → **Healthcare & Surveillance Applications** → **Video & Motion Analysis**).
2. **📚 Book Architecture (5 Parts)**: Explores the conceptual progression from raw signal capture to deep vision (Parts I through V).
3. **⚡ Instant Unit Filtering & Search**: Click `Unit I`, `Unit II`, `Unit III`, or `Unit IV` pills, or type keywords in the real-time search box to instantly find chapters covering specific syllabus line items (e.g. Otsu, SIFT, JPEG, Autoencoders, CNNs, YUV).

---

## 📚 Curriculum & Official Syllabus Mapping (4 Units · 31 Chapters)

### Unit - I: Introduction to Digital Image Processing
*Syllabus: Fundamentals of Image Processing, Image Formation, Sampling, and Quantization, Types of Images: Grayscale, RGB, Multispectral, Image Representation: Pixels, Bit Depth, and Resolution, Color Models: RGB, HSV, CMY, YUV, File Formats: BMP, JPEG, PNG, TIFF.*

| Ch | Title | Official Syllabus Topic Covered |
|---|---|---|
| **01** | The Big Picture: What is an Image? | **Fundamentals of Image Processing**: Definition of DIP, steps in digital image processing, components of an image processing system, visual perception, EM spectrum. |
| **02** | Image Formation & Physical Acquisition | **Image Formation**: Illumination-reflectance model $f(x,y)=i(x,y)r(x,y)$, sensor geometries, camera geometry, thin lens formula. |
| **03** | Spatial Sampling & Quantization | **Sampling, and Quantization**: 2D sampling lattice, Nyquist sampling theorem, spatial aliasing, uniform & non-uniform quantization, bit depth $k$, levels $L=2^k$. |
| **04** | Pixels, Matrices, Tensors & Resolution | **Types of Images & Image Representation**: Grayscale, RGB, Multispectral, Pixels, Bit Depth, Resolution, 4/8/m-connectivity, adjacency, distance metrics ($D_e, D_4, D_8$). |
| **05** | Colour Models & Image File Formats | **Color Models & File Formats**: RGB, HSV, CMY, YUV, CIE chromaticity, chroma subsampling (4:4:4, 4:2:2, 4:2:0), BMP, JPEG, PNG, TIFF. |

---

### Unit - II: Image Enhancement and Restoration
*Syllabus: Spatial Domain Techniques, Histogram Equalization, Spatial Filtering: Smoothing, Sharpening, Edge Detection, Frequency Domain Techniques, Fourier Transform and Its Applications, Frequency Filters: Low-Pass, High-Pass, Band-Pass, Noise Reduction and Image Restoration Techniques.*

| Ch | Title | Official Syllabus Topic Covered |
|---|---|---|
| **06** | Point Processing & Intensity Transformations | **Spatial Domain Techniques**: Point processing, image negative, log transform, power-law (Gamma) correction, contrast stretching, bit-plane slicing. |
| **07** | Histograms & Contrast Enhancement | **Histogram Equalization**: Histogram definition, normalized histogram, discrete equalization derivation, histogram matching, local processing, CLAHE. |
| **08** | Spatial Filtering & Convolution | **Spatial Filtering (Mechanics & Convolution)**: Mechanics of 2D linear filtering, correlation vs convolution (180° kernel rotation), boundary padding, separable filters. |
| **09** | Smoothing & Noise Reduction | **Spatial Filtering: Smoothing**: Box filter, weighted average, Gaussian filter derivation, non-linear median filtering, salt-and-pepper noise reduction, bilateral smoothing. |
| **10** | Sharpening & Edge Detection | **Spatial Filtering: Sharpening, Edge Detection**: First derivatives (Roberts, Prewitt, Sobel), second derivative (Laplacian), unsharp masking, highboost, LoG, Canny edge detector. |
| **11** | Geometric Transformations & Interpolation | **Spatial Domain: Geometric Transformations**: Forward vs inverse mapping, affine coordinate matrices in homogeneous coordinates, nearest-neighbor, bilinear, bicubic interpolation. |
| **12** | 2D Fourier Transform & Frequency Domain | **Frequency Domain Techniques, Fourier Transform & Applications**: 1D and 2D DFT, magnitude & phase spectrum, centering via $(-1)^{x+y}$, 2D Convolution Theorem, FFT. |
| **13** | Frequency-Domain Filtering | **Frequency Filters: Low-Pass, High-Pass, Band-Pass**: Ideal, Butterworth, Gaussian lowpass (ILPF, BLPF, GLPF) and highpass (IHPF, BHPF, GHPF) filters, Gibbs ringing, notch filters. |
| **14** | Image Restoration & Deblurring | **Noise Reduction and Image Restoration Techniques**: Degradation models $g=f*h+n$, noise probability distributions, inverse filtering, Wiener (MMSE) filter, constrained least squares. |

---

### Unit - III: Image Analysis and Compression
*Syllabus: Image Segmentation, Thresholding (Global, Adaptive), Region-Based Segmentation, Morphological Operations: Erosion, Dilation, Opening, Closing, Image Features and Descriptors, SIFT, SURF, HOG, Image Compression, Lossless vs. Lossy Compression, JPEG Compression Steps and Implementation.*

| Ch | Title | Official Syllabus Topic Covered |
|---|---|---|
| **15** | Image Segmentation Fundamentals & Edge Linking | **Image Segmentation**: Discontinuity detection, point, line, and edge detection, local edge linking, global Hough transform ($\rho = x\cos\theta + y\sin\theta$). |
| **16** | Thresholding & Otsu’s Method | **Thresholding (Global, Adaptive)**: Role of illumination, basic global thresholding, Otsu’s between-class variance maximization, dual thresholding, local adaptive thresholding. |
| **17** | Region-Based Segmentation | **Region-Based Segmentation**: Seeded region growing, quadtree split-and-merge hierarchical segmentation, watershed transform. |
| **18** | Mathematical Morphology | **Morphological Operations: Erosion, Dilation, Opening, Closing**: Structuring elements, hit-or-miss transform, boundary extraction, hole filling, connected components, thinning. |
| **19** | Image Features & Descriptors | **Image Features and Descriptors**: Boundary chain codes, shape numbers, Fourier descriptors, regional Euler number, GLCM texture analysis, Hu’s 7 invariant moments. |
| **20** | Local Feature Detectors (SIFT, SURF, ORB & HOG) | **SIFT, SURF, HOG**: Scale-space Difference of Gaussians (DoG), SIFT 128-D descriptor, SURF integral box filters, FAST/ORB binary descriptors, Histogram of Oriented Gradients (HOG). |
| **21** | Image Compression Fundamentals | **Image Compression**: Coding redundancy, spatial / interpixel redundancy, psychovisual redundancy, compression ratio, Shannon information entropy, fidelity criteria (MSE, PSNR). |
| **22** | Lossless Coding (RLE, Huffman & LZW) | **Lossless vs. Lossy Compression**: Run-Length Encoding (RLE), bit-plane compression, Huffman optimal prefix-free code trees, average codeword length, coding efficiency, LZW coding. |
| **23** | Transform Coding & Discrete Cosine Transform | **JPEG Compression Steps: Transform & DCT**: 2D Discrete Cosine Transform (DCT-II), energy compaction, sub-image 8x8 block decomposition, psychoacoustic quantization matrices, zigzag scan. |
| **24** | JPEG Compression End to End & JPEG 2000 | **JPEG Compression Steps: Pipeline & Implementation**: Baseline sequential JPEG standard, DC DPCM differential coding, AC zero-run Huffman coding, JPEG 2000 DWT overview. |

---

### Unit - IV: Advanced Topics in Digital Image Processing
*Syllabus: Image Classification and Object Detection, Introduction to Convolutional Neural Networks (CNNs), Pretrained Models (VGG, ResNet, YOLO), Image Denoising using Autoencoders, Applications in Healthcare and Surveillance, Introduction to Video Processing and Motion Analysis.*

*Arranged below in the exact sequence of the uploaded syllabus:*

| Syllabus Order | Ch | Title | Official Syllabus Topic Covered |
|---|---|---|---|
| **#1** | **25** | Image Classification Foundations | **Image Classification and Object Detection (Part 1: Classification)**: Feature space decision boundaries, k-Nearest Neighbors (k-NN), linear classifiers ($Wx + b$), Softmax cross-entropy loss. |
| **#2** | **26** | CNNs for Image Processing | **Introduction to Convolutional Neural Networks (CNNs)**: Connection between spatial filtering and CNNs, 2D conv layers, parameter sharing, receptive fields, stride & padding, ReLU, pooling layers. |
| **#3** | **27** | Modern Vision Architectures: VGG & ResNet | **Pretrained Models (VGG, ResNet)**: VGGNet 3x3 filter factorization, vanishing gradients, ResNet residual skip connections ($H(x) = F(x) + x$), transfer learning. |
| **#4** | **28** | Object Detection & YOLO | **Pretrained Models (YOLO) & Object Detection**: Localization vs detection, bounding box $[x,y,w,h]$, IoU, Non-Maximum Suppression (NMS), YOLO unified grid regression. |
| **#5** | **29** | Image Denoising with Autoencoders | **Image Denoising using Autoencoders**: Unsupervised visual learning, encoder-decoder bottleneck, Convolutional Autoencoder (CAE), transpose convolutions, reconstruction loss. |
| **#6** | **31** | Applications in Healthcare & Surveillance | **Applications in Healthcare and Surveillance**: Medical imaging (CT Hounsfield units, MRI artifact removal, automated tumor segmentation), surveillance monitoring, biometrics, ethical AI. |
| **#7** | **30** | Video Processing & Motion Analysis | **Introduction to Video Processing and Motion Analysis**: 3D spatiotemporal volume $I(x,y,t)$, frame differencing, background subtraction (MOG2), optical flow constraint equation, Lucas-Kanade. |

---

## 🛠️ Pedagogical & Interactive Features

- **Unit & Topic Alignment Badges:** Every chapter header displays its corresponding University Unit and specific syllabus line item.
- **Interactive Syllabus Filter:** Real-time client-side filter on the home portal (`index.html`) and study dashboard (`progress.html`).
- **MathJax 3 Typesetting:** Full LaTeX mathematical derivations rendered cleanly across all chapters.
- **Study Dashboard (`progress.html`):** Real-time reading depth, checklist tracking, and stats broken down by University Unit.

---

## 🚀 Running Locally

```bash
cd dip
python3 -m http.server 8080
# Open http://localhost:8080 in your browser
```
