#!/usr/bin/env python3
"""
Digital Image Processing (DIP) MiniBook — Master Enrichment & Compilation Suite
Unifies manuscript variants, injects 3-Tier Layer A/B/C visual evidence,
creates comprehensive 2,000+ line chapters matching the AIML standard,
and compiles production-grade HTML for Part I (Chapters 01 - 05).
"""

import os
import re
import sys
import html
import markdown

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES_DIR = os.path.join(BASE_DIR, 'content-sources', 'main')
CHAPTERS_DIR = os.path.join(BASE_DIR, 'chapters')

from build_chapter import CHAPTERS_META

ALL_DIP_PARTS = [
    {
        'part_id': 'part-i', 'part_name': 'Part I — The Image',
        'chapters': [
            (1, 'The Big Picture', 'ch01-big-picture.html'),
            (2, 'Formation & Acquisition', 'ch02-image-formation.html'),
            (3, 'Sampling & Quantization', 'ch03-sampling-quantization.html'),
            (4, 'Pixels, Matrices & Resolution', 'ch04-image-representation.html'),
            (5, 'Colour Models & Formats', 'ch05-colour-models-file-formats.html'),
        ]
    },
    {
        'part_id': 'part-ii', 'part_name': 'Part II — Improving the Image',
        'chapters': [
            (6, 'Point Processing & Intensity', 'ch06-point-processing.html'),
            (7, 'Histograms & Equalization', 'ch07-histograms-equalization.html'),
            (8, 'Spatial Filtering & Convolution', 'ch08-spatial-filtering.html'),
            (9, 'Smoothing & Noise Reduction', 'ch09-smoothing-noise-reduction.html'),
            (10, 'Sharpening & Edge Detection', 'ch10-sharpening-edge-detection.html'),
            (11, 'Geometric Transforms', 'ch11-geometric-transforms.html'),
            (12, 'Fourier Transform & Frequency', 'ch12-fourier-transform.html'),
            (13, 'Frequency-Domain Filtering', 'ch13-frequency-filtering.html'),
            (14, 'Restoration & Deblurring', 'ch14-image-restoration.html'),
        ]
    },
    {
        'part_id': 'part-iii', 'part_name': 'Part III — Understanding Content',
        'chapters': [
            (15, 'Segmentation Fundamentals', 'ch15-segmentation-fundamentals.html'),
            (16, 'Thresholding & Otsu Method', 'ch16-thresholding-otsu.html'),
            (17, 'Region-Based Segmentation', 'ch17-region-segmentation.html'),
            (18, 'Mathematical Morphology', 'ch18-mathematical-morphology.html'),
            (19, 'Image Features & Descriptors', 'ch19-features-descriptors.html'),
            (20, 'SIFT, SURF, ORB & HOG', 'ch20-sift-surf-orb-hog.html'),
        ]
    },
    {
        'part_id': 'part-iv', 'part_name': 'Part IV — Compressing Images',
        'chapters': [
            (21, 'Compression & Entropy', 'ch21-compression-entropy.html'),
            (22, 'Lossless: RLE & Huffman', 'ch22-lossless-coding.html'),
            (23, 'Lossy: DCT & JPEG', 'ch23-lossy-dct-jpeg.html'),
            (24, 'Wavelets & JPEG 2000', 'ch24-wavelets-jpeg2000.html'),
        ]
    },
    {
        'part_id': 'part-v', 'part_name': 'Part V — Intelligent Vision',
        'chapters': [
            (25, 'Image Classification', 'ch25-image-classification.html'),
            (26, 'CNNs for Image Processing', 'ch26-cnns-image-processing.html'),
            (27, 'Modern Vision Architectures', 'ch27-modern-vision-architectures.html'),
            (28, 'Object Detection: YOLO', 'ch28-object-detection-yolo.html'),
            (29, 'Image Denoising Autoencoders', 'ch29-image-denoising-autoencoders.html'),
            (30, 'Video & Motion Analysis', 'ch30-video-motion-analysis.html'),
            (31, 'DIP Applications & Ethics', 'ch31-dip-applications-engineering.html'),
        ]
    }
]

def escape_math_and_blocks(text):
    """Protects MathJax formulas and code blocks from Markdown parser corruption."""
    token_map = {}
    counter = [0]

    def make_token(val):
        t = f"%%DIP_TOKEN_{counter[0]}%%"
        counter[0] += 1
        token_map[t] = val
        return t

    # 1. Protect Mermaid diagrams
    def repl_mermaid(m):
        code = m.group(1).strip()
        rendered = f'<div class="diagram-box"><div class="mermaid">\n{code}\n</div></div>'
        return make_token(rendered)
    text = re.sub(r'```mermaid\s*\n(.*?)\n```', repl_mermaid, text, flags=re.DOTALL)

    # 2. Protect Code blocks
    def repl_code(m):
        lang = m.group(1).strip() if m.group(1) else 'text'
        code = m.group(2)
        escaped_code = html.escape(code)
        rendered = f'''<div class="code-block">
  <div class="code-header">
    <span>{lang}</span>
    <button class="code-copy-btn">📋 Copy</button>
  </div>
  <pre><code>{escaped_code}</code></pre>
</div>'''
        return make_token(rendered)
    text = re.sub(r'```([a-zA-Z0-9_\-\+]*)\s*\n(.*?)\n```', repl_code, text, flags=re.DOTALL)

    # 3. Protect display math $$ ... $$ and \[ ... \]
    def repl_display_math(m):
        return make_token(f"\n$${m.group(1)}$$\n")
    text = re.sub(r'\$\$(.*?)\$\$', repl_display_math, text, flags=re.DOTALL)
    text = re.sub(r'\\\[(.*?)\\\]', repl_display_math, text, flags=re.DOTALL)

    # 4. Protect inline math $ ... $ and \( ... \)
    def repl_inline_math(m):
        content = m.group(1).strip()
        return make_token(f"${content}$")
    text = re.sub(r'(?<!\$)\$([^\$\n]+?)\$(?!\$)', repl_inline_math, text)
    text = re.sub(r'\\\((.*?)\\\)', repl_inline_math, text)

    return text, token_map

