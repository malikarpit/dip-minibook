#!/usr/bin/env python3
"""
Digital Image Processing (DIP) MiniBook — Part II Master Enrichment & Compilation Suite
Compiles Chapters 06 to 14 (Spatial Filtering, Histograms, Sharpening, Geometry, Fourier Domain, and Restoration)
into comprehensive 2,000+ line production-grade HTML chapters matching the AIML standard.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_DIR = os.path.join(BASE_DIR, 'tools')
sys.path.append(TOOLS_DIR)

from enrich_and_build import build_enriched_chapter
from build_chapter import CHAPTERS_META

# ── CHAPTER 06 ENRICHMENTS: POINT PROCESSING ─────────────────────────
ch06_extra = r"""
# 06.47 Worked Numerical Problem: Piecewise Linear Contrast Stretching
### Problem Statement
An 8-bit grayscale image of size $4 \times 4$ exhibits low contrast with pixel intensities concentrated in the range $[r_{\min}, r_{\max}] = [60, 140]$.
1. Design a piecewise linear contrast stretching transformation function $s = T(r)$ that maps the range $[60, 140]$ linearly to full dynamic range $[0, 255]$ while clipping intensities below 60 to 0 and above 140 to 255.
2. Formulate the mathematical piecewise equation with explicit slopes $\alpha, \beta, \gamma$.
3. Compute the output intensities for the input matrix:
$$A = \begin{bmatrix} 50 & 70 & 80 & 60 \\ 100 & 140 & 130 & 90 \\ 110 & 150 & 65 & 120 \\ 75 & 85 & 135 & 105 \end{bmatrix}$$

### Step-by-Step Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. Threshold Parameters:</strong><br>
  Let $(r_1, s_1) = (60, 0)$ and $(r_2, s_2) = (140, 255)$.</p>

  <p><strong>2. Piecewise Linear Function Formulation:</strong><br>
  $$s = T(r) = \begin{cases}
  \alpha \cdot r = 0 & 0 \le r < 60 \\
  s_1 + \beta (r - r_1) = 0 + \frac{255 - 0}{140 - 60} (r - 60) = 3.1875 (r - 60) & 60 \le r \le 140 \\
  s_2 + \gamma (r - r_2) = 255 & 140 < r \le 255
  \end{cases}$$
  Here, slope in the active region is $\beta = \frac{255}{80} = 3.1875 > 1$, which stretches contrast dynamically.</p>

  <p><strong>3. Matrix Output Calculation:</strong><br>
  - $r = 50 < 60 \implies s = 0$<br>
  - $r = 60 \implies s = 3.1875(60 - 60) = 0$<br>
  - $r = 65 \implies s = \text{round}(3.1875 \times 5) = \text{round}(15.94) = 16$<br>
  - $r = 70 \implies s = \text{round}(3.1875 \times 10) = 32$<br>
  - $r = 75 \implies s = \text{round}(3.1875 \times 15) = 48$<br>
  - $r = 80 \implies s = \text{round}(3.1875 \times 20) = 64$<br>
  - $r = 85 \implies s = \text{round}(3.1875 \times 25) = 80$<br>
  - $r = 90 \implies s = \text{round}(3.1875 \times 30) = 96$<br>
  - $r = 100 \implies s = \text{round}(3.1875 \times 40) = 128$<br>
  - $r = 105 \implies s = \text{round}(3.1875 \times 45) = 143$<br>
  - $r = 110 \implies s = \text{round}(3.1875 \times 50) = 159$<br>
  - $r = 120 \implies s = \text{round}(3.1875 \times 60) = 191$<br>
  - $r = 130 \implies s = \text{round}(3.1875 \times 70) = 223$<br>
  - $r = 135 \implies s = \text{round}(3.1875 \times 75) = 239$<br>
  - $r = 140 \implies s = 3.1875(80) = 255$<br>
  - $r = 150 > 140 \implies s = 255$</p>

  <p><strong>Resulting Contrast-Stretched Matrix:</strong>
  $$A_{out} = \begin{bmatrix} 0 & 32 & 64 & 0 \\ 128 & 255 & 223 & 96 \\ 159 & 255 & 16 & 191 \\ 48 & 80 & 239 & 143 \end{bmatrix}$$
  Notice that subtle variations within $[60, 140]$ now span the full range $0$ to $255$, dramatically enhancing perceptual readability.</p>
</div>

# 06.48 Bit-Plane Slicing Architecture & Steganography Lab Blueprint
### Mathematical Formulation of Bit Planes
Every 8-bit grayscale pixel $f(x,y) \in [0, 255]$ can be uniquely expanded as an 8-term binary polynomial:
$$f(x,y) = a_7(x,y) 2^7 + a_6(x,y) 2^6 + a_5(x,y) 2^5 + a_4(x,y) 2^4 + a_3(x,y) 2^3 + a_2(x,y) 2^2 + a_1(x,y) 2^1 + a_0(x,y) 2^0$$
where $a_k(x,y) \in \{0, 1\}$ represents the $k$-th bit-plane binary slice:
$$a_k(x,y) = \left\lfloor \frac{f(x,y)}{2^k} \right\rfloor \bmod 2$$

