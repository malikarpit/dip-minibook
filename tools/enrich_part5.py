#!/usr/bin/env python3
"""
Digital Image Processing (DIP) MiniBook — Part V Master Enrichment & Compilation Suite
Compiles Chapters 25 to 31 (Intelligent Vision: Classification, CNNs, VGG/ResNet, YOLO,
Autoencoders, Video Optical Flow, Engineering Applications, and Master Synthesis)
into comprehensive 2,200+ line production-grade HTML chapters matching the AIML standard.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_DIR = os.path.join(BASE_DIR, 'tools')
sys.path.append(TOOLS_DIR)

from enrich_and_build import build_enriched_chapter
from build_chapter import CHAPTERS_META

# ── CHAPTER 25 ENRICHMENTS: IMAGE CLASSIFICATION FOUNDATIONS ───────────
ch25_extra = r"""
# 25.41 Worked Example — 10-Mark University Model Answer: Distance Classifiers, Decision Boundaries & Softmax Loss
### Problem Statement
A computer vision classifier maps extracted feature vectors $x \in \mathbb{R}^2$ representing normalized brightness and edge density into three distinct scene categories: $\omega_1$ (Urban), $\omega_2$ (Forest), and $\omega_3$ (Water). The prototype class mean vectors are:
$$m_1 = \begin{bmatrix} 0.8 \\ 0.7 \end{bmatrix}, \qquad m_2 = \begin{bmatrix} 0.3 \\ 0.8 \end{bmatrix}, \qquad m_3 = \begin{bmatrix} 0.2 \\ 0.1 \end{bmatrix}$$
An unknown query feature vector is observed as $x = \begin{bmatrix} 0.75 \\ 0.65 \end{bmatrix}$.
1. Formulate the Minimum Distance Classifier decision rule based on Euclidean distance.
2. Calculate the Euclidean distance $D_k(x)$ from query $x$ to all three class mean vectors and assign $x$ to the optimal class.
3. Derive the equation of the linear decision boundary separating class $\omega_1$ and class $\omega_2$.
4. Given raw classifier logit scores $z = [z_1, z_2, z_3] = [3.2, 1.1, -0.5]$, compute the normalized Softmax class posterior probabilities $P(\omega_k | x)$.
5. If the true label is $\omega_1$ (one-hot target $y = [1, 0, 0]$), compute the categorical cross-entropy loss $\mathcal{L}_{CE}$.

### Step-by-Step Mathematical Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. Minimum Distance Classifier Formulation:</strong><br>
  For $K$ classes with mean vectors $m_k$, the squared Euclidean distance from an unknown vector $x$ is:
  $$D_k^2(x) = \|x - m_k\|^2 = (x - m_k)^T (x - m_k) = x^T x - 2 m_k^T x + m_k^T m_k$$
  Since $x^T x$ is identical for all candidate classes, minimizing distance is mathematically equivalent to maximizing the linear discriminant function:
  $$d_k(x) = m_k^T x - \frac{1}{2} m_k^T m_k = w_k^T x + w_{k0}$$
  where $w_k = m_k$ is the weight vector and $w_{k0} = -\frac{1}{2} \|m_k\|^2$ is the threshold bias.</p>

  <p><strong>2. Distance Computations to Query $x = [0.75, 0.65]^T$:</strong><br>
  - Distance to $m_1 = [0.8, 0.7]^T$:
    $$\Delta_1 = x - m_1 = \begin{bmatrix} 0.75 - 0.80 \\ 0.65 - 0.70 \end{bmatrix} = \begin{bmatrix} -0.05 \\ -0.05 \end{bmatrix}$$
    $$D_1(x) = \sqrt{(-0.05)^2 + (-0.05)^2} = \sqrt{0.0025 + 0.0025} = \sqrt{0.0050} \approx \mathbf{0.0707}$$
  - Distance to $m_2 = [0.3, 0.8]^T$:
    $$\Delta_2 = x - m_2 = \begin{bmatrix} 0.75 - 0.30 \\ 0.65 - 0.80 \end{bmatrix} = \begin{bmatrix} +0.45 \\ -0.15 \end{bmatrix}$$
    $$D_2(x) = \sqrt{(0.45)^2 + (-0.15)^2} = \sqrt{0.2025 + 0.0225} = \sqrt{0.2250} \approx \mathbf{0.4743}$$
  - Distance to $m_3 = [0.2, 0.1]^T$:
    $$\Delta_3 = x - m_3 = \begin{bmatrix} 0.75 - 0.20 \\ 0.65 - 0.10 \end{bmatrix} = \begin{bmatrix} +0.55 \\ +0.55 \end{bmatrix}$$
    $$D_3(x) = \sqrt{(0.55)^2 + (0.55)^2} = \sqrt{0.3025 + 0.3025} = \sqrt{0.6050} \approx \mathbf{0.7778}$$
  <strong>Classification Decision:</strong> Since $D_1(x) = 0.0707 < D_2(x) < D_3(x)$, the query sample $x$ is unambiguously assigned to <strong>Class $\omega_1$ (Urban)</strong>.</p>

  <p><strong>3. Linear Decision Boundary between $\omega_1$ and $\omega_2$:</strong><br>
  The decision boundary corresponds to the locus of points equidistant from $m_1$ and $m_2$:
  $$d_1(x) - d_2(x) = 0 \iff (m_1 - m_2)^T x - \frac{1}{2} (\|m_1\|^2 - \|m_2\|^2) = 0$$
  Vector difference: $m_1 - m_2 = [0.8 - 0.3, 0.7 - 0.8]^T = [0.5, -0.1]^T$.<br>
  Norms: $\|m_1\|^2 = 0.8^2 + 0.7^2 = 0.64 + 0.49 = 1.13$.<br>
  $\|m_2\|^2 = 0.3^2 + 0.8^2 = 0.09 + 0.64 = 0.73$.<br>
  Constant term: $\frac{1}{2}(1.13 - 0.73) = \frac{1}{2}(0.40) = 0.20$.<br>
  $$0.5 x_1 - 0.1 x_2 - 0.20 = 0 \iff \mathbf{5 x_1 - x_2 - 2 = 0} \iff \mathbf{x_2 = 5 x_1 - 2}$$
  This is a straight line perpendicular to the line segment connecting mean vectors $m_1$ and $m_2$, bisecting them at their midpoint.</p>

  <p><strong>4. Softmax Class Posterior Probability Computation:</strong><br>
  Given logits $z = [3.2, 1.1, -0.5]$:
  $$e^{z_1} = e^{3.2} \approx 24.5325$$
  $$e^{z_2} = e^{1.1} \approx 3.0042$$
  $$e^{z_3} = e^{-0.5} \approx 0.6065$$
  Normalization partition sum $\sum_{j=1}^3 e^{z_j} = 24.5325 + 3.0042 + 0.6065 = \mathbf{28.1432}$.<br>
  Posterior probabilities:
  $$P(\omega_1 | x) = \frac{24.5325}{28.1432} \approx \mathbf{0.8717 \ (87.17\%)}$$
  $$P(\omega_2 | x) = \frac{3.0042}{28.1432} \approx \mathbf{0.1067 \ (10.67\%)}$$
  $$P(\omega_3 | x) = \frac{0.6065}{28.1432} \approx \mathbf{0.0216 \ (2.16\%)}$$</p>

  <p><strong>5. Categorical Cross-Entropy Loss:</strong><br>
  $$\mathcal{L}_{CE} = -\sum_{k=1}^3 y_k \ln P(\omega_k | x) = -1 \cdot \ln(0.8717) - 0 - 0 = -\ln(0.8717) \approx \mathbf{0.1373 \text{ nats}}$$
  The low cross-entropy loss indicates high model confidence in the correct ground truth class.</p>
