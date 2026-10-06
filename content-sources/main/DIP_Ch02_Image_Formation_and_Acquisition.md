---
title: "Chapter 02 — Image Formation and Acquisition"
series: "Engineering Minibooks"
book: "Digital Image Processing"
chapter: 2
part: "Part I — The Image"
status: "Prototype / reference-quality"
content_tags: [CORE, EXAM, DEEP_DIVE, EXTENSION]
source_scope: "University of Delhi Digital Image Processing (DSE–3) syllabus"
---

# Chapter 02 — Image Formation and Acquisition

> **Chapter thesis**
> A pixel is the end product of a measurement process: scene information is shaped by illumination, optics, sensor response, and digitisation before it becomes a numerical value.

**Part I — The Image**  
**Syllabus anchor:** Unit I — image formation; sampling and quantization.

---

## 02.0 Why this chapter exists

Chapter 01 treated a digital image as structured numerical data. The next step is to understand where those numbers came from.

A camera does not simply “take a picture.” An imaging system performs a chain of physical and computational operations:

```text
Scene
  ↓
Illumination / emitted radiation
  ↓
Interaction with the scene
  ↓
Optical system
  ↓
Sensor response
  ↓
Signal formation
  ↓
Sampling
  ↓
Quantization
  ↓
Digital image
```

The exact physics changes with the imaging modality, but this chain provides the foundational mental model required for DIP.

The University of Delhi syllabus names **image formation**, **sampling**, and **quantization** explicitly within Unit I. fileciteturn4file0L32-L35

---

# 02.1 What does “image formation” mean?

**Image formation** is the process by which information about a scene is transformed into a spatially varying signal that an imaging device can measure.

For a conventional visible-light camera, the chain involves light arriving from the environment, interaction with objects, optics that collect and focus the light, and a sensor that converts the received energy into an electrical response.

A useful high-level model is:

```text
         REAL SCENE
             │
             ▼
      Light / radiation
             │
             ▼
     Scene interaction
             │
             ▼
        OPTICS
   focus + magnification
             │
             ▼
          SENSOR
             │
             ▼
      Analog response
             │
             ▼
     Sampling + ADC
             │
             ▼
      Digital image
```

### Important distinction

A digital image is therefore **not a direct copy of the scene**.

It is a measurement influenced by:

- illumination;
- surface properties;
- geometry;
- optical focus and blur;
- sensor response;
- exposure;
- noise;
- sampling;
- quantization;
- subsequent processing.

This is why the same object can produce very different digital images under different conditions.

---

# 02.2 A simple model of what a camera observes

A useful idealised model separates illumination and reflectance:

\[
f(x,y)=i(x,y)r(x,y)
\]

where:

- \(i(x,y)\) represents illumination over the scene;
- \(r(x,y)\) represents the scene's reflectance or local response;
- \(f(x,y)\) is the resulting image intensity model.

This is an **approximate modelling tool**, not a universal physical law for every imaging modality.

### Why is this model useful?

Suppose the object has the same reflectance but illumination changes dramatically.

Then the measured intensity can change even though the object itself has not changed.

That explains everyday observations such as:

- a white wall appearing dark at night;
- a face looking different in direct sunlight and indoor lighting;
- shadows changing measured intensity;
- uneven illumination making one side of a document darker.

### Mental model

```text
Measured appearance
      ≈
illumination × scene response
```

This becomes useful later when studying illumination correction, enhancement, and segmentation.

---

# 02.3 From a 3-D scene to a 2-D image

The physical world is three-dimensional, but most ordinary camera images are two-dimensional projections.

A simplified pinhole-camera relationship is:

\[
x=f\frac{X}{Z},
\qquad
y=f\frac{Y}{Z}
\]

where:

- \((X,Y,Z)\) is a 3-D point in the camera coordinate system;
- \((x,y)\) is its projected image-plane location;
- \(f\) is focal length.

**EXTENSION:** Real cameras are more complicated. Lens distortion, principal point, sensor geometry, and camera calibration parameters affect the final mapping.

### Why projection matters in DIP

It explains why an image loses or transforms some of the geometric information present in the original scene.