<div class="table-wrap">
  <table class="comparison-table">
    <thead>
      <tr>
        <th>Bit Plane</th>
        <th>Bit Weight ($2^k$)</th>
        <th>Visual Energy Contribution</th>
        <th>Structural Significance</th>
        <th>Application & Engineering Role</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Plane 7 (MSB)</strong></td>
        <td>128</td>
        <td>~50.0% of total image variance</td>
        <td>High-contrast macroscopic scene geometry, broad object boundaries.</td>
        <td>Primary visual intelligibility; retained in heavy lossy compression.</td>
      </tr>
      <tr>
        <td><strong>Plane 6</strong></td>
        <td>64</td>
        <td>~25.0% of total image variance</td>
        <td>Major shading gradients and primary surface textures.</td>
        <td>Secondary structural contours.</td>
      </tr>
      <tr>
        <td><strong>Plane 5</strong></td>
        <td>32</td>
        <td>~12.5% of total image variance</td>
        <td>Subtle lighting variations and secondary relief textures.</td>
        <td>Reconstruction threshold for human identification.</td>
      </tr>
      <tr>
        <td><strong>Plane 4</strong></td>
        <td>16</td>
        <td>~6.25% of total image variance</td>
        <td>Fine textural details and faint surface modulations.</td>
        <td>Combined with planes 5-7 restores >93% perceptual quality.</td>
      </tr>
      <tr>
        <td><strong>Plane 3</strong></td>
        <td>8</td>
        <td>~3.12% of total image variance</td>
        <td>Micro-textures and low-amplitude noise.</td>
        <td>Often zeroed out in rate-distortion compression pipelines.</td>
      </tr>
      <tr>
        <td><strong>Plane 2</strong></td>
        <td>4</td>
        <td>~1.56% of total image variance</td>
        <td>High-frequency sensor thermal noise and grain.</td>
        <td>Perceptually indistinguishable to human eye under normal viewing.</td>
      </tr>
      <tr>
        <td><strong>Plane 1</strong></td>
        <td>2</td>
        <td>~0.78% of total image variance</td>
        <td>High-frequency pseudo-random sensor fluctuations.</td>
        <td>Steganographic auxiliary channel.</td>
      </tr>
      <tr>
        <td><strong>Plane 0 (LSB)</strong></td>
        <td>1</td>
        <td>~0.39% of total image variance</td>
        <td>Visually indistinguishable white Gaussian noise.</td>
        <td><strong>LSB Steganography:</strong> Replacement with covert data without visible degradation.</td>
      </tr>
    </tbody>
  </table>
</div>
"""

# ── CHAPTER 07 ENRICHMENTS: HISTOGRAMS ────────────────────────────────
ch07_extra = r"""
# 07.40 Worked Example — 10-Mark University Model Answer: Discrete Histogram Equalization
### Problem Statement
A $64 \times 64$ digital image ($MN = 4096$ pixels) with 3-bit grayscale representation ($L = 8$ gray levels, $r_k \in \{0, 1, 2, 3, 4, 5, 6, 7\}$) has the following gray-level distribution:

<div class="table-wrap">
  <table class="comparison-table">
    <thead>
      <tr>
        <th>Gray Level $r_k$</th>
        <th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Pixel Count $n_k$</strong></td>
        <td>790</td><td>1023</td><td>850</td><td>656</td><td>329</td><td>245</td><td>122</td><td>81</td>
      </tr>
    </tbody>
  </table>
</div>

1. Compute the normalized histogram values $p_r(r_k)$.
2. Calculate the discrete cumulative distribution function (CDF).
3. Compute the equalized output gray levels $s_k = T(r_k) = \text{round}[(L-1) \sum_{j=0}^k p_r(r_j)]$.
4. Determine the transformation mapping and compile the final equalized histogram $n_{s_k}$.

### Step-by-Step Mathematical Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p>Total number of pixels $MN = 64 \times 64 = 4096$. Number of levels $L = 8 \implies L - 1 = 7$.</p>

  <div class="table-wrap">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>$k$</th>
          <th>$r_k$</th>
          <th>$n_k$</th>
          <th>$p_r(r_k) = n_k/4096$</th>
          <th>$CDF_k = \sum_{j=0}^k p_r(r_j)$</th>
          <th>$(L-1) \times CDF_k$</th>
          <th>$s_k = \text{round}(7 \cdot CDF_k)$</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>0</td><td>0</td><td>790</td><td>0.1929</td><td>0.1929</td><td>1.3503</td><td><strong>1</strong></td></tr>
        <tr><td>1</td><td>1</td><td>1023</td><td>0.2498</td><td>0.4427</td><td>3.0989</td><td><strong>3</strong></td></tr>
        <tr><td>2</td><td>2</td><td>850</td><td>0.2075</td><td>0.6502</td><td>4.5514</td><td><strong>5</strong></td></tr>
        <tr><td>3</td><td>3</td><td>656</td><td>0.1602</td><td>0.8104</td><td>5.6728</td><td><strong>6</strong></td></tr>
        <tr><td>4</td><td>4</td><td>329</td><td>0.0803</td><td>0.8907</td><td>6.2349</td><td><strong>6</strong></td></tr>
        <tr><td>5</td><td>5</td><td>245</td><td>0.0598</td><td>0.9505</td><td>6.6535</td><td><strong>7</strong></td></tr>
        <tr><td>6</td><td>6</td><td>122</td><td>0.0298</td><td>0.9803</td><td>6.8621</td><td><strong>7</strong></td></tr>
        <tr><td>7</td><td>7</td><td>81</td><td>0.0198</td><td>1.0000</td><td>7.0000</td><td><strong>7</strong></td></tr>
      </tbody>
    </table>
  </div>

  <p><strong>Gray-Level Mapping Summary:</strong><br>
  - Input level $0 \to$ Output level $1$<br>
  - Input level $1 \to$ Output level $3$<br>
  - Input level $2 \to$ Output level $5$<br>
  - Input levels $3, 4 \to$ Merged into Output level $6$<br>
  - Input levels $5, 6, 7 \to$ Merged into Output level $7$</p>

  <p><strong>Final Equalized Histogram Distribution $n_{s_k}$:</strong></p>
  <div class="table-wrap">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Equalized Level $s_k$</th>
          <th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>Total</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Pixel Count $n_s$</strong></td>
          <td>0</td><td>790</td><td>0</td><td>1023</td><td>0</td><td>850</td><td>985 (656+329)</td><td>448 (245+122+81)</td><td><strong>4096</strong></td>
        </tr>
        <tr>
          <td><strong>$p_s(s_k)$</strong></td>
          <td>0.000</td><td>0.193</td><td>0.000</td><td>0.250</td><td>0.000</td><td>0.208</td><td>0.240</td><td>0.109</td><td><strong>1.000</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  <p><strong>Key Analytical Observations:</strong><br>
  1. The original image was underexposed and low-contrast, with 65% of pixels concentrated in levels 0, 1, and 2.<br>
  2. Equalization stretched the dynamic range across the full scale from 1 to 7.<br>
  3. Because digital intensities are discrete integers, several input levels map to the same output level ($3,4 \to 6$ and $5,6,7 \to 7$), leaving levels 0, 2, and 4 completely empty. This proves that <em>discrete histogram equalization does NOT yield an ideally flat uniform histogram</em>, but rather expands the distance between high-probability bins.</p>
