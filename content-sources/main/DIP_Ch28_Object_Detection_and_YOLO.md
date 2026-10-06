---
id: "C28"
title: "Object Detection and YOLO"
layer: "MAIN"
part: "V — From DIP to Intelligent Vision"
unit: "Unit IV"
version: "1.0"
status: "PRODUCTION"
syllabus_scope: "Image Classification and Object Detection; YOLO; Practical 9 — Object Detection using YOLO"
tags:
  - digital-image-processing
  - object-detection
  - yolo
  - bounding-box
  - iou
  - confidence
  - computer-vision
  - real-time
prerequisites:
  - "C25 — Image Classification"
  - "C26 — Convolutional Neural Networks"
  - "C27 — VGG and ResNet"
related_math:
  - "Intersection over Union"
  - "Bounding-box geometry"
  - "Probability"
related_lab:
  - "LAB-09 — Object Detection using YOLO"
related_code:
  - "CODE-09 — YOLO Inference"
related_exam:
  - "EXAM-Object-Detection-YOLO"
related_practice:
  - "PRACTICE-Detection"
---

# C28 — Object Detection and YOLO

> **Chapter thesis:** Object detection extends image classification by predicting both what objects are present and where they occur, usually through class labels, bounding boxes, and confidence scores.

---

# 1. Why This Chapter Exists

Classification answers:

```text
What is in the image?
```

Object detection answers:

```text
What objects are present?
Where are they?
How confident is the detector?
```

The university syllabus explicitly includes:

- Image Classification and Object Detection;
- YOLO as a pretrained model;
- a practical on real-time object detection using YOLO. fileciteturn4file0L48-L52 fileciteturn4file0L80-L84

Therefore this chapter must cover both:

```text
detection theory
+
YOLO practical workflow
```

---

# 2. Learning Contract

After this chapter, you should be able to:

- define object detection;
- distinguish classification, detection and segmentation;
- explain bounding boxes;
- explain class labels and confidence scores;
- represent a bounding box using coordinates;
- calculate intersection over union (IoU);
- explain predicted vs ground-truth boxes;
- explain non-maximum suppression conceptually;
- understand one-stage vs two-stage detection at a high level;
- explain the core idea behind YOLO;
- explain why YOLO is associated with real-time detection;
- understand why “YOLO” refers to a family rather than one immutable implementation;
- run a pretrained YOLO model on an image/video/webcam;
- interpret detections;
- identify common detection failures;
- evaluate detections using appropriate concepts.

---

# 3. Classification vs Detection

Suppose an image contains:

```text
car + person + bicycle
```

### Classification

May produce:

```text
"street scene"
```

or a single class depending on the task.

### Detection

Produces multiple object hypotheses:

```text
person → box
car    → box
bicycle → box
```

So:

\[
\boxed{\text{Detection}=\text{classification}+\text{localization}}
\]

This is an introductory mental model, not a claim that every detector is literally composed of two independent algorithms.

---

# 4. Detection Output

A typical detection for one object contains:

```text
class
bounding box
confidence
```

Example:

```text
person
x1 = 120
y1 = 85
x2 = 310
y2 = 420
confidence = 0.94
```

The detector may output many such records.

---

# 5. Bounding Box

A common rectangular bounding box uses:

\[
(x_1,y_1,x_2,y_2)
\]

where:

- \((x_1,y_1)\) = top-left;
- \((x_2,y_2)\) = bottom-right.

Width:

\[
w=x_2-x_1.
\]

Height:

\[
h=y_2-y_1.
\]

Area:

\[
A=wh.
\]

---

# 6. Worked Bounding-Box Example

Suppose:

\[
(x_1,y_1)=(100,50)
\]

and:

\[
(x_2,y_2)=(300,250).
\]

Then:

\[
w=300-100=200
\]

\[
h=250-50=200.
\]

Area:

\[
A=200\times200
=
\boxed{40{,}000}.
\]

---

# 7. Alternative Box Representations

Some models/APIs use:

\[
(x_c,y_c,w,h)
\]

where:

