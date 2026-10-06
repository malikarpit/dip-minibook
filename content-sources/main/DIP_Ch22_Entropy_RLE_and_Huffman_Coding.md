---
id: "C22"
title: "Entropy, Run-Length Encoding and Huffman Coding"
layer: "MAIN"
part: "IV — Compressing Images"
unit: "Unit III"
version: "1.0"
status: "PRODUCTION"
syllabus_scope: "Supporting foundation for Image Compression; directly prepares JPEG and lossless/lossy comparison"
tags:
  - digital-image-processing
  - entropy
  - information-theory
  - run-length-encoding
  - huffman-coding
  - lossless-compression
prerequisites:
  - "C21 — Image Compression Fundamentals"
related_math:
  - "Probability"
  - "Logarithms"
  - "Entropy"
related_lab:
  - "LAB-07 — Image Compression"
related_code:
  - "CODE-07 — Compression Implementations"
related_exam:
  - "EXAM-Entropy-Coding"
related_practice:
  - "PRACTICE-Entropy-RLE-Huffman"
---

# C22 — Entropy, Run-Length Encoding and Huffman Coding

> **Chapter thesis:** Efficient lossless compression begins by understanding how much information a source contains and then assigning compact representations to predictable patterns.

---

# 1. Why This Chapter Exists

C21 established the question:

> Why can an image be represented with fewer bits?

C22 moves from intuition to coding.

The central path is:

```text
symbol probabilities
       ↓
information
       ↓
entropy
       ↓
coding efficiency
       ↓
RLE / Huffman coding
       ↓
compressed representation
```

The focus is not merely on memorizing algorithms. You should understand **why the code lengths make sense** and how the ideas later appear inside JPEG.

---

# 2. Learning Contract

You should be able to:

- explain information content;
- calculate self-information;
- calculate entropy for a discrete distribution;
- explain what entropy does and does not mean;
- encode simple data using Run-Length Encoding (RLE);
- explain when RLE is effective;
- construct a Huffman tree;
- assign prefix codes;
- calculate weighted average code length;
- calculate coding efficiency and redundancy;
- compare fixed-length and variable-length coding;
- explain why Huffman coding is lossless;
- connect entropy coding to JPEG.

---

# 3. Symbols, Probabilities and Information

Imagine a source that emits symbols.

For an image, a symbol could be:

- a grayscale value;
- a quantized coefficient;
- a run/value pair;
- another intermediate representation selected by a codec.

Let:

\[
X\in\{x_1,x_2,\ldots,x_n\}.
\]

Each symbol has probability:

\[
P(X=x_i)=p_i.
\]

The probabilities satisfy:

\[
\sum_{i=1}^{n}p_i=1.
\]

---

# 4. Self-Information

A rare event is more informative than an event that was highly predictable.

For symbol \(x_i\), self-information is:

\[
I(x_i)=-\log_2 p_i.
\]

Equivalent form:

\[
I(x_i)=\log_2\frac{1}{p_i}.
\]

### Example

If:

\[
p=0.5,
\]

then:

\[
I=-\log_2(0.5)=1
\]

bit.

If:

\[
p=0.125,
\]

then:

\[
I=-\log_2(0.125)=3
\]

bits.

So:

```text
probability ↓
information ↑
```

This does not yet define an entire compression code. It defines the information associated with one event.

---

# 5. Why the Logarithm Is Used

The logarithm gives information a useful additive property.

Suppose two independent events have probabilities:

\[
p_1,\quad p_2.
\]

The combined probability is:

\[
p_1p_2.
\]

Their information is:

\[
-\log_2(p_1p_2)
\]

which becomes:

\[
-\log_2p_1-\log_2p_2.
\]

Thus independent information contributions add.

The base 2 gives the unit:

\[
\boxed{\text{bits}}.
\]

---

# 6. Entropy

The source entropy is the expected information per symbol:

\[
\boxed{
H(X)=
-\sum_i p_i\log_2p_i
}
\]

This is one of the most important formulas in information-theoretic compression.

---

# 7. Worked Example — Entropy

Suppose an image source produces four symbols:

| Symbol | Probability |
|---|---:|
| A | 0.50 |
| B | 0.25 |
| C | 0.125 |
| D | 0.125 |

Then:

\[
H=
-(0.5\log_2 0.5
+0.25\log_2 0.25
+0.125\log_2 0.125
+0.125\log_2 0.125).
\]

Now:

\[
-\log_2(0.5)=1
\]

\[
-\log_2(0.25)=2
\]

\[
-\log_2(0.125)=3.
\]

Therefore:

\[
H
=
0.5(1)+0.25(2)+0.125(3)+0.125(3).
\]

\[
=0.5+0.5+0.375+0.375
\]

\[
=\boxed{1.75\text{ bits/symbol}}.
\]

---

# 8. Entropy Is an Average, Not a Code

This distinction matters.

Entropy of:

\[
1.75\text{ bits/symbol}
\]

does **not** mean that every symbol must be encoded using 1.75 bits.

A code operates with actual codewords.

For example:

```text
A → 0
B → 10
C → 110
D → 111
```

has lengths:

```text
A = 1
B = 2
C = 3
D = 3
```

The weighted average length is:

\[
L
=
0.5(1)+0.25(2)+0.125(3)+0.125(3)
\]

\[
=1.75.
\]

This particular distribution is an ideal example where the average code length reaches the entropy value exactly.

---

# 9. Entropy Bounds

For a discrete source:

\[
H(X)\ge0.
\]

If there are \(M\) possible symbols:

\[
H(X)\le\log_2M.
\]

The maximum occurs for a uniform distribution.

### Example

For four equally likely symbols:

\[
p_i=\frac14.
\]

Then:

\[
H=
-\sum_{i=1}^{4}
\frac14\log_2\frac14
\]

and because:

\[
-\log_2\frac14=2,
\]

we get:

\[
H=4\cdot\frac14\cdot2=2.
\]

Thus:

\[
\boxed{H_{\max}=2\text{ bits/symbol}}.
\]

---

# 10. Predictability and Entropy

Compare:

### Case A — Uniform

```text
A B C D
25% each
```

High uncertainty.

### Case B — Highly skewed

```text
A = 97%
B = 1%
C = 1%
D = 1%
```

Low uncertainty.

The second source is much more predictable and therefore offers greater opportunity for variable-length coding.

This is the conceptual bridge:

\[
\boxed{
\text{lower uncertainty}
\Rightarrow
\text{potentially shorter average code}
}
\]

---

# 11. Entropy and the Best Possible Average Code Length

For important classes of prefix codes, the entropy acts as a lower bound on the ideal average code length.

Conceptually:

\[
H(X)
\le L
\]

where \(L\) is the average number of bits per symbol of a suitable uniquely decodable code.

For binary Huffman coding, a standard bound is:

\[
H(X)\le L < H(X)+1
\]

for the source model under the usual coding assumptions.

The important interpretation is:

> **Entropy tells us the information-theoretic floor; a practical code tries to approach it.**

---

# 12. Coding Redundancy

Suppose a fixed-length code uses:

\[
L_{\text{fixed}}
\]

bits per symbol, while a variable-length code uses:

\[
L_{\text{avg}}.
\]

The extra average representation beyond the source entropy can be considered coding inefficiency.

A simple fractional redundancy measure is:

\[
R=
1-\frac{H}{L}.
\]

This is one useful engineering metric; naming conventions vary in different texts.

### Example

Suppose:

\[
H=1.75
\]

and a code uses:

\[
L=2.
\]

Then:

\[
R=1-\frac{1.75}{2}
=0.125.
\]

So the fractional redundancy is:

\[
\boxed{12.5\%}.
\]

---

# 13. Fixed-Length Coding

If there are \(M\) equally represented possible symbols, a simple fixed-length binary code requires:

\[
\lceil\log_2M\rceil
\]

bits per symbol.

For:

\[
M=256,
\]

we need:

\[
\log_2 256=8
\]

bits.

That is exactly the standard 8-bit grayscale representation.

But if one intensity is much more common than others, fixed-length coding ignores that statistical structure.

This motivates variable-length coding.

---

# 14. Run-Length Encoding

**Run-Length Encoding (RLE)** represents consecutive repeated symbols as a value plus its run length.

Instead of:

```text
AAAAABBBCC
```

store:

```text
A×5
B×3
C×2
```

or a pair sequence:

```text
(5,A) (3,B) (2,C)
```

The exact storage order depends on the implementation.

---

# 15. Why RLE Works

RLE exploits a very specific form of redundancy:

> **long repeated runs.**

This is different from general probability-based entropy coding.

RLE is highly effective when:

```text
AAAAAAA
BBBB
CCCCCCCC
```

occurs frequently.

It can be poor when the data alternates:

```text
ABABABABABAB
```

because there are many short runs.

---

# 16. Worked Example — RLE

Input:

```text
AAAAAABBCCCCCCCCDD
```

Count:

```text
A → 6
B → 2
C → 8
D → 2
```

RLE representation:

```text
(6,A) (2,B) (8,C) (2,D)
```

Original symbol count:

\[
6+2+8+2=18.
\]

There are now four run records instead of 18 raw symbols.

The actual bit saving depends on how the pair \((count,symbol)\) is represented.

This is important:

> **RLE is not automatically smaller. The representation overhead matters.**

---

# 17. RLE on Binary Images

RLE is especially intuitive on binary images.

Suppose a row is:

```text
000000001111110000
```

A run description can be:

```text
8 zeros
6 ones
4 zeros
```

For images dominated by large foreground/background regions, this can be extremely compact.

A scanned document with large blank areas is a good conceptual example.

---

# 18. RLE Failure Case

Consider:

```text
010101010101010101
```

The runs are:

```text
0,1,0,1,0,1,...
```

Almost every run has length 1.

Instead of making the representation dramatically shorter, an RLE format may add overhead.

This leads to a general rule:

\[
\boxed{\text{RLE efficiency depends on run structure}}
\]

---

# 19. Huffman Coding

Huffman coding is a variable-length, prefix-free coding method.

The core principle is:

```text
high probability
→ shorter codeword

low probability
→ longer codeword
```

The resulting code is designed so that no valid codeword is a prefix of another.

This allows unambiguous decoding.

---

# 20. Prefix-Free Codes

Consider:

```text
A → 0
B → 10
C → 110
D → 111
```

No codeword is a prefix of another.

For example:

- `0` is not the beginning of any longer valid codeword;
- `10` is not the beginning of `110` or `111`.

This property allows the decoder to read the stream without explicit separators between symbols.

---

# 21. Why Prefix Freedom Matters

Suppose the stream is:

```text
010110111
```

The decoder can parse:

```text
0 | 10 | 110 | 111
```

so:

```text
A | B | C | D
```

No commas are needed.

A code such as:

```text
A → 0
B → 01
```

would be problematic for simple prefix decoding because `0` is a prefix of `01`.

---

# 22. Huffman Algorithm

Given symbol probabilities/frequencies:

1. Create one node for each symbol.
2. Select the two least frequent nodes.
3. Combine them into one parent node.
4. Assign the combined frequency as their sum.
5. Repeat until one tree remains.
6. Assign binary digits to branches.
7. Read each symbol's path from root to leaf.

The exact left/right assignment can vary.

If left and right are swapped consistently, the code changes but its optimal average length does not.

---

# 23. Worked Huffman Example

Suppose:

| Symbol | Frequency |
|---|---:|
| A | 45 |
| B | 25 |
| C | 15 |
| D | 10 |
| E | 5 |

Total:

\[
100.
\]

We combine the two smallest:

\[
E(5)+D(10)=15.
\]

Now:

```text
A = 45
B = 25
C = 15
DE = 15
```

Combine:

\[
C(15)+DE(15)=30.
\]

Now:

```text
A 45
B 25
CDE 30
```

Combine:

\[
B(25)+CDE(30)=55.
\]

Finally:

\[
A(45)+BCDE(55)=100.
\]

One valid tree produces, for example:

```text
A     → 0
B     → 10
C     → 110
D     → 1110
E     → 1111
```

The exact bit assignments can differ while preserving the same code lengths.

---

# 24. Average Huffman Code Length

Code lengths:

| Symbol | Probability | Code length |
|---|---:|---:|
| A | 0.45 | 1 |
| B | 0.25 | 2 |
| C | 0.15 | 3 |
| D | 0.10 | 4 |
| E | 0.05 | 4 |

Then:

\[
L=
0.45(1)
+0.25(2)
+0.15(3)
+0.10(4)
+0.05(4).
\]

\[
=0.45+0.50+0.45+0.40+0.20
\]

\[
=\boxed{2.00\text{ bits/symbol}}.
\]

---

# 25. Compare with Fixed-Length Coding

There are 5 possible symbols.

A simple fixed-length binary code requires:

\[
\lceil\log_2 5\rceil=3
\]

bits/symbol.

Huffman:

\[
2.0\text{ bits/symbol}
\]

Fixed:

\[
3.0\text{ bits/symbol}
\]

So Huffman reduces the average representation length.

