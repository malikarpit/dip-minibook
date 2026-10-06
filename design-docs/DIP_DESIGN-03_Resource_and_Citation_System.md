---
title: "DESIGN-03 — Digital Image Processing Resource & Citation System"
system: "Engineering Minibooks"
subject: "Digital Image Processing"
version: "1.0"
status: "RESOURCE GOVERNANCE FOUNDATION"
---

# DESIGN-03 — Digital Image Processing Resource & Citation System

> **Purpose:** Maintain trustworthy, traceable and useful sources for the DIP system without turning the learner-facing chapters into reference dumps.

---

# 1. Governing Principle

Resources serve three roles:

```text
VERIFY
→ establish correctness / provenance

LEARN DEEPER
→ provide additional treatment

IMPLEMENT
→ provide current tool/documentation guidance
```

A resource should be included because it serves one of these roles.

---

# 2. Source Hierarchy

Use this order when judging a source for technical authority.

```text
TIER 1 — Standards / official documentation / primary sources
TIER 2 — Established university textbooks / academic references
TIER 3 — Reputable university/course material
TIER 4 — High-quality technical documentation / educational sites
TIER 5 — Secondary tutorials / community explanations
TIER 6 — Forums / informal discussion
```

The lower tiers may be useful, but they should not silently override stronger sources on technical questions.

---

# 3. University-Specified References

The supplied DIP syllabus lists:

1. Rafael C. Gonzalez and Richard E. Woods, *Digital Image Processing*.
2. Richard Szeliski, *Computer Vision: Algorithms and Applications*.
3. Adrian Rosebrock, *Deep Learning for Computer Vision with Python*.
4. Jan Erik Solem, *Programming Computer Vision with Python*.

These should be represented as the **course-facing reference baseline**.

They are not automatically the best source for every software-version detail.

---

# 4. Resource Classes

Every resource should be classified.

| Class | Purpose |
|---|---|
| `COURSE` | Direct syllabus/course support |
| `TEXTBOOK` | Formal conceptual reference |
| `RESEARCH` | Primary research/technical paper |
| `OFFICIAL` | Official documentation or specification |
| `TUTORIAL` | Supporting explanation |
| `DATASET` | Image/video dataset |
| `TOOL` | Software/tool reference |
| `VISUAL-SOURCE` | Image/diagram provenance |
| `VIDEO` | Lecture/demo/resource |
| `EXTENSION` | Optional advanced study |

---

# 5. Resource Records

A canonical resource record should capture:

```yaml
id: "RS-K08.03-01"
title: "..."
type: "TEXTBOOK"
creator: "..."
publisher: "..."
year: "..."
edition: "..."
url: "..."
topic_ids:
  - "K08.03"
role: "CONCEPTUAL REFERENCE"
authority: "HIGH"
notes: "..."
```

Not every field applies to every resource.

---

# 6. Topic-to-Resource Mapping

The resource system should map resources to concepts, not merely chapters.

Example:

```text
K07.02 Histogram Equalization
│
├── MAIN → C07
├── MATH → M07...
├── LAB → LAB...
├── EXAM → EXAM...
└── RESOURCE
      ├── textbook section
      ├── university note
      └── optional tutorial
```

This allows resource retrieval at the moment of need.

---

# 7. Main Book Reference Policy

Do not turn every Main Book paragraph into a citation wall.

Use citations when:

- a non-obvious technical fact is being asserted,
- a formal definition benefits from a source,
- an algorithm has a canonical source,
- an image needs provenance,
- a current software behaviour needs verification,
- a research claim is being discussed.

Use a bibliography/reference section for broader textbook attribution.

---

# 8. Citation Placement

Citations should appear close enough to the claim they support.

Prefer:

> The DCT concentrates much of the image energy into a relatively small number of coefficients for many natural images. [REF]

over:

> Several pages later: “Sources: …”

The second makes provenance difficult to reconstruct.

---

# 9. Technical Claim Levels

Classify claims mentally before citing them.

