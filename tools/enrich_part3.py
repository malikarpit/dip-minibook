#!/usr/bin/env python3
"""
Digital Image Processing (DIP) MiniBook — Part III Master Enrichment & Compilation Suite
Compiles Chapters 15 to 20 (Segmentation, Thresholding, Morphology, Descriptors, and SIFT/SURF/ORB/HOG)
into comprehensive 2,200+ line production-grade HTML chapters matching the AIML standard.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_DIR = os.path.join(BASE_DIR, 'tools')
sys.path.append(TOOLS_DIR)

from enrich_and_build import build_enriched_chapter
from build_chapter import CHAPTERS_META

# ── CHAPTER 15 ENRICHMENTS: SEGMENTATION & HOUGH TRANSFORM ───────────
ch15_extra = r"""
# 15.59 Worked Example — 10-Mark University Model Answer: Hough Transform for Collinear Detection
### Problem Statement
In an automated industrial inspection system, three edge pixels are detected at Cartesian coordinates:
$$P_1 = (1, 1), \qquad P_2 = (2, 2), \qquad P_3 = (3, 3)$$
A fourth noisy edge pixel is detected at $P_4 = (1, 3)$.
1. Explain the limitation of the Cartesian slope-intercept form $y = mx + c$ in Hough parameter space and formulate the normal parameterization equation $\rho = x \cos\theta + y \sin\theta$.
2. Compute the parametric values $\rho$ for the candidate quantization angles $\theta \in \{-45^\circ, 0^\circ, 45^\circ, 90^\circ, 135^\circ\}$ for all four points.
3. Construct the discretized Hough accumulator array $A(\rho, \theta)$ and identify the collinear line equation from the peak accumulator cell.

### Step-by-Step Mathematical Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. Limitation of Slope-Intercept Form:</strong><br>
  In $y = mx + c$, vertical lines parallel to the y-axis have infinite slope ($m \to \infty$), which requires an unbounded accumulator array.
  Duda and Hart resolved this using the normal form:
  $$\rho = x \cos\theta + y \sin\theta$$
  where $\rho$ is the perpendicular distance from the coordinate origin to the line, and $\theta \in [-90^\circ, +90^\circ]$ or $[0^\circ, 180^\circ]$ is the angle of the normal vector with respect to the horizontal x-axis.</p>

  <p><strong>2. Parametric Calculation Table:</strong><br>
  Evaluate $\rho(\theta) = x \cos\theta + y \sin\theta$ for each point:<br>
  - $\cos(-45^\circ) = \frac{\sqrt{2}}{2} \approx 0.707, \quad \sin(-45^\circ) = -\frac{\sqrt{2}}{2} \approx -0.707$<br>
  - $\cos(0^\circ) = 1.0, \quad \sin(0^\circ) = 0.0$<br>
  - $\cos(45^\circ) \approx 0.707, \quad \sin(45^\circ) \approx 0.707$<br>
  - $\cos(90^\circ) = 0.0, \quad \sin(90^\circ) = 1.0$<br>
  - $\cos(135^\circ) \approx -0.707, \quad \sin(135^\circ) \approx 0.707$</p>

  <div class="table-wrap">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Point $(x, y)$</th>
          <th>$\rho(-45^\circ)$</th>
          <th>$\rho(0^\circ)$</th>
          <th>$\rho(45^\circ)$</th>
          <th>$\rho(90^\circ)$</th>
          <th>$\rho(135^\circ)$</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>$P_1(1, 1)$</strong></td>
          <td>$0.707 - 0.707 = \mathbf{0.00}$</td>
          <td>$1(1) + 1(0) = 1.00$</td>
          <td>$0.707 + 0.707 = 1.41$</td>
          <td>$1(0) + 1(1) = 1.00$</td>
          <td>$-0.707 + 0.707 = \mathbf{0.00}$</td>
        </tr>
        <tr>
          <td><strong>$P_2(2, 2)$</strong></td>
          <td>$1.414 - 1.414 = \mathbf{0.00}$</td>
          <td>$2(1) + 2(0) = 2.00$</td>
          <td>$1.414 + 1.414 = 2.83$</td>
          <td>$2(0) + 2(1) = 2.00$</td>
          <td>$-1.414 + 1.414 = \mathbf{0.00}$</td>
        </tr>
        <tr>
          <td><strong>$P_3(3, 3)$</strong></td>
          <td>$2.121 - 2.121 = \mathbf{0.00}$</td>
          <td>$3(1) + 3(0) = 3.00$</td>
          <td>$2.121 + 2.121 = 4.24$</td>
          <td>$3(0) + 3(1) = 3.00$</td>
          <td>$-2.121 + 2.121 = \mathbf{0.00}$</td>
        </tr>
        <tr>
          <td><strong>$P_4(1, 3)$ (Noise)</strong></td>
          <td>$0.707 - 2.121 = -1.41$</td>
          <td>$1(1) + 3(0) = 1.00$</td>
          <td>$0.707 + 2.121 = 2.83$</td>
          <td>$1(0) + 3(1) = 3.00$</td>
          <td>$-0.707 + 2.121 = 1.41$</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p><strong>3. Accumulator Peak Analysis:</strong><br>
  Examining the column $\theta = -45^\circ$ (or equivalently $\theta = 135^\circ$):<br>
  - All three points $P_1, P_2, P_3$ evaluate to $\rho = 0.00$.<br>
  - Therefore, the accumulator cell $A(\rho=0, \theta=-45^\circ)$ accumulates <strong>3 votes</strong>.<br>
  - In contrast, $P_4(1, 3)$ produces $\rho = -1.41$ at this angle, voting elsewhere.<br>
  The peak detects the dominant line equation:
  $$x \cos(-45^\circ) + y \sin(-45^\circ) = 0 \iff 0.707x - 0.707y = 0 \iff y = x$$
  This demonstrates the noise robustness of the Hough Transform: isolated noise points cannot corrupt the detection of the dominant collinear structure.</p>
