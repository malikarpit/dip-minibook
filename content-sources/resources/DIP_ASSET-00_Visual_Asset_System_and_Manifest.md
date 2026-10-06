---
id: "ASSET-00"
title: "Digital Image Processing — Visual Asset System & Manifest Architecture"
layer: "ASSET"
version: "1.0"
status: "FOUNDATION LOCK"
---

# ASSET-00 — Visual Asset System & Manifest Architecture

> **Role:** Define how diagrams, example images, matrices, histograms, spectra, pipelines and other visual evidence are stored, named, sourced and connected to concepts.

---

# 1. Asset Philosophy

Assets are not decoration.

They are evidence used to teach:

```text
spatial structure
numerical transformation
algorithmic process
comparison
cause/effect
```

---

# 2. Asset Categories

```text
DIAGRAM
IMAGE-EXAMPLE
MATRIX
HISTOGRAM
SPECTRUM
PIPELINE
ALGORITHM
COMPARISON-FIGURE
ARCHITECTURE
ANNOTATION
```

---

# 3. Naming

Recommended:

```text
D-K08.03-01-convolution-walkthrough.svg
IMG-K07.02-01-histogram-example.png
MAT-K08.03-01-local-neighbourhood.svg
HIST-K07.02-01-original.png
SPEC-K12.01-01-fourier-magnitude.png
PIPE-K24.01-01-jpeg.svg
```

---

# 4. Asset Metadata

```yaml
asset_id: "D-K08.03-01"
type: "DIAGRAM"
concept_id: "K08.03"
title: "Convolution walkthrough"
status: "VERIFIED"
source: "ORIGINAL"
license: "N/A"
created_for: "DIP MiniBook"
used_in:
  - "C08"
```

---

# 5. Original vs External

Every asset should be classified:

```text
ORIGINAL
DERIVED
EXTERNAL-LICENSED
EXTERNAL-OFFICIAL
SCREENSHOT
GENERATED
```

---

# 6. Image Example Manifest

For educational image examples, record:

```text
asset ID
source
license/terms where relevant
dimensions
channels
datatype
intensity range
processing performed
concept
```

---

# 7. Figure Sequence Standard

Where an operation is the teaching target:

```text
ORIGINAL
→ OPERATION
→ RESULT
→ INTERPRETATION
```

Where a pipeline is the target:

```text
INPUT
→ STEP 1
→ STEP 2
→ STEP 3
→ OUTPUT
```

---

# 8. Asset QA

- [ ] technically correct,
- [ ] labels correct,
- [ ] dimensions/ranges correct where shown,
- [ ] text legible,
- [ ] caption present,
- [ ] source/provenance recorded,
- [ ] concept ID attached,
- [ ] no accidental misleading visual convention,
- [ ] print-size legibility checked.

---

# 9. Asset Reuse

A single verified asset may support:

```text
Main Book
Exam
Practice
Lab
Website
PDF
```

Do not duplicate visually identical assets under different names.

---

# 10. Asset Status

```text
PLANNED
DRAFT
REVIEW
VERIFIED
DEPRECATED
```

---

# 11. Definition of Done

The Asset system is ready when every required visual can be:

```text
identified
→ sourced
→ reviewed
→ linked to a concept
→ reused across outputs
```
