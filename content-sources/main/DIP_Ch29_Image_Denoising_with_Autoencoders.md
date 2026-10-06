---
id: "C29"
title: "Image Denoising with Autoencoders"
layer: "MAIN"
part: "V — From DIP to Intelligent Vision"
unit: "Unit IV"
version: "1.0"
status: "PRODUCTION"
syllabus_scope: "Image Denoising using Autoencoders"
tags:
  - digital-image-processing
  - denoising
  - autoencoder
  - convolutional-autoencoder
  - deep-learning
  - reconstruction
  - image-restoration
prerequisites:
  - "C09 — Smoothing and Noise Reduction"
  - "C14 — Image Restoration and Deblurring"
  - "C26 — Convolutional Neural Networks"
related_math:
  - "Reconstruction loss"
  - "Mean squared error"
  - "Tensor shapes"
  - "Gradient descent"
related_lab:
  - "LAB-04 — Noise Removal"
  - "LAB-08 — CNN-Based Image Classification"
related_code:
  - "CODE-09 — Autoencoder Denoising"
related_exam:
  - "EXAM-Autoencoder-Denoising"
related_practice:
  - "PRACTICE-Autoencoder"
---

# C29 — Image Denoising with Autoencoders

> **Chapter thesis:** A denoising autoencoder learns to map a corrupted image to a cleaner reconstruction by compressing and reconstructing visual information through a learned latent representation.

---

# 1. Why This Chapter Exists

Earlier chapters treated denoising primarily as an engineered filtering problem:

```text
noisy image
→ designed filter
→ cleaner image
```

C29 introduces a learned approach:

```text
noisy image
→ encoder
→ latent representation
→ decoder
→ reconstructed clean image
```

The university syllabus specifically requires:

> **Image Denoising using Autoencoders.** fileciteturn4file0L48-L52

The important transition is:

```text
hand-designed restoration rule
          ↓
learned reconstruction function
```

The goal is not to claim that autoencoders always outperform classical filters. The goal is to understand when and how a learned denoising system can work.

---

# 2. Learning Contract

After this chapter, you should be able to:

- define an autoencoder;
- distinguish encoder, latent representation and decoder;
- explain reconstruction as the learning objective;
- distinguish an ordinary autoencoder from a denoising autoencoder;
- explain the noisy-input/clean-target training setup;
- calculate simple reconstruction loss values;
- explain convolutional autoencoder structure;
- trace tensor shapes through encoder and decoder stages;
- explain why bottlenecks can encourage compact representations;
- explain the effect of the latent representation;
- understand training and inference for image denoising;
- implement a simple denoising autoencoder;
- compare learned denoising with classical filtering;
- identify failure modes such as over-smoothing and distribution mismatch.

---

# 3. What Is an Autoencoder?

An autoencoder learns a reconstruction function.

The structure is:

```text
input
  ↓
encoder
  ↓
latent representation
  ↓
decoder
  ↓
reconstruction
```

Let:

\[
x
\]

be the input.

The encoder is:

\[
z=f_{\theta}(x)
\]

and the decoder is:

\[
\hat{x}=g_{\phi}(z).
\]

Therefore:

\[
\boxed{
\hat{x}=g_{\phi}(f_{\theta}(x))
}
\]

The training objective is to make:

\[
\hat{x}\approx x.
\]

---

# 4. Ordinary Autoencoder

For a conventional autoencoder:

```text
clean image
→ encoder
→ latent
→ decoder
→ clean reconstruction
```

The target is usually the same image used as input.

The model learns:

\[
x\rightarrow\hat{x}.
\]

The reconstruction loss measures how closely the output matches the input.

---

# 5. Denoising Autoencoder

A denoising autoencoder changes the learning task:

```text
clean image
    │
    ├────► add corruption/noise
    │           │
    │           ▼
    │       noisy image
    │           │
    │           ▼
    │        encoder
    │           ↓
    │         latent
    │           ↓
    │        decoder
    │           ↓
    │      reconstructed
    │           │
    └───────────┘
       compare with
       clean target
```

Formally:

\[
x_{\text{clean}}
\rightarrow
\tilde{x}_{\text{noisy}}
\]

and the model learns:

\[
g_{\phi}(f_{\theta}(\tilde{x}))
\approx
x.
\]

The crucial distinction is:

> **The input is noisy; the target is clean.**

---

# 6. Why This Works

Suppose the network sees many examples of:

```text
clean image + noise
```

with the corresponding clean target.

It can learn statistical regularities such as:

```text
stable structure
vs.
random corruption
```

The network does not simply “know what noise is.” It learns from the training distribution.

Therefore the quality of denoising strongly depends on:

- noise model;
- training data;
- image domain;
- architecture;
- loss;
- optimization;
- deployment distribution.

---

# 7. Denoising Pipeline

The complete training workflow is:

```text
clean training images
        ↓
noise/corruption generation
        ↓
noisy training images
        ↓
encoder
        ↓
latent representation
        ↓
decoder
        ↓
reconstructed clean images
        ↓
loss against clean targets
        ↓
backpropagation
        ↓
parameter update
```

At inference:

```text
new noisy image
      ↓
trained denoising autoencoder
      ↓
cleaner reconstruction
```

No clean target is needed during inference.

---

# 8. Encoder

The encoder maps an image into a latent representation:

\[
z=f_{\theta}(x).
\]

It can use convolution, activation and downsampling operations:

```text
image
 ↓
Conv
 ↓
ReLU
 ↓
Downsample
 ↓
Conv
 ↓
ReLU
 ↓
latent feature maps
```

The representation generally has fewer spatial degrees of freedom than the original image.

---

# 9. Decoder

The decoder maps the latent representation back into image space:

\[
\hat{x}=g_{\phi}(z).
\]

A convolutional decoder can use:

```text
latent
 ↓
upsampling / transpose convolution
 ↓
activation
 ↓
upsampling
 ↓
reconstruction
```

Its goal is to recreate the target image at the desired resolution.

---

# 10. Latent Representation

The latent variable:

\[
z
\]

is a learned intermediate representation.

Conceptually:

```text
input image
████████████████
        ↓
     encoder
        ↓
   compact features
        ↓
     decoder
        ↓
reconstructed image
████████████████
```

A bottleneck may force the network to retain information that is useful for reconstruction.

However:

> **A small latent tensor does not automatically guarantee that it contains only “important” semantic information.**

The learned representation depends on the objective and architecture.

---

# 11. Reconstruction Loss

A common choice for image reconstruction is mean squared error:

\[
MSE=
\frac{1}{N}
\sum_{i=1}^{N}
(x_i-\hat{x}_i)^2.
\]

For an image:

\[
L=
\frac{1}{HWC}
\sum_{h,w,c}
(x_{h,w,c}-\hat{x}_{h,w,c})^2.
\]

This gives the network a quantitative target.

---

# 12. Worked MSE Example

Suppose a four-pixel clean target is:

\[
x=
[10,20,30,40]
\]

and reconstruction is:

\[
\hat{x}=
[11,18,33,39].
\]

Errors:

\[
[-1,2,-3,1].
\]

Squared errors:

\[
[1,4,9,1].
\]

Therefore:

\[
MSE=
\frac{1+4+9+1}{4}
=
\frac{15}{4}
=
\boxed{3.75}.
\]

Lower MSE means the reconstruction is numerically closer under this particular loss.

---

# 13. Other Reconstruction Losses

MSE is not the only possibility.

A denoising system can use alternatives such as:

- mean absolute error;
- perceptual losses;
- task-specific losses;
- combinations of losses.

For a university introduction, MSE is a useful starting point because it is easy to understand and calculate.

Do not assume that lowest MSE always means best perceptual image quality.

---

# 14. Convolutional Autoencoder

For images, fully connected autoencoders are often inefficient because they ignore spatial structure.

A convolutional autoencoder preserves spatial organization:

```text
Input image
   ↓
Conv + activation
   ↓
Downsampling
   ↓
Conv + activation
   ↓
Latent
   ↓
Upsampling / transpose convolution
   ↓
Conv + activation
   ↓
Output image
```

This connects directly to C26.

---

# 15. Tensor Shape Example

Suppose the noisy input is:

\[
28\times28\times1.
\]

A simple encoder:

```text
28×28×1
 ↓ Conv
28×28×32
 ↓ Pool
14×14×32
 ↓ Conv
14×14×64
 ↓ Pool
7×7×64
```

The latent representation has:

\[
7\times7\times64
=
3136
\]

values.

The decoder reverses the spatial reduction:

```text
7×7×64
 ↓ upsample
14×14×64
 ↓ conv
14×14×32
 ↓ upsample
28×28×32
 ↓ conv
28×28×1
```

Exact architecture choices are not fixed by the syllabus.

---

# 16. Why the Encoder Compresses

Downsampling reduces spatial resolution.

For example:

\[
28\times28
\rightarrow
14\times14
\rightarrow
7\times7.
\]

This encourages the representation to capture broader structures.

But information can be lost through aggressive downsampling.

The decoder therefore has to reconstruct fine detail from the latent representation.

---

# 17. Denoising as a Learned Prior

A useful engineering interpretation is:

> The trained network learns a statistical prior for what clean images from its training domain tend to look like.

For example, if the network is trained on handwritten digits, it learns regularities of handwritten-digit images.

That can allow it to reconstruct plausible clean structure from noisy observations.

But the same network may perform poorly on a very different domain.

---

# 18. Noise Model Matters

Consider:

```text
Gaussian noise
salt-and-pepper noise
speckle noise
```

A model trained primarily on one corruption type may not generalize equally well to another.

This is a key connection to C09.

```text
C09
noise models
+
classical filtering

C29
learned denoising
+
training distribution
```

---

# 19. Synthetic Noise for Training

A common educational workflow is:

```text
clean image
→ add known synthetic noise
→ train on noisy/clean pair
```

For Gaussian noise:

\[
\tilde{x}=x+n
\]

where:

\[
n\sim\mathcal{N}(0,\sigma^2)
\]

in a simplified additive model.

The noise level \(\sigma\) controls corruption strength.

---

# 20. Worked Noise Example

Suppose:

\[
x=100
\]

and noise sample:

\[
n=8.
\]

Then:

\[
\tilde{x}=100+8=108.
\]

If a model receives:

\[
108
\]

but the target is:

\[
100,
\]

the learning process encourages the reconstruction toward the clean value.

This simple scalar example illustrates the training idea.

---

# 21. Why Over-Smoothing Can Occur

Suppose a small texture has little statistical support in the training data.

A denoising model may remove it along with noise.

The result can become:

```text
noise ↓
detail ↓
```

Therefore:

\[
\boxed{
\text{cleaner image} \not\Rightarrow \text{more faithful image}
}
\]

Denoising always involves a trade-off between suppression of corruption and preservation of real detail.

---

# 22. Autoencoder vs Classical Filter

| Property | Classical filter | Denoising autoencoder |
|---|---|---|
| Main mechanism | Designed mathematical operation | Learned nonlinear mapping |
| Training required | No | Yes |
| Noise assumptions | Often explicit/known | Learned from training data |
| Adaptation to domain | Manual parameter/design choices | Data-driven |
| Computation | Often lightweight | Potentially substantial |
| Generalization | Rule-based | Depends strongly on training distribution |
| Interpretability | Often easier | More complex |
| Can learn complex restoration | Limited by chosen model | Potentially strong |

Neither approach dominates every image-restoration problem.

---

# 23. Autoencoder vs CNN Classifier

C26:

```text
image
→ CNN
→ class
```

C29:

```text
noisy image
→ encoder
→ latent
→ decoder
→ image
```

The output task is different.

Classification outputs a label.

Denoising outputs an image.

---

# 24. Training Target Matters

Suppose:

```text
input = noisy image
target = noisy image
```

That is not the same denoising objective.

For denoising:

```text
input  = noisy image
target = clean image
```

This must be explicit in both code and experiment documentation.

---

# 25. Keras Denoising Autoencoder

A simple educational convolutional model:

```python
from __future__ import annotations

import numpy as np
from tensorflow import keras
from tensorflow.keras import layers


def build_denoising_autoencoder() -> keras.Model:
    inputs = keras.Input(shape=(28, 28, 1))

    # Encoder
    x = layers.Conv2D(32, 3, activation="relu", padding="same")(inputs)
    x = layers.MaxPooling2D(2, padding="same")(x)

    x = layers.Conv2D(64, 3, activation="relu", padding="same")(x)
    latent = layers.MaxPooling2D(2, padding="same", name="latent")(x)

    # Decoder
    x = layers.Conv2D(64, 3, activation="relu", padding="same")(latent)
    x = layers.UpSampling2D(2)(x)

    x = layers.Conv2D(32, 3, activation="relu", padding="same")(x)
    x = layers.UpSampling2D(2)(x)

    outputs = layers.Conv2D(1, 3, activation="sigmoid", padding="same")(x)

    return keras.Model(inputs, outputs)


model = build_denoising_autoencoder()
model.compile(
    optimizer="adam",
    loss="mse",
)

model.summary()
```

This is a teaching architecture, not the only valid autoencoder design.

---

# 26. Generating Noisy Training Data

For normalized images in \([0,1]\):

```python
rng = np.random.default_rng(42)

noise_strength = 0.20
noise = noise_strength * rng.normal(
    size=x_train.shape
).astype("float32")

x_noisy = np.clip(
    x_train + noise,
    0.0,
    1.0,
)
```

Then:

```python
model.fit(
    x_noisy,
    x_train,
    epochs=10,
    batch_size=128,
    validation_split=0.1,
)
```

The key relationship is:

```text
x_noisy → input
x_train → clean target
```

---

# 27. Inference

```python
reconstructed = model.predict(
    x_noisy[:10],
    verbose=0,
)
```

The output should be compared against:

```text
clean target
```

rather than simply against the noisy input.

---

# 28. Practical Visualization

Display three images side by side conceptually:

```text
NOISY             RECONSTRUCTED          CLEAN

████████          ████████               ████████
██▒██▒██          ████████               ████████
████▒███          ████████               ████████
```

The three-way comparison is much more informative than showing only the output.

Measure:

```text
noisy vs clean
reconstructed vs clean
```

to see whether denoising reduced error.

---

# 29. Denoising Evaluation

Let:

\[
MSE_{\text{noisy}}
\]

be the MSE between noisy and clean images.

Let:

\[
MSE_{\text{recon}}
\]

be the MSE between reconstructed and clean images.

A useful result is:

\[
MSE_{\text{recon}}
<
MSE_{\text{noisy}}.
\]

That indicates numerical improvement under MSE.

But also inspect:

- edges;
- texture;
- small structures;
- ringing;
- blur.

---

# 30. PSNR Comparison

For 8-bit images:

\[
PSNR=
10\log_{10}
\left(
\frac{255^2}{MSE}
\right).
\]

If MSE decreases, PSNR increases.

But PSNR remains only one evaluation dimension.

---

# 31. Failure Mode — Distribution Shift

Training:

```text
Gaussian noise
σ = 0.1
```

Deployment:

```text
strong salt-and-pepper noise
```

The network may fail.

This is not necessarily a coding error.

It may be a mismatch between training and deployment distributions.

---

# 32. Failure Mode — Hallucinated Detail

A learned restoration model can produce visually plausible structure that was not actually present in the observation.

For ordinary photographs this may be visually acceptable in some contexts.

For scientific or medical workflows, it can be dangerous.

Therefore:

> **Restoration quality must be judged according to the application's evidence requirements.**

---

# 33. Failure Mode — Edge Loss

A model may suppress noise near edges but unintentionally blur the edge.

Compare:

```text
ideal edge:
████████

over-smoothed:
████▒▒▒▒
```

Evaluation should therefore include local edge inspection.

---

# 34. Engineering Comparison

Suppose:

```text
input noise is well characterized
+
very low latency required
+
limited compute
```

A classical filter may be attractive.

Suppose:

```text
large representative training dataset
+
complex noise patterns
+
sufficient compute
```

A learned denoiser may be attractive.

The choice is driven by system requirements.

---

# 35. Autoencoder Architecture Variants

Common conceptual variations include:

### Undercomplete

Latent representation is smaller than the input.

### Convolutional

Uses spatially structured feature extraction.

### Denoising

Input is corrupted; target is clean.

### Sparse / regularized

Adds constraints encouraging particular latent behaviour.