</div>

# 25.42 Comprehensive Delhi University Examination Checklist & Mark Distribution
<div class="exam-checklist">
  <h4>Delhi University Semester Examination Quick Revision & Marking Distribution</h4>
  <ul>
    <li><strong>Question 1 (10 Marks): Minimum Distance Classifier vs k-NN.</strong>
      <ul>
        <li>Definition of class mean prototype vectors and Euclidean distance discriminant formulation (3 Marks).</li>
        <li>k-Nearest Neighbors majority voting algorithm and choice of $k$ (odd integer to prevent ties) (3 Marks).</li>
        <li>Voronoi tessellation and piece-wise linear vs non-linear decision boundaries (2 Marks).</li>
        <li>Computational complexity during inference ($O(K \cdot D)$ for prototype vs $O(N \cdot D)$ for k-NN) (2 Marks).</li>
      </ul>
    </li>
    <li><strong>Question 2 (10 Marks): Softmax Activation & Cross-Entropy Loss.</strong>
      <ul>
        <li>Mathematical derivation of Softmax function and conversion of real logits $\mathbb{R}^K$ to valid probability simplex (3 Marks).</li>
        <li>Derivation of the gradient of Cross-Entropy with respect to logits: $\frac{\partial \mathcal{L}}{\partial z_i} = P_i - y_i$ (4 Marks).</li>
        <li>Numerical example demonstrating numerical stability using the log-sum-exp trick (3 Marks).</li>
      </ul>
    </li>
  </ul>
</div>
"""

# ── CHAPTER 26 ENRICHMENTS: CONVOLUTIONAL NEURAL NETWORKS ─────────────
ch26_extra = r"""
# 26.46 Worked Example — 10-Mark University Model Answer: CNN Layer Dimensions, Receptive Fields & Parameter Counts
### Problem Statement
A Convolutional Neural Network processes input colour images of spatial dimension $W_{in} \times H_{in} \times C_{in} = 224 \times 224 \times 3$. The initial feature extraction block consists of the following consecutive stages:
- **Layer 1 (Conv1):** 64 filters of size $7 \times 7$, stride $S = 2$, padding $P = 3$.
- **Layer 2 (BatchNorm + ReLU):** Non-linear point activation.
- **Layer 3 (MaxPool1):** Max pooling window of size $3 \times 3$, stride $S = 2$, padding $P = 1$.
- **Layer 4 (Conv2):** 128 filters of size $3 \times 3$, stride $S = 1$, padding $P = 1$.
1. State the fundamental formula determining the output spatial dimensions $(W_{out}, H_{out})$ of a 2D convolution or pooling layer.
2. Calculate the exact output feature tensor shape $[B, C, H, W]$ after Conv1, MaxPool1, and Conv2 (assuming batch size $B = 16$).
3. Compute the total number of learnable parameters (weights and biases) in Layer 1 (Conv1) and Layer 4 (Conv2).
4. Contrast the parameter count of Conv1 with an equivalent fully-connected (dense) layer operating on the flattened $224 \times 224 \times 3$ input to produce 64 outputs.
5. Compute the effective receptive field ($RF$) of a neuron in Conv2 with respect to the original input image.

### Step-by-Step Mathematical Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. Output Spatial Dimension Formula:</strong><br>
  For an input spatial dimension $W$, filter kernel size $K$, zero-padding $P$, and stride $S$:
  $$W_{out} = \left\lfloor \frac{W - K + 2P}{S} \right\rfloor + 1$$
  This formula applies independently to width and height.</p>

  <p><strong>2. Step-by-Step Tensor Dimensional Tracking:</strong><br>
  - <strong>Input:</strong> Shape $[16, 3, 224, 224]$.<br>
  - <strong>Layer 1 (Conv1: $K=7, S=2, P=3, C_{out}=64$):</strong>
    $$W_{1} = \left\lfloor \frac{224 - 7 + 2(3)}{2} \right\rfloor + 1 = \left\lfloor \frac{224 - 7 + 6}{2} \right\rfloor + 1 = \left\lfloor \frac{223}{2} \right\rfloor + 1 = 111 + 1 = 112$$
    Feature map tensor shape after Conv1: $\mathbf{[16, 64, 112, 112]}$.<br>
  - <strong>Layer 2 (BatchNorm + ReLU):</strong> Pointwise operations; preserves spatial dimensions and channels exactly: $\mathbf{[16, 64, 112, 112]}$.<br>
  - <strong>Layer 3 (MaxPool1: $K=3, S=2, P=1$):</strong>
    $$W_{3} = \left\lfloor \frac{112 - 3 + 2(1)}{2} \right\rfloor + 1 = \left\lfloor \frac{111}{2} \right\rfloor + 1 = 55 + 1 = 56$$
    Feature map tensor shape after MaxPool1: $\mathbf{[16, 64, 56, 56]}$.<br>
  - <strong>Layer 4 (Conv2: $K=3, S=1, P=1, C_{out}=128$):</strong>
    $$W_{4} = \left\lfloor \frac{56 - 3 + 2(1)}{1} \right\rfloor + 1 = \left\lfloor \frac{55}{1} \right\rfloor + 1 = 55 + 1 = 56$$
    Feature map tensor shape after Conv2: $\mathbf{[16, 128, 56, 56]}$.</p>

  <p><strong>3. Learnable Parameter Count Calculations:</strong><br>
  For a convolutional layer with $C_{in}$ input channels, $C_{out}$ filters of size $K \times K$:
  $$\text{Parameters} = C_{out} \times (K \times K \times C_{in} + 1)$$
  where $+1$ accounts for the per-filter scalar bias.<br>
  - <strong>Conv1:</strong> $C_{in} = 3, C_{out} = 64, K = 7$:
    $$\text{Params}_{\text{Conv1}} = 64 \times (7 \times 7 \times 3 + 1) = 64 \times (147 + 1) = 64 \times 148 = \mathbf{9,472 \text{ parameters}}$$
  - <strong>Conv2:</strong> $C_{in} = 64, C_{out} = 128, K = 3$:
    $$\text{Params}_{\text{Conv2}} = 128 \times (3 \times 3 \times 64 + 1) = 128 \times (576 + 1) = 128 \times 577 = \mathbf{73,856 \text{ parameters}}$$</p>

  <p><strong>4. Comparison with Fully Connected Layer:</strong><br>
  If the input were flattened into a 1D vector of dimension $N = 224 \times 224 \times 3 = 150,528$, a fully connected dense layer producing 64 outputs would require:
  $$\text{Params}_{\text{Dense}} = (150,528 \times 64) + 64 = 9,633,792 + 64 = \mathbf{9,633,856 \text{ parameters}}$$
  $$\text{Reduction Factor} = \frac{9,633,856}{9,472} \approx \mathbf{1,017 \times \text{ fewer parameters!}}$$
  This dramatic efficiency demonstrates the power of <strong>parameter sharing</strong> and <strong>local receptive fields</strong> in convolutional layers.</p>

  <p><strong>5. Effective Receptive Field ($RF$) Derivation:</strong><br>
  Receptive field propagates recursively according to: $RF_{out} = RF_{in} + (K - 1) \times J_{in}$, where $J_{in}$ is the cumulative stride.<br>
  - Input: $RF_0 = 1, J_0 = 1$.<br>
  - Conv1 ($K=7, S=2$): $RF_1 = 1 + (7 - 1) \times 1 = 7$. Cumulative stride $J_1 = 1 \times 2 = 2$.<br>
  - MaxPool1 ($K=3, S=2$): $RF_2 = 7 + (3 - 1) \times 2 = 7 + 4 = 11$. Cumulative stride $J_2 = 2 \times 2 = 4$.<br>
  - Conv2 ($K=3, S=1$): $RF_3 = 11 + (3 - 1) \times 4 = 11 + 8 = \mathbf{19 \times 19 \text{ pixels}}$.<br>
  Each feature vector in Conv2 looks at a $19 \times 19$ patch in the original pristine image.</p>
