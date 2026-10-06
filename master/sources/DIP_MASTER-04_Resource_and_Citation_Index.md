---
id: "MASTER-04"
title: "Digital Image Processing — Resource & Citation Index"
layer: "MASTER"
version: "1.0"
status: "FOUNDATION LOCK"
---

# MASTER-04 — Resource & Citation Index

> **Role:** Maintain the authoritative concept-to-source relationship and prevent bibliography duplication or provenance gaps.

---

# 1. Relationship Model

```text
CONCEPT
 ↓
COURSE SOURCE
 ↓
DEEPER SOURCE
 ↓
RESEARCH / PRIMARY SOURCE
 ↓
IMPLEMENTATION DOCUMENTATION
 ↓
VISUAL / DATASET PROVENANCE
```

Not every concept needs every source type.

---

# 2. Resource Record

```yaml
resource_id: "RS-K12.01-01"
concept_id: "K12.01"
type: "TEXTBOOK"
role: "CONCEPTUAL"
authority: "HIGH"
status: "VERIFIED"
```

---

# 3. Citation Status

```text
UNVERIFIED
VERIFIED
OUTDATED
REPLACE
DEPRECATED
```

---

# 4. Provenance Audit

For every external asset or important external claim:

```text
source identified
→ source purpose identified
→ usage/provenance recorded
→ concept linked
```

---

# 5. Resource Coverage Table

| Concept | Course source | Deepening | Official tool | Visual provenance |
|---|---:|---:|---:|---:|
| Sampling | ✓ | ✓ | — | ✓ |
| Convolution | ✓ | ✓ | ✓ | ✓ |
| Fourier filtering | ✓ | ✓ | ✓ | ✓ |
| JPEG | ✓ | ✓ | ✓ | ✓ |
| CNN | ✓ | ✓ | ✓ | ✓ |

---

# 6. Source Conflict Log

When a material decision is made:

```yaml
claim: "..."
sources:
  - "RS-..."
decision: "..."
reason: "authority/version/convention"
affected_concepts:
  - "K..."
```

---

# 7. Definition of Done

MASTER-04 should make it possible to answer:

> Where did this important technical statement come from?

> What is the best source for learning it?

> Is the linked software guidance still current?

> Does this visual have known provenance?
