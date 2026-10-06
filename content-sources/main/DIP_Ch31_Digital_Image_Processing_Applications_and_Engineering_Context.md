---
id: "C31"
title: "DIP Applications, Engineering Context and Responsible Use"
layer: "MAIN"
part: "V — From DIP to Intelligent Vision"
unit: "Unit IV"
version: "1.0"
status: "PRODUCTION"
syllabus_scope: "Applications in Healthcare and Surveillance; engineering context; supporting application view across the course"
tags:
  - digital-image-processing
  - applications
  - healthcare
  - surveillance
  - industrial-inspection
  - remote-sensing
  - engineering
  - responsible-use
  - computer-vision
prerequisites:
  - "C01 — Digital Image Processing: The Big Picture"
  - "C14 — Image Restoration and Deblurring"
  - "C15 — Image Segmentation Fundamentals"
  - "C25 — Image Classification"
  - "C28 — Object Detection and YOLO"
  - "C30 — Video Processing and Motion Analysis"
related_math:
  - "Metrics"
  - "Uncertainty"
  - "Error analysis"
  - "Confusion matrix"
related_lab:
  - "LAB-08 — CNN-Based Image Classification"
  - "LAB-09 — Object Detection using YOLO"
  - "LAB-10 — Motion Tracking in Video"
related_code:
  - "CODE-11 — Application Integration Patterns"
related_exam:
  - "EXAM-Applications-and-Case-Studies"
related_practice:
  - "PRACTICE-System-Design"
---

# C31 — DIP Applications, Engineering Context and Responsible Use

> **Chapter thesis:** Digital image processing becomes an engineering system when image formation, enhancement, restoration, segmentation, features, compression, learning, detection, and temporal analysis are connected to a real task with measurable requirements, failure modes, and human consequences.

---

# 1. Why This Chapter Exists

A digital-image-processing course should not end at:

```text
apply algorithm
→ obtain image
→ done
```

Real systems need a larger chain:

```text
real-world problem
      ↓
image/video acquisition
      ↓
data quality
      ↓
preprocessing
      ↓
DIP / vision algorithm
      ↓
result
      ↓
interpretation
      ↓
decision
      ↓
action
```

The university syllabus specifically identifies applications such as:

- healthcare;
- surveillance;

and the course outcomes expect students to analyze and interpret image data across domains such as healthcare, surveillance and entertainment. fileciteturn4file0L22-L31 fileciteturn4file0L48-L52

This chapter therefore acts as the system-level conclusion of the Main Book.

---

# 2. Learning Contract

After this chapter, you should be able to:

- map DIP techniques to real engineering applications;
- explain an end-to-end image-processing system;
- identify how acquisition quality affects downstream results;
- choose appropriate DIP operations for a stated application;
- distinguish enhancement, restoration, segmentation, classification, detection and tracking in system design;
- explain application-specific trade-offs;
- discuss healthcare and surveillance use cases at an engineering level;
- identify common sources of error;
- distinguish algorithm failure from data or deployment failure;
- explain why validation must match the intended application;
- reason about privacy, bias, security and human oversight;
- design a basic DIP pipeline from requirements to evaluation;
- communicate limitations and uncertainty honestly.

---

# 3. From Algorithm to System

A laboratory exercise can be:

```text
image
→ filter
→ display
```

An engineering system might be:

```text
camera
→ sensor
→ acquisition
→ quality checks
→ preprocessing
→ enhancement
→ segmentation
→ feature extraction
→ classifier/detector
→ temporal tracking
→ decision
→ user interface / alert / record
```

The second is not simply “more algorithms.”

It introduces:

- interfaces;
- failure handling;
- timing;
- storage;
- security;
- validation;
- human interaction.

This is the difference between learning an algorithm and engineering a system.

---

# 4. The Application Taxonomy

A useful way to organize DIP applications is by the question being asked.

| Goal | Typical DIP / vision task |
|---|---|
| Make an image easier to inspect | Enhancement |
| Recover information from degradation | Restoration |
| Isolate an object/region | Segmentation |
| Describe visual structure | Features/descriptors |
| Store/transmit efficiently | Compression |
| Decide what a whole image contains | Classification |
| Find and localize objects | Detection |
| Follow change over time | Motion analysis/tracking |
| Reconstruct a cleaner image from corruption | Learned denoising |

This taxonomy ties the entire Main Book together.