</div>

# 26.47 Convolutional Mechanics Architecture Diagram
```mermaid
graph LR
    Input["Input Image<br>[3, 224, 224]"] --> Conv1["Conv 7x7, s=2, p=3<br>64 Kernels"]
    Conv1 --> Feat1["Feature Map<br>[64, 112, 112]"]
    Feat1 --> Pool1["MaxPool 3x3, s=2<br>Downsampling"]
    Pool1 --> Feat2["Feature Map<br>[64, 56, 56]"]
    Feat2 --> Conv2["Conv 3x3, s=1, p=1<br>128 Kernels"]
    Conv2 --> Feat3["Deep Feature Tensor<br>[128, 56, 56]"]
```
"""

# ── CHAPTER 27 ENRICHMENTS: VGG & RESNET ARCHITECTURES ────────────────
ch27_extra = r"""
# 27.42 Worked Example — 10-Mark University Model Answer: VGG Filter Factorization & ResNet Skip Connections
### Problem Statement
Modern deep convolutional neural networks overcame the severe degradation and vanishing gradient problems through architectural innovations:
1. State and prove the **Small Filter Factorization Theorem** introduced in VGG-16: why two cascaded $3 \times 3$ convolutional layers are superior to a single $5 \times 5$ layer, and three cascaded $3 \times 3$ layers are superior to a single $7 \times 7$ layer.
2. Compute the exact percentage reduction in parameters and FLOPs achieved by replacing one $5 \times 5$ convolution with two $3 \times 3$ convolutions for $C$ channels.
3. Formulate the **Degradation Problem** observed when training plain deep networks (e.g. plain 20-layer vs 56-layer networks).
4. Write the mathematical formulation of a **ResNet Residual Block** ($H(x) = F(x) + x$) and derive the backpropagation gradient $\frac{\partial \mathcal{E}}{\partial x}$ to prove why gradients never vanish in ResNet.

### Step-by-Step Mathematical Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. Proof of the Small Filter Factorization Theorem:</strong><br>
  Consider two consecutive convolutional layers with kernel size $K_1 = 3 \times 3$ and $K_2 = 3 \times 3$ with stride $S = 1$:<br>
  - Layer 1 output pixel at coordinate $(i, j)$ depends on a $3 \times 3$ neighborhood of the input.<br>
  - Layer 2 output pixel at $(i, j)$ depends on a $3 \times 3$ neighborhood of Layer 1.<br>
  - The corner pixels of Layer 2's $3 \times 3$ window extend the receptive field by 1 pixel in each direction:
    $$RF_{\text{effective}} = 1 + (3 - 1) + (3 - 1) = 1 + 2 + 2 = \mathbf{5 \times 5}$$
  Thus, two cascaded $3 \times 3$ convolutions cover the identical $5 \times 5$ receptive field as a single $5 \times 5$ filter.<br>
  Similarly, three cascaded $3 \times 3$ convolutions produce:
  $$RF_{\text{effective}} = 1 + 2 + 2 + 2 = \mathbf{7 \times 7}$$
  matching a single large $7 \times 7$ convolution.</p>

  <p><strong>2. Parameter Count and Expressiveness Comparison:</strong><br>
  Assume input and output feature maps both have $C$ channels:<br>
  - <strong>Single $5 \times 5$ Layer:</strong>
    $$\text{Params}_{5\times5} = 5 \times 5 \times C \times C = \mathbf{25 C^2}$$
  - <strong>Two Stacked $3 \times 3$ Layers:</strong>
    $$\text{Params}_{2 \times (3\times3)} = 2 \times (3 \times 3 \times C \times C) = 2 \times 9 C^2 = \mathbf{18 C^2}$$
  $$\text{Parameter Reduction} = \frac{25 C^2 - 18 C^2}{25 C^2} = \frac{7}{25} = \mathbf{28\% \text{ reduction}}$$
  <strong>Dual Pedagogical Advantages:</strong><br>
  1. <strong>Fewer Parameters:</strong> Saves 28% memory and computational FLOPs, acting as powerful regularization against overfitting.<br>
  2. <strong>Greater Non-Linearity:</strong> Two $3 \times 3$ layers incorporate two consecutive ReLU non-linearities ($\text{Conv} \to \text{ReLU} \to \text{Conv} \to \text{ReLU}$) instead of just one, enabling the network to learn significantly more discriminative decision surfaces.</p>

  <p><strong>3. The Degradation Problem:</strong><br>
  As network depth increases beyond ~20 layers in standard networks, accuracy saturates and then degrades rapidly. Crucially, this degradation is <strong>not caused by overfitting</strong> (both training error and test error are higher on a 56-layer network than a 20-layer network). Instead, it is an optimization failure: deeper networks struggle to learn identity mappings ($H(x) = x$), causing gradient signals to vanish or explode during backpropagation across dozens of non-linear matrix multiplications.</p>

  <p><strong>4. ResNet Mathematical Formulation & Gradient Flow:</strong><br>
  Instead of forcing stacked layers to approximate the underlying mapping $H(x)$, ResNet explicitly reformulates the layers to fit a <strong>residual mapping</strong>:
  $$F(x) = H(x) - x \implies H(x) = F(x) + x$$
  where $x$ is the identity shortcut connection.<br>
  For a deep residual network with $L$ blocks, the feature representation at any deeper block $L$ is:
  $$x_L = x_l + \sum_{i=l}^{L-1} F(x_i, \mathcal{W}_i)$$
  Let $\mathcal{E}$ denote the loss function. Using the chain rule, the backpropagation gradient with respect to an earlier activation $x_l$ is:
  $$\frac{\partial \mathcal{E}}{\partial x_l} = \frac{\partial \mathcal{E}}{\partial x_L} \frac{\partial x_L}{\partial x_l} = \frac{\partial \mathcal{E}}{\partial x_L} \left( \mathbf{I} + \frac{\partial}{\partial x_l} \sum_{i=l}^{L-1} F(x_i, \mathcal{W}_i) \right)$$
  $$\frac{\partial \mathcal{E}}{\partial x_l} = \underbrace{\frac{\partial \mathcal{E}}{\partial x_L}}_{\text{Unattenuated Gradient}} + \underbrace{\frac{\partial \mathcal{E}}{\partial x_L} \left( \frac{\partial}{\partial x_l} \sum_{i=l}^{L-1} F(x_i, \mathcal{W}_i) \right)}_{\text{Residual Gradient}}$$
  <strong>The Key Insight:</strong> The term $\mathbf{I}$ ensures that the gradient $\frac{\partial \mathcal{E}}{\partial x_L}$ is propagated <strong>directly and unattenuated</strong> back to any earlier layer $x_l$, even if the weight-dependent term $\frac{\partial F}{\partial x_l}$ approaches zero! This completely solves the vanishing gradient problem, allowing successful training of networks with 50, 101, or 152 layers.</p>