Two objects that are far apart in 3-D can overlap in the 2-D image.

That matters later for:

- segmentation;
- object detection;
- depth estimation;
- geometric correction;
- tracking.

### Visual intuition

```text
3-D scene                   image plane
   ● P                         • p
    \                          |
     \                         |
      \                        |
       \                       |
        \                      |
         \                     |
          ● camera ------------┘
```

The image is a projection, not a complete 3-D copy.

---

# 02.4 The role of illumination

Illumination determines how much energy is available to the imaging system.

### Uniform illumination

A simple object under relatively uniform illumination is easier to analyse because intensity variation is more strongly related to the object's own properties.

### Non-uniform illumination

Consider a document where the left side is brightly lit and the right side is in shadow.

A single global threshold may fail even though the document itself is perfectly legible.

This is one motivation for later techniques such as:

- contrast correction;
- adaptive thresholding;
- background estimation;
- illumination normalisation.

### Example

Suppose a page contains black text on a white background.

Under ideal lighting:

```text
background ≈ bright
text       ≈ dark
```

Under strong illumination variation:

```text
left background  ≈ very bright
right background ≈ moderately bright
text              ≈ dark, but not equally dark everywhere
```

A threshold chosen from one part of the image may no longer separate the classes globally.

**FORWARD LINK:** This exact problem reappears in Unit III when global and adaptive thresholding are studied.

---

# 02.5 Optics: how an imaging system focuses information

The optical system determines how scene information is mapped onto the sensor.

Ideally, a point in the scene would map to one point in the image.

Real systems are not perfect.

A point object generally produces a small spatial distribution of energy rather than an infinitely small point. This motivates the **point spread function (PSF)**.

### Point spread function

The PSF describes how the imaging system responds spatially to a point-like input.

Conceptually:

```text
Ideal point         Real optical response
    •                    ╭───╮
                         │ • │
                         ╰───╯
```

A blurred point spreads over neighbouring pixels.

### Why this matters

Blur reduces high-frequency spatial detail.

Later, when we study restoration, a degradation model can describe the observed image as approximately:

\[
g(x,y)=h(x,y)*f(x,y)+\eta(x,y)
\]

where:

- \(f(x,y)\) = ideal/original image;
- \(h(x,y)\) = degradation function, often related to system blur;
- \(*\) = convolution;
- \(\eta(x,y)\) = noise;
- \(g(x,y)\) = observed degraded image.

**This equation is introduced here only as a bridge.** The full restoration model belongs to Chapter 14.

---

# 02.6 Sensor response

A sensor converts incident energy into a measurable response.

The exact mechanism depends on the modality, but for a simple conceptual model:

```text
More received energy
        ↓
larger sensor response
        ↓
larger recorded intensity
```

within the usable operating range.

The response does not usually remain physically useful forever. Sensors have limits.

---

# 02.7 Exposure, saturation, and clipping

Suppose a simplified sensor pipeline produces an internal response that is later mapped into an 8-bit range.

For illustration, imagine the output is clipped to:

\[
0\le g\le255
\]

and a simplified gain stage produces:

\[
g'=200s
\]

where \(s\) is a normalised scene-response quantity.

For:

\[
s=0.2
\]

we obtain:

\[
g'=200(0.2)=40
\]

For:

\[
s=0.8
\]

we obtain:

\[
g'=200(0.8)=160
\]

For:

\[
s=1.5
\]

we obtain:

\[
g'=200(1.5)=300
\]

but the 8-bit output cannot represent 300, so clipping yields:

\[
g=255
\]

### Table

| Normalised response \(s\) | Internal value \(200s\) | Stored 8-bit result |
|---:|---:|---:|
| 0.0 | 0 | 0 |
| 0.2 | 40 | 40 |
| 0.8 | 160 | 160 |
| 1.0 | 200 | 200 |
| 1.5 | 300 | 255 after clipping |

### Why clipping matters

Once a value is clipped to the maximum, different scene values can collapse to the same stored value.

For example:

\[
260,\;280,\;300\rightarrow255
\]

Information about the differences among those values is lost at that stage.

The same idea applies at the dark end if a pipeline clips values to zero.

