---
id: "C27"
title: "VGG and ResNet"
layer: "MAIN"
part: "V — From DIP to Intelligent Vision"
unit: "Unit IV"
version: "1.0"
status: "PRODUCTION"
syllabus_scope: "Pretrained Models (VGG, ResNet, YOLO) — VGG and ResNet"
tags:
  - digital-image-processing
  - deep-learning
  - cnn
  - vgg
  - resnet
  - pretrained-models
  - transfer-learning
prerequisites:
  - "C25 — Image Classification"
  - "C26 — Convolutional Neural Networks"
related_math:
  - "Convolution"
  - "Tensor shapes"
  - "Parameter count"
  - "Residual addition"
related_lab:
  - "LAB-08 — CNN-Based Image Classification"
  - "LAB-09 — Object Detection using YOLO"
related_code:
  - "CODE-08 — CNN / Pretrained Model Inference"
related_exam:
  - "EXAM-VGG-ResNet"
related_practice:
  - "PRACTICE-Architectures"
---

# C27 — VGG and ResNet

> **Chapter thesis:** VGG and ResNet demonstrate two major ways of scaling CNNs—systematic depth with small filters in VGG, and residual learning in ResNet to make very deep networks easier to optimize.

---

# 1. Why This Chapter Exists

The syllabus explicitly names:

- pretrained models;
- VGG;
- ResNet;
- YOLO. fileciteturn4file0L48-L52

C26 explained the basic CNN building blocks.

C27 now asks:

> **What happens when a CNN becomes much deeper and more systematic?**

Two architectures are especially useful for learning this:

```text
VGG
→ disciplined stacking of small convolutions

ResNet
→ residual / skip connections
```

The purpose is not to memorize every layer of every model variant.

The goal is to understand the architectural ideas that made these families important.

---

# 2. Learning Contract

After this chapter, you should be able to:

- explain why CNN depth matters;
- describe the core VGG design idea;
- explain the use of repeated small convolution kernels in VGG;
- distinguish VGG family variants conceptually;
- explain why deeper networks can become difficult to train;
- describe the degradation problem;
- explain residual learning;
- explain the identity shortcut;
- trace tensor shapes through a simple residual block;
- calculate the output of a residual addition;
- compare VGG and ResNet;
- explain the meaning of “pretrained model”;
- explain transfer learning at an introductory level;
- choose between a simple CNN, VGG-style model, and ResNet-style model for an engineering scenario.

---

# 3. From CNN to CNN Architecture

C26 introduced a generic architecture:

```text
image
 ↓
convolution
 ↓
activation
 ↓
pooling
 ↓
convolution
 ↓
activation
 ↓
classification
```

Architecture design determines:

- how many layers are used;
- how feature dimensions change;
- how channels grow;
- where downsampling occurs;
- how information flows through the network.

VGG and ResNet are therefore not new mathematical universes.

They are carefully engineered arrangements of CNN components.

---

# 4. Why Make a CNN Deeper?

A deeper network can represent more complex hierarchical functions.

Conceptually:

```text
shallow
pixels
→ simple patterns
→ class

deep
pixels
→ edges
→ motifs
→ parts
→ larger structures
→ class evidence
```

But depth introduces optimization challenges.

Adding more layers does not automatically improve performance.

---

# 5. The Depth Problem

Suppose we progressively increase network depth:

```text
10 layers
20 layers
30 layers
40 layers
...
```

A naive expectation is:

> More layers should always make the training error smaller.

In practice, very deep plain networks can become difficult to optimize.

Problems may include:

- vanishing gradients;
- exploding gradients;
- optimization difficulty;
- degradation of training accuracy;
- increased computational and memory requirements.

This motivated architectural solutions rather than simply adding more layers.

---

# 6. VGG — The Central Idea

The VGG family is known for a relatively simple, systematic architecture built largely from:

```text
small 3×3 convolutions
+
ReLU
+
pooling
+
progressively deeper blocks
```

Instead of mixing many unusual convolution sizes, the architecture emphasizes repeated small kernels.

Conceptually:

```text
Input
 ↓
3×3 Conv
 ↓
3×3 Conv
 ↓
Pool
 ↓
3×3 Conv
 ↓
3×3 Conv
 ↓
Pool
 ↓
...
 ↓
Classifier
```