</div>

# 15.60 Comparative Edge Linking Architectural Matrix
<div class="table-wrap">
  <table class="comparison-table">
    <thead>
      <tr>
        <th>Edge Linking Paradigm</th>
        <th>Mathematical Formulation</th>
        <th>Computational Complexity</th>
        <th>Noise Tolerance</th>
        <th>Typical Vision Domain</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Local Gradient Matching</strong></td>
        <td>$|M(x,y) - M(x_0,y_0)| \le E$ and $|\alpha(x,y) - \alpha(x_0,y_0)| \le A$</td>
        <td>$O(M \cdot N)$ (Fast $3 \times 3$ window trace)</td>
        <td>Low (Gaps occur wherever noise drops gradient magnitude).</td>
        <td>Real-time boundary tracking in high-contrast video.</td>
      </tr>
      <tr>
        <td><strong>Global Hough Transform</strong></td>
        <td>$\rho = x\cos\theta + y\sin\theta$, Peak voting in accumulator $A(\rho, \theta)$</td>
        <td>$O(N_{edges} \cdot N_\theta)$ (Parameter space binning)</td>
        <td><strong>Extremely High:</strong> Bridges fragmented occluded edges globally.</td>
        <td>Lane detection in autonomous vehicles, circular pupil tracking.</td>
      </tr>
      <tr>
        <td><strong>Graph-Theoretic Search (A*)</strong></td>
        <td>$f(n) = g(n) + h(n)$, edge transition cost $c(p, q) = M_{\max} - M(q)$</td>
        <td>$O(V \log V + E)$ (Dijkstra / A* heuristic search)</td>
        <td>Moderate to High (Finds globally optimal minimum-cost path).</td>
        <td>Medical contour delineation (coronary artery tracking in angiography).</td>
      </tr>
    </tbody>
  </table>
</div>
"""

# ── CHAPTER 16 ENRICHMENTS: THRESHOLDING & OTSU ──────────────────────
ch16_extra = r"""
# 16.55 Worked Example — 10-Mark University Model Answer: Otsu's Optimum Global Thresholding
### Problem Statement
An 8-gray-level digital image ($L = 8$, gray levels $i \in \{0, 1, 2, 3, 4, 5, 6, 7\}$) of size $1000$ pixels has the following intensity histogram:

<div class="table-wrap">
  <table class="comparison-table">
    <thead>
      <tr>
        <th>Gray Level $i$</th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Count $n_i$</strong></td><td>100</td><td>200</td><td>300</td><td>150</td><td>50</td><td>100</td><td>50</td><td>50</td>
      </tr>
    </tbody>
  </table>
</div>

1. State the objective function of Otsu's thresholding method.
2. Calculate the global mean level $\mu_G$ of the image.
3. Compute the cumulative probabilities $\omega_1(k)$, cumulative means $\mu(k)$, and the between-class variance $\sigma_B^2(k)$ for candidate thresholds $k \in \{1, 2, 3, 4\}$.
4. Identify the optimum threshold $k^*$ that maximizes the between-class variance.

