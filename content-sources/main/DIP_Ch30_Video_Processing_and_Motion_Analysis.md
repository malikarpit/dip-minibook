---
id: "C30"
title: "Video Processing and Motion Analysis"
layer: "MAIN"
part: "V — From DIP to Intelligent Vision"
unit: "Unit IV"
version: "1.0"
status: "PRODUCTION"
syllabus_scope: "Introduction to Video Processing and Motion Analysis; Practical 10 — Motion Tracking in Video using optical flow"
tags:
  - digital-image-processing
  - video-processing
  - motion-analysis
  - optical-flow
  - motion-detection
  - tracking
  - opencv
prerequisites:
  - "C08 — Spatial Filtering and Convolution"
  - "C15 — Image Segmentation Fundamentals"
  - "C25 — Image Classification"
  - "C28 — Object Detection and YOLO"
related_math:
  - "Image gradients"
  - "Optical flow constraint"
  - "Vector fields"
  - "Linear equations"
related_lab:
  - "LAB-10 — Motion Tracking in Video"
related_code:
  - "CODE-10 — Optical Flow and Motion Analysis"
related_exam:
  - "EXAM-Video-and-Motion"
related_practice:
  - "PRACTICE-Optical-Flow"
---

# C30 — Video Processing and Motion Analysis

> **Chapter thesis:** Video processing extends image processing into the temporal dimension, allowing systems to detect, estimate, and track motion by comparing information across successive frames.

---

# 1. Why This Chapter Exists

A single image gives a spatial snapshot.

A video provides:

\[
\boxed{\text{space}+\text{time}}
\]

The university syllabus explicitly requires:

- Introduction to Video Processing;
- Motion Analysis.

The tenth practical requires:

> **Motion Tracking in Video — Implement motion tracking using optical flow.** fileciteturn4file0L48-L52 fileciteturn4file0L82-L86

This chapter therefore focuses on the transition:

```text
image
→ sequence of images
→ temporal change
→ motion information
→ tracking / interpretation
```

---

# 2. Learning Contract

After this chapter, you should be able to:

- define a digital video as a sequence of frames;
- explain frame rate and temporal sampling;
- distinguish spatial resolution from temporal resolution;
- explain video as a 3-D/4-D data structure depending on channel convention;
- distinguish frame differencing, background subtraction, motion detection and tracking;
- explain motion vectors conceptually;
- explain optical flow;
- state the optical-flow constraint equation;
- explain the brightness-constancy assumption;
- explain the aperture problem;
- distinguish sparse and dense optical flow;
- describe common optical-flow algorithms at an introductory level;
- implement simple optical-flow motion visualization in OpenCV;
- interpret motion vectors;
- connect YOLO detection to tracking;
- identify common motion-analysis failure modes.

---

# 3. Video Is a Sequence of Frames

A video can be represented as:

\[
I(x,y,t)
\]

where:

- \(x\) = horizontal position;
- \(y\) = vertical position;
- \(t\) = time/frame index.

Thus:

```text
Frame 1
Frame 2
Frame 3
...
Frame N
```

Each frame is an image.

The new dimension is time.

---

# 4. Spatial vs Temporal Information

### Spatial

Variation across:

\[
x,y.
\]

### Temporal

Variation across:

\[
t.
\]

A moving object changes its location over time.

Therefore motion can be inferred from:

\[
I(x,y,t)
\quad\text{and}\quad
I(x,y,t+\Delta t).
\]

---

# 5. Frame Rate

Frame rate is commonly measured in frames per second:

\[
FPS=
\frac{\text{number of frames}}{\text{seconds}}.
\]

For example:

\[
30\text{ FPS}
\]

means approximately 30 frames are captured/displayed each second.

Higher temporal sampling can capture faster changes more smoothly.

But it can also increase:

- storage;
- processing;
- transmission requirements.

---

# 6. Temporal Sampling

A high-speed movement may be under-sampled at a low frame rate.

Conceptually:

```text
fast motion
↓
few sampled frames
↓
large apparent jumps
```

At a higher frame rate:

```text
fast motion
↓
more temporal samples
↓
smaller frame-to-frame displacement
```