</div>

# 07.41 Mathematical Proof: Continuous Histogram Equalization Yields a Uniform PDF
### The Continuous Transformation Operator
Let the input continuous intensity variable $r$ be defined on $[0, L-1]$ with probability density function $p_r(r) \ge 0$ such that $\int_0^{L-1} p_r(r)dr = 1$.
Consider the monotonic cumulative transformation function:
$$s = T(r) = (L-1) \int_0^r p_r(w) dw$$

### Derivative of the Transformation Function
By the Fundamental Theorem of Calculus (Leibniz rule), the derivative of $s$ with respect to $r$ is:
$$\frac{ds}{dr} = \frac{d}{dr} \left[ (L-1) \int_0^r p_r(w) dw \right] = (L-1) p_r(r)$$
Since $p_r(r) \ge 0$, $\frac{ds}{dr} \ge 0$, confirming that $T(r)$ is monotonically non-decreasing.

### Applying Probability Density Transformation Theory
From random variable transformation theory, the probability density function $p_s(s)$ of the transformed variable $s$ is related to $p_r(r)$ by the Jacobian determinant:
$$p_s(s) = p_r(r) \cdot \left| \frac{dr}{ds} \right| = p_r(r) \cdot \frac{1}{\left| \frac{ds}{dr} \right|}$$
Substituting $\frac{ds}{dr} = (L-1) p_r(r)$:
$$p_s(s) = p_r(r) \cdot \frac{1}{(L-1) p_r(r)} = \frac{1}{L-1} \qquad \text{for } 0 \le s \le L-1$$
This yields an exact constant value independent of the input PDF $p_r(r)$.

$$\therefore p_s(s) = \frac{1}{L-1} \implies \text{Uniform Probability Density Function}$$
This formal mathematical proof confirms that continuous histogram equalization transforms *any* arbitrary input probability density function into a perfectly uniform distribution spanning $[0, L-1]$.
"""

# ── CHAPTER 08 ENRICHMENTS: SPATIAL FILTERING ────────────────────────
ch08_extra = r"""
# 08.68 Worked Example — 10-Mark University Model Answer: 2D Spatial Convolution vs Correlation
### Problem Statement
Given a $5 \times 5$ input image patch $F$ and a $3 \times 3$ filter kernel $W$:
$$F = \begin{bmatrix}
2 & 4 & 6 & 8 & 10 \\
3 & 5 & 7 & 9 & 11 \\
4 & 6 & 8 & 10 & 12 \\
5 & 7 & 9 & 11 & 13 \\
6 & 8 & 10 & 12 & 14
\end{bmatrix}, \qquad
W = \begin{bmatrix}
1 & 0 & -1 \\
2 & 0 & -2 \\
1 & 0 & -1
\end{bmatrix}$$
1. State the mathematical definitions of 2D Spatial Correlation and 2D Spatial Convolution.
2. Demonstrate how kernel rotation accounts for the difference between the two operations.
3. Compute the output value at central pixel $(x, y) = (2, 2)$ (0-indexed, where $F(2,2) = 8$) for both 2D Correlation and 2D Convolution.
4. Evaluate boundary handling effects under Zero Padding vs Replicate Border Padding.