### Step-by-Step Mathematical Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. Otsu's Objective Function:</strong><br>
  Otsu's algorithm finds the threshold $k^*$ that maximizes the between-class variance $\sigma_B^2(k)$:
  $$\sigma_B^2(k) = \frac{[\mu_G \omega_1(k) - \mu(k)]^2}{\omega_1(k)(1 - \omega_1(k))}$$
  where $\omega_1(k) = \sum_{i=0}^k p_i$ is the background class probability, $\mu(k) = \sum_{i=0}^k i p_i$ is the cumulative mean, and $\mu_G = \sum_{i=0}^{L-1} i p_i$ is the global mean.</p>

  <p><strong>2. Global Mean $\mu_G$ Calculation:</strong><br>
  Total pixels $N = 1000$. Normalized histogram probabilities $p_i = n_i / 1000$:<br>
  $p_0 = 0.10, \ p_1 = 0.20, \ p_2 = 0.30, \ p_3 = 0.15, \ p_4 = 0.05, \ p_5 = 0.10, \ p_6 = 0.05, \ p_7 = 0.05$.<br>
  $$\mu_G = \sum_{i=0}^7 i p_i = 0(0.10) + 1(0.20) + 2(0.30) + 3(0.15) + 4(0.05) + 5(0.10) + 6(0.05) + 7(0.05)$$
  $$\mu_G = 0.00 + 0.20 + 0.60 + 0.45 + 0.20 + 0.50 + 0.30 + 0.35 = \mathbf{2.60}$$</p>

  <p><strong>3. Step-by-Step Evaluation for Candidate Thresholds:</strong></p>
  <div class="table-wrap">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Threshold $k$</th>
          <th>$\omega_1(k) = \sum_{i=0}^k p_i$</th>
          <th>$1 - \omega_1(k)$</th>
          <th>$\mu(k) = \sum_{i=0}^k i p_i$</th>
          <th>$\mu_G \omega_1(k) - \mu(k)$</th>
          <th>Numerator $[\dots]^2$</th>
          <th>Denominator $\omega_1(1-\omega_1)$</th>
          <th>$\sigma_B^2(k)$</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>$k = 1$</strong></td>
          <td>$0.10 + 0.20 = 0.30$</td>
          <td>$0.70$</td>
          <td>$0(0.10) + 1(0.20) = 0.20$</td>
          <td>$2.60(0.30) - 0.20 = 0.58$</td>
          <td>$0.58^2 = 0.3364$</td>
          <td>$0.30 \times 0.70 = 0.2100$</td>
          <td><strong>1.6019</strong></td>
        </tr>
        <tr>
          <td><strong>$k = 2$</strong></td>
          <td>$0.30 + 0.30 = 0.60$</td>
          <td>$0.40$</td>
          <td>$0.20 + 2(0.30) = 0.80$</td>
          <td>$2.60(0.60) - 0.80 = 0.76$</td>
          <td>$0.76^2 = 0.5776$</td>
          <td>$0.60 \times 0.40 = 0.2400$</td>
          <td><strong>2.4067</strong></td>
        </tr>
        <tr>
          <td><strong>$k = 3$</strong></td>
          <td>$0.60 + 0.15 = 0.75$</td>
          <td>$0.25$</td>
          <td>$0.80 + 3(0.15) = 1.25$</td>
          <td>$2.60(0.75) - 1.25 = 0.70$</td>
          <td>$0.70^2 = 0.4900$</td>
          <td>$0.75 \times 0.25 = 0.1875$</td>
          <td><strong>2.6133</strong></td>
        </tr>
        <tr>
          <td><strong>$k = 4$</strong></td>
          <td>$0.75 + 0.05 = 0.80$</td>
          <td>$0.20$</td>
          <td>$1.25 + 4(0.05) = 1.45$</td>
          <td>$2.60(0.80) - 1.45 = 0.63$</td>
          <td>$0.63^2 = 0.3969$</td>
          <td>$0.80 \times 0.20 = 0.1600$</td>
          <td><strong>2.4806</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  <p><strong>4. Optimum Threshold Determination:</strong><br>
  Comparing the calculated between-class variances:<br>
  - $\sigma_B^2(1) = 1.6019$<br>
  - $\sigma_B^2(2) = 2.4067$<br>
  - $\sigma_B^2(3) = \mathbf{2.6133}$ (Maximum Peak)<br>
  - $\sigma_B^2(4) = 2.4806$<br>
  $$\therefore \text{Optimum Otsu Threshold } k^* = 3$$
  Pixels with intensities $0, 1, 2, 3$ are assigned to the background class ($C_1$), and pixels with intensities $4, 5, 6, 7$ are assigned to the foreground class ($C_2$).</p>
</div>
"""

# ── CHAPTER 17 ENRICHMENTS: REGION SEGMENTATION ──────────────────────
ch17_extra = r"""
# 17.61 Axiomatic Mathematical Criteria for Image Segmentation
Let $R$ represent the entire image spatial domain. Image segmentation partitions $R$ into $n$ connected subregions $R_1, R_2, \dots, R_n$ such that:
1. **Completeness:** Every pixel belongs to a region:
   $$\bigcup_{i=1}^n R_i = R$$