</div>

# 27.43 ResNet Residual Block Architecture
```mermaid
graph TD
    Input["Input Tensor x"] --> Conv1["Weight Layer (Conv 3x3)"]
    Conv1 --> Relu1["ReLU Activation"]
    Relu1 --> Conv2["Weight Layer (Conv 3x3)"]
    Input ----> Shortcut["Identity Shortcut Connection: x"]
    Conv2 --> Add["Element-wise Addition: F(x) + x"]
    Shortcut --> Add
    Add --> OutRelu["Output ReLU: H(x) = ReLU(F(x) + x)"]
```
"""

# ── CHAPTER 28 ENRICHMENTS: OBJECT DETECTION & YOLO ───────────────────
ch28_extra = r"""
# 28.45 Worked Example — 10-Mark University Model Answer: Intersection over Union (IoU) & Non-Maximum Suppression (NMS)
### Problem Statement
In an automated traffic surveillance system, an object detector outputs candidate bounding boxes for a detected vehicle. Bounding boxes are parameterized as $[x_{min}, y_{min}, x_{max}, y_{max}]$ with corresponding vehicle detection confidence scores:
- **Box A:** $[50, 50, 150, 200]$, Confidence $S_A = 0.92$
- **Box B:** $[60, 55, 155, 205]$, Confidence $S_B = 0.85$
- **Box C:** $[55, 60, 160, 210]$, Confidence $S_C = 0.78$
- **Box D:** $[220, 100, 310, 220]$, Confidence $S_D = 0.88$
1. Define the **Intersection over Union (IoU)** metric mathematically and state its role as a localization fidelity measure.
2. Compute the exact area of Box A, Box B, their intersection area, and the resulting $IoU(A, B)$.
3. Trace the **Non-Maximum Suppression (NMS)** algorithm on candidate set $\{A, B, C, D\}$ with an NMS suppression threshold of $\tau = 0.50$.
4. Specify the final retained detection bounding boxes with their confidence scores.

### Step-by-Step Mathematical Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. Mathematical Definition of IoU:</strong><br>
  For two bounding boxes $B_1$ and $B_2$, the Jaccard Index / Intersection over Union is:
  $$IoU(B_1, B_2) = \frac{\text{Area}(B_1 \cap B_2)}{\text{Area}(B_1 \cup B_2)} = \frac{\text{Area}(B_1 \cap B_2)}{\text{Area}(B_1) + \text{Area}(B_2) - \text{Area}(B_1 \cap B_2)}$$
  $IoU$ ranges between $0.0$ (disjoint boxes) and $1.0$ (identical geometry). In standard evaluation (PASCAL VOC / COCO), a detection is considered a True Positive if $IoU \ge 0.50$.</p>

  <p><strong>2. Detailed Area and IoU Computations for Box A and Box B:</strong><br>
  - <strong>Box A:</strong> $[x_{min}, y_{min}, x_{max}, y_{max}] = [50, 50, 150, 200]$
    $$\text{Width } W_A = 150 - 50 = 100, \qquad \text{Height } H_A = 200 - 50 = 150$$
    $$\text{Area}(A) = 100 \times 150 = \mathbf{15,000 \text{ pixels}^2}$$
  - <strong>Box B:</strong> $[x_{min}, y_{min}, x_{max}, y_{max}] = [60, 55, 155, 205]$
    $$\text{Width } W_B = 155 - 60 = 95, \qquad \text{Height } H_B = 205 - 55 = 150$$
    $$\text{Area}(B) = 95 \times 150 = \mathbf{14,250 \text{ pixels}^2}$$
  - <strong>Intersection Box $(A \cap B)$:</strong>
    $$x_{min}^{\cap} = \max(50, 60) = 60, \qquad y_{min}^{\cap} = \max(50, 55) = 55$$
    $$x_{max}^{\cap} = \min(150, 155) = 150, \qquad y_{max}^{\cap} = \min(200, 205) = 200$$
    $$\text{Width } W_{\cap} = 150 - 60 = 90, \qquad \text{Height } H_{\cap} = 200 - 55 = 145$$
    $$\text{Area}(A \cap B) = 90 \times 145 = \mathbf{13,050 \text{ pixels}^2}$$
  - <strong>Union Area:</strong>
    $$\text{Area}(A \cup B) = 15,000 + 14,250 - 13,050 = \mathbf{16,200 \text{ pixels}^2}$$
  - <strong>$IoU(A, B)$:</strong>
    $$IoU(A, B) = \frac{13,050}{16,200} = \mathbf{0.8056 \ (80.56\%)}$$</p>

  <p><strong>3. Step-by-Step NMS Algorithm Trace ($\tau = 0.50$):</strong><br>
  - <strong>Step 1: Sort candidates in descending order of confidence:</strong>
    $$\mathcal{B} = [A (0.92), D (0.88), B (0.85), C (0.78)], \qquad \mathcal{D}_{\text{final}} = \emptyset$$
  - <strong>Step 2: Select candidate with highest confidence:</strong> Select <strong>Box A (0.92)</strong>.
    Add Box A to $\mathcal{D}_{\text{final}} = \{A\}$. Remove A from $\mathcal{B}$.
    Compute IoU between Box A and remaining boxes in $\mathcal{B}$:
    - $IoU(A, D)$: Box D has $x \in [220, 310]$, Box A has $x \in [50, 150]$. Completely disjoint! $IoU(A, D) = 0.0 < 0.50 \implies$ <strong>Keep Box D</strong>.
    - $IoU(A, B) = 0.8056 > 0.50 \implies$ <strong>Suppress Box B!</strong>
    - $IoU(A, C)$: Box C has $W_{\cap} = 150 - 55 = 95, H_{\cap} = 200 - 60 = 140 \implies \text{Area}_{\cap} = 13,300$.
      $\text{Area}(C) = (160 - 55) \times (210 - 60) = 105 \times 150 = 15,750$.
      $IoU(A, C) = \frac{13,300}{15,000 + 15,750 - 13,300} = \frac{13,300}{17,450} \approx 0.7622 > 0.50 \implies$ <strong>Suppress Box C!</strong>
    Remaining list: $\mathcal{B} = [D (0.88)]$.
  - <strong>Step 3: Process next highest candidate in $\mathcal{B}$</strong>: Select <strong>Box D (0.88)</strong>.
    Add Box D to $\mathcal{D}_{\text{final}} = \{A, D\}$. Remove D from $\mathcal{B}$.
    No candidate boxes remain in $\mathcal{B}$. Terminate.</p>

  <p><strong>4. Final Detections Retained:</strong><br>
  - <strong>Vehicle 1:</strong> Box A $[50, 50, 150, 200]$, Confidence $\mathbf{0.92}$<br>
  - <strong>Vehicle 2:</strong> Box D $[220, 100, 310, 220]$, Confidence $\mathbf{0.88}$<br>
  Redundant overlapping predictions B and C were successfully eliminated.</p>
