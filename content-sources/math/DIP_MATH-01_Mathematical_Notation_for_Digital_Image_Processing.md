---
id: "M01"
title: "Mathematical Notation for Digital Image Processing"
layer: "MATH"
part: "03 — Mathematics Companion"
unit_links:
  - "Unit I"
  - "Unit II"
  - "Unit III"
  - "Unit IV"
version: "1.0"
status: "PRODUCTION"
syllabus_scope: "Mathematical notation and representation required to understand, calculate, implement and evaluate the complete DIP syllabus"
tags:
  - digital-image-processing
  - mathematics
  - notation
  - variables
  - indexing
  - functions
  - summation
  - sets
prerequisites:
  - "Arithmetic"
  - "Basic algebra"
related_main:
  - "C01–C31"
---

# M01 — Mathematical Notation for Digital Image Processing

> **Purpose:** Build a notation system that lets the learner read, calculate and communicate Digital Image Processing mathematics without treating mathematical symbols as an independent language.

---

# 1. Why This Chapter Exists

DIP is full of compact mathematical notation.

For example:

\[
f(x,y)
\]

looks simple, but it carries several ideas:

- \(f\) is a function;
- \(x\) and \(y\) are coordinates;
- the pair \((x,y)\) identifies a location;
- \(f(x,y)\) is the intensity/value associated with that location.

Later, the same notation grows into:

\[
g(x,y)
=
\sum_m\sum_n
f(m,n)h(x-m,y-n),
\]

or:

\[
H(u,v)
=
-\sum_k p(k)\log_2p(k),
\]

or:

\[
F(u,v)
=
\sum_x\sum_y
f(x,y)e^{-j2\pi(ux/M+vy/N)}.
\]

The mathematics is not the difficult part by itself.

The difficult part is being able to answer:

> **What does each symbol mean in the image-processing system?**

This chapter builds that translation skill.

---

# 2. Learning Contract

By the end of this chapter, you should be able to:

- distinguish constants, variables, functions and parameters;
- read subscripts and superscripts;
- interpret image coordinates;
- distinguish a scalar, vector, matrix and tensor;
- read finite summation notation;
- read product notation;
- understand set and interval notation;
- distinguish equality, assignment and approximation;
- interpret common operators such as \(\max\), \(\min\), \(|\cdot|\), \(\sqrt{\cdot}\), \(\log\);
- understand index ranges and off-by-one issues;
- translate formulas into plain-language DIP operations;
- write mathematically clear image-processing expressions.

---

# 3. Mathematics Should Always Map Back to an Image

Use this rule:

```text
SYMBOL
  ↓
MATHEMATICAL MEANING
  ↓
IMAGE MEANING
  ↓
ENGINEERING PURPOSE
```

Example:

\[
f(x,y)
\]

becomes:

```text
f       → image function
x,y     → spatial coordinates
f(x,y)  → pixel intensity/value
purpose → access one image sample
```

This is the most important habit in the entire Math Companion.

---

# 4. Scalars

A scalar is a single numerical value.

Examples:

\[
7
\]

\[
255
\]

\[
0.5
\]

\[
\sigma^2
\]

In DIP, scalars can represent:

- a pixel intensity;
- a threshold;
- a filter coefficient;
- a standard deviation;
- a learning rate;
- a compression quality parameter.

### Example

For an 8-bit grayscale image:

\[
g=128.
\]

Here \(g\) is one scalar intensity value.

---

# 5. Variables

A variable represents a value that can change.

Example:

\[
T
\]

may represent a threshold.

Then:

\[
T=128
\]

is one chosen value, while another experiment may use:

\[
T=180.
\]

Do not confuse a variable with a random variable automatically. The word “variable” alone does not imply probability.

---

# 6. Constants

A constant remains fixed within the expression or defined context.

Examples:

\[
255
\]

for the maximum 8-bit sample value, or:

\[
\pi
\]

as the mathematical constant.

A value can be constant within one calculation and variable across experiments.

For example:

```text
MAX = 255
```

may be fixed for an 8-bit experiment but not for a 16-bit image.

---

# 7. Parameters

Parameters control the behaviour of an operation or model.

Examples:

- threshold \(T\);
- standard deviation \(\sigma\);
- kernel size \(K\);
- stride \(S\);
- padding \(P\);
- learning rate \(\eta\).

