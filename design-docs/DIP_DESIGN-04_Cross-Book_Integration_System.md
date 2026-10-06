---
title: "DESIGN-04 — Digital Image Processing Cross-Book Integration System"
system: "Engineering Minibooks"
subject: "Digital Image Processing"
version: "1.0"
status: "INTEGRATION FOUNDATION"
---

# DESIGN-04 — Digital Image Processing Cross-Book Integration System

> **Purpose:** Define how the DIP Main Book, Math Companion, Practical/Lab and Code layer, Exam layer, Practice layer, Resource layer, Assets layer, and Master controls operate as one system.

---

# 1. Governing Model

The DIP project is one knowledge graph with multiple learning views.

```text
                         ONE DIP KNOWLEDGE GRAPH
                                  │
          ┌───────────────────────┼───────────────────────┐
          │                       │                       │
        MAIN                    MATH                 PRACTICAL
      understand             calculate/derive          build
          │                       │                       │
          └───────────────────────┼───────────────────────┘
                                  │
             ┌────────────────────┼────────────────────┐
             │                    │                    │
           EXAM               PRACTICE              RESOURCE
           answer               solve                deepen
             │                    │                    │
             └────────────────────┼────────────────────┘
                                  │
                               ASSETS
                                  │
                               MASTERY
```

The learner should experience these as connected views, not as unrelated books.

---

# 2. Ownership Contract

| Layer | Primary ownership |
|---|---|
| Main | Canonical conceptual teaching |
| Math | Mathematical prerequisites, derivations and calculation depth |
| Practical/Lab | Experiment procedure, observation, interpretation and submission-oriented workflow |
| Code | Reusable implementation, coding patterns and debugging |
| Exam | Exam-specific recall, answer structures and assessment preparation |
| Practice | Guided problem solving, transfer and debugging practice |
| Resource | Sources, provenance and deeper learning |
| Assets | Visual files and their metadata |
| Master | Integration, inventory, dependencies, progress and QA |
| Design | Rules governing all other layers |

---

# 3. Canonical Concept Identity

Every substantial concept should eventually have a stable concept ID.

Recommended pattern:

```text
K<chapter>.<section>.<concept>
```

Example:

```text
K08.03
```

means a concept inside Chapter 08, Section 03.

Related objects:

```text
F-K08.03-01   Formula
D-K08.03-01   Diagram
EX-K08.03-01  Worked example
P-K08.03-01   Practice
E-K08.03-01   Exam
LAB-K08.03-01 Lab
CL-K08.03-01  Code
M-K08.03-01   Mathematics
RS-K08.03-01  Resource
```

The exact section number may be finalized when the chapter is produced.

---

# 4. Why Canonical IDs Exist

Readable filenames are useful to humans:

```text
DIP_Ch08_Spatial_Filtering_and_Convolution.md
```

IDs are useful to systems:

```text
K08.03
```

The two should coexist.

Do not make filenames unreadable just to force IDs into filenames.

---

# 5. Concept Ownership Rule

For each concept:

```text
MAIN
→ owns the canonical explanation

MATH
→ owns mathematical depth

LAB
→ owns experiment

CODE
→ owns implementation

EXAM
→ owns assessment form

PRACTICE
→ owns repeated solving

RESOURCE
→ owns provenance/deeper learning

ASSETS
→ owns reusable visual material

MASTER
→ owns relationship and status
```

---

# 6. The Connection Strip

Each major Main Book concept should expose a compact connection strip when useful.

Example:

```text
K08.03 · Convolution

UNDERSTAND   → Main Ch 08
CALCULATE    → Math M08...
BUILD        → Code CL-K08.03...
LAB          → LAB-K08.03...
PRACTICE     → P-K08.03...
EXAM         → E-K08.03...
DEEPEN       → RS-K08.03...
VISUAL       → D-K08.03...
```

This lets the reader choose the next learning action without interrupting the main explanation.

---

# 7. Dependency Graph

Concepts should have explicit prerequisite relationships.

Example:

```text
C03 Sampling & Quantization
            ↓
C04 Image Representation
            ↓
C06 Point Processing
            ↓
C08 Convolution
      ┌─────┴─────┐
      ↓           ↓
C09 Smoothing   C10 Edges
      │           │
      └─────┬─────┘
            ↓
C12 Fourier Domain
            ↓
C13 Frequency Filtering
```

The actual graph is maintained in `MASTER-01`.

---

# 8. Cross-Layer Navigation

Use action-oriented language rather than generic “See also.”

Preferred:

```text
Understand → Main
Calculate → Math
Implement → Code
Perform → Lab
Revise → Exam
Practice → Practice
Read more → Resource
Inspect visual → Asset
```

---

# 9. Main-to-Math Rule

The Main Book should include enough mathematics to understand the current concept.

A Math link is needed when:

- the reader wants a deeper derivation,
- a prerequisite is mathematically substantial,
- several chapters depend on the same mathematical idea,
- a numerical treatment is too large for the Main Book.

Do not require the Math Companion simply to understand a basic syllabus definition.

---

# 10. Main-to-Code Rule

Code links should appear when code materially reinforces understanding.

Examples:

```text
image loading
colour conversion
histogram construction
convolution
filtering
Fourier transform
segmentation
morphology
feature detection
JPEG stages
CNN classification
YOLO
optical flow
```

The code layer should identify implementation-specific assumptions rather than silently redefining the theory.

---

# 11. Main-to-Lab Rule

When a topic directly corresponds to a university practical:

```text
LAB BRIDGE
Experiment: ...
Objective: ...
Connection: ...
```

The Main Book explains the concept; the Lab file explains how to perform it.

---

# 12. Main-to-Exam Rule

Main chapters may provide:

```text
EXAM BRIDGE
• Definition
• 5-mark structure
• 10-mark structure
• Numerical pattern
• Diagram pattern
• Comparison pattern
```

Detailed question banks remain in the Exam layer.

---

# 13. Main-to-Practice Rule

At the end of major concepts, suggest a small practice route:

```text
1 guided
1 standard
1 numerical/visual
1 transfer or debug
```

The complete problem set belongs elsewhere.

---

# 14. Resource Linking

Resources should be linked to concepts.

```text
Concept
 ↓
authoritative source
 ↓
optional deeper source
 ↓
implementation documentation
```

This avoids a giant chapter bibliography with no explanation of why each source matters.

---

# 15. Visual Asset Linking

A figure should have an asset ID.

Example:

```text
D-K12.01
```

The Main Book references it.

The asset repository stores the actual visual file and metadata.

This enables:

```text
same teaching diagram
→ web
→ PDF
→ slide
→ practice
```

without manually redrawing it for every output.

---

# 16. Companion Duplication Rule

Do not duplicate complete paragraphs unnecessarily.

Allowed repetition:

```text
Main:
conceptual explanation

Math:
mathematical derivation

Exam:
compressed answer

Code:
implementation explanation

Practice:
problem statement
```

Not allowed:

> Copy the complete Main chapter into Exam, Math and Code.

---

# 17. Cross-Link Granularity

Link to the smallest useful destination.

Prefer:

```text
Math → convolution derivation
```

over:

```text
Math → entire Math Companion
```

But avoid link explosion.

Only expose links that help the current learning task.

---

# 18. Prerequisite Types

Track three types separately:

### Hard prerequisite

Without it, the current topic is difficult to understand.

Example:

```text
Image Representation → Convolution
```

### Soft prerequisite

Useful but not essential.

### Review prerequisite

A previously learned concept that can be refreshed through a short reminder.

This distinction belongs in `MASTER-01`.

---

# 19. Integration States

Each relationship may be:

```text
PLANNED
CONNECTED
VERIFIED
BROKEN
DEPRECATED
```

A broken link or missing companion should become a visible integration issue rather than being silently ignored.

---

# 20. Cross-Book Metadata

Each file should eventually expose metadata including:

```yaml
id:
layer:
part:
unit:
topic_ids:
prerequisites:
related:
math:
lab:
code:
exam:
practice:
resources:
assets:
status:
```

Not every field needs to be populated for every file.

---

# 21. Learning Routes

The system should support several routes.

## Course-first route

```text
Main
→ Lab
→ Practice
→ Exam
```

## Understanding-first route

```text
Main
→ Math
→ Deep Dive
→ Main
```

## Exam-first route

```text
Exam
→ Main
→ Practice
→ Exam
```

## Implementation-first route

```text
Code
→ Main
→ Lab
→ Debug
→ Main
```

## Research/extension route

```text
Main
→ Resource
→ Deep Dive
→ Research source
```

---

# 22. Master Index Responsibilities

`MASTER-00` answers:

> What exists?

`MASTER-01` answers:

> Where does each concept live and what does it depend on?

`MASTER-02` answers:

> What have I mastered?

`MASTER-03` answers:

> What should I practice?

`MASTER-04` answers:

> What should I read or verify?

`MASTER-05` answers:

> Is the system ready to release?

---

# 23. Integration QA

For every major concept:

```text
[ ] Main exists
[ ] Required mathematics exists
[ ] Required practical exists
[ ] Code exists where appropriate
[ ] Exam treatment exists
[ ] Practice exists
[ ] Resource path exists
[ ] Visual assets exist where required
[ ] IDs are stable
[ ] Links are valid
```

A missing optional resource should not block release. A missing required syllabus concept should.

---

# 24. Change Management

When a Main chapter changes:

```text
review concept IDs
→ check formulas
→ check diagrams
→ check code
→ check labs
→ check exam references
→ check practice references
→ update Master index
```

Do not casually alter an ID when the conceptual identity remains the same.

---

# 25. Versioning

Use versions at the system level:

```text
v1.0 architecture lock
v1.1 integration refinement
v1.2 QA correction
```

Chapter files may also have their own status:

```text
DRAFT
REVIEW
QA
RELEASED
```

---

# 26. Integration Anti-Patterns

Avoid:

```text
one giant master document containing all learner content
```

Avoid:

```text
same concept rewritten independently in every companion
```

Avoid:

```text
links to entire books instead of useful destinations
```

Avoid:

```text
companion files created without Main concepts to anchor them
```

Avoid:

```text
resource lists with no provenance or purpose
```

Avoid:

```text
IDs that change whenever a filename changes
```

---

# 27. Definition of Done

The integration system is complete when:

- [ ] Every major Main concept has a stable identity.
- [ ] Prerequisite relationships are represented.
- [ ] Main-to-companion links are defined.
- [ ] Companion ownership is unambiguous.
- [ ] Practice, Lab, Exam and Code do not duplicate Main unnecessarily.
- [ ] Resource provenance is connected.
- [ ] Visual assets have stable identities.
- [ ] Master indexes can reconstruct the system.
- [ ] Broken/obsolete relationships can be identified.
- [ ] A learner can move between learning modes without losing context.
