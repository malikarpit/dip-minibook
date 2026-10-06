**ENGINEERING MINIBOOKS**

# Digital Image Processing

Master Content & Learning Architecture

Version 1.0  ·  Scope locked  ·  Prototype-ready

> **DESIGN DECISION Rebuild the DIP MiniBook as a visual engineering textbook: every major concept moves from intuition to image, matrix, mathematics, worked example, implementation, interpretation, limitations, and exam/lab relevance.**

| Dimension | Decision |
| --- | --- |
| Primary purpose | Teach DIP deeply while remaining tightly traceable to the University of Delhi syllabus. |
| Primary product | Responsive interactive website; PDF is a deliberate print derivative. |
| Learning style | Visual + mathematical + algorithmic + practical + exam-oriented. |
| Depth | Syllabus-complete, with clearly labelled extension material. |
| Reference system | Same universal Engineering Minibooks design language as AIML/CN. |
| Prototype unit | Chapters 01–02 establish the content and presentation standard for the rest of the title. |

## SOURCE BASIS

The supplied university syllabus is the scope authority. It defines the course objectives, outcomes, four units, suggested readings, and ten suggested practical experiments. This specification preserves that scope while defining a deeper teaching architecture around it.

Source note: the supplied syllabus shows Practical = 1 in the credit-distribution table and P = 02 in the Course Hours line. These refer to different quantities (credit allocation versus course hours), so this is not treated as an error. The MiniBook will preserve both values with their original labels.

## 0. Specification Map

| Section | Purpose |
| --- | --- |
| 1. Authority & Scope Lock | What counts as authoritative; how syllabus and extensions are handled. |
| 2. Content Architecture | Parts, chapter map, cross-cutting layers and chapter dependencies. |
| 3. Chapter Anatomy | Exact internal structure every major chapter follows. |
| 4. Visual & Information System | Images, diagrams, matrices, tables, pipelines and visual evidence. |
| 5. Mathematical Teaching System | Formula conventions, worked examples and numerical QA. |
| 6. Practical & Implementation System | MATLAB/Python/OpenCV integration and reproducibility. |
| 7. Content QA & Error Control | Checks designed to catch conceptual, mathematical and implementation errors. |
| 8. DIP-Specific Fact & Terminology Rules | Known areas where wording easily creates misconceptions. |
| 9. Production Plan | Prototype, chapter batches and release gates. |
| 10. Definition of Done | Acceptance criteria for the MiniBook as a whole. |

## 1. Authority & Scope Lock

### 1.1 Source hierarchy

- University syllabus = mandatory scope. A syllabus topic must be covered, even when it is not the most elegant way to structure the chapter sequence.

- Established mathematical/technical definitions = accuracy authority for explanations and worked examples.

- Engineering Minibooks design system = presentation authority.

- Extension material = allowed only when it strengthens understanding or professional relevance and is visibly marked as extension.

- Implementation details = must match the stated tool/version/assumptions; code is never allowed to contradict the mathematics.

> **CONTENT STATUS TAGS Use a visible tag system: CORE (syllabus-essential), EXAM (high-yield exam lens), LAB (direct practical connection), DEEP DIVE (more rigorous explanation), and EXTENSION (useful beyond the syllabus).**

### 1.2 Current-stage bug / risk ledger

| Risk | Failure mode | Design control |
| --- | --- | --- |
| Shallow definitions | A topic is technically defined but not understood. | Require intuition + visual + worked example + interpretation for major concepts. |
| Formula orphaning | Equations appear without meaning or numerical context. | Every important formula gets variable definitions, assumptions and a worked example. |
| Image/text disconnect | Figures show outputs without explaining the data transformation. | Use original → operation → result → interpretation sequences. |
| Matrix invisibility | Algorithms feel abstract because pixel arithmetic is skipped. | Use small, hand-solvable matrices for local operations. |
| Pipeline fragmentation | Students memorize stages without knowing how a real system fits together. | Use master pipelines and per-application pipelines. |
| Terminology drift | Common words such as resolution, convolution and compression are used loosely. | Maintain the DIP-specific terminology rules in Section 8. |
| Tool mismatch | Code silently assumes different channel order, range or datatype. | State implementation conventions explicitly and run code QA. |
| Model ambiguity | A family name such as YOLO is treated as one frozen implementation. | Name the concrete implementation/version used for each practical. |
| Exam-only optimization | Notes become lists of memorisable points without conceptual depth. | Keep EXAM content as a layer over the main explanation, not as the main explanation. |
| Layout fragmentation | Headings or table headers are stranded at page bottoms. | Use page-break/keep-together rules and visual QA before release. |