Example:

\[
G_\sigma(x,y)
\]

uses \(\sigma\) as a parameter controlling Gaussian spread.

---

# 8. Functions

A function maps an input to an output.

Example:

\[
g=T(f).
\]

In DIP:

```text
input image f
      ↓
operation T
      ↓
output image g
```

A point transformation might be written:

\[
s=T(r).
\]

Here:

- \(r\) = input intensity;
- \(T\) = transformation;
- \(s\) = output intensity.

---

# 9. Function of Two Variables

A grayscale image is often represented conceptually as:

\[
f(x,y).
\]

There are two spatial coordinates.

For a particular point:

\[
x=10,\quad y=25,
\]

we might access:

\[
f(10,25).
\]

This returns one scalar value for a scalar grayscale image.

---

# 10. Coordinate Pair

The notation:

\[
(x,y)
\]

represents one location in a 2-D spatial domain.

Example:

\[
(5,8).
\]

Do not automatically assume which coordinate comes first in every software library.

In mathematical notation, the first component is typically horizontal/\(x\), second vertical/\(y\). In array indexing, however, many systems use:

```text
[row, column]
```

which corresponds conceptually to:

```text
[y, x]
```

depending on the convention.

This difference is a major practical source of bugs.

---

# 11. Continuous vs Discrete Coordinates

A theoretical continuous image may use:

\[
x,y\in\mathbb{R}.
\]

A digital image uses a discrete coordinate grid:

\[
x\in\{0,1,\ldots,M-1\}
\]

\[
y\in\{0,1,\ldots,N-1\}.
\]

The continuous model is useful for image formation and theory.

The discrete model is what the computer stores and processes.

---

# 12. Indexing Conventions

Two common conventions are:

### Zero-based

\[
0,1,2,\ldots,N-1
\]

### One-based

\[
1,2,3,\ldots,N.
\]

Python/NumPy use zero-based indexing.

MATLAB uses one-based indexing.

This must be stated when moving between mathematics and code.

---

# 13. Off-by-One Example

Suppose there are:

\[
8
\]

samples.

Zero-based positions are:

\[
0,1,2,3,4,5,6,7.
\]

One-based positions are:

\[
1,2,3,4,5,6,7,8.
\]

Thus the mathematical size can be 8 even though the largest index differs.

This is one of the most common implementation mistakes in image processing.

---

# 14. Dimensions vs Indices

Suppose an image has:

\[
M\times N
\]

pixels.

This means:

```text
number of rows = M
number of columns = N
```

under a common matrix convention.

But if using mathematical coordinates:

```text
x → column
y → row
```

the same image may be described as width \(N\), height \(M\).

Never assume \(M\) always means width.

Define the convention.

---

# 15. Subscripts

A subscript identifies one member of a sequence or a coordinate component.

Examples:

\[
x_i
\]

means the \(i\)-th element.

For an image matrix:

\[
f[m,n]
\]

may denote the sample at row/index \(m\) and column/index \(n\).

In a probability distribution:

\[
p_i
\]

can represent the probability of the \(i\)-th symbol.

---

# 16. Superscripts

A superscript may mean different things depending on context.

Examples:

\[
x^2
\]

means square.

But:

\[
f^{(1)}
\]

may mean first iteration/order/version rather than a power.

Likewise:

\[
I^{(t)}
\]

may indicate the frame at time \(t\).

Therefore:

> **Never interpret a superscript as an exponent without reading the surrounding notation.**

---

# 17. Prime Symbol

A prime can indicate a transformed or estimated quantity.

Examples:

\[
x'
\]

or:

\[
f'(x).
\]

These have different meanings.

In image processing:

\[
f'(x,y)
\]

might mean an intermediate transformed image.

In calculus:

\[
f'(x)
\]

means the derivative of \(f\).

Context determines meaning.

---

# 18. Hat Notation

A hat often indicates an estimate or reconstruction.

For example:

\[
\hat{x}
\]

can mean an estimated value.

In compression:

\[
\hat{I}
\]

may denote the reconstructed image.

Then:

\[
I-\hat I
\]

is the reconstruction error/difference.

This notation appears in restoration, denoising and compression.

---

# 19. Tilde Notation

A tilde can indicate a modified/corrupted version.

For example:

\[
\tilde{x}
\]

might represent a noisy image.

