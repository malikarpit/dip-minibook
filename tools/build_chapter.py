#!/usr/bin/env python3
"""
Digital Image Processing (DIP) MiniBook — Master Chapter Generator Script
Compiles complete manuscript markdown files from content-sources/main/ into
rich, production-grade 1,800–2,500 line HTML chapters adhering to DIP_DESIGN-01,
DIP_DESIGN-02, and the Master Minibook Framework v2.0.
"""

import os
import re
import sys
import html
import markdown

CHAPTERS_META = [
    # ── PART I: THE IMAGE ─────────────────────────────────────────────
    {
        'id': 'DIP-U1-C01',
        'file': 'DIP_Ch01_Digital_Image_Processing_The_Big_Picture.md',
        'chapter_num': 1,
        'unit_name': 'Unit I', 'part_num': 'Part I',
        'part_id': 'part-i',
        'part_name': 'The Image',
        'title': 'The Big Picture: What is an Image?',
        'subtitle': 'Physical Scenes, Measured Signals, Digital Matrices, the EM Spectrum, and the Master DIP Pipeline',
        'concept_id': '[CONCEPT-DIP-001]',
        'output_file': 'ch01-big-picture.html',
        'read_time': '~40 min read',
        'exam_priority': 'Core Foundation',
        'uni_syllabus_text': '<strong>Fundamentals of Image Processing:</strong> What is DIP, steps in image processing, components of an image processing system, visual perception, electromagnetic spectrum imaging, and the imaging continuum.',
        'uni_sections': ['01.1', '01.2', '01.3', '01.4', '01.5', '01.6', '01.7', '01.8', '01.10', '01.11'],
        'gate_sections': ['01.2', '01.5', '01.8', '01.10'],
        'prev_link': '../index.html',
        'prev_label': '← Portal Home',
        'next_link': 'ch02-image-formation.html',
        'next_label': 'Next: Ch 2 — Image Formation & Acquisition →'
    },
    {
        'id': 'DIP-U1-C02',
        'file': 'DIP_Ch02_Image_Formation_and_Acquisition.md',
        'chapter_num': 2,
        'unit_name': 'Unit I', 'part_num': 'Part I',
        'part_id': 'part-i',
        'part_name': 'The Image',
        'title': 'Image Formation & Physical Acquisition',
        'subtitle': 'The Illumination-Reflectance Model f(x,y)=i(x,y)r(x,y), Thin Lens Optics, Sensor Geometries, and Clipping',
        'concept_id': '[CONCEPT-DIP-002]',
        'output_file': 'ch02-image-formation.html',
        'read_time': '~45 min read',
        'exam_priority': 'High Yield (5–10 mark guarantee)',
        'uni_syllabus_text': '<strong>Image Formation & Sensing:</strong> Physical basis of illumination and reflectance, physical constraints, camera geometry, thin lens formula, single sensor, sensor strip, and 2D focal plane arrays.',
        'uni_sections': ['02.1', '02.2', '02.3', '02.4', '02.5', '02.6', '02.7', '02.8', '02.10', '02.12', '02.13', '02.16'],
        'gate_sections': ['02.2', '02.3', '02.5', '02.7', '02.12'],
        'prev_link': 'ch01-big-picture.html',
        'prev_label': '← Ch 1 — The Big Picture',
        'next_link': 'ch03-sampling-quantization.html',
        'next_label': 'Next: Ch 3 — Sampling & Quantization →'
    },
    {
        'id': 'DIP-U1-C03',
        'file': 'DIP_Ch03_Sampling_and_Quantization.md',
        'chapter_num': 3,
        'unit_name': 'Unit I', 'part_num': 'Part I',
        'part_id': 'part-i',
        'part_name': 'The Image',
        'title': 'Spatial Sampling & Quantization',
        'subtitle': 'Continuous to Discrete Coordinate Mapping, 2D Nyquist-Shannon Theorem, Spatial Aliasing, Bit Depth, and Quantization Noise',
        'concept_id': '[CONCEPT-DIP-003]',
        'output_file': 'ch03-sampling-quantization.html',
        'read_time': '~50 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Sampling & Quantization:</strong> Spatial sampling lattice, Nyquist sampling theorem, spatial aliasing, Moiré patterns, uniform and non-uniform amplitude quantization, bit depth k, number of levels L=2^k, false contouring, and storage footprint calculations.',
        'uni_sections': ['03.1', '03.2', '03.3', '03.4', '03.7', '03.8', '03.9', '03.10', '03.11', '03.15', '03.16', '03.18', '03.20', '03.21'],
        'gate_sections': ['03.3', '03.8', '03.9', '03.10', '03.16', '03.18', '03.21'],
        'prev_link': 'ch02-image-formation.html',
        'prev_label': '← Ch 2 — Formation & Acquisition',
        'next_link': 'ch04-image-representation.html',
        'next_label': 'Next: Ch 4 — Pixels, Matrices & Resolution →'
    },
    {
        'id': 'DIP-U1-C04',
        'file': 'DIP_Ch04_Image_Representation_Pixels_Matrices_Tensors_and_Resolution.md',
        'chapter_num': 4,
        'unit_name': 'Unit I', 'part_num': 'Part I',
        'part_id': 'part-i',
        'part_name': 'The Image',
        'title': 'Pixels, Matrices, Tensors & Resolution',
        'subtitle': 'Pixel Coordinate Systems, 4/8/m-Connectivity, Topological Path Ambiguities, Distance Metrics (De, D4, D8), and Matrix Operations',
        'concept_id': '[CONCEPT-DIP-004]',
        'output_file': 'ch04-image-representation.html',
        'read_time': '~50 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Image Representation & Pixel Relationships:</strong> Neighbors of a pixel (N4, ND, N8), Adjacency, 4-connectivity, 8-connectivity, mixed m-connectivity, boundary tracing, Distance metrics (Euclidean, City-block D4, Chessboard D8), and Image arithmetic (addition, subtraction, multiplication).',
        'uni_sections': ['04.1', '04.2', '04.3', '04.4', '04.5', '04.7', '04.8', '04.9', '04.10', '04.12', '04.13', '04.14', '04.15'],
        'gate_sections': ['04.3', '04.5', '04.8', '04.9', '04.10', '04.12', '04.13'],
        'prev_link': 'ch03-sampling-quantization.html',
        'prev_label': '← Ch 3 — Sampling & Quantization',
        'next_link': 'ch05-colour-models-file-formats.html',
        'next_label': 'Next: Ch 5 — Colour Models & Formats →'
    },
    {
        'id': 'DIP-U1-C05',
        'file': 'DIP_Ch05_Colour_Models_and_Image_File_Formats.md',
        'chapter_num': 5,
        'unit_name': 'Unit I', 'part_num': 'Part I',
        'part_id': 'part-i',
        'part_name': 'The Image',
        'title': 'Colour Models & Image File Formats',
        'subtitle': 'Trichromatic Human Vision, RGB Cube, CMYK Printing, HSV/HSI Geometric Derivations, YCbCr Video Subsampling, and File Formats (BMP, PNG, JPEG, TIFF)',
        'concept_id': '[CONCEPT-DIP-005]',
        'output_file': 'ch05-colour-models-file-formats.html',
        'read_time': '~50 min read',
        'exam_priority': 'High Yield (5–10 mark guarantee)',
        'uni_syllabus_text': '<strong>Colour Models & File Formats:</strong> Primary colours, CIE chromaticity diagram, RGB, CMY/CMYK, HSV (Hue, Saturation, Value), HSI, YCbCr chroma subsampling (4:4:4, 4:2:2, 4:2:0), BMP header structure, PNG lossless Deflate, JPEG lossy DCT overview, and OpenCV BGR vs RGB convention.',
        'uni_sections': ['05.1', '05.2', '05.3', '05.4', '05.5', '05.7', '05.8', '05.9', '05.10', '05.11', '05.13', '05.14', '05.15', '05.18'],
        'gate_sections': ['05.3', '05.4', '05.7', '05.9', '05.10', '05.11', '05.14'],
        'prev_link': 'ch04-image-representation.html',
        'prev_label': '← Ch 4 — Pixels, Matrices & Resolution',
        'next_link': 'ch06-point-processing.html',
        'next_label': 'Next: Ch 6 — Point Processing & Intensity →'
    },
    # ── PART II: IMPROVING THE IMAGE ─────────────────────────────────
    {
        'id': 'DIP-U2-C06',
        'file': 'DIP_Ch06_Point_Processing_and_Intensity_Transformations.md',
        'chapter_num': 6,
        'unit_name': 'Unit II', 'part_num': 'Part II',
        'part_id': 'part-ii',
        'part_name': 'Improving the Image',
        'title': 'Point Processing & Intensity Transformations',
        'subtitle': 'Digital Negatives, Logarithmic Dynamic Range Compression, Power-Law (Gamma) Correction, Contrast Stretching, and Bit-Plane Slicing',
        'concept_id': '[CONCEPT-DIP-006]',
        'output_file': 'ch06-point-processing.html',
        'read_time': '~45 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Intensity Transformations:</strong> Basic gray-level transformations (image negative, log transform, power-law gamma transformations), Piecewise linear transformation functions (contrast stretching, gray-level slicing with and without background, bit-plane slicing and steganography).',
        'uni_sections': ['06.1', '06.2', '06.3', '06.4', '06.5', '06.6', '06.7', '06.8', '06.9', '06.10', '06.12', '06.14', '06.15', '06.18', '06.20'],
        'gate_sections': ['06.3', '06.4', '06.5', '06.7', '06.9', '06.10', '06.15'],
        'prev_link': 'ch05-colour-models-file-formats.html',
        'prev_label': '← Ch 5 — Colour Models & Formats',
        'next_link': 'ch07-histograms-equalization.html',
        'next_label': 'Next: Ch 7 — Histograms & Contrast Enhancement →'
    },
    {
        'id': 'DIP-U2-C07',
        'file': 'DIP_Ch07_Histograms_and_Contrast_Enhancement.md',
        'chapter_num': 7,
        'unit_name': 'Unit II', 'part_num': 'Part II',
        'part_id': 'part-ii',
        'part_name': 'Improving the Image',
        'title': 'Histograms & Contrast Enhancement',
        'subtitle': 'Discrete Probability Density Functions, Mathematical Derivation of Histogram Equalization, Histogram Specification/Matching, Local Processing, and CLAHE',
        'concept_id': '[CONCEPT-DIP-007]',
        'output_file': 'ch07-histograms-equalization.html',
        'read_time': '~50 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Histogram Processing:</strong> Histogram definition, normalized histogram, continuous and discrete histogram equalization derivation, proof of uniform density, histogram matching (specification), local histogram processing, CLAHE, and image statistics (mean, variance).',
        'uni_sections': ['07.1', '07.2', '07.3', '07.4', '07.5', '07.6', '07.8', '07.9', '07.10', '07.12', '07.14', '07.15', '07.18', '07.22'],
        'gate_sections': ['07.2', '07.3', '07.4', '07.5', '07.8', '07.10', '07.18'],
        'prev_link': 'ch06-point-processing.html',
        'prev_label': '← Ch 6 — Point Processing & Intensity',
        'next_link': 'ch08-spatial-filtering.html',
        'next_label': 'Next: Ch 8 — Spatial Filtering & Convolution →'
    },
    {
        'id': 'DIP-U2-C08',
        'file': 'DIP_Ch08_Spatial_Filtering_and_Convolution.md',
        'chapter_num': 8,
        'unit_name': 'Unit II', 'part_num': 'Part II',
        'part_id': 'part-ii',
        'part_name': 'Improving the Image',
        'title': 'Spatial Filtering & Convolution',
        'subtitle': 'Mechanics of 2D Spatial Filtering, Correlation vs Convolution (180° Kernel Rotation), Boundary Padding Strategies, and Separable Kernel Optimization',
        'concept_id': '[CONCEPT-DIP-008]',
        'output_file': 'ch08-spatial-filtering.html',
        'read_time': '~55 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Spatial Filtering Fundamentals:</strong> Linear vs non-linear filters, mechanics of 2D convolution and correlation, boundary padding (zero, clamp, reflection, wrap), separable 2D convolution decomposition, computational complexity O(k^2) vs O(2k).',
        'uni_sections': ['08.1', '08.2', '08.3', '08.4', '08.5', '08.6', '08.8', '08.10', '08.12', '08.14', '08.16', '08.20', '08.24'],
        'gate_sections': ['08.2', '08.3', '08.4', '08.6', '08.8', '08.10', '08.16'],
        'prev_link': 'ch07-histograms-equalization.html',
        'prev_label': '← Ch 7 — Histograms & Equalization',
        'next_link': 'ch09-smoothing-noise-reduction.html',
        'next_label': 'Next: Ch 9 — Smoothing & Noise Reduction →'
    },
    {
        'id': 'DIP-U2-C09',
        'file': 'DIP_Ch09_Smoothing_and_Noise_Reduction.md',
        'chapter_num': 9,
        'unit_name': 'Unit II', 'part_num': 'Part II',
        'part_id': 'part-ii',
        'part_name': 'Improving the Image',
        'title': 'Smoothing & Noise Reduction',
        'subtitle': 'Linear Smoothing (Box & Weighted Average), 2D Gaussian Kernel Derivation ($6\\sigma+1$ Rule), Non-Linear Order-Statistic Median Filters, and Bilateral Filtering',
        'concept_id': '[CONCEPT-DIP-009]',
        'output_file': 'ch09-smoothing-noise-reduction.html',
        'read_time': '~50 min read',
        'exam_priority': 'High Yield (5–10 mark guarantee)',
        'uni_syllabus_text': '<strong>Smoothing Spatial Filters:</strong> Box filter, weighted average filter, Gaussian lowpass filter derivation and parameter sigma selection, order-statistic filters (median, min, max, alpha-trimmed), salt-and-pepper noise removal, and bilateral edge-preserving smoothing.',
        'uni_sections': ['09.1', '09.2', '09.3', '09.4', '09.5', '09.6', '09.8', '09.10', '09.12', '09.14', '09.16', '09.20', '09.22'],
        'gate_sections': ['09.2', '09.3', '09.5', '09.6', '09.8', '09.10', '09.16'],
        'prev_link': 'ch08-spatial-filtering.html',
        'prev_label': '← Ch 8 — Spatial Filtering & Convolution',
        'next_link': 'ch10-sharpening-edge-detection.html',
        'next_label': 'Next: Ch 10 — Sharpening & Edge Detection →'
    },
    {
        'id': 'DIP-U2-C10',
        'file': 'DIP_Ch10_Sharpening_and_Edge_Detection.md',
        'chapter_num': 10,
        'unit_name': 'Unit II', 'part_num': 'Part II',
        'part_id': 'part-ii',
        'part_name': 'Improving the Image',
        'title': 'Sharpening & Edge Detection',
        'subtitle': 'First Derivatives (Roberts, Prewitt, Sobel), Second Derivative (Laplacian Operator), Unsharp Masking & Highboost Filtering, LoG, and Canny Edge Detection Pipeline',
        'concept_id': '[CONCEPT-DIP-010]',
        'output_file': 'ch10-sharpening-edge-detection.html',
        'read_time': '~55 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Sharpening Spatial Filters & Edge Detection:</strong> First-order derivative filters, gradient vector magnitude and angle, Roberts, Prewitt, Sobel operators, second-order derivative Laplacian operator, Laplacian image sharpening, unsharp masking and highboost filtering, Laplacian of Gaussian (LoG), zero-crossing detection, and the complete 5-stage Canny edge detector.',
        'uni_sections': ['10.1', '10.2', '10.3', '10.4', '10.5', '10.6', '10.8', '10.9', '10.11', '10.12', '10.14', '10.16', '10.20', '10.25'],
        'gate_sections': ['10.2', '10.3', '10.4', '10.5', '10.8', '10.9', '10.12', '10.20'],
        'prev_link': 'ch09-smoothing-noise-reduction.html',
        'prev_label': '← Ch 9 — Smoothing & Noise Reduction',
        'next_link': 'ch11-geometric-transforms.html',
        'next_label': 'Next: Ch 11 — Geometric Transformations & Interpolation →'
    },
    {
        'id': 'DIP-U2-C11',
        'file': 'DIP_Ch11_Geometric_Transformations_and_Interpolation.md',
        'chapter_num': 11,
        'unit_name': 'Unit II', 'part_num': 'Part II',
        'part_id': 'part-ii',
        'part_name': 'Improving the Image',
        'title': 'Geometric Transformations & Interpolation',
        'subtitle': 'Forward vs Inverse Coordinate Mapping, 2D Affine Matrices in Homogeneous Coordinates, Nearest Neighbor, Bilinear, and Bicubic Interpolation',
        'concept_id': '[CONCEPT-DIP-011]',
        'output_file': 'ch11-geometric-transforms.html',
        'read_time': '~50 min read',
        'exam_priority': 'High Yield (5–10 mark guarantee)',
        'uni_syllabus_text': '<strong>Geometric Transformations & Interpolation:</strong> Forward mapping vs inverse mapping, transformation matrices in homogeneous coordinates (scaling, translation, rotation about arbitrary point, shear, reflection), affine transformations, image interpolation techniques (nearest-neighbor, bilinear, bicubic spline).',
        'uni_sections': ['11.1', '11.2', '11.3', '11.4', '11.5', '11.6', '11.8', '11.10', '11.12', '11.14', '11.18', '11.22'],
        'gate_sections': ['11.2', '11.3', '11.5', '11.8', '11.10', '11.12', '11.18'],
        'prev_link': 'ch10-sharpening-edge-detection.html',
        'prev_label': '← Ch 10 — Sharpening & Edge Detection',
        'next_link': 'ch12-fourier-transform.html',
        'next_label': 'Next: Ch 12 — Fourier Transform & Frequency Domain →'
    },
    {
        'id': 'DIP-U2-C12',
        'file': 'DIP_Ch12_Fourier_Transform_and_the_Frequency_Domain.md',
        'chapter_num': 12,
        'unit_name': 'Unit II', 'part_num': 'Part II',
        'part_id': 'part-ii',
        'part_name': 'Improving the Image',
        'title': 'Fourier Transform & Frequency Domain',
        'subtitle': 'Continuous to 2D Discrete Fourier Transform (DFT), Fourier Spectrum $|F(u,v)|$, Phase Angle, Centering via $(-1)^{x+y}$, 2D Convolution Theorem, and FFT',
        'concept_id': '[CONCEPT-DIP-012]',
        'output_file': 'ch12-fourier-transform.html',
        'read_time': '~60 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Fourier Transform & Frequency Domain:</strong> 1D and 2D Discrete Fourier Transform (DFT) and Inverse DFT (IDFT), Fourier spectrum, phase angle, power spectrum, dynamic range compression (log transform of spectrum), frequency domain centering using (-1)^(x+y), properties (periodicity, conjugate symmetry, translation, rotation), 2D Convolution Theorem, and Cooley-Tukey FFT algorithm.',
        'uni_sections': ['12.1', '12.2', '12.3', '12.4', '12.5', '12.6', '12.8', '12.10', '12.12', '12.14', '12.16', '12.20', '12.25'],
        'gate_sections': ['12.2', '12.3', '12.4', '12.6', '12.8', '12.10', '12.12', '12.16'],
        'prev_link': 'ch11-geometric-transforms.html',
        'prev_label': '← Ch 11 — Geometric Transformations',
        'next_link': 'ch13-frequency-filtering.html',
        'next_label': 'Next: Ch 13 — Frequency-Domain Filtering →'
    },
    {
        'id': 'DIP-U2-C13',
        'file': 'DIP_Ch13_Frequency_Domain_Filtering.md',
        'chapter_num': 13,
        'unit_name': 'Unit II', 'part_num': 'Part II',
        'part_id': 'part-ii',
        'part_name': 'Improving the Image',
        'title': 'Frequency-Domain Filtering',
        'subtitle': 'Filtering Pipeline, Lowpass Filters (Ideal ILPF, Butterworth BLPF, Gaussian GLPF), Gibbs Ringing Phenomena, Highpass Filtering, High-Frequency Emphasis, and Notch Filters',
        'concept_id': '[CONCEPT-DIP-013]',
        'output_file': 'ch13-frequency-filtering.html',
        'read_time': '~55 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Frequency Domain Filtering:</strong> Filtering in frequency domain workflow, zero padding for wraparound error avoidance, Lowpass filtering (Ideal ILPF, Butterworth BLPF, Gaussian GLPF), Gibbs ringing artifact analysis, Highpass filtering (IHPF, BHPF, GHPF), high-boost / high-frequency emphasis filtering, Bandreject, Bandpass, and Notch filters for periodic noise removal.',
        'uni_sections': ['13.1', '13.2', '13.3', '13.4', '13.5', '13.6', '13.8', '13.10', '13.12', '13.14', '13.16', '13.20', '13.24'],
        'gate_sections': ['13.2', '13.3', '13.4', '13.5', '13.8', '13.10', '13.12', '13.20'],
        'prev_link': 'ch12-fourier-transform.html',
        'prev_label': '← Ch 12 — Fourier Transform',
        'next_link': 'ch14-image-restoration.html',
        'next_label': 'Next: Ch 14 — Image Restoration & Deblurring →'
    },
    {
        'id': 'DIP-U2-C14',
        'file': 'DIP_Ch14_Image_Restoration_and_Deblurring.md',
        'chapter_num': 14,
        'unit_name': 'Unit II', 'part_num': 'Part II',
        'part_id': 'part-ii',
        'part_name': 'Improving the Image',
        'title': 'Image Restoration & Deblurring',
        'subtitle': 'Degradation Model $g(x,y)=f(x,y)*h(x,y)+\\eta(x,y)$, Inverse Filtering Noise Explosion, Wiener (MMSE) Regularized Restoration, Constrained Least Squares (CLS), and Geometric Registration',
        'concept_id': '[CONCEPT-DIP-014]',
        'output_file': 'ch14-image-restoration.html',
        'read_time': '~55 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Image Restoration:</strong> Degradation model in spatial and frequency domains, noise probability density functions (Gaussian, Rayleigh, Erlang, exponential, uniform, impulse salt-and-pepper), estimation of noise parameters, restoration in the presence of noise only, periodic noise reduction, inverse filtering and noise catastrophe, Wiener (minimum mean square error) filtering, Constrained Least Squares (CLS) restoration, and geometric distortion correction.',
        'uni_sections': ['14.1', '14.2', '14.3', '14.4', '14.5', '14.6', '14.8', '14.10', '14.12', '14.14', '14.16', '14.20', '14.25'],
        'gate_sections': ['14.2', '14.3', '14.4', '14.6', '14.8', '14.10', '14.12', '14.20'],
        'prev_link': 'ch13-frequency-filtering.html',
        'prev_label': '← Ch 13 — Frequency-Domain Filtering',
        'next_link': 'ch15-segmentation-fundamentals.html',
        'next_label': 'Next: Ch 15 — Segmentation Fundamentals →'
    },
    # ── PART III: UNDERSTANDING CONTENT ──────────────────────────────
    {
        'id': 'DIP-U3-C15',
        'file': 'DIP_Ch15_Image_Segmentation_Fundamentals.md',
        'chapter_num': 15,
        'unit_name': 'Unit III', 'part_num': 'Part III',
        'part_id': 'part-iii',
        'part_name': 'Understanding Content',
        'title': 'Image Segmentation Fundamentals & Edge Linking',
        'subtitle': 'Point, Line, and Edge Detection, Gradient Masks, Laplacian Zero-Crossings, Local Edge Linking, and the Hough Transform ($\\rho = x\\cos\\theta + y\\sin\\theta$)',
        'concept_id': '[CONCEPT-DIP-015]',
        'output_file': 'ch15-segmentation-fundamentals.html',
        'read_time': '~50 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Image Segmentation Fundamentals:</strong> Detection of discontinuities (point, line, edge detection), edge linking and boundary detection, local processing (gradient magnitude and direction), global processing via Hough Transform (parameter space, accumulator cells), and graph-theoretic approaches.',
        'uni_sections': ['15.1', '15.2', '15.3', '15.4', '15.5', '15.6', '15.8', '15.10', '15.12', '15.14', '15.16', '15.20', '15.25'],
        'gate_sections': ['15.2', '15.3', '15.4', '15.5', '15.8', '15.10', '15.14', '15.20'],
        'prev_link': 'ch14-image-restoration.html',
        'prev_label': '← Ch 14 — Image Restoration & Deblurring',
        'next_link': 'ch16-thresholding-otsu.html',
        'next_label': 'Next: Ch 16 — Thresholding & Otsu Method →'
    },
    {
        'id': 'DIP-U3-C16',
        'file': 'DIP_Ch16_Thresholding.md',
        'chapter_num': 16,
        'unit_name': 'Unit III', 'part_num': 'Part III',
        'part_id': 'part-iii',
        'part_name': 'Understanding Content',
        'title': 'Thresholding & Otsu\'s Method',
        'subtitle': 'Illumination Role, Basic Global Thresholding, Mathematical Derivation of Otsu\'s Optimum Between-Class Variance, and Adaptive/Multiple Thresholding',
        'concept_id': '[CONCEPT-DIP-016]',
        'output_file': 'ch16-thresholding-otsu.html',
        'read_time': '~50 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Thresholding:</strong> Role of illumination in thresholding, basic global thresholding algorithm, Otsu’s optimum global thresholding derivation, between-class variance maximization, separability measure eta, multiple thresholding, and variable/adaptive thresholding using moving averages and local statistics.',
        'uni_sections': ['16.1', '16.2', '16.3', '16.4', '16.5', '16.6', '16.8', '16.10', '16.12', '16.14', '16.16', '16.20', '16.25'],
        'gate_sections': ['16.2', '16.3', '16.4', '16.5', '16.8', '16.10', '16.14', '16.20'],
        'prev_link': 'ch15-segmentation-fundamentals.html',
        'prev_label': '← Ch 15 — Segmentation Fundamentals',
        'next_link': 'ch17-region-segmentation.html',
        'next_label': 'Next: Ch 17 — Region-Based Segmentation →'
    },
    {
        'id': 'DIP-U3-C17',
        'file': 'DIP_Ch17_Region_Based_Segmentation.md',
        'chapter_num': 17,
        'unit_name': 'Unit III', 'part_num': 'Part III',
        'part_id': 'part-iii',
        'part_name': 'Understanding Content',
        'title': 'Region-Based Segmentation',
        'subtitle': 'Axiomatic Segmentation Criteria, Region Growing (Seeds & Stopping Criteria), Region Splitting & Merging (Quadtree Hierarchy), and Watershed Transform',
        'concept_id': '[CONCEPT-DIP-017]',
        'output_file': 'ch17-region-segmentation.html',
        'read_time': '~50 min read',
        'exam_priority': 'High Yield (5–10 mark guarantee)',
        'uni_syllabus_text': '<strong>Region-Based Segmentation:</strong> Region segmentation criteria, region growing based on seed selection and similarity predicates, region splitting and merging using Quadtree hierarchical representation, and watershed segmentation algorithm using distance transforms and markers.',
        'uni_sections': ['17.1', '17.2', '17.3', '17.4', '17.5', '17.6', '17.8', '17.10', '17.12', '17.14', '17.16', '17.20', '17.25'],
        'gate_sections': ['17.2', '17.3', '17.4', '17.5', '17.8', '17.10', '17.14', '17.20'],
        'prev_link': 'ch16-thresholding-otsu.html',
        'prev_label': '← Ch 16 — Thresholding & Otsu Method',
        'next_link': 'ch18-mathematical-morphology.html',
        'next_label': 'Next: Ch 18 — Mathematical Morphology →'
    },
    {
        'id': 'DIP-U3-C18',
        'file': 'DIP_Ch18_Mathematical_Morphology.md',
        'chapter_num': 18,
        'unit_name': 'Unit III', 'part_num': 'Part III',
        'part_id': 'part-iii',
        'part_name': 'Understanding Content',
        'title': 'Mathematical Morphology',
        'subtitle': 'Set Theoretic Foundations, Structuring Elements, Erosion ($A \\ominus B$), Dilation ($A \\oplus B$), Opening ($A \\circ B$), Closing ($A \\bullet B$), Hit-or-Miss, Boundary Extraction, and Grayscale Top-Hat',
        'concept_id': '[CONCEPT-DIP-018]',
        'output_file': 'ch18-mathematical-morphology.html',
        'read_time': '~55 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Morphological Image Processing:</strong> Preliminaries (set theory, reflection, translation), structuring elements, erosion, dilation, duality between erosion and dilation, opening, closing, hit-or-miss transform, morphological algorithms (boundary extraction, hole filling, connected component extraction, convex hull, thinning, skeletons), and grayscale morphology (opening, closing, morphological gradient, top-hat and bottom-hat transforms).',
        'uni_sections': ['18.1', '18.2', '18.3', '18.4', '18.5', '18.6', '18.8', '18.10', '18.12', '18.14', '18.16', '18.20', '18.25'],
        'gate_sections': ['18.2', '18.3', '18.4', '18.5', '18.8', '18.10', '18.14', '18.20'],
        'prev_link': 'ch17-region-segmentation.html',
        'prev_label': '← Ch 17 — Region-Based Segmentation',
        'next_link': 'ch19-features-descriptors.html',
        'next_label': 'Next: Ch 19 — Image Features & Descriptors →'
    },
    {
        'id': 'DIP-U3-C19',
        'file': 'DIP_Ch19_Image_Features_and_Descriptors.md',
        'chapter_num': 19,
        'unit_name': 'Unit III', 'part_num': 'Part III',
        'part_id': 'part-iii',
        'part_name': 'Understanding Content',
        'title': 'Image Features & Descriptors',
        'subtitle': 'Boundary Descriptors (Chain Codes, Shape Numbers, Fourier Descriptors), Regional Descriptors (Compactness, Euler Number $E = C - H$), Texture via GLCM, and Hu\'s 7 Invariant Moments',
        'concept_id': '[CONCEPT-DIP-019]',
        'output_file': 'ch19-features-descriptors.html',
        'read_time': '~65 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Representation and Description:</strong> Boundary representation, Freeman chain codes (4-directional and 8-directional, normalization for rotation and starting point), shape numbers, Fourier descriptors, regional descriptors (simple topological descriptors, Euler number, compactness, circularity), texture analysis (statistical moments, Gray-Level Co-occurrence Matrix GLCM), and moment invariants (central moments, normalized moments, Hu’s 7 moment invariants).',
        'uni_sections': ['19.1', '19.2', '19.3', '19.4', '19.5', '19.6', '19.8', '19.10', '19.12', '19.14', '19.16', '19.20', '19.25', '19.30'],
        'gate_sections': ['19.2', '19.3', '19.4', '19.5', '19.8', '19.10', '19.14', '19.20', '19.30'],
        'prev_link': 'ch18-mathematical-morphology.html',
        'prev_label': '← Ch 18 — Mathematical Morphology',
        'next_link': 'ch20-sift-surf-orb-hog.html',
        'next_label': 'Next: Ch 20 — SIFT, SURF, ORB & HOG →'
    },
    {
        'id': 'DIP-U3-C20',
        'file': 'DIP_Ch20_SIFT_SURF_ORB_and_HOG.md',
        'chapter_num': 20,
        'unit_name': 'Unit III', 'part_num': 'Part III',
        'part_id': 'part-iii',
        'part_name': 'Understanding Content',
        'title': 'Local Feature Detectors (SIFT, SURF, ORB & HOG)',
        'subtitle': 'Harris Corner Autocorrelation Matrix, SIFT 4-Stage Architecture (DoG Scale-Space, Hessian Filtering, 128-D Descriptors), SURF Integral Box Filters, FAST/ORB Binary Descriptors, and HOG Pedestrian Detection',
        'concept_id': '[CONCEPT-DIP-020]',
        'output_file': 'ch20-sift-surf-orb-hog.html',
        'read_time': '~60 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Local Feature Detection & Description:</strong> Moravec and Harris corner detector, corner response function, SIFT (Scale Invariant Feature Transform, DoG octave pyramids, keypoint localization, orientation assignment, 128-D descriptor), SURF (Speeded-Up Robust Features, integral images, box filters), FAST corner test, ORB (Oriented FAST and Rotated BRIEF), and HOG (Histogram of Oriented Gradients).',
        'uni_sections': ['20.1', '20.2', '20.3', '20.4', '20.5', '20.6', '20.8', '20.10', '20.12', '20.14', '20.16', '20.20', '20.25'],
        'gate_sections': ['20.2', '20.3', '20.4', '20.5', '20.8', '20.10', '20.14', '20.20'],
        'prev_link': 'ch19-features-descriptors.html',
        'prev_label': '← Ch 19 — Image Features & Descriptors',
        'next_link': 'ch21-compression-entropy.html',
        'next_label': 'Next: Ch 21 — Compression & Entropy →'
    },
    # ── PART IV: COMPRESSING IMAGES ──────────────────────────────────
    {
        'id': 'DIP-U3-C21',
        'file': 'DIP_Ch21_Image_Compression_Fundamentals.md',
        'chapter_num': 21,
        'unit_name': 'Unit III', 'part_num': 'Part IV',
        'part_id': 'part-iv',
        'part_name': 'Compressing Images',
        'title': 'Image Compression Fundamentals',
        'subtitle': 'Coding, Spatial & Psychovisual Redundancy, Compression Ratios, Shannon Information Entropy, Noiseless Coding Theorem, and Fidelity Metrics (MSE, PSNR)',
        'concept_id': '[CONCEPT-DIP-021]',
        'output_file': 'ch21-compression-entropy.html',
        'read_time': '~45 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Image Compression Fundamentals:</strong> Need for compression, coding redundancy, spatial / interpixel redundancy, psychovisual redundancy, data compression metrics (compression ratio, relative redundancy), information theory (entropy definition, Shannon’s first theorem), and fidelity criteria (objective metrics: MSE, RMSE, PSNR; subjective metrics: MOS).',
        'uni_sections': ['21.1', '21.2', '21.3', '21.4', '21.5', '21.6', '21.7', '21.8', '21.10', '21.12', '21.15', '21.20'],
        'gate_sections': ['21.3', '21.4', '21.5', '21.6', '21.7', '21.8', '21.12'],
        'prev_link': 'ch20-sift-surf-orb-hog.html',
        'prev_label': '← Ch 20 — SIFT, SURF, ORB & HOG',
        'next_link': 'ch22-lossless-coding.html',
        'next_label': 'Next: Ch 22 — Lossless Coding (RLE & Huffman) →'
    },
    {
        'id': 'DIP-U3-C22',
        'file': 'DIP_Ch22_Entropy_RLE_and_Huffman_Coding.md',
        'chapter_num': 22,
        'unit_name': 'Unit III', 'part_num': 'Part IV',
        'part_id': 'part-iv',
        'part_name': 'Compressing Images',
        'title': 'Entropy, Run-Length Encoding & Huffman Coding',
        'subtitle': 'Run-Length Encoding (RLE), Bit-Plane RLE, Prefix-Free Codes, Huffman Optimal Coding Algorithm, Coding Efficiency $\\eta$, and LZW Dictionary Compression',
        'concept_id': '[CONCEPT-DIP-022]',
        'output_file': 'ch22-lossless-coding.html',
        'read_time': '~50 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Lossless Compression Methods:</strong> Run-Length Encoding (RLE) for binary and grayscale images, bit-plane compression, variable-length coding, Huffman coding algorithm derivation, code trees, average codeword length, coding efficiency, redundancy calculation, arithmetic coding concepts, and LZW dictionary coding.',
        'uni_sections': ['22.1', '22.2', '22.3', '22.4', '22.5', '22.6', '22.8', '22.10', '22.12', '22.15', '22.20'],
        'gate_sections': ['22.3', '22.4', '22.5', '22.6', '22.8', '22.10', '22.15'],
        'prev_link': 'ch21-compression-entropy.html',
        'prev_label': '← Ch 21 — Compression & Entropy',
        'next_link': 'ch23-lossy-dct-jpeg.html',
        'next_label': 'Next: Ch 23 — Transform Coding & DCT →'
    },
    {
        'id': 'DIP-U3-C23',
        'file': 'DIP_Ch23_Transform_Coding_and_DCT.md',
        'chapter_num': 23,
        'unit_name': 'Unit III', 'part_num': 'Part IV',
        'part_id': 'part-iv',
        'part_name': 'Compressing Images',
        'title': 'Transform Coding & Discrete Cosine Transform',
        'subtitle': 'Energy Compaction Principles, 2D DCT-II Mathematical Formulation, Parseval\'s Energy Conservation, DCT vs DFT vs KLT Comparison, Sub-Image Partitioning, and Zonal/Threshold Quantization',
        'concept_id': '[CONCEPT-DIP-023]',
        'output_file': 'ch23-lossy-dct-jpeg.html',
        'read_time': '~55 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Transform Coding:</strong> Principles of transform coding, energy compaction and decorrelation, 1D and 2D Discrete Cosine Transform (DCT-II), basis functions, properties (orthogonality, symmetry), comparison of DCT with DFT and KLT, selection of sub-image size (8x8 blocks), zonal coding, and threshold coding.',
        'uni_sections': ['23.1', '23.2', '23.3', '23.4', '23.5', '23.6', '23.8', '23.10', '23.12', '23.15', '23.20'],
        'gate_sections': ['23.3', '23.4', '23.5', '23.6', '23.8', '23.10', '23.12'],
        'prev_link': 'ch22-lossless-coding.html',
        'prev_label': '← Ch 22 — Lossless Coding',
        'next_link': 'ch24-wavelets-jpeg2000.html',
        'next_label': 'Next: Ch 24 — JPEG Compression End to End →'
    },
    {
        'id': 'DIP-U3-C24',
        'file': 'DIP_Ch24_JPEG_Compression_End_to_End.md',
        'chapter_num': 24,
        'unit_name': 'Unit III', 'part_num': 'Part IV',
        'part_id': 'part-iv',
        'part_name': 'Compressing Images',
        'title': 'JPEG Compression End to End',
        'subtitle': 'The Complete Baseline Sequential JPEG Standard: YCbCr 4:2:0 Downsampling, $8 \\times 8$ Block DCT, Psychovisual Quantization Matrices, DC DPCM Coding, AC Zigzag Scanning, and Zero-Run Huffman Coding',
        'concept_id': '[CONCEPT-DIP-024]',
        'output_file': 'ch24-wavelets-jpeg2000.html',
        'read_time': '~60 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>The JPEG Compression Standard:</strong> Baseline sequential JPEG architecture, RGB to YCbCr conversion, 4:2:0 chroma subsampling, 8x8 block DCT, quantization tables and quality scaling factor, DC coefficient differential coding, AC coefficient zigzag scanning, run-length amplitude encoding, Huffman coding of intermediate symbols, and overview of wavelet-based JPEG 2000.',
        'uni_sections': ['24.1', '24.2', '24.3', '24.4', '24.5', '24.6', '24.8', '24.10', '24.12', '24.15', '24.20', '24.25'],
        'gate_sections': ['24.2', '24.3', '24.4', '24.5', '24.8', '24.10', '24.12', '24.15'],
        'prev_link': 'ch23-lossy-dct-jpeg.html',
        'prev_label': '← Ch 23 — Transform Coding & DCT',
        'next_link': 'ch25-image-classification.html',
        'next_label': 'Next: Ch 25 — Image Classification Foundations →'
    },
    # ── PART V: INTELLIGENT VISION ──────────────────────────────────
    {
        'id': 'DIP-U5-C25',
        'file': 'DIP_Ch25_Image_Classification.md',
        'chapter_num': 25,
        'unit_name': 'Unit IV', 'part_num': 'Part V',
        'part_id': 'part-v',
        'part_name': 'Intelligent Vision',
        'title': 'Image Classification Foundations',
        'subtitle': 'Feature Space Mapping, Decision Boundaries, Distance Metric Classifiers (k-NN), Linear Classifiers, Softmax & Cross-Entropy Loss, and Regularization',
        'concept_id': '[CONCEPT-DIP-025]',
        'output_file': 'ch25-image-classification.html',
        'read_time': '~50 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Image Classification:</strong> Feature space mapping, decision boundaries, minimum distance classifier, k-Nearest Neighbors (k-NN) classification, linear classifier formulation ($W x + b$), Softmax function and categorical cross-entropy loss, bias-variance tradeoff, overfitting and regularization.',
        'uni_sections': ['25.1', '25.2', '25.3', '25.4', '25.5', '25.6', '25.7', '25.8', '25.10', '25.12', '25.15', '25.20'],
        'gate_sections': ['25.2', '25.3', '25.4', '25.5', '25.6', '25.8', '25.10', '25.12'],
        'prev_link': 'ch24-wavelets-jpeg2000.html',
        'prev_label': '← Ch 24 — JPEG Compression End to End',
        'next_link': 'ch26-cnns-image-processing.html',
        'next_label': 'Next: Ch 26 — Convolutional Neural Networks →'
    },
    {
        'id': 'DIP-U5-C26',
        'file': 'DIP_Ch26_Convolutional_Neural_Networks.md',
        'chapter_num': 26,
        'unit_name': 'Unit IV', 'part_num': 'Part V',
        'part_id': 'part-v',
        'part_name': 'Intelligent Vision',
        'title': 'Convolutional Neural Networks for Image Processing',
        'subtitle': 'From 2D Spatial Filtering to Learnable Kernels, Receptive Fields, Stride & Padding Mathematics, Activation Functions (ReLU, LeakyReLU), Pooling Layers, and Feature Tensor Volumes',
        'concept_id': '[CONCEPT-DIP-026]',
        'output_file': 'ch26-cnns-image-processing.html',
        'read_time': '~60 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Convolutional Neural Networks:</strong> Connection between spatial domain filtering and CNNs, 2D convolution layers, parameter sharing, receptive field calculation, stride and padding formulas ($W_{out} = \\lfloor(W-K+2P)/S\\rfloor+1$), activation functions (Sigmoid, Tanh, ReLU, Leaky ReLU), pooling layers (max, average, global average pooling), and feature map volume transformations.',
        'uni_sections': ['26.1', '26.2', '26.3', '26.4', '26.5', '26.6', '26.7', '26.8', '26.10', '26.12', '26.15', '26.20', '26.25'],
        'gate_sections': ['26.2', '26.3', '26.4', '26.5', '26.6', '26.8', '26.10', '26.12'],
        'prev_link': 'ch25-image-classification.html',
        'prev_label': '← Ch 25 — Image Classification',
        'next_link': 'ch27-modern-vision-architectures.html',
        'next_label': 'Next: Ch 27 — Modern Vision Architectures (VGG & ResNet) →'
    },
    {
        'id': 'DIP-U5-C27',
        'file': 'DIP_Ch27_VGG_and_ResNet.md',
        'chapter_num': 27,
        'unit_name': 'Unit IV', 'part_num': 'Part V',
        'part_id': 'part-v',
        'part_name': 'Intelligent Vision',
        'title': 'Modern Vision Architectures: VGG & ResNet',
        'subtitle': 'Vanishing Gradients in Deep Networks, VGG Small $3 \\times 3$ Kernel Stacking Theorem, Parameter Calculations, ResNet Residual Blocks ($F(x)+x$), Skip Connections, and Transfer Learning',
        'concept_id': '[CONCEPT-DIP-027]',
        'output_file': 'ch27-modern-vision-architectures.html',
        'read_time': '~55 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Deep Vision Architectures:</strong> Architecture depth and degradation problem, VGG-16 and VGG-19 architectural principles, small 3x3 filter factorization theorem, parameter count and FLOPs, ResNet residual learning framework, identity skip connections, mathematical formulation of residual blocks ($H(x) = F(x) + x$), and transfer learning.',
        'uni_sections': ['27.1', '27.2', '27.3', '27.4', '27.5', '27.6', '27.7', '27.8', '27.10', '27.12', '27.15', '27.20'],
        'gate_sections': ['27.2', '27.3', '27.4', '27.5', '27.6', '27.8', '27.10', '27.12'],
        'prev_link': 'ch26-cnns-image-processing.html',
        'prev_label': '← Ch 26 — Convolutional Neural Networks',
        'next_link': 'ch28-object-detection-yolo.html',
        'next_label': 'Next: Ch 28 — Object Detection & YOLO →'
    },
    {
        'id': 'DIP-U5-C28',
        'file': 'DIP_Ch28_Object_Detection_and_YOLO.md',
        'chapter_num': 28,
        'unit_name': 'Unit IV', 'part_num': 'Part V',
        'part_id': 'part-v',
        'part_name': 'Intelligent Vision',
        'title': 'Object Detection & YOLO',
        'subtitle': 'Classification vs Localization vs Detection, Bounding Box Coordinates $[x,y,w,h]$, Intersection over Union (IoU), Non-Maximum Suppression (NMS), YOLO $S \\times S$ Unified Grid Regression, and Multi-Task Loss',
        'concept_id': '[CONCEPT-DIP-028]',
        'output_file': 'ch28-object-detection-yolo.html',
        'read_time': '~60 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Object Detection:</strong> Localization vs detection, bounding box representation, Intersection over Union (IoU), Non-Maximum Suppression (NMS) algorithm, two-stage detectors (R-CNN family) vs single-stage detectors, YOLO (You Only Look Once) grid-based prediction architecture ($S \\times S$ tensor), anchor boxes, multi-part loss function, and mean Average Precision (mAP).',
        'uni_sections': ['28.1', '28.2', '28.3', '28.4', '28.5', '28.6', '28.7', '28.8', '28.10', '28.12', '28.15', '28.20'],
        'gate_sections': ['28.2', '28.3', '28.4', '28.5', '28.6', '28.8', '28.10', '28.12'],
        'prev_link': 'ch27-modern-vision-architectures.html',
        'prev_label': '← Ch 27 — Modern Vision Architectures',
        'next_link': 'ch29-image-denoising-autoencoders.html',
        'next_label': 'Next: Ch 29 — Image Denoising with Autoencoders →'
    },
    {
        'id': 'DIP-U5-C29',
        'file': 'DIP_Ch29_Image_Denoising_with_Autoencoders.md',
        'chapter_num': 29,
        'unit_name': 'Unit IV', 'part_num': 'Part V',
        'part_id': 'part-v',
        'part_name': 'Intelligent Vision',
        'title': 'Image Denoising with Autoencoders',
        'subtitle': 'Encoder-Decoder Architecture, Latent Bottleneck Representation $z$, Convolutional Autoencoders (CAE), Transpose Convolutions, Gaussian & Impulsive Corruption, and Reconstruction Loss',
        'concept_id': '[CONCEPT-DIP-029]',
        'output_file': 'ch29-image-denoising-autoencoders.html',
        'read_time': '~50 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Image Denoising using Autoencoders:</strong> Unsupervised visual learning, encoder-decoder architecture, latent space representation, Convolutional Autoencoder (CAE), upsampling via transposed convolution, artificial noise injection (Gaussian, salt-and-pepper), mean squared error reconstruction loss, and comparison with spatial domain filtering methods.',
        'uni_sections': ['29.1', '29.2', '29.3', '29.4', '29.5', '29.6', '29.7', '29.8', '29.10', '29.12', '29.15', '29.20'],
        'gate_sections': ['29.2', '29.3', '29.4', '29.5', '29.6', '29.8', '29.10', '29.12'],
        'prev_link': 'ch28-object-detection-yolo.html',
        'prev_label': '← Ch 28 — Object Detection & YOLO',
        'next_link': 'ch30-video-motion-analysis.html',
        'next_label': 'Next: Ch 30 — Video Processing & Motion Analysis →'
    },
    {
        'id': 'DIP-U5-C30',
        'file': 'DIP_Ch30_Video_Processing_and_Motion_Analysis.md',
        'chapter_num': 30,
        'unit_name': 'Unit IV', 'part_num': 'Part V',
        'part_id': 'part-v',
        'part_name': 'Intelligent Vision',
        'title': 'Video Processing & Motion Analysis',
        'subtitle': 'Video as Spatiotemporal Volume $I(x,y,t)$, Optical Flow Constraint Equation, Aperture Problem, Lucas-Kanade Dense & Sparse Solutions, Background Subtraction, and OpenCV Tracking (Lab 10)',
        'concept_id': '[CONCEPT-DIP-030]',
        'output_file': 'ch30-video-motion-analysis.html',
        'read_time': '~60 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Introduction to Video Processing & Motion Analysis:</strong> Video representation as 3D spatiotemporal volume, frame differencing, background subtraction (Gaussian Mixture Models MOG2), optical flow brightness constancy assumption, Optical Flow Constraint Equation ($I_x u + I_y v + I_t = 0$), aperture problem, Lucas-Kanade optical flow method, and Practical 10 implementation.',
        'uni_sections': ['30.1', '30.2', '30.3', '30.4', '30.5', '30.6', '30.7', '30.8', '30.10', '30.12', '30.15', '30.20', '30.25'],
        'gate_sections': ['30.2', '30.3', '30.4', '30.5', '30.6', '30.8', '30.10', '30.12'],
        'prev_link': 'ch29-image-denoising-autoencoders.html',
        'prev_label': '← Ch 29 — Image Denoising with Autoencoders',
        'next_link': 'ch31-dip-applications-engineering.html',
        'next_label': 'Next: Ch 31 — DIP Applications & Engineering Context →'
    },
    {
        'id': 'DIP-U5-C31',
        'file': 'DIP_Ch31_Digital_Image_Processing_Applications_and_Engineering_Context.md',
        'chapter_num': 31,
        'unit_name': 'Unit IV', 'part_num': 'Part V',
        'part_id': 'part-v',
        'part_name': 'Intelligent Vision',
        'title': 'DIP Applications, Engineering Context & Responsible Use',
        'subtitle': 'Medical Imaging (CT Hounsfield Units, MRI, X-ray), Satellite Remote Sensing (NDVI), Industrial Visual Inspection, Biometric Verification, Ethical & Responsible AI, and Master Curriculum Synthesis',
        'concept_id': '[CONCEPT-DIP-031]',
        'output_file': 'ch31-dip-applications-engineering.html',
        'read_time': '~55 min read',
        'exam_priority': 'Highest Yield (10-mark guarantee)',
        'uni_syllabus_text': '<strong>Applications & Engineering Context:</strong> Applications in healthcare (computed tomography, MRI artifact removal, automated tumor segmentation), satellite imaging and remote sensing (multispectral processing, NDVI calculation), industrial automated visual inspection, biometric security, ethics and responsible vision AI (bias, deepfakes, privacy), and complete course synthesis.',
        'uni_sections': ['31.1', '31.2', '31.3', '31.4', '31.5', '31.6', '31.7', '31.8', '31.10', '31.12', '31.15', '31.20'],
        'gate_sections': ['31.2', '31.3', '31.4', '31.5', '31.6', '31.8', '31.10', '31.12'],
        'prev_link': 'ch30-video-motion-analysis.html',
        'prev_label': '← Ch 30 — Video Processing & Motion Analysis',
        'next_link': '../index.html',
        'next_label': 'Complete DIP Curriculum Portal 🏛️'
    }
]