2. **Connectivity:** Points in region $R_i$ form a topologically connected set:
   $$R_i \text{ is a connected region for } i = 1, 2, \dots, n$$
3. **Disjointness:** Regions are mutually exclusive with zero spatial overlap:
   $$R_i \cap R_j = \emptyset \quad \forall i \ne j$$
4. **Homogeneity:** A logical predicate $P(R_i)$ evaluates to TRUE over every individual region:
   $$P(R_i) = \text{TRUE} \quad \text{for } i = 1, 2, \dots, n$$
5. **Maximality (Distinguishability):** Adjacent regions cannot be merged without violating homogeneity:
   $$P(R_i \cup R_j) = \text{FALSE} \quad \text{for any adjacent regions } R_i \text{ and } R_j$$

# 17.62 Worked Example: Quadtree Split-and-Merge Algorithm Trace
### Quadtree Hierarchical Representation
In split-and-merge segmentation, the image is modeled as a rooted 4-ary tree (Quadtree). If a block $R_k$ violates homogeneity predicate $P(R_k)$, it is split into 4 equal quadrants: $R_{k1}, R_{k2}, R_{k3}, R_{k4}$.
Conversely, if two or more adjacent quadrants satisfy $P(R_a \cup R_b) = \text{TRUE}$, they are merged into a single region.

<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Algorithmic Quadtree Trace</span>
    <span class="tag-badge tag-algo">SPLIT-AND-MERGE DECISION PIPELINE</span>
  </div>
  <p><strong>Predicate Definition:</strong> $P(R) = \text{TRUE} \iff |z_{\max} - z_{\min}| \le 3$, where $z$ denotes pixel intensity.</p>
  <p>Consider an $4 \times 4$ image block:
  $$R = \begin{bmatrix}
  10 & 11 & 50 & 52 \\
  10 & 12 & 51 & 53 \\
  11 & 10 & 12 & 10 \\
  10 & 11 & 11 & 12
  \end{bmatrix}$$</p>

  <p><strong>Step 1: Test Root Block $R$:</strong><br>
  $z_{\max} = 53, \ z_{\min} = 10 \implies |53 - 10| = 43 > 3$.<br>
  $P(R) = \text{FALSE} \implies$ Split root into 4 quadrants ($2 \times 2$ blocks):<br>
  - $R_1 \text{ (Top-Left)} = \begin{bmatrix} 10 & 11 \\ 10 & 12 \end{bmatrix} \implies |12 - 10| = 2 \le 3 \implies P(R_1) = \mathbf{TRUE}$ (Stop splitting).<br>
  - $R_2 \text{ (Top-Right)} = \begin{bmatrix} 50 & 52 \\ 51 & 53 \end{bmatrix} \implies |53 - 50| = 3 \le 3 \implies P(R_2) = \mathbf{TRUE}$ (Stop splitting).<br>
  - $R_3 \text{ (Bottom-Left)} = \begin{bmatrix} 11 & 10 \\ 10 & 11 \end{bmatrix} \implies |11 - 10| = 1 \le 3 \implies P(R_3) = \mathbf{TRUE}$ (Stop splitting).<br>
  - $R_4 \text{ (Bottom-Right)} = \begin{bmatrix} 12 & 10 \\ 11 & 12 \end{bmatrix} \implies |12 - 10| = 2 \le 3 \implies P(R_4) = \mathbf{TRUE}$ (Stop splitting).</p>

  <p><strong>Step 2: Merge Adjacency Test:</strong><br>
  - Test $R_1$ and $R_3$: Both contain values around 10-12. Range of $R_1 \cup R_3$ is $[10, 12] \implies |12 - 10| = 2 \le 3 \implies P(R_1 \cup R_3) = \mathbf{TRUE} \implies$ Merge $R_1$ and $R_3$ into a single $4 \times 2$ region.<br>
  - Test $(R_1 \cup R_3)$ and $R_4$: Combined range is $[10, 12] \implies |12 - 10| = 2 \le 3 \implies$ Merge into a 12-pixel L-shaped region.<br>
  - Test with $R_2$: Range of $R_2$ is $[50, 53]$. Merging with any adjacent region yields $|53 - 10| = 43 > 3 \implies P = \mathbf{FALSE}$.<br>
  $$\text{Final Segmentation: 2 Distinct Regions (Background } \sim 11, \text{ Object } \sim 51)$$</p>