### Step-by-Step Mathematical Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. Mathematical Formulations:</strong><br>
  For an $(2a+1) \times (2b+1)$ kernel $w$ (here $a=b=1$):<br>
  - <strong>2D Spatial Correlation:</strong>
  $$(w \star f)(x, y) = \sum_{s=-a}^a \sum_{t=-b}^b w(s, t) f(x+s, y+t)$$
  - <strong>2D Spatial Convolution:</strong>
  $$(w * f)(x, y) = \sum_{s=-a}^a \sum_{t=-b}^b w(s, t) f(x-s, y-t) = \sum_{s=-a}^a \sum_{t=-b}^b w(-s, -t) f(x+s, y+t)$$</p>

  <p><strong>2. 180° Rotated Kernel for Convolution:</strong><br>
  Rotating $W$ by 180° (reversing rows and columns):
  $$W_{rot} = \begin{bmatrix}
  -1 & 0 & 1 \\
  -2 & 0 & 2 \\
  -1 & 0 & 1
  \end{bmatrix}$$
  Notice that because $W$ is anti-symmetric horizontally ($W(s, t) = -W(s, -t)$), rotating it by 180° flips the sign of all non-zero elements: $W_{rot} = -W$.</p>

  <p><strong>3. Numerical Computation at Center Pixel (2, 2):</strong><br>
  The $3 \times 3$ neighborhood around $F(2, 2)$ is:
  $$N_F = \begin{bmatrix}
  5 & 7 & 9 \\
  6 & 8 & 10 \\
  7 & 9 & 11
  \end{bmatrix}$$

  - <strong>Correlation Computation:</strong>
  $$(W \star F)(2, 2) = (1)(5) + (0)(7) + (-1)(9) + (2)(6) + (0)(8) + (-2)(10) + (1)(7) + (0)(9) + (-1)(11)$$
  $$(W \star F)(2, 2) = 5 - 9 + 12 - 20 + 7 - 11 = -16$$

  - <strong>Convolution Computation:</strong>
  $$(W * F)(2, 2) = (W_{rot} \star F)(2, 2) = (-1)(5) + (0)(7) + (1)(9) + (-2)(6) + (0)(8) + (2)(10) + (-1)(7) + (0)(9) + (1)(11)$$
  $$(W * F)(2, 2) = -5 + 9 - 12 + 20 - 7 + 11 = +16$$
  The result shows $(W * F)(2,2) = -(W \star F)(2,2) = 16$, validating the anti-symmetry theorem.</p>

  <p><strong>4. Boundary Padding Comparison Table:</strong></p>
  <div class="table-wrap">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Padding Strategy</th>
          <th>Top-Left Boundary Trace $(0,0)$</th>
          <th>Edge Artifact Characteristics</th>
          <th>Recommended Domain</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Zero Padding</strong></td>
          <td>Appends zeros outside border. Neighborhood at $(0,0)$ contains false zero gradient.</td>
          <td>Creates dark artificial border frames and strong artificial gradient responses.</td>
          <td>Signal processing where domain outside image is explicitly void.</td>
        </tr>
        <tr>
          <td><strong>Replicate (Clamp)</strong></td>
          <td>Duplicates edge pixels: $F(-1, y) = F(0, y)$. Neighborhood reflects local DC bias.</td>
          <td>Eliminates artificial edge ramps; gradient normal to border evaluates to zero.</td>
          <td>Standard computer vision pipelines (OpenCV <code>BORDER_REPLICATE</code>).</td>
        </tr>
        <tr>
          <td><strong>Symmetric Reflection</strong></td>
          <td>Mirrors pixels across border: $F(-1, y) = F(0, y)$, $F(-2, y) = F(1, y)$.</td>
          <td>Preserves continuity of derivative across image boundary.</td>
          <td>High-fidelity wavelet and multi-resolution decomposition.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

# 08.69 Mathematical Proof: Computational Complexity Reduction via Separable Kernels
### Definition of 2D Separability
A 2D spatial convolution kernel $K$ of size $k \times k$ is defined as **separable** if and only if it can be factored into the outer product of a column vector $\mathbf{v} \in \mathbb{R}^{k \times 1}$ and a row vector $\mathbf{h}^T \in \mathbb{R}^{1 \times k}$:
$$K = \mathbf{v} \cdot \mathbf{h}^T \iff K(x, y) = v(x) \cdot h(y)$$
By the rank theorem of linear algebra, a matrix is separable if and only if its matrix rank equals 1:
$$\text{rank}(K) = 1$$

### Complexity Analysis: 2D Direct vs Separable 1D Cascades
Consider an image of dimensions $M \times N$ filtered with a $k \times k$ kernel.

1. **Direct 2D Non-Separable Convolution:**
   For every pixel $(x, y)$, computing the 2D sum of products requires $k \times k = k^2$ multiplications and $k^2 - 1$ additions.
   $$\text{Total Multiplications} = M \cdot N \cdot k^2$$

2. **Separable 2-Pass Convolution:**
   Applying the associative property of 2D convolution:
   $$g(x, y) = (K * f)(x, y) = (\mathbf{v} * (\mathbf{h}^T * f))(x, y)$$
   - *Pass 1 (Horizontal):* Convolve every row with 1D kernel $\mathbf{h}^T$ of length $k \implies M \cdot N \cdot k$ multiplications.
   - *Pass 2 (Vertical):* Convolve intermediate result with 1D kernel $\mathbf{v}$ of length $k \implies M \cdot N \cdot k$ multiplications.
   $$\text{Total Separable Multiplications} = M \cdot N \cdot k + M \cdot N \cdot k = 2 \cdot M \cdot N \cdot k$$

### Speedup Ratio Formulation
$$\text{Speedup Factor } S = \frac{\text{Direct Ops}}{\text{Separable Ops}} = \frac{M \cdot N \cdot k^2}{2 \cdot M \cdot N \cdot k} = \frac{k}{2}$$

<div class="table-wrap">
  <table class="comparison-table">
    <thead>
      <tr>
        <th>Kernel Size $k \times k$</th>
        <th>Direct Ops / Pixel ($k^2$)</th>
        <th>Separable Ops / Pixel ($2k$)</th>
        <th>Speedup Factor ($k/2$)</th>
        <th>Computational Work Reduction</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>$3 \times 3$</td><td>9</td><td>6</td><td>1.50 $\times$</td><td>33.3% savings</td></tr>
      <tr><td>$5 \times 5$</td><td>25</td><td>10</td><td>2.50 $\times$</td><td>60.0% savings</td></tr>
      <tr><td>$7 \times 7$</td><td>49</td><td>14</td><td>3.50 $\times$</td><td>71.4% savings</td></tr>
      <tr><td>$11 \times 11$</td><td>121</td><td>22</td><td>5.50 $\times$</td><td>81.8% savings</td></tr>
      <tr><td>$31 \times 31$</td><td>961</td><td>62</td><td>15.5 $\times$</td><td>93.5% savings</td></tr>
    </tbody>
  </table>
