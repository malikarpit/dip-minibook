---
id: "C02"
title: "Image Formation and Acquisition"
layer: "MAIN"
part: "I — The Image"
unit: "I"
version: "1.1"
status: "REFERENCE BUILD"
syllabus_scope:
  - "Image Formation"
  - "Sampling preview"
  - "Quantization preview"
tags:
  - "CORE"
  - "EXAM"
  - "DEEP DIVE"
  - "EXTENSION"
prerequisites:
  - "C01"
related:
  - "C03"
  - "C04"
  - "C14"
math:
  - "M02"
  - "M16"
lab:
  - "LAB-U1-01"
exam:
  - "EXAM-U1"
practice:
  - "P-C02"
assets:
  - "D-C02-01"
  - "D-C02-02"
  - "D-C02-03"
---

# Chapter 02 — Image Formation and Acquisition

> **Chapter thesis**  
> A digital image begins as a physical measurement. Illumination, scene properties, optics, sensor response, geometry, exposure, noise and digitisation all influence the numerical image that a computer eventually receives.

**Part I — The Image**  
**Syllabus anchor:** Unit I — image formation, followed by sampling and quantization. fileciteturn4file0L32-L35

---

# 02.0 Why Image Formation Matters

Chapter 01 treated the digital image as structured numerical data.

Now we ask:

> **Where did those numbers come from?**

If we do not understand acquisition, later observations can become misleading.

For example:

```text
dark image
```

does not automatically mean:

```text
dark object
```

The image may instead have resulted from:

- insufficient illumination,
- short exposure,
- sensor limitations,
- optical attenuation,
- scene geometry,
- nonlinear processing,
- limited dynamic range.

Likewise:

```text
blurred image
```

does not necessarily mean poor software.

The blur may have been introduced during acquisition.

---

# 02.1 The Acquisition Chain

For a conventional imaging system, a high-level chain is:

```text
        PHYSICAL SCENE
              │
              ▼
       illumination /
       emitted radiation
              │
              ▼
       scene interaction
              │
              ▼
            OPTICS
              │
       focus / projection
              │
              ▼
           SENSOR
              │
       physical response
              │
              ▼
        signal readout
              │
              ▼
      digitisation system
       sampling + quantization
              │
              ▼
         DIGITAL IMAGE
```

Different imaging modalities change the physical details, but the conceptual idea remains:

> **the image is the result of a measurement pipeline.**

---

# 02.2 What Is Image Formation?

**Image formation** is the process by which information from a physical scene is transformed, through an imaging system, into a spatially varying measurable signal.

For ordinary visible-light imaging, the broad sequence is:

```text
light
→ interacts with scene
→ enters imaging system
→ optics form an image
→ sensor measures received energy
→ electronics produce a signal
```

The word *formation* therefore includes more than “taking a photo.”

It includes the factors that determine how scene structure becomes image structure.

---

# 02.3 Illumination

A scene can only be measured according to the radiation available to the imaging system.

For a simple reflective scene, a useful model is:

\[
f(x,y)=i(x,y)\,r(x,y)
\]

where:

- \(i(x,y)\) = illumination component,
- \(r(x,y)\) = reflectance or local scene-response component,
- \(f(x,y)\) = resulting image intensity model.

## What does this model teach?

Suppose an object's reflectance remains approximately constant but illumination changes.

Then:

\[
r(x,y)\approx \text{constant}
\]

while:

\[
i(x,y)
\]

changes.

Therefore \(f(x,y)\) changes too.

This explains why the same physical object can look different:

- in bright sunlight,
- indoors,
- under coloured lighting,
- in shadow,
- under uneven illumination.

> **WARNING:** This multiplicative model is a useful high-level model for reflective imaging. It is not a universal physical equation for every imaging modality.

---

# 02.4 Worked Example — Illumination vs Reflectance

Suppose, at one location:

\[
r(x,y)=0.5
\]

and illumination is:

\[
i_1(x,y)=100
\]

Then:

\[
f_1(x,y)=100(0.5)=50
\]

If illumination changes to:

\[
i_2(x,y)=180
\]

while reflectance remains:

\[
r(x,y)=0.5
\]

then:

\[
f_2(x,y)=180(0.5)=90
\]

### Interpretation

The object did not change its reflectance in this idealized example.

The measured intensity changed because illumination changed.

This is one reason illumination variation is important in:

- segmentation,
- thresholding,
- recognition,
- restoration.

---

# 02.5 Optics and Projection

An imaging system must map scene structure onto the sensor plane.

At a high level, optics determine:

```text
what part of the scene is captured
how it is projected
how sharply it is focused
how much light reaches the sensor
```

Important optical effects include:

- focus,
- magnification,
- perspective,
- defocus blur,
- aberration,
- field of view.