> **ENGINEERING INSIGHT:** Saturation is not merely “a bright pixel.” It represents a measurement region where the available representation can no longer distinguish higher inputs.

---

# 02.8 Dynamic range

**Dynamic range** describes the span between relatively low and high signal levels that an imaging system can meaningfully represent.

It is useful to distinguish:

- the theoretical code range of a representation;
- the actual usable range of the sensor/system;
- the scene's own range of illumination or radiance.

For an 8-bit channel, the code space is 0–255, but this does not guarantee that the physical system uses the full range optimally in every scene.

### Why it matters in DIP

If the useful scene information occupies only a narrow region of the available range, contrast enhancement may improve visibility.

This leads naturally to later topics:

- contrast stretching;
- histogram equalization;
- gamma correction;
- dynamic-range compression.

---

# 02.9 Noise in image acquisition

No real measurement system is perfectly clean.

A simple conceptual model is:

\[
g(x,y)=s(x,y)+n(x,y)
\]

where:

- \(s(x,y)\) is the desired signal;
- \(n(x,y)\) is unwanted variation introduced by the system or environment.

A more realistic restoration model may include blur as well:

\[
g(x,y)=h(x,y)*f(x,y)+\eta(x,y)
\]

### What can create noise or unwanted variation?

Depending on the system, possible sources include:

- sensor electronics;
- random photon arrival;
- temperature-related effects;
- readout electronics;
- transmission/storage corruption;
- environmental interference.

**EXTENSION:** Different noise mechanisms have different statistical structures. That is why noise modelling matters when choosing a restoration or denoising method.

---

# 02.10 The acquisition chain in more detail

A practical acquisition pipeline can be represented as:

```mermaid
flowchart LR
    A[Scene] --> B[Illumination / emitted radiation]
    B --> C[Scene interaction]
    C --> D[Optical / sensing system]
    D --> E[Sensor response]
    E --> F[Analog signal]
    F --> G[Sampling]
    G --> H[Quantization / ADC]
    H --> I[Digital image]
```

Each stage can introduce its own limitations.

| Stage | Main question | Possible effect |
|---|---|---|
| Scene | What physical information exists? | Texture, shape, colour, motion |
| Illumination | How much energy reaches the scene? | Shadows, uneven lighting |
| Interaction | How does the scene modify the signal? | Reflectance / transmission changes |
| Optics | How is spatial information focused? | Blur, magnification, distortion |
| Sensor | How is energy converted to a signal? | Sensitivity, noise, saturation |
| Sampling | At which spatial locations is it measured? | Spatial discretisation, aliasing risk |
| Quantization | Which intensity codes are allowed? | Intensity discretisation |
| Storage | How are values represented and encoded? | Datatype / compression effects |

Sampling and quantization are covered much more deeply in Chapter 03.

---

# 02.11 How does one pixel actually happen?

Think of one final digital pixel as the endpoint of a chain.

```text
Small region of scene
        ↓
physical signal arrives
        ↓
optical system maps energy
        ↓
sensor collects energy
        ↓
electrical response
        ↓
sampled measurement
        ↓
quantized code
        ↓
stored pixel value
```

This is why the statement

> “A pixel is the colour of one tiny point in the real world”

is useful intuition but technically incomplete.

A practical pixel value is better understood as a **sampled measurement associated with an area/region and an acquisition process**.

---

# 02.12 Area measurement versus ideal point measurement

An ideal mathematical function \(f(x,y)\) can describe intensity continuously.

A real detector element has finite extent.

Conceptually, a detector measures some integrated or averaged response over its sensitive area rather than an infinitely small geometric point.

A simplified model is:

\[
p_{mn}\propto \iint_{A_{mn}} f(x,y)\,dx\,dy
\]

where \(A_{mn}\) is the sensor area associated with sample \((m,n)\).

The exact proportionality and normalisation depend on the sensor model.

### Why this matters

It explains why:

- changing pixel size affects spatial detail;
- fine patterns can disappear or alias;
- optical blur and finite sensor area interact;
- sensor design affects the final image before software processing begins.

This is the physical intuition behind sampling theory.

---