ALL_DIP_PARTS = [
    {
        'part_id': 'part-i', 'part_name': 'Part I — The Image',
        'chapters': [
            (1, 'The Big Picture', 'ch01-big-picture.html'),
            (2, 'Formation & Acquisition', 'ch02-image-formation.html'),
            (3, 'Sampling & Quantization', 'ch03-sampling-quantization.html'),
            (4, 'Pixels, Matrices & Resolution', 'ch04-image-representation.html'),
            (5, 'Colour Models & Formats', 'ch05-colour-models-file-formats.html'),
        ]
    },
    {
        'part_id': 'part-ii', 'part_name': 'Part II — Improving the Image',
        'chapters': [
            (6, 'Point Processing & Intensity', 'ch06-point-processing.html'),
            (7, 'Histograms & Equalization', 'ch07-histograms-equalization.html'),
            (8, 'Spatial Filtering & Convolution', 'ch08-spatial-filtering.html'),
            (9, 'Smoothing & Noise Reduction', 'ch09-smoothing-noise-reduction.html'),
            (10, 'Sharpening & Edge Detection', 'ch10-sharpening-edge-detection.html'),
            (11, 'Geometric Transforms', 'ch11-geometric-transforms.html'),
            (12, 'Fourier Transform & Frequency', 'ch12-fourier-transform.html'),
            (13, 'Frequency-Domain Filtering', 'ch13-frequency-filtering.html'),
            (14, 'Restoration & Deblurring', 'ch14-image-restoration.html'),
        ]
    },
    {
        'part_id': 'part-iii', 'part_name': 'Part III — Understanding Content',
        'chapters': [
            (15, 'Segmentation Fundamentals', 'ch15-segmentation-fundamentals.html'),
            (16, 'Thresholding & Otsu Method', 'ch16-thresholding-otsu.html'),
            (17, 'Region-Based Segmentation', 'ch17-region-segmentation.html'),
            (18, 'Mathematical Morphology', 'ch18-mathematical-morphology.html'),
            (19, 'Image Features & Descriptors', 'ch19-features-descriptors.html'),
            (20, 'SIFT, SURF, ORB & HOG', 'ch20-sift-surf-orb-hog.html'),
        ]
    },
    {
        'part_id': 'part-iv', 'part_name': 'Part IV — Compressing Images',
        'chapters': [
            (21, 'Compression & Entropy', 'ch21-compression-entropy.html'),
            (22, 'Lossless: RLE & Huffman', 'ch22-lossless-coding.html'),
            (23, 'Lossy: DCT & JPEG', 'ch23-lossy-dct-jpeg.html'),
            (24, 'Wavelets & JPEG 2000', 'ch24-wavelets-jpeg2000.html'),
        ]
    },
    {
        'part_id': 'part-v', 'part_name': 'Part V — Intelligent Vision',
        'chapters': [
            (25, 'Image Classification', 'ch25-image-classification.html'),
            (26, 'CNNs for Image Processing', 'ch26-cnns-image-processing.html'),
            (27, 'Modern Vision Architectures', 'ch27-modern-vision-architectures.html'),
            (28, 'Object Detection: YOLO', 'ch28-object-detection-yolo.html'),
            (29, 'Image Denoising Autoencoders', 'ch29-image-denoising-autoencoders.html'),
            (30, 'Video & Motion Analysis', 'ch30-video-motion-analysis.html'),
            (31, 'DIP Applications & Ethics', 'ch31-dip-applications-engineering.html'),
        ]
    }
]