The MiniBook does not require a full optical-engineering treatment, but understanding these effects explains why acquisition itself can introduce degradation.

---

# 02.6 Simplified Pinhole Projection

> **DEEP DIVE / EXTENSION**

A simplified pinhole-camera relation is:

\[
x = f\frac{X}{Z},
\qquad
y = f\frac{Y}{Z}
\]

where:

- \((X,Y,Z)\) = 3-D point coordinates in a simplified camera coordinate system,
- \((x,y)\) = projected image-plane coordinates,
- \(f\) = focal length.

The model expresses an important idea:

> objects farther away generally project to smaller image dimensions than equally sized objects nearby.

## Worked Example

Suppose:

\[
X=20\text{ mm}
\]

\[
Z=1000\text{ mm}
\]

\[
f=10\text{ mm}
\]

Then:

\[
x=10\cdot\frac{20}{1000}
\]

\[
x=0.2\text{ mm}
\]

The exact image coordinate convention depends on the chosen camera model and origin, but the proportional relationship is the key idea.

### Why do we care in DIP?

Because geometry affects:

- object size,
- perspective,
- registration,
- image warping,
- camera calibration,
- later computer-vision tasks.

---

# 02.7 Sensor: Where Measurement Becomes Data

A sensor converts incident radiation into a measurable response.

For a simplified digital imaging system:

```text
incident radiation
        ↓
sensor element
        ↓
electrical response
        ↓
readout
        ↓
numeric representation
```

The sensor response is not perfectly ideal.

It can be influenced by:

- sensitivity,
- exposure time,
- noise,
- saturation,
- dark response,
- temperature,
- manufacturing variation.

These effects help explain why acquisition quality matters before any software processing occurs.

---

# 02.8 Sensor Elements and Spatial Structure

An area sensor contains many sensing elements arranged spatially.

Conceptually:

```text
┌───┬───┬───┬───┐
│ S │ S │ S │ S │
├───┼───┼───┼───┤
│ S │ S │ S │ S │
├───┼───┼───┼───┤
│ S │ S │ S │ S │
├───┼───┼───┼───┤
│ S │ S │ S │ S │
└───┴───┴───┴───┘
```

Each sensing location contributes information to the eventual image representation.

This spatial arrangement is the bridge to **sampling**, which becomes the main subject of Chapter 03.

---

# 02.9 Pixel vs Sensor Element

These are related but should not be casually treated as identical physical objects.

A **sensor element** belongs to the physical measurement process.

A **pixel** belongs to the digital image representation.

Depending on the architecture, optical design, colour arrangement and signal-processing pipeline, the relationship between physical sensing elements and final image pixels may be more complicated than:

```text
one sensor element = one final RGB pixel
```

> **Engineering Insight:** Keeping acquisition terminology separate from digital-representation terminology prevents many conceptual mistakes later.

---

# 02.10 Exposure

Exposure determines how much radiation contributes to the sensor response over the capture interval.

Too little exposure may lead to:

```text
underexposed image
→ low recorded values
→ weak detail in dark regions
```

Too much exposure may lead to:

```text
saturation
→ clipped high values
→ lost information in bright regions
```

This gives us an important distinction:

> **A recorded extreme value does not always mean the scene itself contained no additional information. The sensor may simply have reached its representational limit.**

---

# 02.11 Saturation and Clipping

Suppose the representable range is:

\[
0\leq I\leq255
\]

A measured response above the maximum cannot be represented directly in 8-bit unsigned form.

A simplified clipping process might be:

\[
I_{\text{stored}}=
\begin{cases}
0,&I<0\\
I,&0\le I\le255\\
255,&I>255
\end{cases}
\]

This means multiple different physical responses can collapse into the same stored value:

```text
300 → 255
320 → 255
400 → 255
```

After clipping, we cannot uniquely reconstruct whether the original values were 300, 320 or 400 from the clipped pixel alone.

This is an example of information loss during representation.

---

# 02.12 Dynamic Range

A sensor and digitisation pipeline can represent only a finite range of responses.

A high dynamic range generally allows more separation between very weak and very strong responses before saturation or loss of precision becomes important.

For DIP, dynamic range matters because:

- contrast operations depend on available range,
- restoration depends on recorded information,
- enhancement cannot recover detail that was never recorded,
- quantization precision affects low-level differences.

---

# 02.13 Noise During Acquisition

Noise is unwanted variation introduced into or carried by the measurement.

A conceptual model is:

\[
g(x,y)=f(x,y)+\eta(x,y)
\]

where:

- \(f(x,y)\) = ideal image,
- \(\eta(x,y)\) = additive noise,
- \(g(x,y)\) = observed image.

This is a simplified model used to develop intuition.

Later chapters will distinguish several noise models and restoration assumptions.

---

# 02.14 Why Noise Does Not Always Look the Same

