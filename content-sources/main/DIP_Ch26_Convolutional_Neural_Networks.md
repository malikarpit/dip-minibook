---
id: "C26"
title: "Convolutional Neural Networks (CNNs)"
layer: "MAIN"
part: "V — From DIP to Intelligent Vision"
unit: "Unit IV"
version: "1.0"
status: "PRODUCTION"
syllabus_scope: "Introduction to Convolutional Neural Networks (CNNs); required foundation for CNN-based image classification practical"
tags:
  - digital-image-processing
  - cnn
  - convolutional-neural-network
  - deep-learning
  - feature-maps
  - pooling
  - mnist
prerequisites:
  - "C08 — Spatial Filtering and Convolution"
  - "C25 — Image Classification"
related_math:
  - "Convolution"
  - "Matrix multiplication"
  - "Gradients"
  - "Softmax"
  - "Cross-entropy"
related_lab:
  - "LAB-08 — CNN-Based Image Classification"
related_code:
  - "CODE-08 — TensorFlow/Keras CNN"
related_exam:
  - "EXAM-CNN"
related_practice:
  - "PRACTICE-CNN"
---

# C26 — Convolutional Neural Networks

> **Chapter thesis:** A CNN learns spatially structured image representations by applying learned local filters, combining feature maps through nonlinear transformations and pooling, and using the resulting hierarchy for tasks such as image classification.

---

# 1. Why This Chapter Exists

The University syllabus explicitly requires an:

> **Introduction to Convolutional Neural Networks (CNNs)**

and the practical component requires:

> **CNN-based handwritten digit classification using the MNIST dataset.** fileciteturn4file0L48-L52 fileciteturn4file0L76-L80

This makes CNNs a core Unit IV topic.

The most important conceptual bridge is from earlier DIP:

```text
C08
fixed / human-designed convolution kernel
            ↓
C26
learned convolution kernel
```

The mathematics of convolution is familiar.

What changes is:

> **The kernel values are learned from data.**

---

# 2. Learning Contract

After this chapter, you should be able to:

- explain what a CNN is;
- explain why CNNs are suitable for images;
- connect CNN convolution to classical spatial filtering;
- explain kernels, feature maps, stride and padding;
- calculate output dimensions for a convolution/pooling layer;
- explain nonlinear activation functions;
- explain pooling;
- trace tensor shapes through a CNN;
- distinguish parameters from activations;
- explain flattening and dense classification layers;
- explain softmax and cross-entropy at an introductory level;
- explain the forward pass and training loop;
- describe backpropagation conceptually;
- build a basic MNIST CNN in TensorFlow/Keras;
- evaluate and inspect classification errors.

---

# 3. CNN in One Picture

A typical CNN classifier can be represented as:

```text
Input image
    │
    ▼
Convolution
    │
    ▼
Activation
    │
    ▼
Pooling
    │
    ▼
Convolution
    │
    ▼
Activation
    │
    ▼
Pooling
    │
    ▼
Feature representation
    │
    ▼
Classifier
    │
    ▼
Class scores / probabilities
```

A deeper network repeats these ideas several times.

---

# 4. Why Ordinary Dense Networks Are Awkward for Images

Suppose an image has:

\[
224\times224\times3
\]

values.

Flattening gives:

\[
224\times224\times3
=
150{,}528
\]

input values.

A dense layer with 1000 neurons would require approximately:

\[
150{,}528\times1000
=
150{,}528{,}000
\]

weights, before biases.

A CNN instead uses **local connectivity** and **parameter sharing**.

The same learned filter can scan across many image locations.

This drastically changes the parameterization.

---

# 5. Local Connectivity

Edges and patterns are often local.

A small filter might inspect a neighbourhood such as:

```text
[x x x]
[x x x]
[x x x]
```

rather than the entire image at once.

A CNN therefore builds local evidence and gradually combines it into larger structures.

---

# 6. Parameter Sharing

Suppose a 3×3 filter is learned.

Its nine weights can be applied at many positions:

```text
image
 ↓
filter at position 1
filter at position 2
filter at position 3
...
```

The same weights are reused.

This is called **parameter sharing**.

It provides two key benefits:

- fewer parameters;
- a feature can be detected at different spatial locations.

---

# 7. Convolution vs Correlation — Important Engineering Caveat

In mathematical signal processing, convolution traditionally includes kernel reversal.

Many deep-learning libraries implement what is mathematically closer to **cross-correlation** while calling the operation convolution.

For example, a framework computes:

\[
y(i,j)
=
\sum_{m,n}
x(i+m,j+n)w(m,n)
\]

without explicitly flipping \(w\).

This distinction usually does not prevent CNN learning because the filters are learned.

For this chapter:

> Use “convolution” as the standard deep-learning term, but know that many implementations actually perform cross-correlation.

This is an important bridge from C08.

---

# 8. A Single CNN Filter

Consider a grayscale image region:

\[
X=
\begin{bmatrix}
1&2&0\\
0&1&3\\
2&0&1
\end{bmatrix}
\]

and kernel:

\[
K=
\begin{bmatrix}
1&0&-1\\
1&0&-1\\
1&0&-1
\end{bmatrix}.
\]

The local response is:

\[
1(1)+2(0)+0(-1)
\]

\[
+0(1)+1(0)+3(-1)
\]

\[
+2(1)+0(0)+1(-1).
\]

Therefore:

\[
1-3+2-1=-1.
\]

The output value measures the response of this local pattern to the filter.

---

# 9. Feature Map

As the same filter is moved across the image, one output value is produced at each valid position.

The resulting matrix is a **feature map**.

Conceptually:

```text
image
  ↓
same learned filter everywhere
  ↓
feature map
```

One filter produces one feature map.

Multiple filters produce multiple feature maps.

---

# 10. Multiple Filters

Suppose a convolution layer has:

\[
C_{\text{out}}=32
\]

filters.

For a single-channel image:

\[
3\times3
\]

kernels produce 32 feature maps.

The layer output therefore has:

\[
H'\times W'\times32
\]

for channels-last representation.

Each channel corresponds to one learned pattern detector.

---

# 11. Multi-Channel Convolution

For an RGB input:

\[
H\times W\times3,
\]

a 3×3 convolution with 32 output channels has weights shaped approximately as:

\[
3\times3\times3\times32
\]

for channels-last conceptual notation.

The number of kernel weights is:

\[
3\times3\times3\times32
=
864.
\]

With one bias per output channel:

\[
864+32=896
\]

trainable parameters.

This illustrates parameter sharing and structured connectivity.

---

# 12. Parameter Count Formula

For a 2-D convolution layer:

\[
P=
K_hK_wC_{\text{in}}C_{\text{out}}+C_{\text{out}}
\]

where:

- \(K_h\) = kernel height;
- \(K_w\) = kernel width;
- \(C_{\text{in}}\) = input channels;
- \(C_{\text{out}}\) = output channels.

### Worked Example

\[
K_h=3,\quad K_w=3,\quad C_{\text{in}}=1,\quad C_{\text{out}}=32.
\]

Then:

\[
P=3\times3\times1\times32+32
\]

\[
=288+32
\]

\[
=\boxed{320}.
\]

---

# 13. Stride

**Stride** determines how far the filter moves at each step.

For stride:

\[
S=1
\]

the filter moves one pixel at a time.

For:

\[
S=2
\]

it skips every second position.

Larger stride generally reduces spatial output dimensions.

---

# 14. Padding

Padding adds values around the input border.

A common choice is:

```text
zero padding
```

but other padding modes exist.

Padding allows control over spatial size and boundary handling.

Two common conceptual cases:

### Valid

No padding.

### Same

Padding is selected so the output spatial dimensions can be maintained at a desired relationship to the input, especially with stride 1.

---

# 15. Convolution Output Size

For one spatial dimension:

\[
H_{\text{out}}
=
\left\lfloor
\frac{H+2P-D(K-1)-1}{S}
+1
\right\rfloor
\]

where:

- \(H\) = input size;
- \(K\) = kernel size;
- \(P\) = padding;
- \(S\) = stride;
- \(D\) = dilation.

For the common case:

\[
D=1,
\]

this becomes:

\[
H_{\text{out}}
=
\left\lfloor
\frac{H+2P-K}{S}
+1
\right\rfloor.
\]

Width uses the analogous equation.

---

# 16. Worked Output-Size Example

Input:

\[
28\times28
\]

Kernel:

\[
3\times3
\]

Stride:

\[
1
\]

Padding:

\[
0.
\]

Then:

\[
H_{\text{out}}
=
\frac{28-3}{1}+1
=
26.
\]

So:

\[
\boxed{26\times26}
\]

is the spatial output.

If the layer has 32 filters:

\[
\boxed{26\times26\times32}.
\]

---

# 17. Same-Padding Example

Suppose:

\[
H=28,\quad K=3,\quad S=1.
\]

With one-pixel padding:

\[
P=1.
\]

Then:

\[
H_{\text{out}}
=
\frac{28+2(1)-3}{1}+1
=
28.
\]

Thus:

\[
\boxed{28\times28}
\]

is preserved spatially.

---

# 18. Activation Functions

A convolution produces linear responses.

CNNs introduce nonlinear activation functions.

A common choice is ReLU:

\[
\operatorname{ReLU}(x)=\max(0,x).
\]

Therefore:

```text
x < 0 → 0
x > 0 → x
```

Example:

\[
[-2,-1,0,2,5]
\]

becomes:

\[
[0,0,0,2,5].
\]

---

# 19. Why Nonlinearity Matters

If every layer only performed a linear operation, a deep stack could collapse into another linear transformation.

Nonlinearity allows the network to represent more complex relationships.

Conceptually:

```text
linear filter
→ nonlinear activation
→ another linear filter
→ nonlinear activation
→ complex function
```

ReLU is therefore more than an arbitrary formula.

It is part of the representational power of the network.

---

# 20. Pooling

Pooling reduces spatial resolution while retaining selected information.

A common operation is max pooling.

For a 2×2 region:

```text
1 7
3 4
```

max pooling produces:

\[
7.
\]

For:

```text
5 2
1 3
```

it produces:

\[
5.
\]

---

# 21. Why Pooling Is Used

Pooling can:

- reduce spatial dimensions;
- reduce computation;
- provide some local invariance;
- summarize local activations.

But it can also remove spatial detail.

Modern architectures do not all use traditional max pooling at every stage.

For this introductory syllabus topic, understand the concept and trade-off.

---

# 22. Pooling Output Size

For a 2×2 pool with stride 2:

\[
28\times28
\]

becomes approximately:

\[
14\times14.
\]

If there are 32 channels:

\[
28\times28\times32
\]

becomes:

\[
14\times14\times32.
\]

The number of channels stays the same under ordinary spatial pooling.

---

# 23. Tensor Shape Is a Core Skill

Suppose:

```text
Input:       28 × 28 × 1
Conv 32:     28 × 28 × 32
Pool 2×2:    14 × 14 × 32
Conv 64:     14 × 14 × 64
Pool 2×2:     7 ×  7 × 64
```

Flattening gives:

\[
7\times7\times64
=
3136
\]

features.

This is the bridge into a dense classifier.

Shape tracing is one of the most practical CNN debugging skills.

---

# 24. Flattening

Suppose the final convolutional representation is:

\[
7\times7\times64.
\]

Flattening converts it into one vector:

\[
\mathbf{x}\in\mathbb{R}^{3136}.
\]

The spatial grid is no longer represented as separate dimensions in that vector, but the values came from spatial feature maps.

---

# 25. Dense Classification Layer

A dense layer maps the flattened feature vector to class scores.

For:

\[
3136
\]

inputs and:

\[
128
\]

neurons:

\[
3136\times128+128
\]

parameters.

Calculate:

\[
401{,}408+128
\]

\[
=\boxed{401{,}536}.
\]

This can be much larger than an earlier convolution layer.

---

# 26. Why CNNs Are Parameter-Efficient

Compare two conceptual approaches.

### Dense

Each neuron sees every pixel.

### CNN

A filter sees a small local region and reuses the same weights across positions.

This provides:

\[
\boxed{\text{local connectivity + parameter sharing}}
\]

which is central to the CNN architecture.

---

# 27. Hierarchical Feature Learning

