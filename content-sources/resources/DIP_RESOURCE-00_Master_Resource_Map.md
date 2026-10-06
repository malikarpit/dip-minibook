---
id: "RESOURCE-00"
title: "Digital Image Processing — Master Resource Map"
layer: "RESOURCE"
system: "Engineering Minibooks · Digital Image Processing"
version: "1.0"
status: "FOUNDATION LOCK"
---

# RESOURCE-00 — Master Resource Map

> **Role:** Maintain one canonical map of authoritative course references, deeper texts, research sources, implementation documentation, datasets and visual provenance.

---

# 1. Resource Purpose

Resources serve one of three main goals:

```text
VERIFY
→ confirm correctness/provenance

DEEPEN
→ study beyond the Main Book

IMPLEMENT
→ obtain current tool/framework guidance
```

---

# 2. Course Reference Baseline

The supplied university syllabus lists:

1. Rafael C. Gonzalez and Richard E. Woods — *Digital Image Processing*
2. Richard Szeliski — *Computer Vision: Algorithms and Applications*
3. Adrian Rosebrock — *Deep Learning for Computer Vision with Python*
4. Jan Erik Solem — *Programming Computer Vision with Python*

These form the initial course-facing reference baseline.

---

# 3. Resource Categories

```text
COURSE
TEXTBOOK
RESEARCH
OFFICIAL
TUTORIAL
DATASET
TOOL
VISUAL-SOURCE
VIDEO
EXTENSION
```

---

# 4. Resource Record

Recommended structure:

```yaml
id: "RS-K08.03-01"
title: "..."
type: "TEXTBOOK"
creator: "..."
publisher: "..."
edition: "..."
year: "..."
url: "..."
role: "CONCEPTUAL REFERENCE"
authority: "HIGH"
topics:
  - "K08.03"
notes: "..."
```

Do not invent bibliographic fields when they have not been verified.

---

# 5. Topic Mapping

Resources are mapped to **concepts**, not merely units.

Example:

```text
K12.01 Fourier Transform
│
├── Main → C12
├── Math → M18/M19
├── Lab → LAB-U2-02
├── Exam → EXAM-U2
└── Resource → RS-K12.01-...
```

---

# 6. Resource Selection Rule

Prefer:

```text
1 core authoritative source
+
1 strong implementation/deepening source
+
additional sources only when they add something distinct
```

Do not give the learner long lists of equivalent links.

---

# 7. Textbook Roles

Use textbooks according to their strengths rather than citing all of them everywhere.

```text
Gonzalez & Woods
→ classical DIP foundations

Szeliski
→ broader computer vision context

Rosebrock
→ practical computer-vision/deep-learning context

Solem
→ Python-oriented computer vision programming
```

Specific edition/section claims should be verified before inclusion.

---

# 8. Research Source Policy

Methods with strong research provenance should use appropriate primary literature where useful.

Examples:

- SIFT
- HOG
- ResNet
- YOLO family
- autoencoders
- optical flow methods

Distinguish original research from later implementations and variants.

---

# 9. Tool Documentation

Use current official documentation for:

- MATLAB functions/toolboxes,
- Python libraries,
- OpenCV,
- deep-learning frameworks,
- model implementations.

Software behaviour must not be frozen in the conceptual Main Book when it can change.

---

# 10. Visual Provenance

Every external visual requires a record containing, where applicable:

```text
asset ID
source
creator
license/usage status
URL
access context
modified?
chapter placement
```

An image being publicly viewable does not by itself establish permission to reuse it.

---

# 11. Dataset Records

For each dataset:

```text
name
source
task
license/terms
format
relevant dimensions
limitations
bias/coverage notes where material
```

---

# 12. Source Conflict Handling

When sources disagree:

```text
identify exact claim
→ classify disagreement
→ compare authority
→ distinguish convention/version/context
→ choose or document the appropriate treatment
→ record material decisions in MASTER-05
```

---

# 13. Resource Links in Learner Experience

Prefer action labels:

```text
Core reference
Read deeper
Official documentation
Research source
Dataset
Visual provenance
```

Avoid generic “See also” lists.

---

# 14. Resource QA

- [ ] Title/author correct.
- [ ] Edition/version correct where relevant.
- [ ] Source is mapped to a concept.
- [ ] Purpose is clear.
- [ ] Important external visuals have provenance.
- [ ] Software links point to appropriate/current documentation when needed.
- [ ] Duplicate resources consolidated.
- [ ] Unsupported performance claims are not built on weak sources.

---

# 15. Definition of Done

The resource layer can support any major concept with:

```text
course reference
→ deeper reference
→ implementation source
→ provenance
```

without creating unnecessary link overload.