- \(x_c,y_c\) = center;
- \(w,h\) = width and height.

Conversions:

\[
x_1=x_c-\frac{w}{2}
\]

\[
y_1=y_c-\frac{h}{2}
\]

\[
x_2=x_c+\frac{w}{2}
\]

\[
y_2=y_c+\frac{h}{2}.
\]

This is important when reading annotation formats.

---

# 8. Confidence Score

A detector often provides a score indicating how strongly the model supports a detection hypothesis.

A simplified interpretation is:

```text
high confidence
→ stronger model score

low confidence
→ weaker detection
```

Do not assume confidence is perfectly calibrated probability.

It is best interpreted as a model output used to rank/filter detections.

---

# 9. Detection Threshold

A practical detector commonly applies a confidence threshold.

For example:

\[
t=0.50.
\]

Then:

```text
0.92 → keep
0.73 → keep
0.41 → reject
```

The appropriate threshold depends on the application.

Lower threshold:

```text
more detections
+
more false positives
```

Higher threshold:

```text
fewer detections
+
potentially more missed objects
```

This is a precision–recall trade-off.

---

# 10. Ground Truth vs Prediction

For evaluation:

### Ground truth

The correct annotation supplied by the dataset.

```text
class = car
box = reference rectangle
```

### Prediction

The detector's output.

```text
class = car
box = predicted rectangle
confidence = ...
```

Evaluation asks:

> How closely does the prediction agree with the ground truth?

---

# 11. Intersection over Union (IoU)

IoU measures overlap between two boxes:

\[
\boxed{
IoU=
\frac{\text{intersection area}}
{\text{union area}}
}
\]

where:

\[
\text{union}
=
A_{\text{pred}}
+
A_{\text{gt}}
-
A_{\text{intersection}}.
\]

IoU ranges from:

\[
0\le IoU\le1.
\]

Interpretation:

```text
0 → no overlap
1 → identical boxes
```

---

# 12. Worked IoU Example

Suppose:

```text
Ground-truth box area = 1000
Predicted box area     = 900
Intersection area      = 700
```

Union:

\[
1000+900-700=1200.
\]

Therefore:

\[
IoU=\frac{700}{1200}
\approx0.5833.
\]

So:

\[
\boxed{IoU\approx0.583}.
\]

---

# 13. IoU with Coordinates

Suppose:

Ground truth:

\[
(10,10,50,50)
\]

Prediction:

\[
(20,20,60,60).
\]

Ground-truth area:

\[
40\times40=1600.
\]

Prediction area:

\[
40\times40=1600.
\]

Intersection:

```text
x overlap = 20 to 50 → 30
y overlap = 20 to 50 → 30
```

so:

\[
A_{\cap}=30\times30=900.
\]

Union:

\[
1600+1600-900=2300.
\]

Thus:

\[
IoU=\frac{900}{2300}
\approx0.391.
\]

---

# 14. Non-Maximum Suppression

A detector may produce multiple overlapping boxes for the same object.

Example:

```text
person
 ┌───────────────┐
 │   box A       │
 │   ┌───────────┐
 │   │ box B     │
 │   └───────────┘
 └───────────────┘
```

Non-maximum suppression (NMS) removes redundant detections.

Conceptually:

```text
1. rank boxes by confidence
2. keep highest-scoring box
3. remove highly overlapping boxes
4. repeat
```

The overlap threshold is typically based on IoU.

---

# 15. Simple NMS Example

Suppose three boxes have:

| Box | Confidence |
|---|---:|
| A | 0.92 |
| B | 0.81 |
| C | 0.40 |

and A/B overlap strongly.

A simplified NMS process:

```text
keep A
compare B to A
if IoU > threshold → suppress B
retain C if it survives threshold rules
```

The exact implementation may use class-aware or class-agnostic suppression and modern variants may use different suppression strategies.

---

# 16. Why NMS Is Needed

Neural detectors often produce several nearby hypotheses because multiple spatial locations/features can respond to the same object.

Without suppression:

```text
one object
→ many boxes
```