def restore_tokens(html_content, token_map):
    for token, val in token_map.items():
        html_content = html_content.replace(token, val)
    return html_content

def post_process_html(html_text):
    def repl_table(m):
        table_code = m.group(0)
        table_code = re.sub(r'<table>', '<table class="comparison-table">', table_code)
        return f'<div class="table-wrap">{table_code}</div>'
    return re.sub(r'<table>.*?</table>', repl_table, html_text, flags=re.DOTALL)

def split_chapter_sections(ch_num, full_md):
    """
    Extracts preamble and distinct top-level sections with strict code-block protection
    and robust title extraction. Never matches comments inside code blocks or level 3+ headers.
    """
    code_tokens = {}
    counter = [0]
    def mask_code(m):
        tok = f"%%CODE_FENCE_{counter[0]}%%"
        counter[0] += 1
        code_tokens[tok] = m.group(0)
        return tok
    masked = re.sub(r'```.*?```', mask_code, full_md, flags=re.DOTALL)

    lines = masked.split('\n')
    header_indices = []

    c_str = str(ch_num)
    extra_keywords = (
        'worked example', 'mathematical proof', 'mathematical derivation',
        'axiomatic', 'comparative', 'topological', 'sift 128', 'resnet',
        'yolo grid', 'denoising autoencoder', 'convolutional mechanics',
        'the complete 31-chapter', 'practical lab', 'bit-plane slicing',
        'pixel topologies', 'mixed (m-)', 'chroma subsampling',
        'comprehensive delhi university', 'numerical problem'
    )

    for idx, line in enumerate(lines):
        line_clean = line.strip()
        if not line_clean.startswith('#'):
            continue
        # Never match level 3+ headers (###)
        if line_clean.startswith('###'):
            continue
        # Ignore Chapter title like # Chapter 01 — Digital Image Processing...
        if re.match(r'^#\s+Chapter\s+\d+', line_clean, re.IGNORECASE):
            continue

        matched_title = None

        if ch_num <= 20:
            m = re.match(r'^(?:#|##)\s+(?:0?' + c_str + r')\.(\d+)\.?\s+(.+)$', line_clean)
            if m:
                matched_title = m.group(2).strip()
        else:
            m = re.match(r'^#{1,2}\s+(\d+)\.\s+([A-Za-z].+)$', line_clean)
            if m:
                # Exclude sub-questions like "## 2-mark questions"
                if not re.match(r'^\d+-mark', m.group(2).strip(), re.IGNORECASE):
                    matched_title = m.group(2).strip()

        if not matched_title:
            # Check for extra keywords in level 1/2 headers
            m_extra = re.match(r'^#{1,2}\s+(?:\d+(?:\.\d+)*\.?\s+)?(.+)$', line_clean)
            if m_extra:
                candidate = m_extra.group(1).strip()
                if any(candidate.lower().startswith(kw) for kw in extra_keywords):
                    matched_title = candidate

        if matched_title:
            header_indices.append((idx, line_clean, matched_title))

    if not header_indices:
        return "", []

    # Preamble is everything before the first section header
    preamble_raw = '\n'.join(lines[:header_indices[0][0]])
    for tok, code in code_tokens.items():
        if tok in preamble_raw:
            preamble_raw = preamble_raw.replace(tok, code)
    preamble = re.sub(r'^---\s*\n.*?\n---\s*\n', '', preamble_raw, flags=re.DOTALL).strip()

    raw_sections = []
    for h_i, (line_idx, orig_line, title) in enumerate(header_indices):
        start_line = line_idx + 1
        end_line = header_indices[h_i + 1][0] if h_i + 1 < len(header_indices) else len(lines)
        sec_body = '\n'.join(lines[start_line:end_line])
        for tok, code in code_tokens.items():
            if tok in sec_body:
                sec_body = sec_body.replace(tok, code)
        raw_sections.append({
            'title': title,
            'body': sec_body.strip()
        })

    return preamble, raw_sections