One of the most useful mental models is:

```text
Early layers
→ edges / local contrasts

Middle layers
→ textures / motifs / parts

Later layers
→ combinations of parts / class evidence
```

This is a conceptual description, not a guarantee that every channel corresponds neatly to a human-interpretable object part.

The representations are learned from data.

---

# 28. CNNs vs Classical DIP Filters

This bridge should be remembered.

### Classical filter

```text
kernel = designed by engineer
```

Example:

```text
Sobel
Gaussian
Laplacian
```

### CNN filter

```text
kernel = learned from training data
```

The mathematical operation resembles convolution/cross-correlation, but the filter values are optimized automatically.

This is why earlier DIP material is not discarded when learning CNNs.

---

# 29. Forward Pass

A simplified forward pass is:

```text
input image
 ↓
Conv
 ↓
ReLU
 ↓
Pooling
 ↓
Conv
 ↓
ReLU
 ↓
Pooling
 ↓
Flatten
 ↓
Dense
 ↓
class scores
```

The network computes an output without changing its weights.

This is **inference** or the forward computation stage.

---

# 30. Loss Function

For multiclass classification, cross-entropy is a common loss.

For target class \(y\):

\[
L=-\log(p_y).
\]

Example:

If the correct class receives:

\[
p_y=0.9,
\]

then:

\[
L=-\log(0.9)\approx0.1053.
\]

If:

\[
p_y=0.1,
\]

then:

\[
L=-\log(0.1)\approx2.3026.
\]

The network is penalized much more strongly when it assigns low probability to the correct class.

---

# 31. Softmax

Given logits:

\[
z_1,\ldots,z_K,
\]

softmax gives:

\[
p_i=
\frac{e^{z_i}}
{\sum_{j=1}^{K}e^{z_j}}.
\]

The probabilities satisfy:

\[
p_i\ge0
\]

and:

\[
\sum_i p_i=1.
\]

For MNIST:

\[
K=10.
\]

---

# 32. A Stable Softmax Implementation

Directly computing:

\[
e^{z_i}
\]

can overflow for large values.

A common stable calculation subtracts:

\[
m=\max_i z_i
\]

before exponentiation:

\[
p_i=
\frac{e^{z_i-m}}
{\sum_j e^{z_j-m}}.
\]

Subtracting the same value from every logit does not change the resulting softmax probabilities.

This is an implementation detail worth knowing.

---

# 33. Training

Training repeatedly performs:

```text
batch of images
      ↓
forward pass
      ↓
predictions
      ↓
loss
      ↓
backpropagation
      ↓
parameter update
```

Repeat for many batches and epochs.

---

# 34. Backpropagation — Conceptual View

Backpropagation computes how the loss changes with respect to model parameters.

For parameter \(\theta\):

\[
\frac{\partial L}{\partial\theta}
\]

is the gradient of the loss with respect to that parameter.

An optimizer uses these gradients to update parameters.

A simple gradient-descent update is:

\[
\theta_{\text{new}}
=
\theta_{\text{old}}
-
\eta
\frac{\partial L}{\partial\theta}
\]

where \(\eta\) is the learning rate.

---

# 35. Learning Rate

The learning rate controls the step size.

Too small:

```text
training may be very slow
```

Too large:

```text
training can become unstable
```

The correct value depends on architecture, optimizer, data and training setup.

---

# 36. Epoch and Batch

### Batch

A group of training examples processed together.

### Epoch

One complete pass through the training dataset.

Example:

```text
60,000 training images
batch size = 128
```

means one epoch contains many batches.

The exact number is approximately:

\[
\left\lceil\frac{60{,}000}{128}\right\rceil.
\]

---

# 37. CNN Training Loop

```text
for each epoch:
    for each batch:
        predictions = model(batch)
        loss = compare(predictions, labels)
        gradients = backpropagate(loss)
        optimizer.update(parameters)
```

Validation is then performed without updating weights.

---

# 38. Training vs Inference

### Training

```text
input
→ prediction
→ loss
→ gradients
→ update parameters
```

### Inference

```text
input
→ prediction
```

No parameter update is intended during ordinary inference.

