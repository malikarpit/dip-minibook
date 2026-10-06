/*
 * DIGITAL IMAGE PROCESSING (DIP) MINIBOOK
 * glossary.js — Technical Glossary & Contextual Definitions
 */
'use strict';

const DIPGlossary = (() => {
  const TERMS = {
    'pixel': {
      term: 'Pixel (Picture Element)',
      def: 'The smallest discrete addressable spatial element in a raster digital image, holding numerical intensity or color values.'
    },
    'sampling': {
      term: 'Spatial Sampling',
      def: 'The process of digitizing continuous spatial coordinates (x, y) into a discrete grid of discrete rows and columns.'
    },
    'quantization': {
      term: 'Amplitude Quantization',
      def: 'The mapping of continuous physical luminance measurements into a finite set of discrete integer digital values (gray levels).'
    },
    'dynamic-range': {
      term: 'Dynamic Range',
      def: 'The ratio between the maximum measurable light intensity and the minimum detectable light intensity in an imaging sensor system.'
    },
    'spatial-resolution': {
      term: 'Spatial Resolution',
      def: 'A measure of the smallest discernible spatial detail in an image, typically quantified in line pairs per millimetre (lp/mm) or dots per inch (DPI).'
    },
    'intensity-resolution': {
      term: 'Intensity Resolution (Bit Depth)',
      def: 'The number of discrete intensity levels an image can represent, determined by bit depth k as L = 2^k levels (e.g., 8-bit = 256 levels).'
    },
    'nyquist-theorem': {
      term: 'Nyquist-Shannon Sampling Theorem',
      def: 'States that to reconstruct a continuous signal without spatial aliasing, the spatial sampling frequency fs must be at least twice the maximum spatial frequency fmax (fs >= 2*fmax).'
    },
    'aliasing': {
      term: 'Spatial Aliasing',
      def: 'A phenomenon occurring when an image is sampled below the Nyquist rate, causing high-frequency scene details to impersonate low-frequency artifacts such as Moiré patterns.'
    },
    'psf': {
      term: 'Point Spread Function (PSF)',
      def: 'The impulse response of an optical or digital imaging system to a point source of light, characterizing blurring introduced by lenses and apertures.'
    },
    'convolution': {
      term: '2D Spatial Convolution',
      def: 'A mathematical filtering operation that slides a flipped kernel across an image, computing weighted sums of neighbourhood pixels to produce a transformed output pixel.'
    },
    'kernel': {
      term: 'Filter Kernel / Mask',
      def: 'A small 2D matrix of numerical coefficients (weights) applied across local pixel neighbourhoods during spatial filtering operations.'
    },
    'histogram': {
      term: 'Intensity Histogram',
      def: 'A discrete frequency distribution plot showing the number of pixels in an image occurring at each available intensity level r_k.'
    },
    'histogram-equalization': {
      term: 'Histogram Equalization',
      def: 'A nonlinear point transformation using the Cumulative Distribution Function (CDF) to redistribute pixel intensities uniformly across the dynamic range, maximizing global contrast.'
    },
    'hsv': {
      term: 'HSV / HSB Colour Model',
      def: 'A cylindrical colour representation that separates chromatic information into Hue (dominant wavelength) and Saturation (purity) from achromatic Value (brightness).'
    },
    'ycbcr': {
      term: 'YCbCr Colour Model',
      def: 'A digital video colour space separating luminance (Y) from blue-difference (Cb) and red-difference (Cr) chroma channels, enabling perceptual chroma subsampling.'
    },
    'connectivity': {
      term: 'Pixel Connectivity (4-, 8-, m-)',
      def: 'Topological rules defining when two adjacent pixels with values from a given set V form a connected path. Mixed (m-) connectivity eliminates topological ambiguities.'
    }
  };

  function init() {
    document.querySelectorAll('[data-term]').forEach(el => {
      const key = el.dataset.term.toLowerCase();
      const entry = TERMS[key];
      if (!entry) return;

      el.classList.add('glossary-term');
      el.title = `${entry.term}: ${entry.def}`;
    });
  }

  return { init, get: (k) => TERMS[k] };
})();

document.addEventListener('DOMContentLoaded', DIPGlossary.init);