This is analogous to spatial sampling from C03, but now the sampling axis is time.

---

# 7. Video Data Shape

A grayscale video can be represented conceptually as:

\[
T\times H\times W.
\]

An RGB video can be:

\[
T\times H\times W\times3.
\]

For a batch of videos:

\[
B\times T\times H\times W\times C.
\]

The exact tensor ordering depends on the software framework.

---

# 8. Video Processing Pipeline

A generic system is:

```text
video stream
   ↓
frame capture
   ↓
frame preprocessing
   ↓
motion / feature analysis
   ↓
detection / segmentation / optical flow
   ↓
temporal interpretation
   ↓
tracking / event decision
   ↓
output
```

Different systems use different subsets of these stages.

---

# 9. Frame Differencing

One of the simplest motion-detection methods is frame differencing.

Given two grayscale frames:

\[
I_t(x,y)
\]

and:

\[
I_{t-1}(x,y),
\]

calculate:

\[
D(x,y)
=
|I_t(x,y)-I_{t-1}(x,y)|.
\]

Large values indicate significant pixel change.

---

# 10. Thresholding the Difference

A binary motion mask can be:

\[
M(x,y)=
\begin{cases}
1,&D(x,y)>T\\
0,&D(x,y)\le T
\end{cases}
\]

where \(T\) is a threshold.

This converts change into a binary motion region.

The approach is simple but sensitive to:

- camera motion;
- illumination change;
- noise;
- shadows.

---

# 11. Worked Frame-Difference Example

Suppose:

\[
I_{t-1}(x,y)=100
\]

and:

\[
I_t(x,y)=130.
\]

Then:

\[
D=|130-100|=30.
\]

If:

\[
T=20,
\]

then:

\[
D>T
\]

and the pixel is marked as changed.

If:

\[
T=40,
\]

it is not marked.

Thus threshold selection controls sensitivity.

---

# 12. Motion Detection vs Tracking

### Motion detection

Answers:

> Where did something change?

### Tracking

Answers:

> Where is the same moving object over time?

A binary motion mask does not automatically establish object identity.

Tracking requires temporal association.

---

# 13. Background Subtraction

If the camera is stationary, a background model can be used.

Conceptually:

```text
current frame
      ↓
compare with background
      ↓
foreground mask
```

This can isolate moving objects from a relatively stable scene.

But it can struggle with:

- dynamic backgrounds;
- lighting changes;
- camera motion;
- shadows.

---

# 14. Motion Vector

A motion vector describes displacement:

\[
\mathbf{v}
=
(u,v)
\]

where:

- \(u\) = horizontal displacement;
- \(v\) = vertical displacement.

Example:

\[
\mathbf{v}=(4,-2)
\]

means approximately:

```text
4 pixels right
2 pixels up
```

under the selected coordinate convention.

---

# 15. Optical Flow

Optical flow estimates apparent motion of image structures between frames.

It is often represented as a vector field:

\[
\mathbf{v}(x,y)
=
(u(x,y),v(x,y)).
\]

Conceptually:

```text
Frame t
   ↓
optical-flow estimation
   ↓
vector field
   ↓
motion interpretation
```

---

# 16. Brightness Constancy Assumption

A classical starting assumption is that the brightness of a moving point remains approximately constant over a small time interval.

Suppose:

\[
I(x,y,t)
\]

tracks a moving point.

Then:

\[
I(x,y,t)
\approx
I(x+dx,y+dy,t+dt).
\]

This assumption allows a motion relationship to be derived.

---

# 17. Deriving the Optical-Flow Constraint

Start with:

\[
I(x,y,t)
=
I(x+dx,y+dy,t+dt).
\]

Apply a first-order Taylor expansion:

\[
I(x+dx,y+dy,t+dt)
\approx
I
+
I_xdx
+
I_ydy
+
I_tdt.
\]

Therefore:

\[
I_xdx+I_ydy+I_tdt=0.
\]

Divide by \(dt\):

\[
\boxed{
I_xu+I_yv+I_t=0
}
\]

where:

\[
u=\frac{dx}{dt},\qquad
v=\frac{dy}{dt}.
\]

This is the **optical-flow constraint equation**.

