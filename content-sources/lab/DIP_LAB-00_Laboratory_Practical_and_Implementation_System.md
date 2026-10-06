---
id: "LAB-00"
title: "Digital Image Processing — Laboratory, Practical & Implementation System"
layer: "PRACTICAL"
system: "Engineering Minibooks · Digital Image Processing"
version: "1.0"
status: "LAB ARCHITECTURE LOCK"
---

# LAB-00 — Digital Image Processing Laboratory, Practical & Implementation System

> **Purpose:** Define the practical learning system that connects DIP theory to MATLAB/Python/OpenCV experiments, reproducible workflows, output interpretation and engineering debugging.

---

# 1. Practical Philosophy

A DIP practical is not merely:

```text
write code
→ run code
→ paste screenshot
```

It should be:

```text
CONCEPT
↓
TASK
↓
INPUT
↓
ALGORITHM
↓
IMPLEMENTATION
↓
OUTPUT
↓
OBSERVATION
↓
INTERPRETATION
↓
LIMITATION
↓
CONCLUSION
```

The practical system must teach the learner how image-processing operations behave, not just how to invoke library functions.

---

# 2. University Practical Scope

The supplied syllabus specifies ten suggested experiments:

1. Basics of Image Processing
2. Image Enhancement
3. Frequency Domain Filtering
4. Noise Removal
5. Image Segmentation
6. Feature Detection
7. Image Compression
8. CNN-based Image Classification
9. Object Detection using YOLO
10. Motion Tracking in Video

The syllabus also associates these with Python/OpenCV/PIL, MATLAB, NumPy, SciPy, TensorFlow/Keras and relevant pretrained model tooling.

The practical system should map each experiment to theory chapters and provide implementation guidance.

---

# 3. Practical File Architecture

```text
LAB-00
Laboratory System

LAB-U1-01
Image Input/Output and Colour Spaces

LAB-U1-02
Pixel Intensity and Perception

LAB-U1-03
Point Operations and Geometric Transformations

LAB-U1-04
Histogram Processing

LAB-U2-01
Spatial Filtering / Enhancement

LAB-U2-02
Frequency-Domain Filtering

LAB-U2-03
Noise Removal / Restoration

LAB-U3-01
Thresholding and Segmentation

LAB-U3-02
Morphological Operations

LAB-U3-03
Feature Detection and Descriptors

LAB-U3-04
Image Compression / JPEG

LAB-U4-01
CNN Image Classification

LAB-U4-02
Object Detection with YOLO

LAB-U4-03
Video Motion Analysis / Optical Flow
```

This practical architecture may contain more files than the ten syllabus experiments because the learner's existing practical record already separates several fundamental operations and because splitting complex experiments improves reproducibility.

---

# 4. Practical vs Code Ownership

## LAB

Answers:

> What am I performing, what should I observe, and how should I document it?

## CODE

Answers:

> How is the operation implemented, parameterized, tested and debugged?

Therefore:

```text
LAB
→ experiment-oriented

CODE
→ implementation-oriented
```

The same function may be reused by several LAB files.

---

# 5. Standard Practical Anatomy

Every experiment should follow:

```text
1. Title
2. Aim
3. Learning objectives
4. Theory
5. Prerequisites
6. Required tools
7. Input data
8. Expected output
9. Algorithm
10. Step-by-step procedure
11. Implementation
12. Result
13. Observation
14. Interpretation
15. Parameters
16. Variations
17. Common errors
18. Viva questions
19. Conclusion
20. Extension
```

---

# 6. Aim vs Learning Objective

Keep these separate.

### Aim

A concise statement of the experiment.

### Learning objectives

What the learner should understand or be able to do afterward.

Example:

> **Aim:** Implement histogram equalization on a grayscale image.

Learning objectives:

- compute a histogram,
- derive a normalized histogram,
- compute a CDF,
- create an intensity mapping,
- interpret the change in contrast.

---

# 7. Input Specification

Every experiment should declare:

```text
image type
colour space
dimensions
datatype
intensity range
expected file format
```

Example:

```text
Input:
grayscale image
H × W
uint8
range: 0–255
```

Do not rely on undocumented assumptions.

---

# 8. Output Specification

State exactly what should be produced.

For example:

```text
Output:
1. enhanced image
2. original histogram
3. transformed histogram
4. numerical observation
```

For CNN/detection tasks:

```text
prediction
confidence
class
location
evaluation measure where applicable
```

---

# 9. Algorithm-to-Code Alignment

Every implementation should map directly to the algorithm.

Example:

```text
Algorithm step 1
→ code section 1

Algorithm step 2
→ code section 2
```

