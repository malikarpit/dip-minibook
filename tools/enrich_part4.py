#!/usr/bin/env python3
"""
Digital Image Processing (DIP) MiniBook — Part IV Master Enrichment & Compilation Suite
Compiles Chapters 21 to 24 (Information Theory, Lossless Coding, DCT, and JPEG Compression)
into comprehensive 2,200+ line production-grade HTML chapters matching the AIML standard.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_DIR = os.path.join(BASE_DIR, 'tools')
sys.path.append(TOOLS_DIR)

from enrich_and_build import build_enriched_chapter
from build_chapter import CHAPTERS_META

# ── CHAPTER 21 ENRICHMENTS: COMPRESSION FUNDAMENTALS ─────────────────
ch21_extra = r"""
# 21.43 Worked Example — 10-Mark University Model Answer: Shannon Information Entropy & Fidelity Metrics
### Problem Statement
A digital image with $MN = 10,000$ pixels has an 8-bit dynamic range ($L = 256$, baseline $b = 8$ bits/pixel). However, only 4 discrete intensity values appear in the image with the following probabilities:
$$p(r_1) = 0.50, \qquad p(r_2) = 0.25, \qquad p(r_3) = 0.125, \qquad p(r_4) = 0.125$$
1. State the three fundamental data redundancies exploited in image compression.
2. Compute the Shannon Information Entropy $H$ of the image source in bits/pixel.
3. Determine the theoretical maximum compression ratio $C$ and the relative coding redundancy $R_D$.
4. Reconstructed pixel intensities at 4 coordinates are $\hat{f} = [102, 120, 135, 150]$ while pristine intensities are $f = [100, 124, 130, 152]$. Compute the Mean Square Error (MSE), Root Mean Square Error (RMSE), and Peak Signal-to-Noise Ratio (PSNR in dB).

### Step-by-Step Mathematical Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. Three Fundamental Data Redundancies:</strong><br>
  - <strong>Coding Redundancy:</strong> Occurs when pixel intensities are represented using more bits than theoretically necessary (e.g. using fixed 8-bit codes for symbols with highly unequal probabilities).<br>
  - <strong>Spatial / Interpixel Redundancy:</strong> Results from the high spatial correlation between adjacent pixels in natural scenes (neighboring pixels usually have almost identical values).<br>
  - <strong>Psychovisual Redundancy:</strong> Information that the Human Visual System (HVS) cannot perceive (e.g. high-frequency chromatic variations, subtle quantization noise in dark or textured areas).</p>

  <p><strong>2. Shannon Information Entropy ($H$):</strong><br>
  $$H = -\sum_{i=1}^4 p(r_i) \log_2 p(r_i)$$
  Evaluating term by term:<br>
  - $p(r_1) = 0.50 \implies \log_2(0.50) = -1.0 \implies -0.50(-1.0) = 0.50$<br>
  - $p(r_2) = 0.25 \implies \log_2(0.25) = -2.0 \implies -0.25(-2.0) = 0.50$<br>
  - $p(r_3) = 0.125 \implies \log_2(0.125) = -3.0 \implies -0.125(-3.0) = 0.375$<br>
  - $p(r_4) = 0.125 \implies \log_2(0.125) = -3.0 \implies -0.125(-3.0) = 0.375$<br>
  $$H = 0.50 + 0.50 + 0.375 + 0.375 = \mathbf{1.75 \text{ bits/pixel}}$$
  By Shannon's First Theorem (Noiseless Coding Theorem), the average codeword length cannot be less than $1.75$ bits/pixel without information loss.</p>

  <p><strong>3. Compression Ratio and Coding Redundancy:</strong><br>
  Baseline uncompressed representation: $b = 8$ bits/pixel.<br>
  $$\text{Theoretical Optimal Compression Ratio } C = \frac{b}{H} = \frac{8}{1.75} \approx \mathbf{4.5714 : 1}$$
  $$\text{Relative Coding Redundancy } R_D = 1 - \frac{1}{C} = 1 - \frac{1.75}{8} = 1 - 0.21875 = \mathbf{0.78125 \ (78.13\%)}$$
  This indicates that 78.13% of the data bits in the uncompressed 8-bit image represent pure redundant overhead.</p>

  <p><strong>4. Objective Fidelity Criteria (MSE, RMSE, PSNR):</strong><br>
  Difference vector $e = f - \hat{f} = [100 - 102, 124 - 120, 130 - 135, 152 - 150] = [-2, +4, -5, +2]$.<br>
  Squared differences: $e^2 = [4, 16, 25, 4]$.<br>
  $$MSE = \frac{1}{4} (4 + 16 + 25 + 4) = \frac{49}{4} = \mathbf{12.25}$$
  $$RMSE = \sqrt{MSE} = \sqrt{12.25} = \mathbf{3.50 \text{ gray levels}}$$
  Peak Signal-to-Noise Ratio for 8-bit dynamic range ($L - 1 = 255$):
  $$PSNR = 10 \log_{10} \left( \frac{255^2}{MSE} \right) = 10 \log_{10} \left( \frac{65025}{12.25} \right) = 10 \log_{10}(5308.16)$$
  $$PSNR = 10 \times 3.7249 = \mathbf{37.25 \text{ dB}}$$
  A PSNR above 30 dB in lossy compression indicates excellent fidelity where reconstruction errors are generally imperceptible to the human eye.</p>