Different acquisition mechanisms can produce different statistical structures.

Examples include:

| Noise/context | Qualitative appearance | Later implication |
|---|---|---|
| Sensor/electronic fluctuations | small random intensity variation | smoothing may help |
| Impulse-like corruption | isolated extreme values | median-like approaches can be useful |
| Multiplicative effects | variation related to local signal | model choice becomes important |
| Photon/statistical effects | signal-dependent variation | statistical treatment may be needed |

This is why “remove noise” is not one universal operation.

---

# 02.15 Blur During Acquisition

An acquired image can be blurred before any software filter is applied.

A simplified model is:

\[
g(x,y)=h(x,y)*f(x,y)
\]

where:

- \(f\) = ideal scene image,
- \(h\) = point-spread/degradation function,
- \(*\) = convolution,
- \(g\) = observed image.

With noise added:

\[
g(x,y)=h(x,y)*f(x,y)+\eta(x,y)
\]

This is the conceptual degradation model that later becomes central to image restoration.

> **Key connection:** Restoration is easier to understand when you realize that some “image-processing problems” are actually attempts to undo limitations introduced during acquisition.

---

# 02.16 Worked Degradation Example

Suppose the original 1-D signal is:

\[
f=[0,0,100,0,0]
\]

and a simple averaging blur is approximated by:

\[
h=\frac{1}{3}[1,1,1]
\]

The central peak becomes distributed into neighbouring positions.

Conceptually:

```text
Original
      █
      █
      █

After blur
    ▄ █ ▄
```

The exact boundary treatment changes the numerical output, so the MiniBook will state the border convention whenever a full calculation is performed.

The key point is:

> **Blur spreads localized information across neighbouring spatial locations.**

---

# 02.17 Image Formation vs Sampling vs Quantization

These three concepts must remain distinct.

| Stage | Main question |
|---|---|
| Image formation | How does scene information become a measurable signal? |
| Sampling | At which spatial locations do we record the signal? |
| Quantization | Which numerical intensity levels can represent each measurement? |

Conceptually:

```text
physical scene
      ↓
image formation
      ↓
continuous/spatially varying signal
      ↓
sampling
      ↓
discrete spatial locations
      ↓
quantization
      ↓
finite intensity levels
      ↓
digital image
```

Chapter 03 will study the last part in depth.

---

# 02.18 Worked Conceptual Chain

Imagine a document under uneven lighting.

### Physical stage

The paper reflects available illumination.

### Optical stage

The imaging system projects the page onto the sensor.

### Sensor stage

The sensor measures the incoming response.

### Acquisition issues

One region may receive less light.

### Digitisation

The continuous spatial/response information is sampled and quantized.

### Final digital image

The resulting pixel values may show:

```text
bright page region
+
darkened region
+
sensor noise
+
optical blur
```

Later algorithms can attempt:

```text
contrast enhancement
noise reduction
deblurring
thresholding
```

But software cannot guarantee perfect recovery of information that was never captured.

---

# 02.19 The Information Boundary

This is an important engineering principle.

Suppose a bright region has saturated:

```text
true response:
300, 340, 420, 500

stored:
255, 255, 255, 255
```

The stored image no longer contains enough information to distinguish the original values.

Similarly:

```text
very fine spatial pattern
```

may disappear under insufficient sampling.

Or:

```text
fine detail
```

may be suppressed by optical blur.

Therefore:

> **Image processing can transform available information, but it cannot universally reconstruct arbitrary information that the acquisition chain completely discarded.**

This principle will return in restoration, compression and super-resolution discussions.

---

# 02.20 Acquisition Quality as an Engineering Trade-Off

Real imaging systems trade among factors such as:

```text
spatial detail
signal strength
noise
exposure time
dynamic range
field of view
data volume
hardware limits
```

Improving one quantity can affect another.

For example:

```text
higher spatial sampling
→ potentially more detail
→ potentially more data

longer exposure
→ potentially more signal
→ potentially more motion blur
```

These are engineering trade-offs, not purely software decisions.

---

# 02.21 Acquisition Examples Across Modalities

The exact physical process changes by modality.

| Modality | Measured/used information | Example output |
|---|---|---|
| Visible-light camera | reflected/emitted optical radiation | RGB/grayscale image |
| Scanner | reflected/transmitted light along a controlled path | document image |
| Infrared imaging | infrared radiation | thermal/spectral representation |
| X-ray imaging | transmitted X-ray intensity | projection image |
| MRI | magnetic-resonance-derived measurements | reconstructed image |
| Ultrasound | acoustic reflections | reconstructed image |

The DIP principles remain relevant because all ultimately produce numerical data for computational processing, even though the acquisition physics differ.

> **EXTENSION:** A good DIP engineer understands where a numerical image came from because acquisition assumptions affect how later algorithms should be interpreted.