This regularity makes VGG easier to study than many highly specialized architectures.

---

# 7. Why 3×3 Kernels?

A 3×3 kernel provides a local spatial neighbourhood:

```text
■ ■ ■
■ ■ ■
■ ■ ■
```

Two stacked 3×3 convolutions have a larger effective receptive field than one 3×3 convolution.

Under a simple stride-1 reasoning:

```text
3×3
 →
effective 5×5 after two layers
```

while using fewer weights than a dense 5×5 layer with the same channel dimensions, depending on the architecture.

---

# 8. Parameter Comparison — 3×3 vs 5×5

Suppose one input channel and one output channel for simplicity.

A 5×5 kernel requires:

\[
5\times5=25
\]

weights.

Two 3×3 kernels require:

\[
3\times3 + 3\times3
=
18
\]

weights, ignoring biases and intermediate channels.

The comparison becomes architecture-dependent when channels are included, but the basic lesson is:

> **Stacked small kernels can achieve larger receptive fields while introducing more nonlinear processing between layers.**

---

# 9. Small Kernels and Nonlinearity

Two 3×3 convolution layers with ReLU between them are not equivalent to one 5×5 convolution.

The deeper arrangement contains an extra nonlinear transformation:

```text
3×3
 ↓
ReLU
 ↓
3×3
 ↓
ReLU
```

This increases representational flexibility.

That is one of the important architectural ideas behind VGG-style networks.

---

# 10. VGG Block Structure

A typical VGG-style pattern is:

```text
Convolution
Convolution
Pooling
```

followed by deeper blocks with more channels.

The overall trend is often:

```text
spatial dimensions ↓
channel count ↑
```

For example:

```text
224×224×64
      ↓
112×112×128
      ↓
56×56×256
      ↓
28×28×512
      ↓
14×14×512
```

Exact dimensions depend on the particular variant and layer configuration.

---

# 11. VGG Variants

Common names include:

- VGG-11
- VGG-13
- VGG-16
- VGG-19

The number broadly reflects the depth convention used to name the architecture family.

The important syllabus-level insight is not to memorize every layer.

Understand:

```text
VGG-11
VGG-13
VGG-16
VGG-19
     ↓
increasing depth within the family
```

---

# 12. VGG-16 Conceptual Anatomy

A simplified VGG-16-style progression can be visualized as:

```text
Input
 ↓
Conv block
 ↓
Conv block
 ↓
Conv block
 ↓
Conv block
 ↓
Conv block
 ↓
classifier
```

Within blocks, 3×3 convolutions are repeatedly stacked.

Pooling reduces spatial dimensions.

Later stages operate on smaller spatial grids with more feature channels.

---

# 13. VGG Tensor Evolution

A simplified example:

| Stage | Spatial size | Channels |
|---|---:|---:|
| Input | 224×224 | 3 |
| Early features | 224×224 | 64 |
| Pool | 112×112 | 64 |
| Next block | 112×112 | 128 |
| Pool | 56×56 | 128 |
| Next block | 56×56 | 256 |
| Pool | 28×28 | 256 |
| Deep block | 28×28 | 512 |
| Pool | 14×14 | 512 |

The exact final classification head varies across implementations.

This table teaches the architectural pattern rather than one implementation contract.

---

# 14. Why Channels Increase

Early layers detect relatively simple local patterns.

As the spatial dimensions shrink, the network can allocate more channels to represent increasingly diverse features.

Conceptually:

```text
large image
+
few channels
        ↓
smaller image
+
more channels
        ↓
compact but rich representation
```

This is a common CNN design pattern, not something unique to VGG.

---

# 15. VGG Strengths

VGG's major educational and historical strengths include:

- simple regular structure;
- repeated small convolutions;
- easy-to-understand hierarchy;
- strong feature extraction capability;
- useful pretrained weights.

Its simplicity makes it excellent for architecture teaching.

---

# 16. VGG Limitations

VGG is relatively heavy compared with many later architectures.

Potential costs include:

- large parameter count;
- high memory usage;
- substantial computation;
- slower inference relative to more efficient modern models.

Therefore:

> **A historically important model is not automatically the best deployment model.**