The syllabus requires denoising with autoencoders; the other terms are supporting context.

---

# 36. Why a Bottleneck Does Not Guarantee Perfect Compression

A model can still encode information through distributed features.

Also, skip connections can bypass a bottleneck in some architectures.

Therefore:

> **Architecture determines the information path; it does not guarantee one simple semantic meaning for the latent vector.**

---

# 37. Exam Lens

## 2-mark questions

**What is an autoencoder?**  
A neural network trained to reconstruct an input through an encoder, latent representation and decoder.

**What is a denoising autoencoder?**  
An autoencoder trained using a corrupted input and a clean target.

**What is the main loss in a basic image reconstruction example?**

\[
MSE.
\]

---

# 38. 5-Mark Question

### Explain denoising using an autoencoder.

Use:

```text
clean image
→ add noise
→ noisy image
→ encoder
→ latent representation
→ decoder
→ reconstructed image
→ compare with clean target
→ update weights
```

Then explain why the model can learn noise-resistant representations.

---

# 39. 10-Mark Question

### Explain a convolutional denoising autoencoder.

Include:

1. motivation;
2. noisy/clean pair;
3. encoder;
4. latent representation;
5. decoder;
6. reconstruction loss;
7. training loop;
8. inference;
9. evaluation;
10. advantages;
11. limitations;
12. domain-shift concerns.

---

# 40. Numerical Practice

Given:

\[
x=[50,100,150]
\]

and:

\[
\hat{x}=[55,98,147].
\]

Calculate:

\[
MSE.
\]

Errors:

\[
[-5,2,3].
\]

Squared:

\[
[25,4,9].
\]

Thus:

\[
MSE=
\frac{25+4+9}{3}
=
\boxed{\frac{38}{3}\approx12.67}.
\]

---

# 41. Chapter Checkpoint

### Q1

What is the difference between an ordinary autoencoder and a denoising autoencoder?

### Q2

Why must the noisy image be the input and the clean image be the target?

### Q3

Why can a denoiser remove useful detail?

### Q4

Why can a model trained on Gaussian noise perform poorly on another noise type?

### Q5

Why is a lower MSE not sufficient to prove that an image looks better?

### Q6

What happens during inference that differs from training?

---

# 42. One-Page Recall Sheet

```text
DENOISING AUTOENCODER
│
├── Clean image
│      ↓ add noise
│   Noisy image
│      ↓
├── Encoder
│      ↓
├── Latent representation
│      ↓
├── Decoder
│      ↓
├── Reconstructed image
│      ↓
└── Compare with clean target

Training:
noisy → network → clean target → loss → backprop

Inference:
new noisy image → trained network → reconstruction
```

---

# 43. Cross-Book Links

| Layer | Connection |
|---|---|
| MAIN | C29 explains learned image denoising |
| MATH | MSE, noise model, tensor dimensions |
| LAB | Practical 4 noise removal + advanced denoising extension |
| CODE | TensorFlow/Keras convolutional autoencoder |
| EXAM | Autoencoder architecture and denoising pipeline |
| PRACTICE | Loss calculations, architecture reasoning, failure diagnosis |
| RESOURCE | Course deep-learning/computer-vision references |
| ASSETS | Encoder-decoder pipeline, noisy/clean/reconstructed triptych |
| MASTER | Links classical restoration to learned restoration |

---

# 44. Final Chapter Summary

The essential architecture is:

\[
\boxed{
\text{noisy image}
\rightarrow
\text{encoder}
\rightarrow
\text{latent representation}
\rightarrow
\text{decoder}
\rightarrow
\text{cleaner reconstruction}
}
\]

Training uses:

\[
\boxed{
\text{noisy input}
\rightarrow
\text{clean target}
}
\]

The central engineering limitation is:

\[
\boxed{
\text{learned denoising depends on its training distribution}
}
\]

C29 therefore extends the classical denoising/restoration concepts from C09 and C14 into the deep-learning part of the course.

The next chapter changes the input structure from one image to a sequence:

```text
C29
one noisy image → restored image

C30
frame t + frame t+1 → motion information
```

---

**Next chapter:** C30 — Video Processing and Motion Analysis