</div>
"""

# ── CHAPTER 22 ENRICHMENTS: LOSSLESS CODING & HUFFMAN ────────────────
ch22_extra = r"""
# 22.52 Worked Example — 10-Mark University Model Answer: Huffman Variable-Length Coding
### Problem Statement
A discrete memoryless source emits 6 independent symbols $s_1, s_2, s_3, s_4, s_5, s_6$ with the following probability distribution:
$$p(s_1) = 0.40, \quad p(s_2) = 0.20, \quad p(s_3) = 0.15, \quad p(s_4) = 0.10, \quad p(s_5) = 0.10, \quad p(s_6) = 0.05$$
1. Construct the optimal binary Huffman code tree by successive source reduction.
2. Formulate the code assignment table with codeword lengths $l_i$.
3. Compute the source entropy $H$.
4. Calculate the average codeword length $\bar{L}$ and the coding efficiency $\eta$.
5. Verify whether the code satisfies the prefix-free property.

### Step-by-Step Mathematical Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. Step-by-Step Source Reduction Trace:</strong><br>
  Arrange symbols in descending order of probability and successively merge the two lowest probabilities:</p>

  <div class="table-wrap">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Symbol</th><th>Original Prob</th><th>Reduction 1</th><th>Reduction 2</th><th>Reduction 3</th><th>Reduction 4</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>$s_1$</td><td>0.40</td><td>0.40</td><td>0.40</td><td>0.40</td><td><strong>0.60</strong> (from 0.35+0.25)</td></tr>
        <tr><td>$s_2$</td><td>0.20</td><td>0.20</td><td>0.25 (from 0.15+0.10)</td><td><strong>0.35</strong> (from 0.20+0.15)</td><td><strong>0.40</strong></td></tr>
        <tr><td>$s_3$</td><td>0.15</td><td>0.15</td><td>0.20</td><td>0.25</td><td>-</td></tr>
        <tr><td>$s_4$</td><td>0.10</td><td>0.15 (from 0.10+0.05)</td><td>0.15</td><td>-</td><td>-</td></tr>
        <tr><td>$s_5$</td><td>0.10</td><td>0.10</td><td>-</td><td>-</td><td>-</td></tr>
        <tr><td>$s_6$</td><td>0.05</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
      </tbody>
    </table>
  </div>

  <p><strong>2. Backward Assignment of Binary Codewords (0 to upper, 1 to lower):</strong><br>
  - Final step: $0.60 \to 0$, $0.40 \to 1$.<br>
  - Expanding backwards to original symbols yields the code table:</p>

  <div class="table-wrap">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Symbol $s_i$</th>
          <th>Probability $p(s_i)$</th>
          <th>Huffman Codeword</th>
          <th>Length $l_i$ (bits)</th>
          <th>$p(s_i) \cdot l_i$</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>$s_1$</td><td>0.40</td><td><code>1</code></td><td>1</td><td>$0.40 \times 1 = 0.40$</td></tr>
        <tr><td>$s_2$</td><td>0.20</td><td><code>01</code></td><td>2</td><td>$0.20 \times 2 = 0.40$</td></tr>
        <tr><td>$s_3$</td><td>0.15</td><td><code>000</code></td><td>3</td><td>$0.15 \times 3 = 0.45$</td></tr>
        <tr><td>$s_4$</td><td>0.10</td><td><code>0010</code></td><td>4</td><td>$0.10 \times 4 = 0.40$</td></tr>
        <tr><td>$s_5$</td><td>0.10</td><td><code>00110</code></td><td>5</td><td>$0.10 \times 5 = 0.50$</td></tr>
        <tr><td>$s_6$</td><td>0.05</td><td><code>00111</code></td><td>5</td><td>$0.05 \times 5 = 0.25$</td></tr>
        <tr><td><strong>Total</strong></td><td><strong>1.00</strong></td><td>-</td><td>-</td><td><strong>$\bar{L} = 2.40$ bits</strong></td></tr>
      </tbody>
    </table>
  </div>

  <p><strong>3. Source Entropy ($H$):</strong><br>
  $$H = -\sum_{i=1}^6 p(s_i) \log_2 p(s_i)$$
  - $0.40 \log_2(0.40) = 0.40(-1.3219) = -0.5288$<br>
  - $0.20 \log_2(0.20) = 0.20(-2.3219) = -0.4644$<br>
  - $0.15 \log_2(0.15) = 0.15(-2.7370) = -0.4106$<br>
  - $0.10 \log_2(0.10) = 0.10(-3.3219) = -0.3322$<br>
  - $0.10 \log_2(0.10) = -0.3322$<br>
  - $0.05 \log_2(0.05) = 0.05(-4.3219) = -0.2161$<br>
  $$H = 0.5288 + 0.4644 + 0.4106 + 0.3322 + 0.3322 + 0.2161 = \mathbf{2.2843 \text{ bits/symbol}}$$</p>

  <p><strong>4. Coding Efficiency ($\eta$) and Redundancy:</strong><br>
  $$\text{Average Codeword Length } \bar{L} = \sum_{i=1}^6 p(s_i) l_i = 0.40 + 0.40 + 0.45 + 0.40 + 0.50 + 0.25 = \mathbf{2.40 \text{ bits/symbol}}$$
  $$\text{Coding Efficiency } \eta = \frac{H}{\bar{L}} = \frac{2.2843}{2.40} \approx \mathbf{0.9518 \ (95.18\%)}$$
  $$\text{Coding Redundancy } R = \bar{L} - H = 2.40 - 2.2843 = \mathbf{0.1157 \text{ bits/symbol}}$$
  A fixed-length code would require $\lceil \log_2 6 \rceil = 3$ bits/symbol. Huffman reduces this to 2.40 bits, achieving a 20% bitrate reduction with 95.18% efficiency.</p>

  <p><strong>5. Prefix-Free Verification:</strong><br>
  No codeword is a prefix of any other codeword (e.g. `1` is unique; all other codewords start with `0`; `01` is unique; all longer ones start with `00`).
  Therefore, the stream is instantaneously and uniquely decodable without lookahead buffers.</p>
