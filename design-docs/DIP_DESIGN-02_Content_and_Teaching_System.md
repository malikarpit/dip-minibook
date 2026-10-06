---
title: "DESIGN-02 — Digital Image Processing Content & Teaching System"
system: "Engineering Minibooks"
subject: "Digital Image Processing"
version: "1.0"
status: "CONTENT AUTHORING FOUNDATION"
---

# DESIGN-02 — Digital Image Processing Content & Teaching System

> **Purpose:** Define how Digital Image Processing concepts are authored so that the Main Book, Math Companion, Practical/Code layer, Exam layer, Practice layer, and Resource layer all teach the same knowledge from different perspectives.

---

# 1. Governing Principle

## One concept, one identity, many learning views

The DIP system should behave as one knowledge graph.

```text
                         ONE DIP CONCEPT
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
       MAIN                   MATH                 PRACTICAL
     understand            calculate/derive          build
        │                      │                      │
        └──────────────────────┼──────────────────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
            EXAM            PRACTICE          RESOURCE
            answer           solve             verify/deepen
              │                │                │
              └────────────────┼────────────────┘
                               │
                            MASTERY
```

The learning views must not become competing explanations.

---

# 2. Content Ownership

| Layer | Owns | Does not own |
|---|---|---|
| Main | Canonical conceptual explanation | Full exam question bank |
| Math | Deeper derivation and numerical mathematics | Entire conceptual narrative |
| Practical/Lab | Experiment workflow and observation | General theory duplication |
| Code | Implementation patterns and reusable code | Full exam preparation |
| Exam | Compressed answer structures and recall | Canonical conceptual teaching |
| Practice | Repeated problem solving and transfer | Full theory |
| Resource | Sources, provenance, further study | Core teaching narrative |
| Master | Navigation, status, dependencies and QA | Subject teaching |

---

# 3. Content Status System

Every substantial concept can carry explicit status tags.

```text
CORE
EXAM
LAB
MATH
DEEP DIVE
EXTENSION
WARNING
REFERENCE
```

## CORE

Required to understand or satisfy the course scope.

## EXAM

High-yield content for assessment.

## LAB

Directly relevant to practical implementation.

## MATH

Formula, derivation or mathematical dependency.

## DEEP DIVE

More rigorous treatment.

## EXTENSION

Beyond the stated syllabus but useful.

## WARNING

A misconception, caveat, boundary condition or common failure mode.

## REFERENCE

A source or provenance note.

---

# 4. Main Book Teaching Contract

The Main Book is the primary teaching experience.

A major concept should normally progress through:

```text
PROBLEM
↓
INTUITION
↓
CONCEPT
↓
REPRESENTATION
↓
VISUALIZATION
↓
MATHEMATICAL MODEL
↓
WORKED EXAMPLE
↓
ALGORITHM
↓
IMPLEMENTATION CONNECTION
↓
RESULT
↓
INTERPRETATION
↓
LIMITATIONS
↓
APPLICATION
↓
EXAM / LAB / PRACTICE CONNECTION
↓
NEXT CONCEPT
```

Not every step needs to be equally long. The structure is a decision framework, not a rigid page template.

---

# 5. Problem-First Rule

Whenever a technique is introduced, begin by stating the problem it solves.

Weak:

> Median filtering is a nonlinear spatial filter.

Preferred:

> An image contaminated with isolated extreme pixels needs a method that can reject those outliers without averaging them into their neighbours. Median filtering addresses this by replacing a pixel with the median value in a local neighbourhood.

Then formalize the method.

This ensures that algorithms are introduced as solutions rather than vocabulary.

---

# 6. Intuition Before Formalism

Use a progression:

```text
plain language
→ visual intuition
→ precise definition
→ mathematical representation
```

Do not introduce a dense formula before the reader understands what quantity or operation the formula represents.

---

# 7. Representation Before Operation

Before manipulating an image, establish what is being manipulated.

Depending on the topic, identify:

```text
image dimensions
channels
datatype
intensity range
spatial coordinates
neighbourhood
colour space
sampling grid
```

Example:

```text
Image
= 512 × 512
= grayscale
= uint8
= intensity range 0–255
```

The exact values in examples must be declared, not assumed.

---

# 8. The DIP Concept Ladder

Use this hierarchy to control depth.

### Level 1 — Recognition

> What is the concept?

### Level 2 — Understanding

