---
id: "C25"
title: "Image Classification"
layer: "MAIN"
part: "V — From DIP to Intelligent Vision"
unit: "Unit IV"
version: "1.0"
status: "PRODUCTION"
syllabus_scope: "Image Classification and Object Detection — classification foundation"
tags:
  - digital-image-processing
  - image-classification
  - computer-vision
  - machine-learning
  - deep-learning
  - mnist
prerequisites:
  - "C04 — Image Representation: Pixels, Matrices, Tensors and Resolution"
  - "C19 — Image Features and Descriptors"
related_math:
  - "Vectors"
  - "Probability"
  - "Matrices"
  - "Confusion matrix"
related_lab:
  - "LAB-08 — CNN-Based Image Classification"
related_code:
  - "CODE-08 — Image Classification"
related_exam:
  - "EXAM-Classification"
related_practice:
  - "PRACTICE-Classification"
---

# C25 — Image Classification

> **Chapter thesis:** Image classification maps an input image to a class decision, turning numerical image data into a categorical interpretation.

---

# 1. Why This Chapter Exists

Digital Image Processing begins by asking:

> How can we represent and manipulate an image?

Advanced vision systems ask:

> What does the image contain?

**Image classification** is one of the first answers.

A classifier receives an image and predicts a class:

```text
image
  ↓
representation
  ↓
feature extraction / learned representation
  ↓
classifier
  ↓
class prediction
```

Examples:

```text
digit image → "7"

fruit image → "apple"

road image → "road"

medical image → "class A"
```

The exact application varies, but the computational structure is similar.

---

# 2. Learning Contract

After this chapter, you should be able to:

- define image classification;
- distinguish classification from detection and segmentation;
- explain class labels, features, training, validation and testing;
- distinguish classical feature-based pipelines from learned feature pipelines;
- explain supervised image classification;
- represent an image as a feature vector or tensor;
- understand class scores, probabilities and predicted labels;
- read a confusion matrix;
- calculate accuracy, precision, recall and F1 for simple cases;
- explain overfitting and generalization in image classification;
- trace a complete MNIST classification workflow;
- connect classical DIP features to CNN-based classification.

---

# 3. Classification as a Mapping

Let an input image be:

\[
X.
\]

A classifier implements a function:

\[
f(X)\rightarrow y
\]

where:

\[
y\in\{1,2,\ldots,K\}
\]

is one of \(K\) possible classes.

For example:

\[
f(X_{\text{digit}})\rightarrow 7.
\]

The model does not literally “understand” the semantic concept in the human sense. It learns a mapping from image representations to target labels using examples.

---

# 4. What Is a Class?

A **class** is a category assigned to an image under a particular task definition.

Example:

```text
Classes:
0
1
2
3
4
5
6
7
8
9
```

for handwritten digit classification.

The same image could belong to different classes under a different task.

For example:

```text
car image
```

could be classified as:

- vehicle type;
- manufacturer;
- colour;
- road condition;
- scene category.

Therefore:

> **Classification depends on the label definition, not only on the image.**

---

# 5. The Classification Pipeline

A useful generic pipeline is:

```text
Raw image
    ↓
Preprocessing
    ↓
Representation
    ↓
Feature extraction
    ↓
Classifier
    ↓
Scores / probabilities
    ↓
Predicted class
    ↓
Evaluation
```

In classical systems:

```text
image
→ manually designed features
→ classifier
```

In deep learning systems:

```text
image
→ learned features
→ classifier
```

The second architecture becomes the focus of C26.

---

# 6. Classification vs Detection vs Segmentation

This distinction is essential.

```text
Classification
→ What is in the image?

Detection
→ What is present, and where?

Segmentation
→ Which pixels belong to which region/class?
```

### Example

Suppose an image contains a cat and a dog.

### Classification

```text
cat + dog
```

or, if the task permits only one label:

```text
"animals"
```

### Object detection

```text
cat → bounding box
dog → bounding box
```

### Semantic segmentation

```text
cat pixels → cat
dog pixels → dog
background → background
```

The output structure is different even when the same image is used.

---

# 7. Single-Label vs Multi-Label Classification

### Single-label

One image receives one class.

```text
image → "cat"
```

### Multi-label

One image can receive multiple class labels.

```text
image → {"cat", "sofa", "indoor"}
```

The syllabus does not require a separate treatment of multi-label learning, but the distinction prevents confusion when reading modern computer-vision systems.