---

# 17. What Does “Pretrained” Mean?

A pretrained model has parameters learned previously from a large training task/dataset.

Instead of starting from random initialization:

```text
random weights
→ train on your dataset
```

you can use:

```text
pretrained weights
→ adapt/fine-tune for your task
```

This can be especially useful when your dataset is smaller than the datasets typically used to train large vision models from scratch.

---

# 18. Transfer Learning

A typical transfer-learning idea is:

```text
large source dataset
        ↓
pretrained feature extractor
        ↓
target dataset
        ↓
new classifier / fine-tuning
```

Early learned filters can provide useful generic visual features.

The exact effectiveness depends on how similar the source and target domains are.

---

# 19. Frozen vs Fine-Tuned

### Frozen feature extractor

Keep pretrained parameters fixed:

```text
pretrained backbone
→ frozen
→ new classification head
```

### Fine-tuning

Allow some or all pretrained parameters to update:

```text
pretrained backbone
→ selected layers trainable
→ adapt to target dataset
```

Fine-tuning can improve specialization but increases the risk of overfitting when the target dataset is small.

---

# 20. Why ResNet?

The deeper plain-CNN problem led to a crucial architectural question:

> How can we make very deep networks easier to optimize?

ResNet introduced **residual learning**.

Instead of forcing stacked layers to directly learn:

\[
H(x),
\]

the block learns a residual:

\[
F(x)=H(x)-x.
\]

The block output becomes:

\[
\boxed{y=F(x)+x}.
\]

The \(x\) path is the **shortcut** or **skip connection**.

---

# 21. Residual Block

The simplest conceptual residual block is:

```text
              ┌──────────────────────┐
              │                      │
x ────────────┼──────────────────────┤
│             │                      │
│        Conv → ReLU → Conv          │
│             │                      │
└─────────────┴──────── Add ◄────────┘
                        │
                        ▼
                        y
```

Mathematically:

\[
y=F(x)+x.
\]

The network learns the residual correction \(F(x)\) rather than the entire mapping directly.

---

# 22. Identity Shortcut

In the simplest residual block:

\[
\operatorname{shortcut}(x)=x.
\]

The shortcut performs an identity mapping.

This gives information a direct path through the network.

The output is:

\[
y=F(x)+x.
\]

If the residual branch learns values close to zero:

\[
F(x)\approx0,
\]

then:

\[
y\approx x.
\]

This makes the block capable of behaving approximately like an identity mapping.

---

# 23. Why Residual Learning Helps

Consider a deeper network trying to preserve a useful representation.

A plain stack has to learn:

\[
H(x).
\]

A residual block can instead learn:

\[
F(x)=H(x)-x.
\]

If the desired mapping is close to identity, learning:

\[
F(x)\approx0
\]

may be easier than learning:

\[
H(x)\approx x
\]

from scratch through a sequence of nonlinear transformations.

This is the core intuition behind residual learning.

---

# 24. Residual Addition — Worked Example

Suppose:

\[
x=
\begin{bmatrix}
1\\2\\3
\end{bmatrix}
\]

and the residual branch produces:

\[
F(x)=
\begin{bmatrix}
0.5\\-1\\2
\end{bmatrix}.
\]

Then:

\[
y=F(x)+x.
\]

Therefore:

\[
y=
\begin{bmatrix}
0.5+1\\
-1+2\\
2+3
\end{bmatrix}
\]

\[
=
\boxed{
\begin{bmatrix}
1.5\\1\\5
\end{bmatrix}
}.
\]

This is the essential arithmetic of a residual block.

---

# 25. Shape Compatibility

The addition:

\[
F(x)+x
\]

requires compatible shapes.

If:

```text
F(x) → H×W×64
x    → H×W×64
```

element-wise addition is straightforward.

But what if:

```text
F(x) → H/2 × W/2 × 128
x    → H × W × 64
```

?

They cannot be directly added.

The shortcut therefore needs a transformation.

---

# 26. Projection Shortcut

When shapes differ, a learned projection can be used:

```text
x
 ↓
1×1 convolution
 ↓
matching shape
 ↓
add with F(x)
```

Conceptually:

\[
y=F(x)+W_sx.
\]

where \(W_s\) is the shortcut projection.