A denoising problem can be expressed as:

\[
\tilde{x}\rightarrow\hat{x}\approx x.
\]

Interpretation:

```text
x
→ clean image

x̃
→ corrupted/noisy image

x̂
→ reconstructed estimate
```

This simple notation makes C29 much easier to read.

---

# 20. Equality, Assignment and Approximation

These are not identical.

### Equality

\[
a=b
\]

means they are mathematically equal.

### Assignment

In programming:

```python
a = b
```

means store \(b\) in \(a\).

### Approximation

\[
a\approx b
\]

means they are close or approximately equal.

### Example

A noisy reconstruction may satisfy:

\[
\hat{I}\approx I
\]

but not:

\[
\hat{I}=I.
\]

---

# 21. Inequalities

Symbols:

\[
<
\]

\[
>
\]

\[
\le
\]

\[
\ge
\]

appear frequently.

Example thresholding:

\[
f(x,y)\ge T.
\]

This means:

> retain/assign one class when the pixel intensity is at least the threshold.

---

# 22. Absolute Value

The notation:

\[
|x|
\]

means the magnitude of a scalar value.

Example:

\[
|-7|=7.
\]

In frame differencing:

\[
D(x,y)=|I_t(x,y)-I_{t-1}(x,y)|.
\]

The absolute value makes change magnitude non-negative.

---

# 23. Norm Notation

For a vector:

\[
\mathbf v=
\begin{bmatrix}
u\\v
\end{bmatrix},
\]

the Euclidean norm is:

\[
\|\mathbf v\|_2
=
\sqrt{u^2+v^2}.
\]

In optical flow, this represents motion-vector magnitude.

Example:

\[
\mathbf v=(3,4)
\]

gives:

\[
\|\mathbf v\|_2=5.
\]

---

# 24. Maximum and Minimum

\[
\max(a,b)
\]

returns the larger value.

\[
\min(a,b)
\]

returns the smaller.

In image processing:

\[
g(x,y)=\max_{(m,n)\in\mathcal N}f(m,n)
\]

is the conceptual basis of a max filter over neighbourhood \(\mathcal N\).

---

# 25. Argmax

A related notation is:

\[
\arg\max_i p_i.
\]

It returns the **index** of the largest value, not the largest value itself.

In classification:

\[
\hat y=
\arg\max_k p(y=k\mid x).
\]

Meaning:

> predict the class whose probability is largest.

This distinction is extremely useful in CNN output interpretation.

---

# 26. Floor and Ceiling

\[
\lfloor x\rfloor
\]

is the greatest integer less than or equal to \(x\).

\[
\lceil x\rceil
\]

is the smallest integer greater than or equal to \(x\).

Example:

\[
\lfloor3.7\rfloor=3
\]

\[
\lceil3.7\rceil=4.
\]

They appear in:

- output-size equations;
- quantization;
- block calculations.

---

# 27. Rounding

\[
\operatorname{round}(x)
\]

maps a real number to an integer according to a specified rounding rule.

For example:

\[
\operatorname{round}(3.7)=4.
\]

In quantization:

\[
\hat F
=
\operatorname{round}
\left(
\frac{F}{Q}
\right).
\]

The exact tie-breaking behaviour can depend on the programming environment.

---

# 28. Square Root

\[
\sqrt{x}
\]

returns the principal non-negative square root.

Examples:

\[
\sqrt{25}=5
\]

and:

\[
\sqrt{u^2+v^2}
\]

gives Euclidean vector magnitude.

---

# 29. Logarithm

\[
\log_b x
\]

is the logarithm of \(x\) to base \(b\).

Important bases in DIP:

```text
ln / log_e
log₂
log₁₀
```

Entropy uses:

\[
\log_2.
\]

PSNR often uses:

\[
\log_{10}.
\]

Never replace one base silently.

---

# 30. Why Log Base Matters

For entropy:

\[
H=-\sum_i p_i\log_2p_i.
\]

The base 2 expresses information in bits.

Using natural logarithm changes the unit to nats.

For most university DIP entropy calculations:

\[
\boxed{\log_2}
\]

should be used unless the problem states otherwise.

---

# 31. Summation Notation

The symbol:

\[
\sum
\]

means addition over an indexed range.

Example:

\[
\sum_{i=1}^{4}x_i
\]

means:

\[
x_1+x_2+x_3+x_4.
\]

This notation appears everywhere in DIP.

---

# 32. Double Summation

For a 2-D image:

\[
\sum_x\sum_y f(x,y)
\]

means:

```text
sum over y
for each x
```

or, operationally, sum all samples over the stated ranges.

Example:

\[
\sum_{x=0}^{1}\sum_{y=0}^{1}f(x,y)
\]

for:

\[
f=
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix}
\]

gives:

\[
1+2+3+4=10.
\]

---

# 33. Order of Summation

For finite sums, changing the order is usually allowed:

\[
\sum_x\sum_y f(x,y)
=
\sum_y\sum_x f(x,y)
\]

provided the same finite set of terms is included.

This is useful when reading DFT/DCT equations.

---

# 34. Product Notation

The product symbol:

\[
\prod
\]

means multiplication across an indexed range.

Example:

\[
\prod_{i=1}^{3}x_i
=
x_1x_2x_3.
\]

It is less common than \(\sum\) in introductory DIP but appears in probability and coding theory.

---

# 35. Sets

A set is a collection of objects.

Example:

\[
S=\{0,1,2,\ldots,255\}.
\]

For an 8-bit grayscale image, the intensity alphabet can be represented conceptually as:

\[
L=\{0,\ldots,255\}.
\]

A pixel value satisfies:

\[
f(x,y)\in L.
\]

---

# 36. Set Membership

The symbol:

\[
\in
\]

means “belongs to.”

Example:

\[
128\in\{0,\ldots,255\}.
\]

The symbol:

\[
\notin
\]

means “does not belong to.”

---

# 37. Intervals

An interval describes a continuous range.

Example:

\[
x\in[0,1]
\]

means:

\[
0\le x\le1.
\]

For normalized image values:

\[
I(x,y)\in[0,1].
\]

This is common for floating-point image representations.

---

# 38. Function Domain and Range

A function has:

```text
domain
→ allowed input values

range
→ possible output values
```

For a point transformation:

\[
T:[0,255]\rightarrow[0,255].
\]

This means:

```text
input intensity
0–255
   ↓
output intensity
0–255
```

A particular operation may use a different output range.

---

# 39. Piecewise Functions

Many DIP operations are naturally expressed piecewise.

Thresholding:

\[
g(x,y)=
\begin{cases}
1,&f(x,y)\ge T\\
0,&f(x,y)<T.
\end{cases}
\]

Interpretation:

```text
condition true
→ output 1

condition false
→ output 0
```

Learn to read the condition first.

---

# 40. Indicator-Style Thinking

A binary mask can be thought of as:

\[
M(x,y)\in\{0,1\}.
\]

For a threshold:

\[
M(x,y)=
\mathbf 1[f(x,y)\ge T].
\]

The indicator is 1 when the condition is true and 0 otherwise.

This notation is useful but optional; the piecewise form is often clearer for exams.

---

# 41. Variables with Time

Video introduces:

\[
I(x,y,t).
\]

Now \(t\) is another index/variable.

For discrete video frames:

\[
t\in\{0,1,\ldots,T-1\}
\]

under zero-based indexing.

Then:

\[
I(x,y,t)
\]

means:

> intensity/value at spatial location \((x,y)\) in frame \(t\).

---

# 42. Channel Index

A colour image may be represented as:

\[
I(x,y,c).
\]

Here:

\[
c\in\{R,G,B\}
\]

or:

\[
c\in\{0,1,2\}.
\]

Thus:

\[
I(x,y,R)
\]

could mean the red-channel value at \((x,y)\).

The specific channel indexing convention should always be declared.

---

# 43. Batch Index in Deep Learning

A neural-network tensor may include:

\[
X(b,x,y,c)
\]

where \(b\) is the sample/batch index.

This can become:

\[
B\times H\times W\times C.
\]

The exact order depends on the framework.

The mathematics describes dimensions; software determines the memory/tensor convention.

---

# 44. Scalar Image vs Vector-Valued Image

A grayscale image can be treated as scalar-valued:

\[
f(x,y)\in\mathbb R.
\]

A colour image can be vector-valued:

\[
\mathbf f(x,y)
=
\begin{bmatrix}
R(x,y)\\
G(x,y)\\
B(x,y)
\end{bmatrix}.
\]

This makes an important distinction:

```text
grayscale pixel
→ one value

RGB pixel
→ three values
```

---

# 45. Matrix Notation

A grayscale image can also be represented as a matrix:

\[
F=
\begin{bmatrix}
f_{00}&f_{01}&f_{02}\\
f_{10}&f_{11}&f_{12}\\
f_{20}&f_{21}&f_{22}
\end{bmatrix}.
\]

This is a convenient finite representation.

The same data can therefore be described in different mathematical languages:

```text
function view
f(x,y)

array view
F[m,n]

matrix view
F
```

These are related representations, not automatically different images.

---

# 46. Vector Notation

A vector is often written:

\[
\mathbf{x}.
\]

For example:

\[
\mathbf{x}=
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}.
\]

A feature descriptor may be:

\[
\mathbf d\in\mathbb R^n.
\]

This means:

> descriptor \(d\) has \(n\) numerical components.

---

# 47. Transpose

The superscript \(T\) commonly denotes transpose:

\[
\mathbf{x}^T.
\]

For:

\[
\mathbf{x}
=
\begin{bmatrix}
1\\2\\3
\end{bmatrix},
\]

we have:

\[
\mathbf{x}^T=
\begin{bmatrix}
1&2&3
\end{bmatrix}.
\]

Do not confuse transpose notation with exponentiation.

---

# 48. Dot Product

For vectors:

\[
\mathbf a=
\begin{bmatrix}
a_1\\a_2\\a_3
\end{bmatrix},
\qquad
\mathbf b=
\begin{bmatrix}
b_1\\b_2\\b_3
\end{bmatrix},
\]

their dot product is:

\[
\mathbf a^T\mathbf b
=
a_1b_1+a_2b_2+a_3b_3.
\]

In image processing, a small filter response can be interpreted as a dot product between:

```text
flattened local image patch
```

and:

```text
flattened kernel
```

---

# 49. Matrix Multiplication

For:

\[
A\in\mathbb R^{m\times n}
\]

and:

\[
B\in\mathbb R^{n\times p},
\]

the product:

\[
AB
\]

is:

\[
m\times p.
\]

The inner dimensions must match.

This becomes important in:

- transform matrices;
- geometric transformations;
- neural-network dense layers;
- DCT matrix formulations.

---

# 50. Element-Wise Multiplication

The notation:

\[
A\odot B
\]

can denote element-wise multiplication when defined that way.

For:

\[
A=
\begin{bmatrix}
1&2\\3&4
\end{bmatrix},
\quad
B=
\begin{bmatrix}
5&6\\7&8
\end{bmatrix},
\]

we get:

\[
A\odot B=
\begin{bmatrix}
5&12\\
21&32
\end{bmatrix}.
\]

This differs from matrix multiplication.

---

# 51. Why This Matters in DIP

A filter may use an element-wise multiplication followed by summation:

\[
y=
\sum_{i,j}X_{i,j}K_{i,j}.
\]

Conceptually:

```text
patch
×
kernel element-by-element
→
sum
→
one output
```

This is the mathematical heart of a local filter response.

---

# 52. Linear vs Nonlinear Notation

A linear operation should satisfy:

\[
T(a f+b g)
=
aT(f)+bT(g).
\]

Many classical filters such as convolution with a fixed kernel are linear.

Other operations are not, such as:

- median filtering;
- thresholding;
- max filtering.

Do not infer linearity merely because an operation contains arithmetic.

---

# 53. Operator Notation

Sometimes an operation is represented as:

\[
g=Hf.
\]

Here \(H\) can represent a linear operator.

This notation is useful for:

- restoration;
- system models;
- inverse filtering.

It does not necessarily mean \(H\) is an ordinary scalar.

---

# 54. Probability Notation Preview

A probability may be written:

\[
P(X=x).
\]

This means:

> probability that random variable \(X\) takes value \(x\).

For image histograms:

\[
p(r_k)
=
\frac{n_k}{MN}.
\]

This treats the normalized histogram as an empirical probability distribution.

---

# 55. Expectation Notation Preview

The expectation of a random variable \(X\) can be written:

\[
E[X].
\]

For a discrete variable:

\[
E[X]
=
\sum_x xp(x).
\]

This becomes useful when deriving mean and entropy-related quantities.

---

# 56. Conditional Probability Notation

\[
P(A\mid B)
\]

