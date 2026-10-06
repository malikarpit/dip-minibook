---
id: "MATH-00"
title: "Digital Image Processing — Mathematics Companion Foundation & Learning Map"
layer: "MATH"
system: "Engineering Minibooks · Digital Image Processing"
version: "1.0"
status: "ARCHITECTURE LOCK"
---

# MATH-00 — Mathematics Companion Foundation & Learning Map

> **Purpose:** Provide a dedicated mathematical route through Digital Image Processing without making the Main Book mathematically shallow or forcing every learner to study all mathematical derivations before progressing.

---

# 1. Why DIP Needs a Mathematics Companion

Digital Image Processing is fundamentally mathematical because an image can be represented as structured numerical data.

```text
IMAGE
↓
FUNCTION / ARRAY
↓
MATRIX / VECTOR / TENSOR
↓
TRANSFORMATION
↓
FILTER / OPERATOR
↓
MEASUREMENT
↓
DECISION
```

The Main Book teaches the mathematics needed at the point of use.

The Math Companion goes deeper into:

- notation,
- matrices,
- vectors,
- discrete functions,
- probability and statistics,
- derivatives and gradients,
- convolution,
- transforms,
- coding/entropy,
- image-quality measures,
- mathematical aspects of CNNs.

---

# 2. Governing Rule

The Math Companion must answer:

> **What mathematics is required to understand, calculate, derive, implement or evaluate this DIP concept?**

It must not become a generic mathematics textbook.

Every mathematical topic should eventually map to one or more DIP concepts.

---

# 3. Mathematical Learning Model

Use:

```text
INTUITION
↓
NOTATION
↓
DEFINITION
↓
FORMULA
↓
SMALL NUMERICAL EXAMPLE
↓
MATRIX / GRAPH / VISUAL
↓
DIP INTERPRETATION
↓
APPLICATION
```

For difficult topics:

```text
intuition
→ derivation
→ worked example
→ edge cases
→ engineering interpretation
```

---

# 4. Mathematical Prerequisite Levels

## Level M0 — Arithmetic

- arithmetic
- fractions
- percentages
- powers
- logarithms
- rounding

## Level M1 — Algebra

- equations
- functions
- transformations
- coordinate notation
- summation notation

## Level M2 — Linear Algebra

- vectors
- matrices
- matrix multiplication
- element-wise operations
- dot products
- linear transformations

## Level M3 — Discrete Mathematics for Images

- discrete coordinates
- finite sums
- neighbourhoods
- sets
- binary representations

## Level M4 — Calculus

- derivatives
- partial derivatives
- gradients
- second derivatives

## Level M5 — Probability & Statistics

- probability
- distributions
- expectation
- variance
- covariance
- entropy

## Level M6 — Transforms

- Fourier concepts
- DFT
- 2-D DFT
- DCT

## Level M7 — Optimization / Learning Mathematics

- loss
- gradients
- optimization
- learned convolution
- reconstruction objectives

The learner should not need to master every level before beginning DIP.

---

# 5. Proposed Math Companion Structure

```text
MATH-00
Foundation and navigation

M01 — Mathematical Notation for DIP
M02 — Functions, Coordinates and Discrete Images
M03 — Summation, Products and Indexing
M04 — Vectors and Image Feature Representation
M05 — Matrices and Image Representation
M06 — Matrix Operations for DIP
M07 — Linear Operators and Transformations
M08 — Convolution and Correlation Mathematics

M09 — Intensity Statistics
M10 — Probability, Histograms and Empirical Distributions
M11 — Mean, Variance and Standard Deviation
M12 — Covariance and Correlation
M13 — Entropy and Information

M14 — Discrete Derivatives and Gradients
M15 — Second Derivatives and the Laplacian
M16 — Geometric Coordinate Transformations
M17 — Interpolation Mathematics

M18 — Fourier Mathematics
M19 — DFT and 2-D DFT
M20 — Frequency-Domain Filtering Mathematics
M21 — DCT Mathematics

M22 — Mathematical Morphology and Set Operations
M23 — Compression Mathematics and Coding Efficiency
M24 — Image Quality Metrics

M25 — CNN Mathematics: Tensors, Convolution and Feature Maps
M26 — Learning and Reconstruction Objectives

MATH-99 — Master Formula & Mathematical Revision
```