### 1.3 Syllabus coverage lock

| Unit | Syllabus scope | MiniBook treatment |
| --- | --- | --- |
| I | Fundamentals; image formation; sampling and quantization; grayscale/RGB/multispectral; pixels, bit depth, resolution; RGB/HSV/CMY/YUV; BMP/JPEG/PNG/TIFF. | Parts I, Chapters 01–05. Expand the image as physical signal → sampled/quantized data → matrix/tensor → colour representation → stored file. |
| II | Spatial enhancement; histogram equalization; smoothing, sharpening, edge detection; Fourier/frequency techniques; LP/HP/BP filters; noise reduction and restoration. | Part II, Chapters 06–14. Every filter gets intuition + kernel/matrix + worked example + visual before/after + limitations. |
| III | Segmentation; global/adaptive thresholding; region methods; morphology; SIFT/SURF/HOG; lossless/lossy compression; JPEG. | Parts III–IV, Chapters 15–24. Strong algorithm comparisons, matrices, shape diagrams, feature visualizations, compression pipeline and numerical examples. |
| IV | Classification/object detection; CNNs; VGG/ResNet/YOLO; autoencoder denoising; healthcare/surveillance; video and motion analysis. | Part V, Chapters 25–31. Connect classical DIP to learned features, detection and motion, without pretending that all methods are interchangeable. |

### 1.3 Practical scope lock

| Lab | Required activity | MiniBook integration |
| --- | --- | --- |
| 01 | Image I/O and colour-space conversion | Chapter 05 + Lab panel + data-type/channel-order notes. |
| 02 | Histogram and spatial enhancement | Chapters 07–10 with before/after evidence. |
| 03 | Fourier / frequency filtering | Chapters 12–13 with spectrum visualizations. |
| 04 | Noise removal | Chapters 09 and 14; compare filters against noise type. |
| 05 | Segmentation and morphology | Chapters 15–18 with binary matrices. |
| 06 | SIFT, SURF, HOG | Chapters 19–20 with descriptor pipeline. |
| 07 | JPEG | Chapters 21–24 with full compression pipeline. |
| 08 | CNN/MNIST | Chapters 25–26 with tensor shapes and feature maps. |
| 09 | YOLO | Chapter 28 with detection anatomy and explicit model/version lab note. |
| 10 | Optical flow / motion tracking | Chapter 30 with frame-to-frame motion explanation. |

## 2. Content Architecture

### 2.1 Master learning arc

```text
WORLD
  ↓
Image formation / acquisition
  ↓
Sampling + quantization
  ↓
Digital image = structured numerical data
  ↓
Representation / colour / storage
  ↓
Processing domains and tasks
  ├──→ Spatial-domain enhancement / filtering
  ├──→ Frequency-domain analysis / filtering
  └──→ Restoration
          ↓
      Segmentation
          ↓
      Features / descriptors
          ├──→ Compression (when storage/transmission is the goal)
          └──→ Classification / detection / learned representation
                         ↓
                   Video + motion
                         ↓
                Application / decision
```

> **CENTRAL IDEA DIP should read as a progression of representations and operations, not as a bag of algorithms. Each new chapter should answer what information is being represented, changed, removed, preserved, or extracted.**

### 2.2 Chapter map