Do not describe one algorithm and silently implement a different library method without explaining the distinction.

---

# 10. Reproducibility Standard

Record:

```text
software
version
libraries/toolboxes
image/data source
parameters
random seed where relevant
model weights/version where relevant
hardware assumptions
```

For modern model experiments, a family name alone is insufficient.

---

# 11. MATLAB Standard

MATLAB examples should clearly state when functionality relies on a toolbox.

Where possible:

```text
MATLAB built-in
Image Processing Toolbox
Deep Learning Toolbox
```

Do not imply that every command is available in a bare installation.

---

# 12. Python Standard

State the intended stack.

Typical categories:

```text
Python
NumPy
OpenCV
Pillow
SciPy
Matplotlib
TensorFlow/Keras or equivalent framework
```

Only introduce a dependency when it serves the experiment.

---

# 13. Channel and Datatype Discipline

The practical system must explicitly handle:

- grayscale vs RGB,
- RGB vs BGR convention,
- integer vs floating-point representation,
- intensity scaling,
- clipping,
- normalization.

A common implementation bug is correct-looking code operating on the wrong numeric range.

---

# 14. LAB-U1-01 — Image I/O and Colour Spaces

Cover:

- read image
- inspect dimensions
- inspect datatype
- display image
- convert grayscale
- split RGB channels
- convert to HSV
- compare representations

Required observations:

```text
shape
channels
datatype
range
visual difference
```

---

# 15. LAB-U1-02 — Pixel Intensity and Visual Perception

Connect to the practical record's pixel-intensity/perception work where applicable.

Possible activities:

- intensity manipulation,
- Mach bands,
- simultaneous contrast.

The experiment should distinguish:

```text
physical/numerical intensity
vs
human perceptual response
```

Do not imply that perceived brightness is determined solely by a single pixel value.

---

# 16. LAB-U1-03 — Point Operations and Geometric Transformations

Cover:

- negative
- flip
- threshold
- contrast stretching
- translation where applicable
- scaling/rotation where applicable

For each:

```text
formula
→ image result
→ observation
```

---

# 17. LAB-U1-04 — Histogram Processing

Cover:

- histogram computation,
- contrast stretching,
- histogram equalization,
- CDF-based mapping.

Required outputs:

```text
original image
original histogram
mapping/CDF
processed image
processed histogram
```

This is an ideal experiment for connecting theory, mathematics and visual evidence.

---

# 18. LAB-U2-01 — Spatial Filtering / Enhancement

Cover representative:

- mean filter,
- Gaussian filter,
- median filter,
- sharpening,
- edge operators.

Do not make the experiment a huge catalogue.

Select examples that expose the conceptual differences.

---

# 19. LAB-U2-02 — Frequency-Domain Filtering

Pipeline:

```text
image
→ grayscale if appropriate
→ DFT/FFT
→ shifted spectrum for visualization
→ frequency mask
→ inverse transform
→ result
```

Record:

- transform dimensions,
- visualization convention,
- filter parameters,
- output interpretation.

---

# 20. LAB-U2-03 — Noise Removal and Restoration

Use controlled corruption where possible.

Example pipeline:

```text
clean image
→ add known noise
→ noisy image
→ filter/restoration
→ comparison
```

This is superior to testing only on an unknown noisy image because the learner knows what degradation was introduced.

---

# 21. LAB-U3-01 — Thresholding and Segmentation

Compare:

```text
global threshold
vs
adaptive threshold
```

Use an image where the difference is visible.

Record:

- threshold values,
- local-window parameters,
- segmentation quality,
- failure cases.

---

# 22. LAB-U3-02 — Morphological Operations

Perform:

```text
erosion
dilation
opening
closing
```

Use a controlled binary example.

Show:

```text
input
→ operation
→ result
```

and explain which structures were removed, expanded, connected or filled.

---

# 23. LAB-U3-03 — Feature Detection and Descriptors

Cover the syllabus methods:

- SIFT
- SURF
- HOG

Where an extension is added, label it clearly.

Required output examples:

```text
keypoints / feature locations
descriptor concept
matching or feature representation where relevant
```

Explain what the visual result means.

---

# 24. LAB-U3-04 — Image Compression / JPEG

Do not simply call an image-saving function and declare JPEG “implemented.”

The practical should demonstrate selected JPEG stages:

```text
colour transform
→ block formation
→ DCT
→ quantization
→ zig-zag concept
→ coding concept
```

A full production JPEG encoder may be treated as an advanced extension.

---

# 25. LAB-U4-01 — CNN Image Classification

The syllabus specifies MNIST as a suggested dataset.