The 1×1 convolution can change channel count and, with stride, spatial dimensions.

---

# 27. Why 1×1 Convolution Helps

A 1×1 convolution can mix channel information without directly looking across neighbouring spatial positions.

It can therefore:

```text
change number of channels
+
allow controlled projection
```

while maintaining the spatial location structure.

It is useful both inside modern CNN architectures and for residual projection shortcuts.

---

# 28. Residual Block with Projection

Conceptually:

```text
                ┌───────────────────────────┐
                │                           │
x ──────────────┼──── 1×1 projection ───────┤
│               │                           │
│          Conv → ReLU → Conv               │
│               │                           │
└───────────────┴──────── Add ◄─────────────┘
                              │
                              ▼
                              y
```

Again:

\[
y=F(x)+W_sx.
\]

---

# 29. Batch Normalization — Architectural Context

Many classic ResNet descriptions include batch normalization in the residual branches.

The exact ordering depends on the ResNet variant and implementation.

Conceptually:

```text
Convolution
→ normalization
→ activation
```

may appear inside a residual block.

Do not memorize one universal sequence as “the ResNet block.”

Different variants include different block arrangements.

---

# 30. ResNet Depth Variants

Common model names include:

- ResNet-18
- ResNet-34
- ResNet-50
- ResNet-101
- ResNet-152

The numbers indicate increasing network depth according to the family definition.

A useful conceptual split is:

```text
ResNet-18 / 34
→ basic residual blocks

ResNet-50 / 101 / 152
→ bottleneck residual blocks
```

The exact implementation details differ.

---

# 31. Basic Residual Block

A simplified basic block:

```text
3×3 Conv
 ↓
Normalization
 ↓
ReLU
 ↓
3×3 Conv
 ↓
Normalization
 ↓
Add shortcut
 ↓
ReLU
```

This form is associated with shallower classic ResNet variants.

---

# 32. Bottleneck Block

A bottleneck block uses:

```text
1×1
 ↓
3×3
 ↓
1×1
```

conceptually.

The 1×1 operations can reduce and then expand channel dimensions.

This allows very deep networks to have manageable computation compared with simply stacking many wide 3×3 convolutions.

---

# 33. VGG vs ResNet — Core Comparison

| Property | VGG | ResNet |
|---|---|---|
| Main idea | Deep stack of small convolutions | Residual/skip connections |
| Typical kernels | Mostly 3×3 | 3×3 plus 1×1 in bottlenecks |
| Information path | Sequential | Sequential + shortcuts |
| Very deep training | Becomes expensive/difficult | Residual design improves optimization |
| Parameter efficiency | Relatively heavy | Often more efficient for comparable depth/task |
| Architecture complexity | Relatively simple | More structured block design |
| Historical significance | Systematic deep CNN design | Enabled practical very deep CNNs |

The exact parameter count depends on the model variant.

---

# 34. A More Useful Comparison: What Problem Does Each Solve?

```text
VGG
→ "How can we build a deep CNN with a simple repeated design?"

ResNet
→ "How can we make very deep networks easier to optimize?"
```

This is a much better way to remember the models than memorizing names only.

---

# 35. VGG and Feature Extraction

In transfer learning, a pretrained VGG backbone can act as:

```text
image
 ↓
VGG feature extractor
 ↓
feature representation
 ↓
new classifier
```

For a new application, the classifier head may be replaced.

This connects C27 directly to C25.

---

# 36. ResNet and Feature Extraction

Similarly:

```text
image
 ↓
ResNet backbone
 ↓
deep feature representation
 ↓
classification / detection / other task head
```

ResNet-style backbones became useful beyond image classification, including detection architectures.

This prepares the transition to C28.

---

# 37. Pretrained Model Workflow

A practical workflow is:

```text
1. Choose pretrained backbone
2. Inspect expected input format
3. Match preprocessing
4. Replace/adapt task head
5. Freeze or fine-tune selected layers
6. Train on target data if needed
7. Validate
8. Evaluate
```

A major practical warning:

> **Preprocessing is part of the model interface.**

Input size, normalization, channel order and expected numeric range must match the pretrained model's requirements.

---

# 38. Pretrained Inference vs Fine-Tuning

### Inference only