# 02.13 Single sensor, sensor strip, and sensor array

Classical DIP texts describe several acquisition arrangements.

## Single sensor

A single sensing element measures one location at a time.

Spatial information may require mechanical movement or scanning.

## Sensor strip / line sensor

A one-dimensional array captures a line at a time.

Movement of the object or sensor builds the two-dimensional image.

Commonly useful in scanning systems and some industrial or remote-sensing applications.

## Two-dimensional sensor array

A 2-D array measures many spatial locations simultaneously.

This is the common conceptual model for ordinary digital cameras.

### Comparison

| Architecture | Samples at once | How 2-D image forms | Typical concept |
|---|---:|---|---|
| Single sensor | 1 | Scanning | Point-by-point acquisition |
| Line sensor | One line | Mechanical / object motion | Line scanning |
| 2-D array | Many pixels | Direct 2-D capture | Camera-like acquisition |

---

# 02.14 How colour is acquired

Colour requires more than a single scalar intensity measurement.

A simple conceptual model is to measure different spectral responses and represent them as channels.

For RGB imagery:

```text
Scene
  ↓
Spectral information
  ↓
three colour responses
  ├── R
  ├── G
  └── B
  ↓
three aligned channels
  ↓
RGB image
```

**EXTENSION:** Many consumer cameras use a colour filter array so neighbouring sensor elements respond differently to parts of the visible spectrum. A reconstruction/demosaicing process can then form a full RGB representation. The exact sensor architecture varies.

### Why colour-space conversion later becomes useful

RGB is convenient for acquisition and display, but not always the most convenient representation for a particular processing task.

That is why the syllabus later requires colour models such as:

- RGB;
- HSV;
- CMY;
- YUV.

Different representations expose different aspects of the image data.

---

# 02.15 Acquisition of different kinds of images

“Image formation” does not always mean a visible-light camera.

| Imaging modality | Measured phenomenon | Typical information |
|---|---|---|
| Visible camera | Reflected visible light | Colour, texture, shape |
| Infrared imaging | Infrared radiation | Thermal/material differences depending on band and system |
| X-ray imaging | X-ray attenuation | Internal structure |
| Microscopy | Optical response at microscopic scale | Cells, tissue, microstructure |
| Remote sensing | Reflected/emitted radiation from Earth | Land cover, vegetation, environmental properties |
| Radar imaging | Radio-frequency response | Structure / motion / surface properties |

The same digital-image ideas—representation, noise, sampling, filtering, segmentation, compression—can be reused, but the physical acquisition model changes.

---

# 02.16 A deeper mathematical acquisition model

A useful layered representation is:

### Stage 1 — Continuous scene signal

\[
s(x,y)
\]

### Stage 2 — Optical/sensor response

\[
a(x,y)=h(x,y)*s(x,y)+\eta(x,y)
\]

where \(h\) models spatial system response and \(\eta\) models additive disturbance in this simplified model.

### Stage 3 — Sampling

\[
a(x,y)\rightarrow a[m,n]
\]

Only discrete spatial locations are retained.

### Stage 4 — Quantization

\[
a[m,n]\rightarrow I[m,n]
\]

Continuous-valued measurements are mapped to allowed digital code levels.

### Combined conceptual chain

\[
\boxed{
s(x,y)
\xrightarrow{\text{imaging}}
a(x,y)
\xrightarrow{\text{sampling}}
a[m,n]
\xrightarrow{\text{quantization}}
I[m,n]
}
\]

This compact chain should stay in your mental model throughout Part I.

---

# 02.17 Worked example — from scene response to an 8-bit pixel

Suppose a simplified sensor chain produces a normalised signal value:

\[
s=0.62
\]

Assume a gain stage maps this to a nominal 0–255 scale:

\[
v=255s
\]

Then:

\[
v=255(0.62)=158.1
\]

If the system rounds to the nearest integer:

\[
I=158
\]

So the final stored pixel value is:

\[
\boxed{158}
\]

### What happened?

It is tempting to say “the scene had intensity 158,” but that is not what the calculation means.

The actual statement is:

> Under the assumed acquisition and scaling model, a normalised measured response of 0.62 was mapped to the digital code 158.