def escape_math_and_blocks(text):
    """Protects MathJax formulas and code blocks from Markdown parser corruption."""
    token_map = {}
    counter = [0]

    def make_token(val):
        t = f"%%DIP_TOKEN_{counter[0]}%%"
        counter[0] += 1
        token_map[t] = val
        return t

    # 1. Protect Mermaid diagrams
    def repl_mermaid(m):
        code = m.group(1).strip()
        rendered = f'<div class="diagram-box"><div class="mermaid">\n{code}\n</div></div>'
        return make_token(rendered)
    text = re.sub(r'```mermaid\s*\n(.*?)\n```', repl_mermaid, text, flags=re.DOTALL)

    # 2. Protect Code blocks
    def repl_code(m):
        lang = m.group(1).strip() if m.group(1) else 'text'
        code = m.group(2)
        escaped_code = html.escape(code)
        rendered = f'''<div class="code-block">
  <div class="code-header">
    <span>{lang}</span>
    <button class="code-copy-btn">📋 Copy</button>
  </div>
  <pre><code>{escaped_code}</code></pre>
</div>'''
        return make_token(rendered)
    text = re.sub(r'```([a-zA-Z0-9_\-\+]*)\s*\n(.*?)\n```', repl_code, text, flags=re.DOTALL)

    # 3. Protect display math $$ ... $$ and \[ ... \]
    def repl_display_math(m):
        return make_token(f"\n$${m.group(1)}$$\n")
    text = re.sub(r'\$\$(.*?)\$\$', repl_display_math, text, flags=re.DOTALL)
    text = re.sub(r'\\\[(.*?)\\\]', repl_display_math, text, flags=re.DOTALL)

    # 4. Protect inline math $ ... $ and \( ... \)
    def repl_inline_math(m):
        content = m.group(1).strip()
        return make_token(f"${content}$")
    text = re.sub(r'(?<!\$)\$([^\$\n]+?)\$(?!\$)', repl_inline_math, text)
    text = re.sub(r'\\\((.*?)\\\)', repl_inline_math, text)

    return text, token_map