```text
pretrained weights
→ image
→ output
```

No training is required.

### Fine-tuning

```text
pretrained weights
→ target data
→ training
→ adapted weights
```

The second method can improve task-specific performance but requires a suitable training pipeline.

---

# 39. Transfer Learning Example

Suppose you have:

```text
5000 images
3 target classes
```

A large CNN trained from scratch may be unnecessarily data-hungry.

A possible strategy:

```text
pretrained ResNet
        ↓
remove original classifier
        ↓
add 3-class head
        ↓
freeze backbone initially
        ↓
train head
        ↓
optionally fine-tune upper layers
```

This is a common engineering pattern.

The exact results depend on domain similarity and data quality.

---

# 40. Input Preprocessing Caveat

A pretrained model might expect:

```text
224×224
RGB
specific normalization
```

If your image is supplied as:

```text
640×480
BGR
0–255
```

and passed directly without correct preprocessing, results may be poor even if the neural network itself is functioning correctly.

This is one of the most common real-world sources of inference mistakes.

---

# 41. Tensor Shape Example — ResNet Input

A typical channels-last input batch could be:

\[
B\times224\times224\times3.
\]

For:

\[
B=8,
\]

the tensor is:

\[
\boxed{8\times224\times224\times3}.
\]

The exact expected input resolution can vary among model variants and implementations.

Always inspect the specific model API.

---

# 42. Model Selection Example

### Scenario A

You need a visually understandable architecture for teaching or debugging.

A VGG-style model is conceptually attractive because its structure is regular.

### Scenario B

You need a deep backbone and care about strong representation capacity with residual connections.

A ResNet-style backbone is a natural candidate.

### Scenario C

You need real-time object detection.

A classification backbone alone is not enough.

That leads to:

\[
\boxed{\text{C28 — Object Detection and YOLO}}
\]

---

# 43. Why ResNet Matters for Detection

Object detection networks often use a backbone to extract visual features.

Conceptually:

```text
image
 ↓
CNN backbone
 ↓
feature maps
 ↓
detection head
 ↓
boxes + classes + confidence
```

ResNet can serve as a backbone in broader vision systems.

This is the bridge between classification and detection.

---

# 44. VGG/ResNet Are Not Detection Algorithms

This distinction is important.

```text
VGG
→ image-classification / feature-extraction architecture family

ResNet
→ image-classification / feature-extraction architecture family

YOLO
→ object-detection architecture family
```

They solve related but different task roles.

---

# 45. Architecture Vocabulary

| Term | Meaning |
|---|---|
| Backbone | Main feature-extraction network |
| Head | Task-specific output layers |
| Block | Reusable group of layers |
| Shortcut | Alternate path around layers |
| Residual | Learned difference/correction |
| Pretrained | Parameters learned on an earlier task/dataset |
| Fine-tuning | Further training pretrained parameters |
| Freeze | Keep selected parameters fixed |
| Bottleneck | Structure that compresses/expands channel representation |

---

# 46. Common Traps

### Trap 1 — ResNet removes convolution.

False.

ResNet is still a CNN family.

### Trap 2 — VGG uses only one convolution layer.

False.

Its defining style involves repeated convolution layers and pooling blocks.

### Trap 3 — Residual learning means ignoring the input.

False.

The input is explicitly added through the shortcut.

### Trap 4 — Every ResNet has exactly the same block.

False.

Different variants use different block structures.

### Trap 5 — Pretrained means permanently fixed.

False.

Weights can be frozen or fine-tuned.

### Trap 6 — More depth always means better performance.

False.

Architecture, optimization, data and compute all matter.

### Trap 7 — VGG and ResNet are object detectors.

Not by themselves.

They are primarily CNN architecture families used for classification/feature extraction and can serve as backbones.

---

# 47. Exam Lens

## 2-mark questions

**What is VGG?**  
A CNN architecture family characterized by systematic stacking of small convolutional layers, especially 3×3 convolutions.

**What is ResNet?**  
A CNN architecture family that uses residual/skip connections to facilitate optimization of deep networks.

**What is a residual connection?**

\[
y=F(x)+x
\]

in the identity-shortcut case.

**What is transfer learning?**  
Reusing knowledge/parameters learned on one task or dataset for another related task.