Workflow:

```text
dataset
→ preprocessing
→ model
→ training
→ validation/test
→ prediction
→ evaluation
```

Record:

- input shape,
- normalization,
- architecture,
- loss,
- optimizer,
- epochs,
- batch size,
- evaluation result.

Avoid focusing only on final accuracy.

---

# 26. LAB-U4-02 — Object Detection with YOLO

Workflow:

```text
image/video
→ preprocessing
→ model inference
→ boxes
→ class labels
→ confidence
→ visualization
```

The implementation file must state the concrete YOLO implementation/version used.

Do not assume all YOLO versions expose identical APIs or architecture.

---

# 27. LAB-U4-03 — Video Motion Analysis / Optical Flow

Explain:

```text
video
→ frames
→ temporal change
→ motion representation
→ tracking/analysis
```

Where optical flow is used, distinguish:

> estimating apparent image motion

from:

> recovering full physical 3-D motion.

The experiment should visualize motion vectors or another meaningful representation.

---

# 28. Observation Standard

An observation should describe evidence.

Weak:

> The image looks better.

Preferred:

> The median filter removed isolated extreme pixels while preserving major edge structure more effectively than the corresponding mean-filter result for this example.

Observations should remain tied to the actual experiment rather than universal claims.

---

# 29. Parameter Study

Important experiments should vary at least one meaningful parameter.

Examples:

```text
Gaussian σ
kernel size
threshold
morphological structuring-element size
JPEG quality/quantization strength
CNN depth or regularization
detection confidence threshold
```

Show how the result changes.

---

# 30. Failure-Case Requirement

At least one failure mode should be demonstrated or discussed when meaningful.

Examples:

- over-smoothing,
- over-sharpening,
- bad threshold,
- uneven illumination,
- excessive morphological erosion,
- JPEG artifacts,
- false detections,
- optical-flow failure.

This teaches engineering judgment.

---

# 31. Result Presentation

A good practical result page should use:

```text
INPUT
PARAMETERS
OUTPUT
VISUAL COMPARISON
NUMERICAL/STATISTICAL MEASURE
INTERPRETATION
```

Avoid pages that consist mainly of code screenshots.

---

# 32. Viva Layer

Every experiment should include questions in three levels.

### Recall

> What is histogram equalization?

### Understanding

> Why can equalization alter contrast unevenly?

### Transfer

> Which technique would you choose when illumination varies across the image, and why?

---

# 33. Debugging Layer

Common DIP implementation failures should have dedicated explanations.

Examples:

```text
wrong colour channel order
wrong datatype
uint8 overflow
missing normalization
wrong image range
incorrect kernel dimensions
border handling mismatch
unexpected FFT spectrum interpretation
model input-shape mismatch
incorrect coordinate convention
```

---

# 34. Code Quality Standard

Practical code should be:

- reproducible,
- readable,
- parameterized,
- minimally dependent,
- clearly commented,
- separated into input/process/output where useful.

Do not optimize prematurely.

The practical goal is understanding first.

---

# 35. Lab Submission Compatibility

Where the university requires a formal record, retain standard sections:

```text
Experiment number
Date
Aim
Theory
Algorithm
Code
Output
Result
Viva
```

The MiniBook adds engineering interpretation rather than replacing the expected record structure.

---

# 36. Practical-to-Main Map

```text
LAB-U1-01 → C04–C05
LAB-U1-02 → C04
LAB-U1-03 → C06, C11
LAB-U1-04 → C07

LAB-U2-01 → C08–C10
LAB-U2-02 → C12–C13
LAB-U2-03 → C09, C14

LAB-U3-01 → C15–C16
LAB-U3-02 → C18
LAB-U3-03 → C19–C20
LAB-U3-04 → C21–C24

LAB-U4-01 → C25–C26
LAB-U4-02 → C28
LAB-U4-03 → C30
```

---

# 37. Practical Definition of Done

An experiment is ready when:

- [ ] Aim is clear.
- [ ] Required theory is linked.
- [ ] Inputs are specified.
- [ ] Tool/version assumptions are stated.
- [ ] Algorithm matches implementation.
- [ ] Parameters are explained.
- [ ] Output is reproducible.
- [ ] Results are interpreted.
- [ ] At least one relevant limitation/failure mode is addressed.
- [ ] Viva questions exist.
- [ ] Code has been clean-run where practical.
- [ ] Related Main/Math/Exam/Practice IDs can be attached.

---

# 38. Practical System Final Principle

The learner should finish a practical knowing:

> **not only what code to run, but what changed in the image, why it changed, what assumption made it work, and where the method might fail.**