The distinction matters because raw sensor readings, calibrated physical quantities, and display-oriented pixel codes are not automatically the same thing.

---

# 02.18 Worked example — quantization step preview

Suppose a normalised signal lies in the interval:

\[
0\le s<1
\]

and an ideal 3-bit quantizer is used.

The number of levels is:

\[
L=2^3=8
\]

The approximate step width is:

\[
\Delta=\frac{1}{8}=0.125
\]

A signal of:

\[
s=0.62
\]

falls into one of these quantization intervals depending on the chosen quantizer convention.

The key lesson is not the particular rounding rule but the fact that **many possible continuous values are represented by a finite set of digital codes**.

Chapter 03 will build this precisely with sampling and quantization mathematics.

---

# 02.19 Where acquisition errors enter the final image

A useful debugging map is:

```text
Scene / illumination
        │
        ├── wrong exposure
        ├── shadows
        └── insufficient signal
        ↓
Optics
        │
        ├── blur
        ├── distortion
        └── defocus
        ↓
Sensor
        │
        ├── noise
        ├── saturation
        └── sensitivity limits
        ↓
Sampling
        │
        └── spatial discretisation / aliasing
        ↓
Quantization
        │
        └── intensity discretisation
        ↓
Storage / processing
        │
        ├── compression
        ├── format conversion
        └── numerical errors
        ↓
FINAL DIGITAL IMAGE
```

When an image looks “bad,” the cause may have happened **before** any enhancement algorithm was run.

That distinction is central to restoration.

---

# 02.20 Restoration versus enhancement — early distinction

The acquisition model explains an important conceptual difference.

### Enhancement

Goal:

> Produce an image that is more useful or visually informative for a chosen task.

There may be many acceptable outcomes.

### Restoration

Goal:

> Estimate the original or intended image using an explicit or assumed degradation model.

The model might be:

\[
g=h*f+\eta
\]

This distinction is important because it explains why restoration is more model-driven than generic visual enhancement.

---

# 02.21 Acquisition metadata is part of practical image information

The pixel matrix is not always the complete story.

Depending on the image source, metadata may include:

- acquisition time;
- device information;
- orientation;
- exposure-related settings;
- spatial reference;
- spectral band information;
- calibration parameters.

Not all file formats contain the same metadata, and metadata may be lost or altered during conversion.

**EXTENSION:** In scientific and geospatial imaging, metadata can be essential to interpretation. A numerical array without the context of how it was measured can be misleading.

---

# 02.22 Common image-formation mistakes

### Mistake 1 — Treating the pixel value as a direct physical measurement

A stored 8-bit value is often a processed code, not a universal physical unit.

### Mistake 2 — Assuming brighter always means more “important”

Brightness depends on illumination, sensor response, processing, and representation.

### Mistake 3 — Ignoring saturation

A clipped region may have lost distinctions that no post-processing algorithm can reliably reconstruct.

### Mistake 4 — Assuming blur is only a software problem

Blur can originate in optics, motion during acquisition, defocus, resampling, and later processing.

### Mistake 5 — Treating all noise as the same

Different noise mechanisms have different spatial/statistical behaviour.

### Mistake 6 — Confusing projection with measurement of 3-D structure

A 2-D image is a projection/measurement of the scene; multiple 3-D configurations can produce similar 2-D observations.

### Mistake 7 — Forgetting the acquisition context

The same digital values can have different meanings depending on modality, calibration, colour space, and datatype.

---

# 02.23 A practical “read the image” checklist

Before processing any image, inspect:

```text
1. What is the acquisition source?
2. What are the dimensions?
3. How many channels are there?
4. What is the datatype?
5. What is the valid value range?
6. Which colour space is used?
7. Has the image been compressed?
8. Is there visible noise?
9. Is there blur or motion smear?
10. Is there saturation or clipping?
11. Is illumination uniform?
12. What task will the processing serve?
```

This checklist is more valuable than blindly applying filters.

---

# 02.24 Image formation and acquisition — system comparison