---

# 48. 5-Mark Question

### Compare VGG and ResNet.

Use:

```text
VGG
→ small repeated convolutions
→ sequential depth
→ simple regular design
→ computationally heavy

ResNet
→ residual blocks
→ shortcut connections
→ improved deep optimization
→ supports very deep variants
```

Conclude with the problem each architecture addresses.

---

# 49. 10-Mark Question

### Explain the ResNet architecture and residual learning.

Recommended structure:

1. motivation for deep CNNs;
2. limitations of plain deep networks;
3. residual formulation;
4. shortcut connection;
5. identity mapping;
6. shape-compatible addition;
7. projection shortcut;
8. basic block;
9. bottleneck block;
10. depth variants;
11. benefits;
12. limitations.

---

# 50. Numerical Practice — Residual Block

Given:

\[
x=
\begin{bmatrix}
2\\3\\5\\
\end{bmatrix}
\]

and:

\[
F(x)=
\begin{bmatrix}
-1\\2\\0
\end{bmatrix},
\]

find:

\[
y=F(x)+x.
\]

Answer:

\[
y=
\boxed{
\begin{bmatrix}
1\\5\\5
\end{bmatrix}
}.
\]

The arithmetic is simple; the important understanding is **why addition is possible**.

---

# 51. Numerical Practice — Convolution Parameters

Suppose a VGG-style layer uses:

- \(3\times3\) kernels;
- 64 input channels;
- 128 output channels.

Parameter count:

\[
3\times3\times64\times128+128.
\]

\[
=73{,}728+128
\]

\[
=\boxed{73{,}856}.
\]

This illustrates why channel count becomes a major computational factor in deep CNNs.

---

# 52. Chapter Checkpoint

### Q1

What is the central architectural idea of VGG?

### Q2

What is the mathematical form of an identity residual block?

### Q3

Why can two 3×3 convolutions be useful compared with one 5×5 convolution?

### Q4

Why must shortcut and residual outputs have compatible shapes?

### Q5

What is the difference between freezing and fine-tuning a pretrained model?

### Q6

Why is a pretrained model's preprocessing pipeline important?

### Q7

Why is YOLO not simply another name for ResNet?

---

# 53. One-Page Recall Sheet

```text
VGG
│
├── simple regular architecture
├── repeated 3×3 convolutions
├── pooling
├── deeper feature hierarchy
└── pretrained feature extraction

RESNET
│
├── deep CNN
├── residual block
│      y = F(x) + x
│
├── shortcut / skip connection
├── projection shortcut when shape changes
├── basic blocks
└── bottleneck blocks

TRANSFER LEARNING
pretrained model
→ adapt head
→ freeze / fine-tune
→ target task
```

---

# 54. Cross-Book Links

| Layer | Connection |
|---|---|
| MAIN | C27 explains VGG, ResNet and pretrained-model concepts |
| MATH | Parameter counts, residual addition, tensor shapes |
| LAB | CNN classification / pretrained inference |
| CODE | Model loading, preprocessing and inference |
| EXAM | VGG vs ResNet, residual learning |
| PRACTICE | Shape tracing, parameter calculations, architecture reasoning |
| RESOURCE | Course-specified deep-learning/computer-vision references |
| ASSETS | VGG block diagram, residual block, transfer-learning pipeline |
| MASTER | Dependency into C28 object detection |

---

# 55. Final Chapter Summary

The two architecture families answer different engineering questions.

### VGG

\[
\boxed{
\text{Build depth using a simple repeated stack of small convolutions}
}
\]

### ResNet

\[
\boxed{
\text{Make deep learning easier to optimize through residual paths}
}
\]

The key ResNet equation is:

\[
\boxed{y=F(x)+x}
\]

and when shapes differ:

\[
\boxed{y=F(x)+W_sx}.
\]

The broader Unit IV journey is now:

```text
C25
classification
 ↓
C26
CNN fundamentals
 ↓
C27
VGG / ResNet / pretrained representations
 ↓
C28
object detection
```

The next chapter moves from:

```text
WHAT is in the image?
```

to:

```text
WHAT is in the image
+
WHERE is it?
```

---

**Next chapter:** C28 — Object Detection and YOLO