</div>
This proof demonstrates why 2D Gaussian filters ($G(x,y) = g(x) \cdot g(y)$) are ubiquitously executed as horizontal and vertical 1D convolutions in production image processing engines.
"""

# ── CHAPTER 09 ENRICHMENTS: SMOOTHING & NOISE ────────────────────────
ch09_extra = r"""
# 09.56 Mathematical Derivation: 2D Gaussian Kernel & Parameter $\sigma$
### Continuous 2D Gaussian Distribution
The circularly symmetric continuous 2D Gaussian function centered at the origin is defined as:
$$G(x, y) = \frac{1}{2\pi \sigma^2} e^{-\frac{x^2 + y^2}{2\sigma^2}}$$
where $\sigma$ denotes the standard deviation (spread of the bell curve).

### Mathematical Proof of Separability
$$G(x, y) = \left( \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{x^2}{2\sigma^2}} \right) \cdot \left( \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{y^2}{2\sigma^2}} \right) = g(x) \cdot g(y)$$
This confirms that the 2D Gaussian kernel is mathematically separable into two identical 1D Gaussian operations along the horizontal and vertical axes.

### The $6\sigma + 1$ Filter Window Size Rule
The integral of a Gaussian distribution within $[-3\sigma, +3\sigma]$ contains $99.73\%$ of its total volume under the curve:
$$\int_{-3\sigma}^{3\sigma} g(x) dx \approx 0.9973$$
To prevent sharp boundary truncation that produces high-frequency ringing artifacts, the spatial discrete window size $k \times k$ must span at least $6\sigma$:
$$k \ge 2 \lceil 3\sigma \rceil + 1$$
For example, if $\sigma = 1.0$, $k \ge 2(3) + 1 = 7 \implies 7 \times 7$ window.

### Derivation of the Canonical $3 \times 3$ Integer Gaussian Kernel
For $k = 3$ ($x, y \in \{-1, 0, 1\}$), choose $\sigma \approx 0.84932$ such that the corner values satisfy $G(1,1) / G(0,0) = 0.25$:
- Center $(0, 0): e^0 = 1.0 \to 4$
- Orthogonal neighbors $(\pm 1, 0), (0, \pm 1): e^{-1/(2\sigma^2)} \approx 0.5 \to 2$
- Diagonal corners $(\pm 1, \pm 1): e^{-2/(2\sigma^2)} \approx 0.25 \to 1$

Sum of integer weights $= 4(1) + 4(2) + 1(4) = 16 = 2^4$.
$$K_{Gaussian} = \frac{1}{16} \begin{bmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 1 \end{bmatrix}$$
Because the normalization factor is $16 = 2^4$, convolution can be implemented on embedded hardware using bitwise right-shift `>> 4` without floating-point division.
"""

# ── CHAPTER 10 ENRICHMENTS: SHARPENING & EDGES ───────────────────────
ch10_extra = r"""
# 10.54 Mathematical Derivation: 2D Laplacian Operator & Image Sharpening
### Derivation from Second-Order Finite Differences
The continuous Laplacian of an image function $f(x,y)$ is the divergence of the gradient vector:
$$\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}$$
Using central finite difference approximations for second derivatives:
$$\frac{\partial^2 f}{\partial x^2} \approx f(x+1, y) - 2f(x, y) + f(x-1, y)$$
$$\frac{\partial^2 f}{\partial y^2} \approx f(x, y+1) - 2f(x, y) + f(x, y-1)$$
Summing both orthogonal components yields the 4-neighbor discrete Laplacian:
$$\nabla^2 f(x, y) = f(x+1, y) + f(x-1, y) + f(x, y+1) + f(x, y-1) - 4f(x, y)$$

In convolution matrix notation:
$$\nabla_4^2 = \begin{bmatrix} 0 & 1 & 0 \\ 1 & -4 & 1 \\ 0 & 1 & 0 \end{bmatrix}$$
Extending this derivation to include the 4 diagonal neighbors produces the isotropic 8-neighbor Laplacian:
$$\nabla_8^2 = \begin{bmatrix} 1 & 1 & 1 \\ 1 & -8 & 1 \\ 1 & 1 & 1 \end{bmatrix}$$

### Image Sharpening via Laplacian
Because the Laplacian has a negative center coefficient ($-4$ or $-8$), subtracting the Laplacian from the original image enhances high-frequency edge transitions:
$$g(x, y) = f(x, y) - \nabla^2 f(x, y)$$
Substituting the 4-neighbor kernel:
$$g(x, y) = f(x, y) - [f(x+1,y) + f(x-1,y) + f(x,y+1) + f(x,y-1) - 4f(x,y)]$$
$$g(x, y) = 5f(x, y) - f(x+1,y) - f(x-1,y) - f(x,y+1) - f(x,y-1)$$
This yields the composite sharpening kernel:
$$K_{sharp} = \begin{bmatrix} 0 & -1 & 0 \\ -1 & 5 & -1 \\ 0 & -1 & 0 \end{bmatrix}$$
Notice that the sum of coefficients equals $5 - 4(1) = 1$, which preserves the average DC brightness in uniform regions while boosting edge discontinuities.
"""

# ── CHAPTER 11 ENRICHMENTS: GEOMETRY & INTERPOLATION ─────────────────
ch11_extra = r"""
# 11.58 Worked Example — 10-Mark University Model Answer: Bilinear Interpolation
### Problem Statement
An image scaling algorithm maps an output pixel $(x', y')$ back to a non-integer continuous coordinate $(x, y) = (3.4, 2.7)$ in the source image matrix $F$.
The four surrounding integer grid points and their known pixel intensity values are:
- Top-Left: $F(3, 2) = 100$
- Top-Right: $F(4, 2) = 140$
- Bottom-Left: $F(3, 3) = 110$
- Bottom-Right: $F(4, 3) = 160$