### Level A — Stable foundational fact

Example:

> A grayscale image can be represented as a 2-D array of intensity values.

Usually supported by standard textbook treatment.

### Level B — Specific algorithmic statement

Example:

> The Sobel operator approximates first-order image gradients using two directional kernels.

Prefer a formal reference.

### Level C — Research/history claim

Prefer original paper or authoritative historical source.

### Level D — Software/tool behaviour

Use current official documentation.

### Level E — Performance claim

Require careful evidence and context.

Avoid unsupported statements such as:

> “Method X is always faster.”

---

# 10. Textbook Usage

Textbooks should be treated as conceptual anchors.

Suggested role:

```text
Gonzalez & Woods
→ classical DIP foundations

Szeliski
→ broader computer vision context

Rosebrock
→ practical deep-learning/computer-vision implementation context

Solem
→ Python-oriented computer vision programming context
```

The exact coverage should be checked against the edition/source actually used.

Do not attribute a specific page or section unless verified.

---

# 11. Research Paper Policy

Use primary papers when a concept is historically or technically tied to a specific method.

Examples of categories:

```text
SIFT
HOG
ResNet
YOLO family
Autoencoders
Optical Flow methods
JPEG / DCT-related standards and literature
```

When citing research:

- identify the original method where relevant,
- avoid claiming that the paper represents all later variants,
- distinguish the original method from modern implementations.

---

# 12. Software Documentation Policy

For changing libraries and frameworks:

```text
CURRENT OFFICIAL DOCUMENTATION
        ↓
implementation details
        ↓
practical file
```

Do not hard-code unstable UI/API assumptions into the conceptual Main Book.

Implementation files should state the tested version where practical.

---

# 13. Image Provenance System

Every non-original external visual must be traceable.

Record:

| Field | Purpose |
|---|---|
| Asset ID | Stable identity |
| Source | Where it came from |
| Creator | Attribution |
| License | Usage rights |
| URL | Retrieval/provenance |
| Access date | Version/provenance context |
| Modification | Whether edited |
| Placement | Which chapter uses it |

---

# 14. Preferred Visual Source Strategy

Priority:

```text
1. Original teaching diagram created for DIP MiniBook
2. Public-domain / appropriately licensed source
3. Official source visual where reuse is permitted
4. External image with clear permission/license
5. Screenshot used only when necessary
```

Do not assume that an image being available on a website means it is reusable.

---

# 15. Generated Visuals

Generated or newly designed illustrations should record:

```text
asset ID
concept
purpose
creation method
human review status
```

A generated illustration must still be technically reviewed.

A visually attractive but incorrect filter diagram is worse than no diagram.

---

# 16. Dataset Records

Image/video datasets used for examples or practical work should have records.

Capture:

```text
dataset name
source
license/terms
task
image/video format
expected dimensions if fixed
splitting method if relevant
limitations / bias notes
```

Do not assume that all public datasets have identical usage terms.

---

# 17. Resource Selection by Learning Goal

A learner should not be given ten equivalent links.

For important topics, prefer a compact pattern:

```text
CORE REFERENCE
→ authoritative textbook/source

IMPLEMENTATION
→ current official documentation

OPTIONAL DEEPENING
→ one strong supplementary resource
```

Only expand the list when different resources serve genuinely different purposes.

---

# 18. Resource Cards

A learner-facing resource card should say why the resource matters.

Example:

> **Gonzalez & Woods — Digital Image Processing**  
> **Use for:** classical DIP theory, mathematical foundations, enhancement/restoration and transforms.

Not:

> Gonzalez & Woods — link

---

# 19. Resource Reliability Notes

Where appropriate, maintain:

```text
AUTHORITATIVE
STRONG
SUPPORTING
OPTIONAL
UNVERIFIED
```

`UNVERIFIED` resources should not be used as primary support for important claims.

---

# 20. Current-Information Boundary

Some DIP concepts are stable:

```text
sampling
quantization
histograms
convolution
Fourier transform
morphology
DCT
```

Other details change:

```text
software APIs
framework commands
model releases
hardware support
cloud tooling
dataset availability
licensing
```

For changing details, verify current documentation at the time of implementation.

---

# 21. Citation Consistency

Use one citation convention across the DIP system.

The final web/PDF rendering may transform the exact syntax, but the underlying record should remain stable.

Recommended conceptual notation:

```text
[RS-K07.02-01]
```

or a rendered bibliography link tied to the same resource ID.

Do not create multiple IDs for the same resource unless different editions/versions materially differ.

---

# 22. Edition and Version Discipline

For books:

```text
title
author
edition
publisher
year
```

For software:

```text
tool
version
documentation version/date where available
```

For standards:

```text
standard
version
issuer
date
```

This prevents “version drift.”

---

# 23. Source Conflict Policy

When two sources disagree:

```text
1. Identify the exact claim.
2. Identify whether the disagreement is factual, definitional,
   version-specific, convention-specific, or contextual.
3. Prefer the higher-authority source.
4. Preserve legitimate convention differences explicitly.
5. Record the decision in MASTER QA if it affects multiple files.
```

Never silently blend conflicting definitions.

---

# 24. Convention Tracking

DIP contains convention-sensitive material.

Examples:

- coordinate origin
- row/column indexing
- convolution vs correlation notation
- Fourier spectrum centering
- frequency-coordinate ordering
- RGB channel order in software
- image intensity range
- rounding/clipping behaviour

When a convention affects results, state it.

---

# 25. Resource-to-Concept Coverage

MASTER-04 should eventually provide:

```text
Concept
→ Main
→ Math
→ Lab
→ Code
→ Exam
→ Practice
→ Resource
```

This makes it possible to discover what is missing.

Example:

```text
K12.01 Fourier Transform

MAIN      ✓
MATH      ✓
LAB       ✓
CODE      ✓
EXAM      ✓
PRACTICE  ?
RESOURCE  ✓
```

The question mark becomes a visible integration gap.

---

# 26. Resource Duplication Policy

Avoid:

```text
same textbook listed in 14 different chapter bibliographies
```

Instead:

```text
RESOURCE-00 / RESOURCE-04
→ canonical bibliography

chapters
→ local reference IDs
```

The rendered reader experience can still show local references.

---

# 27. Research Depth Levels

For extended topics:

### Level 1 — Textbook understanding

Enough for course learning.

### Level 2 — Implementation understanding

Enough to implement.

### Level 3 — Research understanding

Enough to understand the original method, assumptions and major limitations.

### Level 4 — Current landscape

Used only when useful for modern context and verified with current sources.

The Main Book should usually operate at Levels 1–2, with controlled Level 3/4 extensions.

---

# 28. Resource QA Checklist

Before release:

- [ ] Resource title is correct.
- [ ] Author/creator is correct.
- [ ] Edition/version is correct where relevant.
- [ ] Source URL is valid where used.
- [ ] License/usage status recorded for external visual assets.
- [ ] Resource is mapped to at least one concept.
- [ ] Reason for inclusion is clear.
- [ ] No unsupported performance claim depends on it.
- [ ] Current software documentation is not mistaken for stable theory.
- [ ] Duplicate resource records have been merged.

---

# 29. Minimal Learner-Facing Resource Layer

The learner should normally see:

```text
CORE REFERENCE
1–2 sources

DEEPEN
1–3 carefully chosen sources

IMPLEMENT
official documentation where relevant
```

The complete provenance inventory remains in the Resource/Master files.

---

# 30. Definition of Done

The resource system is ready when:

- every major concept has an appropriate reference path,
- official course references are represented,
- important visuals have provenance,
- changing implementation details point toward current documentation,
- research methods have appropriate primary references where needed,
- resource IDs are stable,
- source conflicts are recorded rather than hidden,
- no citation exists merely for decoration,
- MASTER-04 can answer “where did this concept come from?”.