</div>
"""

# ── CHAPTER 18 ENRICHMENTS: MATHEMATICAL MORPHOLOGY ──────────────────
ch18_extra = r"""
# 18.64 Worked Example — 10-Mark University Model Answer: Fundamental Binary Morphology
### Problem Statement
A $6 \times 6$ binary image $A$ contains a solid foreground object with a single 1-pixel background hole and an isolated noise spur.
Let structuring element $B$ be a $3 \times 3$ cross structuring element centered at $(0,0)$:
$$B = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 1 & 1 \\ 0 & 1 & 0 \end{bmatrix}$$
1. Define the mathematical operations of Binary Erosion ($A \ominus B$) and Binary Dilation ($A \oplus B$).
2. Formulate Binary Opening ($A \circ B$) and Binary Closing ($A \bullet B$) and state their geometric filtering properties.
3. Express the formula for Morphological Boundary Extraction $\beta(A)$ and explain why erosion is preferred over dilation for boundary extraction.

### Step-by-Step Mathematical Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. Fundamental Definitions:</strong><br>
  - <strong>Binary Erosion ($A \ominus B$):</strong> The set of all translation points $z$ such that $B$, translated by $z$, is completely contained inside $A$:
  $$A \ominus B = \{z \mid (B)_z \subseteq A\}$$
  Erosion shrinks the object boundaries by peeling away an outer layer of pixels. Any foreground feature smaller than the structuring element is eradicated.</p>

  <p>- <strong>Binary Dilation ($A \oplus B$):</strong> The set of all translation points $z$ such that the reflected structuring element $\hat{B}$, translated by $z$, overlaps with $A$ by at least one pixel:
  $$A \oplus B = \{z \mid (\hat{B})_z \cap A \ne \emptyset\}$$
  Dilation expands foreground boundaries, bridging narrow gaps and filling small concave notches.</p>

  <p><strong>2. Compound Operators & Geometric Role:</strong><br>
  - <strong>Opening ($A \circ B$):</strong> Erosion followed by dilation with the same structuring element:
  $$A \circ B = (A \ominus B) \oplus B$$
  <em>Geometric Effect:</em> Eliminates thin foreground protrusions, severs narrow isthmuses connecting two larger bodies, and removes isolated noise spurs without significantly altering the global area of the primary object.</p>

  <p>- <strong>Closing ($A \bullet B$):</strong> Dilation followed by erosion with the same structuring element:
  $$A \bullet B = (A \oplus B) \ominus B$$
  <em>Geometric Effect:</em> Fuses narrow breaks and thin cracks, bridges small gaps between nearby segments, and fills small interior background holes without altering the macroscopic contour.</p>

  <p><strong>3. Morphological Boundary Extraction:</strong><br>
  The internal boundary $\beta(A)$ of set $A$ is obtained by subtracting the eroded set $A \ominus B$ from the original set $A$:
  $$\beta(A) = A - (A \ominus B) = A \cap (A \ominus B)^c$$
  <em>Rationale:</em> Because erosion removes exactly the outermost perimeter layer of pixels where the structuring element fails to fit entirely inside $A$, subtracting the eroded core leaves precisely the 1-pixel-thick boundary contour.</p>
</div>

# 18.65 Grayscale Morphology & The Top-Hat Transform
### Mathematical Definitions of Grayscale Morphology
Let $f(x, y)$ be the input grayscale image and $b(x, y)$ be a flat structuring element defined on support domain $D_b$:
- **Grayscale Erosion:** $[f \ominus b](x, y) = \min_{(s, t) \in D_b} \{ f(x + s, y + t) \}$
- **Grayscale Dilation:** $[f \oplus b](x, y) = \max_{(s, t) \in D_b} \{ f(x - s, y - t) \}$
- **Grayscale Opening:** $f \circ b = (f \ominus b) \oplus b$ (removes bright features smaller than $b$)
- **Grayscale Closing:** $f \bullet b = (f \oplus b) \ominus b$ (suppresses dark features smaller than $b$)

### Top-Hat and Bottom-Hat Transforms for Non-Uniform Illumination
In document scanning and biomedical microscopy, uneven illumination produces severe low-frequency background shading variations that defeat global thresholding.
The **Top-Hat Transform** extracts bright objects on a non-uniform dark background:
$$h_{top}(x, y) = f(x, y) - [f \circ b](x, y)$$
Because the morphological opening $f \circ b$ estimates the smoothly varying illumination background by removing all small sharp foreground text features, subtracting the opening leaves pristine, background-free foreground objects with a perfectly uniform zero-level reference.
"""

# ── CHAPTER 19 ENRICHMENTS: FEATURES & DESCRIPTORS ───────────────────
ch19_extra = r"""
# 19.96 Worked Example — 10-Mark University Model Answer: Gray-Level Co-occurrence Matrix (GLCM)
### Problem Statement
A $4 \times 4$ sub-image with $L = 4$ gray levels ($0, 1, 2, 3$) is given by:
$$F = \begin{bmatrix}
0 & 0 & 1 & 1 \\
0 & 0 & 1 & 1 \\
0 & 2 & 2 & 2 \\
2 & 2 & 3 & 3
\end{bmatrix}$$
1. Formulate the definition of the Gray-Level Co-occurrence Matrix $P(i, j \mid d, \theta)$.
2. Compute the unnormalized and normalized GLCM for distance $d = 1$ and horizontal angle $\theta = 0^\circ$.
3. Compute the following texture descriptors from the normalized GLCM:
   - Angular Second Moment (Energy / Uniformity): $ASM = \sum_i \sum_j p(i, j)^2$
   - Contrast: $CON = \sum_i \sum_j (i - j)^2 p(i, j)$
   - Homogeneity: $HOM = \sum_i \sum_j \frac{p(i, j)}{1 + |i - j|}$