With NMS:

```text
one object
→ preferred box
```

This improves the usability of detection output.

---

# 17. One-Stage vs Two-Stage Detection

A useful high-level distinction is:

### Two-stage

```text
region proposals
→ classify/refine proposals
```

### One-stage

```text
image
→ dense/direct prediction
```

Two-stage methods can emphasize localization/refinement quality.

One-stage methods are often attractive for simpler real-time inference pipelines.

YOLO belongs to the one-stage family conceptually.

---

# 18. YOLO — The Core Idea

YOLO stands for:

> **You Only Look Once**

The historical idea was to treat object detection as a direct prediction problem from the full image in one unified network.

Conceptually:

```text
whole image
     ↓
CNN / detection network
     ↓
object predictions
     ↓
boxes + classes + confidence
```

This differs from older pipelines that explicitly generated candidate regions and then classified them separately.

---

# 19. Why YOLO Is Associated with Real-Time Detection

The original YOLO family emphasized a unified detection pipeline with speed as a major objective.

The broad engineering idea is:

```text
single integrated inference
→ efficient processing
→ suitable for real-time/near-real-time systems
```

Actual speed depends on:

- model variant;
- hardware;
- input resolution;
- implementation;
- preprocessing/postprocessing;
- acceleration backend.

Therefore:

> **“YOLO = always real-time” is too simplistic.**

---

# 20. YOLO Is a Family

A critical modern understanding is:

```text
YOLO
≠
one immutable algorithm
```

The YOLO family has evolved through many versions and implementations.

Differences can include:

- backbone;
- neck;
- detection head;
- box representation;
- training losses;
- data augmentation;
- inference strategy;
- model size;
- supported tasks.

For this course, understand **the general YOLO detection concept** and then identify the concrete implementation used in the practical.

---

# 21. YOLO Detection Pipeline

A practical YOLO system can be understood as:

```text
Input image / frame
       ↓
Resize / preprocess
       ↓
YOLO model
       ↓
raw detection predictions
       ↓
confidence filtering
       ↓
NMS / postprocessing
       ↓
final boxes
       ↓
class labels + scores
       ↓
visualized output
```

This is the most useful operational diagram for the practical.

---

# 22. Detection Anatomy

For each final detection:

```text
┌───────────────────────────┐
│        person             │
│      confidence           │
│                           │
│   x1,y1        x2,y1      │
│      ┌──────────────┐     │
│      │    object    │     │
│      └──────────────┘     │
│   x1,y2        x2,y2      │
└───────────────────────────┘
```

The output combines:

\[
\boxed{\text{what}+\text{where}+\text{score}}
\]

---

# 23. Class Score and Box Quality Are Different

A model may be highly confident that:

```text
object = car
```

while its box is poorly localized.

Similarly, the box can be spatially good but the class can be wrong.

Therefore detection quality has multiple dimensions:

```text
classification quality
+
localization quality
```

This is why IoU and classification metrics both matter.

---

# 24. Detection Evaluation

At a simplified level, a detection is considered a correct match when:

```text
predicted class matches
+
IoU exceeds chosen criterion
```

Unmatched predictions may become false positives.

Unmatched ground-truth objects may become false negatives.

The exact matching and evaluation protocol depends on the benchmark.

---

# 25. Precision and Recall for Detection

Conceptually:

\[
\text{Precision}
=
\frac{TP}{TP+FP}
\]

\[
\text{Recall}
=
\frac{TP}{TP+FN}.
\]

### High precision

Few false alarms.

### High recall

Few missed objects.

A surveillance system may prefer higher recall in some situations, while another system may prioritize avoiding false alarms.

---

# 26. Mean Average Precision — Conceptual Introduction

Object-detection benchmarks often use **AP** and **mAP**.

At a high level:

```text
prediction ranking by confidence
        ↓
precision–recall behaviour
        ↓
area / summary measure
        ↓
AP per class
        ↓
mAP across classes
```

Different detection benchmarks specify different IoU thresholds and averaging procedures.