---

# 18. Meaning of the Variables

\[
I_x
\]

= spatial intensity gradient in the x direction.

\[
I_y
\]

= spatial intensity gradient in the y direction.

\[
I_t
\]

= temporal intensity change.

\[
u,v
\]

= optical-flow velocity components.

So:

\[
I_xu+I_yv+I_t=0
\]

states that under the brightness-constancy approximation, the observed intensity change is related to image motion.

---

# 19. Why One Equation Is Not Enough

Unknowns:

\[
u,v.
\]

One equation contains two unknowns.

Therefore the equation alone cannot uniquely determine motion.

This is the basis of the **aperture problem**.

Additional assumptions or constraints are needed.

---

# 20. Aperture Problem

Imagine a long straight edge.

You may detect motion perpendicular to the edge more reliably than motion along the edge.

For example:

```text
──────────────
──────────────
```

A small local window may not contain enough information to determine the full 2-D motion.

Thus:

> **Local image information can be insufficient to uniquely determine 2-D motion.**

Optical-flow algorithms add spatial smoothness, feature structure, or other constraints to solve the problem.

---

# 21. Sparse vs Dense Optical Flow

### Sparse

Estimate flow at selected points/features.

```text
•       →
      •
  •      ↓
```

Advantages:

- less computation;
- useful for tracking distinctive points.

### Dense

Estimate flow for many/all pixels.

```text
→ → → ↓ ↘
→ → ↓ ↓ ↘
→ ↓ ↓ ↘ →
```

Advantages:

- rich motion field;
- useful for motion visualization and scene analysis.

---

# 22. Lucas–Kanade — Conceptual Introduction

Lucas–Kanade is a classical sparse/dense-local optical-flow approach.

The basic assumption is that nearby pixels have similar motion.

A local window provides multiple equations:

\[
I_xu+I_yv=-I_t.
\]

The equations can be organized as:

\[
A\mathbf{v}=\mathbf{b}
\]

where:

\[
\mathbf{v}=
\begin{bmatrix}
u\\v
\end{bmatrix}.
\]

A least-squares solution can estimate the motion.

---

# 23. Lucas–Kanade Matrix Form

For a local window with \(n\) pixels:

\[
A=
\begin{bmatrix}
I_{x1} & I_{y1}\\
I_{x2} & I_{y2}\\
\vdots & \vdots\\
I_{xn} & I_{yn}
\end{bmatrix}
\]

and:

\[
\mathbf{b}=
\begin{bmatrix}
-I_{t1}\\
-I_{t2}\\
\vdots\\
-I_{tn}
\end{bmatrix}.
\]

Then:

\[
A\mathbf{v}=\mathbf{b}.
\]

A least-squares estimate is:

\[
\boxed{
\mathbf{v}
=
(A^TA)^{-1}A^T\mathbf{b}
}
\]

when the inverse exists and the conditioning is suitable.

---

# 24. Why the Local Window Helps

One pixel gives:

\[
I_xu+I_yv=-I_t.
\]

Many nearby pixels give multiple equations.

That can make:

\[
u,v
\]

estimable.

The assumption is that the local region shares approximately the same motion.

This is a powerful but imperfect assumption.

---

# 25. Farnebäck — Conceptual Introduction

Farnebäck optical flow is a dense optical-flow method based on local polynomial representations of image neighbourhoods.

At a university introductory level, remember:

```text
Lucas–Kanade
→ local point/window-based estimation

Farnebäck
→ dense flow estimation
```

The practical can use OpenCV's available implementation without requiring a full derivation of the underlying polynomial model.

---

# 26. Optical Flow Visualization

A useful visualization is:

```text
image frame
+
arrows representing motion vectors
```

For example:

```text
object →→→→
      ↗
   ↗
```

Vector direction indicates motion direction.

Vector magnitude indicates estimated displacement/speed over the selected time interval.

---

# 27. Motion Magnitude

Given:

\[
\mathbf{v}=(u,v),
\]

the magnitude is:

\[
|\mathbf{v}|
=
\sqrt{u^2+v^2}.
\]

Example:

\[
u=3,\quad v=4.
\]

Then:

\[
|\mathbf{v}|
=
\sqrt{3^2+4^2}
=
\sqrt{25}
=
\boxed5.
\]

---

# 28. Motion Direction

The direction angle can be represented as:

\[
\theta=
\operatorname{atan2}(v,u).
\]

For:

\[
(u,v)=(1,1),
\]

the direction is approximately:

\[
45^\circ
\]

under the mathematical coordinate convention.

Image-coordinate y direction may point downward, so visualization code must handle coordinate conventions carefully.

---

# 29. Optical Flow Does Not Equal Physical Velocity

An image-space vector such as:

\[
(5,0)
\]

means approximately 5 pixels of apparent horizontal displacement over the selected time interval.

It does not automatically mean:

```text
5 metres/second
```

To infer physical velocity, additional scene geometry, calibration, depth and timing information are needed.

This is an important engineering distinction.

---

# 30. Camera Motion

Optical flow can be generated by:

```text
object motion
+
camera motion
+
both
```

If the camera moves, the background can produce large flow.

Therefore a system may need:

- camera stabilization;
- background modeling;
- global-motion estimation;
- inertial information;
- geometric compensation.

---

# 31. Lighting Changes

Brightness constancy can fail when illumination changes.

Example:

```text
same object
before light change → dark
after light change  → bright
```

Pixel intensities change even without object motion.

Thus:

\[
I_t\neq0
\]

does not necessarily imply object motion.

---

# 32. Occlusion

An object may disappear behind another object.

Optical flow cannot always maintain a continuous correspondence through the occluded region.

Tracking systems must therefore reason about:

```text
appearance
+
motion
+
visibility
+
identity
```

---

# 33. Motion Blur

Fast motion can blur objects.

This makes feature localization and correspondence more difficult.

The system may observe:

```text
sharp object
→ blurred region
```

rather than a simple translated copy.

This connects motion analysis to image-formation and restoration ideas from earlier chapters.

---

# 34. YOLO + Tracking

C28 detects objects.

C30 can maintain temporal information.

A practical system can combine:

```text
frame
 ↓
YOLO detection
 ↓
boxes
 ↓
tracker
 ↓
object identity
 ↓
trajectory
```

or:

```text
frame
 ↓
feature points
 ↓
optical flow
 ↓
motion estimates
```

These are related but distinct strategies.

---

# 35. Feature Tracking with Optical Flow

Suppose selected feature points are:

\[
P_t=
\{p_1,p_2,\ldots,p_n\}.
\]

Optical flow estimates:

\[
p_i(t+\Delta t)
\]

from their previous positions.

Then trajectories can be constructed:

```text
p(t0)
 ↓
p(t1)
 ↓
p(t2)
 ↓
p(t3)
```

This turns local motion vectors into temporal tracks.

---

# 36. OpenCV Lucas–Kanade Example

A common educational implementation is:

```python
from __future__ import annotations

import cv2
import numpy as np


cap = cv2.VideoCapture("input.mp4")

if not cap.isOpened():
    raise RuntimeError("Could not open the video.")

feature_params = dict(
    maxCorners=100,
    qualityLevel=0.3,
    minDistance=7,
    blockSize=7,
)

lk_params = dict(
    winSize=(15, 15),
    maxLevel=2,
    criteria=(
        cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
        10,
        0.03,
    ),
)

ok, first_frame = cap.read()
if not ok:
    cap.release()
    raise RuntimeError("Could not read the first frame.")

old_gray = cv2.cvtColor(
    first_frame,
    cv2.COLOR_BGR2GRAY,
)

old_points = cv2.goodFeaturesToTrack(
    old_gray,
    mask=None,
    **feature_params,
)

while True:
    ok, frame = cap.read()
    if not ok:
        break

    frame_gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY,
    )

    if old_points is not None:
        new_points, status, _ = cv2.calcOpticalFlowPyrLK(
            old_gray,
            frame_gray,
            old_points,
            None,
            **lk_params,
        )

        if new_points is not None:
            valid_new = new_points[status == 1]
            valid_old = old_points[status == 1]

            for (x1, y1), (x2, y2) in zip(valid_old, valid_new):
                cv2.arrowedLine(
                    frame,
                    (int(x1), int(y1)),
                    (int(x2), int(y2)),
                    (255, 255, 255),
                    1,
                    tipLength=0.25,
                )

            old_points = valid_new.reshape(-1, 1, 2)

    old_gray = frame_gray

    cv2.imshow("Optical Flow", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
```