---

# 5. Application Design Starts with the Requirement

Do not begin with:

> “Which algorithm should I use?”

Start with:

```text
What is the task?
What is the input?
What is the output?
What errors are unacceptable?
What latency is acceptable?
What data is available?
What hardware is available?
What level of human review exists?
```

Only then choose an algorithm.

---

# 6. Requirement → Pipeline Mapping

Suppose the requirement is:

> Detect vehicles in a road camera stream.

A reasonable conceptual mapping is:

```text
video
 ↓
frame capture
 ↓
optional preprocessing
 ↓
object detection
 ↓
vehicle filtering
 ↓
tracking
 ↓
count / trajectory / event
```

This uses:

```text
C28 → detection
C30 → tracking/motion
```

The application requirement determines why these chapters are connected.

---

# 7. Enhancement vs Restoration in Applications

These terms should not be casually exchanged.

### Enhancement

Goal:

> Make an image more useful or visually suitable for a task.

Examples:

```text
contrast enhancement
sharpening
illumination correction
```

### Restoration

Goal:

> Estimate an image from a known or modeled degradation process.

Examples:

```text
deblurring
noise restoration
inverse filtering
```

The difference is especially important in scientific and engineering applications.

---

# 8. Healthcare Imaging

Healthcare is one of the major application domains identified in the syllabus. fileciteturn4file0L22-L31 fileciteturn4file0L48-L52

A conceptual medical-imaging pipeline may be:

```text
medical image
      ↓
quality check
      ↓
preprocessing
      ↓
enhancement / restoration
      ↓
segmentation
      ↓
feature extraction or learned representation
      ↓
classification / detection
      ↓
measurement / decision support
      ↓
clinician review
```

The exact pipeline differs by modality and clinical task.

---

# 9. Why Preprocessing Matters in Healthcare

Suppose a segmentation model receives images with highly variable contrast.

An enhancement or normalization stage may improve consistency.

But aggressive preprocessing can also:

```text
remove clinically relevant detail
```

Therefore the rule is:

> **Preprocessing should be validated as part of the clinical workflow, not treated as automatically harmless.**

---

# 10. Medical Image Segmentation Example

Suppose the task is to estimate the region of an anatomical structure.

Possible pipeline:

```text
image
 ↓
denoise
 ↓
contrast adjustment
 ↓
segmentation
 ↓
morphological cleanup
 ↓
region measurement
```

The output may not be a class label.

It may be a binary or multiclass mask:

\[
M(x,y)\in\{0,1,\ldots,K\}.
\]

This connects:

```text
C09
C15–C18
```

to application-level measurement.

---

# 11. Measurement vs Visualization

A particularly important engineering distinction:

```text
image enhancement for visual inspection
```

is not equivalent to:

```text
image processing for quantitative measurement
```

A sharpening method that makes edges look clearer may alter intensities.

If the next stage measures intensity quantitatively, that change must be understood and validated.

---

# 12. Classification in Healthcare

A classifier might produce:

```text
image → class A / B / C
```

But an engineering deployment should also consider:

- class imbalance;
- sensitivity/recall;
- false-negative cost;
- data distribution;
- subgroup performance;
- calibration;
- human review.

A high overall accuracy can still hide clinically important failures.

---

# 13. Detection in Healthcare

Object detection can be used conceptually to localize findings:

```text
medical image
→ detector
→ bounding regions
→ label + confidence
```

But bounding boxes may not be sufficient for every medical task.

Some tasks require:

```text
pixel-level segmentation
```

or more specialized outputs.

Thus the application determines the appropriate representation.

---

# 14. Healthcare Validation

A model should not be treated as clinically reliable merely because:

```text
test accuracy = high
```

Validation should consider:

```text
dataset
+
acquisition conditions
+
patient/population variation
+
clinical task
+
error cost
+
workflow integration
```

This is engineering reasoning rather than a specific medical claim.

---

# 15. Surveillance

Surveillance provides a natural integration of:

```text
camera
→ video
→ detection
→ tracking
→ event analysis
```

A conceptual pipeline is:

```text
camera
 ↓
video stream
 ↓
motion / scene analysis
 ↓
YOLO-style detection
 ↓
object association
 ↓
tracking
 ↓
event rules
 ↓
alert / record
```

This directly connects C28 and C30.

---

# 16. Surveillance False Alarms