For 1000 symbols:

Fixed:

\[
1000\times3=3000\text{ bits}.
\]

Huffman, ignoring tree/header overhead:

\[
1000\times2=2000\text{ bits}.
\]

Idealized saving:

\[
1000\text{ bits}.
\]

---

# 26. Important Huffman Caveat — Tree Overhead

A practical compressed file must also communicate enough information for the decoder to reconstruct the code.

Therefore:

```text
total file size
=
encoded payload
+
code/tree metadata
+
format/header overhead
```

For very small images, overhead can dominate.

This is one reason theoretical bit counts should not automatically be equated with actual file size.

---

# 27. Huffman Is Lossless

Huffman coding does not intentionally discard source symbols.

The decoder reconstructs the exact sequence represented by the code.

Conceptually:

\[
\boxed{D(E(S))=S}
\]

where \(S\) is the source symbol sequence.

Therefore Huffman belongs to the **lossless coding** family.

---

# 28. RLE vs Huffman

| Property | RLE | Huffman |
|---|---|---|
| Main idea | Encode runs | Encode symbols with variable-length prefix codes |
| Exploits | Consecutive repetition | Symbol probability |
| Best for | Long runs | Unequal probabilities |
| Needs probability model? | No | Yes, explicitly or implicitly |
| Lossless | Yes | Yes |
| Can work together? | Yes | Yes |

They are not competitors in every system.

A codec may first transform data into a representation with many repeated or sparse values and then use entropy coding.

---

# 29. RLE + Entropy Coding

A common compression design principle is:

```text
Input
 ↓
Transform / rearrange
 ↓
Create simpler statistics
 ↓
RLE or related representation
 ↓
Entropy coding
 ↓
Bitstream
```

The exact pipeline depends on the codec.

This pattern becomes important when understanding JPEG's run-based coding of quantized AC coefficients.

---

# 30. Image Example — Why Transform Coding Helps Entropy Coding

Imagine an 8×8 transform block after quantization:

```text
12   4   1   0   0   0   0   0
 3   1   0   0   0   0   0   0
 1   0   0   0   0   0   0   0
 0   0   0   0   0   0   0   0
 0   0   0   0   0   0   0   0
 0   0   0   0   0   0   0   0
 0   0   0   0   0   0   0   0
 0   0   0   0   0   0   0   0
```

There are many zeros.

A poor representation might explicitly store every zero separately.

A better system can exploit the runs of zeros.

This is part of the reason the DCT + quantization + entropy-coding architecture works so well for photographic images.

---

# 31. Entropy Calculation — Matrix/Frequency View

Suppose a small grayscale image contains:

```text
0 0 0 1
0 0 1 1
0 1 1 1
1 1 1 1
```

Count:

- zeros = 6
- ones = 10

Total:

\[
16.
\]

Thus:

\[
p(0)=\frac{6}{16}=0.375
\]

\[
p(1)=\frac{10}{16}=0.625.
\]

Entropy:

\[
H
=
-0.375\log_2(0.375)
-0.625\log_2(0.625).
\]

Numerically:

\[
H\approx0.954\text{ bits/pixel}.
\]

A naive binary fixed-length representation uses:

\[
1\text{ bit/pixel}.
\]

This source has entropy slightly below that fixed-length representation, indicating limited opportunity for further lossless improvement under this simple symbol model.

---

# 32. Entropy Does Not Mean “Compressibility” in Isolation

Entropy depends on the model.

A source may have dependencies between neighbouring symbols even when the single-symbol distribution looks uniform.

For example:

```text
0101010101010101...
```

has:

\[
P(0)\approx0.5,\quad P(1)\approx0.5.
\]

Single-symbol entropy is close to:

\[
1\text{ bit/symbol}.
\]

Yet the sequence is highly structured.

A model that captures **relationships between symbols** can exploit that structure.

Therefore:

> **A first-order symbol entropy estimate can miss spatial dependencies.**

This is a major conceptual insight for image compression.

---

# 33. Zero-Order vs Contextual Thinking

### Zero-order model

Treat each symbol independently:

\[
P(X_i).
\]

### Contextual model

Use previous symbols or neighbourhood information:

\[
P(X_i\mid X_{i-1},\ldots).
\]

Images contain strong spatial context, so practical codecs often exploit more than a simple independent-symbol model.

This explains why predicting or transforming image data before entropy coding can be powerful.

---

# 34. Entropy and Quantization Have Different Roles