---

# 8. Classical Image Classification

A traditional pipeline might be:

```text
image
 ↓
preprocessing
 ↓
feature extraction
 ↓
feature vector
 ↓
classifier
 ↓
label
```

Features might include:

- intensity statistics;
- edges;
- corners;
- texture;
- shape;
- SIFT/HOG-style descriptors.

This creates a direct connection to Part III.

For example:

```text
C19/C20
hand-designed features
        ↓
C25
classification using those features
```

---

# 9. Feature Vector

Suppose an image is represented by measurements:

\[
x_1,x_2,\ldots,x_n.
\]

Then:

\[
\mathbf{x}=
[x_1,x_2,\ldots,x_n]^T
\]

is a feature vector.

For example:

```text
mean intensity
edge density
texture measure
shape descriptor
...
```

can become a numerical vector.

A classical classifier receives \(\mathbf{x}\), not necessarily the raw image.

---

# 10. Learned Feature Representation

Deep learning changes the architecture:

```text
raw image
    ↓
learned filters
    ↓
feature maps
    ↓
higher-level representation
    ↓
classifier
```

Instead of manually specifying all useful features, the model learns intermediate representations from training data.

This is the conceptual bridge from C25 to C26.

---

# 11. Dataset Structure

A supervised classification dataset contains examples of:

\[
(X,y)
\]

where:

- \(X\) = input image;
- \(y\) = target label.

Example:

| Image | Label |
|---|---|
| handwritten 0 | 0 |
| handwritten 1 | 1 |
| handwritten 7 | 7 |

A training dataset should contain enough variation to represent the kinds of inputs expected at inference time.

---

# 12. Training, Validation and Test

A standard workflow is:

```text
Dataset
  │
  ├── Training set
  ├── Validation set
  └── Test set
```

### Training set

Used to fit model parameters.

### Validation set

Used to make development decisions, such as:

- hyperparameter choices;
- model selection;
- early stopping.

### Test set

Used for final evaluation after development choices are complete.

The test set should not become an informal repeated tuning set.

---

# 13. Why Data Splitting Matters

Suppose a model is evaluated on images it has effectively memorized.

A high score can then be misleading.

The real question is:

> How well does the model perform on unseen examples drawn from the intended data distribution?

This is **generalization**.

---

# 14. Preprocessing

Images may need preprocessing before classification.

Common operations include:

- resizing;
- normalization;
- colour conversion;
- cropping;
- alignment;
- noise handling;
- data augmentation.

For MNIST, for example, grayscale digit images can be normalized into a convenient numeric range before entering the CNN.

---

# 15. Normalization Example

Suppose pixel values are stored in:

\[
0\le x\le255.
\]

A simple normalization is:

\[
x'=\frac{x}{255}.
\]

Then:

\[
0\le x'\le1.
\]

Example:

\[
x=128
\]

becomes:

\[
x'=\frac{128}{255}\approx0.502.
\]

Normalization does not change the semantic image content. It changes the numerical scale used by the model.

---

# 16. Class Scores and Probabilities

A classifier may produce a score for each class.

For ten classes:

```text
class 0 → score
class 1 → score
...
class 9 → score
```

The predicted class is commonly chosen as the class with the highest output score.

For probability-style outputs:

\[
\hat y=
\arg\max_k p(y=k\mid X).
\]

For example:

| Class | Probability |
|---|---:|
| 0 | 0.01 |
| 1 | 0.03 |
| 2 | 0.02 |
| 3 | 0.04 |
| 4 | 0.05 |
| 5 | 0.01 |
| 6 | 0.02 |
| 7 | **0.79** |
| 8 | 0.02 |
| 9 | 0.01 |

Prediction:

\[
\boxed{7}
\]

because it has the largest probability.

---

# 17. Probability Output vs Confidence

A numerical output such as:

\[
0.79
\]

should not automatically be interpreted as:

> “The model is 79% certain in a perfectly calibrated sense.”

Model probabilities can be poorly calibrated.

For a university-level introduction, it is enough to understand:

```text
class score/probability distribution
→ selected label
```

while recognizing that probability calibration is a separate topic.

---

# 18. Confusion Matrix

For \(K\) classes, a confusion matrix records:

```text
predicted class
        ↓
actual class → matrix
```

For a binary case:

| | Predicted + | Predicted − |
|---|---:|---:|
| Actual + | TP | FN |
| Actual − | FP | TN |

where:

- TP = true positive;
- TN = true negative;
- FP = false positive;
- FN = false negative.

---

# 19. Accuracy

Accuracy is:

\[
\text{Accuracy}
=
\frac{TP+TN}
{TP+TN+FP+FN}.
\]

For a multiclass confusion matrix:

\[
\text{Accuracy}
=
\frac{\sum_i C_{ii}}
{\sum_{i,j} C_{ij}}.
\]

The diagonal contains correct classifications.

---

# 20. Precision, Recall and F1

For a binary class:

\[
\text{Precision}
=
\frac{TP}{TP+FP}
\]

\[
\text{Recall}
=
\frac{TP}{TP+FN}.
\]

F1 score is:

\[
F1=
\frac{2PR}{P+R}.
\]

These are useful when the cost of false positives and false negatives differs.

They are supporting evaluation concepts rather than separate syllabus headings.

---

# 21. Worked Metric Example

Suppose:

\[
TP=90,\quad TN=850,\quad FP=30,\quad FN=30.
\]

Total:

\[
90+850+30+30=1000.
\]

Accuracy:

\[
\frac{90+850}{1000}
=
0.94
\]

or:

\[
\boxed{94\%}.
\]

Precision:

\[
\frac{90}{90+30}
=
0.75.
\]

Recall:

\[
\frac{90}{90+30}
=
0.75.
\]

Therefore:

\[
F1=0.75.
\]

---

# 22. Why Accuracy Can Mislead

Suppose:

```text
990 images → class A
10 images  → class B
```

A classifier that always predicts A gets:

\[
99\%
\]

accuracy.

Yet it completely fails to identify B.

Therefore:

```text
accuracy alone
≠
complete evaluation
```

This matters in imbalanced datasets.

---

# 23. Training Objective

A classifier learns model parameters from training data.

In a neural classification system, training often minimizes a loss such as cross-entropy.

For one example with target class \(y\):

\[
L=-\log p_y
\]

where \(p_y\) is the predicted probability assigned to the correct class.

If the correct class receives high probability:

\[
p_y\rightarrow1
\]

then:

\[
L\rightarrow0.
\]

If it receives a very small probability, the loss becomes large.

The detailed neural optimization process is developed in C26.

---

# 24. Overfitting

A model may perform very well on training data and poorly on unseen data.

Conceptually:

```text
training performance
        ↑
        │      ______
        │     /
        │    /
        │___/____________

generalization
        ↑
        │    /\
        │   /  \____
        │__/___________
```

Overfitting is encouraged by factors such as:

- insufficient data;
- excessive model capacity;
- noisy labels;
- excessive training;
- distribution mismatch.

Possible responses include:

- more representative data;
- augmentation;
- regularization;
- simpler models;
- early stopping;
- better validation procedures.

---

# 25. Underfitting

Underfitting occurs when the model is too limited to capture the relevant structure.

Typical conceptual pattern:

```text
training performance → poor
test performance     → poor
```

The model has not learned enough useful structure.

---

# 26. Generalization

The true objective is not to memorize examples.

It is to learn a useful decision function that works on unseen examples from the target problem.

The ideal chain is:

```text
training examples
      ↓
learn useful representation
      ↓
learn class boundaries
      ↓
generalize to unseen images
```

This is why dataset quality is a first-class engineering concern.

---

# 27. Image Classification with Classical Features

Consider classifying two types of objects:

```text
Class A: circles
Class B: squares
```

A simple feature vector might contain:

```text
area
perimeter
circularity
edge density
```

A classical pipeline is:

```text
image
→ segmentation / preprocessing
→ shape feature extraction
→ feature vector
→ classifier
→ class
```

This demonstrates that classification does not inherently require CNNs.

---

# 28. Why CNNs Became Important

Raw images contain enormous numbers of pixels.

A CNN can learn hierarchical representations:

```text
pixels
 ↓
edges / simple local patterns
 ↓
textures / motifs
 ↓
parts
 ↓
higher-level structures
 ↓
class evidence
```

This allows the feature extractor and classifier to be learned jointly.

C26 explains how.

---

# 29. Classification Example — MNIST

The university practical specifically asks for:

> CNN-based handwritten digit classification using the MNIST dataset. fileciteturn4file0L76-L80

Conceptual workflow:

```text
MNIST image
    ↓
normalize
    ↓
tensor shape
    ↓
CNN
    ↓
feature maps
    ↓
classifier
    ↓
10 class scores
    ↓
argmax
    ↓
predicted digit
```

A typical input example is represented as a grayscale image with spatial dimensions and a channel dimension.

---

# 30. MNIST as a Classification Problem

The labels are:

\[
\{0,1,2,\ldots,9\}.
\]

So:

\[
K=10.
\]

The model solves:

\[
f(X)\rightarrow\{0,\ldots,9\}.
\]

The input is visual, but the output is categorical.

---

# 31. End-to-End Classification Workflow

```text
1. Define classes
2. Collect/load labeled images
3. Inspect dataset
4. Split train/validation/test
5. Preprocess images
6. Choose representation
7. Build classifier
8. Train
9. Validate
10. Test
11. Inspect confusion matrix/errors
12. Save model
13. Run inference on unseen images
```

This is the minimum useful engineering workflow.

---

# 32. Error Analysis

A percentage score is not enough.

Inspect examples where the classifier fails:

```text
true class → 7
prediction → 1
```

Ask:

- Was the handwriting ambiguous?
- Was there noise?
- Was the image shifted?
- Was preprocessing inconsistent?
- Are some classes systematically confused?

Error analysis turns evaluation into engineering knowledge.

---

# 33. Confusion Matrix for MNIST

A 10×10 confusion matrix can reveal patterns such as:

```text
5 confused with 6
3 confused with 8
1 confused with 7
```

The exact pattern depends on the model and dataset evaluation.

The important idea is:

> **Off-diagonal entries show which classes the model confuses.**

---

# 34. Feature Learning vs Hand-Designed Features

| Aspect | Classical pipeline | CNN-style pipeline |
|---|---|---|
| Input | Raw image | Raw image |
| Feature design | Human-designed | Learned |
| Intermediate representation | Explicit feature vector | Feature maps / learned representation |
| Classifier | Separate classical model often used | Often trained jointly |
| Adaptation | Depends on selected features | Features adapt to training objective |
| Interpretability | Often easier to describe | Usually more distributed/complex |

Neither column is universally “better.” The choice depends on data, task, computational resources, and requirements.

---

# 35. Classification Failure Modes

### Distribution shift

Training images differ substantially from deployment images.

### Label noise

Training labels contain mistakes.

### Class imbalance

Some classes have far more examples than others.

### Preprocessing mismatch

Training uses one transformation while deployment uses another.

### Data leakage

Information from validation/test data influences model development improperly.

### Overfitting

The model learns training-specific patterns rather than robust task structure.

---

# 36. Engineering Decision Example

Suppose you need to classify:

```text
100 categories
1 million labeled images
high compute budget
```

A CNN/deep-learning approach is a natural candidate.

Now suppose the dataset contains:

```text
200 images total
simple geometric classes
limited compute
```

A classical feature-based solution may be sufficient.

The right approach depends on the problem.

---

# 37. Tensor View

A grayscale image can be represented as:

\[
H\times W
\]

or, in a deep-learning framework:

\[
H\times W\times C
\]

for channels-last representation.

A batch adds another dimension:

\[
B\times H\times W\times C.
\]

For channels-first systems, the arrangement may be:

\[
B\times C\times H\times W.
\]

This convention difference matters greatly in implementation.

---

# 38. Shape Example

Suppose one grayscale image is:

\[
28\times28.
\]

With one channel:

\[
28\times28\times1.
\]

A batch of 64 images:

\[
64\times28\times28\times1
\]

in channels-last notation.

In a channels-first framework:

\[
64\times1\times28\times28.
\]

Both represent the same logical information, but the memory/tensor dimension order differs.

---

# 39. Mini Classification Model

A simple conceptual neural classifier is:

```text
image
 ↓
feature extractor
 ↓
flatten / global representation
 ↓
dense classifier
 ↓
class scores
```

C26 replaces the generic feature extractor with explicit CNN operations.

---

# 40. Keras Classification Skeleton

The university practical specifies Python with TensorFlow/Keras. fileciteturn4file0L76-L80

A simple architecture can be represented as:

```python
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, 3, activation="relu"),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, activation="relu"),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(10, activation="softmax"),
])

model.summary()
```

The exact architecture is one valid educational example, not a requirement that the syllabus mandates those exact layer counts.