def build_enriched_chapter(meta, extra_sections_md=""):
    primary_file = os.path.join(SOURCES_DIR, meta['file'])
    with open(primary_file, 'r', encoding='utf-8') as f:
        primary_md = f.read()

    full_md = primary_md
    if extra_sections_md:
        full_md += "\n\n" + extra_sections_md

    preamble, raw_sections = split_chapter_sections(meta['chapter_num'], full_md)
    print(f"[{meta['id']}] Processing {len(raw_sections)} deep sections...")

    # Determine start section number (0 for Ch 01-20 if intro section exists, 1 for Ch 21-31)
    has_zero = any('what this chapter is for' in s['title'].lower() or 'why this chapter' in s['title'].lower() for s in raw_sections[:2])
    first_num = 0 if (meta['chapter_num'] <= 20 and has_zero) else 1

    sections_data = []
    sidebar_links = []
    toc_items = []

    for idx, s in enumerate(raw_sections):
        sec_num_str = f"{meta['chapter_num']:02d}.{idx + first_num}"
        sec_id = f"s-{sec_num_str.replace('.', '-')}"
        sec_title = s['title']
        content_md = s['body']

        # 1. Transform Teacher Notes / Hinglish
        def transform_teacher_hinglish(text):
            parts = re.split(r'(### (?:Hinglish|Teacher explanation — Hinglish|Teacher explanation|Intuition)[^\n]*\n)', text)
            if len(parts) == 1:
                return text
            out = [parts[0]]
            for i in range(1, len(parts), 2):
                hdr = parts[i].replace('###', '').strip()
                block = parts[i+1]
                subparts = re.split(r'(\n(?:###|---|\Z))', block, maxsplit=1)
                t_content = subparts[0].strip()
                rest = ''.join(subparts[1:])
                out.append(f'\n\n<div class="teacher-box"><div class="teacher-title"><span>👨‍🏫</span> {hdr} <span class="hinglish-tag">Teacher Note</span></div>\n\n{t_content}\n\n</div>\n\n{rest}')
            return ''.join(out)
        content_md = transform_teacher_hinglish(content_md)

        # 2. Transform Misconceptions / Traps / Warnings
        def transform_traps(text):
            parts = re.split(r'(### (?:Misconception|Mistake|Pitfall|Warning|Common Trap|Common conceptual trap|Trap \d+)[^\n]*\n)', text, flags=re.IGNORECASE)
            if len(parts) == 1:
                return text
            out = [parts[0]]
            for i in range(1, len(parts), 2):
                hdr = parts[i].replace('###', '').strip()
                block = parts[i+1]
                subparts = re.split(r'(\n(?:###|---|\Z))', block, maxsplit=1)
                m_content = subparts[0].strip()
                rest = ''.join(subparts[1:])
                out.append(f'\n\n<div class="trap-box"><div class="trap-title"><span>⚠️</span> {hdr}</div>\n\n{m_content}\n\n</div>\n\n{rest}')
            return ''.join(out)
        content_md = transform_traps(content_md)

        # 3. Transform Worked Examples
        def transform_worked_examples(text):
            parts = re.split(r'(### (?:Worked Example|Tiny worked example|Step-by-step calculation|Mini Worked Example)[^\n]*\n)', text, flags=re.IGNORECASE)
            if len(parts) == 1:
                return text
            out = [parts[0]]
            for i in range(1, len(parts), 2):
                hdr = parts[i].replace('###', '').strip()
                block = parts[i+1]
                subparts = re.split(r'(\n(?:###|---|\Z))', block, maxsplit=1)
                w_content = subparts[0].strip()
                rest = ''.join(subparts[1:])
                out.append(f'\n\n<div class="worked-example"><div class="worked-example-header"><span class="worked-example-title"><span>🧮</span> {hdr}</span><span class="tag-badge tag-exam">NUMERICAL WORKTHROUGH</span></div>\n\n{w_content}\n\n</div>\n\n{rest}')
            return ''.join(out)
        content_md = transform_worked_examples(content_md)

        # 4. Transform Review Questions / Exam Ladders
        def transform_review_questions(text):
            parts = re.split(r'(### (?:Review questions|\d+-mark question|Self-Assessment|EXAM lens|High-yield conceptual questions)[^\n]*\n)', text, flags=re.IGNORECASE)
            if len(parts) == 1:
                return text
            out = [parts[0]]
            for i in range(1, len(parts), 2):
                hdr = parts[i].replace('###', '').strip()
                block = parts[i+1]
                subparts = re.split(r'(\n(?:###|---|\Z))', block, maxsplit=1)
                q_content = subparts[0].strip()
                rest = ''.join(subparts[1:])
                out.append(f'\n\n<div class="exam-connection"><div class="exam-title"><span>📝</span> {hdr}</div>\n\n{q_content}\n\n</div>\n\n{rest}')
            return ''.join(out)
        content_md = transform_review_questions(content_md)

        # 5. Protect math & blocks
        proc_md, token_map = escape_math_and_blocks(content_md)

        # 6. Convert to HTML
        sec_html = markdown.markdown(proc_md, extensions=['tables', 'fenced_code'])

        # 7. Restore tokens
        sec_html = restore_tokens(sec_html, token_map)
        sec_html = post_process_html(sec_html)

        sections_data.append({
            'num': sec_num_str,
            'id': sec_id,
            'title': sec_title,
            'html': sec_html
        })

        badge = ""
        if sec_num_str in meta.get('uni_sections', []):
            badge = '<span class="tag-badge tag-core" style="font-size:0.65rem; padding:1px 5px;">Uni Core</span>'
        elif sec_num_str in meta.get('gate_sections', []):
            badge = '<span class="tag-badge tag-math" style="font-size:0.65rem; padding:1px 5px;">Analytical</span>'

        sidebar_links.append(
            f'<a href="#{sec_id}" class="sidebar-link"><span class="link-icon">📌</span><span>{sec_num_str} {html.escape(sec_title)}</span> {badge}</a>'
        )

        toc_items.append(
            f'<li class="part-chapter-item"><a href="#{sec_id}"><strong>{sec_num_str}</strong> {html.escape(sec_title)}</a> {badge}</li>'
        )

    # Render Preamble
    preamble_html = ""
    if preamble.strip():
        p_proc, p_tokens = escape_math_and_blocks(preamble)
        p_html = markdown.markdown(p_proc, extensions=['tables', 'fenced_code'])
        p_html = restore_tokens(p_html, p_tokens)
        p_html = post_process_html(p_html)
        preamble_html = f'<div class="concept-hook" style="margin-bottom:var(--em-space-8);">{p_html}</div>'

    sidebar_sections_html = '\n      '.join(sidebar_links)
    toc_items_html = '\n      '.join(toc_items)

    sections_rendered_html = []
    for s in sections_data:
        rendered = f'''
  <!-- SECTION {s['num']}: {html.escape(s['title'])} -->
  <section id="{s['id']}" class="section-block">
    <div class="section-header">
      <span class="section-num">{s['num']}</span>
      <h2>{html.escape(s['title'])}</h2>
      <button class="bookmark-btn" data-id="{s['id']}" title="Bookmark this section" aria-label="Bookmark section">📌</button>
    </div>
    <div class="section-body">
      {s['html']}
    </div>
  </section>'''
        sections_rendered_html.append(rendered)

    all_sections_str = '\n'.join(sections_rendered_html)

    # Master Sidebar Navigation across all 5 Parts (31 chapters)
    master_sidebar_parts = []
    for part in ALL_DIP_PARTS:
        ch_links = []
        for ch_num, ch_title, ch_file in part['chapters']:
            active = ' active' if meta['chapter_num'] == ch_num else ''
            ch_links.append(f'<a href="{ch_file}" class="sidebar-link{active}"><span class="link-icon">{ch_num:02d}</span><span>{ch_title}</span></a>')
        ch_links_str = '\n      '.join(ch_links)
        master_sidebar_parts.append(f'''
    <div class="sidebar-section">
      <div class="sidebar-section-label part-label {part['part_id']}">{part['part_name']}</div>
      {ch_links_str}
    </div>''')
    master_sidebar_parts_str = '\n'.join(master_sidebar_parts)

    page_html = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="author" content="Arpit">
  <meta name="description" content="Chapter {meta['chapter_num']:02d}: {html.escape(meta['title'])} — Digital Image Processing MiniBook. {html.escape(meta['subtitle'])}">
  <title>C{meta['chapter_num']:02d}: {html.escape(meta['title'])} | DIP MiniBook 📷 Arpit</title>

  <link rel="stylesheet" href="../assets/css/main.css">
  <link rel="stylesheet" href="../assets/css/components.css">
  <link rel="stylesheet" href="../assets/css/chapters.css">
  <link rel="stylesheet" href="../assets/css/animations.css">
  <link rel="stylesheet" href="../assets/css/timer.css">

  <script>
    window.MathJax = {{
      tex: {{
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
      }},
      svg: {{ fontCache: 'global' }}
    }};
  </script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body data-chapter-id="{meta['output_file'].replace('.html', '')}">
  <div id="progress-bar"></div>

  <!-- Header -->
  <header id="main-header">
    <div class="header-left">
      <button id="sidebar-toggle" class="icon-btn" aria-label="Toggle navigation drawer" title="Toggle Sidebar (S)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="3" y1="12" x2="21" y2="12"></line>
          <line x1="3" y1="6" x2="21" y2="6"></line>
          <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
      </button>
      <a href="../index.html" class="brand-logo">
        <div class="brand-icon">DIP</div>
        <div class="brand-text">
          <span class="main">Digital Image Processing</span>
          <span class="sub">DU DSE-3 Engineering MiniBook</span>
        </div>
      </a>
    </div>

    <div class="header-chapter-title">C{meta['chapter_num']:02d}: {html.escape(meta['title'])}</div>

    <div class="header-right">
      <button id="reading-mode-btn" class="icon-btn" aria-label="Toggle reading focus mode" title="Focus Mode (F)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
          <line x1="8" y1="21" x2="16" y2="21"></line>
          <line x1="12" y1="17" x2="12" y2="21"></line>
        </svg>
      </button>
      <button id="tts-toggle" class="icon-btn" aria-label="Audio Reader" title="Audio Reader">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
          <path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>
          <path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path>
        </svg>
      </button>
      <button id="theme-toggle" class="icon-btn" aria-label="Cycle theme" title="Theme (T)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
          <circle cx="12" cy="12" r="4.5"></circle>
          <path d="M12 2v2M12 20v2M4.93 4.93l1.42 1.42M17.65 17.65l1.42 1.42M2 12h2M20 12h2M4.93 19.07l1.42-1.42M17.65 6.35l1.42-1.42"></path>
        </svg>
      </button>
    </div>
  </header>

  <!-- Sidebar Overlay -->
  <div id="sidebar-overlay"></div>

  <!-- Sidebar -->
  <aside id="sidebar" aria-expanded="true">
    <div class="sidebar-nav">
      <div class="sidebar-section">
        <div class="sidebar-section-label">General</div>
        <a href="../index.html" class="sidebar-link">
          <span class="link-icon">🏛️</span>
          <span>Subject Portal</span>
        </a>
        <a href="../progress.html" class="sidebar-link">
          <span class="link-icon">📊</span>
          <span>Study Dashboard</span>
        </a>
      </div>

      <div class="sidebar-section">
        <div class="sidebar-section-label">Current Chapter Sections</div>
        {sidebar_sections_html}
      </div>

      {master_sidebar_parts_str}
    </div>

    <div class="sidebar-footer">
      <div class="sidebar-brand-mark">
        <div class="mark">DU</div>
        <div>
          <strong>DSE-3 MiniBook</strong>
          <div>University of Delhi</div>
        </div>
      </div>
    </div>
  </aside>

  <!-- Mandatory Shell Wrapper -->
  <div id="main-content">
    <main class="chapter-content">
      <!-- Chapter Hero -->
      <div class="chapter-hero">
        <div class="hero-meta">
          <span class="part-badge {meta['part_id']}">{meta['part_name']}</span>
          <span class="chapter-number">CHAPTER {meta['chapter_num']:02d}</span>
          <span class="reading-time">⏱️ {meta['read_time']}</span>
          <span class="tag-badge tag-core">{meta['exam_priority']}</span>
        </div>
        <h1 class="chapter-title">{html.escape(meta['title'])}</h1>
        <p class="chapter-subtitle">
          {html.escape(meta['subtitle'])}
        </p>

        <div class="syllabus-anchor">
          <span class="syllabus-anchor-label">DU Syllabus</span>
          <span>{meta['uni_syllabus_text']}</span>
        </div>
      </div>

      <!-- In-Page TOC -->
      <div class="chapter-checklist-card" style="margin-bottom:var(--em-space-8);">
        <div class="checklist-title">
          <span>Table of Contents &amp; Visual Section Map</span>
          <span class="tag-badge tag-math">{len(sections_data)} Deep Sections</span>
        </div>
        <ul class="part-chapters-list">
          {toc_items_html}
        </ul>
      </div>

      {preamble_html}

      <!-- All Numbered Sections -->
      {all_sections_str}

      <!-- Chapter End Package -->
      <section class="chapter-end-package">
        <div class="chapter-nav-grid">
          <a href="{meta['prev_link']}" class="chapter-nav-card">
            <div class="chapter-nav-dir">← Previous</div>
            <div class="chapter-nav-title">{meta['prev_label']}</div>
          </a>
          <a href="{meta['next_link']}" class="chapter-nav-card next">
            <div class="chapter-nav-dir">Next →</div>
            <div class="chapter-nav-title">{meta['next_label']}</div>
          </a>
        </div>
      </section>
    </main>
  </div>

  <!-- FLOATING TTS PANEL (SAFE MANUAL MODE ONLY) -->
  <div id="tts-panel" style="position:fixed; bottom:20px; right:20px; background:var(--em-surface-1); border:1px solid var(--em-border); border-radius:var(--em-radius-md); padding:12px 16px; box-shadow:var(--sh-lg); z-index:var(--z-float); display:none; gap:10px; align-items:center;">
    <button class="icon-btn" id="tts-play" title="Play / Pause" style="background:var(--em-accent); color:#fff; border-radius:50%; width:36px; height:36px;">▶</button>
    <button class="icon-btn" id="tts-stop" title="Stop">⏹</button>
    <div style="font-size:0.75rem; color:var(--em-text-muted);">
      <span id="tts-status">Ready</span> · <span id="tts-rate-label">1.0x</span>
    </div>
  </div>

  <script src="../assets/js/state.js"></script>
  <script src="../assets/js/core.js"></script>
  <script src="../assets/js/tts.js"></script>
  <script src="../assets/js/glossary.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      mermaid.initialize({{
        startOnLoad: true,
        theme: document.documentElement.getAttribute('data-theme') === 'light' ? 'default' : 'dark'
      }});
    }});
  </script>