### Step-by-Step Mathematical Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. GLCM Definition:</strong><br>
  The element $P(i, j \mid d, \theta)$ counts the number of times a pixel with intensity $i$ occurs horizontally adjacent ($d=1, \theta=0^\circ$) to a pixel with intensity $j$.</p>

  <p><strong>2. Horizontal Pixel Pair Inventory (Row-by-Row):</strong><br>
  - Row 1: $(0, 0), (0, 1), (1, 1) \implies (0,0): 1, \ (0,1): 1, \ (1,1): 1$<br>
  - Row 2: $(0, 0), (0, 1), (1, 1) \implies (0,0): 1, \ (0,1): 1, \ (1,1): 1$<br>
  - Row 3: $(0, 2), (2, 2), (2, 2) \implies (0,2): 1, \ (2,2): 2$<br>
  - Row 4: $(2, 2), (2, 3), (3, 3) \implies (2,2): 1, \ (2,3): 1, \ (3,3): 1$</p>

  <p>Total horizontal pairs $= 4 \text{ rows} \times 3 \text{ pairs/row} = \mathbf{12}$.</p>

  <p><strong>Unnormalized GLCM $P(i, j)$ and Normalized GLCM $p(i, j) = P(i, j) / 12$:</strong></p>
  <div class="table-wrap">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>$i \backslash j$</th>
          <th>$j = 0$</th>
          <th>$j = 1$</th>
          <th>$j = 2$</th>
          <th>$j = 3$</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>$i = 0$</strong></td><td>$2 \ (2/12)$</td><td>$2 \ (2/12)$</td><td>$1 \ (1/12)$</td><td>$0 \ (0)$</td></tr>
        <tr><td><strong>$i = 1$</strong></td><td>$0 \ (0)$</td><td>$2 \ (2/12)$</td><td>$0 \ (0)$</td><td>$0 \ (0)$</td></tr>
        <tr><td><strong>$i = 2$</strong></td><td>$0 \ (0)$</td><td>$0 \ (0)$</td><td>$3 \ (3/12)$</td><td>$1 \ (1/12)$</td></tr>
        <tr><td><strong>$i = 3$</strong></td><td>$0 \ (0)$</td><td>$0 \ (0)$</td><td>$0 \ (0)$</td><td>$1 \ (1/12)$</td></tr>
      </tbody>
    </table>
  </div>

  <p><strong>3. Numerical Computation of Texture Descriptors:</strong><br>
  - <strong>Energy (Angular Second Moment):</strong>
  $$ASM = \sum_{i=0}^3 \sum_{j=0}^3 p(i, j)^2 = \left(\frac{2}{12}\right)^2 + \left(\frac{2}{12}\right)^2 + \left(\frac{1}{12}\right)^2 + \left(\frac{2}{12}\right)^2 + \left(\frac{3}{12}\right)^2 + \left(\frac{1}{12}\right)^2 + \left(\frac{1}{12}\right)^2$$
  $$ASM = \frac{4 + 4 + 1 + 4 + 9 + 1 + 1}{144} = \frac{24}{144} = \frac{1}{6} \approx \mathbf{0.1667}$$</p>

  <p>- <strong>Contrast:</strong>
  $$CON = \sum_{i=0}^3 \sum_{j=0}^3 (i - j)^2 p(i, j)$$
  Diagonal terms ($i=j$) contribute $(0)^2 = 0$.<br>
  Non-zero off-diagonal terms:<br>
  - $(0, 1): (0 - 1)^2 \left(\frac{2}{12}\right) = 1 \left(\frac{2}{12}\right) = \frac{2}{12}$<br>
  - $(0, 2): (0 - 2)^2 \left(\frac{1}{12}\right) = 4 \left(\frac{1}{12}\right) = \frac{4}{12}$<br>
  - $(2, 3): (2 - 3)^2 \left(\frac{1}{12}\right) = 1 \left(\frac{1}{12}\right) = \frac{1}{12}$<br>
  $$CON = \frac{2 + 4 + 1}{12} = \frac{7}{12} \approx \mathbf{0.5833}$$</p>

  <p>- <strong>Homogeneity:</strong>
  $$HOM = \sum_{i=0}^3 \sum_{j=0}^3 \frac{p(i, j)}{1 + |i - j|}$$
  - Diagonal $(i=j \implies |i-j|=0)$: $(p_{00} + p_{11} + p_{22} + p_{33}) = \frac{2 + 2 + 3 + 1}{12} = \frac{8}{12} \times \frac{1}{1+0} = \frac{8}{12}$<br>
  - Pair $(0, 1): \frac{2/12}{1 + 1} = \frac{1}{12}$<br>
  - Pair $(0, 2): \frac{1/12}{1 + 2} = \frac{1}{36}$<br>
  - Pair $(2, 3): \frac{1/12}{1 + 1} = \frac{1}{24}$<br>
  $$HOM = \frac{8}{12} + \frac{1}{12} + \frac{1}{36} + \frac{1}{24} = \frac{48 + 6 + 2 + 3}{72} = \frac{59}{72} \approx \mathbf{0.8194}$$</p>