This is a practical Lucas–Kanade feature-tracking demonstration.

---

# 37. Why Detect Features First?

Lucas–Kanade tracking is commonly applied to selected points rather than blindly tracking every pixel.

Therefore:

```text
frame
→ detect good feature points
→ track those points
→ visualize trajectories
```

Feature selection improves the usefulness of sparse tracking.

---

# 38. Feature Quality

Good tracking points tend to have strong spatial structure.

A flat region:

```text
██████████
██████████
```

contains little directional information.

A corner:

```text
█████.....
█████.....
█████.....
.....     
.....
```

provides stronger local constraints.

This connects optical flow to feature detection from C19/C20.

---

# 39. Dense Optical Flow Example

OpenCV also provides dense-flow methods.

Conceptually:

```python
flow = cv2.calcOpticalFlowFarneback(
    previous_gray,
    current_gray,
    None,
    0.5,
    3,
    15,
    3,
    5,
    1.2,
    0,
)
```

The result contains approximately:

```text
flow[..., 0] → horizontal displacement
flow[..., 1] → vertical displacement
```

Parameter meanings depend on the API and should be documented in the practical.

---

# 40. Converting Flow to Magnitude and Angle

```python
magnitude, angle = cv2.cartToPolar(
    flow[..., 0],
    flow[..., 1],
)
```

Then:

```text
magnitude
→ how much apparent motion

angle
→ direction
```

A visualization can map the vector field into arrows or colour-coded direction/magnitude displays.

---

# 41. Optical Flow Practical Pipeline

For the university practical:

```text
Video
 ↓
Read first frame
 ↓
Convert to grayscale
 ↓
Choose feature points / use dense flow
 ↓
Read next frame
 ↓
Estimate optical flow
 ↓
Filter invalid/poor tracks
 ↓
Compute displacement
 ↓
Visualize vectors
 ↓
Repeat for next frame
```

The practical requirement specifically names optical flow, so the experiment should make the temporal correspondence visible rather than merely run a prebuilt tracker. fileciteturn4file0L82-L86

---

# 42. Tracking an Object's Average Motion

Suppose a set of feature points inside an object produces vectors:

\[
(2,1),\quad
(3,2),\quad
(1,2),\quad
(2,1).
\]

Mean horizontal motion:

\[
\bar u=
\frac{2+3+1+2}{4}
=
2.
\]

Mean vertical motion:

\[
\bar v=
\frac{1+2+2+1}{4}
=
1.5.
\]

Thus average motion is approximately:

\[
\boxed{(2,\ 1.5)}.
\]

This can be used as a simple object-motion estimate when the selected points belong to the same rigid moving region.

---

# 43. Why Average Flow Can Fail

If the feature points include:

```text
object
+
background
```

the mean vector mixes different motions.

Likewise, for a rotating object, different points can move in different directions.

Therefore motion statistics should be computed over meaningful regions or tracked objects.

---

# 44. Motion Segmentation

A motion field can be converted into regions.

Conceptually:

```text
flow magnitude
      ↓
threshold
      ↓
motion mask
      ↓
connected components
      ↓
moving regions
```

This connects motion analysis to segmentation.

---

# 45. Temporal Smoothing

Frame-by-frame measurements can fluctuate.

A system may smooth motion estimates over time:

```text
raw:
2.1, 2.8, 1.7, 3.0, ...

smoothed:
2.2, 2.3, 2.4, ...
```

Temporal filtering can improve stability but can also introduce lag.

Thus:

\[
\boxed{\text{stability} \leftrightarrow \text{responsiveness}}
\]

is another engineering trade-off.

---

# 46. Frame Skipping

A system can estimate motion between:

```text
t and t+1
```

or:

```text
t and t+2
```

Larger time gaps can produce larger apparent displacement, potentially making correspondence more difficult.

Smaller gaps give smaller movement but require more processing.