</div>
"""

# ── CHAPTER 23 ENRICHMENTS: TRANSFORM CODING & DCT ───────────────────
ch23_extra = r"""
# 23.45 Mathematical Derivation: 2D Discrete Cosine Transform (DCT-II)
### Continuous to Discrete Cosine Basis
For an $N \times N$ spatial block $f(x, y)$, the forward 2D DCT-II is defined as:
$$C(u, v) = \alpha(u) \alpha(v) \sum_{x=0}^{N-1} \sum_{y=0}^{N-1} f(x, y) \cos\left[ \frac{(2x+1)u\pi}{2N} \right] \cos\left[ \frac{(2y+1)v\pi}{2N} \right]$$
for $u, v = 0, 1, \dots, N-1$, where the normalizing orthogonal scale factors are:
$$\alpha(u) = \begin{cases} \sqrt{\frac{1}{N}} & \text{if } u = 0 \\ \sqrt{\frac{2}{N}} & \text{if } u > 0 \end{cases}$$

### DC Component Physical Meaning
For $u = 0, v = 0$:
$$\alpha(0) \alpha(0) = \sqrt{\frac{1}{N}} \sqrt{\frac{1}{N}} = \frac{1}{N}$$
$$\cos(0) \cdot \cos(0) = 1 \cdot 1 = 1$$
$$C(0, 0) = \frac{1}{N} \sum_{x=0}^{N-1} \sum_{y=0}^{N-1} f(x, y)$$
Notice that the average brightness (DC value) of the $N \times N$ block is $\bar{f} = \frac{1}{N^2} \sum \sum f(x, y)$.
$$\therefore C(0, 0) = N \cdot \bar{f}$$
The DC coefficient represents exactly $N$ times the average intensity of the entire block, concentrating the bulk of the image energy into a single scalar value.