</div>

# 19.97 Topological Invariant: The Euler Number
The **Euler Number** (Euler Characteristic) $E$ is a fundamental topological descriptor that remains invariant under arbitrary rubber-sheet stretching, warping, and rotation.
For a 2D binary image:
$$E = C - H$$
where $C$ denotes the number of connected components (objects) and $H$ denotes the total number of holes (interior background cavities).

<div class="table-wrap">
  <table class="comparison-table">
    <thead>
      <tr>
        <th>Geometric Character / Glyph</th>
        <th>Connected Components ($C$)</th>
        <th>Holes ($H$)</th>
        <th>Euler Number ($E = C - H$)</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Letter 'A'</td><td>1</td><td>1</td><td>$1 - 1 = \mathbf{0}$</td></tr>
      <tr><td>Letter 'B'</td><td>1</td><td>2</td><td>$1 - 2 = \mathbf{-1}$</td></tr>
      <tr><td>Letter 'C', 'E', 'L', 'S'</td><td>1</td><td>0</td><td>$1 - 0 = \mathbf{1}$</td></tr>
      <tr><td>Colon symbol ':'</td><td>2</td><td>0</td><td>$2 - 0 = \mathbf{2}$</td></tr>
      <tr><td>Number '8'</td><td>1</td><td>2</td><td>$1 - 2 = \mathbf{-1}$</td></tr>
    </tbody>
  </table>
</div>
"""

# ── CHAPTER 20 ENRICHMENTS: SIFT, SURF, ORB, HOG ─────────────────────
ch20_extra = r"""
# 20.75 Worked Example — 10-Mark University Model Answer: Harris Corner Response Matrix
### Problem Statement
The local spatial derivative products across an image patch produce the following $2 \times 2$ Harris autocorrelation matrix (structure tensor):
$$M = \sum_{(x, y) \in W} w(x, y) \begin{bmatrix} I_x^2 & I_x I_y \\ I_x I_y & I_y^2 \end{bmatrix} = \begin{bmatrix} 24 & 6 \\ 6 & 16 \end{bmatrix}$$
1. Formulate the Taylor series derivation of the local auto-correlation function $E(u, v)$ for a spatial shift $(u, v)$.
2. Explain the physical significance of the eigenvalues $\lambda_1, \lambda_2$ of matrix $M$.
3. Compute the determinant $\det(M)$ and trace $\text{Tr}(M)$.
4. Calculate the Harris corner response measure $R = \det(M) - k (\text{Tr}(M))^2$ with empirical parameter $k = 0.04$, and classify the underlying image feature.