> Why does it exist?

### Level 3 — Mechanics

> How does it work?

### Level 4 — Computation

> Can I calculate it?

### Level 5 — Implementation

> Can I implement it?

### Level 6 — Evaluation

> Can I judge its result?

### Level 7 — Transfer

> Can I choose or adapt it in a new situation?

A concept is considered deeply taught when the learner can move through the later levels, not merely define it.

---

# 9. Image Explanation Contract

Every substantial visual operation should be explained as a transformation:

```text
INPUT IMAGE
+
PARAMETERS
+
OPERATION
=
OUTPUT IMAGE
```

Then answer:

```text
What changed?
Why did it change?
What information was preserved?
What information was suppressed?
What artifacts might appear?
```

---

# 10. Matrix Explanation Contract

For local operations, use small matrices.

Minimum sequence:

```text
Input neighbourhood
→ operator/kernel/structuring element
→ arithmetic
→ output
```

### Example authoring pattern

```text
Given:

A = [...]

Kernel:

K = [...]

Required:

Output at the centre pixel.

Step 1:
Multiply corresponding entries.

Step 2:
Sum the products.

Step 3:
Apply scale/normalization if required.

Step 4:
Interpret the result.
```

Explicitly state whether the operation is being described as convolution or correlation, especially when kernel orientation matters.

---

# 11. Formula Contract

For every important formula:

## 1. Formula

Display clearly.

## 2. Symbols

Define every symbol.

## 3. Conditions

State assumptions, domains, dimensions or special cases.

## 4. Meaning

Explain what the equation says physically or computationally.

## 5. Worked example

Use actual values.

## 6. Interpretation

Explain the result in image-processing terms.

## 7. Trap

State at least one likely misconception for high-risk formulas.

---

# 12. Worked Example Contract

Use:

```text
GIVEN
↓
FIND
↓
RELEVANT FORMULA / RULE
↓
SUBSTITUTE
↓
CALCULATE
↓
ANSWER
↓
INTERPRET
```

Do not skip intermediate values when they are educationally important.

For matrix examples, retain enough visible arithmetic for the reader to reproduce the calculation.

---

# 13. Visual Example Contract

A visual example should have an explicit purpose.

Preferred forms:

```text
original → transformed

original → degraded → restored

image → histogram → mapping → result

image → Fourier spectrum → mask → output

image → segmentation mask → extracted object

image → features → descriptor → matching
```

Each figure must be followed by interpretation, even when the visual seems self-explanatory.

---

# 14. Algorithm Contract

Algorithms should be expressed in three forms when useful:

### Conceptual

```text
Input → processing → output
```

### Procedure

Numbered human-readable steps.

### Technical

Pseudocode or code.

Do not substitute code for algorithmic explanation.

---

# 15. Explanation of Parameters

Whenever a technique has meaningful parameters, explain them.

Example categories:

| Parameter class | Example questions |
|---|---|
| Size | What does kernel size change? |
| Strength | What does sigma/threshold control? |
| Range | What happens at minimum/maximum? |
| Geometry | Does orientation matter? |
| Iterations | What changes with repeated application? |
| Boundary | What happens at image borders? |

A parameter table should identify both **effect** and **trade-off**.

---

# 16. Boundary and Edge-Case Contract

DIP operations often behave differently at borders or extreme values.

Where relevant, explain:

- image borders
- padding/border assumptions
- odd vs even kernel sizes
- constant images
- minimum/maximum intensity
- empty foreground/background
- very small images
- extreme threshold values
- overexposure/underexposure
- heavy noise
- dimension compatibility

Avoid presenting a formula as universally valid when it has hidden conditions.

---

# 17. Comparison-First Topics

When several methods solve similar problems, introduce a comparison frame early.

Examples:

```text
mean vs Gaussian vs median

Sobel vs Prewitt vs Laplacian vs Canny

global vs adaptive thresholding

erosion vs dilation

opening vs closing

SIFT vs SURF vs HOG

lossless vs lossy

RLE vs Huffman vs transform coding
```

For each comparison ask:

```text
What problem?
What input assumption?
What operation?
What output?
What strength?
What weakness?
When would I choose it?
```

---

# 18. “Why This Works” Requirement

Major algorithms should have an explicit causal explanation.

Examples:

### Low-pass filtering

> Removing rapidly varying spatial components suppresses fine detail/noise, which produces a smoother image.