def restore_tokens(html_content, token_map):
    """Restores saved tokens back into the final HTML."""
    for token, val in token_map.items():
        html_content = html_content.replace(token, val)
    return html_content

def post_process_html(html_text):
    """Wraps tables with responsive div and applies comparison-table class."""
    def repl_table(m):
        table_code = m.group(0)
        table_code = re.sub(r'<table>', '<table class="comparison-table">', table_code)
        return f'<div class="table-wrap">{table_code}</div>'
    return re.sub(r'<table>.*?</table>', repl_table, html_text, flags=re.DOTALL)

def build_chapter(md_path, meta):
    """Reads complete manuscript markdown, parses all sections, and outputs exhaustive HTML."""
    with open(md_path, 'r', encoding='utf-8') as f:
        raw_md = f.read()

    # Split into sections based on # 0X.Y or ## 0X.Y
    sec_regex = re.compile(r'^(#+\s+\d+\.\d+.*?)(?=\n#+\s+\d+\.\d+|\Z)', re.MULTILINE | re.DOTALL)

    first_sec_match = re.search(r'\n#+\s+\d+\.\d+', raw_md)
    if first_sec_match:
        preamble = raw_md[:first_sec_match.start()]
        body = raw_md[first_sec_match.start():]
    else:
        preamble = ""
        body = raw_md

    # Clean YAML frontmatter
    preamble = re.sub(r'^---\s*\n.*?\n---\s*\n', '', preamble, flags=re.DOTALL)

    raw_sections = sec_regex.findall(body)
    print(f"[{meta['id']}] Processing {len(raw_sections)} numbered sections...")

    sections_data = []
    sidebar_links = []
    toc_items = []

    for idx, sec_text in enumerate(raw_sections):
        lines = sec_text.strip().split('\n')
        h_line = lines[0]
        m = re.match(r'^#+\s+(\d+\.\d+)\s*(.*)$', h_line)
        if m:
            sec_num_str = m.group(1).strip()
            sec_title = m.group(2).strip()
        else:
            sec_num_str = f"{meta['chapter_num']:02d}.{idx+1}"
            sec_title = h_line.replace('#', '').strip()

        sec_id = f"s-{sec_num_str.replace('.', '-')}"
        content_md = '\n'.join(lines[1:]).strip()

        # 1. Transform Teacher Notes / Hinglish
        def transform_teacher_hinglish(text):
            parts = re.split(r'(### (?:Hinglish|Teacher explanation — Hinglish|Teacher explanation|Intuition)[^\n]*\n)', text)
            if len(parts) == 1:
                return text
            out = [parts[0]]
            for i in range(1, len(parts), 2):
                hdr = parts[i].replace('###', '').strip()
                block = parts[i+1]
                subparts = re.split(r'(\n(?:###|---|\Z))', block, maxsplit=1)
                t_content = subparts[0].strip()
                rest = ''.join(subparts[1:])
                out.append(f'\n\n<div class="teacher-box"><div class="teacher-title"><span>👨‍🏫</span> {hdr} <span class="hinglish-tag">Teacher Note</span></div>\n\n{t_content}\n\n</div>\n\n{rest}')
            return ''.join(out)
        content_md = transform_teacher_hinglish(content_md)

        # 2. Transform Misconceptions / Traps / Warnings
        def transform_traps(text):
            parts = re.split(r'(### (?:Misconception|Mistake|Pitfall|Warning|Common Trap|Common conceptual trap)[^\n]*\n)', text, flags=re.IGNORECASE)
            if len(parts) == 1:
                return text
            out = [parts[0]]
            for i in range(1, len(parts), 2):
                hdr = parts[i].replace('###', '').strip()
                block = parts[i+1]
                subparts = re.split(r'(\n(?:###|---|\Z))', block, maxsplit=1)
                m_content = subparts[0].strip()
                rest = ''.join(subparts[1:])
                out.append(f'\n\n<div class="trap-box"><div class="trap-title"><span>⚠️</span> {hdr}</div>\n\n{m_content}\n\n</div>\n\n{rest}')
            return ''.join(out)
        content_md = transform_traps(content_md)

        # 3. Transform Worked Examples
        def transform_worked_examples(text):
            parts = re.split(r'(### (?:Worked Example|Tiny worked example|Step-by-step calculation)[^\n]*\n)', text, flags=re.IGNORECASE)
            if len(parts) == 1:
                return text
            out = [parts[0]]
            for i in range(1, len(parts), 2):
                hdr = parts[i].replace('###', '').strip()
                block = parts[i+1]
                subparts = re.split(r'(\n(?:###|---|\Z))', block, maxsplit=1)
                w_content = subparts[0].strip()
                rest = ''.join(subparts[1:])
                out.append(f'\n\n<div class="worked-example"><div class="worked-example-header"><span class="worked-example-title"><span>🧮</span> {hdr}</span><span class="tag-badge tag-exam">NUMERICAL WORKTHROUGH</span></div>\n\n{w_content}\n\n</div>\n\n{rest}')
            return ''.join(out)
        content_md = transform_worked_examples(content_md)

        # 4. Transform Review Questions / Exam Ladders
        def transform_review_questions(text):
            parts = re.split(r'(### (?:Review questions|\d+-mark question|Self-Assessment)[^\n]*\n)', text, flags=re.IGNORECASE)
            if len(parts) == 1:
                return text
            out = [parts[0]]
            for i in range(1, len(parts), 2):
                hdr = parts[i].replace('###', '').strip()
                block = parts[i+1]
                subparts = re.split(r'(\n(?:###|---|\Z))', block, maxsplit=1)
                q_content = subparts[0].strip()
                rest = ''.join(subparts[1:])
                out.append(f'\n\n<div class="exam-connection"><div class="exam-title"><span>📝</span> {hdr}</div>\n\n{q_content}\n\n</div>\n\n{rest}')
            return ''.join(out)
        content_md = transform_review_questions(content_md)

        # 5. Protect math & blocks
        proc_md, token_map = escape_math_and_blocks(content_md)

        # 6. Convert to HTML
        sec_html = markdown.markdown(proc_md, extensions=['tables', 'fenced_code'])

        # 7. Restore tokens
        sec_html = restore_tokens(sec_html, token_map)
        sec_html = post_process_html(sec_html)

        sections_data.append({
            'num': sec_num_str,
            'id': sec_id,
            'title': sec_title,
            'html': sec_html
        })

        badge = ""
        if sec_num_str in meta.get('uni_sections', []):
            badge = '<span class="tag-badge tag-core" style="font-size:0.65rem; padding:1px 5px;">Uni Core</span>'
        elif sec_num_str in meta.get('gate_sections', []):
            badge = '<span class="tag-badge tag-math" style="font-size:0.65rem; padding:1px 5px;">Analytical</span>'

        sidebar_links.append(
            f'<a href="#{sec_id}" class="sidebar-link"><span class="link-icon">📌</span><span>{sec_num_str} {html.escape(sec_title)}</span> {badge}</a>'
        )

        toc_items.append(
            f'<li class="part-chapter-item"><a href="#{sec_id}"><strong>{sec_num_str}</strong> {html.escape(sec_title)}</a> {badge}</li>'
        )

    # Render Preamble if present
    preamble_html = ""
    if preamble.strip():
        p_proc, p_tokens = escape_math_and_blocks(preamble)
        p_html = markdown.markdown(p_proc, extensions=['tables', 'fenced_code'])
        p_html = restore_tokens(p_html, p_tokens)
        p_html = post_process_html(p_html)
        preamble_html = f'<div class="concept-hook" style="margin-bottom:var(--em-space-8);">{p_html}</div>'

    sidebar_sections_html = '\n      '.join(sidebar_links)
    toc_items_html = '\n      '.join(toc_items)

    sections_rendered_html = []
    for s in sections_data:
        rendered = f'''
  <!-- SECTION {s['num']}: {html.escape(s['title'])} -->
  <section id="{s['id']}" class="section-block">
    <div class="section-header">
      <span class="section-num">{s['num']}</span>
      <h2>{html.escape(s['title'])}</h2>
      <button class="bookmark-btn" data-id="{s['id']}" title="Bookmark this section" aria-label="Bookmark section">📌</button>
    </div>
    <div class="section-body">
      {s['html']}
    </div>
  </section>'''
        sections_rendered_html.append(rendered)

    all_sections_str = '\n'.join(sections_rendered_html)

    # Build Master Sidebar across all 5 Parts (31 chapters)
    master_sidebar_parts = []
    for part in ALL_DIP_PARTS:
        ch_links = []
        for ch_num, ch_title, ch_file in part['chapters']:
            active = ' active' if meta['chapter_num'] == ch_num else ''
            ch_links.append(f'<a href="{ch_file}" class="sidebar-link{active}"><span class="link-icon">{ch_num:02d}</span><span>{ch_title}</span></a>')
        ch_links_str = '\n      '.join(ch_links)
        master_sidebar_parts.append(f'''
    <div class="sidebar-section">
      <div class="sidebar-section-label part-label {part['part_id']}">{part['part_name']}</div>
      {ch_links_str}
    </div>''')
    master_sidebar_parts_str = '\n'.join(master_sidebar_parts)

    page_html = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="author" content="Arpit">
  <meta name="description" content="Chapter {meta['chapter_num']:02d}: {html.escape(meta['title'])} — Digital Image Processing MiniBook. {html.escape(meta['subtitle'])}">
  <title>C{meta['chapter_num']:02d}: {html.escape(meta['title'])} | DIP MiniBook 📷 Arpit</title>

  <link rel="stylesheet" href="../assets/css/main.css">
  <link rel="stylesheet" href="../assets/css/components.css">
  <link rel="stylesheet" href="../assets/css/chapters.css">
  <link rel="stylesheet" href="../assets/css/animations.css">
  <link rel="stylesheet" href="../assets/css/timer.css">

  <script>
    window.MathJax = {{
      tex: {{
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
      }},
      svg: {{ fontCache: 'global' }}
    }};
  </script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body data-chapter-id="{meta['output_file'].replace('.html', '')}">
  <div id="progress-bar"></div>

  <!-- Header -->
  <header id="main-header">
    <div class="header-left">
      <button id="sidebar-toggle" class="icon-btn" aria-label="Toggle navigation drawer" title="Toggle Sidebar (S)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="3" y1="12" x2="21" y2="12"></line>
          <line x1="3" y1="6" x2="21" y2="6"></line>
          <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
      </button>
      <a href="../index.html" class="brand-logo">
        <div class="brand-icon">DIP</div>
        <div class="brand-text">
          <span class="main">Digital Image Processing</span>
          <span class="sub">DU DSE-3 Engineering MiniBook</span>
        </div>
      </a>
    </div>

    <div class="header-chapter-title">C{meta['chapter_num']:02d}: {html.escape(meta['title'])}</div>

    <div class="header-right">
      <button id="reading-mode-btn" class="icon-btn" aria-label="Toggle reading focus mode" title="Focus Mode (F)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
          <line x1="8" y1="21" x2="16" y2="21"></line>
          <line x1="12" y1="17" x2="12" y2="21"></line>
        </svg>
      </button>
      <button id="tts-toggle" class="icon-btn" aria-label="Audio Reader" title="Audio Reader">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
          <path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>
          <path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path>
        </svg>
      </button>
      <button id="theme-toggle" class="icon-btn" aria-label="Cycle theme" title="Theme (T)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
          <circle cx="12" cy="12" r="4.5"></circle>
          <path d="M12 2v2M12 20v2M4.93 4.93l1.42 1.42M17.65 17.65l1.42 1.42M2 12h2M20 12h2M4.93 19.07l1.42-1.42M17.65 6.35l1.42-1.42"></path>
        </svg>
      </button>
    </div>
  </header>

  <!-- Sidebar Overlay -->
  <div id="sidebar-overlay"></div>

  <!-- Sidebar -->
  <aside id="sidebar" aria-expanded="true">
    <div class="sidebar-nav">
      <div class="sidebar-section">
        <div class="sidebar-section-label">General</div>
        <a href="../index.html" class="sidebar-link">
          <span class="link-icon">🏛️</span>
          <span>Subject Portal</span>
        </a>
        <a href="../progress.html" class="sidebar-link">
          <span class="link-icon">📊</span>
          <span>Study Dashboard</span>
        </a>
      </div>

      <div class="sidebar-section">
        <div class="sidebar-section-label">Current Chapter Sections</div>
        {sidebar_sections_html}
      </div>

      {master_sidebar_parts_str}
    </div>

    <div class="sidebar-footer">
      <div class="sidebar-brand-mark">
        <div class="mark">DU</div>
        <div>
          <strong>DSE-3 MiniBook</strong>
          <div>University of Delhi</div>
        </div>
      </div>
    </div>
  </aside>

  <!-- Mandatory Shell Wrapper -->
  <div id="main-content">
    <main class="chapter-content">
      <!-- Chapter Hero -->
      <div class="chapter-hero">
        <div class="hero-meta">
          <span class="unit-badge {'unit-badge-u1' if meta['unit_name'] == 'Unit I' else 'unit-badge-u2' if meta['unit_name'] == 'Unit II' else 'unit-badge-u3' if meta['unit_name'] == 'Unit III' else 'unit-badge-u4'}">🎓 {meta['unit_name']}</span>
          <span class="part-badge {meta['part_id']}">{meta['part_name']}</span>
          <span class="chapter-number">CHAPTER {meta['chapter_num']:02d}</span>
          <span class="reading-time">⏱️ {meta['read_time']}</span>
          <span class="tag-badge tag-core">{meta['exam_priority']}</span>
        </div>
        <h1 class="chapter-title">{html.escape(meta['title'])}</h1>
        <p class="chapter-subtitle">
          {html.escape(meta['subtitle'])}
        </p>

        <div class="syllabus-anchor">
          <div class="syllabus-anchor-header">
            <span class="syllabus-anchor-label">🎓 DU DSE-3 Syllabus Alignment</span>
            <span class="unit-badge {'unit-badge-u1' if meta['unit_name'] == 'Unit I' else 'unit-badge-u2' if meta['unit_name'] == 'Unit II' else 'unit-badge-u3' if meta['unit_name'] == 'Unit III' else 'unit-badge-u4'}">{meta['unit_name']}</span>
          </div>
          <span>{meta['uni_syllabus_text']}</span>
        </div>
      </div>

      <!-- In-Page TOC -->
      <div class="chapter-checklist-card" style="margin-bottom:var(--em-space-8);">
        <div class="checklist-title">
          <span>Table of Contents &amp; Visual Section Map</span>
          <span class="tag-badge tag-math">{len(sections_data)} Deep Sections</span>
        </div>
        <ul class="part-chapters-list">
          {toc_items_html}
        </ul>
      </div>

      {preamble_html}

      <!-- All Numbered Sections -->
      {all_sections_str}

      <!-- Chapter End Package -->
      <section class="chapter-end-package">
        <div class="chapter-nav-grid">
          <a href="{meta['prev_link']}" class="chapter-nav-card">
            <div class="chapter-nav-dir">← Previous</div>
            <div class="chapter-nav-title">{meta['prev_label']}</div>
          </a>
          <a href="{meta['next_link']}" class="chapter-nav-card next">
            <div class="chapter-nav-dir">Next →</div>
            <div class="chapter-nav-title">{meta['next_label']}</div>
          </a>
        </div>
      </section>
    </main>
  </div>

  <script src="../assets/js/state.js"></script>
  <script src="../assets/js/core.js"></script>
  <script src="../assets/js/tts.js"></script>
  <script src="../assets/js/glossary.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      mermaid.initialize({{
        startOnLoad: true,
        theme: document.documentElement.getAttribute('data-theme') === 'light' ? 'default' : 'dark'
      }});
    }});
  </script>
</body>
</html>
'''

    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'chapters', meta['output_file'])
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(page_html)

    print(f"Generated {meta['output_file']} ({len(page_html)} bytes, {page_html.count(chr(10))} lines) with {len(sections_data)} sections.")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sources_dir = os.path.join(base_dir, 'content-sources', 'main')

    print(f"=== COMPILING DIP PART I CHAPTERS (C01 - C05) ===")
    for meta in CHAPTERS_META:
        md_file = os.path.join(sources_dir, meta['file'])
        if os.path.exists(md_file):
            build_chapter(md_file, meta)
        else:
            print(f"ERROR: Manuscript {md_file} not found!")

    print(f"=== COMPILATION COMPLETE ===")