1. Derive the mathematical equation for 2D Bilinear Interpolation.
2. Calculate the fractional coordinate offsets $\Delta x$ and $\Delta y$.
3. Compute the interpolated pixel intensity at $(3.4, 2.7)$ with full step-by-step arithmetic.
4. Compare Bilinear Interpolation with Nearest-Neighbor and Bicubic Interpolation in terms of computational complexity and perceptual sharpness.

### Step-by-Step Mathematical Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. Mathematical Formula:</strong><br>
  Let continuous coordinate $(x, y)$ lie inside unit cell $[x_1, x_2] \times [y_1, y_2]$ where $x_1 = 3, x_2 = 4, y_1 = 2, y_2 = 3$.<br>
  Fractional horizontal offset: $\Delta x = x - x_1 = 3.4 - 3 = 0.4$.<br>
  Fractional vertical offset: $\Delta y = y - y_1 = 2.7 - 2 = 0.7$.</p>

  <p><strong>2. Two-Stage Interpolation Trace:</strong><br>
  - <em>Stage 1: Horizontal Linear Interpolation along row $y_1 = 2$:</em>
  $$f(x, y_1) = (1 - \Delta x) F(x_1, y_1) + \Delta x F(x_2, y_1)$$
  $$f(3.4, 2) = (1 - 0.4)(100) + (0.4)(140) = 0.6(100) + 0.4(140) = 60 + 56 = 116$$

  - <em>Stage 2: Horizontal Linear Interpolation along row $y_2 = 3$:</em>
  $$f(x, y_2) = (1 - \Delta x) F(x_1, y_2) + \Delta x F(x_2, y_2)$$
  $$f(3.4, 3) = (1 - 0.4)(110) + (0.4)(160) = 0.6(110) + 0.4(160) = 66 + 64 = 130$$

  - <em>Stage 3: Vertical Linear Interpolation between the two intermediate values:</em>
  $$f(x, y) = (1 - \Delta y) f(x, y_1) + \Delta y f(x, y_2)$$
  $$f(3.4, 2.7) = (1 - 0.7)(116) + (0.7)(130) = 0.3(116) + 0.7(130) = 34.8 + 91.0 = 125.8$$
  Rounding to the nearest 8-bit integer:
  $$f(3.4, 2.7) = 126$$</p>

  <p><strong>3. Direct 4-Point Bilinear Weighted Equation:</strong><br>
  $$f(x, y) = (1-\Delta x)(1-\Delta y)F(3,2) + \Delta x(1-\Delta y)F(4,2) + (1-\Delta x)\Delta y F(3,3) + \Delta x \Delta y F(4,3)$$
  $$f(3.4, 2.7) = (0.6)(0.3)(100) + (0.4)(0.3)(140) + (0.6)(0.7)(110) + (0.4)(0.7)(160)$$
  $$f(3.4, 2.7) = 0.18(100) + 0.12(140) + 0.42(110) + 0.28(160)$$
  $$f(3.4, 2.7) = 18.0 + 16.8 + 46.2 + 44.8 = 125.8 \to 126$$</p>

  <p><strong>4. Algorithmic Comparison:</strong></p>
  <div class="table-wrap">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Method</th>
          <th>Support Kernel</th>
          <th>Ops / Pixel</th>
          <th>Visual Artifacts</th>
          <th>Typical Use Case</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Nearest Neighbor</strong></td>
          <td>$1 \times 1$ (Closest point)</td>
          <td>0 math ops (Round index)</td>
          <td>Severe blockiness, jagged staircase pixelation edges.</td>
          <td>Real-time gaming, segmentation mask rescaling.</td>
        </tr>
        <tr>
          <td><strong>Bilinear</strong></td>
          <td>$2 \times 2$ (4 neighbors)</td>
          <td>3 linear interpolations (8 mult, 6 add)</td>
          <td>Smooth transitions; mild high-frequency blurring.</td>
          <td>Real-time video scaling, mobile screen rendering.</td>
        </tr>
        <tr>
          <td><strong>Bicubic</strong></td>
          <td>$4 \times 4$ (16 neighbors)</td>
          <td>16 cubic polynomial weights</td>
          <td>Preserves edge sharpness and fine textures with minimal ringing.</td>
          <td>Photoshop, print publication, satellite imagery.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