This distinction becomes important when saving/deploying a trained model.

---

# 39. MNIST Tensor Pipeline

The university practical specifies MNIST and TensorFlow/Keras. fileciteturn4file0L76-L80

A typical channels-last pipeline is:

```text
raw MNIST image
28 × 28

      ↓ add channel dimension

28 × 28 × 1

      ↓ batch

B × 28 × 28 × 1

      ↓ CNN

B × 7 × 7 × 64

      ↓ flatten

B × 3136

      ↓ dense

B × 128

      ↓ output

B × 10
```

Exact intermediate shapes depend on architecture choices.

---

# 40. Complete Keras MNIST Example

```python
from __future__ import annotations

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


# ---------------------------------------------------------
# 1. Load data
# ---------------------------------------------------------
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# ---------------------------------------------------------
# 2. Normalize to [0, 1]
# ---------------------------------------------------------
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Add channel dimension: H x W -> H x W x 1
x_train = x_train[..., np.newaxis]
x_test = x_test[..., np.newaxis]

# ---------------------------------------------------------
# 3. Build CNN
# ---------------------------------------------------------
model = keras.Sequential([
    layers.Input(shape=(28, 28, 1)),

    layers.Conv2D(32, (3, 3), padding="same", activation="relu"),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(64, (3, 3), padding="same", activation="relu"),
    layers.MaxPooling2D((2, 2)),

    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(10, activation="softmax"),
])

# ---------------------------------------------------------
# 4. Compile
# ---------------------------------------------------------
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

# ---------------------------------------------------------
# 5. Inspect architecture
# ---------------------------------------------------------
model.summary()

# ---------------------------------------------------------
# 6. Train
# ---------------------------------------------------------
history = model.fit(
    x_train,
    y_train,
    validation_split=0.1,
    epochs=5,
    batch_size=128,
)

# ---------------------------------------------------------
# 7. Evaluate
# ---------------------------------------------------------
test_loss, test_accuracy = model.evaluate(
    x_test,
    y_test,
    verbose=0,
)

print(f"Test loss: {test_loss:.4f}")
print(f"Test accuracy: {test_accuracy:.4f}")

# ---------------------------------------------------------
# 8. Inference
# ---------------------------------------------------------
sample = x_test[:1]
prediction = model.predict(sample, verbose=0)

predicted_class = int(np.argmax(prediction[0]))
actual_class = int(y_test[0])

print("Predicted:", predicted_class)
print("Actual:", actual_class)
```

This is an educational baseline. Exact accuracy depends on implementation details, environment, training duration and randomness.

---

# 41. Why `sparse_categorical_crossentropy`?

MNIST labels are integer class IDs:

```text
0, 1, 2, ..., 9
```

rather than one-hot vectors.

Therefore sparse categorical cross-entropy is a convenient match.

If labels were represented as one-hot vectors such as:

```text
[0,0,0,0,0,0,0,1,0,0]
```

then a categorical cross-entropy formulation would be appropriate.

---

# 42. Predicting One Image

```python
prediction = model.predict(x_test[:1], verbose=0)

probs = prediction[0]
predicted_digit = int(np.argmax(probs))

print("Probabilities:", probs)
print("Predicted digit:", predicted_digit)
```

A good practical exercise is to print the complete probability vector rather than only the predicted class.

That lets you inspect ambiguity.

---

# 43. Confusion Matrix in Python

```python
from sklearn.metrics import confusion_matrix

probs = model.predict(x_test, verbose=0)
predictions = np.argmax(probs, axis=1)

cm = confusion_matrix(y_test, predictions)

print(cm)
```

The diagonal corresponds to correct predictions.

Off-diagonal entries reveal confusions.

---

# 44. Error Inspection

```python
wrong = np.where(predictions != y_test)[0]

for idx in wrong[:10]:
    print(
        "Index:", idx,
        "Actual:", int(y_test[idx]),
        "Predicted:", int(predictions[idx]),
    )
```

A stronger lab should also visualize selected incorrect examples.

This turns:

```text
model score
```

into:

```text
model behaviour
```

---

# 45. Visualizing Feature Maps

Feature maps can be inspected to understand what different learned filters respond to.