</div>

# 28.46 YOLO Grid-Based Unified Detection Pipeline
```mermaid
graph TD
    Img["Input Image 448x448x3"] --> Backbone["Darknet CNN Backbone"]
    Backbone --> Grid["SxS Grid Division (7x7)"]
    Grid --> Tensor["Output 3D Tensor: S x S x (B*5 + C)<br>7 x 7 x (2*5 + 20) = 7 x 7 x 30"]
    Tensor --> Boxes["Bounding Box Predictions<br>[x, y, w, h, Confidence]"]
    Tensor --> Probs["Class Conditional Probabilities<br>P(Class | Object)"]
    Boxes --> NMS["Non-Maximum Suppression (NMS)<br>IoU Threshold = 0.5"]
    Probs --> NMS
    NMS --> Final["Final Bounding Boxes & Labels"]
```
"""

# ── CHAPTER 29 ENRICHMENTS: AUTOENCODERS & IMAGE DENOISING ────────────
ch29_extra = r"""
# 29.41 Worked Example — 10-Mark University Model Answer: Convolutional Autoencoder Denoising & Loss Formulations
### Problem Statement
A medical radiography department implements an unsupervised deep learning pipeline for denoising low-dose CT and X-ray images. A Convolutional Autoencoder (CAE) takes a noise-corrupted image $\tilde{x} = x + n$ and reconstructs pristine estimate $\hat{x} = g_\theta(f_\phi(\tilde{x}))$.
1. Diagram and explain the structural roles of the **Encoder**, the **Latent Bottleneck ($z$)**, and the **Decoder**.
2. Explain why a bottleneck constraint ($\dim(z) \ll \dim(x)$) is mathematically essential to prevent trivial identity mapping.
3. Formulate the Mean Squared Error (MSE) reconstruction loss function for a training batch of $N$ images of size $W \times H$.
4. Contrast the denoising mechanism of an Autoencoder with classical spatial filters (Bilateral Filter and Wiener Filter).
5. Suppose an input image $x$ has pixel variance $\sigma_x^2 = 0.08$ and additive Gaussian noise has variance $\sigma_n^2 = 0.02$. The pristine pixel at coordinate $(10, 10)$ is $x(10,10) = 0.70$ and corrupted pixel is $\tilde{x}(10,10) = 0.88$. If the trained autoencoder outputs $\hat{x}(10,10) = 0.72$, compute the individual squared error before and after denoising.

### Step-by-Step Mathematical Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. Architectural Components of a Denoising Autoencoder:</strong><br>
  - <strong>Encoder ($z = f_\phi(\tilde{x})$):</strong> Successive convolutional and downsampling pooling layers that compress the high-dimensional noisy input $\tilde{x} \in \mathbb{R}^{H \times W \times C}$ into a compact, low-dimensional latent feature vector $z \in \mathbb{R}^d$.<br>
  - <strong>Latent Bottleneck ($z$):</strong> A low-dimensional manifold representation. Because $d \ll H \cdot W \cdot C$, high-frequency uncorrelated noise cannot fit through the information bottleneck.<br>
  - <strong>Decoder ($\hat{x} = g_\theta(z)$):</strong> Successive transposed convolutional (deconvolution) or bilinear upsampling layers that reconstruct the clean image $\hat{x} \in \mathbb{R}^{H \times W \times C}$ from the latent code $z$.</p>

  <p><strong>2. Mathematical Necessity of the Bottleneck:</strong><br>
  If an autoencoder had unconstrained capacity ($\dim(z) \ge \dim(x)$), the network could easily learn the trivial identity function $f(x) = x$ by simply copying corrupted input pixels directly to the output. By enforcing an <strong>information bottleneck</strong>, the network is forced to learn the true underlying data manifold—retaining salient visual structures (edges, textures, anatomical shapes) while filtering out uncorrelated stochastic noise perturbations.</p>

  <p><strong>3. Reconstruction Loss Function Formulation:</strong><br>
  For a batch of $N$ images, each of spatial dimensions $H \times W$ with $C$ channels:
  $$\mathcal{L}_{MSE}(\theta, \phi) = \frac{1}{N \cdot H \cdot W \cdot C} \sum_{i=1}^N \sum_{h=1}^H \sum_{w=1}^W \sum_{c=1}^C \left( x_{i,h,w,c} - \hat{x}_{i,h,w,c} \right)^2$$
  <strong>Critical Training Detail:</strong> The loss is computed between the network's reconstruction $\hat{x} = g_\theta(f_\phi(\tilde{x}))$ and the <strong>original pristine image $x$</strong> (NOT the noisy input $\tilde{x}$). This forces the gradient descent optimization to penalize the residual noise.</p>

  <p><strong>4. Autoencoders vs Classical Spatial Filters:</strong></p>
  <div class="table-wrap">
    <table class="comparison-table">
      <thead>
        <tr><th>Dimension</th><th>Bilateral Filter</th><th>Wiener Filter</th><th>Denoising Autoencoder (CAE)</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Mathematical Principle</strong></td><td>Non-linear range and spatial Gaussian weighting</td><td>Minimum Mean Square Error (MMSE) in frequency domain</td><td>Deep non-linear manifold projection via neural optimization</td></tr>
        <tr><td><strong>Noise Prior</strong></td><td>Assumes local photometric smoothness</td><td>Requires known noise power spectral density $S_\eta(u,v)$</td><td>Learns arbitrary noise distributions from training data</td></tr>
        <tr><td><strong>Edge Preservation</strong></td><td>Preserves sharp step edges; blurs textures</td><td>Blurs edges due to linear low-pass nature</td><td>Learns semantic edges and high-frequency textures simultaneously</td></tr>
        <tr><td><strong>Adaptability</strong></td><td>Static hand-crafted parameters ($\sigma_s, \sigma_r$)</td><td>Linear stationary assumption</td><td>Adapts dynamically to complex semantic scene priors</td></tr>
      </tbody>
    </table>
  </div>

  <p><strong>5. Numerical Error Reduction Trace:</strong><br>
  - Pristine ground truth: $x = 0.70$.<br>
  - Corrupted input: $\tilde{x} = 0.88 \implies \text{Initial Squared Error } e_{\text{noisy}}^2 = (0.88 - 0.70)^2 = (0.18)^2 = \mathbf{0.0324}$.<br>
  - Autoencoder output: $\hat{x} = 0.72 \implies \text{Denoised Squared Error } e_{\text{denoised}}^2 = (0.72 - 0.70)^2 = (0.02)^2 = \mathbf{0.0004}$.<br>
  $$\text{Error Reduction} = \frac{0.0324 - 0.0004}{0.0324} = \frac{0.0320}{0.0324} \approx \mathbf{98.77\% \text{ noise variance removed!}}$$</p>