# ── CHAPTER 12 ENRICHMENTS: FOURIER TRANSFORM ────────────────────────
ch12_extra = r"""
# 12.70 Mathematical Proof: Centering the 2D Discrete Fourier Spectrum
### The Spectrum Centering Theorem
In the standard 2D DFT formulation, the DC frequency component $F(0, 0)$ is situated at the top-left corner $(0, 0)$ of the $M \times N$ discrete grid.
To display the spectrum with zero frequency shifted to the optical center $(M/2, N/2)$, the input image must be multiplied spatially by $(-1)^{x+y}$ before computing the DFT:
$$\mathcal{F}\left\{ f(x, y) \cdot (-1)^{x+y} \right\} = F\left(u - \frac{M}{2}, v - \frac{N}{2}\right)$$

### Formal Mathematical Proof
Recall Euler's identity:
$$e^{j\pi} = \cos(\pi) + j\sin(\pi) = -1$$
Therefore:
$$(-1)^{x+y} = (-1)^x (-1)^y = (e^{j\pi})^x (e^{j\pi})^y = e^{j\pi x} e^{j\pi y} = e^{j 2\pi \left( \frac{x}{2} + \frac{y}{2} \right)}$$
Multiplying numerator and denominator by $M$ and $N$ respectively:
$$(-1)^{x+y} = e^{j 2\pi \left( \frac{x \cdot (M/2)}{M} + \frac{y \cdot (N/2)}{N} \right)}$$

Now evaluate the 2D DFT of the modified image $g(x, y) = f(x, y) (-1)^{x+y}$:
$$G(u, v) = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} g(x, y) e^{-j 2\pi \left( \frac{ux}{M} + \frac{vy}{N} \right)}$$
Substituting $g(x, y) = f(x, y) e^{j 2\pi \left( \frac{x(M/2)}{M} + \frac{y(N/2)}{N} \right)}$:
$$G(u, v) = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x, y) e^{-j 2\pi \left( \frac{ux}{M} + \frac{vy}{N} \right)} e^{j 2\pi \left( \frac{(M/2)x}{M} + \frac{(N/2)y}{N} \right)}$$
Combining exponential exponents:
$$G(u, v) = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x, y) e^{-j 2\pi \left( \frac{(u - M/2)x}{M} + \frac{(v - N/2)y}{N} \right)}$$
By definition of the 2D DFT:
$$G(u, v) = F\left(u - \frac{M}{2}, v - \frac{N}{2}\right)$$
This completes the proof. Centering places the dominant low-frequency energy in the center of the visual display, surrounded symmetrically by radial high-frequency spectral components.
"""

# ── CHAPTER 13 ENRICHMENTS: FREQUENCY FILTERING ──────────────────────
ch13_extra = r"""
# 13.70 Comparative Analysis: Ideal, Butterworth, and Gaussian Lowpass Filters
### Mathematical Transfer Functions
Let $D(u, v) = \sqrt{(u - P/2)^2 + (v - Q/2)^2}$ represent the Euclidean distance from the centered frequency origin.

1. **Ideal Lowpass Filter (ILPF):**
   $$H(u, v) = \begin{cases} 1 & \text{if } D(u, v) \le D_0 \\ 0 & \text{if } D(u, v) > D_0 \end{cases}$$

2. **Butterworth Lowpass Filter (BLPF) of order $n$:**
   $$H(u, v) = \frac{1}{1 + \left[ \frac{D(u, v)}{D_0} \right]^{2n}}$$

3. **Gaussian Lowpass Filter (GLPF):**
   $$H(u, v) = e^{-\frac{D^2(u, v)}{2D_0^2}}$$

<div class="table-wrap">
  <table class="comparison-table">
    <thead>
      <tr>
        <th>Filter Type</th>
        <th>Cutoff Transition Profile</th>
        <th>Spatial Domain Impulse Response $h(x, y)$</th>
        <th>Ringing Artifacts (Gibbs Phenomenon)</th>
        <th>Optimal Engineering Application</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Ideal (ILPF)</strong></td>
        <td>Infinitely sharp step discontinuity at $D_0$.</td>
        <td>2D Sinc function $\frac{J_1(2\pi D_0 r)}{\pi r}$ with infinite periodic side lobes.</td>
        <td><strong>Severe:</strong> Concentric ripple waves around all prominent high-contrast edges.</td>
        <td>Theoretical benchmarking; strictly avoided in practical vision systems.</td>
      </tr>
      <tr>
        <td><strong>Butterworth (BLPF)</strong></td>
        <td>Smooth transition controlled by filter order $n$. Cutoff at $H(D_0) = 0.5$.</td>
        <td>Damped oscillations. At $n=1$, zero ringing; at $n \ge 3$, ringing becomes noticeable.</td>
        <td><strong>Controllable:</strong> Minimal at $n=2$ (the standard compromise order).</td>
        <td>High-grade contrast filtering where controlled high-frequency attenuation is required.</td>
      </tr>
      <tr>
        <td><strong>Gaussian (GLPF)</strong></td>
        <td>Infinitely smooth bell curve transition. Cutoff at $H(D_0) = e^{-0.5} \approx 0.607$.</td>
        <td>Exact 2D Gaussian function (Fourier transform of Gaussian is another Gaussian).</td>
        <td><strong>Completely Ringing-Free:</strong> Zero side lobes in spatial impulse response.</td>
        <td>Medical imaging, machine learning preprocessing, and edge-preserving scale space.</td>
      </tr>
    </tbody>
  </table>
</div>
"""