---

# 02.22 Common Acquisition Artifacts

Examples:

```text
blur
noise
saturation
underexposure
overexposure
illumination non-uniformity
geometric distortion
sensor non-uniformity
compression artifacts introduced later in the storage pipeline
```

The final artifact may have multiple causes, so diagnosis should be evidence-driven.

---

# 02.23 Acquisition Artifact → Later DIP Method

| Acquisition issue | Potential downstream response |
|---|---|
| uneven illumination | contrast correction / adaptive processing |
| impulse-like noise | nonlinear filtering |
| smooth random noise | smoothing / restoration |
| blur | deconvolution/restoration |
| geometric distortion | geometric correction |
| limited dynamic range | enhancement or acquisition redesign |
| saturation | often cannot be perfectly recovered |

The table is a decision aid, not a guarantee that one method always solves the problem.

---

# 02.24 Common Traps

## Trap 1 — “A camera records the scene exactly.”

False.

It records a measurement influenced by the entire imaging chain.

## Trap 2 — “A pixel is the physical scene point.”

Incomplete.

A digital pixel is a representation associated with a sampled image location; the physical sensing process involves finite sensor areas, optics and integration effects.

## Trap 3 — “More exposure always gives a better image.”

False.

Too much exposure can lead to clipping/saturation.

## Trap 4 — “Software can recover any lost information.”

False.

If information is fully destroyed by clipping, insufficient sampling, severe blur or other irreversible operations, exact recovery is generally not guaranteed.

## Trap 5 — “Image formation and sampling are the same.”

False.

Formation concerns how scene information produces a measurable signal; sampling concerns discrete spatial recording of that signal.

---

# 02.25 Engineering Insight — Diagnose the Acquisition Before the Algorithm

When a new image looks poor, ask:

```text
Was the illumination adequate?
Was the scene properly exposed?
Was the focus appropriate?
Is there motion?
Is the dynamic range sufficient?
Is the sensor noisy?
Is there saturation?
Was the image resampled or compressed?
```

Only then choose a processing method.

A strong DIP workflow therefore begins with **measurement diagnosis**, not automatic filtering.

---

# 02.26 Cross-Book Bridges

> **MATH BRIDGE — M02 / M16**  
> Review discrete image coordinates and geometric transformation mathematics.

> **LAB BRIDGE — LAB-U1-01**  
> Inspect actual image dimensions, datatype, channels and range after loading an image.

> **PRACTICE BRIDGE**  
> Diagnose whether a described artifact is more plausibly caused by illumination, noise, blur, sampling or saturation.

> **EXAM BRIDGE**  
> Be able to explain the image-acquisition pipeline, the illumination/reflectance model, the role of sensors and the distinction between image formation, sampling and quantization.

> **RESOURCE BRIDGE**  
> Consult the classical DIP references for more detailed acquisition and degradation models.

---

# 02.27 Quick Recall

```text
SCENE
↓
ILLUMINATION / EMISSION
↓
SCENE INTERACTION
↓
OPTICS
↓
SENSOR
↓
READOUT
↓
SAMPLING
↓
QUANTIZATION
↓
DIGITAL IMAGE
```

A useful reflective-scene model:

\[
f(x,y)=i(x,y)r(x,y)
\]

A simple additive-noise model:

\[
g(x,y)=f(x,y)+\eta(x,y)
\]

A simple degradation model:

\[
g(x,y)=h(x,y)*f(x,y)+\eta(x,y)
\]

---

# 02.28 Chapter Checkpoint

You should now be able to answer:

1. What is image formation?
2. Why is a digital image considered a measurement rather than an exact copy of a scene?
3. What roles do illumination and reflectance play?
4. What does the simplified model \(f=i\,r\) tell us?
5. What is the difference between a sensor element and a digital pixel?
6. What is saturation?
7. Why can clipped data be impossible to reconstruct exactly?
8. How can acquisition introduce blur and noise?
9. Distinguish image formation, sampling and quantization.
10. Why should image quality problems be diagnosed before choosing a processing algorithm?

---

# 02.29 Connection Forward

The acquisition system gives us a continuously varying physical signal.

But a computer needs discrete numerical data.

That creates the next fundamental question:

> **How do we turn continuous spatial information and continuously varying measurements into discrete samples and finite numeric levels?**

That is the problem of:

```text
SAMPLING + QUANTIZATION
```

and it is the focus of Chapter 03.

---

# 02.30 Final Mental Model

```text
A digital image starts long before the pixel array exists.

Scene
  ↓
physics
  ↓
optics
  ↓
sensor
  ↓
measurement
  ↓
digitisation
  ↓
pixel values

Every stage can preserve, distort, limit or discard information.

Understanding that chain is the foundation for understanding
enhancement, restoration, segmentation and vision.
```