Suppose the system raises:

```text
alert
alert
alert
alert
```

but most alerts are harmless.

A technically accurate detector can still be operationally poor.

Therefore system evaluation must ask:

> How many alerts are meaningful, and how much human effort does the system create?

This connects precision to real operational cost.

---

# 17. Camera Motion in Surveillance

A simple background-subtraction system assumes a relatively stable camera.

If the camera itself moves:

```text
camera motion
→ background changes
→ false foreground
```

A robust system may require:

- camera stabilization;
- global-motion estimation;
- feature matching;
- stronger detection models.

Thus a failure in deployment may not mean the original algorithm was incorrectly implemented.

---

# 18. Privacy as a System Requirement

Image/video systems can capture information about people.

A production design may need:

```text
data minimization
access control
retention policy
secure storage
audit logging
```

The appropriate requirements depend on the application and jurisdiction.

The engineering point is:

> **Privacy should be designed into the system, not added after deployment.**

---

# 19. Security of Image Pipelines

An image-processing system is also a software system.

Possible engineering concerns include:

```text
malicious input files
model tampering
unauthorized data access
unsafe metadata
untrusted camera streams
dependency vulnerabilities
```

The image itself is data entering a computing pipeline.

Therefore standard software-security practices remain relevant.

---

# 20. Adversarial or Deceptive Inputs

Learning systems can behave unexpectedly on inputs that differ from normal training examples.

For example:

```text
clean input
→ expected prediction

unusual input
→ unreliable prediction
```

The correct response is not to assume:

> “The model must be correct.”

System designers should define:

- confidence thresholds;
- rejection/abstention policies;
- human review;
- input validation.

---

# 21. Industrial Inspection

A manufacturing example might be:

```text
camera
 ↓
image acquisition
 ↓
lighting normalization
 ↓
segmentation
 ↓
feature extraction / detection
 ↓
defect classification
 ↓
pass / inspect / reject
```

DIP is used not just for visual appearance but for automated measurement and quality control.

---

# 22. Lighting in Industrial Vision

A camera system can fail because of uncontrolled illumination.

Consider:

```text
same object
+ bright lighting
→ one image

same object
+ dark lighting
→ another image
```

A robust system may require controlled:

- lighting;
- camera exposure;
- background;
- viewpoint.

This illustrates a general principle:

> **Better data acquisition can sometimes produce a larger improvement than a more sophisticated algorithm.**

---

# 23. Document Processing

A document-processing pipeline may be:

```text
scan/photo
 ↓
grayscale
 ↓
denoise
 ↓
threshold
 ↓
morphology
 ↓
layout/region segmentation
 ↓
feature extraction
 ↓
OCR/classification
```

This brings together several course concepts:

```text
C05
C09
C16
C18
C19
C25
```

The application pipeline therefore reinforces the chapter dependencies.

---

# 24. Remote Sensing

Remote-sensing imagery can contain:

- multiple spectral bands;
- large spatial dimensions;
- different resolutions;
- atmospheric effects.

The course's Unit I explicitly introduces multispectral images. fileciteturn4file0L32-L35

A conceptual remote-sensing system can be:

```text
multispectral acquisition
→ preprocessing
→ enhancement/calibration
→ segmentation/features
→ classification
→ mapping / analysis
```

This demonstrates why image representation matters before algorithms are selected.

---

# 25. Entertainment and Media

Applications may include:

```text
image enhancement
compression
restoration
video effects
motion estimation
object detection
```

Compression is especially important when storing/transmitting large quantities of photographic and video data.

This connects Part IV to practical multimedia systems.

---

# 26. Mobile and Edge Vision

A mobile or edge device introduces constraints:

```text
limited compute
limited memory
battery
latency
network availability
```

The design objective becomes:

\[
\text{accuracy}
+
\text{latency}
+
\text{memory}
+
\text{energy}
\]

rather than accuracy alone.

A smaller model may be more appropriate even if a larger model scores slightly better on a benchmark.

---

# 27. Cloud vs Edge

### Edge

```text
camera
→ local processing
→ immediate result
```

Advantages can include:

- low latency;
- reduced data transmission;
- local operation.

### Cloud

```text
camera
→ network
→ remote compute
→ result
```

Advantages can include:

- more compute;
- centralized management;
- easier large-scale storage/analysis.

Trade-offs include:

```text
latency
privacy
bandwidth
cost
availability
```

The correct architecture depends on the application.

---

# 28. End-to-End Engineering Stack

A modern image system can be viewed in layers:

```text
L1 — Scene
L2 — Optics / sensor
L3 — Acquisition
L4 — Representation
L5 — DIP processing
L6 — Features / learned representation
L7 — Decision / detection
L8 — Temporal reasoning
L9 — Application logic
L10 — Human / system action
```

This expands the simple DIP pipeline from C01 into an engineering architecture.

---

# 29. Data Quality Pipeline

Before the algorithm:

```text
capture
 ↓
validate
 ↓
check dimensions
 ↓
check channel order
 ↓
check range / dtype
 ↓
check corruption
 ↓
process
```

Many “algorithm failures” actually originate in:

- wrong image format;
- unexpected channel order;
- incorrect normalization;
- corrupted frames;
- resolution mismatch.

This is why the Code layer should contain debugging guidance.

---

# 30. Algorithm Failure vs System Failure

### Algorithm failure

The method behaves poorly even with valid, representative inputs.

### Data failure

Inputs differ from assumptions.

### Integration failure

The output is correct, but the downstream component interprets it incorrectly.

### Operational failure

The system is too slow, expensive, fragile or difficult to use.

### Governance failure

The system produces technically valid outputs but is deployed without suitable controls.

This classification makes debugging much more systematic.

---

# 31. Evaluation Must Match the Task

Different tasks require different metrics.

| Task | Example evaluation |
|---|---|
| Enhancement | visual quality / downstream task performance |
| Restoration | MSE, PSNR, perceptual/task-specific measures |
| Segmentation | overlap / region metrics |
| Classification | accuracy, precision, recall, F1, confusion matrix |
| Detection | IoU, precision/recall, AP/mAP |
| Tracking | identity/trajectory consistency and task-specific metrics |
| Compression | bitrate/file size + distortion/quality |

There is no single “DIP accuracy” number.

---

# 32. Benchmark vs Deployment

A benchmark answer might be:

```text
Model A > Model B
```

on a dataset.

Deployment asks:

```text
Does Model A work in our camera?
our lighting?
our hardware?
our population?
our latency budget?
our failure tolerance?
```

A benchmark result is evidence, not a complete deployment guarantee.

---

# 33. Reproducibility

An engineering experiment should record:

```text
dataset
image dimensions
preprocessing
model
weights
parameters
random seed where relevant
software version
hardware
evaluation metric
thresholds
```

Otherwise reproducing the result becomes difficult.

This is particularly important for the YOLO, CNN and denoising practicals.

---

# 34. Human-in-the-Loop Systems

For high-consequence applications, a useful system may be:

```text
algorithm
 ↓
result + confidence
 ↓
human review
 ↓
final decision
```

This is different from:

```text
algorithm
 ↓
automatic irreversible decision
```

The appropriate level of human involvement depends on the application.

---

# 35. Confidence Is Not Certainty

A score such as:

\[
0.97
\]

can indicate a strong model output.

It does not prove:

\[
97\%\text{ probability of truth}
\]

unless the system is appropriately calibrated and the interpretation is justified.

For engineering communication:

> **Report scores with their definition and evaluation context.**

---

# 36. Bias and Dataset Dependence

Suppose the training data overrepresents one environment.

Then deployment in another environment can produce:

```text
performance degradation
```

Possible sources include:

- lighting;
- camera models;
- geography;
- image quality;
- object appearance;
- class distribution.

Therefore a model's performance is tied to its data and task definition.

---

# 37. Responsible Use in Surveillance

A surveillance system can be technically capable but still require strong controls.

Relevant system questions include:

```text
What is collected?
Why is it collected?
Who can access it?
How long is it retained?
What actions can an alert trigger?
How are false alarms handled?
How is human review performed?
```

The goal is not to replace engineering with abstract ethics.

The goal is to recognize that deployment requirements extend beyond model accuracy.

---

# 38. Responsible Use in Healthcare

Healthcare systems similarly require:

```text
validation
traceability
error analysis
workflow integration
human oversight
```

A visually impressive model is not enough.

This is especially important when a preprocessing step can alter image appearance or numerical values.

---

# 39. A General Engineering Decision Framework

When selecting a DIP/vision method:

```text
1. Define task
2. Define input
3. Define output
4. Identify data characteristics
5. Identify failure costs
6. Choose baseline
7. Measure
8. Analyze failures
9. Improve
10. Validate on representative data
11. Check deployment constraints
12. Document limitations
```

This is more robust than selecting the most advanced-looking algorithm first.

---

# 40. Baseline First

A good engineering process often starts with a simple baseline.

Example:

```text
Problem: detect moving objects

Baseline:
frame difference

Then:
background subtraction

Then:
object detector

Then:
detector + tracker
```

Each step should demonstrate why additional complexity is justified.

This prevents unnecessary model complexity.

---

# 41. Application Design Example — Smart Traffic Camera

### Requirement

Count vehicles and track movement.

### Pipeline

```text
camera
 ↓
frame capture
 ↓
quality check
 ↓
YOLO detection
 ↓
vehicle class filter
 ↓
tracking
 ↓
trajectory
 ↓
line-crossing / counting rule
 ↓
statistics
```

Relevant chapters:

```text
C28
→ detection

C30
→ temporal tracking

C31
→ system-level evaluation
```

---

# 42. Application Design Example — Document Scanner

### Requirement

Produce clean, readable text pages.

Pipeline:

```text
camera
 ↓
geometric correction
 ↓
grayscale
 ↓
denoise
 ↓
contrast enhancement
 ↓
threshold
 ↓
morphological cleanup
 ↓
document output / OCR
```

Relevant topics:

```text
C06
C09
C11
C16
C18
```

This demonstrates how seemingly separate chapters become one practical system.

---

# 43. Application Design Example — Industrial Defect Detection

```text
controlled camera
 ↓
image acquisition
 ↓
normalization
 ↓
ROI extraction
 ↓
feature / CNN representation
 ↓
classification or detection
 ↓
pass / fail
 ↓
human inspection for uncertain cases
```

The important engineering principle is:

> **Control the acquisition conditions when possible before increasing algorithmic complexity.**

---

# 44. Application Design Example — Video Security

```text
camera
 ↓
frame sampling
 ↓
motion estimation
 ↓
object detection
 ↓
tracking
 ↓
event rule
 ↓
alert
```

Possible failure points:

```text
camera shake
lighting changes
occlusion
false positives
missed detections
latency
```

A good system design anticipates them.

---

# 45. Responsible System Checklist

Before deployment, ask:

```text
□ Is the task clearly defined?
□ Is the training/test data representative?
□ Is preprocessing documented?
□ Are important failure modes known?
□ Are thresholds justified?
□ Is human review required?
□ Is sensitive data protected?
□ Is model/version provenance recorded?
□ Is performance measured on deployment-like data?
□ Are limitations communicated?
```

This checklist is more useful than simply saying “the model is accurate.”

---

# 46. A DIP System Can Be Visualized as a Graph

```text
                 ┌───────────────┐
                 │   Acquisition │
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │ Representation│
                 └───────┬───────┘
                         ↓
             ┌───────────┼───────────┐
             ↓           ↓           ↓
         Enhancement  Restoration  Compression
             │           │           │
             └───────┬───┴───────────┘
                     ↓
                Segmentation
                     ↓
                  Features
                     ↓
              Classification
                     ↓
                 Detection
                     ↓
                  Tracking
                     ↓
                 Application
```

This is a conceptual relationship graph, not a statement that every system must execute every branch.

---

# 47. Course-Wide Synthesis

The entire Main Book can now be compressed into:

```text
WORLD
 ↓
IMAGE FORMATION
 ↓
SAMPLING + QUANTIZATION
 ↓
DIGITAL REPRESENTATION
 ↓
COLOUR / STORAGE
 ↓
ENHANCEMENT
 ↓
RESTORATION
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
 ↓
APPLICATION
```

The chapters are connected because each stage changes what can be done next.

---

# 48. What “Engineering Understanding” Looks Like

A student who only memorizes:

```text
Sobel = edge detector
JPEG = compression
CNN = classification
YOLO = detection
```

has vocabulary.

A student with engineering understanding can explain:

```text
why the method exists
→
what assumptions it makes
→
what data it needs
→
what output it produces
→
how to implement it
→
how to evaluate it
→
where it fails
→
when to choose something else
```

That is the intended end state of the MiniBook.

---

# 49. Exam Lens

## 2-mark questions

**Name two applications of DIP.**