</div>

# 29.42 Denoising Autoencoder Information Flow
```mermaid
graph LR
    Clean["Clean Image x"] -.-> Noise["Additive Noise +n"]
    Noise --> Corrupt["Noisy Image x̃"]
    Corrupt --> Enc["Encoder Network<br>Conv + Downsampling"]
    Enc --> Latent["Latent Bottleneck z<br>Compressed Representation"]
    Latent --> Dec["Decoder Network<br>Transposed Conv + Upsampling"]
    Dec --> Reconstruct["Clean Reconstruction x̂"]
    Clean --> Loss["MSE Loss: ||x - x̂||²"]
    Reconstruct --> Loss
```
"""

# ── CHAPTER 30 ENRICHMENTS: VIDEO PROCESSING & OPTICAL FLOW ───────────
ch30_extra = r"""
# 30.43 Worked Example — 10-Mark University Model Answer: Optical Flow Equation & Lucas-Kanade Solution
### Problem Statement
In video motion analysis and object tracking, motion between consecutive frames $I(x,y,t)$ and $I(x,y,t+\Delta t)$ is modeled by the 2D apparent velocity vector $v = [u, v]^T = \left[ \frac{dx}{dt}, \frac{dy}{dt} \right]^T$.
1. State the **Brightness Constancy Assumption** and derive the fundamental **Optical Flow Constraint Equation** using first-order Taylor series expansion.
2. Explain why a single equation with two unknowns $(u, v)$ leads to the **Aperture Problem**.
3. Formulate the **Lucas-Kanade method**: state its key spatial coherence assumption and derive the normal equations in matrix form $A^T A v = A^T b$.
4. Under what conditions is the Lucas-Kanade system invertible and reliable? Connect this directly to the Harris Corner spatial structure matrix.
5. In a $3 \times 3$ window centered at pixel $(x_0, y_0)$, the evaluated spatio-temporal derivatives yield the following sums:
   $$\sum I_x^2 = 25, \qquad \sum I_y^2 = 16, \qquad \sum I_x I_y = 5, \qquad \sum I_x I_t = -30, \qquad \sum I_y I_t = -14$$
   Compute the exact apparent velocity vector $[u, v]^T$.