| ID | Title |
| --- | --- |
| PART I — THE IMAGE |  |
| 01 | Digital Image Processing: The Big Picture |
| 02 | Image Formation and Acquisition |
| 03 | Sampling and Quantization |
| 04 | Image Representation: Pixels, Matrices, Tensors and Resolution |
| 05 | Colour Models and Image File Formats |
| PART II — MAKING IMAGES BETTER |  |
| 06 | Point Processing and Intensity Transformations |
| 07 | Histograms and Contrast Enhancement |
| 08 | Spatial Filtering and Convolution |
| 09 | Smoothing and Noise Reduction |
| 10 | Sharpening and Edge Detection |
| 11 | Geometric Transformations and Interpolation |
| 12 | Fourier Transform and the Frequency Domain |
| 13 | Frequency-Domain Filtering |
| 14 | Image Restoration and Deblurring |
| PART III — UNDERSTANDING IMAGE CONTENT |  |
| 15 | Segmentation Fundamentals |
| 16 | Thresholding: Global and Adaptive |
| 17 | Region-Based Segmentation |
| 18 | Mathematical Morphology |
| 19 | Image Features and Descriptors |
| 20 | SIFT, SURF, ORB and HOG |
| PART IV — COMPRESSING IMAGES |  |
| 21 | Image Compression Fundamentals |
| 22 | Entropy, RLE and Huffman Coding |
| 23 | Transform Coding and DCT |
| 24 | JPEG Compression End to End |
| PART V — FROM DIP TO INTELLIGENT VISION |  |
| 25 | Image Classification |
| 26 | CNN Fundamentals |
| 27 | VGG and ResNet |
| 28 | Object Detection and YOLO |
| 29 | Image Denoising with Autoencoders |
| 30 | Video Processing and Motion Analysis |
| 31 | DIP in Healthcare, Surveillance and Other Applications |

### 2.3 Appendices

| Appendix | Purpose |
| --- | --- |
| A | MATLAB DIP Toolkit |
| B | Python/OpenCV Toolkit |
| C | Matrix Operations Refresher for DIP |
| D | Formula & Numerical Quick Sheet |
| E | DIP Terminology / Glossary |
| F | Viva + Exam Question Bank |
| G | Practical Experiment - Chapter Map |
| H | Troubleshooting / Common Implementation Errors |

## 3. Chapter Anatomy

### 3.1 Standard chapter sequence

| Step | Component | Rule |
| --- | --- | --- |
| 01 | Chapter opener | A one-sentence thesis, visual motif and “why this matters”. |
| 02 | Learning objectives | What the reader should be able to explain, calculate, implement and interpret. |
| 03 | Prerequisite bridge | Only prerequisites genuinely needed for this chapter. |
| 04 | Conceptual model | Plain-language explanation before equations. |
| 05 | Visual model | Diagram, image, pipeline, geometry or representation. |
| 06 | Mathematical core | Definitions, notation, assumptions and equations. |
| 07 | Worked example | Small, fully solved numerical/image example. |
| 08 | Algorithm / procedure | Step-by-step procedure or pseudocode. |
| 09 | Implementation | MATLAB first when aligned with the lab; Python/OpenCV where useful. |
| 10 | Interpret the result | Explain the visual output, not merely display it. |
| 11 | Engineering insight | Trade-offs, limitations, edge cases, failure modes. |
| 12 | Exam + viva lens | Definitions, comparisons, short answers, derivations and likely traps. |
| 13 | Connection forward | Why the next chapter exists; how the concept will be reused. |
| 14 | Chapter checkpoint | A small retrieval exercise / mini-problem before moving on. |

### 3.2 Explanation density

| Topic type | Minimum depth |
| --- | --- |
| Definition | Definition + intuition + one concrete example + one non-example if confusion is likely. |
| Algorithm | Goal → input/output → intuition → steps → pseudocode → example → complexity/limitations where meaningful → implementation. |
| Formula | Meaning → variable definitions → derivation/justification when appropriate → worked numerical example → interpretation. |
| Matrix operation | Matrix setup → alignment → element-by-element operation → output matrix → visual/semantic interpretation. |
| Image operation | Before → operation → after → what changed → why → where it fails. |
| Comparison | Use a table with criteria that answer real engineering questions, not just feature lists. |

## 4. Visual & Information System

### 4.1 Visual primitives

