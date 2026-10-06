---
id: "CODE-00"
title: "Digital Image Processing — Coding Environment & Conventions"
layer: "PRACTICAL/CODE"
system: "Engineering Minibooks · Digital Image Processing"
version: "1.0"
status: "FOUNDATION LOCK"
---

# CODE-00 — Coding Environment & Conventions

> **Role:** Establish implementation conventions so MATLAB and Python/OpenCV examples remain reproducible and technically consistent with the mathematics.

---

# 1. Supported Implementation Paths

The practical system may use:

```text
MATLAB
Python + NumPy
Python + OpenCV
Python + Pillow
Python + SciPy
Python + Matplotlib
TensorFlow/Keras or another declared deep-learning framework
```

A specific experiment should use only the dependencies it actually needs.

---

# 2. The Four-Layer Implementation Pattern

Every substantial implementation follows:

```text
INPUT
→ REPRESENTATION
→ OPERATION
→ OUTPUT
```

For more complex work:

```text
load
→ inspect
→ preprocess
→ process
→ evaluate
→ visualize
```

---

# 3. Image Inspection Standard

Before processing an unfamiliar image, inspect:

```text
shape
channels
datatype
minimum
maximum
colour representation
file format
```

This catches many implementation mistakes before the algorithm runs.

---

# 4. Channel Convention

Document channel conventions explicitly.

Important example:

```text
Many image libraries represent colour channels differently.
```

Never assume that a variable named `RGB` guarantees the underlying channel order.

The Code layer should state the actual representation used in the example.

---

# 5. Numeric Range Convention

Declare whether the current operation expects:

```text
0–255 integer
0–1 normalized float
another explicitly stated range
```

Avoid silently mixing ranges.

---

# 6. Datatype Discipline

Pay attention to:

```text
uint8
uint16
float32
float64
```

Operations may behave differently because of:

- overflow,
- clipping,
- scaling,
- conversion,
- rounding.

Examples should expose these issues where they are pedagogically important.

---

# 7. Border Handling

Spatial operations must state the border policy when the output depends on it.

Possible conventions include:

```text
zero padding
replication
reflection
circular
valid/interior-only
```

Do not leave the assumption hidden.

---

# 8. Reproducibility

Record:

```text
software
version
library/toolbox
data source
parameters
random seed where applicable
model weights/version
```

---

# 9. MATLAB Pattern

A typical classical DIP implementation:

```text
read
→ inspect
→ convert if needed
→ process
→ display
→ quantify
→ save/result
```

Where a toolbox is required, state it.

---

# 10. Python Pattern

Typical workflow:

```text
read
→ NumPy/OpenCV representation
→ inspect dtype/range
→ process
→ visualize
→ evaluate
```

Keep library-specific behaviour explicit.

---

# 11. Code vs Library Call

Library calls are useful, but the learning material should explain the algorithm they execute.

For example:

```text
cv2.GaussianBlur(...)
```

must not be treated as an explanation of Gaussian filtering.

The Code file should connect:

```text
concept
→ formula
→ parameters
→ function
→ output
```

---

# 12. Debugging Contract

When code fails or produces an unexpected image:

```text
OBSERVE
→ isolate
→ inspect representation
→ test minimal case
→ identify cause
→ correct
→ re-run
→ verify output
```

---

# 13. Code Testing

Useful tests include:

- constant image,
- tiny matrix,
- known synthetic pattern,
- identity-like case,
- maximum/minimum intensities,
- controlled noise,
- known transformation.

Synthetic tests often reveal mistakes more clearly than large photographs.

---

# 14. Visualization Standard

Implementation results should show enough evidence to interpret the operation.

Examples:

```text
original + filtered
original + histogram
image + spectrum
image + segmentation mask
input + detections
clean + noisy + restored
```

---

# 15. Code QA

- [ ] Code runs under the declared environment.
- [ ] Inputs are valid.
- [ ] Output dimensions make sense.
- [ ] datatype/range is understood.
- [ ] parameters are explained.
- [ ] implementation matches stated algorithm or clearly identifies a library approximation.
- [ ] result is interpretable.
- [ ] no hidden dependency is required.

---

# 16. Definition of Done

CODE-00 is complete when all later code files can inherit a consistent:

```text
environment
representation convention
parameter convention
testing approach
visualization approach
debugging approach
```