# ── CHAPTER 14 ENRICHMENTS: RESTORATION & DEBLURRING ─────────────────
ch14_extra = r"""
# 14.57 Mathematical Derivation: Inverse Filtering Noise Catastrophe
### Spatial and Frequency Domain Degradation Model
The forward image degradation process is mathematically modeled as:
$$g(x, y) = f(x, y) * h(x, y) + \eta(x, y)$$
where $f(x,y)$ is the original pristine scene, $h(x,y)$ is the blur Point Spread Function (PSF), and $\eta(x,y)$ is additive noise.
Taking the 2D Discrete Fourier Transform:
$$G(u, v) = F(u, v) \cdot H(u, v) + N(u, v)$$

### Direct Inverse Filtering Formulation
Direct inverse filtering attempts to recover $F(u,v)$ by dividing $G(u,v)$ by the optical transfer function $H(u,v)$:
$$\hat{F}(u, v) = \frac{G(u, v)}{H(u, v)} = \frac{F(u, v) H(u, v) + N(u, v)}{H(u, v)}$$
$$\hat{F}(u, v) = F(u, v) + \frac{N(u, v)}{H(u, v)}$$

### The Noise Catastrophe Proof
Optical degradation transfer functions $H(u, v)$ (such as atmospheric turbulence $e^{-k(u^2+v^2)^{5/6}}$ or motion blur $\frac{\sin(\pi u a)}{\pi u a}$) act as lowpass filters:
$$\lim_{D(u,v) \to \infty} H(u, v) \to 0$$
However, additive sensor noise $N(u,v)$ typically exhibits broad high-frequency spectrum (white or thermal noise):
$$|N(u, v)| > 0 \qquad \forall (u, v)$$
As frequency distance increases:
$$\lim_{H(u,v) \to 0} \left| \frac{N(u, v)}{H(u, v)} \right| \to \infty$$
Even if the noise amplitude $N(u,v)$ is minuscule ($10^{-5}$), dividing by a vanishing transfer function $H(u,v) \approx 10^{-6}$ amplifies noise by $10^6$, completely dominating the true signal $F(u,v)$ and rendering the restored image a chaotic pattern of high-frequency static.

# 14.58 Worked Example — 10-Mark University Model Answer: Wiener (MMSE) Filtering
### Problem Statement
1. Derive the Wiener Filter transfer function $W(u, v)$ that minimizes the Mean Square Error (MSE):
$$e^2 = \mathbb{E}\left\{ |f(x, y) - \hat{f}(x, y)|^2 \right\}$$
2. Express the Wiener restoration formula using the constant ratio approximation $K = S_\eta(u,v) / S_f(u,v)$.
3. Analyze the asymptotic behavior of the Wiener filter when the Signal-to-Noise Ratio (SNR) approaches infinity ($K \to 0$) versus when SNR approaches zero ($K \to \infty$).

### Step-by-Step Mathematical Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. Wiener Filter Transfer Function Derivation:</strong><br>
  Under the assumption that noise $\eta$ and image $f$ are uncorrelated zero-mean stationary random fields, the optimal linear filter that minimizes MSE in the frequency domain is:
  $$\hat{F}(u, v) = \left[ \frac{H^*(u, v)}{|H(u, v)|^2 + \frac{S_\eta(u, v)}{S_f(u, v)}} \right] G(u, v)$$
  where $H^*(u,v)$ is the complex conjugate of $H(u,v)$, $S_\eta(u,v) = |N(u,v)|^2$ is the noise power spectral density, and $S_f(u,v) = |F(u,v)|^2$ is the pristine signal power spectral density.</p>

  <p>Multiplying and dividing the bracketed term by $H(u,v)$:
  $$\hat{F}(u, v) = \left[ \frac{1}{H(u, v)} \frac{|H(u, v)|^2}{|H(u, v)|^2 + \frac{S_\eta(u, v)}{S_f(u, v)}} \right] G(u, v)$$</p>

  <p><strong>2. Constant Ratio Approximation Formulation:</strong><br>
  In practice, the true power spectrum of the original pristine image $S_f(u,v)$ is unknown. We approximate the noise-to-signal power ratio by an empirical tuning constant $K$:
  $$K = \frac{S_\eta(u, v)}{S_f(u, v)} \approx \text{const}$$
  $$\hat{F}(u, v) = \left[ \frac{1}{H(u, v)} \frac{|H(u, v)|^2}{|H(u, v)|^2 + K} \right] G(u, v)$$</p>

  <p><strong>3. Asymptotic Boundary Analysis:</strong><br>
  - <em>Case 1: Noise-Free Condition (High SNR, $K \to 0$):</em>
  $$\lim_{K \to 0} \hat{F}(u, v) = \left[ \frac{1}{H(u, v)} \frac{|H(u, v)|^2}{|H(u, v)|^2 + 0} \right] G(u, v) = \frac{G(u, v)}{H(u, v)}$$
  The Wiener filter gracefully simplifies to the direct <strong>Inverse Filter</strong> when no noise is present.</p>

  <p>- <em>Case 2: Pure Noise Condition ($|H(u,v)|^2 \ll K$ at high frequencies):</em>
  $$\lim_{|H(u,v)| \to 0} \hat{F}(u, v) \approx \left[ \frac{1}{H(u, v)} \frac{0}{K} \right] G(u, v) = 0$$
  When $|H(u,v)|^2$ drops below noise floor threshold $K$, the filter automatically attenuates the output to zero instead of blowing up to infinity. This proves how the Wiener filter completely eradicates the catastrophic noise explosion of inverse filtering.</p>
</div>
"""

PART2_ENRICHMENTS = {
    6: ch06_extra,
    7: ch07_extra,
    8: ch08_extra,
    9: ch09_extra,
    10: ch10_extra,
    11: ch11_extra,
    12: ch12_extra,
    13: ch13_extra,
    14: ch14_extra
}

def compile_part2():
    print("=" * 60)
    print("COMPILING ENRICHED DIP PART II CHAPTERS (C06 - C14)")
    print("=" * 60)

    part2_metas = [m for m in CHAPTERS_META if 6 <= m['chapter_num'] <= 14]
    
    for meta in part2_metas:
        c_num = meta['chapter_num']
        extra = PART2_ENRICHMENTS.get(c_num, None)
        print(f"\n--- Compiling Chapter {c_num:02d}: {meta['title']} ---")
        build_enriched_chapter(meta, extra_sections_md=extra)

    print("\n" + "=" * 60)
    print("ALL 9 PART II CHAPTERS SUCCESSFULLY COMPILED!")
    print("=" * 60)

if __name__ == '__main__':
    compile_part2()