Do not treat “mAP” as one universal formula independent of evaluation protocol.

For this syllabus, understanding what it measures is more important than reproducing every benchmark convention.

---

# 27. Practical YOLO Example

Suppose an image produces:

```text
person  0.94  [100,80,250,420]
car     0.87  [300,200,580,390]
dog     0.61  [650,220,760,410]
```

After thresholding at 0.70:

```text
person
car
```

remain.

The dog is removed.

If two person boxes overlap strongly, NMS may retain only the best one.

---

# 28. Image-Level vs Object-Level Output

Classification:

```text
image → one/few class labels
```

Detection:

```text
image
→ object 1
→ object 2
→ object 3
→ ...
```

Therefore one image can contain many detections.

This is a fundamental task difference.

---

# 29. Video Detection

For video:

```text
Frame 1
→ YOLO
→ detections

Frame 2
→ YOLO
→ detections

Frame 3
→ YOLO
→ detections
```

This can produce a real-time stream of predictions.

Detection itself does not automatically provide persistent object identity across frames.

That is a tracking problem.

This distinction becomes important in C30.

---

# 30. Detection vs Tracking

### Detection

```text
What objects are here?
Where are they now?
```

### Tracking

```text
Is this the same object as before?
Where did it move?
```

A system may combine:

```text
YOLO detection
+
tracker
```

to maintain object identities across frames.

C30 will address motion analysis and tracking.

---

# 31. Practical 9 — Syllabus Alignment

The university practical states:

> **Object Detection using YOLO — Detect objects in real-time using YOLO.** fileciteturn4file0L80-L84

The requirements include:

- Python;
- pretrained YOLO weights;
- webcam.

Therefore the lab should explicitly demonstrate:

```text
webcam
 ↓
frame capture
 ↓
preprocessing
 ↓
pretrained YOLO
 ↓
detections
 ↓
confidence filtering
 ↓
NMS/postprocessing
 ↓
bounding boxes
 ↓
labels
 ↓
real-time display
```

---

# 32. Why a Pretrained Model Is Appropriate

The practical explicitly mentions pretrained YOLO weights. fileciteturn4file0L80-L84

For an introductory engineering lab, using pretrained weights makes it possible to study:

```text
model loading
+
inference
+
detection output
+
real-time pipeline
```

without requiring a complete detector to be trained from scratch.

Training a YOLO detector is a substantially different practical problem.

---

# 33. Implementation Architecture

A robust practical program can be structured as:

```text
capture.py
    ↓
preprocess
    ↓
detector.py
    ↓
postprocess.py
    ↓
visualize.py
    ↓
main.py
```

Or, for a smaller lab:

```text
load model
→ open webcam
→ read frame
→ infer
→ filter
→ draw
→ display
```

The second is sufficient for a university demonstration, while modular structure is better for reusable engineering code.

---

# 34. Python/OpenCV-Style Webcam Pipeline

A generic implementation can be:

```python
from __future__ import annotations

import cv2


def main() -> None:
    capture = cv2.VideoCapture(0)

    if not capture.isOpened():
        raise RuntimeError("Could not open webcam.")

    try:
        while True:
            ok, frame = capture.read()

            if not ok:
                raise RuntimeError("Could not read webcam frame.")

            # Run the chosen YOLO model here.
            # The exact API depends on the model implementation.
            #
            # detections = model(frame)

            # Visualize detections here.

            cv2.imshow("YOLO", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
```

The detection call is intentionally abstract because the syllabus specifies YOLO rather than one specific library/version.

---

# 35. Why Model Version Must Be Recorded

A lab report should record:

```text
model family
model variant
weights/source
input size
confidence threshold
IoU/NMS threshold
hardware
software/library version
```

Otherwise:

```text
"YOLO worked"
```

is not a reproducible experiment.

This is particularly important because YOLO is a family, not one fixed implementation.

---

# 36. Preprocessing and Input Resolution

Detection models often resize input frames before inference.

Conceptually:

```text
webcam frame
640×480
   ↓
resize / letterbox
model input dimensions
   ↓
inference
```