---

# 47. Real-Time Motion Analysis

A real-time pipeline must process frames fast enough.

If input rate is:

\[
30\text{ FPS}
\]

and the algorithm processes only:

\[
10\text{ FPS},
\]

frames accumulate or are dropped depending on system design.

Therefore real-time design may require:

- lower resolution;
- fewer tracked points;
- smaller search windows;
- frame skipping;
- hardware acceleration;
- lightweight algorithms.

---

# 48. Video Processing Applications

The syllabus specifically mentions motion analysis, and video processing has applications such as:

- surveillance;
- traffic monitoring;
- sports analysis;
- human motion understanding;
- robotics;
- industrial monitoring.

These should be treated as application contexts rather than a replacement for the underlying motion-analysis concepts.

---

# 49. Healthcare Connection

Video or motion analysis can support applications such as:

```text
patient movement
gait analysis
rehabilitation monitoring
```

But such applications require careful validation.

Image/video measurements can be affected by:

- camera placement;
- occlusion;
- lighting;
- calibration;
- subject variation.

The existence of a computer-vision output does not automatically make it clinically valid.

---

# 50. Surveillance Connection

A simplified surveillance pipeline may be:

```text
camera
 ↓
video frames
 ↓
motion detection
 ↓
object detection
 ↓
tracking
 ↓
event rule
 ↓
alert / recording
```

This integrates:

```text
C28 detection
+
C30 temporal analysis
```

It also introduces practical issues such as privacy, false alarms and camera motion.

---

# 51. Motion Analysis vs Optical Flow

Optical flow is one technique for motion estimation.

Motion analysis is broader.

```text
Motion analysis
├── frame difference
├── background subtraction
├── optical flow
├── feature tracking
├── object tracking
└── trajectory analysis
```

Thus:

\[
\boxed{\text{optical flow} \subset \text{motion analysis}}
\]

This distinction is useful in exams and system design.

---

# 52. Common Traps

### Trap 1 — Difference between frames always means object motion.

False.

It can also be caused by illumination, sensor noise or camera motion.

### Trap 2 — Optical flow gives real-world speed directly.

False.

It gives image-space apparent motion unless additional geometry/calibration is available.

### Trap 3 — Every pixel has a unique reliable flow vector.

False.

Textureless regions, occlusion and ambiguity make estimation difficult.

### Trap 4 — Tracking and detection are the same.

False.

Detection finds objects; tracking links observations over time.

### Trap 5 — Brightness constancy always holds.

False.

Lighting and appearance changes can violate it.

### Trap 6 — More frames always improve tracking.

Not necessarily. More temporal samples increase compute and storage; frame spacing also matters.

---

# 53. Exam Lens

## 2-mark questions

**What is video processing?**  
Processing a temporal sequence of image frames to extract, enhance, interpret or transform spatial and temporal information.

**Define optical flow.**  
The estimated apparent motion of image structures represented as vectors across an image.

**Write the optical-flow constraint equation.**

\[
\boxed{I_xu+I_yv+I_t=0}
\]

---

# 54. 5-Mark Question

### Explain optical flow.

Recommended structure:

```text
successive frames
→ brightness-constancy assumption
→ image gradients
→ optical-flow constraint
→ motion vectors
→ sparse/dense flow
→ interpretation
```

Mention the aperture problem.

---

# 55. 10-Mark Question

### Explain video motion analysis using optical flow.

Include:

1. video/frame concept;
2. temporal dimension;
3. frame differencing;
4. motion detection;
5. brightness constancy;
6. derivation of constraint equation;
7. aperture problem;
8. sparse vs dense flow;
9. feature tracking;
10. visualization;
11. practical implementation;
12. limitations.

---

# 56. Numerical Practice — Optical Flow

Given:

\[
I_x=2,\quad
I_y=3,\quad
I_t=-5.
\]

The optical-flow constraint is:

\[
2u+3v-5=0.
\]

Therefore:

\[
2u+3v=5.
\]

There are infinitely many \((u,v)\) pairs satisfying this equation.

This demonstrates why another constraint is required to determine unique 2-D motion.

---

# 57. Numerical Practice — Motion Magnitude