means:

> probability of \(A\) given \(B\).

The vertical bar is read as “given.”

It appears in:

- probabilistic models;
- classification;
- Bayesian reasoning;
- entropy extensions.

It should not be confused with division.

---

# 57. Gradient Notation Preview

For:

\[
L(w_1,w_2),
\]

the gradient is:

\[
\nabla L
=
\begin{bmatrix}
\frac{\partial L}{\partial w_1}\\
\frac{\partial L}{\partial w_2}
\end{bmatrix}.
\]

This points in the direction of greatest local increase of \(L\).

Gradient-based learning moves parameters in a direction intended to reduce the loss.

---

# 58. Partial Derivative Notation

\[
\frac{\partial L}{\partial w}
\]

means:

> how \(L\) changes with respect to \(w\), treating other variables according to the multivariable context.

CNN training depends heavily on these derivatives.

They are developed formally later in the Math Companion.

---

# 59. Differential / Change Notation

You may encounter:

\[
\Delta x
\]

for a finite change, and:

\[
dx
\]

for an infinitesimal differential in calculus.

In optical flow:

\[
dx,\ dy,\ dt
\]

represent small changes used in the derivation of the constraint equation.

---

# 60. Frequency Notation

Spatial-frequency variables often use:

\[
u,v
\]

while spatial coordinates use:

\[
x,y.
\]

Thus:

```text
x,y → spatial domain
u,v → frequency domain
```

The symbols are conventional, not universal.

What matters is consistent definition.

---

# 61. Image-Processing Notation Map

| Symbol | Typical meaning |
|---|---|
| \(f(x,y)\) | Input image/function |
| \(g(x,y)\) | Output image |
| \(x,y\) | Spatial coordinates |
| \(m,n\) | Discrete spatial indices |
| \(t\) | Time/frame |
| \(c\) | Channel |
| \(T\) | Transformation/threshold, depending on context |
| \(H(u,v)\) | Frequency filter/system response |
| \(F(u,v)\) | Transform-domain representation |
| \(I\) | Image |
| \(\hat I\) | Estimated/reconstructed image |
| \(\tilde I\) | Modified/corrupted image |
| \(K\) or \(h\) | Kernel/filter |
| \(M,N\) | Image dimensions, if defined so |
| \(p_i\) | Probability |
| \(H(X)\) | Entropy |
| \(L\) | Loss or code length, depending on context |
| \(\eta\) | Learning rate or efficiency, depending on context |
| \(\sigma\) | Standard deviation/noise scale |
| \(u,v\) | Frequency coordinates or flow components, depending on context |

**Never rely on a symbol's appearance alone.**

---

# 62. Context Controls Meaning

The symbol \(T\) can mean:

```text
threshold
transformation
transpose
temperature
```

depending on context.

The symbol \(L\) can mean:

```text
loss
number of gray levels
code length
```

depending on context.

Therefore every production chapter should define symbols immediately after an important formula.

---

# 63. Formula Reading Template

Whenever you see:

\[
G=HF,
\]

read it in this order:

### 1. What are the symbols?

\[
G,\ H,\ F
\]

### 2. What domain?

Frequency domain?

### 3. What operation?

Multiplication.

### 4. What is the image meaning?

Filter response is applied to the transform.

### 5. What comes next?

Inverse transform to obtain spatial-domain output.

This five-step habit prevents formula memorization without understanding.

---

# 64. Dimensions Must Always Be Checked

Suppose:

\[
A\in\mathbb R^{3\times4}
\]

and:

\[
B\in\mathbb R^{4\times2}.
\]

Then:

\[
AB\in\mathbb R^{3\times2}.
\]

If instead:

\[
B\in\mathbb R^{5\times2},
\]

then:

\[
AB
\]

is undefined.

In DIP, dimensional checking is a practical debugging method.

---

# 65. Units

Mathematical notation can hide units.

Examples:

- intensity → intensity units / stored numeric range;
- pixels → spatial samples;
- FPS → frames/second;
- bitrate → bits/second;
- bpp → bits/pixel;
- angle → degrees or radians.

Always state the unit when it matters.

---

# 66. Degrees vs Radians

Trigonometric formulas normally use radians.

For example:

\[
\cos(\theta)
\]

in a mathematical DCT expression assumes the angle is interpreted consistently with the formula.

