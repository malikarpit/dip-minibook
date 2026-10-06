# DIP MiniBook — File Map

Where every collected source lives and what role it plays. Update this file whenever a file is added, moved, or superseded.
Folder layout mirrors the AIML MiniBook (`content-sources/`, `design-docs/`, `master/sources/`, `practicals/`).

## Folder Layout

| Folder | Purpose |
|---|---|
| `design-docs/` | Specification and design-system documents (how the book is built) |
| `master/sources/` | MASTER-00…05 control documents (index, maps, trackers, QA) |
| `content-sources/main/` | Main conceptual book: master TOC + chapter sources (C01–C31) |
| `content-sources/math/` | Math Companion layer sources |
| `content-sources/coding/` | Coding Lab layer sources |
| `content-sources/lab/` | Laboratory / practical system sources |
| `content-sources/exam/` | Exam suite sources |
| `content-sources/practice/` | Practice and transfer sources |
| `content-sources/resources/` | Resource map and visual asset manifest |
| `practicals/` | Practical files received (university/friend submissions) |
| `references/` | Syllabus and reference textbook |

## Files

### design-docs/
| File | Role |
|---|---|
| `DIP_Minibook_Master_Specification_v1.0.md` | Top-level master specification |
| `DIP_DESIGN-01_Visual_Design_System.md` | Visual design system |
| `DIP_DESIGN-02_Content_and_Teaching_System.md` | Content and teaching system |
| `DIP_DESIGN-03_Resource_and_Citation_System.md` | Resource and citation system |
| `DIP_DESIGN-04_Cross-Book_Integration_System.md` | Cross-layer integration system |

### master/sources/
| File | Role |
|---|---|
| `DIP_MASTER-00_Integrated_System_Index_and_Gap_Audit.md` | Integrated index and gap audit |
| `DIP_MASTER-01_Cross-Book_Map_and_Dependency_Graph.md` | Cross-layer map and dependency graph |
| `DIP_MASTER-02_Mastery_and_Progress_Tracker.md` | Mastery and progress tracker |
| `DIP_MASTER-03_Practice_and_Transfer_Index.md` | Practice and transfer index |
| `DIP_MASTER-04_Resource_and_Citation_Index.md` | Resource and citation index |
| `DIP_MASTER-05_Final_QA_Release_and_Print_Digital_Checklist.md` | Final QA / release checklist |

### content-sources/main/ (20 Chapters Collected · 22 Files)
| File | Chapter & Title |
|---|---|
| `DIP_MAIN-00_Master_TOC_and_Learning_Map.md` | Master TOC: 5 parts, 31 chapters (C01–C31) |
| `DIP_Ch01_Digital_Image_Processing_The_Big_Picture.md` | C01 — version A (27,059 B) |
| `DIP_Ch01_Digital_Image_Processing_The_Big_Picture-2.md` | C01 — version B (22,183 B) |
| `DIP_Ch02_Image_Formation_and_Acquisition.md` | C02 — version A (27,504 B) |
| `DIP_Ch02_Image_Formation_and_Acquisition-2.md` | C02 — version B (20,606 B) |
| `DIP_Ch03_Sampling_and_Quantization.md` | C03 — Sampling and Quantization (23,469 B) |
| `DIP_Ch04_Image_Representation_Pixels_Matrices_Tensors_and_Resolution.md` | C04 — Image Representation: Pixels, Matrices, Tensors and Resolution (22,070 B) |
| `DIP_Ch05_Colour_Models_and_Image_File_Formats.md` | C05 — Colour Models and Image File Formats (23,160 B) |
| `DIP_Ch06_Point_Processing_and_Intensity_Transformations.md` | C06 — Point Processing and Intensity Transformations (22,898 B) |
| `DIP_Ch07_Histograms_and_Contrast_Enhancement.md` | C07 — Histograms and Contrast Enhancement (20,990 B) |
| `DIP_Ch08_Spatial_Filtering_and_Convolution.md` | C08 — Spatial Filtering and Convolution (29,364 B) |
| `DIP_Ch09_Smoothing_and_Noise_Reduction.md` | C09 — Smoothing and Noise Reduction (25,285 B) |
| `DIP_Ch10_Sharpening_and_Edge_Detection.md` | C10 — Sharpening and Edge Detection (23,889 B) |
| `DIP_Ch11_Geometric_Transformations_and_Interpolation.md` | C11 — Geometric Transformations and Interpolation (26,230 B) |
| `DIP_Ch12_Fourier_Transform_and_the_Frequency_Domain.md` | C12 — Fourier Transform and the Frequency Domain (29,317 B) |
| `DIP_Ch13_Frequency_Domain_Filtering.md` | C13 — Frequency-Domain Filtering (29,102 B) |
| `DIP_Ch14_Image_Restoration_and_Deblurring.md` | C14 — Image Restoration and Deblurring (26,068 B) |
| `DIP_Ch15_Image_Segmentation_Fundamentals.md` | C15 — Image Segmentation Fundamentals (26,440 B) |
| `DIP_Ch16_Thresholding.md` | C16 — Thresholding (23,514 B) |
| `DIP_Ch17_Region_Based_Segmentation.md` | C17 — Region-Based Segmentation (24,506 B) |
| `DIP_Ch18_Mathematical_Morphology.md` | C18 — Mathematical Morphology (25,200 B) |
| `DIP_Ch19_Image_Features_and_Descriptors.md` | C19 — Image Features and Descriptors (38,590 B) |
| `DIP_Ch20_SIFT_SURF_ORB_and_HOG.md` | C20 — SIFT, SURF, ORB and HOG (29,093 B) |

> **Note on C01/C02:** The `-2` files differ from the originals. Both are kept safe until you decide which version to designate as canonical.

### Other layers (one foundation file each so far)
| File | Layer |
|---|---|
| `content-sources/math/DIP_MATH-00_Mathematics_Companion_Foundation_and_Learning_Map.md` | Math |
| `content-sources/coding/DIP_CODE-00_Coding_Environment_and_Conventions.md` | Coding |
| `content-sources/lab/DIP_LAB-00_Laboratory_Practical_and_Implementation_System.md` | Lab |
| `content-sources/exam/DIP_EXAM-00_Exam_System_and_Revision_Architecture.md` | Exam |
| `content-sources/practice/DIP_PRACTICE-00_Practice_and_Transfer_System.md` | Practice |
| `content-sources/resources/DIP_RESOURCE-00_Master_Resource_Map.md` | Resources |
| `content-sources/resources/DIP_ASSET-00_Visual_Asset_System_and_Manifest.md` | Visual assets |

### practicals/ and references/
| File | Role |
|---|---|
| `practicals/DIP_Practical_1.pdf` | Practical 1 (not yet reviewed) |
| `references/dip.md` | Syllabus extract — Digital Image Processing (DSE-3) |
| `references/Gonzales,Woods-Digital.Image.Processing.4th.Edition.pdf` | Reference textbook (Gonzalez & Woods, 4th ed.) |
