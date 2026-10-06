---
id: "MASTER-01"
title: "Digital Image Processing — Cross-Book Map & Dependency Graph"
layer: "MASTER"
version: "1.0"
status: "FOUNDATION LOCK"
---

# MASTER-01 — Cross-Book Map & Dependency Graph

> **Role:** Locate every major concept across Main, Math, Practical/Code, Exam, Practice, Resource and Assets.

---

# 1. Integration Model

```text
                      CONCEPT K-ID
                           │
       ┌───────────────────┼───────────────────┐
       │                   │                   │
      MAIN                MATH              PRACTICAL
   understand          calculate/derive         build
       │                   │                   │
       └───────────────────┼───────────────────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
            EXAM        PRACTICE      RESOURCE
            answer        solve        deepen
              │            │            │
              └────────────┼────────────┘
                           │
                         ASSET
                           │
                        MASTERY
```

---

# 2. Relationship Types

```text
PREREQUISITE
→ must/should be understood first

RELATED
→ conceptually connected

DERIVES-FROM
→ current method depends on prior concept

IMPLEMENTS
→ code/lab realizes the concept

ASSESSES
→ exam evaluates the concept

PRACTICES
→ exercise trains the concept

SOURCES
→ resource supports the concept

VISUALIZES
→ asset explains the concept
```

---

# 3. Dependency Examples

```text
C03 Sampling & Quantization
        ↓
C04 Image Representation
        ↓
C06 Point Processing
        ↓
C08 Convolution
   ┌────┴────┐
   ↓         ↓
 C09       C10
smoothing  edges
   │         │
   └────┬────┘
        ↓
C12 Fourier
        ↓
C13 Frequency Filtering
```

---

# 4. Cross-Layer Example

```text
K08.03 — Convolution

MAIN
C08

MATH
M08

LAB/CODE
LAB-U2-01
CL-K08.03-01

EXAM
EXAM-U2

PRACTICE
P-K08.03-...

RESOURCE
RS-K08.03-...

ASSET
D-K08.03-...
```

---

# 5. Metadata Contract

A concept relationship may be represented as:

```yaml
concept_id: "K08.03"
main: "C08"
math:
  - "M08"
lab:
  - "LAB-U2-01"
code:
  - "CL-K08.03-01"
exam:
  - "EXAM-U2"
practice:
  - "P-K08.03-01"
resources:
  - "RS-K08.03-01"
assets:
  - "D-K08.03-01"
prerequisites:
  - "K04.02"
related:
  - "K09.01"
  - "K10.01"
```

---

# 6. Normalization Principle

Do not rename existing readable files merely to satisfy the ID system.

Use:

```text
human-readable file
+
stable concept ID
+
Master mapping
```

This allows gradual normalization.

---

# 7. Integration Status

```text
PLANNED
CONNECTED
VERIFIED
BROKEN
DEPRECATED
```

---

# 8. Dependency Rules

A prerequisite should be marked:

```text
HARD
SOFT
REVIEW
```

Example:

```text
C08 Convolution
HARD → C04 Image Representation
REVIEW → M06 Matrix Operations
```

---

# 9. Integration QA

For every major concept:

- [ ] Main mapping exists.
- [ ] Math mapping exists when needed.
- [ ] Practical mapping exists where applicable.
- [ ] Exam mapping exists.
- [ ] Practice mapping exists.
- [ ] Resource mapping exists.
- [ ] Required visual asset exists.
- [ ] prerequisites are coherent.
- [ ] IDs remain stable.

---

# 10. Definition of Done

MASTER-01 can reconstruct where a learner should go next for any major concept.