Conceptually:

```text
input
 ↓
Conv layer
 ↓
channels 0...31
 ↓
feature maps
```

An engineering caution:

> A feature map should not automatically be interpreted as a single human concept such as “vertical edges.” Some learned channels are distributed, mixed, or task-specific.

---

# 46. Why CNN Convolution Is Powerful

A CNN learns:

```text
where a local pattern occurs
+
how strongly it occurs
```

because the same filter is applied across the image.

This creates a form of spatial reuse.

Later layers combine lower-level activations to detect more complex patterns.

---

# 47. Receptive Field

A neuron's **receptive field** is the region of the original image that can influence its activation.

With stacked convolution and pooling layers, the receptive field grows.

Conceptually:

```text
early neuron
→ small image neighbourhood

deeper neuron
→ larger image region
```

This helps a deep CNN move from local patterns toward larger-scale structures.

---

# 48. Pooling and Receptive Field

Pooling reduces spatial resolution while increasing the effective receptive field of later units.

For example:

```text
28×28
 ↓ pool
14×14
 ↓ pool
7×7
```

A later activation can correspond to a larger region of the original image than an early activation.

---

# 49. CNN Hyperparameters

Important choices include:

| Parameter | Meaning |
|---|---|
| Number of filters | Output feature-map count |
| Kernel size | Local pattern size |
| Stride | Movement step |
| Padding | Border handling/output size |
| Activation | Nonlinear transformation |
| Pool size | Local aggregation size |
| Learning rate | Update step scale |
| Batch size | Samples per update |
| Epochs | Dataset passes |

Not every architecture uses every parameter in the same way.

---

# 50. CNN Design Trade-offs

### More filters

Can increase representation capacity.

But:

```text
more parameters
→ more computation
```

### Larger kernels

Larger local context.

But:

```text
more parameters / compute
```

### More layers

Potentially richer hierarchical representation.

But:

```text
training complexity
+
memory
+
optimization difficulty
```

The appropriate design depends on the task.

---

# 51. Overfitting in CNNs

CNNs can overfit.

Typical warning sign:

```text
training accuracy ↑
validation accuracy stops improving
```

or:

```text
training loss ↓
validation loss ↑
```

Potential responses:

- data augmentation;
- regularization;
- dropout;
- early stopping;
- more data;
- architecture changes.

These are engineering tools rather than guaranteed fixes.

---

# 52. Data Augmentation

Augmentation creates additional training variation.

For suitable tasks:

```text
original
→ slight shift
→ rotation
→ crop
→ brightness variation
```

But augmentation must preserve the label.

For handwritten digits, arbitrary transformations may alter the identity of the digit.

Therefore:

> **Augmentation should reflect realistic variation, not random distortion.**

---

# 53. CNNs Do Not Eliminate Preprocessing

A common misconception is:

> “CNNs can take anything exactly as it is.”

Real systems still need careful handling of:

- image size;
- channels;
- numeric ranges;
- missing values;
- normalization;
- orientation;
- train/inference consistency.

Good models cannot compensate for every data pipeline error.

---

# 54. Classical DIP → CNN Integration

The conceptual journey is:

```text
Sobel / Gaussian / Laplacian
        ↓
hand-designed spatial filters

DCT / frequency representation
        ↓
engineered transform

SIFT / HOG
        ↓
hand-designed descriptors

CNN
        ↓
learned filters + learned representation
```

CNNs do not make earlier DIP topics irrelevant.

They provide a learned alternative to part of the manually designed representation pipeline.

---

# 55. Exam Lens

## 2-mark questions

**Define CNN.**  
A neural architecture designed to process structured grid data such as images using local connectivity, shared filters, nonlinearities and hierarchical feature extraction.

**What is a feature map?**  
The spatial output generated when a convolutional filter responds across an input.

**What is parameter sharing?**  
Using the same filter weights at multiple spatial locations.

---

## 5-mark question

### Explain CNN architecture.

Use:

```text
input
→ convolution
→ activation
→ pooling
→ deeper convolution
→ flatten / global representation
→ dense layer
→ output
```

Then explain the role of each stage.

---

## 10-mark question