### Step-by-Step Mathematical Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. Derivation of the Optical Flow Constraint Equation:</strong><br>
  - <strong>Brightness Constancy Assumption:</strong> The intensity of a physical scene point remains constant as it moves over a small time increment $\Delta t$:
    $$I(x + \Delta x, y + \Delta y, t + \Delta t) = I(x, y, t)$$
  - Expanding the left-hand side in a first-order Taylor series around $(x, y, t)$:
    $$I(x + \Delta x, y + \Delta y, t + \Delta t) \approx I(x, y, t) + \frac{\partial I}{\partial x} \Delta x + \frac{\partial I}{\partial y} \Delta y + \frac{\partial I}{\partial t} \Delta t$$
  - Substituting into the constancy equation:
    $$I(x, y, t) + I_x \Delta x + I_y \Delta y + I_t \Delta t = I(x, y, t) \implies I_x \Delta x + I_y \Delta y + I_t \Delta t = 0$$
  - Dividing throughout by $\Delta t$ and taking the limit as $\Delta t \to 0$:
    $$I_x \frac{dx}{dt} + I_y \frac{dy}{dt} + I_t = 0 \iff \mathbf{I_x u + I_y v + I_t = 0} \iff \nabla I^T \mathbf{v} = -I_t$$
  where $I_x, I_y$ are spatial intensity gradients, $I_t$ is temporal frame difference, and $u, v$ are optical flow velocity components.</p>

  <p><strong>2. The Aperture Problem:</strong><br>
  At any single pixel, the optical flow constraint is a single linear scalar equation in two unknowns $(u, v)$. This means we can only determine the velocity component <strong>parallel to the image gradient</strong> (normal flow $v_\perp$). The velocity component orthogonal to the gradient (tangential flow $v_\parallel$) is completely undetectable through a narrow local aperture (e.g. observing an edge through a small circle cannot distinguish diagonal motion from vertical motion).</p>

  <p><strong>3. Lucas-Kanade Matrix Formulation:</strong><br>
  - <strong>Spatial Coherence Assumption:</strong> Lucas-Kanade assumes that velocity $v = [u, v]^T$ is constant across a small local window of $n$ pixels (e.g. $3 \times 3$ window, $n = 9$).<br>
  - For $n$ pixels $p_1, p_2, \dots, p_n$, this yields an overdetermined system of $n$ equations:
    $$\begin{bmatrix} I_x(p_1) & I_y(p_1) \\ I_x(p_2) & I_y(p_2) \\ \vdots & \vdots \\ I_x(p_n) & I_y(p_n) \end{bmatrix} \begin{bmatrix} u \\ v \end{bmatrix} = - \begin{bmatrix} I_t(p_1) \\ I_t(p_2) \\ \vdots \\ I_t(p_n) \end{bmatrix} \iff A \mathbf{v} = b$$
  - Solving via the standard Least Squares Normal Equations:
    $$A^T A \mathbf{v} = A^T b \implies \begin{bmatrix} \sum I_x^2 & \sum I_x I_y \\ \sum I_x I_y & \sum I_y^2 \end{bmatrix} \begin{bmatrix} u \\ v \end{bmatrix} = - \begin{bmatrix} \sum I_x I_t \\ \sum I_y I_t \end{bmatrix}$$</p>

  <p><strong>4. Invertibility Condition and Harris Corner Connection:</strong><br>
  The system has a unique, stable solution if and only if the matrix $M = A^T A$ is non-singular and well-conditioned:
  - Both eigenvalues $\lambda_1, \lambda_2$ of $M$ must be strictly positive and sufficiently large ($\lambda_1 \ge \lambda_2 > \epsilon$).<br>
  - Notice that $M = \begin{bmatrix} \sum I_x^2 & \sum I_x I_y \\ \sum I_x I_y & \sum I_y^2 \end{bmatrix}$ is <strong>identical to the Harris Corner structure tensor</strong>!
  - <strong>Physical Meaning:</strong> Optical flow can be solved reliably at corners and textured regions (where gradients exist in multiple directions). It fails on flat regions ($\lambda_1 \approx \lambda_2 \approx 0$) and along straight edges ($\lambda_1 \gg \lambda_2 \approx 0$).</p>

  <p><strong>5. Numerical Computation of Apparent Velocity:</strong><br>
  Given:
  $$M = A^T A = \begin{bmatrix} 25 & 5 \\ 5 & 16 \end{bmatrix}, \qquad A^T b = - \begin{bmatrix} -30 \\ -14 \end{bmatrix} = \begin{bmatrix} 30 \\ 14 \end{bmatrix}$$
  - Determinant of $M$:
    $$\det(M) = (25 \times 16) - (5 \times 5) = 400 - 25 = \mathbf{375}$$
    Since $\det(M) = 375 \neq 0$, the matrix is invertible.
  - Matrix inverse $M^{-1}$:
    $$M^{-1} = \frac{1}{375} \begin{bmatrix} 16 & -5 \\ -5 & 25 \end{bmatrix}$$
  - Solving for velocity $\mathbf{v} = [u, v]^T$:
    $$\begin{bmatrix} u \\ v \end{bmatrix} = \frac{1}{375} \begin{bmatrix} 16 & -5 \\ -5 & 25 \end{bmatrix} \begin{bmatrix} 30 \\ 14 \end{bmatrix} = \frac{1}{375} \begin{bmatrix} (16 \times 30) + (-5 \times 14) \\ (-5 \times 30) + (25 \times 14) \end{bmatrix}$$
    $$u = \frac{480 - 70}{375} = \frac{410}{375} \approx \mathbf{+1.0933 \text{ pixels/frame}}$$
    $$v = \frac{-150 + 350}{375} = \frac{200}{375} \approx \mathbf{+0.5333 \text{ pixels/frame}}$$
  The feature is moving rightward at $1.09$ px/frame and downward at $0.53$ px/frame.</p>
</div>

# 30.44 Practical Lab 10: Complete Motion Tracking Pipeline in OpenCV
```python
import cv2
import numpy as np

# Shi-Tomasi Corner Detector Parameters
feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)

# Lucas-Kanade Optical Flow Parameters
lk_params = dict(winSize=(15, 15), maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Initialize Camera Stream or Video Capture
cap = cv2.VideoCapture(0)

# Read First Frame and Find Good Tracking Features
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

# Create Canvas Mask for Drawing Tracking Trajectories
mask = np.zeros_like(old_frame)

while True:
    ret, frame = cap.read()
    if not ret: break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate Optical Flow via Lucas-Kanade
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    # Select Valid Tracking Points
    if p1 is not None:
        good_new = p1[st == 1]
        good_old = p0[st == 1]

        # Draw Motion Vectors / Trajectory Trails
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel().astype(int)
            c, d = old.ravel().astype(int)
            mask = cv2.line(mask, (a, b), (c, d), (0, 255, 0), 2)
            frame = cv2.circle(frame, (a, b), 5, (0, 0, 255), -1)

        img = cv2.add(frame, mask)
        cv2.imshow('DIP Lab 10 - Lucas-Kanade Optical Flow Tracking', img)

    # Update Previous Frame and Points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)

    if cv2.waitKey(30) & 0xFF == 27: break

cap.release()
cv2.destroyAllWindows()
```
"""

# ── CHAPTER 31 ENRICHMENTS: ENGINEERING APPLICATIONS & SYNTHESIS ──────
ch31_extra = r"""
# 31.42 Worked Example — 10-Mark University Model Answer: Medical & Remote Sensing Imaging Pipeline Design
### Problem Statement
As a lead Computer Vision Engineer, you are tasked with designing complete digital image processing and analysis systems for two mission-critical domains:
1. **Domain A (Medical Radiography — CT Pulmonary Lesion Detection):**
   - Explain the physical meaning and calibration of the **Hounsfield Unit (HU)** scale:
     $$HU = 1000 \times \frac{\mu - \mu_{\text{water}}}{\mu_{\text{water}} - \mu_{\text{air}}}$$
   - Contrast the windowing and leveling settings used for viewing bone structures ($W = 2000, L = 500$) versus lung parenchyma ($W = 1500, L = -600$).
   - Formulate the 5-stage automated tumor segmentation pipeline: Preprocessing $\to$ Morphological Filtering $\to$ Active Contours / U-Net Segmentation $\to$ Radiomic Feature Extraction $\to$ Diagnostic Classification.
2. **Domain B (Satellite Remote Sensing — Multispectral Environmental Monitoring):**
   - State the physical rationale for combining Red and Near-Infrared (NIR) spectral bands.
   - Formulate the **Normalized Difference Vegetation Index (NDVI)** and explain why healthy photosynthetic vegetation exhibits high positive values ($0.6 \le NDVI \le 0.9$) while water exhibits negative values.
   - For a satellite pixel recording reflectance values $\rho_{\text{NIR}} = 0.72$ and $\rho_{\text{Red}} = 0.08$, compute the exact NDVI and classify the ground landcover.
3. **Engineering Ethics & Responsible Vision AI:** State three critical ethical concerns in computer vision deployments (algorithmic bias, deepfake manipulation, biometric privacy) and their corresponding engineering mitigation safeguards.