Examples include healthcare and surveillance, both explicitly identified in the course outcomes/syllabus.

**Why is acquisition important?**

Because image quality and representation at the input affect every downstream processing stage.

**What is human-in-the-loop processing?**

A system in which an algorithm provides analysis or recommendations while a human participates in the final interpretation/decision.

---

# 50. 5-Mark Question

### Explain DIP applications in healthcare and surveillance.

A strong answer should include:

```text
application requirement
→ acquisition
→ preprocessing
→ analysis method
→ output
→ evaluation
→ limitations
```

For example:

```text
healthcare
image → preprocess → segment/classify → measurement/support

surveillance
video → detect → track → event analysis → alert
```

---

# 51. 10-Mark Question

### Design an image-processing system for a real-world application.

Recommended structure:

1. problem statement;
2. input/data;
3. acquisition;
4. preprocessing;
5. selected DIP methods;
6. feature/representation stage;
7. decision stage;
8. evaluation metrics;
9. failure modes;
10. computational constraints;
11. privacy/security considerations;
12. human oversight;
13. limitations;
14. expected output.

This tests understanding rather than isolated algorithm recall.

---

# 52. Chapter Checkpoint

### Q1

Why should system design begin with requirements instead of algorithms?

### Q2

Why can better image acquisition sometimes improve performance more than a more complex model?

### Q3

Give a pipeline connecting YOLO detection to tracking.

### Q4

Why can a high classification accuracy still be insufficient in healthcare?

### Q5

What is the difference between an algorithm failure and a data failure?

### Q6

Why should confidence scores not automatically be treated as certainty?

### Q7

Why are privacy and security part of an image-processing system rather than separate topics?

---

# 53. One-Page Recall Sheet

```text
DIP ENGINEERING
│
├── Requirement
│     ↓
├── Acquisition
│     ↓
├── Representation
│     ↓
├── Processing
│  ├── enhancement
│  ├── restoration
│  ├── segmentation
│  └── compression
│     ↓
├── Understanding
│  ├── features
│  ├── classification
│  └── detection
│     ↓
├── Time
│  └── motion / tracking
│     ↓
├── Evaluation
│     ├── accuracy / precision / recall
│     ├── IoU / AP
│     ├── MSE / PSNR
│     └── task-specific metrics
│
└── Deployment
    ├── latency
    ├── compute
    ├── privacy
    ├── security
    ├── failure handling
    └── human oversight
```

---

# 54. Cross-Book Links

| Layer | Connection |
|---|---|
| MAIN | C31 integrates the entire DIP journey |
| MATH | Metrics, uncertainty, error reasoning |
| LAB | Uses C08–C10 practical outputs in application-style scenarios |
| CODE | System integration patterns and deployment checks |
| EXAM | Applications, case studies, system-design questions |
| PRACTICE | Pipeline design, method selection, failure analysis |
| RESOURCE | Course references + domain-specific deepening |
| ASSETS | End-to-end architecture diagrams and application pipelines |
| MASTER | Final integration and syllabus completion |

---

# 55. Final Chapter Summary

The deepest lesson of the course is not a particular filter, transform, descriptor, CNN or detector.

It is:

\[
\boxed{
\text{Choose and connect image-processing operations according to the task, data, constraints, and consequences of error.}
}
\]

The full journey is:

```text
scene
→ image
→ digital representation
→ enhancement/restoration
→ segmentation/features
→ compression or intelligent interpretation
→ classification/detection
→ video/motion
→ application decision
```

The syllabus identifies healthcare and surveillance as application domains and expects students to analyze and interpret image data in such contexts. fileciteturn4file0L22-L31 fileciteturn4file0L48-L52

This chapter therefore closes the **31-chapter Main Book** by connecting individual techniques to complete engineering systems.

---

# 56. Main Book Completion

```text
PART I   — The Image
C01–C05  ✅

PART II  — Improving the Image
C06–C14  ✅

PART III — Understanding Image Content
C15–C20  ✅

PART IV  — Compressing Images
C21–C24  ✅

PART V   — From DIP to Intelligent Vision
C25–C31  ✅
```

\[
\boxed{\text{31 / 31 Main Chapters Complete}}
\]

The Main Book is now complete at the syllabus-theory level. The remaining MiniBook work belongs primarily to the companion layers: mathematics, laboratory, reusable code, examination, deliberate practice, resources, visual assets, and master integration/QA.