Do not confuse these two.

### Quantization

Changes/limits numeric precision.

In lossy compression, it can discard information.

### Entropy coding

Represents already-selected symbols using fewer bits.

It is generally lossless with respect to those symbols.

So:

```text
quantization
→ may lose information

entropy coding
→ efficiently stores the resulting information
```

This distinction is essential for understanding JPEG.

---

# 35. JPEG Connection Preview

A simplified conceptual JPEG pipeline is:

```text
RGB
 ↓
colour transform
 ↓
8×8 blocks
 ↓
DCT
 ↓
quantization   ← major lossy stage
 ↓
zig-zag order
 ↓
RLE / coefficient representation
 ↓
entropy coding
 ↓
JPEG bitstream
```

C23 explains the DCT.

C24 explains the complete JPEG flow.

C22 gives the coding concepts needed to understand the final stages.

---

# 36. Worked Problem — Compare Entropy and a Code

Source probabilities:

| Symbol | Probability |
|---|---:|
| A | 0.5 |
| B | 0.25 |
| C | 0.125 |
| D | 0.125 |

We already calculated:

\[
H=1.75.
\]

A code:

```text
A → 0
B → 10
C → 110
D → 111
```

has average length:

\[
L=1.75.
\]

Thus:

\[
L-H=0.
\]

Under these idealized assumptions, the average code length meets the entropy value exactly.

For other distributions, practical prefix codes generally have a nonzero coding gap.

---

# 37. Worked Problem — RLE Decision

Two sequences contain 20 binary symbols.

### Sequence A

```text
00000000001111111111
```

Runs:

```text
10 zeros
10 ones
```

Only two runs.

### Sequence B

```text
01010101010101010101
```

Runs:

```text
20 runs
```

RLE is strongly favoured for Sequence A and poorly suited to Sequence B.

The lesson is more important than the arithmetic:

\[
\boxed{\text{RLE follows run structure, not simply file size}}
\]

---

# 38. Pseudocode — RLE Encoder

```text
function RLE_encode(sequence):
    output = []
    count = 1

    for i from 1 to length(sequence)-1:
        if sequence[i] == sequence[i-1]:
            count = count + 1
        else:
            append (sequence[i-1], count) to output
            count = 1

    append (sequence[last], count) to output
    return output
```

A real implementation should also define:

- maximum run length;
- integer representation of counts;
- treatment of empty input;
- file format/header rules.

---

# 39. Pseudocode — Huffman Construction

```text
function build_huffman_tree(frequencies):
    create one node per symbol

    while more than one node remains:
        a = node with smallest frequency
        b = node with second-smallest frequency
        parent = merge(a, b)
        insert parent back

    return remaining node as root
```

Then traverse:

```text
left  → 0
right → 1
```

to obtain symbol codewords.

A production implementation must specify tie-breaking rules and serialization of the tree/code table.

---

# 40. Python Mini-Exercise

The following example calculates entropy from a symbol-count dictionary.

```python
from __future__ import annotations

from collections import Counter
from math import log2
from typing import Iterable, Hashable


def entropy(symbols: Iterable[Hashable]) -> float:
    items = list(symbols)
    if not items:
        raise ValueError("Input sequence must not be empty.")

    counts = Counter(items)
    total = len(items)

    return -sum(
        (count / total) * log2(count / total)
        for count in counts.values()
    )


data = list("AAAABBBCCD")
print(f"Entropy = {entropy(data):.4f} bits/symbol")
```

For DIP, the same idea can be applied to flattened image arrays after carefully deciding what constitutes the source symbol.

---

# 41. MATLAB Mini-Exercise

A simple empirical entropy calculation can be written as:

```matlab
img = imread('image.png');

if ndims(img) == 3
    img = rgb2gray(img);
end

counts = imhist(img);
p = counts / sum(counts);

p = p(p > 0);

H = -sum(p .* log2(p));

fprintf('Entropy = %.4f bits/pixel\n', H);
```

The calculation is based on the observed histogram and therefore represents an empirical single-symbol entropy estimate.

---

# 42. Coding Efficiency

Define average code length:

\[
L=
\sum_i p_i l_i
\]

where \(l_i\) is the code length for symbol \(i\).

A useful efficiency measure is:

\[
\eta=\frac{H}{L}.
\]

If:

\[
H=1.75,\qquad L=2,
\]

then:

\[
\eta=0.875.
\]

So the efficiency is:

\[
\boxed{87.5\%}.
\]

Different textbooks may define “efficiency” or “redundancy” with slightly different conventions. Always state the formula you use.

---

# 43. Common Traps

### Trap 1 — Entropy is the number of bits in the compressed file.

Not exactly.

Entropy is an information-theoretic quantity, typically interpreted as a lower-bound-style average rate under a specified source model.

### Trap 2 — Huffman assigns the shortest code to the least frequent symbol.

False.

The most frequent symbols generally get the shortest codewords.

### Trap 3 — RLE always compresses images.

False.

RLE can expand data when runs are short and overhead becomes significant.

### Trap 4 — Huffman coding is lossy.

False.

Huffman coding is a lossless coding method.

### Trap 5 — Entropy only depends on the image dimensions.

False.

It depends on the probability distribution/model of the source symbols.

### Trap 6 — A histogram tells you every spatial dependency.

False.

A histogram captures value frequency, not full spatial arrangement.

---

# 44. Exam Lens

## 2-mark questions

**Define entropy.**

\[
H(X)=-\sum_i p_i\log_2p_i.
\]

**What is RLE?**  
A lossless encoding method that represents consecutive repeated symbols using run information.

**What is Huffman coding?**  
A variable-length prefix-free coding method that assigns shorter codewords to more probable symbols.

---

## 5-mark question

### Explain Huffman coding.

Recommended sequence:

```text
frequency table
→ select two smallest
→ merge
→ repeat
→ construct tree
→ assign 0/1
→ read codewords
→ calculate average length
```

---

## 10-mark numerical question

Given symbol frequencies:

```text
A  B  C  D  E
```

you should be able to:

1. calculate probabilities;
2. calculate entropy;
3. construct the Huffman tree;
4. write codewords;
5. calculate average code length;
6. compare with fixed-length coding;
7. comment on coding efficiency.

---

# 45. Chapter Checkpoint

### Problem 1 — Entropy

Calculate the entropy of:

\[
P(A)=0.5,\quad P(B)=0.5.
\]

### Problem 2 — RLE

Encode:

```text
AAAAAAABBBBCCCAAAAA
```

using run-length notation.

### Problem 3 — Huffman

Construct one valid Huffman code for:

| Symbol | Frequency |
|---|---:|
| A | 50 |
| B | 25 |
| C | 15 |
| D | 10 |

### Problem 4 — Conceptual

Why can RLE and Huffman coding be used together?

### Problem 5 — JPEG bridge

In the JPEG pipeline, why is entropy coding performed after quantization rather than before it?

---

# 46. One-Page Recall Sheet

```text
INFORMATION THEORY
│
├── Self-information
│   I(x) = -log2 p(x)
│
├── Entropy
│   H(X) = -Σ p log2 p
│
├── Fixed-length code
│   ≈ ceil(log2 M)
│
├── Average code length
│   L = Σ p_i l_i
│
├── Efficiency
│   η = H/L
│
├── RLE
│   runs → compact run representation
│
└── Huffman
    probabilities
      ↓
    merge least frequent nodes
      ↓
    prefix-free variable-length code
```

---

# 47. Cross-Book Links

| Layer | Connection |
|---|---|
| MAIN | C22 develops lossless coding foundations |
| MATH | Probability, logarithms, entropy |
| LAB | Manual entropy/RLE/Huffman experiments can support JPEG practical |
| CODE | Empirical histogram entropy and coding implementations |
| EXAM | Entropy numericals, Huffman tree, RLE, comparisons |
| PRACTICE | Guided → numerical → algorithm-trace → debugging |
| RESOURCE | Gonzalez & Woods and other course references |
| ASSETS | Huffman trees, probability tables, RLE strip diagrams |
| MASTER | Dependency link to C23/C24 and Practical 7 |

---

# 48. Final Chapter Summary

Three ideas should remain after this chapter.

### 1. Entropy measures uncertainty/information rate under a source model

\[
\boxed{
H(X)=-\sum p_i\log_2p_i
}
\]

### 2. RLE exploits repeated runs

```text
AAAAAA
→
(6,A)
```

### 3. Huffman exploits unequal symbol probabilities

```text
high probability → short code
low probability  → long code
```

Together, these ideas demonstrate a general compression principle:

> **First expose structure; then represent that structure efficiently.**

That principle becomes increasingly powerful after transform coding and DCT are introduced in C23.

---

**Next chapter:** C23 — Transform Coding and DCT