| Primitive | Required behaviour |
| --- | --- |
| Image pair | Whenever a transformation is taught, show original and result with identical scale/crop where practical. |
| Difference image | Use when it reveals what an algorithm removed, added or altered. |
| Pixel grid | Use for sampling, point processing, convolution, morphology and thresholding. |
| Matrix card | Show small numeric matrices for mathematically important local operations. |
| Histogram | Show intensity distribution when contrast/intensity operations are central. |
| Frequency spectrum | Show magnitude spectrum before/after frequency filtering. |
| Pipeline | Use for multi-stage workflows such as JPEG, CNN inference and image restoration. |
| Comparison table | Use when selecting between methods, domains, noise models, colour spaces or compression types. |
| Callout | Use sparingly for definition, warning, engineering insight, exam lens and lab connection. |

### 4.2 Master image-processing pipeline

```text
[Scene]
   ↓
[Optics / Illumination]
   ↓
[Sensor / Acquisition]
   ↓
[Sampling] → spatial discretization
   ↓
[Quantization] → intensity discretization
   ↓
[Digital Image / Matrix / Tensor]
   ↓
[Pre-processing]
   ├──→ [Enhancement] ──┐
   └──→ [Restoration] ──┴──→ [Segmentation]
                              ↓
                 [Feature extraction / learned representation]
                              ↓
              [Classification / Detection / Tracking]
                              ↓
                    [Decision / Application]
```

### 4.3 Image information panel

| Property | Must explain |
| --- | --- |
| Spatial dimensions | Width × height; what a pixel coordinate means. |
| Channels | Grayscale, RGB and multi-band images. |
| Bit depth | How many levels are representable per sample; relate to storage and quantization. |
| Dynamic range | Available intensity interval; do not conflate with spatial resolution. |
| Spatial resolution | Ability to distinguish spatial detail; state context instead of using “resolution” vaguely. |
| Radiometric resolution | Ability to distinguish intensity levels. |
| Colour space | Coordinate system used for colour representation and why conversion can help a task. |
| Datatype | uint8, uint16, float32 etc.; numeric range and downstream implications. |
| File format | Container/storage encoding; distinguish format from compression. |
| Metadata | Capture/device/context information when relevant. |

### 4.4 Matrix protocol

- Prefer small matrices that can be solved by hand over visually complex matrices that cannot be understood.

- Label row/column coordinates whenever spatial position matters.

- For convolution/filtering, show the neighbourhood, kernel alignment and output position.

- State border handling when an operation touches the image boundary.

- State whether a displayed operation is true convolution or correlation when the distinction matters.

> **VISUAL QA Every diagram must be checked for directional arrows, coordinate orientation, kernel alignment, labels, legends, and consistency with the written explanation. Decorative visuals must never imply a false technical relationship.**

## 5. Mathematical Teaching System

### 5.1 Formula rule

```text
FORMULA
  ↓
What problem does it solve?
  ↓
What does every symbol mean?
  ↓
What assumptions are being made?
  ↓
Worked numbers
  ↓
Result + units / interpretation
  ↓
What changes if an input changes?
```

### 5.2 Required worked-example families

| Topic | Example to include |
| --- | --- |
| Bit depth | Calculate representable intensity levels for 1-, 2-, 4-, and 8-bit cases. |
| Sampling / quantization | Map a small continuous/intensity example to discrete coordinates and levels. |
| Histogram | Compute frequency counts and normalized probabilities for a tiny grayscale image. |
| Histogram equalization | Compute CDF and mapped intensity values for a small example. |
| Point transform | Apply negative / threshold / contrast stretching to a small matrix. |
| Convolution | Perform one or more kernel positions by hand. |
| Sobel / edge | Calculate Gx, Gy and gradient magnitude/direction for a small local patch. |
| Mean / Gaussian / median | Compare outputs for a matrix containing an outlier. |
| Fourier | Use a small 1-D or conceptual 2-D example to explain frequency content before the full transform. |
| Restoration | Evaluate a simple degradation model and explain the inverse problem. |
| Morphology | Apply a structuring element to a binary matrix step by step. |
| Entropy | Calculate entropy for a small probability distribution. |
| Huffman | Construct a small tree and derive code lengths. |
| DCT/JPEG | Show a small block, qualitative coefficient interpretation, then quantization effect. |

### 5.3 Numerical answer format