### Step-by-Step Mathematical Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. Shift Auto-Correlation Derivation:</strong><br>
  The change in intensity produced by a small shift $(u, v)$ weighted by window $w(x, y)$ is:
  $$E(u, v) = \sum_{x, y} w(x, y) [I(x+u, y+v) - I(x, y)]^2$$
  Approximating $I(x+u, y+v)$ via first-order 2D Taylor series:
  $$I(x+u, y+v) \approx I(x, y) + u I_x(x, y) + v I_y(x, y)$$
  $$E(u, v) \approx \sum_{x, y} w(x, y) [u I_x + v I_y]^2 = \begin{bmatrix} u & v \end{bmatrix} M \begin{bmatrix} u \\ v \end{bmatrix}$$
  where $M$ is the symmetric positive semi-definite structure tensor.</p>

  <p><strong>2. Physical Significance of Eigenvalues $\lambda_1, \lambda_2$:</strong><br>
  The eigenvalues of $M$ represent the principal curvatures of the local auto-correlation surface:<br>
  - $\lambda_1 \approx 0, \ \lambda_2 \approx 0 \implies$ <strong>Flat Region:</strong> No significant gradient in any direction.<br>
  - $\lambda_1 \gg \lambda_2 \approx 0 \text{ (or vice versa)} \implies$ <strong>Edge:</strong> Strong gradient perpendicular to edge, zero gradient along edge.<br>
  - $\lambda_1 \gg 0 \text{ and } \lambda_2 \gg 0 \implies$ <strong>Corner:</strong> Strong intensity variations in all spatial directions.</p>

  <p><strong>3. Matrix Determinant and Trace:</strong><br>
  Given $M = \begin{bmatrix} 24 & 6 \\ 6 & 16 \end{bmatrix}$:<br>
  $$\det(M) = (24 \times 16) - (6 \times 6) = 384 - 36 = \mathbf{348}$$
  $$\text{Tr}(M) = 24 + 16 = \mathbf{40}$$</p>

  <p><strong>4. Harris Corner Response $R$:</strong><br>
  $$R = \det(M) - k [\text{Tr}(M)]^2 = 348 - 0.04(40)^2$$
  $$R = 348 - 0.04(1600) = 348 - 64 = \mathbf{+284}$$
  $$\because R = +284 > 0 \implies \text{Classified as a Distinct Corner Feature}$$
  Because $R$ is strongly positive, the local patch contains significant gradient energy in multiple orthogonal directions, making it an ideal anchor keypoint for image matching.</p>
</div>

# 20.76 SIFT 128-Dimensional Keypoint Descriptor Architectural Blueprint
<div class="table-wrap">
  <table class="comparison-table">
    <thead>
      <tr>
        <th>SIFT Pipeline Stage</th>
        <th>Mathematical Formulation</th>
        <th>Invariance Achieved</th>
        <th>Engineering Significance</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Scale-Space Extrema</strong></td>
        <td>$D(x, y, \sigma) = (G(x, y, k\sigma) - G(x, y, \sigma)) * I(x, y)$</td>
        <td><strong>Scale Invariance</strong></td>
        <td>Approximates scale-normalized Laplacian $\sigma^2 \nabla^2 G$ efficiently via DoG octaves.</td>
      </tr>
      <tr>
        <td><strong>2. Sub-Pixel Localization &amp; Edge Rejection</strong></td>
        <td>$\hat{x} = -H^{-1} \frac{\partial D}{\partial x}$, Hessian ratio $\frac{\text{Tr}(H)^2}{\det(H)} < \frac{(r+1)^2}{r}$ ($r=10$)</td>
        <td><strong>Contrast &amp; Edge Noise Invariance</strong></td>
        <td>Discards low-contrast keypoints ($|D(\hat{x})| < 0.03$) and unstable 1D edge ridges.</td>
      </tr>
      <tr>
        <td><strong>3. Orientation Assignment</strong></td>
        <td>$\theta = \arctan \frac{L(x, y+1) - L(x, y-1)}{L(x+1, y) - L(x-1, y)}$, 36-bin orientation histogram</td>
        <td><strong>Rotation Invariance</strong></td>
        <td>Assigns canonical orientation corresponding to peak gradient direction.</td>
      </tr>
      <tr>
        <td><strong>4. 128-D Feature Descriptor</strong></td>
        <td>$16 \times 16$ pixel window $\to 4 \times 4$ subregions $\to 8$ orientation bins each ($4 \times 4 \times 8 = 128$)</td>
        <td><strong>Illumination &amp; 3D Viewpoint Robustness</strong></td>
        <td>Normalized to unit length $\|\mathbf{v}\|=1$, clipped at 0.2, and re-normalized.</td>
      </tr>
    </tbody>
  </table>
</div>
"""

PART3_ENRICHMENTS = {
    15: ch15_extra,
    16: ch16_extra,
    17: ch17_extra,
    18: ch18_extra,
    19: ch19_extra,
    20: ch20_extra
}

def compile_part3():
    print("=" * 60)
    print("COMPILING ENRICHED DIP PART III CHAPTERS (C15 - C20)")
    print("=" * 60)

    part3_metas = [m for m in CHAPTERS_META if 15 <= m['chapter_num'] <= 20]

    for meta in part3_metas:
        c_num = meta['chapter_num']
        extra = PART3_ENRICHMENTS.get(c_num, None)
        print(f"\n--- Compiling Chapter {c_num:02d}: {meta['title']} ---")
        build_enriched_chapter(meta, extra_sections_md=extra)

    print("\n" + "=" * 60)
    print("ALL 6 PART III CHAPTERS SUCCESSFULLY COMPILED!")
    print("=" * 60)

if __name__ == '__main__':
    compile_part3()