### High-pass filtering

> Emphasizing rapid spatial changes enhances edges and fine detail.

### Median filtering

> Replacing a value with the neighbourhood median reduces the influence of isolated extreme outliers.

### Opening

> Erosion removes small structures; dilation then restores the surviving larger structures, so small isolated foreground components can be removed.

These are conceptual explanations, not substitutes for the mathematical treatment.

---

# 19. “When It Fails” Requirement

Every major algorithm should state at least one important limitation.

Examples:

| Technique | Important limitation |
|---|---|
| Histogram equalization | Can over-enhance some regions or amplify noise |
| Mean filtering | Blurs edges |
| Median filtering | Can remove small legitimate structures when overused |
| Global thresholding | Performs poorly when illumination varies strongly |
| SIFT-like local features | Computational cost and environment sensitivity can matter |
| Lossy compression | Discarded information is not exactly recoverable |
| CNN classification | Performance depends strongly on data, training and distribution |
| Object detection | False positives/negatives and dataset bias remain possible |

Avoid absolute language such as “always,” “never,” or “best” unless the statement is genuinely guaranteed.

---

# 20. Engineering Insight Layer

Major concepts should contain a short practical interpretation:

> **Engineering Insight**

This answers:

- what engineers actually tune,
- what trade-off matters,
- what failure would look like,
- why one method might be preferred.

This keeps the book connected to real systems.

---

# 21. Exam Integration

The Main Book can include a concise local exam bridge:

```text
EXAM BRIDGE
→ definition
→ derivation
→ numerical pattern
→ comparison
→ diagram
```

But detailed questions remain in the Exam layer.

---

# 22. Lab Integration

Use:

```text
LAB BRIDGE
Experiment: ...
What you will implement: ...
What to observe: ...
```

Where possible, link the current concept to the exact experiment.

---

# 23. Practice Integration

Use:

```text
PRACTICE BRIDGE
Try:
1 guided question
1 numerical question
1 interpretation question
1 transfer/debug question
```

The Main Book should not contain the entire practice bank.

---

# 24. Cross-Chapter Continuity

Every chapter should end with:

### What you now know

### What you should be able to do

### What depends on this

### Where this goes next

This creates an explicit dependency chain.

Example:

```text
Sampling & Quantization
        ↓
Image Representation
        ↓
Spatial Operations
        ↓
Convolution
        ↓
Frequency Interpretation
        ↓
CNN Convolution
```

---

# 25. Difficulty Signalling

Use a restrained progression:

```text
FOUNDATION
INTERMEDIATE
ADVANCED
EXTENSION
```

Difficulty should not be inferred from colourful styling alone.

---

# 26. Content Density Rules

### Foundation content

Short paragraphs + more visuals.

### Mechanism-heavy content

Diagrams + matrices + formula walkthroughs.

### Mathematics-heavy content

Stepwise derivations + worked examples.

### Reference-heavy content

Tables + compact lists.

### Exam revision

Dense but highly structured.

---

# 27. Repetition Policy

Repeat concepts only when repetition serves a new purpose.

Allowed:

```text
Main Book:
understand histogram equalization

Math:
calculate it

Exam:
write it

Practice:
solve it

Lab:
implement it
```

Not allowed:

```text
Main Book:
full explanation

Exam:
full explanation again

Code:
full explanation again

Math:
same explanation again
```

Use cross-links instead.

---

# 28. Deep-Dive Policy

A DEEP DIVE should exist when one of these applies:

- the concept is mathematically subtle,
- the algorithm is frequently misunderstood,
- a boundary condition matters,
- the concept connects several chapters,
- the engineering trade-off is important.

Deep dives may be collapsible on the website but must remain accessible in print/PDF.

---

# 29. Extension Policy

Extension content should be marked clearly.

Examples:

```text
EXTENSION
→ ORB beyond the syllabus
→ PSNR as an evaluation measure
→ modern YOLO implementation details
→ optical flow variants
```

Do not allow extension content to crowd out the core syllabus path.

---

# 30. Source Discipline

Technical claims should be traceable when a source is important.

For textbook-level facts, prefer authoritative references such as the prescribed course texts.

For changing software/tool behaviour, use current official documentation when the implementation is being written.

Do not cite a source merely to decorate a paragraph.

---

# 31. Error Prevention Rules

## Terminology

Do not use a term loosely just because common tutorials do.