> **WORKED EXAMPLE TEMPLATE Given → Required → Formula → Substitute → Calculate → Boxed answer → Interpretation → Sanity check. A numerical answer is incomplete if the reader cannot tell what the number means.**

### 5.4 Formula QA

- Recalculate every numeric example independently before publication.

- Check indexing conventions and summation limits.

- Check dimensions for matrices/tensors.

- Check units/ranges when a quantity has them.

- Check edge cases such as zero variance, constant images, empty masks and maximum intensity.

## 6. Practical & Implementation System

### 6.1 Tool policy

| Tool | Role |
| --- | --- |
| MATLAB | Primary practical alignment because the current lab record and syllabus practical structure use MATLAB-oriented image processing workflows. |
| Python + OpenCV | Engineering implementation path; especially useful for image I/O, filtering, feature work, video, YOLO and application integration. |
| NumPy / SciPy | Numerical understanding and selected transform/filter demonstrations. |
| TensorFlow / Keras or equivalent | CNN/MNIST practical layer when explicitly used. |
| No-code visual evidence | Useful for conceptual figures, but never a substitute for an explainable algorithm. |

### 6.2 Code block anatomy

- Purpose: one sentence.

- Inputs and assumptions.

- Minimal runnable code.

- Expected output or figure.

- Interpretation.

- Common implementation trap.

### 6.3 Critical implementation traps to guard against

| Area | QA rule |
| --- | --- |
| Channel order | Explicitly distinguish conceptual RGB from library-specific memory/order conventions when relevant. |
| Data type | Warn when arithmetic on uint8/integers can behave differently from floating-point arithmetic. |
| Range normalization | State whether intensities are 0–255, 0–1, or another range before applying formulas. |
| Image coordinates | State row/column versus x/y conventions where ambiguity can affect code. |
| Border handling | State padding/border policy for filters and convolutions. |
| Colour conversion | Show input and output colour-space assumptions, including channel count. |
| Model version | For architectures such as YOLO, state the specific implementation/model version used in the lab rather than implying “YOLO” is one frozen algorithm. |
| Randomness | Where ML examples involve random initialization, state seeds if reproducibility matters. |

### 6.4 Lab-to-chapter pattern

```text
THEORY
  ↓
LAB PREP
  ↓
Minimal code
  ↓
Expected visual output
  ↓
Interpretation questions
  ↓
Common error checklist
  ↓
Mini extension / experiment
```

## 7. Content QA & Error Control

### 7.1 Ten-gate QA system

| Gate | Check | Acceptance condition |
| --- | --- | --- |
| 1 | Scope QA | Every syllabus topic has a chapter/section anchor. |
| 2 | Definition QA | Terminology is internally consistent and not casually overloaded. |
| 3 | Math QA | Formulas, derivations and numerical results are independently checked. |
| 4 | Matrix QA | Dimensions, alignment, border handling and arithmetic are checked. |
| 5 | Algorithm QA | Narrated procedure matches the mathematics and intended algorithm. |
| 6 | Visual QA | Figures and examples actually depict what the prose claims. |
| 7 | Code QA | Code assumptions match the explanation, ranges, channel conventions and outputs. |
| 8 | Cross-chapter QA | Later chapters do not contradict earlier definitions or notation. |
| 9 | Exam QA | Core definitions/comparisons/derivations remain easy to retrieve. |
| 10 | Editorial QA | Spacing, hierarchy, captions, tables, accessibility and print behaviour meet the universal design system. |

### 7.2 Error classes

| Class | Examples to catch |
| --- | --- |
| Conceptual | Calling enhancement and restoration the same task; treating classification and detection as equivalent. |
| Terminological | Using “resolution” without specifying spatial/radiometric context. |
| Mathematical | Wrong transform formula, incorrect normalization, indexing error. |
| Operational | Wrong kernel orientation, missing normalization factor, wrong threshold convention. |
| Implementation | Unexpected datatype overflow, channel mismatch, shape mismatch, library convention mismatch. |
| Visual | Mislabelled axes, mirrored geometry, incorrect kernel placement, misleading before/after pair. |
| Scope | A topic implied but never actually taught; a lab experiment disconnected from theory. |
| Pedagogical | Formula shown without variable definitions; example shown without interpretation. |

