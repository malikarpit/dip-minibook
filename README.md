# 📷 DIP MiniBook — Arpit | DU B.Tech / B.Sc CSE (DSE-3)

> **Digital Image Processing** · University of Delhi · DSE-3
> A Visual, Mathematical, and Algorithmic Self-Teaching Interactive Textbook across 5 Parts and 31 Complete Chapters.

An interactive study companion and textbook for Digital Image Processing covering the complete university syllabus + modern computer vision foundations. Built for deep conceptual understanding, mathematical rigor, algorithmic intuition, and offline self-study.

## 🌐 Live Site

Hosted on GitHub Pages → [`malikarpit.github.io/dip-minibook`](https://malikarpit.github.io/dip-minibook/)

---

## 📚 Curriculum & Content Coverage (31 Chapters)

### Part I: The Image — Acquisition, Sampling, Representation & Color
- **Ch 01: The Big Picture: What is an Image?** — Physical scenes, measured signals, 2D continuous functions, the EM spectrum, and the master DIP pipeline.
- **Ch 02: Image Formation & Acquisition** — Pinhole cameras, thin lens equation, Bayer sensors, radiometric calibration, and dynamic range.
- **Ch 03: Sampling & Quantization** — 2D Whittaker-Shannon sampling theorem, spatial resolution, aliasing, Moire patterns, bit-depth, and uniform/Lloyd-Max quantization.
- **Ch 04: Image Representation: Pixels, Matrices, Tensors & Resolution** — Pixel coordinate conventions, intensity matrix representation, spatial/intensity resolution trade-offs, and multi-channel tensor structures.
- **Ch 05: Colour Models & Image File Formats** — Trichromacy, CIE XYZ & chromaticity diagrams, RGB, CMY/CMYK, HSI/HSV, YCbCr/YUV color spaces, and lossless vs. lossy container formats.

### Part II: Improving the Image — Enhancement, Filtering, Frequency & Restoration
- **Ch 06: Point Processing & Intensity Transformations** — Identity, negative, log transformations, power-law (Gamma) correction, and piecewise linear transformations.
- **Ch 07: Histograms & Contrast Enhancement** — Histogram definitions, equalization derivation, exact specification/matching, and adaptive local histogram equalization (CLAHE).
- **Ch 08: Spatial Filtering & Convolution** — Correlation vs. convolution, boundary handling, padding modes, separability, and linear filtering mechanics.
- **Ch 09: Smoothing & Noise Reduction** — Box filters, Gaussian kernels, impulse noise, median filters, min/max filters, and bilateral edge-preserving smoothing.
- **Ch 10: Sharpening & Edge Detection** — First vs. second derivatives, Laplacian, Unsharp Masking, High-Boost filtering, gradient operators (Sobel, Prewitt), and the Canny edge detector.
- **Ch 11: Geometric Transformations & Interpolation** — Affine matrix representations, forward vs. inverse mapping, nearest-neighbor, bilinear, and bicubic interpolation.
- **Ch 12: Fourier Transform & the Frequency Domain** — 1D/2D continuous and discrete Fourier transform (DFT), magnitude and phase spectra, convolution theorem, and FFT algorithms.
- **Ch 13: Frequency-Domain Filtering** — Ideal, Butterworth, and Gaussian lowpass & highpass filters, homomorphic filtering, and bandpass/bandreject filters.
- **Ch 14: Image Restoration & Deblurring** — Image degradation models, noise probability distributions, inverse filtering, Wiener filtering, and constrained least squares restoration.

### Part III: Understanding Image Content — Segmentation, Morphology & Feature Descriptors
- **Ch 15: Image Segmentation Fundamentals** — Discontinuity vs. similarity paradigms, point/line detection, and the foundational taxonomy of segmentation.
- **Ch 16: Thresholding & Otsu’s Method** — Global thresholding, Otsu’s between-class variance maximization, dual-thresholding, and local adaptive thresholding.
- **Ch 17: Region-Based Segmentation** — Seeded region growing, quadtree-based split-and-merge segmentation, and watershed algorithm.
- **Ch 18: Mathematical Morphology** — Structuring elements, erosion, dilation, opening, closing, Hit-or-Miss transform, morphological gradient, boundary extraction, and top-hat transforms.
- **Ch 19: Image Features & Descriptors** — Corners, blobs, edges, Harris Corner Detector, Hessian matrix, and rotational invariance.
- **Ch 20: SIFT, SURF, ORB & HOG** — Scale-space representation, Difference of Gaussians (DoG), FAST corners, BRIEF binary descriptors, ORB rotation compensation, and Histogram of Oriented Gradients (HOG).

### Part IV: Compressing Images — Information Theory, Quantization & Standards
- **Ch 21: Image Compression Fundamentals & Entropy** — Coding, inter-pixel, and psychovisual redundancies, fidelity criteria (MSE, PSNR), and Shannon’s source coding theorem.
- **Ch 22: Lossless Coding Techniques** — Run-Length Encoding (RLE), Huffman coding, Arithmetic coding, and LZW compression.
- **Ch 23: Lossy Compression, Transform Coding & JPEG** — Block-based discrete cosine transform (DCT), energy compaction, psychoacoustic quantization matrices, zigzag scan, and baseline JPEG.
- **Ch 24: Wavelet Transform & JPEG 2000** — Multi-resolution analysis, Continuous vs. Discrete Wavelet Transform (DWT), sub-band decomposition, and the EBCOT algorithm.

### Part V: From DIP to Intelligent Vision — Deep Learning & Modern Computer Vision
- **Ch 25: Image Classification Foundations** — Classical pipelines vs. representation learning, Nearest Neighbors, Linear classifiers, and Softmax loss.
- **Ch 26: CNNs for Image Processing** — Convolutional layers, receptive fields, spatial dimensions, pooling layers, and backpropagation in 2D grids.
- **Ch 27: Modern Vision Architectures (VGG & ResNet)** — VGGNet small 3x3 filter philosophy, vanishing gradients, residual skip connections, and ResNet architectures.
- **Ch 28: Object Detection & YOLO** — Localization vs. detection, sliding windows, R-CNN family, Anchor boxes, Non-Maximum Suppression (NMS), and YOLO real-time unified detection.
- **Ch 29: Image Denoising with Autoencoders** — Encoder-decoder bottleneck architectures, reconstruction loss, Denoising Autoencoders (DAE), and U-Net skip architectures.
- **Ch 30: Video Processing & Motion Analysis** — Spatio-temporal representation, frame differencing, background subtraction (MOG2), and Optical Flow (Lucas-Kanade & Horn-Schunck).
- **Ch 31: DIP Applications, Engineering & Ethics** — Medical imaging (CT, MRI), satellite remote sensing, biometric identification, computational photography, model bias, and digital forensics.

---

## 🛠️ Pedagogical & Interactive Features

- **MathJax 3 Typesetting:** Full LaTeX mathematical derivations rendered cleanly across all chapters.
- **Bilingual & Intuitive Insights:** Key engineering intuition, common pitfalls, and exam tips.
- **Study Dashboard (`progress.html`):** Real-time reading depth, checklist tracking, and stats.
- **Responsive Navigation:** Interactive Table of Contents, dark/light theme toggle, and quick sidebar navigation.

---

## 🚀 Running Locally

```bash
cd dip
python3 -m http.server 8080
# Open http://localhost:8080 in your browser
```