Do not silently plug degree values into a formula expecting radians.

For example:

\[
\pi
\]

radians equals:

\[
180^\circ.
\]

---

# 67. Common Mathematical Operators in DIP

| Operator | Meaning | DIP example |
|---|---|---|
| \(+\) | addition | image sum |
| \(-\) | subtraction | frame difference |
| \(\times\) | multiplication | scaling |
| \(\div\) | division | normalization |
| \(|x|\) | absolute value | absolute difference |
| \(\sum\) | summation | convolution/entropy |
| \(\max\) | maximum | max filter |
| \(\min\) | minimum | min filter |
| \(\lfloor\cdot\rfloor\) | floor | output-size formula |
| \(\lceil\cdot\rceil\) | ceiling | block count |
| \(\log\) | logarithm | entropy/PSNR |
| \(\sqrt{\cdot}\) | square root | magnitude |
| \(\arg\max\) | index of maximum | classification |
| \(\nabla\) | gradient | optical flow/learning |
| \(\partial\) | partial derivative | backpropagation |

---

# 68. Translating a DIP Formula

Consider:

\[
g(x,y)=
\frac{1}{K}
\sum_{(m,n)\in\mathcal N}
f(x+m,y+n).
\]

Translate:

```text
g(x,y)
→ output pixel

1/K
→ normalization

Σ
→ add values

(m,n)∈N
→ use a neighbourhood

f(x+m,y+n)
→ read nearby image samples
```

Plain language:

> The output is the average of values inside a local neighbourhood.

That is the notation-to-concept skill we want.

---

# 69. Mathematical Communication Standard

When writing an equation in your own notes:

```text
Formula
↓
Define symbols
↓
State domain/range
↓
State assumptions
↓
Give one example
```

Example:

\[
L=2^k
\]

where:

- \(k\) = number of bits per intensity sample;
- \(L\) = number of representable intensity levels.

For:

\[
k=8,
\]

\[
L=2^8=256.
\]

---

# 70. Common Notation Traps

### Trap 1 — \(f(x,y)\) is automatically a continuous function.

Not necessarily. It can be used as notation for a discrete image model as well. The coordinate domain must be stated.

### Trap 2 — row = \(x\), column = \(y\) everywhere.

False. Mathematical and programming conventions may differ.

### Trap 3 — \(\log\) always means base 10.

False.

### Trap 4 — superscript always means a power.

False.

### Trap 5 — \(\hat{x}\) always means derivative.

False.

### Trap 6 — \(AB\) and \(A\odot B\) are interchangeable.

False.

### Trap 7 — an index is a physical unit.

False. An index identifies a location/element.

---

# 71. Notation for Common Course Problems

### Thresholding

\[
g(x,y)=
\begin{cases}
1,&f(x,y)\ge T\\
0,&f(x,y)<T
\end{cases}
\]

### Convolution

\[
g[m,n]
=
\sum_k\sum_l
f[k,l]h[m-k,n-l]
\]

### Histogram probability

\[
p(r_k)=\frac{n_k}{MN}
\]

### Entropy

\[
H=-\sum_kp_k\log_2p_k
\]

### MSE

\[
MSE=
\frac1{MN}
\sum_{x,y}
[f(x,y)-g(x,y)]^2
\]

### PSNR

\[
PSNR=
10\log_{10}
\frac{MAX_I^2}{MSE}
\]

### Optical flow

\[
I_xu+I_yv+I_t=0
\]

### CNN softmax

\[
p_i=
\frac{e^{z_i}}
{\sum_je^{z_j}}
\]

These are anchor formulas for later Math chapters.

---

# 72. Worked Mini-Example — Read a Convolution Formula

Given:

\[
g[m,n]
=
\sum_k\sum_l f[k,l]h[m-k,n-l].
\]

Suppose the output location is:

\[
(m,n)=(2,3).
\]

Then:

\[
g[2,3]
=
\sum_k\sum_l
f[k,l]h[2-k,3-l].
\]

Interpretation:

```text
choose output location
→ align kernel according to convolution rule
→ multiply overlapping samples
→ sum
→ produce one output value
```

Do not treat the summation as abstract algebra detached from the image.

---

# 73. Worked Mini-Example — Read an Entropy Formula

\[
H(X)=-\sum_ip_i\log_2p_i.
\]

Translate:

```text
H(X)
→ average information

p_i
→ probability of symbol i

log₂
→ information measured in bits

Σ
→ combine contributions from all symbols

negative sign
→ makes the resulting entropy non-negative
```

This is more important than memorizing the expression alone.

---

# 74. Worked Mini-Example — Read a CNN Formula

\[
z=\sum_iw_ix_i+b.
\]

Translate:

```text
x_i
→ inputs

w_i
→ learned weights

w_i x_i
→ weighted contribution

Σ
→ combine all contributions

b
→ bias

z
→ pre-activation value
```

Then:

\[
a=\operatorname{ReLU}(z)
\]

adds nonlinearity.

This notation is the foundation of CNN mathematics.

---

# 75. Cross-Book Notation Consistency

The Main Book and Math Companion should use the same meaning whenever practical.

For example:

```text
f(x,y) → image
g(x,y) → processed image
F(u,v) → transform-domain representation
H(u,v) → frequency filter
I_t → frame t
T → threshold when explicitly defined
```

When a symbol needs a different meaning, define it locally rather than silently changing conventions.

---

# 76. Exam Lens

### 2-mark

**What is the difference between a scalar and vector?**

A scalar contains one numerical value; a vector contains an ordered collection of components.

### 5-mark

**Explain the notation \(f(x,y)\) for a digital image.**

Mention:

```text
f → image function
x,y → spatial coordinates
f(x,y) → intensity/value
domain → discrete coordinate grid
range → valid intensity/value range
```

### 10-mark

**Explain mathematical notation required for DIP.**

Organize:

```text
scalars
→ variables/parameters
→ coordinates
→ indexing
→ functions
→ matrices/vectors
→ operators
→ summation
→ probability
→ transforms
→ derivatives
```

Use image examples throughout.

---

# 77. Chapter Checkpoint

### Q1

Interpret:

\[
f(12,8)=150.
\]

### Q2

For a zero-based image with 512 columns, what are the valid column indices?

### Q3

What is the difference between:

\[
AB
\]

and:

\[
A\odot B?
\]

### Q4

Interpret:

\[
\arg\max_k p_k.
\]

### Q5

Why must the logarithm base be specified in entropy calculations?

### Q6

What does \(\hat I\) usually indicate?

### Q7

Why can row/column conventions create bugs when implementing \(f(x,y)\)?

---

# 78. One-Page Recall Sheet

```text
DIP MATHEMATICAL LANGUAGE
│
├── Scalar
│   └── one value
│
├── Vector
│   └── ordered values
│
├── Matrix
│   └── 2-D numerical arrangement
│
├── Function
│   └── input → output
│
├── Coordinates
│   └── (x,y)
│
├── Indexing
│   ├── zero-based
│   └── one-based
│
├── Operators
│   ├── Σ
│   ├── max / min
│   ├── |·|
│   ├── ∇
│   └── argmax
│
├── Statistics
│   └── p, E, variance, entropy
│
└── Core discipline
    └── define symbols + dimensions + assumptions
```

---

# 79. Cross-Book Links

| Layer | Connection |
|---|---|
| MAIN | All C01–C31 formulas and notation |
| MATH | Foundation for every mathematical companion chapter |
| LAB | Translate formulas into experiment parameters |
| CODE | Map zero/one-based indexing, tensor shapes and operators into software |
| EXAM | Formula definitions and notation-based questions |
| PRACTICE | Symbol interpretation and expression tracing |
| RESOURCE | Mathematical conventions in textbooks |
| ASSETS | Annotated formula/notation diagrams |
| MASTER | Notation consistency across the complete book |

---

# 80. Final Summary

The central principle is:

\[
\boxed{
\text{Every mathematical symbol should have an image-processing meaning.}
}
\]

For DIP, this means understanding the chain:

```text
symbol
→ quantity
→ image meaning
→ operation
→ result
```

The most important notations to become fluent with are:

\[
f(x,y)
\]

\[
\sum
\]

\[
\mathbf{x}
\]

\[
AB,\quad A\odot B
\]

\[
\hat{x},\quad\tilde{x}
\]

\[
\arg\max
\]

\[
\nabla
\]

and explicit index ranges.

This chapter is intentionally foundational: it makes later work on matrices, convolution, histograms, Fourier analysis, DCT, entropy, CNNs and optical flow substantially easier.