## 8. DIP-Specific Fact & Terminology Rules

> **RULE The following are not “extra trivia”; they are deliberate anti-confusion rules. They exist because DIP terminology is often presented too loosely.**

| Topic | Rule for the MiniBook |
| --- | --- |
| Image vs pixel data | Always distinguish the visual object (image) from its numerical representation (array/matrix/tensor). |
| Sampling vs quantization | Sampling discretizes spatial coordinates; quantization discretizes intensity/amplitude values. Teach them separately first. |
| Bit depth vs resolution | Do not use bit depth as a synonym for spatial resolution. |
| Dynamic range vs contrast | Dynamic range describes representable/used intensity extent; contrast describes intensity separation within an image/context. |
| Grayscale vs binary | Binary is a two-level representation; grayscale generally has multiple intensity levels. |
| RGB channel semantics | Three channels do not mean three grayscale images are automatically “colours”; explain channel composition. |
| Histogram | A histogram describes intensity frequency/distribution in a specified image; it does not preserve spatial arrangement. |
| Convolution vs correlation | State the kernel-flipping distinction when the chapter uses mathematical convolution; state implementation conventions explicitly. |
| Spatial vs frequency domain | They are different representations/domains for manipulating image information, not two unrelated sets of filters. |
| Enhancement vs restoration | Enhancement is task/appearance-oriented; restoration is model-based estimation of a degraded image. |
| Edge detection | An edge is a spatial intensity transition; kernels such as Sobel approximate derivatives/gradients. |
| Thresholding vs segmentation | Thresholding is one segmentation mechanism; segmentation is the broader partitioning task. |
| Morphological operations | Opening = erosion followed by dilation; closing = dilation followed by erosion. Explain shape effects visually. |
| Feature vs descriptor | A feature is a salient/meaningful image structure; a descriptor is a representation used to characterize/match it. |
| SIFT/SURF/HOG | Do not present them as identical algorithms; distinguish local keypoint-based methods from gradient-histogram descriptors. |
| Compression vs file format | JPEG is both a commonly encountered image format and a compression standard/workflow; PNG is an image format that uses lossless compression. |
| JPEG loss | Identify where information loss occurs in the workflow instead of implying that every JPEG stage is lossy. |
| CNN convolution | Explain learned filters/kernels rather than equating CNN convolution with a fixed classical filter. |
| Classification vs detection | Classification assigns labels; detection also estimates object locations. |
| Video vs image sequence | Video processing inherits spatial image processing and adds the temporal dimension. |

### 8.1 Syllabus wording that should be preserved but clarified

- “File formats: BMP, JPEG, PNG, TIFF” should be taught as storage/encoding choices, while compression is taught as a separate concept with explicit lossless/lossy distinctions.

- “Pretrained models (VGG, ResNet, YOLO)” should be presented as a heterogeneous set: VGG/ResNet are primarily classification/backbone families, while YOLO is an object-detection family. The book should avoid presenting them as identical categories.

- The supplied syllabus shows “Practical = 1” in the credit-distribution line and “P = 02” in Course Hours. Preserve both values with their labels because they describe different quantities: credits versus hours.

## 9. Production Plan

| Stage | Output | Gate |
| --- | --- | --- |
| Stage 0 | This Master Specification v1.0 | Architecture, scope, QA and presentation rules frozen. |
| Stage 1 | Ch 01–02 reference-quality prototype | Every chapter anatomy component demonstrated at full quality. |
| Stage 2 | Ch 03–05 + Unit I closure | Image fundamentals complete; matrices, diagrams and practical links proven. |
| Stage 3 | Ch 06–10 | Spatial enhancement/filtering suite complete. |
| Stage 4 | Ch 11–14 | Geometric + frequency + restoration suite complete. |
| Stage 5 | Ch 15–20 | Segmentation, morphology and features complete. |
| Stage 6 | Ch 21–24 | Compression and JPEG complete. |
| Stage 7 | Ch 25–31 | AI/vision/video bridge complete. |
| Stage 8 | Appendices + global QA | Cross-book consistency, exam mapping, code review and accessibility/print QA. |
| Stage 9 | Release candidate | Render, responsive review, PDF output and final content audit. |