| Factor | What changes | DIP consequence |
|---|---|---|
| Illumination | Signal level across scene | Contrast, shadows, thresholding difficulty |
| Focus | Spatial sharpness | Edge/detail quality |
| Motion | Position during exposure | Motion blur |
| Optics | Spatial response | Blur/distortion |
| Sensor sensitivity | Signal response | Brightness/noise behaviour |
| Exposure | Amount of received energy | Under/overexposure |
| Sampling | Spatial sample density | Detail / aliasing |
| Quantization | Number of code levels | Intensity precision |
| Compression | Encoding of stored data | File size / possible information loss |

---

# 02.25 EXAM lens

### High-yield definitions

1. Define image formation.
2. Explain image acquisition.
3. Explain the role of a sensor in image acquisition.
4. Define dynamic range.
5. Explain saturation/clipping.
6. Explain the concept of PSF at a conceptual level.
7. Explain the image degradation model.

### High-yield formulas

\[
f(x,y)=i(x,y)r(x,y)
\]

Simple illumination–reflectance model.

\[
x=f\frac{X}{Z},\qquad y=f\frac{Y}{Z}
\]

Simple pinhole projection model — extension material.

\[
g(x,y)=h(x,y)*f(x,y)+\eta(x,y)
\]

Basic degradation model.

### Typical conceptual question

> Why can an image be degraded before any digital image-processing algorithm is applied?

Expected reasoning:

```text
scene / illumination / optics / sensor / acquisition
                    ↓
            degraded measurement
                    ↓
               digital image
```

---

# 02.26 Chapter checkpoint

### Concept 1

Explain why a pixel should be considered the result of a measurement-and-digitisation process rather than simply a “tiny square in the world.”

### Concept 2

Two photographs of the same object are taken using different lighting. The object does not move, but the pixel intensities differ substantially.

List at least three reasons why this can happen.

### Numerical

A simplified acquisition model maps a normalised sensor response \(s\) to an 8-bit value using:

\[
I=\operatorname{round}(255s)
\]

Calculate the output for:

\[
s\in\{0.10,0.50,0.90\}
\]

### System reasoning

An image contains a large bright region with many pixels at exactly 255.

What does this suggest about the acquisition process, and what information may be lost?

### Design question

Draw the complete chain from a real-world scene to a stored digital pixel. Label where blur, noise, sampling, and quantization can appear.

---

# 02.27 Lab / implementation bridge

Although the first university practical focuses on loading, displaying, and converting images between colour spaces, it is useful to connect every loaded image back to its acquisition context.

The syllabus explicitly requires image input/output and colour-space conversion in Experiment 1. fileciteturn4file0L58-L61

Before calling an API, inspect the data conceptually:

```text
shape      → spatial dimensions + channels
channel    → what component is being represented?
dtype      → how is each value stored?
range      → what values are valid?
colour     → which colour-space convention?
origin     → how was the image acquired?
```

This habit will prevent many later implementation bugs.

---

# 02.28 Forward connection — sampling and quantization

We now know that a real imaging system produces a continuous or analogue signal and that the computer eventually needs a finite digital representation.

The bridge between those two worlds is:

\[
\boxed{
\text{continuous spatial signal}
\rightarrow
\text{sampling}
\rightarrow
\text{discrete coordinates}
}
\]

and:

\[
\boxed{
\text{continuous intensity}
\rightarrow
\text{quantization}
\rightarrow
\text{finite digital levels}
}
\]

The next chapter develops both ideas rigorously, including aliasing, sampling density, bit depth, quantization error, and worked numerical examples.

---

## Chapter summary

Image formation and acquisition explain why a digital image is a **measurement produced by a system**, not a perfect copy of reality.

The chain is:

```text
scene
 → illumination / emitted radiation
 → scene interaction
 → optics
 → sensor response
 → analogue signal
 → sampling
 → quantization
 → digital image
```

Every stage can affect the final data. Illumination changes intensity, optics affect spatial detail, sensors introduce response limits and noise, sampling determines spatial discretisation, and quantization determines intensity discretisation.

The most important idea to retain is:

> **When you inspect a digital image, you are looking at the output of an acquisition pipeline. Understanding that pipeline explains many of the image's strengths, weaknesses, and failure modes.**