### Explain CNN-based image classification.

Recommended answer:

1. image/tensor input;
2. convolution;
3. learned kernels;
4. feature maps;
5. activation;
6. pooling;
7. repeated feature extraction;
8. flattening;
9. classifier;
10. softmax;
11. loss;
12. forward pass;
13. backpropagation;
14. parameter update;
15. evaluation.

For the course practical, connect the answer to MNIST. fileciteturn4file0L76-L80

---

# 56. Numerical Practice — Output Shape

Input:

\[
32\times32\times3
\]

Convolution:

- kernel \(5\times5\)
- stride \(1\)
- padding \(0\)
- 16 filters

Spatial output:

\[
32-5+1=28.
\]

Therefore:

\[
\boxed{28\times28\times16}.
\]

---

# 57. Numerical Practice — Parameter Count

For:

\[
3\times3,
\quad C_{\text{in}}=3,
\quad C_{\text{out}}=16
\]

parameters:

\[
3\times3\times3\times16+16
\]

\[
=432+16
\]

\[
=\boxed{448}.
\]

---

# 58. Numerical Practice — Pooling

Input:

\[
28\times28\times32
\]

2×2 max pooling, stride 2:

\[
14\times14\times32.
\]

Number of values before:

\[
28\times28\times32=25{,}088.
\]

After:

\[
14\times14\times32=6{,}272.
\]

So the number of spatial activation values is reduced by a factor of:

\[
\boxed{4}.
\]

---

# 59. Chapter Checkpoint

### Q1

Why can the same CNN filter detect a pattern in different image locations?

### Q2

For an input of \(28\times28\times1\), a 3×3 valid convolution with 32 filters and stride 1 produces what shape?

### Q3

How many trainable parameters does that layer contain?

### Q4

Why is ReLU inserted between learned linear operations?

### Q5

What is the difference between training and inference?

### Q6

Where does the learning of filter values happen?

### Q7

Why can pooling reduce computation but also remove detail?

---

# 60. One-Page Recall Sheet

```text
CNN
│
├── Input image tensor
│
├── Convolution
│   ├── local connectivity
│   ├── shared kernels
│   └── feature maps
│
├── ReLU
│   └── nonlinearity
│
├── Pooling
│   └── spatial reduction
│
├── Deeper layers
│   └── hierarchical representation
│
├── Flatten / global representation
│
├── Dense classifier
│
├── Softmax
│   └── class probabilities
│
└── Training
    ├── loss
    ├── backpropagation
    └── optimizer update
```

---

# 61. Cross-Book Links

| Layer | Connection |
|---|---|
| MAIN | C26 explains the CNN architecture |
| MATH | Convolution, output dimensions, parameter count, softmax, loss |
| LAB | Practical 8 — MNIST classification |
| CODE | TensorFlow/Keras implementation |
| EXAM | CNN architecture, convolution, pooling, training |
| PRACTICE | Shape tracing, parameter counts, architecture reasoning |
| RESOURCE | Deep-learning/computer-vision references listed by the course |
| ASSETS | CNN pipeline, tensor shapes, feature-map illustrations |
| MASTER | Dependency into C27 VGG/ResNet and C28 YOLO |

---

# 62. Final Chapter Summary

A CNN replaces much of the manually designed image feature pipeline with a learned hierarchy:

\[
\boxed{
\text{pixels}
\rightarrow
\text{learned local filters}
\rightarrow
\text{feature maps}
\rightarrow
\text{hierarchical representation}
\rightarrow
\text{class decision}
}
\]

The three concepts to remember most strongly are:

\[
\boxed{\text{local connectivity}}
\]

\[
\boxed{\text{parameter sharing}}
\]

\[
\boxed{\text{learned hierarchical features}}
\]

The practical requirement turns these ideas into a complete system:

```text
MNIST
→ preprocessing
→ CNN
→ training
→ testing
→ prediction
→ error analysis
```

The university syllabus identifies CNNs as a Unit IV topic and explicitly requires MNIST-based CNN classification as Practical 8. fileciteturn4file0L48-L52 fileciteturn4file0L76-L80

---

**Next chapter:** C27 — VGG and ResNet
