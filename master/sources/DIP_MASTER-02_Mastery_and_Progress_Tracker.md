---
id: "MASTER-02"
title: "Digital Image Processing — Mastery & Progress Tracker"
layer: "MASTER"
version: "1.0"
status: "FOUNDATION LOCK"
---

# MASTER-02 — Mastery & Progress Tracker

> **Role:** Track learning across independent competence dimensions instead of using one “chapter complete” flag.

---

# 1. Mastery Dimensions

```text
CONCEPT
MATH
PRACTICE
LAB
CODE
EXAM
```

A learner may understand a concept while still being unable to derive it or implement it.

---

# 2. Suggested Statuses

```text
NOT STARTED
LEARNING
PRACTICED
CONFIDENT
MASTERED
REVIEW
```

---

# 3. Concept Record

```yaml
concept_id: "K08.03"
title: "Convolution"

concept: "LEARNING"
math: "PRACTICED"
practice: "LEARNING"
lab: "NOT STARTED"
code: "LEARNING"
exam: "REVIEW"

last_reviewed: "YYYY-MM-DD"
notes: ""
```

---

# 4. Mastery Evidence

## Concept

Can the learner explain what it does and why?

## Math

Can the learner calculate/derive it?

## Practice

Can the learner solve an unfamiliar problem?

## Lab

Can the learner perform and interpret the experiment?

## Code

Can the learner implement and debug it?

## Exam

Can the learner communicate the concept under time/format constraints?

---

# 5. Mastery Threshold

A concept should not be called “mastered” merely because:

```text
chapter read
```

A stronger criterion is:

```text
explain
+
calculate where relevant
+
apply
+
interpret
+
retrieve
```

Not every concept requires code or a lab.

---

# 6. Review Triggers

Mark `REVIEW` when:

- a formula repeatedly causes errors,
- a concept is forgotten after a gap,
- the learner depends heavily on notes,
- an implementation error reveals a conceptual gap,
- exam recall is weak.

---

# 7. Unit-Level Progress

Each unit should summarize:

```text
concept coverage
math coverage
lab completion
code completion
practice performance
exam readiness
```

Avoid inventing a single fake percentage that hides weak dimensions.

---

# 8. Review Queue

Generate a review queue from:

```text
REVIEW statuses
failed practice
failed viva
wrong numericals
unreliable formulas
unresolved misconceptions
```

---

# 9. Mastery Evidence Log

Optional record:

```yaml
date: "YYYY-MM-DD"
concept: "K07.02"
activity: "histogram numerical"
result: "PASS"
independent: true
notes: "CDF mapping now clear"
```

---

# 10. Definition of Done

MASTER-02 is useful when it can tell the learner:

> What do I know?

> What can I calculate?

> What can I implement?

> What should I revise next?