The system then maps detections back to the original frame coordinates.

Incorrect coordinate scaling can cause boxes to appear shifted or incorrectly sized.

---

# 37. Letterboxing

A common preprocessing strategy preserves aspect ratio by:

```text
resize while preserving ratio
+
pad remaining area
```

Conceptually:

```text
original
┌──────────────┐
│              │
│              │
└──────────────┘

resize + pad

┌────────────────┐
│  ████████████  │
│  ████████████  │
│                │
└────────────────┘
```

Exact preprocessing depends on the model implementation.

---

# 38. Common Detection Errors

### False positive

Detector reports an object that is not present.

### False negative

Object is present but detector misses it.

### Localization error

Correct class but poor bounding box.

### Class confusion

Correct region but incorrect class.

### Duplicate detections

Multiple boxes for the same object.

### Small-object failure

Tiny objects contain limited visual evidence.

### Occlusion

Part of an object is hidden.

### Domain shift

Training and deployment environments differ.

---

# 39. Confidence Threshold Trade-off

Suppose detections have:

```text
0.97
0.89
0.58
0.42
0.31
```

Threshold 0.50:

```text
0.97
0.89
0.58
```

Threshold 0.80:

```text
0.97
0.89
```

The higher threshold removes weaker detections but may also remove real objects.

Thus:

\[
\boxed{\text{threshold selection is an application decision}}
\]

---

# 40. Small Object Problem

Suppose a person occupies only:

\[
12\times18
\]

pixels of a high-resolution frame.

After resizing into a model input, the object may contain very little detail.

This can make detection difficult.

Possible engineering responses include:

- suitable input resolution;
- model choice;
- multi-scale features;
- better data;
- task-specific tuning.

---

# 41. Occlusion

Consider:

```text
person A
██████████

person B behind A
   █████
```

The visible evidence for B is incomplete.

Detectors must infer object presence from partial evidence.

This is a fundamental computer-vision challenge, not simply an implementation bug.

---

# 42. Real-Time Performance

Frame rate depends on:

\[
FPS
=
\frac{\text{processed frames}}
{\text{time}}.
\]

For example, if a system processes 150 frames in 5 seconds:

\[
FPS=\frac{150}{5}=30.
\]

This is an average throughput measure.

It does not guarantee uniform frame latency.

---

# 43. Latency vs Throughput

### Throughput

How many frames per second can be processed.

### Latency

How long one frame takes to move through the pipeline.

A system can have good average throughput but still experience occasional large latency spikes.

For real-time applications, both matter.

---

# 44. Detection Pipeline Bottlenecks

A webcam system spends time in:

```text
capture
→ preprocessing
→ model inference
→ postprocessing
→ drawing
→ display
```

Optimizing only inference may not maximize end-to-end FPS.

This is an important engineering insight.

---

# 45. Model Size Trade-off

YOLO-style systems often provide multiple model sizes or capacity levels.

Conceptually:

```text
smaller model
→ faster
→ less compute
→ potentially lower accuracy

larger model
→ slower
→ more compute
→ potentially higher accuracy
```

The actual trade-off varies by model family and hardware.

---

# 46. Classification Backbone vs Detector

C27 introduced VGG/ResNet as CNN architecture families.

A detector adds detection-specific output logic:

```text
backbone
 ↓
feature maps
 ↓
detection head
 ↓
boxes + class scores
```

YOLO is commonly described as an integrated detection architecture family rather than simply “a classifier with boxes added afterward.”

---

# 47. Exam Lens

## 2-mark questions

**Define object detection.**  
The task of identifying object classes and locating object instances in an image, commonly using bounding boxes.

**What is IoU?**

\[
IoU=
\frac{A_{\cap}}{A_{\cup}}.
\]

**What is NMS?**  
A postprocessing method that suppresses redundant overlapping detections.

**Expand YOLO.**  
You Only Look Once.

---

# 48. 5-Mark Question

### Differentiate image classification and object detection.

Use:

```text
classification
→ image-level class

object detection
→ multiple object instances
→ class + location + confidence
```