## Mathematics

Recalculate worked examples independently.

## Code

Check implementation against the stated mathematical operation.

## Visuals

Check every label against the underlying operation.

## Tables

Check that comparisons are genuinely comparable.

## Pipelines

Check that every arrow represents a valid dependency.

---

# 32. Canonical Example Types

Across the Main Book, deliberately distribute:

```text
TYPE A — Tiny numeric example
TYPE B — Small matrix example
TYPE C — Real image example
TYPE D — Algorithm trace
TYPE E — Before/after visual
TYPE F — Engineering scenario
TYPE G — Failure case
TYPE H — Exam-style problem
TYPE I — Implementation/debug example
```

This prevents every chapter from teaching in the same monotonous way.

---

# 33. Recommended Chapter Anatomy

```text
CHAPTER OPENER
│
├── One-Sentence Idea
├── Why This Matters
├── Learning Objectives
├── Prerequisites
│
├── 1. Problem / Motivation
├── 2. Intuition
├── 3. Core Concept
├── 4. Representation
├── 5. Mathematical Model
├── 6. Worked Example
├── 7. Visual Example
├── 8. Algorithm
├── 9. Implementation Connection
├── 10. Interpretation
├── 11. Comparison / Trade-offs
├── 12. Failure Modes
├── 13. Applications
│
├── LAB BRIDGE
├── MATH BRIDGE
├── EXAM BRIDGE
├── PRACTICE BRIDGE
│
├── Key Takeaways
├── Quick Recall
├── Common Traps
└── Connection Forward
```

A short chapter may combine sections. A major chapter may split them further.

---

# 34. Unit-Level Architecture

Each Part/Unit should have:

```text
Part opener
→ learning map
→ prerequisite map
→ chapters
→ unit visual map
→ unit comparison table
→ unit formula map
→ unit practical map
→ unit exam map
→ unit consolidation
```

---

# 35. Unit Consolidation

A consolidation file/page should answer:

> What did this unit teach as a connected system?

Example:

```text
UNIT II

Point operations
      ↓
Histogram
      ↓
Spatial filtering
      ↓
Edges
      ↓
Fourier transform
      ↓
Frequency filtering
      ↓
Restoration
```

Then:

- key distinctions,
- formulas,
- algorithm selection,
- practical mapping,
- exam recall.

---

# 36. Main Book “Canonical Truth” Rule

When a companion file contains a specialized treatment, it must remain consistent with the Main Book's canonical definitions.

If a contradiction is discovered:

```text
flag
→ identify source
→ determine authoritative statement
→ correct the affected file(s)
→ update MASTER QA record
```

Never hide contradictions by silently changing one file.

---

# 37. File-Level Metadata Standard

Every Markdown file should begin with metadata similar to:

```yaml
---
id: "C08"
title: "Spatial Filtering and Convolution"
layer: "MAIN"
part: "II"
unit: "II"
status: "DRAFT | REVIEW | QA | RELEASED"
syllabus: "CORE"
difficulty: "INTERMEDIATE"
prerequisites:
  - "C04"
related:
  - "C09"
  - "C10"
math:
  - "M..."
lab:
  - "LAB..."
exam:
  - "EXAM-U2"
---
```

The exact fields may evolve as the integration system is finalized.

---

# 38. Definition of Done for a Main Chapter

A chapter is ready for release only when:

- [ ] Required scope is covered.
- [ ] Major concepts have clear motivation.
- [ ] Terminology is precise.
- [ ] Important formulas have worked examples.
- [ ] Important matrix operations are demonstrated where appropriate.
- [ ] Visual transformations are interpreted.
- [ ] Algorithms are clearly stated.
- [ ] Implementation assumptions are identified.
- [ ] Limitations are stated.
- [ ] Connections to lab/exam/math/practice exist where useful.
- [ ] No placeholder text remains.
- [ ] Cross-chapter links are valid.
- [ ] Content has passed technical QA.

---

# 39. Final Teaching Principle

The reader should never have to ask:

> “Okay, but what does this actually mean for an image?”

The authoring system exists to answer that question continuously.

```text
MATHEMATICS
must connect to pixels.

PIXELS
must connect to images.

IMAGES
must connect to algorithms.

ALGORITHMS
must connect to outputs.

OUTPUTS
must connect to interpretation.

INTERPRETATION
must connect to engineering decisions.
```