Given:

\[
(u,v)=(6,8),
\]

calculate:

\[
|\mathbf v|
=
\sqrt{6^2+8^2}
=
\sqrt{100}
=
\boxed{10}.
\]

---

# 58. Chapter Checkpoint

### Q1

Why is video different from a sequence of unrelated images?

### Q2

What is the difference between motion detection and tracking?

### Q3

Derive:

\[
I_xu+I_yv+I_t=0.
\]

### Q4

Why does the optical-flow equation alone not uniquely determine \(u\) and \(v\)?

### Q5

What is the difference between sparse and dense optical flow?

### Q6

Why can camera movement create optical flow?

### Q7

Why is optical flow not automatically physical object velocity?

### Q8

How can YOLO detections be combined with tracking?

---

# 59. One-Page Recall Sheet

```text
VIDEO
│
├── Frame sequence
│   └── I(x,y,t)
│
├── Temporal change
│   ├── frame difference
│   └── background subtraction
│
├── Motion
│   └── optical flow
│        I_x u + I_y v + I_t = 0
│
├── Optical flow
│   ├── sparse
│   └── dense
│
├── Tracking
│   └── link observations over time
│
└── Applications
    ├── surveillance
    ├── traffic
    ├── sports
    ├── robotics
    └── monitoring
```

---

# 60. Practical 10 — Motion Tracking in Video

The university practical requires:

> **Implement motion tracking using optical flow.** fileciteturn4file0L82-L86

A strong experiment should include:

```text
1. Load video/webcam
2. Read first frame
3. Convert to grayscale
4. Detect trackable feature points
5. Read next frame
6. Estimate optical flow
7. Reject invalid tracks
8. Draw motion vectors
9. Repeat
10. Save/display result
11. Measure processing speed
12. Interpret failure cases
```

### Evidence to collect

| Evidence | Purpose |
|---|---|
| Original frame | Baseline |
| Feature points | Show what is tracked |
| Vector overlay | Show motion |
| Multiple frames | Show temporal change |
| Trajectory | Show tracking over time |
| FPS | Quantify processing |
| Failure frame | Understand limitations |

---

# 61. Practical Improvement — Detection + Tracking

A richer engineering extension is:

```text
YOLO
 ↓
object boxes
 ↓
select features inside each box
 ↓
optical flow
 ↓
object motion estimate
 ↓
trajectory
```

This demonstrates integration between C28 and C30.

It is an extension of the minimum practical, not a replacement for understanding optical flow itself.

---

# 62. Cross-Book Links

| Layer | Connection |
|---|---|
| MAIN | C30 explains video and motion concepts |
| MATH | Optical-flow constraint, vector magnitude, least squares |
| LAB | Practical 10 — optical-flow motion tracking |
| CODE | OpenCV Lucas–Kanade/Farnebäck-style workflows |
| EXAM | Video basics, optical flow, equation, sparse/dense |
| PRACTICE | Flow calculations, interpretation, debugging |
| RESOURCE | Course computer-vision references |
| ASSETS | Frame sequence, optical-flow vectors, trajectories |
| MASTER | Integrates C28 detection with temporal analysis |

---

# 63. Final Chapter Summary

Video adds a time axis:

\[
\boxed{
I(x,y,t)
}
\]

Motion analysis compares how image information changes across \(t\).

The foundational equation is:

\[
\boxed{
I_xu+I_yv+I_t=0
}
\]

but one equation cannot uniquely determine two motion components, leading to the aperture problem and the need for additional assumptions.

The practical pipeline is:

```text
video
→ frames
→ feature points / dense pixels
→ optical flow
→ motion vectors
→ trajectories / interpretation
```

The major distinction to retain is:

\[
\boxed{
\text{Detection finds objects}
}
\]

\[
\boxed{
\text{Tracking links objects/points across time}
}
\]

The university syllabus explicitly requires video processing and motion analysis, while Practical 10 specifically requires optical-flow motion tracking. fileciteturn4file0L48-L52 fileciteturn4file0L82-L86

This completes the main technical content leading into the final applications chapter.

---

**Next chapter:** C31 — DIP Applications, Engineering Context and Responsible Use