### 9.1 Batch production rule

> **BATCH SIZE Default writing/production batch = two chapters. Do not advance to the next batch until both chapters pass content QA and visual QA. A chapter that is “mostly done” is not a reusable reference pattern.**

### 9.2 Prototype principle

Chapters 01 and 02 must be treated as a design-and-content benchmark, not merely the first two chapters. They need enough depth to prove the full system: opener, explanation, diagram, image information, matrix, formula, worked example, table, implementation, lab connection, engineering insight, exam lens and checkpoint.

## 10. Definition of Done

| Requirement | Done means… |
| --- | --- |
| Syllabus coverage | Every Unit I–IV item and every listed practical has an identifiable home. |
| Depth | Major topics are explained, visualized and demonstrated rather than merely defined. |
| Images | Important image-processing claims are supported by meaningful before/after or representation visuals. |
| Matrices | Core local operations include small, solvable numeric examples. |
| Formulas | No unexplained equation; important formulas have worked examples. |
| Pipelines | Major systems such as acquisition, enhancement/restoration, JPEG, CNN inference and video motion have clear pipeline diagrams. |
| Tables | Comparisons are structured around meaningful engineering criteria. |
| Labs | Theory maps cleanly to practical experiments and expected outputs. |
| Accuracy | QA gates are completed and known ambiguities are explicitly labelled. |
| Presentation | The book follows the universal Engineering Minibooks visual grammar across Light, Dark and Paper themes. |
| Print | PDF export remains readable and deliberate, with captions, tables, formulas and figures preserved. |
| Accessibility | Semantic hierarchy, readable contrast, alt text/meaningful captions and no colour-only meaning are respected. |

## 11. Immediate Build Target: Chapters 01–02

### Chapter 01 — Digital Image Processing: The Big Picture

| Section | Planned content |
| --- | --- |
| Opening thesis | Why images must become computable before they can be enhanced, restored, analysed or understood by machines. |
| Definition | DIP as processing digital images with algorithms/computational systems. |
| Image-processing system | Acquisition → representation → processing → analysis → decision. |
| Visual anatomy | Pixel, coordinate, intensity, channel, dimensions and bit depth. |
| Core representation | Grayscale matrix + RGB tensor example. |
| Domain map | Spatial operations vs frequency operations vs learned representations. |
| Mini worked example | Take a tiny grayscale image and demonstrate a single transformation. |
| Applications | Healthcare, surveillance, document analysis, remote sensing, media. |
| Bridge | Why sampling/quantization must be understood before processing. |

### Chapter 02 — Image Formation and Acquisition

| Section | Planned content |
| --- | --- |
| Opening thesis | A digital image begins as a measurement of the physical world. |
| Image formation | Scene → illumination → optics → sensor → signal. |
| Acquisition components | Sensor, optics, illumination and capture mechanism. |
| Spatial coordinates | Continuous scene coordinates versus discrete image coordinates. |
| Sampling bridge | Why the sensor converts continuous spatial structure into samples. |
| Quantization preview | Why finite numeric intensity levels are needed. |
| Worked model | A small conceptual acquisition → matrix conversion example. |
| Engineering insight | Exposure, noise, dynamic range and acquisition limitations as motivation for later restoration/enhancement. |

> **NEXT PRODUCTION STEP These two chapters are the reference build. After they are written, we should review them specifically for factual precision, visual evidence, mathematical clarity, table usefulness, and consistency with the Minibook design system before locking the pattern for Chapters 03 onward.**

## 12. Source Traceability

The supplied University of Delhi Digital Image Processing syllabus is the scope authority for this specification. It defines the four units, course objectives/outcomes, suggested readings and ten suggested practical experiments. The MiniBook may add explanatory depth and clearly labelled extensions, but it must not silently omit or rewrite the prescribed scope.

Source handling rule: preserve university terminology when reproducing syllabus text; distinguish source-derived facts from additional explanatory material; and flag genuine ambiguities instead of inventing a resolution. The Practical = 1 credit and P = 02 course-hour entries are kept with their own labels because they describe different quantities.