The exact chapter count may be adjusted if later production reveals that two mathematical topics are better combined. The mathematical dependency map should remain stable even if filenames change.

---

# 6. M01 — Mathematical Notation for DIP

Teach:

- scalar
- variable
- function
- subscript
- superscript
- index
- set
- sum
- product
- range
- domain
- coordinate pair
- vector notation

Example:

\[
f(x,y)
\]

means an image intensity value indexed by spatial coordinates \(x,y\).

Important principle:

> Mathematical notation must always be translated back into image meaning.

---

# 7. M02 — Functions, Coordinates and Discrete Images

Bridge:

```text
continuous function
→ sampled function
→ discrete image
```

Cover:

\[
f(x,y)
\]

versus a digital image:

\[
f[m,n]
\]

Discuss the conceptual difference between continuous and discrete spatial variables.

---

# 8. M03 — Summation, Products and Indexing

Needed for:

- convolution,
- filtering,
- histograms,
- MSE,
- entropy,
- DFT.

Examples:

\[
\sum_{x=0}^{M-1}\sum_{y=0}^{N-1} f(x,y)
\]

Teach how to read the notation, determine bounds, and calculate a small example.

---

# 9. M04 — Vectors and Image Feature Representation

Teach:

- vector notation,
- components,
- dimensions,
- feature vectors,
- magnitude,
- dot product.

DIP connection:

```text
image
→ extracted features
→ feature vector
```

Later connect to:

- descriptors,
- classification,
- CNN features.

---

# 10. M05 — Matrices and Image Representation

Teach a grayscale image as:

\[
I=
\begin{bmatrix}
i_{11}&i_{12}&\cdots\\
i_{21}&i_{22}&\cdots\\
\vdots&\vdots&\ddots
\end{bmatrix}
\]

Cover:

- dimensions,
- row/column indices,
- submatrices,
- neighbourhoods,
- element access.

Use small hand-solvable images.

---

# 11. M06 — Matrix Operations for DIP

Cover:

- addition,
- subtraction,
- scalar multiplication,
- element-wise multiplication,
- matrix multiplication,
- transpose where relevant.

Explicitly distinguish:

\[
A\odot B
\]

from:

\[
AB
\]

when notation is used.

This distinction is important for avoiding implementation mistakes.

---

# 12. M07 — Linear Operators and Transformations

Explain:

> A linear operator combines input values according to a rule while satisfying linearity properties.

Bridge to:

- filtering,
- convolution,
- transform operations.

Do not overstate linearity for operations such as median filtering, thresholding and morphology.

---

# 13. M08 — Convolution and Correlation Mathematics

This is one of the most important mathematical chapters.

Cover:

- neighbourhood indexing,
- kernel,
- correlation,
- convolution,
- kernel reversal,
- discrete 2-D convolution,
- normalization,
- boundaries.

Generic form:

\[
g[m,n]
=
\sum_k\sum_l
f[k,l]\,h[m-k,n-l]
\]

State the indexing convention used in the book.

Work through a small matrix example.

Explicitly show:

```text
correlation
→ no kernel reversal

convolution
→ kernel reversal
```

and explain why many software implementations appear to use correlation-like behaviour even when the operation is casually called convolution.

---

# 14. M09 — Intensity Statistics

Cover:

- minimum,
- maximum,
- mean,
- median,
- mode,
- range,
- dynamic range.

Explain why a statistic can describe an image but does not preserve all its spatial structure.

---

# 15. M10 — Probability, Histograms and Empirical Distributions

Connect:

```text
pixel counts
→ histogram
→ normalized histogram
→ empirical probability distribution
```

Use:

\[
p(r_k)=\frac{n_k}{MN}
\]

for an image with \(M\times N\) pixels.

Then work through a tiny image.

---

# 16. M11 — Mean, Variance and Standard Deviation

Cover:

\[
\mu = \frac{1}{N}\sum_i x_i
\]

and variance:

\[
\sigma^2=\frac{1}{N}\sum_i(x_i-\mu)^2
\]

State the context carefully because different statistical conventions use different denominators.

DIP interpretation:

- mean relates to average intensity,
- variance describes intensity spread,
- neither alone describes spatial arrangement.

---

# 17. M12 — Covariance and Correlation

Useful when discussing:

- image/channel relationships,
- feature relationships,
- multidimensional representations.

Distinguish:

> covariance measures joint variation;

from:

> correlation is a normalized measure of linear association.

Do not imply that correlation captures all forms of dependence.

---

# 18. M13 — Entropy and Information

Core formula:

\[
H(X)=-\sum_i p_i\log_2 p_i
\]

Explain:

```text
high predictability
→ lower uncertainty

many equally likely symbols
→ higher uncertainty
```

Then connect entropy to image compression.

Include:

- a tiny numerical example,
- units in bits/symbol,
- interpretation,
- limits of entropy as a complete compression-performance predictor.

---

# 19. M14 — Discrete Derivatives and Gradients

Teach first differences before formal continuous calculus.

Example:

\[
\Delta_x f \approx f(x+1,y)-f(x,y)
\]

Then connect to:

- edge detection,
- Sobel,
- Prewitt,
- gradient magnitude.

---

# 20. M15 — Second Derivatives and the Laplacian

Teach:

\[
\nabla^2 f
=
\frac{\partial^2f}{\partial x^2}
+
\frac{\partial^2f}{\partial y^2}
\]

Then explain discrete approximations and what the second derivative responds to.

Connect to sharpening/edge emphasis.

---

# 21. M16 — Geometric Coordinate Transformations

Cover:

- translation,
- scaling,
- rotation,
- coordinate mapping,
- homogeneous coordinates as an optional deep dive.

Matrix representation where useful:

\[
\begin{bmatrix}
x'\\
y'
\end{bmatrix}
=
A
\begin{bmatrix}
x\\
y
\end{bmatrix}
+
b
\]

Then connect to image warping.

---

# 22. M17 — Interpolation Mathematics

Cover:

- nearest neighbour,
- linear/bilinear interpolation,
- weighted neighbourhood interpretation.

Work through a one-dimensional example before the 2-D case.

Explain why interpolation creates estimated values rather than recovering unknown original values perfectly.

---

# 23. M18 — Fourier Mathematics

Begin with the conceptual model:

```text
complicated signal
≈ combination of simpler oscillatory components
```

Then introduce:

- frequency,
- amplitude,
- phase,
- complex representation.

Do not begin with a full 2-D transform equation without intuition.

---

# 24. M19 — DFT and 2-D DFT

Introduce the discrete Fourier transform.

For 1-D:

\[
F[k]=
\sum_{n=0}^{N-1}
f[n]e^{-j2\pi kn/N}
\]

Then build toward 2-D.

Explain:

- index variables,
- frequency bins,
- complex output,
- magnitude,
- phase.

Include a very small numerical DFT example.

---

# 25. M20 — Frequency-Domain Filtering Mathematics

Show the basic relation:

```text
image
→ transform
→ multiply by filter
→ inverse transform
```

Conceptually:

\[
G(u,v)=H(u,v)F(u,v)
\]

Then explain the assumptions and why multiplication in the frequency domain corresponds to convolution-related operations in the spatial domain.

---

# 26. M21 — DCT Mathematics

Cover:

- cosine basis,
- block transform,
- coefficients,
- low/high spatial-frequency interpretation,
- energy concentration intuition.

Use an intentionally tiny block example where possible rather than pretending a full JPEG block calculation is hand-friendly.

---

# 27. M22 — Mathematical Morphology

Introduce the set interpretation of a binary image.

Cover:

- sets,
- structuring element,
- Minkowski-style intuition where useful,
- erosion,
- dilation,
- opening,
- closing.

Use binary matrices throughout.

---

# 28. M23 — Compression Mathematics and Coding Efficiency

Connect:

```text
representation
→ redundancy
→ coding
→ fewer bits
```

Cover:

- bits/symbol,
- average code length,
- prefix codes,
- compression ratio.

Compression ratio:

\[
CR=\frac{\text{original size}}{\text{compressed size}}
\]

Be explicit about whether sizes refer to bytes, bits or another measure.

---

# 29. M24 — Image Quality Metrics

Cover:

### MSE

\[
MSE=
\frac{1}{MN}
\sum_{x=0}^{M-1}
\sum_{y=0}^{N-1}
[f(x,y)-g(x,y)]^2
\]

### RMSE

\[
RMSE=\sqrt{MSE}
\]

### PSNR

\[
PSNR=
10\log_{10}
\left(
\frac{MAX_I^2}{MSE}
\right)
\]

State:

- assumptions,
- intensity range,
- interpretation,
- edge cases,
- why numerical quality metrics do not fully capture perceptual quality.

---

# 30. M25 — CNN Mathematics

Bridge classical DIP to deep learning.

Cover:

- tensor dimensions,
- kernel dimensions,
- output feature-map dimensions,
- learned weights,
- bias,
- activation.

A key formula:

\[
z = \sum_i w_i x_i+b
\]

Then connect the 1-D conceptual model to 2-D convolution.

---

# 31. M26 — Learning and Reconstruction Objectives

Cover only the mathematics needed for the DIP syllabus's deep-learning extension.

Examples:

- reconstruction loss,
- classification loss intuition,
- gradient-based optimization.

The Main Book should remain the conceptual home of CNNs and autoencoders; this chapter provides mathematical depth where useful.

---

# 32. MATH-99 — Master Formula & Mathematical Revision

Organize by purpose rather than chapter:

```text
IMAGE REPRESENTATION
STATISTICS
POINT OPERATIONS
FILTERING
GRADIENTS
TRANSFORMS
MORPHOLOGY
COMPRESSION
QUALITY
CNN
```

Every formula should show:

```text
formula
→ variables
→ what it measures/does
→ common use
```

---

# 33. Required Worked-Example Families

Across the Math Companion, deliberately include:

1. intensity-transform calculation,
2. histogram/CDF calculation,
3. convolution,
4. gradient/Sobel response,
5. thresholding,
6. morphology,
7. entropy,
8. RLE/Huffman,
9. DCT/transform example,
10. MSE/PSNR,
11. geometric interpolation,
12. CNN output-size calculation.

---

# 34. Mathematical Error-Control Rules

Every numerical example should be checked for:

- arithmetic accuracy,
- indexing consistency,
- dimensions,
- units,
- rounding,
- boundary assumptions,
- valid parameter ranges,
- denominator conventions,
- log base,
- datatype/range assumptions.

---

# 35. Formula Status

Use:

```text
CORE
→ expected course mathematics

SUPPORT
→ helps understanding

DEEP DIVE
→ rigorous extension

REFERENCE
→ useful formula but not required for the course path
```

Do not imply that every formula is equally important for examination.

---

# 36. Math-to-Main Linking

Examples:

```text
C07 Histogram
→ M10 Probability, Histograms and Empirical Distributions

C08 Convolution
→ M08 Convolution and Correlation Mathematics

C10 Edge Detection
→ M14–M15 Derivatives and Laplacian

C12 Fourier
→ M18–M20 Fourier Mathematics

C24 JPEG
→ M21 DCT + M23 Compression Mathematics

C26 CNN
→ M25 CNN Mathematics
```

---

# 37. Mathematics Companion Definition of Done

- [ ] Every major mathematical dependency has a destination.
- [ ] Important formulas have numerical examples.
- [ ] Matrix calculations are dimensionally correct.
- [ ] Convolution/correlation conventions are explicit.
- [ ] Statistical denominator conventions are clear.
- [ ] Fourier notation is internally consistent.
- [ ] DCT notation is declared where multiple conventions exist.
- [ ] Image-quality formulas state assumptions.
- [ ] CNN dimension calculations are checked.
- [ ] Main Book remains understandable without reading every Math chapter.