---

# 41. Why the Final Layer Has 10 Outputs

MNIST has ten digit classes:

\[
0,\ldots,9.
\]

Therefore a multiclass classifier commonly produces ten class scores.

With softmax:

\[
p_i=
\frac{e^{z_i}}
{\sum_{j=1}^{10}e^{z_j}}
\]

where \(z_i\) is the score/logit for class \(i\).

The probabilities satisfy:

\[
\sum_i p_i=1.
\]

---

# 42. Worked Softmax Example

Suppose a three-class model produces logits:

\[
[2,1,0].
\]

Then:

\[
e^2\approx7.389,\quad e^1\approx2.718,\quad e^0=1.
\]

Sum:

\[
7.389+2.718+1=11.107.
\]

Probabilities are approximately:

\[
[0.665,\ 0.245,\ 0.090].
\]

Prediction:

\[
\boxed{\text{class 0}}
\]

because it has the highest probability.

The same principle applies to ten MNIST classes.

---

# 43. Why Classification Belongs After DIP Foundations

The sequence is intentional:

```text
Part I
→ what is an image?

Part II
→ how can we improve it?

Part III
→ how can we extract meaningful structure?

Part IV
→ how can we represent it efficiently?

Part V
→ how can we make decisions from it?
```

Classification therefore acts as a bridge from classical image processing toward intelligent vision.

---

# 44. Exam Lens

## 2-mark questions

**Define image classification.**  
The task of assigning an input image to one or more predefined categories according to a learned or designed decision function.

**What is a class label?**  
A categorical target assigned to an image under a specified classification task.

**What is a confusion matrix?**  
A table that records actual versus predicted class outcomes.

---

## 5-mark question

### Differentiate classification, detection and segmentation.

Use:

```text
classification → image-level label
detection       → labels + bounding boxes
segmentation    → pixel-level regions/classes
```

Then give one example.

---

## 10-mark question

### Explain an image-classification system.

Recommended sequence:

```text
dataset
→ preprocessing
→ representation
→ feature extraction
→ classifier
→ prediction
→ evaluation
→ error analysis
```

Then compare classical feature pipelines with CNN-based learning.

---

# 45. Chapter Checkpoint

### Q1

What is the difference between classification and object detection?

### Q2

Why can accuracy be misleading on highly imbalanced data?

### Q3

For:

\[
TP=80,\ TN=900,\ FP=10,\ FN=10,
\]

calculate accuracy.

### Q4

Why must preprocessing be kept consistent between training and inference?

### Q5

Why does an MNIST classifier normally have ten output classes?

### Q6

What does an off-diagonal confusion-matrix entry indicate?

---

# 46. One-Page Recall Sheet

```text
IMAGE CLASSIFICATION
│
├── Input
│   └── image
│
├── Goal
│   └── assign class
│
├── Pipeline
│   image
│    ↓
│   preprocessing
│    ↓
│   representation
│    ↓
│   features
│    ↓
│   classifier
│    ↓
│   prediction
│
├── Evaluation
│   ├── accuracy
│   ├── precision
│   ├── recall
│   ├── F1
│   └── confusion matrix
│
└── Deep-learning bridge
    └── learned features → CNN
```

---

# 47. Cross-Book Links

| Layer | Connection |
|---|---|
| MAIN | C25 establishes the classification task |
| MATH | Vector representation, softmax, metrics |
| LAB | Practical 8 — MNIST CNN classification |
| CODE | Dataset loading, preprocessing, model inference |
| EXAM | Classification vs detection/segmentation; evaluation |
| PRACTICE | Confusion matrices, metric calculations, architecture reasoning |
| RESOURCE | Course references for deep learning/computer vision |
| ASSETS | Classification pipelines, confusion matrices, tensor diagrams |
| MASTER | Dependency into C26–C28 |

---

# 48. Final Chapter Summary

The central mental model is:

\[
\boxed{
\text{image}
\rightarrow
\text{representation}
\rightarrow
\text{decision}
\rightarrow
\text{class}
}
\]

Classical systems often make the features explicitly.

Deep-learning systems can learn representations directly from images.

The university practical makes this transition concrete through:

```text
MNIST
→ CNN
→ handwritten-digit classification
```

which is developed fully in the next chapter. fileciteturn4file0L76-L80

---

**Next chapter:** C26 — Convolutional Neural Networks
