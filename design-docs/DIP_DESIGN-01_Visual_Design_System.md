---
title: "DESIGN-01 — Digital Image Processing Visual Design System"
system: "Engineering Minibooks"
subject: "Digital Image Processing"
version: "1.0"
status: "DESIGN FOUNDATION"
---

# DESIGN-01 — Digital Image Processing Visual Design System

> **Design direction:** Digital Image Processing should look like a visual engineering textbook: quiet editorial structure for prose, highly legible mathematics, and carefully constructed visual evidence for images, matrices, filters, spectra, pipelines and algorithms.

This document defines the DIP-specific visual layer. The Universal Engineering Minibooks Design System remains the higher-level authority for typography, spacing, responsive behaviour, themes, accessibility and general component logic.

---

# 1. Visual Identity

The DIP title should feel:

```text
precise
visual
analytical
calm
technical
layered
evidence-driven
```

It should not feel:

```text
cyberpunk
neon
camera-app-like
dashboard-heavy
AI-marketing
decorative
photo-gallery-like
```

The visual distinction of DIP comes primarily from **image evidence, grids, diagrams and signal-like structure**, not from excessive decoration.

---

# 2. Visual Hierarchy

The hierarchy should communicate learning order before visual ornament.

```text
PART
 ↓
CHAPTER
 ↓
SECTION
 ↓
CONCEPT
 ↓
EXPLANATION
 ↓
EVIDENCE
 ↓
INTERPRETATION
```

Technical evidence receives its own visual weight:

```text
IMAGE
MATRIX
FORMULA
PIPELINE
TABLE
CODE
RESULT
```

---

# 3. Three Visual Layers

## Layer A — Editorial

Used for:

- prose
- definitions
- explanations
- transitions
- recaps

Treatment:

- spacious
- restrained
- high legibility
- minimal decoration

## Layer B — Analytical

Used for:

- matrices
- equations
- histograms
- spectra
- algorithms
- tables
- plots

Treatment:

- exact
- structured
- alignment-sensitive
- visually quieter than the main concept

## Layer C — Visual Evidence

Used for:

- actual images
- before/after transformations
- colour-space views
- segmentation masks
- edge maps
- feature visualizations
- JPEG stages
- CNN feature maps

Treatment:

- prominent
- captioned
- annotated where necessary
- always interpreted by surrounding prose

---

# 4. Image-First Composition

DIP is a visual subject, but images should never be inserted merely because the topic is visual.

Use a figure when it improves one of these:

```text
spatial understanding
process understanding
comparison
cause/effect understanding
mathematical interpretation
algorithm interpretation
```

### Preferred composition

```text
[ ORIGINAL ]
      ↓
[ OPERATION ]
      ↓
[ RESULT ]
      ↓
[ WHAT CHANGED? ]
```

Alternative:

```text
┌───────────────┬───────────────┐
│ Original      │ Transformed   │
│ image         │ image         │
└───────────────┴───────────────┘
          ↓
     Interpretation
```

---

# 5. Before / After Standard

For image-processing transformations, avoid unexplained side-by-side screenshots.

Every before/after figure should identify:

- operation
- important parameter(s)
- what changed
- what did not change
- whether the effect is intended
- any visible artifact

Example caption pattern:

> **Figure — Gaussian smoothing.** The filter suppresses high-frequency intensity variation and reduces small-scale noise, while also softening sharp transitions. The observed result depends on kernel size and standard deviation.

---

# 6. Matrix Visual Standard

Matrices are treated as **data displays**, not decoration.

Use:

```text
input image matrix
→ kernel / structuring element
→ operation
→ output matrix
```

For local operations, visually emphasize:

- active neighbourhood
- kernel
- multiplication terms
- summation
- resulting centre pixel

Example:

```text
Input neighbourhood      Kernel

┌───────────────┐         ┌───────┐
│ 10  10  10    │         │1 1 1  │
│ 10  50  10    │  ×      │1 1 1  │
│ 10  10  10    │         │1 1 1  │
└───────────────┘         └───────┘

                  ↓

             Output pixel
```

The actual visual implementation may use a richer diagram, but the semantic sequence must remain obvious.

---

# 7. Kernel Presentation

Every important filter kernel should be accompanied by three pieces of information:

```text
KERNEL
WHAT IT RESPONDS TO
WHAT IT DOES TO THE IMAGE
```

For example:

```text
Sobel Gx

[-1  0  1
 -2  0  2
 -1  0  1]

Responds primarily to:
horizontal intensity change

Produces:
vertical-edge emphasis
```

Avoid treating kernels as arbitrary tables to memorize.

---

# 8. Histogram Visual Standard

A histogram is an image-analysis object.

Whenever a histogram is shown, label appropriately:

- x-axis = intensity
- y-axis = frequency/count or probability
- intensity range
- relevant transformation

Preferred conceptual sequence:

```text
Image
  ↓
Pixel values
  ↓
Frequency count
  ↓
Histogram
  ↓
Transformation
  ↓
New histogram
```

For histogram equalization, show:

```text
Original image
→ original histogram
→ CDF
→ mapping
→ enhanced image
→ transformed histogram
```

---

# 9. Frequency-Domain Visual Standard

Frequency-domain pages should distinguish:

```text
Spatial image
        ↓
Fourier transform
        ↓
Complex frequency representation
        ↓
Magnitude spectrum
        ↓
Filter mask
        ↓
Inverse transform
        ↓
Spatial result
```

When a spectrum is shown, explain what the centre and outer regions mean under the stated shift convention.

Never show a spectrum without identifying its interpretation.

---

# 10. Pipeline Diagrams

Pipelines are a primary DIP visual language.

Use them for:

- acquisition
- preprocessing
- enhancement
- restoration
- segmentation
- feature extraction
- compression
- JPEG
- classification
- object detection
- video analysis

Preferred structure:

```text
INPUT
  │
  ▼
STEP 1
  │
  ▼
STEP 2
  │
  ▼
STEP 3
  │
  ▼
OUTPUT
```

For branching systems:

```text
                   IMAGE
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
     ENHANCEMENT            SEGMENTATION
          │                     │
          ▼                     ▼
     RESTORATION           FEATURES
          │                     │
          └──────────┬──────────┘
                     ▼
                  DECISION
```

The diagram must reflect the actual algorithmic relationship.

---

# 11. Colour Systems

DIP colour pages should use the colour itself as evidence where possible.

For RGB:

```text
Original
├── R channel
├── G channel
└── B channel
```

For HSV:

```text
Hue
Saturation
Value
```

Each colour-space figure should state why that representation is useful.

Do not imply that HSV is universally “better” than RGB. Different representations are useful for different tasks.

---

# 12. Comparison Tables

Tables should answer a decision or clarify a distinction.

Good DIP comparison tables include:

- grayscale vs RGB vs multispectral
- spatial vs frequency domain
- mean vs Gaussian vs median
- Sobel vs Prewitt vs Laplacian vs Canny
- global vs adaptive thresholding
- erosion vs dilation
- opening vs closing
- SIFT vs SURF vs HOG
- lossless vs lossy compression
- RLE vs Huffman vs DCT/JPEG
- classification vs detection vs segmentation

Avoid tables that merely repeat prose.

---

# 13. Formula Presentation

A formula block should visually separate:

```text
FORMULA
meaning
variables
assumptions
worked example
```

Example pattern:

> **Histogram probability**

\[
p(r_k)=\frac{n_k}{MN}
\]

Where:

- \(n_k\) = number of pixels at level \(r_k\)
- \(M\times N\) = total number of pixels

Then immediately connect it to interpretation:

> The normalized histogram can be viewed as an empirical probability distribution over intensity levels.

---

# 14. Worked Numerical Example Style

A worked example should visibly progress.

```text
GIVEN
↓
REQUIRED
↓
FORMULA / RULE
↓
SUBSTITUTION
↓
CALCULATION
↓
ANSWER
↓
INTERPRETATION
```

Do not hide important intermediate values.

For a matrix problem, show intermediate matrices when feasible.

For a transform problem, show the transformation logic before the final result.

---

# 15. Algorithm Presentation

Use a three-level algorithm structure.

### Level 1 — Conceptual

```text
INPUT → PROCESS → OUTPUT
```

### Level 2 — Human-readable algorithm

Numbered steps.

### Level 3 — Implementation

MATLAB / Python / pseudocode where relevant.

This prevents code from becoming the first or only explanation.

---

# 16. Code Presentation

Code should be treated as evidence of the algorithm.

Each important code block should state:

```text
Purpose
Input assumptions
Key lines
Output
Interpretation
```

Avoid unexplained “magic” parameters.

For example, a Gaussian filter example should identify what controls:

- kernel size
- standard deviation
- border behaviour

---

# 17. Captions

Every significant figure gets a concise caption.

Recommended structure:

> **Figure X — [What is shown].** [What the reader should notice.]

For complex diagrams:

> **Figure X — [Process].** Step 1 does ..., which causes ...; Step 2 then ...

Captions should not merely restate the figure title.

---

# 18. Visual Annotation

Annotations are allowed when they improve understanding.

Use:

- arrows
- bounding boxes
- grid overlays
- labels
- callouts
- highlighted regions

Avoid:

- excessive arrows
- illegible labels
- decorative circles
- unexplained colours

An annotation must have a reason.

---

# 19. Accessibility

Never encode technical meaning only through colour.

For example, an edge map comparison should distinguish states with:

- labels
- position
- line style
- text

as well as colour when colour is used.

Images require meaningful alternative descriptions in the eventual web implementation.

---

# 20. Figure Naming

Use stable asset IDs.

Example:

```text
D-K03.01-sampling-grid.svg
D-K07.02-histogram-equalization.png
D-K08.01-convolution-walkthrough.svg
D-K12.01-fourier-pipeline.svg
D-K18.01-erosion-example.png
D-K24.01-jpeg-pipeline.svg
```

The Markdown file should refer to the stable ID rather than relying only on a human-readable filename.

---

# 21. Image Provenance

Every externally sourced image must have a provenance record.

Store:

```text
asset ID
source
creator/publisher
source URL if applicable
license/usage status
date accessed where relevant
modification status
```

Original teaching diagrams should be created for the system where practical.

Do not copy third-party diagrams merely because they look good.

---

# 22. Image Selection Rules

Prefer images that:

1. expose a concept clearly,
2. survive downscaling,
3. work in print,
4. have sufficient contrast,
5. have enough context to interpret,
6. can be linked to the explanation.

Avoid:

- unrelated stock photography,
- screenshots of software when a diagram would teach better,
- low-resolution examples,
- cluttered textbook scans,
- decorative photographs with no conceptual role.

---

# 23. Chapter Opener Pattern

Each Main Book chapter should open with:

```text
PART / UNIT
CHAPTER NUMBER
CHAPTER TITLE
ONE-SENTENCE IDEA
SHORT ORIENTATION PARAGRAPH
LEARNING MAP
```

Example:

> **THE CORE IDEA**  
> An image becomes computationally useful only after a physical scene has been converted into structured numerical data.

Then:

```text
YOU WILL LEARN
• ...
• ...
• ...
```

and:

```text
PREREQUISITES
→ ...
LAB CONNECTION
→ ...
```

---

# 24. Reusable DIP Visual Components

The design system should support:

```text
Definition Card
Core Idea Panel
Deep Dive Panel
Worked Example
Formula Card
Matrix Walkthrough
Before/After Figure
Pipeline Diagram
Algorithm Block
Comparison Table
Lab Connection
Code Connection
Exam Connection
Common Trap
Engineering Insight
Visual Check
Quick Recall
Chapter Recap
```

These components should share the universal system geometry.

---

# 25. Density Rules

Not every page/section should have equal density.

Use three broad levels:

### Calm

For:

- introductions
- conceptual explanation
- chapter transitions

### Analytical

For:

- equations
- matrices
- algorithms
- comparison tables

### Dense reference

For:

- formula sheets
- command references
- exam revision tables
- implementation quick references

Density should be intentional.

---

# 26. Print / Screen Parity

The same content system must support:

```text
desktop web
tablet/iPad
mobile
PDF / print
```

Essential meaning must not depend on hover, animation or interaction.

Figures should still make sense when printed.

Code may scroll on screen, but the print version must use a deliberate wrapping/page strategy.

---

# 27. DIP-Specific Visual Motifs

The subject may use restrained recurring motifs inspired by:

```text
pixel grids
sampling lattices
frequency contours
signal traces
matrix alignment
coordinate axes
subtle image crops
```

These should remain subtle.

Do not turn every page into a “technical graphic.”

---

# 28. Visual QA Checklist

Before a chapter ships:

## Image

- [ ] Image is relevant.
- [ ] Image is legible.
- [ ] Transformation is correctly represented.
- [ ] Labels match the prose.
- [ ] Before/after order is obvious.
- [ ] Caption explains what matters.
- [ ] Provenance recorded where required.

## Matrix

- [ ] Dimensions are correct.
- [ ] Values are correct.
- [ ] Kernel orientation is stated where relevant.
- [ ] Boundary assumption is stated.
- [ ] Arithmetic has been checked.

## Formula

- [ ] Symbols defined.
- [ ] Assumptions stated.
- [ ] Formula is dimensionally/technically appropriate.
- [ ] Worked example checked.

## Diagram

- [ ] Arrows represent the real process.
- [ ] No step is implied incorrectly.
- [ ] Labels are readable.
- [ ] Diagram has a clear teaching purpose.

---

# 29. Design Decision Summary

```text
DIP is visual, but not decorative.

Images show evidence.
Matrices show computation.
Formulas show structure.
Pipelines show process.
Tables show distinctions.
Code shows implementation.
Captions show interpretation.

The design should make these relationships immediately readable.
```

---

# 30. Relationship to the Universal Design System

This document does not redefine:

- core typography families
- global spacing tokens
- general responsive breakpoints
- accessibility policy
- theme system
- print architecture
- global navigation model

Those remain governed by the Universal Engineering Minibooks Design System.

This document adds only the **DIP-specific visual vocabulary**.