Then explain bounding boxes.

---

# 49. 10-Mark Question

### Explain YOLO object detection.

Recommended structure:

1. detection problem;
2. bounding boxes;
3. class prediction;
4. confidence scores;
5. YOLO concept;
6. preprocessing;
7. model inference;
8. predictions;
9. thresholding;
10. NMS;
11. final detections;
12. real-time video workflow;
13. advantages;
14. limitations;
15. deployment considerations.

---

# 50. Numerical Practice — IoU

Ground truth:

\[
(0,0,100,100)
\]

Prediction:

\[
(50,50,150,150).
\]

Calculate:

1. intersection area;
2. union area;
3. IoU.

Intersection:

\[
50\times50=2500.
\]

Each box area:

\[
100\times100=10{,}000.
\]

Union:

\[
10{,}000+10{,}000-2500
=
17{,}500.
\]

Therefore:

\[
IoU=
\frac{2500}{17{,}500}
=
\boxed{0.142857\ldots}.
\]

---

# 51. Numerical Practice — FPS

A detector processes:

\[
240
\]

frames in:

\[
8
\]

seconds.

Then:

\[
FPS=\frac{240}{8}
=
\boxed{30}.
\]

---

# 52. Chapter Checkpoint

### Q1

What information does a detection output contain that ordinary classification does not?

### Q2

Why is IoU needed?

### Q3

Why can a high confidence score coexist with a poor box?

### Q4

What problem does NMS solve?

### Q5

Why is YOLO called a family rather than one immutable algorithm?

### Q6

Why must the concrete YOLO model/version be recorded in a lab report?

### Q7

Why can raising the confidence threshold increase precision but reduce recall?

### Q8

What is the difference between detection and tracking?

---

# 53. One-Page Recall Sheet

```text
OBJECT DETECTION
│
├── Output
│   ├── class
│   ├── bounding box
│   └── confidence
│
├── Box
│   ├── x1,y1
│   └── x2,y2
│
├── Evaluation
│   ├── IoU
│   ├── precision
│   ├── recall
│   └── AP / mAP
│
├── Postprocessing
│   ├── confidence threshold
│   └── NMS
│
└── YOLO
    ├── one-stage family
    ├── unified detection
    ├── real-time focus
    └── version/model dependent
```

---

# 54. Cross-Book Links

| Layer | Connection |
|---|---|
| MAIN | C28 explains detection and YOLO |
| MATH | Bounding boxes, IoU, FPS |
| LAB | Practical 9 — real-time YOLO detection |
| CODE | Python + webcam + pretrained weights |
| EXAM | Classification vs detection, YOLO pipeline |
| PRACTICE | IoU calculations, threshold reasoning, NMS |
| RESOURCE | Course-specified deep-learning/computer-vision references |
| ASSETS | Detection anatomy, IoU diagram, YOLO pipeline, NMS illustration |
| MASTER | Dependency into C30 video/motion and completion of YOLO practical branch |

---

# 55. Final Chapter Summary

The key transformation from classification to detection is:

\[
\boxed{
\text{What?}
\rightarrow
\text{What + Where?}
}
\]

A typical detection output contains:

\[
\boxed{
\text{class}+\text{box}+\text{confidence}
}
\]

The central geometric evaluation concept is:

\[
\boxed{
IoU=
\frac{\text{intersection}}
{\text{union}}
}
\]

The practical YOLO pipeline is:

```text
webcam
→ frame
→ preprocess
→ YOLO
→ confidence filtering
→ NMS
→ boxes + labels
→ display
```

The university syllabus specifically requires YOLO and a real-time YOLO object-detection practical, so the chapter and lab must preserve that direct connection. fileciteturn4file0L48-L52 fileciteturn4file0L80-L84

The next transition is:

```text
C28
detect objects in one frame
        ↓
C30
understand change and motion across frames
```

Before that, C29 covers another advanced syllabus requirement:

```text
image denoising
+
autoencoders
```

---

**Next chapter:** C29 — Image Denoising with Autoencoders