</body>
</html>
'''

    out_path = os.path.join(CHAPTERS_DIR, meta['output_file'])
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(page_html)

    lines_count = page_html.count('\n')
    size_kb = len(page_html.encode('utf-8')) / 1024
    print(f"Generated {meta['output_file']}: {size_kb:.1f} KB, {lines_count} lines ({len(sections_data)} sections).")
    return out_path

if __name__ == '__main__':
    # 1. Read complementary sections from Ch01-2 and Ch02-2
    ch01_extra = ""
    f01_2 = os.path.join(SOURCES_DIR, 'DIP_Ch01_Digital_Image_Processing_The_Big_Picture-2.md')
    if os.path.exists(f01_2):
        with open(f01_2, 'r', encoding='utf-8') as f:
            c = f.read()
            # Extract sections starting from # 01.10 or complementary
            m = re.search(r'\n# 01\.10\s', c)
            if m:
                ch01_extra = c[m.start():]
                # Re-index extra sections to 01.24 to 01.35
                ch01_extra = re.sub(r'# 01\.(\d+)', lambda match: f"# 01.{int(match.group(1))+15}", ch01_extra)

    ch02_extra = ""
    f02_2 = os.path.join(SOURCES_DIR, 'DIP_Ch02_Image_Formation_and_Acquisition-2.md')
    if os.path.exists(f02_2):
        with open(f02_2, 'r', encoding='utf-8') as f:
            c = f.read()
            m = re.search(r'\n# 02\.16\s', c)
            if m:
                ch02_extra = c[m.start():]
                ch02_extra = re.sub(r'# 02\.(\d+)', lambda match: f"# 02.{int(match.group(1))+15}", ch02_extra)

    print("=== BUILDING ENRICHED DIP CHAPTERS (C01 - C05) ===")
    
    # Chapter 03 Extra Sections
    ch03_extra = """
# 03.39 Mathematical Derivation: 2D Nyquist-Shannon Sampling Theorem
### 2D Impulse Train Representation
In two spatial dimensions, sampling an analog image $f(x,y)$ with periodic intervals $\Delta x$ and $\Delta y$ is mathematically modelled as multiplication by a 2D Dirac comb (sampling lattice):
$$s(x,y) = \sum_{m=-\infty}^{\infty} \sum_{n=-\infty}^{\infty} \delta(x - m\Delta x, y - n\Delta y)$$
The sampled image $f_s(x,y)$ is given by:
$$f_s(x,y) = f(x,y) \cdot s(x,y) = \sum_{m=-\infty}^{\infty} \sum_{n=-\infty}^{\infty} f(m\Delta x, n\Delta y) \, \delta(x - m\Delta x, y - n\Delta y)$$
Applying the 2D Continuous Fourier Transform, multiplication in the spatial domain becomes 2D convolution in the frequency domain:
$$F_s(u,v) = \frac{1}{\Delta x \Delta y} \sum_{m=-\infty}^{\infty} \sum_{n=-\infty}^{\infty} F\left(u - \frac{m}{\Delta x}, v - \frac{n}{\Delta y}\right)$$
This fundamental equation proves that the spectrum of the sampled image consists of infinite periodic replicas of the original spectrum $F(u,v)$ centered at integer multiples of the spatial sampling frequencies $f_{s,x} = \frac{1}{\Delta x}$ and $f_{s,y} = \frac{1}{\Delta y}$.

### The Non-Overlapping Aliasing Condition
To prevent spectral copies from overlapping (aliasing), the replicas must be separated by at least twice the maximum spatial bandwidth frequencies $u_{\max}$ and $v_{\max}$:
$$f_{s,x} \ge 2 u_{\max} \qquad \text{and} \qquad f_{s,y} \ge 2 v_{\max}$$
If sampling falls below this Nyquist rate, overlapping high-frequency tails wrap into the baseband, irreversibly corrupting low-frequency features with false Moiré fringe artifacts.

# 03.40 Worked Example — 10-Mark University Exam Blueprint: Sampling & Storage
### Problem Statement
A medical imaging department acquires digital chest radiographs of size $35 \text{ cm} \times 43 \text{ cm}$. The optical system resolves up to $5 \text{ line pairs per millimetre (lp/mm)}$.
1. Determine the minimum spatial sampling frequency $f_s$ required to prevent spatial aliasing.
2. Calculate the minimum image dimensions $(M \times N)$ in pixels.
3. If each pixel is quantized to 12 bits per pixel (4096 gray levels), compute the uncompressed file size in Megabytes (MB).
4. Explain why 12-bit quantization is preferred over 8-bit quantization in medical radiography.

### Step-by-Step Solution
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">10-MARK UNIVERSITY MODEL ANSWER</span>
  </div>
  <p><strong>1. Minimum Spatial Sampling Frequency:</strong><br>
  Given maximum spatial frequency $f_{\max} = 5 \text{ lp/mm} = 5 \text{ cycles/mm}$.<br>
  By the Nyquist-Shannon Sampling Theorem:
  $$f_s \ge 2 f_{\max} = 2 \times 5 = 10 \text{ samples/mm (pixels/mm)}$$
  The maximum allowable sampling interval is $\Delta x = \Delta y = \frac{1}{f_s} = 0.1 \text{ mm} = 100 \ \mu\text{m}$.</p>

  <p><strong>2. Minimum Image Matrix Dimensions:</strong><br>
  $$\text{Width } M = 35 \text{ cm} \times 10 \text{ mm/cm} \times 10 \text{ pixels/mm} = 3,500 \text{ pixels}$$
  $$\text{Height } N = 43 \text{ cm} \times 10 \text{ mm/cm} \times 10 \text{ pixels/mm} = 4,300 \text{ pixels}$$
  $$\text{Total Pixels } = 3,500 \times 4,300 = 15,050,000 \text{ pixels} \approx 15.05 \text{ Megapixels}$$</p>

  <p><strong>3. Storage Footprint Calculation:</strong><br>
  Total bits $b = M \times N \times k = 15,050,000 \times 12 = 180,600,000 \text{ bits}$.<br>
  $$\text{Total Bytes} = \frac{180,600,000}{8} = 22,575,000 \text{ bytes}$$
  $$\text{Size in Megabytes (MB)} = \frac{22,575,000}{10^6} \approx 22.58 \text{ MB}$$
  $$\text{Size in Mebibytes (MiB)} = \frac{22,575,000}{1024 \times 1024} \approx 21.53 \text{ MiB}$$</p>

  <p><strong>4. Medical Rationale for 12-bit Quantization:</strong><br>
  Human tissue density variation in X-ray imaging (bone, soft tissue, fat, air cavities) exhibits a dynamic range exceeding 1000:1. An 8-bit representation ($L=256$) produces coarse quantization steps that cause <em>false contouring</em> across subtle lung nodules and microcalcifications. A 12-bit representation ($L=4096$) provides 16 times higher intensity resolution, enabling radiologists to perform contrast windowing without clipping diagnostic features.</p>
</div>

# 03.41 Worked Example — Lloyd-Max Optimal Non-Uniform Quantizer Formulation
### Problem Statement
In non-uniform quantization of natural image luminance distributions, uniform interval quantizers waste bits on rarely occurring high intensities while introducing severe quantization noise in dense mid-tone regions.
1. State the **Lloyd-Max Optimal Quantization Conditions** minimizing Mean Squared Quantization Error $\mathcal{E} = \sum_{k=1}^L \int_{t_{k-1}}^{t_k} (r - q_k)^2 p(r) \, dr$.
2. Derive the centroid update condition for output levels $q_k$.
3. Derive the midpoint decision boundary condition for threshold boundaries $t_k$.
4. Explain how false contouring is mitigated using spatial dithering (pseudorandom noise injection).

### Step-by-Step Mathematical Derivation
<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Examination Trace</span>
    <span class="tag-badge tag-exam">LLOYD-MAX MATHEMATICAL PROOF</span>
  </div>
  <p><strong>1. Minimizing Quantization Error:</strong><br>
  Let $p(r)$ be the continuous probability density function of analog intensity $r \in [r_{\min}, r_{\max}]$. We partition the range into $L$ non-overlapping intervals $[t_{k-1}, t_k)$ with representation reconstruction levels $q_k$. The total mean squared quantization distortion is:
  $$\mathcal{E}(t, q) = \sum_{k=1}^L \int_{t_{k-1}}^{t_k} (r - q_k)^2 p(r) \, dr$$</p>

  <p><strong>2. Centroid Condition for Reconstruction Levels $q_k$:</strong><br>
  Differentiating $\mathcal{E}$ with respect to $q_k$ and setting the derivative to zero:
  $$\frac{\partial \mathcal{E}}{\partial q_k} = -2 \int_{t_{k-1}}^{t_k} (r - q_k) p(r) \, dr = 0$$
  $$\int_{t_{k-1}}^{t_k} r p(r) \, dr - q_k \int_{t_{k-1}}^{t_k} p(r) \, dr = 0 \implies \mathbf{q_k = \frac{\int_{t_{k-1}}^{t_k} r p(r) \, dr}{\int_{t_{k-1}}^{t_k} p(r) \, dr}}$$
  <strong>Pedagogical Insight:</strong> Each optimal reconstruction level $q_k$ is the <em>conditional expectation (centroid of probability mass)</em> of input $r$ over the interval $[t_{k-1}, t_k)$.</p>

  <p><strong>3. Boundary Condition for Decision Thresholds $t_k$:</strong><br>
  Using Leibniz's Rule for differentiating an integral with variable limits:
  $$\frac{\partial \mathcal{E}}{\partial t_k} = (t_k - q_k)^2 p(t_k) - (t_k - q_{k+1})^2 p(t_k) = 0$$
  Assuming $p(t_k) \neq 0$:
  $$(t_k - q_k)^2 = (t_k - q_{k+1})^2 \implies t_k - q_k = -(t_k - q_{k+1}) \implies \mathbf{t_k = \frac{q_k + q_{k+1}}{2}}$$
  <strong>Pedagogical Insight:</strong> Each optimal transition boundary $t_k$ is located precisely at the <em>arithmetic midpoint</em> between adjacent reconstruction levels $q_k$ and $q_{k+1}$.</p>

  <p><strong>4. False Contouring Mitigation via Dithering:</strong><br>
  When coarse quantization (e.g. 2 to 4 bits per pixel) is applied to smoothly varying gradients (like a clear sky), discrete step transitions appear as visible bands known as <em>false contours</em>. Spatial dithering injects zero-mean high-frequency pseudorandom noise before quantization ($r' = r + n$). While this slightly increases background noise variance, it breaks up coherent spatial banding into imperceptible high-frequency grain, exploiting the spatial low-pass filtering nature of the Human Visual System.</p>
</div>
"""

    # Chapter 04 Extra Sections
    ch04_extra = """
# 04.41 Pixel Topologies & Spatial Neighbourhoods
### 4-Neighbours, Diagonal Neighbours, and 8-Neighbours
Given a central pixel $p$ at integer matrix coordinates $(x,y)$:
1. **4-Neighbours $N_4(p)$:** The four horizontally and vertically adjacent pixels:
$$N_4(p) = \{(x+1, y), (x-1, y), (x, y+1), (x, y-1)\}$$
2. **Diagonal Neighbours $N_D(p)$:** The four diagonal corner pixels:
$$N_D(p) = \{(x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)\}$$
3. **8-Neighbours $N_8(p)$:** The union of 4-neighbours and diagonal neighbours:
$$N_8(p) = N_4(p) \cup N_D(p)$$

<div class="before-after-card">
  <div class="before-after-header">
    <span class="before-after-title">Visual Evidence: Pixel Neighbourhood Grids</span>
    <span class="tag-badge tag-math">LAYER C EVIDENCE</span>
  </div>
  <div class="before-after-grid">
    <div class="compare-pane">
      <span class="compare-label">4-Neighbourhood $N_4(p)$</span>
      <div class="compare-visual">
        <div class="matrix-grid" style="grid-template-columns: repeat(3, 44px);">
          <div class="matrix-cell">0</div><div class="matrix-cell neighbourhood">(x, y-1)</div><div class="matrix-cell">0</div>
          <div class="matrix-cell neighbourhood">(x-1, y)</div><div class="matrix-cell centre">p(x,y)</div><div class="matrix-cell neighbourhood">(x+1, y)</div>
          <div class="matrix-cell">0</div><div class="matrix-cell neighbourhood">(x, y+1)</div><div class="matrix-cell">0</div>
        </div>
      </div>
    </div>
    <div class="compare-pane">
      <span class="compare-label">8-Neighbourhood $N_8(p)$</span>
      <div class="compare-visual">
        <div class="matrix-grid" style="grid-template-columns: repeat(3, 44px);">
          <div class="matrix-cell neighbourhood">D</div><div class="matrix-cell neighbourhood">N4</div><div class="matrix-cell neighbourhood">D</div>
          <div class="matrix-cell neighbourhood">N4</div><div class="matrix-cell centre">p(x,y)</div><div class="matrix-cell neighbourhood">N4</div>
          <div class="matrix-cell neighbourhood">D</div><div class="matrix-cell neighbourhood">N4</div><div class="matrix-cell neighbourhood">D</div>
        </div>
      </div>
    </div>
  </div>
</div>

# 04.42 Mixed (m-) Connectivity and Resolving Path Ambiguities
### The 8-Connectivity Ambiguity
Two pixels $p$ and $q$ with values from an intensity set $V$ are 8-connected if $q \in N_8(p)$. However, 8-connectivity allows multiple ambiguous diagonal and orthogonal paths between adjacent pixels, causing boundary-tracing algorithms to fail.
### Definition of m-Connectivity
Two pixels $p$ and $q$ with values from $V$ are **$m$-connected (mixed connected)** if:
1. $q \in N_4(p)$, OR
2. $q \in N_D(p)$ AND the intersection set $N_4(p) \cap N_4(q)$ contains **no pixels whose values belong to $V$**.

<div class="worked-example">
  <div class="worked-example-header">
    <span class="worked-example-title">Numerical Example: Resolving Path Ambiguity with m-Connectivity</span>
    <span class="tag-badge tag-exam">UNIVERSITY HIGH-YIELD PROOF</span>
  </div>
  <p>Consider the binary matrix below with intensity set $V = \{1\}$:</p>
  $$\begin{bmatrix}
  0 & 1 & 1 \\
  0 & 1 & 0 \\
  1 & 0 & 0
  \end{bmatrix}$$
  <p>Under 8-connectivity, there exist two competing paths between the top-right $1$ and center $1$: an orthogonal path via $(0,1)$ and a diagonal path. Under $m$-connectivity, the diagonal path between $(0,2)$ and $(1,1)$ is eliminated because their 4-neighbourhood intersection contains $(0,1)$, which is already in $V$. Thus, $m$-connectivity guarantees a <strong>unique single-pixel boundary path</strong>!</p>
</div>
"""

    # Chapter 05 Extra Sections
    ch05_extra = """
# 05.43 Mathematical Derivation: RGB to HSV / HSI Conversion
### Decoupling Chromaticity from Intensity
The RGB colour cube entangles brightness with chromatic information. The HSI model decouples intensity $I$ from chromaticity (Hue $H$ and Saturation $S$).
Given normalized RGB components $r, g, b \in [0, 1]$:
1. **Intensity Component $I$:**
$$I = \frac{R + G + B}{3}$$
2. **Saturation Component $S$:**
$$S = 1 - \frac{3}{R + G + B} \min(R, G, B)$$
3. **Hue Component $H$:**
$$H = \begin{cases}
\theta & \text{if } B \le G \\
360^\circ - \theta & \text{if } B > G
\end{cases}$$
where the angle $\theta$ is derived from vector projection:
$$\theta = \arccos\left( \frac{\frac{1}{2}[(R - G) + (R - B)]}{\sqrt{(R - G)^2 + (R - B)(G - B)}} \right)$$

# 05.44 Chroma Subsampling: YCbCr 4:4:4 vs 4:2:2 vs 4:2:0
### Biological Motivation
Human retinas possess approximately 120 million rod cells (sensitive to luminance/brightness) but only 6 to 7 million cone cells (sensitive to color). Therefore, spatial bandwidth can be safely stripped from color difference channels ($Cb, Cr$) without human perceptual degradation.

<div class="comparison-table-wrap">
  <table class="comparison-table">
    <thead>
      <tr>
        <th>Subsampling Scheme</th>
        <th>Luma Samples (Y)</th>
        <th>Chroma Samples (Cb, Cr)</th>
        <th>Bandwidth Savings</th>
        <th>Standard Application</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>4:4:4</strong></td>
        <td>4 per row</td>
        <td>4 Cb + 4 Cr (Full Resolution)</td>
        <td>0% (Baseline 24 bpp)</td>
        <td>Medical imaging, cinema mastering, high-end CGI.</td>
      </tr>
      <tr>
        <td><strong>4:2:2</strong></td>
        <td>4 per row</td>
        <td>2 Cb + 2 Cr (Horizontal 2:1 reduction)</td>
        <td>33.3% savings (16 bpp)</td>
        <td>Broadcast television (ProRes, DVCPRO-HD).</td>
      </tr>
      <tr>
        <td><strong>4:2:0</strong></td>
        <td>4 per row</td>
        <td>2 Cb + 2 Cr per 2x2 macroblock</td>
        <td>50% savings (12 bpp)</td>
        <td>JPEG images, MPEG video, YouTube, Netflix streaming.</td>
      </tr>
    </tbody>
  </table>
</div>
"""

    print("=== BUILDING FULLY ENRICHED DIP CHAPTERS (C01 - C05) ===")
    
    # Chapter 01
    build_enriched_chapter(CHAPTERS_META[0], extra_sections_md=ch01_extra)
    
    # Chapter 02
    build_enriched_chapter(CHAPTERS_META[1], extra_sections_md=ch02_extra)
    
    # Chapter 03
    build_enriched_chapter(CHAPTERS_META[2], extra_sections_md=ch03_extra)
    
    # Chapter 04
    build_enriched_chapter(CHAPTERS_META[3], extra_sections_md=ch04_extra)
    
    # Chapter 05
    build_enriched_chapter(CHAPTERS_META[4], extra_sections_md=ch05_extra)

    print("=== ALL 5 PART I CHAPTERS FULLY COMPILED ===")


    print("=== ENRICHMENT & COMPILATION COMPLETE ===")