# 23.46 Comparative Analysis: Why DCT Outperforms DFT and KLT in Video/Image Standards
<div class="table-wrap">
  <table class="comparison-table">
    <thead>
      <tr>
        <th>Transform Metric</th>
        <th>Karhunen-Loève Transform (KLT)</th>
        <th>Discrete Cosine Transform (DCT)</th>
        <th>Discrete Fourier Transform (DFT)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Energy Compaction</strong></td>
        <td><strong>Statistically Optimal:</strong> Completely diagonalizes the covariance matrix.</td>
        <td><strong>Near-Optimal:</strong> Asymptotically approaches KLT for Markov-1 sources ($\rho \approx 0.95$).</td>
        <td>Moderate (Significantly lower than DCT due to complex phase dispersion).</td>
      </tr>
      <tr>
        <td><strong>Data Dependency</strong></td>
        <td>Data-dependent: Basis functions must be computed from image covariance matrix.</td>
        <td><strong>Data-Independent:</strong> Universal cosine basis functions pre-computed offline.</td>
        <td>Data-Independent: Universal complex exponential basis functions.</td>
      </tr>
      <tr>
        <td><strong>Boundary Artifacts</strong></td>
        <td>No boundary assumptions.</td>
        <td><strong>Even Symmetric Extension:</strong> Continuous at block boundaries; no Gibbs ringing.</td>
        <td>Periodic wrap-around causes sharp boundary discontinuities and heavy high-frequency ringing.</td>
      </tr>
      <tr>
        <td><strong>Computational Complexity</strong></td>
        <td>$O(N^3)$ (Requires full covariance matrix diagonalization).</td>
        <td><strong>$O(N \log N)$ (Fast Feig-Winograd / Arai algorithms).</strong></td>
        <td>$O(N \log N)$ (FFT algorithms).</td>
      </tr>
      <tr>
        <td><strong>Standard Adoption</strong></td>
        <td>Theoretical benchmark; never used in real-time standards.</td>
        <td><strong>Universal Standard:</strong> JPEG, MPEG-1/2/4, H.264, HEVC.</td>
        <td>Frequency filtering, radar, optical analysis.</td>
      </tr>
    </tbody>
  </table>
</div>
"""

# ── CHAPTER 24 ENRICHMENTS: JPEG END TO END ──────────────────────────
ch24_extra = r"""
# 24.64 Worked Example — 10-Mark University Model Answer: End-to-End Baseline JPEG Pipeline
### Problem Statement
A $8 \times 8$ grayscale image block undergoes baseline sequential JPEG encoding.
1. Formulate the level shifting operation and state why it is applied prior to DCT.
2. Given a quantized $8 \times 8$ DCT coefficient matrix $F_q$, explain the purpose of Zigzag Scanning.
3. Trace the zigzag sequence and encode the non-zero AC coefficients into Run-Length Amplitude intermediate symbols $((run, size), amplitude)$ ending with an End-of-Block (EOB) marker.
4. Explain why chroma subsampling (4:2:0) is imperceptible to human observers.