### Step-by-Step Mathematical Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. Domain A: Medical CT Imaging Principles & Windowing:</strong><br>
  - <strong>Hounsfield Scale Definition:</strong> Measures radiodensity of tissues relative to distilled water ($\mu_{\text{water}}$) and air ($\mu_{\text{air}} \approx 0$):
    - Air: $HU = -1000$ (radiotransparent)
    - Fat: $HU \in [-120, -90]$
    - Water: $HU = 0$ (reference calibrator)
    - Soft Tissue / Muscle: $HU \in [+40, +80]$
    - Dense Cortical Bone: $HU \in [+1000, +3000]$ (radiopaque)<br>
  - <strong>Windowing / Leveling Transformation:</strong> A raw 12-bit or 16-bit CT scan contains 4096+ gray levels, whereas human vision can only distinguish ~64 levels. Windowing maps an interval $[L - W/2, L + W/2]$ linearly to display intensities $[0, 255]$:
    $$f_{disp}(x) = \begin{cases} 0 & x < L - W/2 \\ 255 \times \frac{x - (L - W/2)}{W} & L - W/2 \le x \le L + W/2 \\ 255 & x > L + W/2 \end{cases}$$
    - <strong>Lung Window ($W = 1500, L = -600$):</strong> Focuses on range $[-1350, +150]$ to clearly resolve low-density alveolar parenchyma and bronchial trees.<br>
    - <strong>Bone Window ($W = 2000, L = +500$):</strong> Focuses on range $[-500, +1500]$ to distinguish cortical fracture lines without saturation.</p>

  <p><strong>2. Domain B: Multispectral Satellite Remote Sensing & NDVI:</strong><br>
  - <strong>Chlorophyll Biophysical Rationale:</strong> Healthy green vegetation strongly absorbs Red light ($\lambda \approx 660 \text{ nm}$) for photosynthesis via chlorophyll pigments, while spongy mesophyll leaf cells strongly reflect and scatter Near-Infrared radiation ($\lambda \approx 860 \text{ nm}$) to avoid overheating.<br>
  - <strong>NDVI Mathematical Formula:</strong>
    $$NDVI = \frac{\rho_{\text{NIR}} - \rho_{\text{Red}}}{\rho_{\text{NIR}} + \rho_{\text{Red}}}$$
    $NDVI$ normalizes illumination changes and ranges strictly between $-1.0$ and $+1.0$.<br>
  - <strong>Numerical Computation for Pixel ($\rho_{\text{NIR}} = 0.72, \rho_{\text{Red}} = 0.08$):</strong>
    $$NDVI = \frac{0.72 - 0.08}{0.72 + 0.08} = \frac{0.64}{0.80} = \mathbf{+0.80}$$
    <strong>Landcover Classification:</strong> $NDVI = +0.80$ corresponds unambiguously to <strong>Dense, Highly Active Photosynthetic Forest Canopy / Healthy Agriculture</strong>.</p>

  <p><strong>3. Engineering Ethics & Responsible Computer Vision:</strong></p>
  <div class="table-wrap">
    <table class="comparison-table">
      <thead>
        <tr><th>Ethical Vulnerability</th><th>Societal / Operational Impact</th><th>Engineering Mitigation Safeguard</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Algorithmic Demographic Bias</strong></td><td>Facial recognition systems exhibit dramatically higher false-positive rates on underrepresented demographic groups</td><td>Balanced stratified dataset curation, adversarial debiasing, and demographic parity constraint validation</td></tr>
        <tr><td><strong>Deepfake Synthetic Media</strong></td><td>Malicious video synthesis and identity theft undermining institutional and personal trust</td><td>Frequency-domain artifact detection (abnormal Fourier phase coherence), eye-blink physiological cadence verification</td></tr>
        <tr><td><strong>Biometric Privacy & Surveillance</strong></td><td>Pervasive tracking of citizens in public spaces without consent or oversight</td><td>Privacy-by-design edge processing, automated real-time face redaction/blurring, and strict cryptographic audit logs</td></tr>
      </tbody>
    </table>
  </div>
</div>

# 31.43 The Complete 31-Chapter Digital Image Processing Grand Architecture
```mermaid
graph TD
    subgraph Part1["Part I: The Image (C01-C05)"]
        Physics["Photon Acquisition & Sampling"] --> Representation["Matrix/Tensor Representations"]
    end
    subgraph Part2["Part II: Improving the Image (C06-C14)"]
        Spatial["Spatial Enhancement & Filtering"] --> Frequency["Fourier Transform & Restoration"]
    end
    subgraph Part3["Part III: Understanding Content (C15-C20)"]
        Segment["Segmentation & Morphology"] --> Descriptors["Feature Descriptors: SIFT, HOG"]
    end
    subgraph Part4["Part IV: Compressing Images (C21-C24)"]
        Entropy["Information Theory & Huffman"] --> JPEG["DCT & JPEG Standard"]
    end
    subgraph Part5["Part V: Intelligent Vision (C25-C31)"]
        Deep["CNNs, ResNet & YOLO"] --> Video["Optical Flow & Motion Tracking"]
        Video --> Apps["Medical, Satellite & Ethical Vision Systems"]
    end

    Part1 --> Part2
    Part2 --> Part3
    Part3 --> Part4
    Part4 --> Part5
```
"""

# Map chapters to extra content
EXTRA_CONTENT = {
    25: ch25_extra,
    26: ch26_extra,
    27: ch27_extra,
    28: ch28_extra,
    29: ch29_extra,
    30: ch30_extra,
    31: ch31_extra,
}

def main():
    print("=" * 70)
    print("  DIP MINIBOOK — PART V MASTER ENRICHMENT & COMPILATION SUITE")
    print("  Compiling Chapters 25 to 31 (Intelligent Vision & Master Curriculum)")
    print("=" * 70)

    part5_chapters = [m for m in CHAPTERS_META if m['chapter_num'] in range(25, 32)]
    print(f"Discovered {len(part5_chapters)} chapters in Part V metadata.")

    for meta in part5_chapters:
        ch_num = meta['chapter_num']
        extra = EXTRA_CONTENT.get(ch_num, "")
        print(f"\n[Compiling Chapter {ch_num:02d}]: {meta['title']}...")
        output_path = build_enriched_chapter(meta, extra)
        print(f"  ✓ Chapter {ch_num:02d} written successfully to: {os.path.basename(output_path)}")

    # Recompile Chapter 24 to update its 'next' link to Chapter 25
    print("\n[Resealing Chapter 24]: Linking forward to Chapter 25...")
    ch24_meta = [m for m in CHAPTERS_META if m['chapter_num'] == 24][0]
    from enrich_part4 import ch24_extra
    ch24_path = build_enriched_chapter(ch24_meta, ch24_extra)
    print(f"  ✓ Chapter 24 resealed with link to: {ch24_meta['next_link']}")

    print("\n" + "=" * 70)
    print("  ALL PART V CHAPTERS COMPILED & SEALED SUCCESSFULLY!")
    print("=" * 70)

if __name__ == '__main__':
    main()
