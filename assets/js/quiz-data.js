// DIP MiniBook Question Bank - 100 Questions with University Syllabus Mapping
// Mapped across Delhi University DSE-3 Digital Image Processing Curriculum

const DIP_QUIZ_DATA = [
  {
    "id": 1,
    "unit": "Unit I",
    "chapter": 1,
    "diff": "Easy",
    "topic": "Fundamentals of Image Processing",
    "q": "In the standard digital image processing hierarchy, which of the following tasks is classified as a 'Mid-Level' vision task?",
    "options": [
      "Noise reduction and contrast stretching",
      "Image segmentation and object classification",
      "Scene interpretation and autonomous navigation",
      "Analog-to-digital sensor conversion"
    ],
    "ans": 1,
    "exp": "DIP is divided into Low-Level (inputs and outputs are images, e.g., noise reduction, contrast stretching), Mid-Level (inputs are images, outputs are attributes/features, e.g., segmentation, object classification, edge descriptors), and High-Level (making sense of recognized objects, e.g., scene interpretation, autonomous navigation).",
    "uni": true
  },
  {
    "id": 2,
    "unit": "Unit I",
    "chapter": 1,
    "diff": "Moderate",
    "topic": "Fundamentals of Image Processing",
    "q": "According to the human visual system, which photoreceptor cells are responsible for photopic (color, high-detail) vision and where are they primarily concentrated?",
    "options": [
      "Rods, concentrated in the peripheral retina",
      "Cones, concentrated in the fovea centralis",
      "Rods, concentrated in the fovea centralis",
      "Cones, distributed evenly across the blind spot"
    ],
    "ans": 1,
    "exp": "Cones (approximately 6–7 million) are highly concentrated in the fovea centralis of the retina and are responsible for photopic (daylight/color) vision and fine spatial resolution. Rods (approximately 75–150 million) are distributed across the periphery and mediate scotopic (monochromatic, low-light) vision.",
    "uni": true
  },
  {
    "id": 3,
    "unit": "Unit I",
    "chapter": 1,
    "diff": "Moderate",
    "topic": "Fundamentals of Image Processing",
    "q": "The visual phenomenon where the perceived brightness along the boundary between adjacent strips of constant but slightly different intensity shows distinct dark and bright overshoot bands is known as:",
    "options": [
      "Weber-Fechner effect",
      "Simultaneous contrast",
      "Mach bands",
      "Spatial aliasing"
    ],
    "ans": 2,
    "exp": "Mach bands are an optical illusion caused by lateral inhibition in the human retina, where the visual system overshoots and undershoots brightness at sharp transitions, making borders appear darker on the darker side and lighter on the lighter side.",
    "uni": true
  },
  {
    "id": 4,
    "unit": "Unit I",
    "chapter": 2,
    "diff": "Moderate",
    "topic": "Image Formation",
    "q": "Under the reflectance-illumination image model $f(x, y) = i(x, y) \\cdot r(x, y)$, which of the following physical constraints is ALWAYS true?",
    "options": [
      "$0 < i(x, y) < \\infty$ and $0 \\le r(x, y) \\le 1$",
      "$0 \\le i(x, y) \\le 1$ and $0 < r(x, y) < \\infty$",
      "$i(x, y) = 1$ in total darkness and $r(x, y) = 0$ for a mirror",
      "$i(x, y)$ is determined solely by object geometry and $r(x, y)$ by the sun"
    ],
    "ans": 0,
    "exp": "In the image model $f(x, y) = i(x, y) \\cdot r(x, y)$, the illumination component $i(x,y)$ represents the amount of source light incident on the scene ($0 < i(x,y) < \\infty$), while the reflectance component $r(x,y)$ represents the fraction of incident light reflected by the object surface ($0 \\le r(x,y) \\le 1$, bounded between total absorption and total reflection).",
    "uni": true
  },
  {
    "id": 5,
    "unit": "Unit I",
    "chapter": 2,
    "diff": "Hard",
    "topic": "Image Formation",
    "q": "According to the camera lens irradiance equation ($E \\propto \\cos^4 \\alpha$), why does image brightness roll off toward the corners of the sensor plane?",
    "options": [
      "Lens flare cancels out photons arriving at the peripheral edges",
      "Light rays at off-axis angle $\\alpha$ travel further and strike the sensor at an oblique angle, reducing apparent pupil area",
      "CMOS photo-sites are physically smaller at the sensor borders",
      "The optical glass absorbs blue wavelengths at non-zero incidence"
    ],
    "ans": 1,
    "exp": "The $\\cos^4 \\alpha$ radiometric law of lens illumination states that image irradiance $E$ drops as $\\cos^4 \\alpha$ away from the optical axis due to four geometric factors: inverse-square distance falloff ($\\cos^2 \\alpha$), projection of the entrance pupil ($\\cos \\alpha$), and projection onto the detector surface ($\\cos \\alpha$).",
    "uni": true
  },
  {
    "id": 6,
    "unit": "Unit I",
    "chapter": 3,
    "diff": "Easy",
    "topic": "Sampling and Quantization",
    "q": "In digital image acquisition, the digitization of spatial coordinates is called ________, whereas the digitization of amplitude/intensity is called ________.",
    "options": [
      "Quantization; Sampling",
      "Sampling; Quantization",
      "Filtering; Interpolation",
      "Thresholding; Resolution"
    ],
    "ans": 1,
    "exp": "Digitizing coordinate values $(x, y)$ is termed Sampling (converting a continuous spatial domain into a discrete grid of pixels). Digitizing amplitude values $f(x, y)$ is termed Quantization (mapping continuous brightness intensities into discrete gray levels).",
    "uni": true
  },
  {
    "id": 7,
    "unit": "Unit I",
    "chapter": 3,
    "diff": "Moderate",
    "topic": "Sampling and Quantization",
    "q": "According to the 2D Nyquist-Shannon Sampling Theorem, to perfectly reconstruct a bandlimited image with maximum spatial frequencies $u_{\\max}$ and $v_{\\max}$, the sampling intervals $\\Delta x$ and $\\Delta y$ must satisfy:",
    "options": [
      "$\\Delta x \\le \\frac{1}{2 u_{\\max}}$ and $\\Delta y \\le \\frac{1}{2 v_{\\max}}$",
      "$\\Delta x \\ge 2 u_{\\max}$ and $\\Delta y \\ge 2 v_{\\max}$",
      "$\\Delta x \\le \\frac{1}{u_{\\max}}$ and $\\Delta y \\le \\frac{1}{v_{\\max}}$",
      "$\\Delta x = u_{\\max} \\cdot v_{\\max}$"
    ],
    "ans": 0,
    "exp": "The Nyquist sampling criterion requires that the sampling rate $f_s \\ge 2 f_{\\max}$. In terms of spatial sampling intervals, $\\Delta x = 1/f_{s,x} \\le 1/(2 u_{\\max})$ and $\\Delta y = 1/f_{s,y} \\le 1/(2 v_{\\max})$. Violating this criterion results in spatial aliasing and moiré artifacts.",
    "uni": true
  },
  {
    "id": 8,
    "unit": "Unit I",
    "chapter": 3,
    "diff": "Moderate",
    "topic": "Sampling and Quantization",
    "q": "When an image is quantized using too few gray levels (e.g., 16 levels / 4 bits instead of 256 levels / 8 bits), what visual artifact predominantly appears in regions of smooth, gradual intensity variation?",
    "options": [
      "Moiré patterns",
      "False contouring (banding)",
      "Speckle noise",
      "Motion blur"
    ],
    "ans": 1,
    "exp": "False contouring (banding) occurs when coarse quantization forces smooth intensity gradients to step abruptly between adjacent discrete levels, causing visible, artificial ridge boundaries resembling topographic elevation lines.",
    "uni": true
  },
  {
    "id": 9,
    "unit": "Unit I",
    "chapter": 3,
    "diff": "Hard",
    "topic": "Sampling and Quantization",
    "q": "An optimal non-uniform quantizer designed to minimize the mean squared quantization error for an arbitrary input probability density function is known as the:",
    "options": [
      "Huffman Quantizer",
      "Lloyd-Max Quantizer",
      "Otsu Quantizer",
      "Sobel Quantizer"
    ],
    "ans": 1,
    "exp": "The Lloyd-Max quantizer iteratively optimizes decision thresholds and reconstruction levels such that each threshold lies halfway between adjacent reconstruction centroids, and each reconstruction level is the centroid of the probability density between its enclosing thresholds, minimizing mean squared error.",
    "uni": true
  },
  {
    "id": 10,
    "unit": "Unit I",
    "chapter": 4,
    "diff": "Easy",
    "topic": "Image Representation: Pixels, Bit Depth, and Resolution",
    "q": "How many bytes of uncompressed storage are required to store a single grayscale image of size $1024 \\times 1024$ pixels with a bit depth of 8 bits per pixel?",
    "options": [
      "131,072 bytes (128 KB)",
      "1,048,576 bytes (1 MB)",
      "8,388,608 bytes (8 MB)",
      "524,288 bytes (512 KB)"
    ],
    "ans": 1,
    "exp": "Storage = $M \\times N \\times (k / 8) \\text{ bytes} = 1024 \\times 1024 \\times (8 / 8) = 1,048,576 \\text{ bytes} = 1 \\text{ MB (or 1 MiB)}$.",
    "uni": true
  },
  {
    "id": 11,
    "unit": "Unit I",
    "chapter": 4,
    "diff": "Moderate",
    "topic": "Image Representation: Pixels, Bit Depth, and Resolution",
    "q": "What is the primary difference between a 'Multispectral' image and a 'Hyperspectral' image?",
    "options": [
      "Multispectral images only use infrared light, while hyperspectral images only use ultraviolet light",
      "Multispectral images acquire 3 to 10 discrete, relatively broad spectral bands, whereas hyperspectral images capture hundreds of narrow, contiguous spectral bands",
      "Multispectral images are uncompressed, whereas hyperspectral images are lossy JPEG files",
      "Multispectral images have higher spatial resolution but zero spectral information"
    ],
    "ans": 1,
    "exp": "Multispectral sensors (like Landsat) sample 3–10 broad, discrete spectral bands across visible, near-IR, and shortwave-IR. Hyperspectral sensors (like AVIRIS) capture hundreds (typically 100–300+) of narrow, contiguous spectral bands (5–10 nm wide), enabling precise spectral signature identification of materials.",
    "uni": true
  },
  {
    "id": 12,
    "unit": "Unit I",
    "chapter": 4,
    "diff": "Moderate",
    "topic": "Image Representation: Pixels, Bit Depth, and Resolution",
    "q": "In scientific and medical imaging, why are 12-bit and 16-bit sensors commonly preferred over standard 8-bit consumer sensors?",
    "options": [
      "They produce smaller file sizes that transfer faster over DICOM networks",
      "They provide 4,096 to 65,536 discrete intensity levels, allowing high dynamic range capture without clipping subtle tissue contrast in shadows or highlights",
      "They automatically eliminate Gaussian noise without filtering",
      "They operate only in the frequency domain"
    ],
    "ans": 1,
    "exp": "An 8-bit sensor resolves only 256 intensity levels. Medical modalities (CT, MRI, digital X-rays) require resolving subtle tissue densities across a wide dynamic range (e.g., 4,096 levels in 12-bit; 65,536 in 16-bit), preventing saturation and preserving diagnostically critical low-contrast details.",
    "uni": true
  },
  {
    "id": 13,
    "unit": "Unit I",
    "chapter": 4,
    "diff": "Easy",
    "topic": "Image Representation: Pixels, Bit Depth, and Resolution",
    "q": "The ability of an imaging system to distinguish two closely spaced point sources of light as distinct entities is defined as:",
    "options": [
      "Radiometric resolution",
      "Spatial resolution",
      "Temporal resolution",
      "Spectral resolution"
    ],
    "ans": 1,
    "exp": "Spatial resolution measures the smallest detectable detail or closest discernible spatial distance between features in an image (often quantified in line pairs per millimeter, dots per inch, or sensor pixel pitch).",
    "uni": true
  },
  {
    "id": 14,
    "unit": "Unit I",
    "chapter": 5,
    "diff": "Easy",
    "topic": "Color Models: RGB, HSV, CMY, YUV",
    "q": "The RGB color model is an ________ color model primarily used for ________, while the CMY color model is a ________ color model used for ________.",
    "options": [
      "Subtractive, printing; Additive, displays",
      "Additive, electronic displays; Subtractive, color printing",
      "Perceptual, video broadcast; Luminance-chrominance, television",
      "Monochrome, cameras; Tristimulus, scanners"
    ],
    "ans": 1,
    "exp": "RGB is an additive model where red, green, and blue light are summed together to produce white light (used in monitors and sensors). CMY (Cyan, Magenta, Yellow) is a subtractive model where pigments absorb/subtract light wavelengths from reflected white paper (used in color printing).",
    "uni": true
  },
  {
    "id": 15,
    "unit": "Unit I",
    "chapter": 5,
    "diff": "Moderate",
    "topic": "Color Models: RGB, HSV, CMY, YUV",
    "q": "Given an RGB image where pixel values are normalized to $[0, 1]$, what is the CMY equivalent of an RGB pixel with values $(R=0.2, G=0.7, B=1.0)$?",
    "options": [
      "$(C=0.8, M=0.3, Y=0.0)$",
      "$(C=0.2, M=0.7, Y=1.0)$",
      "$(C=0.0, M=0.5, Y=0.8)$",
      "$(C=1.0, M=1.0, Y=1.0)$"
    ],
    "ans": 0,
    "exp": "Conversion from RGB to CMY is given by subtractive subtraction: $C = 1 - R = 1 - 0.2 = 0.8$, $M = 1 - G = 1 - 0.7 = 0.3$, $Y = 1 - B = 1 - 1.0 = 0.0$.",
    "uni": true
  },
  {
    "id": 16,
    "unit": "Unit I",
    "chapter": 5,
    "diff": "Moderate",
    "topic": "Color Models: RGB, HSV, CMY, YUV",
    "q": "In the HSV (Hue, Saturation, Value) color space, what geometric quantity represents 'Hue' and how is it measured?",
    "options": [
      "Radial distance from the central vertical cylinder axis, measured from 0 to 1",
      "Vertical height along the central axis, measured from 0% to 100%",
      "Angular position around the color wheel/hexcone, measured from $0^\\circ$ to $360^\\circ$",
      "The Euclidean distance to the black origin in Cartesian space"
    ],
    "ans": 2,
    "exp": "In the cylindrical HSV model, Hue represents pure spectral color tone and is defined as an angular coordinate from $0^\\circ$ to $360^\\circ$ ($0^\\circ$ Red, $120^\\circ$ Green, $240^\\circ$ Blue). Saturation is the radial distance from the central axis, and Value is vertical lightness/brightness.",
    "uni": true
  },
  {
    "id": 17,
    "unit": "Unit I",
    "chapter": 5,
    "diff": "Hard",
    "topic": "Color Models: RGB, HSV, CMY, YUV",
    "q": "Why is the YUV / YCbCr color model universally employed in video broadcast standards (PAL, NTSC) and JPEG compression rather than RGB?",
    "options": [
      "It requires zero floating-point arithmetic to render on displays",
      "It separates luminance (Y) from chrominance (U/V), enabling aggressive downsampling of color channels without noticeable visual degradation",
      "It eliminates all forms of spatial aliasing automatically",
      "It is immune to salt-and-pepper noise"
    ],
    "ans": 1,
    "exp": "The human eye possesses far higher spatial acuity for luminance (achromatic brightness) than for chrominance (color hue). Separating luminance (Y) from color differences (U/V or Cb/Cr) allows chroma subsampling (e.g., 4:2:0 where color data is halved horizontally and vertically) with minimal perceived loss.",
    "uni": true
  },
  {
    "id": 18,
    "unit": "Unit I",
    "chapter": 5,
    "diff": "Hard",
    "topic": "Color Models: RGB, HSV, CMY, YUV",
    "q": "On the CIE 1931 ($x, y$) Chromaticity Diagram, all physically realizable human-visible colors lie within a horseshoe-shaped region. What happens when two primary colors $P_1$ and $P_2$ are mixed?",
    "options": [
      "The mixture generates colors anywhere inside the entire outer perimeter",
      "The resulting colors lie strictly along the straight line segment connecting $P_1$ and $P_2$",
      "The mixture curves outwards toward the pure spectral boundary",
      "The mixture collapses to the achromatic point $(x=1, y=1)$"
    ],
    "ans": 1,
    "exp": "Grassmann's laws of additive color mixture dictate that any additive mixture of two chromaticities $P_1(x_1, y_1)$ and $P_2(x_2, y_2)$ lies strictly on the straight line segment connecting them. Similarly, any three primaries span the interior triangle (gamut) formed by their coordinates.",
    "uni": true
  },
  {
    "id": 19,
    "unit": "Unit I",
    "chapter": 5,
    "diff": "Easy",
    "topic": "File Formats: BMP, JPEG, PNG, TIFF",
    "q": "Which standard image file format utilizes the DEFLATE algorithm (LZ77 + Huffman coding) and provides full 8-bit alpha transparency without patent encumbrances?",
    "options": [
      "BMP",
      "JPEG",
      "PNG",
      "GIF"
    ],
    "ans": 2,
    "exp": "PNG (Portable Network Graphics) was designed as an open-source, lossless replacement for GIF. It uses DEFLATE compression (a combination of LZ77 sliding window and Huffman coding) and supports 8-bit or 16-bit per channel color along with a dedicated true alpha transparency channel.",
    "uni": true
  },
  {
    "id": 20,
    "unit": "Unit I",
    "chapter": 5,
    "diff": "Moderate",
    "topic": "File Formats: BMP, JPEG, PNG, TIFF",
    "q": "What two-byte magic signature is present at the very beginning of every valid Windows BMP file header?",
    "options": [
      "`0xFF 0xD8`",
      "`0x89 0x50` ('%PNG')",
      "`0x42 0x4D` ('BM')",
      "`0x49 0x49` ('II')"
    ],
    "ans": 2,
    "exp": "Every standard Windows Bitmap (BMP) file begins with the ASCII magic characters 'B' and 'M' (`0x42 0x4D` in hexadecimal) in its 14-byte `BITMAPFILEHEADER` structure.",
    "uni": true
  },
  {
    "id": 21,
    "unit": "Unit I",
    "chapter": 5,
    "diff": "Moderate",
    "topic": "File Formats: BMP, JPEG, PNG, TIFF",
    "q": "Why is the TIFF (Tagged Image File Format) format widely favored in remote sensing, GIS, and biomedical microscopy over JPEG?",
    "options": [
      "It has the highest lossy compression ratio in existence",
      "It supports arbitrary metadata tags, floating-point radiometric values, multi-page image stacks, and geo-referencing coordinates without lossy degradation",
      "It is the only format supported by web browsers natively",
      "It completely replaces the need for sensor calibration"
    ],
    "ans": 1,
    "exp": "TIFF uses a flexible, tag-based directory structure (IFDs) allowing arbitrary custom metadata, multiple pages/stacks (e.g. confocal Z-stacks), 16/32-bit floating point pixel data, multi-spectral layers, and geographic projection metadata (GeoTIFF) with lossless compression options.",
    "uni": true
  },
  {
    "id": 22,
    "unit": "Unit I",
    "chapter": 3,
    "diff": "Easy",
    "topic": "Sampling, and Quantization",
    "q": "If an analog 2D signal has a maximum spatial frequency component of 20 cycles/mm along both axes, what is the MINIMUM sampling frequency required to prevent aliasing?",
    "options": [
      "10 samples/mm",
      "20 samples/mm",
      "40 samples/mm",
      "80 samples/mm"
    ],
    "ans": 2,
    "exp": "By the Nyquist criterion, the minimum sampling frequency $f_s$ must be at least twice the maximum signal frequency: $f_s \\ge 2 f_{\\max} = 2 \\times 20 = 40 \\text{ samples/mm}$.",
    "uni": true
  },
  {
    "id": 23,
    "unit": "Unit I",
    "chapter": 4,
    "diff": "Moderate",
    "topic": "Image Representation: Pixels, Bit Depth, and Resolution",
    "q": "In image processing coordinate conventions, what is the standard row-column $(r, c)$ indexing for an image matrix of height $M$ and width $N$?",
    "options": [
      "$r \\in [0, N-1]$ horizontally and $c \\in [0, M-1]$ vertically",
      "$r \\in [0, M-1]$ vertically downwards and $c \\in [0, N-1]$ horizontally to the right",
      "$r$ is the optical angle $\\theta$ and $c$ is the radial distance $\\rho$",
      "Indices start at $(1, 1)$ at the center of the image"
    ],
    "ans": 1,
    "exp": "In digital image matrix notation, $r$ represents the row index running vertically downwards from 0 to $M-1$, and $c$ represents the column index running horizontally to the right from 0 to $N-1$, with the origin $(0, 0)$ located at the top-left corner.",
    "uni": true
  },
  {
    "id": 24,
    "unit": "Unit I",
    "chapter": 2,
    "diff": "Moderate",
    "topic": "Image Formation",
    "q": "What is the primary technological advantage of CMOS image sensors over traditional CCD (Charge-Coupled Device) sensors in modern computer vision hardware?",
    "options": [
      "CMOS sensors have zero dark current noise and infinitely fast readout",
      "CMOS sensors allow per-pixel charge-to-voltage conversion, enabling on-chip ADC, lower power consumption, and direct digital integration",
      "CMOS sensors do not require lenses or optical focusing",
      "CMOS sensors are sensitive to radio frequency waves"
    ],
    "ans": 1,
    "exp": "CMOS (Complementary Metal-Oxide-Semiconductor) sensors feature integrated active pixel sensors (APS) with on-chip amplifiers and ADCs, consuming significantly less power, permitting random pixel access, and integrating directly with digital processing circuitry, whereas CCDs require high-voltage analog clocking.",
    "uni": true
  },
  {
    "id": 25,
    "unit": "Unit I",
    "chapter": 5,
    "diff": "Hard",
    "topic": "Color Models: RGB, HSV, CMY, YUV",
    "q": "In the standard YCbCr transformation from gamma-corrected $R'G'B'$, what is the exact formula for the luminance component $Y'$ according to ITU-R BT.601?",
    "options": [
      "$Y' = 0.333 R' + 0.333 G' + 0.333 B'$",
      "$Y' = 0.299 R' + 0.587 G' + 0.114 B'$",
      "$Y' = 0.707 R' + 0.707 G' + 0.000 B'$",
      "$Y' = \\max(R', G', B')$"
    ],
    "ans": 1,
    "exp": "Under the ITU-R BT.601 standard, perceived luminance accounts for the human eye's peak spectral sensitivity to green wavelengths: $Y' = 0.299 R' + 0.587 G' + 0.114 B'$. Green contributes roughly 59%, red 30%, and blue only 11%.",
    "uni": true
  },
  {
    "id": 26,
    "unit": "Unit II",
    "chapter": 6,
    "diff": "Easy",
    "topic": "Spatial Domain Techniques",
    "q": "Which point processing transformation is commonly used to expand the low-intensity dynamic range while compressing high-intensity values, making it ideal for visualizing the Fourier magnitude spectrum?",
    "options": [
      "Power-law (gamma) transformation with $\\gamma > 1$",
      "Logarithmic transformation $s = c \\log(1 + r)$",
      "Image negative transformation $s = (L-1) - r$",
      "Thresholding transformation"
    ],
    "ans": 1,
    "exp": "The logarithmic transformation $s = c \\log(1 + r)$ maps a narrow range of low gray-level values into a wider output range, while compressing high-level values. This is critical for displaying Fourier transforms whose dynamic ranges span several orders of magnitude ($10^5$ to $10^6$).",
    "uni": true
  },
  {
    "id": 27,
    "unit": "Unit II",
    "chapter": 6,
    "diff": "Moderate",
    "topic": "Spatial Domain Techniques",
    "q": "In power-law (gamma) transformation $s = c \\cdot r^\\gamma$, what happens to an image's visual appearance when $\\gamma < 1$?",
    "options": [
      "The image becomes darker overall, compressing shadow details",
      "The image becomes brighter overall, expanding shadow/dark details",
      "The image is inverted into a negative",
      "All edges are sharpened by the second derivative"
    ],
    "ans": 1,
    "exp": "When $\\gamma < 1$, the transformation curve bows upwards, mapping a narrow band of dark input values into a wider band of output values, brightening the image and enhancing dark shadow details (gamma correction for displays). Conversely, $\\gamma > 1$ darkens the image.",
    "uni": true
  },
  {
    "id": 28,
    "unit": "Unit II",
    "chapter": 7,
    "diff": "Moderate",
    "topic": "Histogram Equalization",
    "q": "The continuous transformation function $s = T(r) = (L-1) \\int_0^r p_r(w) \\, dw$ used in histogram equalization represents what mathematical function?",
    "options": [
      "The Probability Density Function (PDF) of the input image",
      "The Cumulative Distribution Function (CDF) scaled by $(L-1)$",
      "The 2D spatial autocorrelation function",
      "The inverse Fourier transform of the noise power spectrum"
    ],
    "ans": 1,
    "exp": "In histogram equalization, the ideal transformation function is proportional to the cumulative distribution function (CDF) of the input intensity levels. In continuous theory, this maps any input probability density function into a perfectly uniform output distribution with flat histogram.",
    "uni": true
  },
  {
    "id": 29,
    "unit": "Unit II",
    "chapter": 7,
    "diff": "Hard",
    "topic": "Histogram Equalization",
    "q": "Why does discrete histogram equalization rarely produce a completely flat, perfectly uniform output histogram in practice?",
    "options": [
      "Digital cameras cannot capture irrational intensities",
      "Because digital gray levels are discrete integers, probabilities cannot be subdivided, causing grouping/merging of gray levels into discrete spikes",
      "Because the Fourier transform of a discrete image is periodic",
      "Histogram equalization only works on binary 1-bit images"
    ],
    "ans": 1,
    "exp": "In discrete processing, pixels with identical intensity levels must map to the same quantized output integer level; pixels cannot be arbitrarily reassigned across bins. Thus, discrete histogram equalization spreads existing bins across the dynamic range, resulting in gaps and non-uniform spikes.",
    "uni": true
  },
  {
    "id": 30,
    "unit": "Unit II",
    "chapter": 7,
    "diff": "Moderate",
    "topic": "Histogram Equalization",
    "q": "What is the primary benefit of CLAHE (Contrast Limited Adaptive Histogram Equalization) over standard global histogram equalization?",
    "options": [
      "It runs in $O(1)$ constant time on all hardware",
      "It operates on local contextual tiles and clips the histogram height to prevent over-amplification of noise in homogenous regions",
      "It removes blurring caused by atmospheric turbulence",
      "It operates solely in the YUV chrominance channels"
    ],
    "ans": 1,
    "exp": "Standard histogram equalization over-amplifies noise in flat, homogeneous regions because small gradients produce huge peaks in local histograms. CLAHE divides the image into contextual tiles, clips histogram bins at a predefined limit, redistributes the excess uniformly, and blends tiles using bilinear interpolation.",
    "uni": true
  },
  {
    "id": 31,
    "unit": "Unit II",
    "chapter": 8,
    "diff": "Easy",
    "topic": "Spatial Filtering: Smoothing, Sharpening",
    "q": "What is the mathematical distinction between 2D spatial correlation and 2D spatial convolution?",
    "options": [
      "Correlation divides pixel intensities, while convolution multiplies them",
      "In convolution, the filter kernel is rotated by $180^\\circ$ before sliding and computing inner products; in correlation, it is not",
      "Correlation works only in frequency space, while convolution works in spatial space",
      "There is no difference; both operations produce identical outputs for all masks"
    ],
    "ans": 1,
    "exp": "2D convolution rotates (flips) the filter mask by $180^\\circ$ (both horizontally and vertically) prior to computing sum-of-products: $g(x,y) = \\sum \\sum w(s,t) f(x-s, y-t)$. In correlation, the mask is not rotated: $g(x,y) = \\sum \\sum w(s,t) f(x+s, y+t)$. (For symmetric filters like Gaussian, both yield identical results).",
    "uni": true
  },
  {
    "id": 32,
    "unit": "Unit II",
    "chapter": 9,
    "diff": "Moderate",
    "topic": "Spatial Filtering: Smoothing, Sharpening",
    "q": "Which non-linear spatial filter is exceptionally effective at suppressing impulse noise (salt-and-pepper noise) while preserving edge sharpness better than a linear box filter?",
    "options": [
      "Mean (average) filter",
      "Gaussian lowpass filter",
      "Median filter",
      "Laplacian filter"
    ],
    "ans": 2,
    "exp": "The median filter is a non-linear order-statistic filter that sorts all intensities in the neighborhood window and selects the middle value. Because isolated salt (255) and pepper (0) extreme values fall at the sorted ends, they are eliminated without smearing step edges.",
    "uni": true
  },
  {
    "id": 33,
    "unit": "Unit II",
    "chapter": 9,
    "diff": "Hard",
    "topic": "Spatial Filtering: Smoothing, Sharpening",
    "q": "How does a Bilateral Filter successfully smooth noise while maintaining sharp structural edges?",
    "options": [
      "It computes the fast Fourier transform and discards odd frequencies",
      "It combines a spatial Gaussian weight (closeness in coordinates) with a range Gaussian weight (photometric similarity in pixel intensity)",
      "It applies a high-boost filter followed by morphological dilation",
      "It iteratively applies Otsu thresholding"
    ],
    "ans": 1,
    "exp": "The bilateral filter computes weights based on two criteria: spatial distance (pixels close in space receive high weights) AND intensity range distance (pixels with similar gray levels receive high weights). Across an edge, range weights drop close to zero, preventing smoothing across boundaries.",
    "uni": true
  },
  {
    "id": 34,
    "unit": "Unit II",
    "chapter": 10,
    "diff": "Moderate",
    "topic": "Spatial Filtering: Smoothing, Sharpening",
    "q": "The discrete 2D Laplacian operator is given by $\\nabla^2 f(x, y) = f(x+1, y) + f(x-1, y) + f(x, y+1) + f(x, y-1) - 4f(x, y)$. What type of filter is the Laplacian?",
    "options": [
      "A non-linear smoothing filter",
      "A second-order derivative isotropic (rotation-invariant) sharpening filter",
      "A first-order directional edge detector",
      "A lowpass frequency attenuator"
    ],
    "ans": 1,
    "exp": "The Laplacian $\\nabla^2 f = \\frac{\\partial^2 f}{\\partial x^2} + \\frac{\\partial^2 f}{\\partial y^2}$ is a linear, second-order derivative operator. Being an isotropic filter, its response is invariant to the rotation of discontinuities in the image.",
    "uni": true
  },
  {
    "id": 35,
    "unit": "Unit II",
    "chapter": 10,
    "diff": "Moderate",
    "topic": "Edge Detection",
    "q": "What is the primary operational difference between the response of a first-order derivative (e.g., Sobel) and a second-order derivative (e.g., Laplacian) at a ramp edge?",
    "options": [
      "First derivatives produce zero at ramps; second derivatives produce a constant value",
      "First derivatives produce a broad, thick response along the ramp; second derivatives produce a double response with a zero-crossing at the center",
      "First derivatives invert the image negative; second derivatives do not",
      "First derivatives only detect vertical lines"
    ],
    "ans": 1,
    "exp": "At a ramp transition, the first derivative produces a broad constant plateau proportional to the slope. The second derivative produces an initial pulse at the start of the ramp, zero along the linear slope, and an opposite pulse at the end, crossing zero precisely at the edge midpoint (zero-crossing).",
    "uni": true
  },
  {
    "id": 36,
    "unit": "Unit II",
    "chapter": 10,
    "diff": "Hard",
    "topic": "Edge Detection",
    "q": "Which of the following describes the complete four-stage sequence of the Canny Edge Detection algorithm?",
    "options": [
      "Histogram Equalization $\\to$ Sobel Mask $\\to$ Thresholding $\\to$ Dilation",
      "Gaussian Smoothing $\\to$ Gradient Calculation $\\to$ Non-Maximum Suppression $\\to$ Hysteresis Thresholding",
      "Laplacian of Gaussian $\\to$ Zero-Crossing $\\to$ Region Growing $\\to$ Pruning",
      "Fourier Transform $\\to$ Butterworth Filter $\\to$ Inverse FFT $\\to$ Binarization"
    ],
    "ans": 1,
    "exp": "John Canny's optimal edge detector executes four steps: 1. Gaussian convolution to remove noise; 2. Gradient magnitude & angle calculation (Sobel); 3. Non-Maximum Suppression (thinning edge ridges to 1-pixel width); 4. Dual-threshold hysteresis tracking (linking weak edges connected to strong edges).",
    "uni": true
  },
  {
    "id": 37,
    "unit": "Unit II",
    "chapter": 10,
    "diff": "Easy",
    "topic": "Edge Detection",
    "q": "The Sobel horizontal gradient operator kernel $G_x$ incorporates smoothing along the perpendicular axis using which specific weights?",
    "options": [
      "$\\begin{bmatrix} -1 & 0 & 1 \\\\ -1 & 0 & 1 \\\\ -1 & 0 & 1 \\end{bmatrix}$ (Prewitt)",
      "$\\begin{bmatrix} -1 & 0 & 1 \\\\ -2 & 0 & 2 \\\\ -1 & 0 & 1 \\end{bmatrix}$ (Sobel)",
      "$\\begin{bmatrix} 0 & 1 \\\\ -1 & 0 \\end{bmatrix}$ (Roberts)",
      "$\\begin{bmatrix} 0 & -1 & 0 \\\\ -1 & 4 & -1 \\\\ 0 & -1 & 0 \\end{bmatrix}$ (Laplacian)"
    ],
    "ans": 1,
    "exp": "The Sobel operator applies a central difference derivative in the $x$-direction combined with triangular $[1, 2, 1]^T$ smoothing in the $y$-direction to suppress noise: $G_x = \\begin{bmatrix} -1 & 0 & 1 \\\\ -2 & 0 & 2 \\\\ -1 & 0 & 1 \\end{bmatrix}$.",
    "uni": true
  },
  {
    "id": 38,
    "unit": "Unit II",
    "chapter": 11,
    "diff": "Easy",
    "topic": "Frequency Domain Techniques",
    "q": "Before computing the 2D Discrete Fourier Transform (DFT), multiplying the input spatial image by $(-1)^{x+y}$ achieves what useful effect?",
    "options": [
      "Inverts the image contrast into a photographic negative",
      "Shifts the zero-frequency DC component $F(0, 0)$ to the center of the frequency spectrum $(M/2, N/2)$",
      "Multiplies all frequencies by $\\pi$",
      "Eliminates high-frequency sensor noise"
    ],
    "ans": 1,
    "exp": "By the frequency shift property of the Fourier Transform, $f(x, y) e^{j 2\\pi (u_0 x / M + v_0 y / N)} \\iff F(u - u_0, v - v_0)$. Setting $u_0 = M/2$ and $v_0 = N/2$ gives $e^{j \\pi (x + y)} = (-1)^{x+y}$, which shifts the DC origin to the center of the frequency plane.",
    "uni": true
  },
  {
    "id": 39,
    "unit": "Unit II",
    "chapter": 11,
    "diff": "Moderate",
    "topic": "Frequency Domain Techniques",
    "q": "What structural information is predominantly encoded in the PHASE angle $\\phi(u, v) = \\arctan[I(u, v) / R(u, v)]$ of an image's Fourier Transform?",
    "options": [
      "Overall average illumination and global contrast",
      "Spatial location of edges, lines, corners, and structural geometry",
      "Color saturation values only",
      "The exact number of quantization levels"
    ],
    "ans": 1,
    "exp": "Experiments in Fourier synthesis (e.g., Oppenheim) demonstrated that the phase spectrum carries the critical spatial positioning of edges, shapes, and structural geometry. Reconstructing an image with correct phase and unity magnitude yields recognizable objects, whereas correct magnitude and random phase yields pure noise.",
    "uni": true
  },
  {
    "id": 40,
    "unit": "Unit II",
    "chapter": 12,
    "diff": "Moderate",
    "topic": "Frequency Filters: Low-Pass, High-Pass, Band-Pass",
    "q": "Why does an Ideal Lowpass Filter (ILPF) produce pronounced circular ringing artifacts (ripples) around sharp edges in the filtered spatial image?",
    "options": [
      "Because its frequency cutoff $D_0$ must always be zero",
      "Because the inverse Fourier transform of a sharp step cylinder in frequency space is a spatial 2D sinc function (Bessel function of the first kind) with oscillating side lobes",
      "Because the ILPF introduces non-linear phase distortion",
      "Because digital sensors cannot process negative frequencies"
    ],
    "ans": 1,
    "exp": "The transfer function of an ideal lowpass filter is a sharp box/cylinder in frequency space. By the convolution theorem, filtering in frequency is convolution in space with the filter's spatial impulse response, which is $h(r) \\propto J_1(2\\pi D_0 r) / r$ (a Bessel/sinc wave). The decaying oscillatory lobes cause visible ringing.",
    "uni": true
  },
  {
    "id": 41,
    "unit": "Unit II",
    "chapter": 12,
    "diff": "Moderate",
    "topic": "Frequency Filters: Low-Pass, High-Pass, Band-Pass",
    "q": "Which frequency-domain lowpass filter guarantees ZERO spatial ringing artifacts at all cutoff frequencies?",
    "options": [
      "Ideal Lowpass Filter (ILPF)",
      "Butterworth Lowpass Filter of order $n = 4$",
      "Gaussian Lowpass Filter (GLPF)",
      "High-Boost Filter"
    ],
    "ans": 2,
    "exp": "The Fourier transform of a Gaussian function is another Gaussian function ($e^{-D^2/2D_0^2} \\iff 2\\pi D_0^2 e^{-2\\pi^2 D_0^2 r^2}$). Because the Gaussian has no secondary sidelobes or oscillations in either domain, the Gaussian Lowpass Filter yields completely smooth blurring with zero ringing.",
    "uni": true
  },
  {
    "id": 42,
    "unit": "Unit II",
    "chapter": 12,
    "diff": "Moderate",
    "topic": "Frequency Filters: Low-Pass, High-Pass, Band-Pass",
    "q": "The transfer function of a Butterworth Lowpass Filter (BLPF) of order $n$ with cutoff frequency $D_0$ is given by:",
    "options": [
      "$H(u, v) = \\frac{1}{1 + [D(u, v) / D_0]^{2n}}$",
      "$H(u, v) = 1 - e^{-D^2(u,v) / 2D_0^2}$",
      "$H(u, v) = \\frac{D(u, v)}{D_0}$",
      "$H(u, v) = \\log(1 + D(u, v))$"
    ],
    "ans": 0,
    "exp": "The standard Butterworth LPF formula is $H(u, v) = \\frac{1}{1 + [D(u, v) / D_0]^{2n}}$. When $D(u,v) = D_0$, $H(u,v) = 0.5$ (or $1/\\sqrt{2}$ in power), providing a smooth transition controlled by order $n$ without the abrupt step of an ideal filter.",
    "uni": true
  },
  {
    "id": 43,
    "unit": "Unit II",
    "chapter": 13,
    "diff": "Moderate",
    "topic": "Noise Reduction and Image Restoration Techniques",
    "q": "Which noise probability density function is characterized by having zero probability for values less than a threshold $a$, an asymmetric right-skewed tail, and is commonly found in radar, sonar, and ultrasound imaging?",
    "options": [
      "Gaussian noise",
      "Uniform noise",
      "Rayleigh noise",
      "Salt-and-pepper noise"
    ],
    "ans": 2,
    "exp": "Rayleigh noise has the PDF $p(z) = \\frac{2}{b}(z - a) e^{-(z-a)^2 / b}$ for $z \\ge a$ and $0$ for $z < a$. It exhibits a strict lower bound $a$ with a skewed positive tail and models range imaging modalities like ultrasound, MRI magnitude, and coherent radar speckle.",
    "uni": true
  },
  {
    "id": 44,
    "unit": "Unit II",
    "chapter": 13,
    "diff": "Easy",
    "topic": "Noise Reduction and Image Restoration Techniques",
    "q": "Periodic electrical or optical interference that manifests as repetitive sinusoidal ripples across an image appears in the 2D Fourier spectrum as:",
    "options": [
      "A completely flat, uniform white background",
      "Symmetric, concentrated pairs of high-intensity impulse energy spikes off the DC center",
      "A single continuous dark ring of radius $D_0$",
      "Zero values everywhere except the origin"
    ],
    "ans": 1,
    "exp": "A spatial sinusoidal pattern $A \\cos(u_0 x + v_0 y)$ transforms into a pair of symmetric Dirac delta spikes in the frequency domain at $\\pm(u_0, v_0)$. This property allows periodic noise to be eliminated cleanly using a Notch Reject filter.",
    "uni": true
  },
  {
    "id": 45,
    "unit": "Unit II",
    "chapter": 14,
    "diff": "Hard",
    "topic": "Noise Reduction and Image Restoration Techniques",
    "q": "In image restoration, direct Inverse Filtering $\\hat{F}(u, v) = \\frac{G(u, v)}{H(u, v)} = F(u, v) + \\frac{N(u, v)}{H(u, v)}$ fails catastrophically in the presence of noise because:",
    "options": [
      "The Fourier transform cannot be inverted on computers",
      "Degradation transfer functions $H(u, v)$ typically decay to near-zero values at high frequencies, causing $\\frac{N(u, v)}{H(u, v)}$ to explode and overwhelm the true signal",
      "Convolution does not hold in the spatial domain",
      "Noise power spectra are always infinite at $u=0, v=0$"
    ],
    "ans": 1,
    "exp": "Physical blur transfer functions $H(u, v)$ (e.g. motion, defocus, atmosphere) act as low-pass filters whose values drop rapidly toward zero at high spatial frequencies. Dividing random additive noise $N(u, v)$ by tiny numbers near zero amplifies high-frequency noise catastrophically, obscuring the image.",
    "uni": true
  },
  {
    "id": 46,
    "unit": "Unit II",
    "chapter": 14,
    "diff": "Hard",
    "topic": "Noise Reduction and Image Restoration Techniques",
    "q": "The Wiener Filter (Minimum Mean Square Error filter) addresses the inverse filter failure by incorporating what critical ratio?",
    "options": [
      "Signal-to-noise power spectral density ratio: $\\frac{S_\\eta(u, v)}{S_f(u, v)}$",
      "The image aspect ratio $M / N$",
      "The ratio of quantization bits to color channels",
      "The spatial gradient ratio $G_y / G_x$"
    ],
    "ans": 0,
    "exp": "The Wiener filter transfer function is $\\hat{F}(u,v) = \\left[ \\frac{H^*(u,v)}{|H(u,v)|^2 + S_\\eta(u,v)/S_f(u,v)} \\right] G(u,v)$. When the noise power is high or signal is low, the ratio $S_\\eta/S_f$ dominates the denominator, gracefully attenuating corrupted frequencies rather than blowing up.",
    "uni": true
  },
  {
    "id": 47,
    "unit": "Unit II",
    "chapter": 14,
    "diff": "Hard",
    "topic": "Noise Reduction and Image Restoration Techniques",
    "q": "What is the primary operational advantage of the Constrained Least Squares (CLS) filter over the Wiener filter in practical engineering?",
    "options": [
      "CLS runs in time $O(N)$ without Fourier transforms",
      "CLS does not require prior knowledge of the power spectral densities of the signal and noise, relying instead on a second-order smoothness constraint (Laplacian $P(u, v)$) and noise variance",
      "CLS only restores color images",
      "CLS is completely immune to motion blur"
    ],
    "ans": 1,
    "exp": "Wiener filtering requires knowing the explicit power spectral density $S_f(u, v)$ of the uncorrupted image, which is rarely known in practice. CLS minimizes the second derivative (smoothness via Laplacian $P(u,v)$) subject to matching the noise variance, requiring only the degradation function $H(u,v)$ and noise statistics.",
    "uni": true
  },
  {
    "id": 48,
    "unit": "Unit II",
    "chapter": 8,
    "diff": "Easy",
    "topic": "Spatial Filtering: Smoothing, Sharpening",
    "q": "When applying a $5 \\times 5$ spatial filter kernel to an $M \\times N$ image, how many rows and columns of border padding are required to preserve the original image dimensions with 'Same' padding?",
    "options": [
      "1 row and 1 column",
      "2 rows and 2 columns on all four borders (padding $P = 2$)",
      "4 rows and 4 columns",
      "5 rows and 5 columns"
    ],
    "ans": 1,
    "exp": "To maintain spatial dimensions with an odd kernel of size $K \\times K$, the required zero-padding on each side is $P = (K - 1) / 2 = (5 - 1) / 2 = 2$ pixels.",
    "uni": true
  },
  {
    "id": 49,
    "unit": "Unit II",
    "chapter": 10,
    "diff": "Moderate",
    "topic": "Spatial Filtering: Smoothing, Sharpening",
    "q": "In Unsharp Masking, the sharpened image $g(x, y)$ is created by subtracting a blurred version $f_{\\text{smooth}}(x, y)$ from the original $f(x, y)$ to create a mask, and adding it back: $g = f + k \\cdot (f - f_{\\text{smooth}})$. If $k > 1$, the process is specifically referred to as:",
    "options": [
      "High-pass filtering",
      "High-boost filtering",
      "Low-boost filtering",
      "Homomorphic filtering"
    ],
    "ans": 1,
    "exp": "When $k = 1$, the process is standard unsharp masking. When $k > 1$, a larger portion of the edge-emphasizing unsharp mask is added back to the original image, which is known as High-Boost filtering.",
    "uni": true
  },
  {
    "id": 50,
    "unit": "Unit II",
    "chapter": 11,
    "diff": "Moderate",
    "topic": "Frequency Domain Techniques",
    "q": "The 2D Convolution Theorem states that spatial convolution of an image $f(x, y)$ with a filter $h(x, y)$ corresponds in the frequency domain to:",
    "options": [
      "Pointwise addition: $F(u, v) + H(u, v)$",
      "Pointwise multiplication: $F(u, v) \\cdot H(u, v)$",
      "Frequency division: $F(u, v) / H(u, v)$",
      "Matrix transposition: $F(u, v)^T$"
    ],
    "ans": 1,
    "exp": "The Convolution Theorem is a foundational property: $f(x, y) * h(x, y) \\iff F(u, v) \\cdot H(u, v)$. Spatial convolution transforms into simple element-wise multiplication in the frequency domain, enabling fast filtering via the FFT.",
    "uni": true
  },
  {
    "id": 51,
    "unit": "Unit III",
    "chapter": 15,
    "diff": "Easy",
    "topic": "Image Segmentation",
    "q": "Image segmentation algorithms are fundamentally categorized based on which two basic intensity properties?",
    "options": [
      "Hue and Saturation",
      "Discontinuity (e.g., edges, points, lines) and Similarity (e.g., thresholding, region growing)",
      "Bit depth and Sampling rate",
      "Spatial resolution and Temporal frequency"
    ],
    "ans": 1,
    "exp": "Image segmentation approaches partition an image based on either: 1. Discontinuity (abrupt local changes in intensity, such as isolated points, lines, and edges); or 2. Similarity (grouping pixels that satisfy homogeneity predicates, such as thresholding, region growing, and splitting/merging).",
    "uni": true
  },
  {
    "id": 52,
    "unit": "Unit III",
    "chapter": 16,
    "diff": "Moderate",
    "topic": "Thresholding (Global, Adaptive)",
    "q": "Otsu's optimal thresholding algorithm automatically selects an intensity threshold $k^*$ by maximizing which statistical measure?",
    "options": [
      "Within-class variance $\\sigma_W^2$",
      "Between-class variance $\\sigma_B^2(k) = \\omega_0(k)(\\mu_0 - \\mu_T)^2 + \\omega_1(k)(\\mu_1 - \\mu_T)^2$",
      "The sum of squared Laplacian gradients",
      "The Shannon entropy of the color histogram"
    ],
    "ans": 1,
    "exp": "Otsu's method exhaustively evaluates all candidate thresholds $k$ to maximize the between-class variance $\\sigma_B^2(k)$ (or equivalently minimize within-class variance $\\sigma_W^2$). Maximizing between-class separation ensures the background and foreground classes are as statistically distinct as possible.",
    "uni": true
  },
  {
    "id": 53,
    "unit": "Unit III",
    "chapter": 16,
    "diff": "Hard",
    "topic": "Thresholding (Global, Adaptive)",
    "q": "Under what lighting condition does global thresholding (such as Otsu's method) fail completely, necessitating adaptive or local thresholding?",
    "options": [
      "Uniform studio lighting",
      "Severe non-uniform, uneven spatial illumination across the image field",
      "Monochromatic light sources",
      "High bit depth (16-bit) images"
    ],
    "ans": 1,
    "exp": "Global thresholding applies a single scalar threshold across all pixels. When illumination varies non-uniformly across the scene (e.g. shadows, vignetting), dark background areas in bright regions can be brighter than foreground text in shadowed regions, causing catastrophic segmentation errors.",
    "uni": true
  },
  {
    "id": 54,
    "unit": "Unit III",
    "chapter": 17,
    "diff": "Moderate",
    "topic": "Region-Based Segmentation",
    "q": "In Region Growing segmentation, what are the three essential components required to execute the algorithm?",
    "options": [
      "A high-pass filter, a low-pass filter, and a cutoff radius",
      "Seed points, a similarity criterion (growth predicate), and a stopping rule",
      "Four corner coordinates, a bounding box, and an anchor scale",
      "A DCT matrix, a quantization table, and a Huffman tree"
    ],
    "ans": 1,
    "exp": "Region growing groups neighboring pixels into larger regions based on: 1. Initial seed points (manually chosen or automated); 2. A similarity criterion/predicate (e.g., intensity within $\\pm T$ of the seed mean); and 3. A stopping rule (when no unassigned neighbor satisfies the predicate).",
    "uni": true
  },
  {
    "id": 55,
    "unit": "Unit III",
    "chapter": 17,
    "diff": "Moderate",
    "topic": "Region-Based Segmentation",
    "q": "The Region Splitting and Merging algorithm utilizes which hierarchical data structure to represent quadrants of the image during iterative partitioning?",
    "options": [
      "Binary search tree",
      "Quadtree",
      "Red-black tree",
      "B-Tree"
    ],
    "ans": 1,
    "exp": "Region splitting and merging partitions an image into 4 quadrants. If a quadrant does not satisfy homogeneity predicate $P(R_i)$, it is subdivided into 4 subquadrants. This hierarchical spatial structure is stored as a Quadtree where each node has up to four children.",
    "uni": true
  },
  {
    "id": 56,
    "unit": "Unit III",
    "chapter": 17,
    "diff": "Hard",
    "topic": "Region-Based Segmentation",
    "q": "What severe practical flaw typically occurs when applying the classic Watershed Segmentation algorithm to raw gradient images without preprocessing, and how is it solved?",
    "options": [
      "Under-segmentation into a single giant region; solved by increasing contrast",
      "Catastrophic oversegmentation due to microscopic noise peaks; solved by Marker-Controlled Watersheds",
      "Loss of all boundary connectivity; solved by median filtering",
      "Infinite loops during flooding; solved by thresholding"
    ],
    "ans": 1,
    "exp": "Because raw image gradients contain thousands of microscopic local minima caused by sensor noise, standard watershed simulation treats every minimum as a catchment basin, causing severe oversegmentation (thousands of tiny fragmented regions). Marker-controlled watersheds solve this by restricting flooding to designated internal and external markers.",
    "uni": true
  },
  {
    "id": 57,
    "unit": "Unit III",
    "chapter": 18,
    "diff": "Easy",
    "topic": "Morphological Operations: Erosion, Dilation, Opening, Closing",
    "q": "In mathematical morphology, binary EROSION of set $A$ by structuring element $B$ is formally defined as $A \\ominus B = \\{z \\mid (B)_z \\subseteq A\\}$. What is the physical visual effect of erosion on foreground objects?",
    "options": [
      "Expands foreground boundaries and fills small holes",
      "Shrinks/thins foreground objects and eliminates small isolated noise components",
      "Rotates the image by $90^\\circ$",
      "Inverts all pixel values"
    ],
    "ans": 1,
    "exp": "Erosion tests whether the translated structuring element $(B)_z$ is completely contained within the foreground set $A$. Boundary pixels where $B$ overhangs into the background are turned off, shrinking foreground objects and stripping away thin protrusions and small noise specks.",
    "uni": true
  },
  {
    "id": 58,
    "unit": "Unit III",
    "chapter": 18,
    "diff": "Moderate",
    "topic": "Morphological Operations: Erosion, Dilation, Opening, Closing",
    "q": "Morphological OPENING of set $A$ by structuring element $B$ is defined as erosion followed by dilation: $A \\circ B = (A \\ominus B) \\oplus B$. What does morphological opening accomplish?",
    "options": [
      "Bridges narrow breaks and fills small dark holes in objects",
      "Smooths object contours, breaks thin isthmuses/necks, and eliminates small foreground protrusions",
      "Doubles the spatial resolution of the image",
      "Extracts internal skeleton lines"
    ],
    "ans": 1,
    "exp": "Opening ($A \\circ B$) eliminates small bright foreground details, severs thin bridges between objects, and smooths outer object contours without changing the global geometry of large components. Morphological Closing ($A \\bullet B$), by contrast, fills small dark holes and connects narrow gaps.",
    "uni": true
  },
  {
    "id": 59,
    "unit": "Unit III",
    "chapter": 18,
    "diff": "Moderate",
    "topic": "Morphological Operations: Erosion, Dilation, Opening, Closing",
    "q": "Which morphological operation is specifically designed for template matching to detect the exact presence of a particular binary shape configuration within an image?",
    "options": [
      "Top-hat transform",
      "Hit-or-Miss transform ($A \\circledast B$)",
      "Morphological gradient",
      "Geodesic dilation"
    ],
    "ans": 1,
    "exp": "The Hit-or-Miss transform $A \\circledast B = (A \\ominus B_1) \\cap (A^c \\ominus B_2)$ uses a dual structuring element $B = (B_1, B_2)$ where $B_1$ tests for the presence of the foreground shape (hit) and $B_2$ tests for the enclosing background boundary (miss), identifying exact geometric configurations.",
    "uni": true
  },
  {
    "id": 60,
    "unit": "Unit III",
    "chapter": 19,
    "diff": "Moderate",
    "topic": "Image Features and Descriptors",
    "q": "In the Harris Corner Detector, the local auto-correlation matrix (structure tensor) is given by $M = \\sum w(x,y) \\begin{bmatrix} I_x^2 & I_x I_y \\\\ I_x I_y & I_y^2 \\end{bmatrix}$. A region is classified as a CORNER when its eigenvalues $\\lambda_1$ and $\\lambda_2$ satisfy:",
    "options": [
      "Both $\\lambda_1 \\approx 0$ and $\\lambda_2 \\approx 0$ (flat region)",
      "One eigenvalue is large and the other is near zero (edge)",
      "Both eigenvalues $\\lambda_1$ and $\\lambda_2$ are simultaneously large and positive",
      "Both eigenvalues are negative"
    ],
    "ans": 2,
    "exp": "The eigenvalues of the structure tensor describe the directional intensity variations in the local window. If both $\\lambda_1$ and $\\lambda_2$ are large, intensity changes significantly in all directions, defining a true 2D corner. If only one is large, it represents an edge; if both are small, it is a flat region.",
    "uni": true
  },
  {
    "id": 61,
    "unit": "Unit III",
    "chapter": 19,
    "diff": "Hard",
    "topic": "Image Features and Descriptors",
    "q": "Ming-Kuei Hu derived seven moment invariants ($\\\\phi_1$ through $\\\\phi_7$) calculated from normalized central moments. These moments are invariant to which set of geometric transformations?",
    "options": [
      "Perspective distortion and affine shear",
      "Translation, scale change, and planar rotation (and mirroring up to sign)",
      "Non-rigid deformations and elastic stretching",
      "Occlusion and random Poisson noise"
    ],
    "ans": 1,
    "exp": "Hu's 7 Moment Invariants are nonlinear combinations of 2nd and 3rd order normalized central moments that remain invariant under 2D translation (due to central moments), scale changes (due to normalization by $\\eta_{ij} = \\mu_{ij}/\\mu_{00}^\\gamma$), and in-plane rotation.",
    "uni": true
  },
  {
    "id": 62,
    "unit": "Unit III",
    "chapter": 20,
    "diff": "Moderate",
    "topic": "SIFT, SURF, HOG",
    "q": "How does the SIFT (Scale-Invariant Feature Transform) algorithm efficiently approximate the scale-normalized Laplacian of Gaussian (LoG) across octaves?",
    "options": [
      "By taking the 2D Fourier Transform of the gradient magnitude",
      "By subtracting adjacent Gaussian-smoothed images: Difference of Gaussians (DoG) $D(x, y, \\sigma) = L(x, y, k\\sigma) - L(x, y, \\sigma)$",
      "By applying Sobel operators with increasing stride",
      "By computing morphological hit-or-miss transforms"
    ],
    "ans": 1,
    "exp": "Lindeberg proved that $\\sigma^2 \\nabla^2 G$ provides true scale invariance. David Lowe showed that the Difference of Gaussians (DoG) $D(x, y, \\sigma) = (G(x,y,k\\sigma) - G(x,y,\\sigma)) * I(x,y)$ provides a close approximation to $\\sigma^2 \\nabla^2 G$ using simple image subtractions across octaves.",
    "uni": true
  },
  {
    "id": 63,
    "unit": "Unit III",
    "chapter": 20,
    "diff": "Hard",
    "topic": "SIFT, SURF, HOG",
    "q": "What is the dimensionality and spatial arrangement of the canonical SIFT feature descriptor for a localized keypoint?",
    "options": [
      "64 dimensions: an $8 \\times 8$ grid of raw pixel intensities",
      "128 dimensions: a $4 \\times 4$ spatial grid of subregions, each compiling an 8-bin orientation histogram ($4 \\times 4 \\times 8 = 128$)",
      "256 dimensions: a 16-bin color histogram across 16 scale levels",
      "32 dimensions: a binary string of pairwise comparisons"
    ],
    "ans": 1,
    "exp": "The canonical SIFT descriptor samples gradients around the keypoint aligned to its dominant orientation, partitions the $16 \\times 16$ window into a $4 \\times 4$ grid of cells, and computes an 8-bin gradient orientation histogram in each cell: $4 \\times 4 \\times 8 = 128$ floating-point dimensions.",
    "uni": true
  },
  {
    "id": 64,
    "unit": "Unit III",
    "chapter": 20,
    "diff": "Moderate",
    "topic": "SIFT, SURF, HOG",
    "q": "What computational data structure allows the SURF (Speeded-Up Robust Features) algorithm to compute box-filter convolutions in $O(1)$ constant time regardless of filter scale?",
    "options": [
      "Kd-tree",
      "Integral Image (Summed-Area Table)",
      "Skip list",
      "Huffman tree"
    ],
    "ans": 1,
    "exp": "SURF uses the Integral Image $I_\\Sigma(x,y) = \\sum_{x' \\le x, y' \\le y} I(x', y')$. Any rectangular box sum can be evaluated using only 4 array lookups ($D - B - C + A$) in $O(1)$ constant time, enabling ultra-fast multi-scale Hessian approximations.",
    "uni": true
  },
  {
    "id": 65,
    "unit": "Unit III",
    "chapter": 20,
    "diff": "Moderate",
    "topic": "SIFT, SURF, HOG",
    "q": "In Dalal & Triggs' Histogram of Oriented Gradients (HOG) object detector (widely used for pedestrian detection), what is the standard number of orientation bins and angle range used per cell?",
    "options": [
      "4 bins spanning $0^\\circ - 90^\\circ$",
      "9 bins spanning $0^\\circ - 180^\\circ$ (unsigned gradients)",
      "36 bins spanning $0^\\circ - 360^\\circ$ (signed gradients)",
      "256 bins spanning all gray levels"
    ],
    "ans": 1,
    "exp": "Dalal and Triggs discovered that unsigned gradient orientations ($0^\\circ$ to $180^\\circ$) divided into 9 discrete angular bins ($20^\\circ$ each) provide optimal performance for pedestrian detection, making edge contrast insensitive to clothing color polarity.",
    "uni": true
  },
  {
    "id": 66,
    "unit": "Unit III",
    "chapter": 21,
    "diff": "Easy",
    "topic": "Image Compression, Lossless vs. Lossy Compression",
    "q": "Which of the following is NOT one of the three fundamental data redundancies targeted by image compression algorithms?",
    "options": [
      "Coding redundancy (sub-optimal symbol code lengths)",
      "Spatial / Interpixel redundancy (high correlation between neighboring pixels)",
      "Psychovisual redundancy (details the human eye cannot perceive)",
      "Electromagnetic quantum redundancy"
    ],
    "ans": 3,
    "exp": "The three classical data redundancies in digital image compression are: 1. Coding redundancy (using fixed-length codes instead of variable-length entropy codes); 2. Interpixel/Spatial redundancy (correlation between adjacent pixels); and 3. Psychovisual redundancy (information eliminated by lossy compression because human vision ignores it).",
    "uni": true
  },
  {
    "id": 67,
    "unit": "Unit III",
    "chapter": 21,
    "diff": "Moderate",
    "topic": "Image Compression, Lossless vs. Lossy Compression",
    "q": "For an 8-bit image with Mean Squared Error (MSE), what is the standard formula for Peak Signal-to-Noise Ratio (PSNR) in decibels (dB)?",
    "options": [
      "$\\text{PSNR} = 10 \\log_{10} \\left( \\frac{255^2}{\\text{MSE}} \\right)$",
      "$\\text{PSNR} = 20 \\log_{10} \\left( \\frac{\\text{MSE}}{255} \\right)$",
      "$\\text{PSNR} = \\frac{255}{\\sqrt{\\text{MSE}}}$",
      "$\\text{PSNR} = 100 \\times (1 - \\text{MSE})$"
    ],
    "ans": 0,
    "exp": "PSNR is defined as $\\text{PSNR} = 10 \\log_{10} \\left( \\frac{\\text{MAX}_I^2}{\\text{MSE}} \\right) = 20 \\log_{10} \\left( \\frac{255}{\\sqrt{\\text{MSE}}} \\right)$ for 8-bit images where $\\text{MAX}_I = 2^8 - 1 = 255$. Typical acceptable lossy compression yields PSNR values between 30 dB and 50 dB.",
    "uni": true
  },
  {
    "id": 68,
    "unit": "Unit III",
    "chapter": 22,
    "diff": "Moderate",
    "topic": "Image Compression, Lossless vs. Lossy Compression",
    "q": "According to Claude Shannon's Source Coding Theorem, what fundamental quantity defines the absolute theoretical lower bound on average code length (in bits/symbol) for lossless encoding of an information source with symbol probabilities $p_i$?",
    "options": [
      "The standard deviation $\\sigma$",
      "Shannon Entropy $H(X) = -\\sum_{i=1}^n p_i \\log_2 p_i$",
      "The Nyquist rate $2 f_{\\max}$",
      "The dynamic range $2^k - 1$"
    ],
    "ans": 1,
    "exp": "Shannon's noiseless source coding theorem establishes that the average code word length $L_{\\text{avg}} \\ge H(X)$, where entropy $H(X) = -\\sum p_i \\log_2 p_i$ measures the fundamental uncertainty/information content. No lossless coding system can represent the source in fewer average bits than $H(X)$.",
    "uni": true
  },
  {
    "id": 69,
    "unit": "Unit III",
    "chapter": 22,
    "diff": "Moderate",
    "topic": "Image Compression, Lossless vs. Lossy Compression",
    "q": "What essential mathematical property is guaranteed by Huffman Coding?",
    "options": [
      "It produces lossy floating-point coefficients",
      "It yields an optimal, prefix-free variable-length code that minimizes average code length for a given set of symbol probabilities",
      "It runs in $O(1)$ constant time",
      "It completely eliminates psychovisual redundancy"
    ],
    "ans": 1,
    "exp": "Huffman coding is an optimal prefix-free source coding method. Prefix-free means no codeword is a prefix of any other codeword (allowing instantaneous decoding without delimiters). By assigning shorter binary codewords to frequent symbols, it minimizes expected code length.",
    "uni": true
  },
  {
    "id": 70,
    "unit": "Unit III",
    "chapter": 23,
    "diff": "Moderate",
    "topic": "JPEG Compression Steps and Implementation",
    "q": "In the standard baseline JPEG compression pipeline, which specific stage is responsible for all information LOSS?",
    "options": [
      "Color space conversion from RGB to YCbCr",
      "Forward 2D Discrete Cosine Transform (2D-DCT)",
      "Quantization of DCT coefficients by the quantization matrix",
      "Zig-zag scanning and Huffman entropy coding"
    ],
    "ans": 2,
    "exp": "The forward 2D-DCT and Huffman entropy coding stages are mathematically reversible (lossless). Information loss in JPEG occurs exclusively during the Quantization step, where high-frequency DCT coefficients are divided by large quantization factors and rounded to the nearest integer, permanently discarding subtle high-frequency details.",
    "uni": true
  },
  {
    "id": 71,
    "unit": "Unit III",
    "chapter": 23,
    "diff": "Easy",
    "topic": "JPEG Compression Steps and Implementation",
    "q": "What is the standard block size into which an image component is partitioned prior to computing the 2D-DCT in baseline JPEG?",
    "options": [
      "$4 \\times 4$ pixels",
      "$8 \\times 8$ pixels",
      "$16 \\times 16$ pixels",
      "$64 \\times 64$ pixels"
    ],
    "ans": 1,
    "exp": "Baseline JPEG subdivides each color channel into non-overlapping blocks of $8 \\times 8$ pixels. This block size provides an optimal compromise between high energy compaction and low computational complexity.",
    "uni": true
  },
  {
    "id": 72,
    "unit": "Unit III",
    "chapter": 23,
    "diff": "Moderate",
    "topic": "JPEG Compression Steps and Implementation",
    "q": "Why does baseline JPEG reorder the quantized 2D $8 \\times 8$ DCT matrix using a ZIG-ZAG scanning pattern before entropy encoding?",
    "options": [
      "To encrypt the image data against unauthorized decoding",
      "To group low-frequency coefficients first and order higher frequencies into long contiguous runs of zeros, maximizing Run-Length Encoding efficiency",
      "To convert 8-bit pixels into 16-bit floating-point numbers",
      "To compute the inverse Fourier transform faster"
    ],
    "ans": 1,
    "exp": "Because high-frequency coefficients located towards the bottom-right of the $8 \\times 8$ matrix are heavily quantized to zero, zig-zag scanning transverses diagonals from top-left (DC and low frequencies) to bottom-right, producing long consecutive runs of zero values terminated by an End-Of-Block (EOB) symbol.",
    "uni": true
  },
  {
    "id": 73,
    "unit": "Unit III",
    "chapter": 23,
    "diff": "Hard",
    "topic": "JPEG Compression Steps and Implementation",
    "q": "How is the single DC coefficient ($C(0, 0)$) of each $8 \\times 8$ block encoded in baseline JPEG?",
    "options": [
      "It is quantized to zero and discarded",
      "It is encoded differentially relative to the DC coefficient of the preceding block (DPCM: $\\Delta \\text{DC} = \\text{DC}_k - \\text{DC}_{k-1}$)",
      "It is stored as an uncompressed 32-bit floating-point float",
      "It is averaged across all pixels in the entire image"
    ],
    "ans": 1,
    "exp": "Because average brightness varies smoothly between adjacent $8 \\times 8$ blocks, DC coefficients exhibit strong inter-block correlation. JPEG encodes DC coefficients differentially (using Differential Pulse Code Modulation DPCM), recording only the difference $\\Delta \\text{DC}$ between consecutive blocks.",
    "uni": true
  },
  {
    "id": 74,
    "unit": "Unit III",
    "chapter": 24,
    "diff": "Moderate",
    "topic": "Image Compression, Lossless vs. Lossy Compression",
    "q": "What major artifact seen in high-compression DCT JPEG images is completely avoided by the Discrete Wavelet Transform (DWT) used in JPEG 2000?",
    "options": [
      "False contouring",
      "Blocking artifacts (mosaic grid boundaries)",
      "Color fringing",
      "Salt-and-pepper noise"
    ],
    "ans": 1,
    "exp": "Because standard JPEG processes independent $8 \\times 8$ blocks, high compression discards inter-block boundary continuity, producing visible square 'blocking artifacts'. JPEG 2000 applies the Discrete Wavelet Transform globally across the entire image without block partitioning, resulting in gradual, soft blurring rather than block seams.",
    "uni": true
  },
  {
    "id": 75,
    "unit": "Unit III",
    "chapter": 22,
    "diff": "Easy",
    "topic": "Image Compression, Lossless vs. Lossy Compression",
    "q": "For binary bilevel images containing long horizontal sequences of black and white pixels (such as scanned text and fax transmissions), which compression scheme is most efficient and standard?",
    "options": [
      "Run-Length Encoding (RLE) / CCITT Group 3 & 4",
      "Discrete Cosine Transform (DCT)",
      "Bilinear Interpolation",
      "Histogram Matching"
    ],
    "ans": 0,
    "exp": "Run-Length Encoding (RLE) replaces contiguous sequences of identical pixels with a count pair (e.g. 50 white, 3 black). Combined with modified Huffman tables, it forms the CCITT Group 3 and Group 4 standards used for document scanning and fax transmission.",
    "uni": true
  },
  {
    "id": 76,
    "unit": "Unit IV",
    "chapter": 25,
    "diff": "Easy",
    "topic": "Image Classification and Object Detection",
    "q": "What is the primary conceptual difference between Image Classification and Object Detection?",
    "options": [
      "Classification predicts bounding box coordinates; detection predicts pixel colors",
      "Classification assigns a single categorical label to the whole image; detection localizes and classifies multiple objects with spatial bounding boxes",
      "Classification requires neural networks; detection only uses Sobel filters",
      "Classification works on video; detection works only on static JPEG files"
    ],
    "ans": 1,
    "exp": "Image Classification answers 'what is in this image?' by outputting a single class label. Object Detection answers 'what is where?' by simultaneously predicting categorical labels AND spatial bounding coordinates $(x, y, w, h)$ for every instance in the scene.",
    "uni": true
  },
  {
    "id": 77,
    "unit": "Unit IV",
    "chapter": 26,
    "diff": "Moderate",
    "topic": "Introduction to Convolutional Neural Networks (CNNs)",
    "q": "Which two core structural properties explain why Convolutional Neural Networks (CNNs) outperform Fully Connected (Dense) networks on image data?",
    "options": [
      "Infinite precision weights and zero activation functions",
      "Local receptive fields (spatial locality) and parameter sharing (translation equivariance)",
      "Direct processing of frequency spectra without spatial convolution",
      "Exclusively using 1D vectors of size $10^6$"
    ],
    "ans": 1,
    "exp": "Fully connected networks ignore spatial structure and suffer parameter explosion on high-resolution images. CNNs exploit: 1. Local receptive fields (neurons connect only to local neighborhoods, capturing local correlation); and 2. Parameter sharing (the same kernel slides across the entire image, learning translation-equivariant features with drastically fewer weights).",
    "uni": true
  },
  {
    "id": 78,
    "unit": "Unit IV",
    "chapter": 26,
    "diff": "Moderate",
    "topic": "Introduction to Convolutional Neural Networks (CNNs)",
    "q": "Given an input image of size $32 \\times 32$, a convolution kernel of size $5 \\times 5$, zero-padding $P = 2$, and stride $S = 1$, what is the spatial dimension of the output feature map?",
    "options": [
      "$28 \\times 28$",
      "$30 \\times 30$",
      "$32 \\times 32$",
      "$36 \\times 36$"
    ],
    "ans": 2,
    "exp": "Output size formula: $O = \\lfloor (W - K + 2P)/S \\rfloor + 1 = \\lfloor (32 - 5 + 2(2))/1 \\rfloor + 1 = \\lfloor (32 - 5 + 4)/1 \\rfloor + 1 = 31 + 1 = 32$. This configuration preserves dimensions and is known as 'Same' padding.",
    "uni": true
  },
  {
    "id": 79,
    "unit": "Unit IV",
    "chapter": 26,
    "diff": "Hard",
    "topic": "Introduction to Convolutional Neural Networks (CNNs)",
    "q": "How many trainable parameters (weights + biases) exist in a 2D convolution layer that takes 64 input feature channels and produces 128 output feature channels using $3 \\times 3$ kernels?",
    "options": [
      "8,192 parameters",
      "73,728 parameters",
      "73,856 parameters",
      "1,048,576 parameters"
    ],
    "ans": 2,
    "exp": "Number of weights = $K_h \\times K_w \\times C_{\\text{in}} \\times C_{\\text{out}} = 3 \\times 3 \\times 64 \\times 128 = 73,728$. Adding one bias per output filter ($+128$ biases) gives: $73,728 + 128 = 73,856$ trainable parameters.",
    "uni": true
  },
  {
    "id": 80,
    "unit": "Unit IV",
    "chapter": 26,
    "diff": "Easy",
    "topic": "Introduction to Convolutional Neural Networks (CNNs)",
    "q": "What is the primary function of Max Pooling layers ($2 \\times 2$, stride 2) in standard CNN architectures?",
    "options": [
      "To add Gaussian noise for regularization",
      "To downsample spatial dimensions by 50%, reducing computational cost and conferring small translational invariance",
      "To convert multichannel tensors into scalar outputs",
      "To invert color channels from RGB to BGR"
    ],
    "ans": 1,
    "exp": "Max pooling ($2 \\times 2$ with stride 2) extracts the maximum activation in each non-overlapping quadrant, halving spatial height and width ($H/2, W/2$). This progressively reduces tensor dimensionality, reduces memory footprint, and provides local spatial translation invariance.",
    "uni": true
  },
  {
    "id": 81,
    "unit": "Unit IV",
    "chapter": 27,
    "diff": "Moderate",
    "topic": "Pretrained Models (VGG, ResNet, YOLO)",
    "q": "What architectural innovation did VGG-16 introduce regarding convolutional filter design?",
    "options": [
      "Using dynamic $11 \\times 11$ convolutional kernels with stride 4",
      "Replacing large receptive field filters (such as $7 \\times 7$) with a stack of three factorized $3 \\times 3$ filters, achieving the same effective receptive field with fewer parameters and more non-linearities",
      "Removing all activation functions across the network",
      "Completely eliminating fully connected layers"
    ],
    "ans": 1,
    "exp": "A stack of two $3 \\times 3$ conv layers has an effective receptive field of $5 \\times 5$; a stack of three has a receptive field of $7 \\times 7$. Stacking three $3 \\times 3$ layers uses $3 \\times (3^2 C^2) = 27 C^2$ parameters versus $7^2 C^2 = 49 C^2$ (a 45% parameter reduction) while incorporating three non-linear ReLU activations instead of one.",
    "uni": true
  },
  {
    "id": 82,
    "unit": "Unit IV",
    "chapter": 27,
    "diff": "Hard",
    "topic": "Pretrained Models (VGG, ResNet, YOLO)",
    "q": "How did ResNet (Residual Networks) overcome the vanishing/exploding gradient degradation problem that previously prevented training networks deeper than 20–30 layers?",
    "options": [
      "By using 64-bit floating point hardware exclusively",
      "By introducing identity shortcut (skip) connections $\\mathcal{H}(x) = \\mathcal{F}(x) + x$, allowing gradients to backpropagate directly through the identity pathway $\\frac{\\partial \\mathcal{E}}{\\partial x} = \\frac{\\partial \\mathcal{E}}{\\partial \\mathcal{H}}(1 + \\dots)$",
      "By replacing convolution with Fast Fourier Transforms",
      "By training each layer one at a time with SVMs"
    ],
    "ans": 1,
    "exp": "In plain deep networks, gradients vanish as they backpropagate through dozens of weight multiplications. ResNet reformulates layers to learn a residual mapping $\\mathcal{F}(x) = \\mathcal{H}(x) - x$. The addition of identity shortcut $x$ ensures that $\\frac{\\partial \\mathcal{E}}{\\partial x} = \\frac{\\partial \\mathcal{E}}{\\partial \\mathcal{H}} (1 + \\frac{\\partial \\mathcal{F}}{\\partial x})$, guaranteeing a clear gradient highway back to early layers.",
    "uni": true
  },
  {
    "id": 83,
    "unit": "Unit IV",
    "chapter": 28,
    "diff": "Moderate",
    "topic": "Pretrained Models (VGG, ResNet, YOLO)",
    "q": "Why is YOLO (You Only Look Once) radically faster than two-stage detectors such as Faster R-CNN?",
    "options": [
      "YOLO does not use convolutional neural networks",
      "YOLO frames object detection as a single-pass regression problem directly from full image pixels to bounding box coordinates and class probabilities, avoiding separate region proposal generation",
      "YOLO operates exclusively on binary black-and-white images",
      "YOLO ignores bounding box coordinates and only outputs class labels"
    ],
    "ans": 1,
    "exp": "Two-stage detectors (Faster R-CNN) first generate hundreds of candidate region proposals with an RPN, then crop, warp, and classify each proposal. YOLO processes the entire image in a single neural forward pass, dividing it into a grid and simultaneously regressing bounding boxes and class scores.",
    "uni": true
  },
  {
    "id": 84,
    "unit": "Unit IV",
    "chapter": 28,
    "diff": "Moderate",
    "topic": "Pretrained Models (VGG, ResNet, YOLO)",
    "q": "In object detection evaluation, the Intersection over Union (IoU) metric between ground truth box $A$ and predicted box $B$ is calculated as:",
    "options": [
      "$\\text{IoU} = \\frac{\\text{Area}(A) + \\text{Area}(B)}{2}$",
      "$\\text{IoU} = \\frac{\\text{Area}(A \\cap B)}{\\text{Area}(A \\cup B)}$",
      "$\\text{IoU} = \\frac{\\text{Area}(A)}{\\text{Area}(B)}$",
      "$\\text{IoU} = \\text{Area}(A) - \\text{Area}(B)$"
    ],
    "ans": 1,
    "exp": "IoU (also known as the Jaccard Index) measures overlap accuracy: $\\text{IoU} = \\frac{\\text{Area}(A \\cap B)}{\\text{Area}(A \\cup B)}$. A prediction is typically counted as a True Positive (TP) if $\\text{IoU} \\ge 0.5$ (or $0.75$ in strict benchmarks).",
    "uni": true
  },
  {
    "id": 85,
    "unit": "Unit IV",
    "chapter": 28,
    "diff": "Moderate",
    "topic": "Pretrained Models (VGG, ResNet, YOLO)",
    "q": "What post-processing algorithm is used in object detectors to eliminate redundant, overlapping bounding boxes that predict the same object instance?",
    "options": [
      "Otsu's thresholding",
      "Non-Maximum Suppression (NMS)",
      "Laplacian sharpening",
      "K-Means clustering"
    ],
    "ans": 1,
    "exp": "Non-Maximum Suppression (NMS) sorts all candidate bounding boxes by confidence score, picks the highest-scoring box, and suppresses (deletes) all other overlapping boxes whose IoU with it exceeds a suppression threshold (typically 0.45). The process repeats until no redundant duplicates remain.",
    "uni": true
  },
  {
    "id": 86,
    "unit": "Unit IV",
    "chapter": 29,
    "diff": "Moderate",
    "topic": "Image Denoising using Autoencoders",
    "q": "In an Undercomplete Convolutional Autoencoder, what architectural bottleneck forces the network to learn meaningful semantic features rather than a trivial identity mapping?",
    "options": [
      "The latent bottleneck representation $z$ has a much lower spatial and channel dimensionality than the input image",
      "The network uses zero loss functions",
      "The decoder has no trainable weights",
      "The learning rate is set to zero"
    ],
    "ans": 0,
    "exp": "An undercomplete autoencoder restricts the dimensionality of the latent code $z$ (the bottleneck between encoder and decoder). Because $z$ cannot store all input pixels directly, the network is forced to learn a compact, compressed manifold of the most salient structural features.",
    "uni": true
  },
  {
    "id": 87,
    "unit": "Unit IV",
    "chapter": 29,
    "diff": "Moderate",
    "topic": "Image Denoising using Autoencoders",
    "q": "How is a Denoising Autoencoder (DAE) trained to restore noisy corrupted images?",
    "options": [
      "It is fed clean images and trained to produce white Gaussian noise",
      "It is fed artificially corrupted images $\\tilde{x} = x + \\eta$ as input, but its loss function compares the reconstructed output $\\hat{x}$ against the original CLEAN ground truth image $x$",
      "It uses inverse Fourier filters in the latent layer",
      "It runs Canny edge detection before computing loss"
    ],
    "ans": 1,
    "exp": "A Denoising Autoencoder receives an intentionally corrupted image $\\tilde{x} \\sim q(\\tilde{x} \\mid x)$ as input. Its reconstruction loss (MSE: $\\|g(f(\\tilde{x})) - x\\|^2$) penalizes differences against the pristine, uncorrupted ground-truth image $x$, forcing the network to project corrupted states back onto the manifold of clean images.",
    "uni": true
  },
  {
    "id": 88,
    "unit": "Unit IV",
    "chapter": 30,
    "diff": "Hard",
    "topic": "Introduction to Video Processing and Motion Analysis",
    "q": "The fundamental Optical Flow Constraint Equation $I_x u + I_y v + I_t = 0$ is derived by applying a first-order Taylor expansion to which core physical assumption?",
    "options": [
      "The Constant Velocity Assumption",
      "The Brightness Constancy Assumption: $I(x + u, y + v, t + 1) = I(x, y, t)$",
      "The Nyquist Sampling Assumption",
      "The Zero Noise Assumption"
    ],
    "ans": 1,
    "exp": "The brightness constancy assumption states that the illumination of an object point remains constant over a small time increment $\\Delta t$: $I(x+\\Delta x, y+\\Delta y, t+\\Delta t) = I(x, y, t)$. Expanding in a Taylor series yields $I + I_x \\Delta x + I_y \\Delta y + I_t \\Delta t \\approx I$, which simplifies to $I_x u + I_y v + I_t = 0$.",
    "uni": true
  },
  {
    "id": 89,
    "unit": "Unit IV",
    "chapter": 30,
    "diff": "Hard",
    "topic": "Introduction to Video Processing and Motion Analysis",
    "q": "What is the 'Aperture Problem' in optical flow motion estimation?",
    "options": [
      "Camera lenses cannot focus on objects moving faster than the shutter speed",
      "Viewing a moving linear edge through a small local window only allows measuring the component of velocity perpendicular (normal) to the edge; parallel motion is invisible",
      "Sensors with small apertures produce dark video frames",
      "Optical flow equations produce imaginary complex numbers"
    ],
    "ans": 1,
    "exp": "The aperture problem stems from having 1 equation with 2 velocity unknowns $(u, v)$ at each pixel. When looking through a local aperture at a straight edge, motion parallel to the edge produces zero intensity variation, meaning only the normal velocity component can be determined without corner information.",
    "uni": true
  },
  {
    "id": 90,
    "unit": "Unit IV",
    "chapter": 30,
    "diff": "Hard",
    "topic": "Introduction to Video Processing and Motion Analysis",
    "q": "How does the Lucas-Kanade method solve the underdetermined aperture problem for a local window $W$?",
    "options": [
      "It sets horizontal velocity $u = 0$",
      "It assumes velocity $(u, v)$ is constant across all pixels in window $W$, formulating an overdetermined linear system solved via the Harris structure tensor $A^T A \\vec{v} = -A^T b$",
      "It computes the Discrete Cosine Transform of each video frame",
      "It averages velocities across the entire 10-minute video"
    ],
    "ans": 1,
    "exp": "Lucas-Kanade assumes motion $(u, v)$ is identical across an $n \\times n$ local window (e.g., $5 \\times 5 = 25$ pixels). This gives 25 equations for 2 unknowns: $A \\vec{v} = -b$. The least-squares solution is $\\vec{v} = (A^T A)^{-1} A^T (-b)$, which is reliably invertible whenever $A^T A$ (the Harris structure tensor) has two large eigenvalues (i.e. at corners).",
    "uni": true
  },
  {
    "id": 91,
    "unit": "Unit IV",
    "chapter": 30,
    "diff": "Moderate",
    "topic": "Introduction to Video Processing and Motion Analysis",
    "q": "In automated video surveillance, why is a Gaussian Mixture Model (GMM / MoG2) background subtractor superior to simple frame differencing ($|I_t - I_{t-1}| > T$)?",
    "options": [
      "Frame differencing only detects motion at edges and leaves holes inside uniformly colored moving objects, while GMM maintains multi-modal background models capable of handling waving trees, water ripples, and lighting shifts",
      "Frame differencing cannot run in real time",
      "GMM runs without needing camera calibration",
      "GMM converts video frames to frequency space"
    ],
    "ans": 0,
    "exp": "Frame differencing only detects pixels that change between consecutive frames; when an object stops moving or has uniform color, it disappears from the difference mask. GMM models each pixel's background color distribution as a mixture of $K$ Gaussians, robustly handling repetitive background motions (swaying leaves, monitor flicker) and slow illumination changes.",
    "uni": true
  },
  {
    "id": 92,
    "unit": "Unit IV",
    "chapter": 31,
    "diff": "Moderate",
    "topic": "Applications in Healthcare and Surveillance",
    "q": "In medical Computed Tomography (CT), the Hounsfield Unit (HU) scale is calibrated such that distilled water has a value of ________ HU and air has a value of ________ HU.",
    "options": [
      "$0$ HU; $-1000$ HU",
      "$100$ HU; $0$ HU",
      "$-500$ HU; $+500$ HU",
      "$+1000$ HU; $0$ HU"
    ],
    "ans": 0,
    "exp": "The Hounsfield scale standardizes radiodensity: $\\text{HU} = 1000 \\times \\frac{\\mu - \\mu_{\\text{water}}}{\\mu_{\\text{water}} - \\mu_{\\text{air}}}$. Air has $\\mu \\approx 0$, yielding $-1000\\text{ HU}$; distilled water has $\\text{HU} = 0$; soft tissue ranges from $+20$ to $+70\\text{ HU}$; and dense cortical bone reaches $+1000\\text{ to }+3000\\text{ HU}$.",
    "uni": true
  },
  {
    "id": 93,
    "unit": "Unit IV",
    "chapter": 31,
    "diff": "Moderate",
    "topic": "Applications in Healthcare and Surveillance",
    "q": "What is 'Windowing' (Window Level and Window Width) in diagnostic CT image display?",
    "options": [
      "Cropping the image to a rectangular region of interest",
      "A linear contrast-stretching transformation mapping a selected sub-range of 12-bit/16-bit Hounsfield Units into the 8-bit [0, 255] display range to highlight specific tissues (e.g. lung, bone, brain)",
      "A spatial moving average filter",
      "Applying JPEG compression to DICOM files"
    ],
    "ans": 1,
    "exp": "Because computer screens only display 256 gray levels (8-bit) while CT data spans 4000+ HU, Windowing defines a center Window Level (WL) and Window Width (WW). Any HU value below $\\text{WL} - \\text{WW}/2$ is displayed as black (0), and above as white (255), focusing the full visual dynamic range onto target clinical tissues.",
    "uni": true
  },
  {
    "id": 94,
    "unit": "Unit IV",
    "chapter": 31,
    "diff": "Hard",
    "topic": "Applications in Healthcare and Surveillance",
    "q": "What mathematical transform describes the set of parallel line integrals collected by X-ray detectors around a patient in Computed Tomography, and how is the 2D cross-section reconstructed?",
    "options": [
      "Hough Transform; reconstructed via Hough Voting",
      "Radon Transform; reconstructed via Filtered Backprojection (FBP)",
      "Discrete Wavelet Transform; reconstructed via EBCOT",
      "Laplacian Transform; reconstructed via Otsu thresholding"
    ],
    "ans": 1,
    "exp": "The Radon Transform $R\\{f\\}(p, \\theta) = \\int \\int f(x,y) \\delta(x\\cos\\theta + y\\sin\\theta - p) dx dy$ projects 2D tissue attenuation along lines into a sinogram. By the Projection-Slice Theorem, the cross-sectional slice is reconstructed using Filtered Backprojection (FBP), which filters radial projection frequencies before backprojecting.",
    "uni": true
  },
  {
    "id": 95,
    "unit": "Unit IV",
    "chapter": 31,
    "diff": "Moderate",
    "topic": "Applications in Healthcare and Surveillance",
    "q": "In digital image forensics, Error Level Analysis (ELA) detects manipulated or spliced regions in a JPEG image by:",
    "options": [
      "Counting the number of pixels with value 255",
      "Re-saving the image at a known JPEG quality and computing the absolute pixel difference against the candidate image to identify compression inconsistency",
      "Checking the EXIF camera model tag for typos",
      "Applying a high-boost filter and searching for color saturation"
    ],
    "ans": 1,
    "exp": "Because each JPEG compression step progressively reduces high-frequency variance toward an error equilibrium, splicing an uncompressed element or an image from a different source creates a localized discrepancy in error levels when the image is uniformly re-compressed at a known factor.",
    "uni": true
  },
  {
    "id": 96,
    "unit": "Unit IV",
    "chapter": 25,
    "diff": "Easy",
    "topic": "Image Classification and Object Detection",
    "q": "In a k-Nearest Neighbors (k-NN) image classifier, how does the parameter $k$ affect the decision boundary?",
    "options": [
      "Larger $k$ leads to a more complex, jagged decision boundary and severe overfitting",
      "$k = 1$ produces a flexible, complex decision boundary sensitive to outliers; larger $k$ produces a smoother boundary more robust to noise",
      "$k$ has zero impact on decision boundaries",
      "$k$ specifies the number of color channels in the image"
    ],
    "ans": 1,
    "exp": "When $k = 1$, the decision boundary tightly encloses individual training exemplars, leading to high variance and sensitivity to noisy outliers. As $k$ increases, majority voting over larger neighborhoods averages out local noise, yielding smoother and more generalized decision boundaries.",
    "uni": true
  },
  {
    "id": 97,
    "unit": "Unit IV",
    "chapter": 26,
    "diff": "Moderate",
    "topic": "Introduction to Convolutional Neural Networks (CNNs)",
    "q": "Why is the Rectified Linear Unit (ReLU: $f(x) = \\max(0, x)$) preferred over the Sigmoid function ($\\sigma(x) = \\frac{1}{1 + e^{-x}}$) as the hidden layer activation in modern CNNs?",
    "options": [
      "ReLU produces negative numbers that normalize batch tensors",
      "ReLU is computationally trivial ($\\{0, x\\}$) and maintains a constant derivative of 1 for $x > 0$, avoiding the vanishing gradient saturation suffered by Sigmoid at large inputs",
      "ReLU is completely differentiable at $x = 0$",
      "ReLU limits the output values strictly between 0 and 1"
    ],
    "ans": 1,
    "exp": "Sigmoids saturate at values near 0 and 1 where their derivative approaches 0 ($\\sigma'(x) \\approx 0$). In multi-layer networks, chain-rule multiplication of these fractional derivatives causes gradients to rapidly vanish. ReLU has a non-saturating derivative of 1 for all positive activations, accelerating gradient descent convergence.",
    "uni": true
  },
  {
    "id": 98,
    "unit": "Unit IV",
    "chapter": 27,
    "diff": "Moderate",
    "topic": "Pretrained Models (VGG, ResNet, YOLO)",
    "q": "In transfer learning, when we 'freeze' early convolutional layers and only train the newly added classification head on a small dataset, what is the core rationale?",
    "options": [
      "Early layers contain dataset-specific noise that should not be updated",
      "Early layers have learned generic, universal low-level visual features (edges, color blobs, textures) that transfer across virtually all computer vision domains",
      "Freezing layers reduces the number of classes in the target dataset",
      "The backward pass cannot backpropagate past layer 10"
    ],
    "ans": 1,
    "exp": "Empirical studies in deep vision confirm that early CNN layers act as Gabor-like edge, texture, and color blob filters that are universally applicable to natural images. Freezing these generic features prevents destructive updates on small target datasets and avoids overfitting.",
    "uni": true
  },
  {
    "id": 99,
    "unit": "Unit IV",
    "chapter": 30,
    "diff": "Moderate",
    "topic": "Introduction to Video Processing and Motion Analysis",
    "q": "What distinguishes DENSE optical flow (e.g., Farnebäck method) from SPARSE optical flow (e.g., Lucas-Kanade)?",
    "options": [
      "Dense optical flow computes motion vectors for every single pixel in the frame, while sparse optical flow tracks only a subset of prominent feature points (e.g., corners)",
      "Sparse optical flow works in 3D, while dense works in 2D",
      "Dense optical flow is much faster to compute than sparse",
      "Sparse optical flow requires high-resolution infrared sensors"
    ],
    "ans": 0,
    "exp": "Sparse optical flow (Lucas-Kanade) only computes motion vectors $(u, v)$ for selected high-confidence keypoints (e.g. Harris corners or Shi-Tomasi points). Dense optical flow (Gunnar Farnebäck, Horn-Schunck) computes a vector field across every single pixel coordinate in the frame.",
    "uni": true
  },
  {
    "id": 100,
    "unit": "Unit IV",
    "chapter": 31,
    "diff": "Moderate",
    "topic": "Applications in Healthcare and Surveillance",
    "q": "When deploying facial recognition surveillance systems, what documented computer vision failure mode makes algorithmic bias auditing ethically and technically mandatory?",
    "options": [
      "Cameras cannot capture facial features in daylight",
      "Deep models trained on non-representative datasets show significantly higher false match and false rejection error rates on darker skin tones (Fitzpatrick skin types V and VI) and marginalized demographic groups",
      "Facial recognition algorithms only recognize individuals wearing glasses",
      "Neural networks cannot detect faces when images are stored in PNG format"
    ],
    "ans": 1,
    "exp": "Landmark research (e.g., Buolamwini and Gebru's 'Gender Shades' study and NIST benchmarks) revealed that commercial vision models trained on imbalanced datasets exhibit severe performance disparities across skin types and genders, demonstrating the critical need for representative training data, fairness metrics, and algorithmic accountability.",
    "uni": true
  }
];

if (typeof window !== 'undefined') {
  window.DIP_QUIZ_DATA = DIP_QUIZ_DATA;
}