### Step-by-Step Mathematical Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. Level Shifting ($f - 128$):</strong><br>
  For an 8-bit unsigned input $f(x, y) \in [0, 255]$, the baseline JPEG standard shifts intensities to zero-mean signed values $[-128, +127]$:
  $$f_{shifted}(x, y) = f(x, y) - 128$$
  <em>Rationale:</em> Zero-centering ensures that the DC coefficient $C(0, 0)$ is balanced symmetrically around zero, reducing the dynamic range required for DC differential prediction and preventing arithmetic overflow.</p>

  <p><strong>2. Psychovisual Quantization and Zigzag Scanning:</strong><br>
  Division by the luminance quantization matrix $Q(u, v)$ zeros out almost all high-frequency diagonal coefficients.
  Consider a typical quantized block:
  $$F_q = \begin{bmatrix}
  -26 & -3 & -2 & 0 & 0 & 0 & 0 & 0 \\
  1 & -1 & 0 & 0 & 0 & 0 & 0 & 0 \\
  0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
  0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
  0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
  0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
  0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
  0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
  \end{bmatrix}$$</p>

  <p>Zigzag scanning traverses the matrix along diagonal paths of increasing spatial frequency $(u + v)$:<br>
  $(0,0) \to (0,1) \to (1,0) \to (2,0) \to (1,1) \to (0,2) \to (0,3) \to (1,2) \to (2,1) \to (3,0) \dots$<br>
  This orders coefficients from lowest to highest frequency, concentrating the few surviving non-zero coefficients at the beginning of the stream and grouping all zeros into a continuous terminal run.</p>

  <p><strong>3. 1D Zigzag Traversal & Intermediate Symbol Encoding:</strong><br>
  - DC Term: $F_q(0, 0) = -26$ (encoded differentially against previous block DC).<br>
  - AC Sequence:
  $$\text{Pos 1: } (0, 1) = -3$$
  $$\text{Pos 2: } (1, 0) = +1$$
  $$\text{Pos 3: } (2, 0) = 0$$
  $$\text{Pos 4: } (1, 1) = -1$$
  $$\text{Pos 5: } (0, 2) = -2$$
  $$\text{Pos 6: } (0, 3) = 0, \ (1, 2) = 0, \ (2, 1) = +1$$
  $$\text{Pos 9..63: All Remaining 55 Coefficients are 0}$$</p>

  <p><strong>Run-Length Intermediate Symbols $((run, size), amplitude)$:</strong><br>
  1. Value $-3$: Zero run $= 0$, magnitude $3 \implies size = 2$, amplitude code for $-3$ is `00` $\implies \mathbf{((0, 2), -3)}$<br>
  2. Value $+1$: Zero run $= 0$, magnitude $1 \implies size = 1$, amplitude code `1` $\implies \mathbf{((0, 1), +1)}$<br>
  3. Value $-1$ (after 1 zero at $(2,0)$): Zero run $= 1$, magnitude $1 \implies size = 1$, code `0` $\implies \mathbf{((1, 1), -1)}$<br>
  4. Value $-2$: Zero run $= 0$, magnitude $2 \implies size = 2$, code `01` $\implies \mathbf{((0, 2), -2)}$<br>
  5. Value $+1$ (after 2 zeros at $(0,3)$ and $(1,2)$): Zero run $= 2$, magnitude $1 \implies size = 1$, code `1` $\implies \mathbf{((2, 1), +1)}$<br>
  6. Remaining coefficients are all zero $\implies \mathbf{(0, 0) \ [EOB - End \ of \ Block]}$</p>
  <p>Instead of transmitting 63 numbers, the entire AC spectrum is compressed into just 5 compact symbol pairs and a single 4-bit EOB code!</p>

  <p><strong>4. Psychovisual Basis of 4:2:0 Chroma Subsampling:</strong><br>
  The human retina contains approximately 120 million rod photoreceptors (sensitive to luminance/intensity) but only 6 to 7 million cone photoreceptors (sensitive to chrominance/color).
  Consequently, human visual acuity for spatial chromatic detail is less than half that for luminance.
  Downsampling $Cb$ and $Cr$ channels by a factor of 2 horizontally and vertically (4:2:0) discards 50% of the raw color data with zero perceptible degradation under natural viewing conditions.</p>
</div>
"""

PART4_ENRICHMENTS = {
    21: ch21_extra,
    22: ch22_extra,
    23: ch23_extra,
    24: ch24_extra
}

def compile_part4():
    print("=" * 60)
    print("COMPILING ENRICHED DIP PART IV CHAPTERS (C21 - C24)")
    print("=" * 60)

    part4_metas = [m for m in CHAPTERS_META if 21 <= m['chapter_num'] <= 24]

    for meta in part4_metas:
        c_num = meta['chapter_num']
        extra = PART4_ENRICHMENTS.get(c_num, None)
        print(f"\n--- Compiling Chapter {c_num:02d}: {meta['title']} ---")
        build_enriched_chapter(meta, extra_sections_md=extra)

    print("\n" + "=" * 60)
    print("ALL 4 PART IV CHAPTERS SUCCESSFULLY COMPILED!")
    print("=" * 60)

if __name__ == '__main__':
    compile_part4()
