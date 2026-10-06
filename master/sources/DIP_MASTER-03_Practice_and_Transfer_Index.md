---
id: "MASTER-03"
title: "Digital Image Processing — Practice & Transfer Index"
layer: "MASTER"
version: "1.0"
status: "FOUNDATION LOCK"
---

# MASTER-03 — Practice & Transfer Index

> **Role:** Central index linking practice items to concepts and avoiding duplicate question collections across the Main, Exam and Practice layers.

---

# 1. Ownership

```text
PRACTICE FILES
→ own the problem/solution content

EXAM FILES
→ own exam-form questions

MASTER-03
→ owns the index and coverage map
```

---

# 2. Practice Record

```yaml
id: "P-K08.03-01"
concept: "K08.03"
type: "MATRIX"
difficulty: "L2"
main: "C08"
math: "M08"
lab: "LAB-U2-01"
exam: "EXAM-U2"
status: "ACTIVE"
```

---

# 3. Coverage Matrix

| Concept | Guided | Standard | Numerical | Visual | Transfer | Debug |
|---|---:|---:|---:|---:|---:|---:|
| Convolution | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Histogram equalization | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Fourier filtering | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Morphology | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

The actual matrix is populated as practice files are produced.

---

# 4. Difficulty Balance

Avoid concentrating all problems at one level.

Target:

```text
foundation
→ independent
→ multi-step
→ transfer
→ debugging
```

---

# 5. Duplicate Detection

Two problems are considered near-duplicates when they share:

```text
same concept
same operation
same reasoning
same answer path
```

Only retain variants when a meaningful parameter or interpretation changes.

---

# 6. Transfer Index

Track problems that change one major assumption.

Examples:

```text
different noise
different illumination
different datatype
different kernel
different image structure
different quality requirement
```

---

# 7. Definition of Done

MASTER-03 should answer:

> Which concepts lack practice?

> Which concepts have too many repetitive questions?

> Which concepts have no transfer/debug practice?
