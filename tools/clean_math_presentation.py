import glob
import re
import os

def clean_html_formulas(content, is_root=False):
    asset_prefix = "" if is_root else "../"

    # 1. Update MathJax script tag in <head> to prioritize local file with CDN fallback
    old_script_pattern = r'<script id="MathJax-script"[^>]*src="[^"]*"[^>]*></script>'
    new_script_tag = f'<script id="MathJax-script" async src="{asset_prefix}assets/js/mathjax/tex-mml-chtml.js" onerror="this.onerror=null;this.src=\'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js\';"></script>'
    
    if re.search(old_script_pattern, content):
        content = re.sub(old_script_pattern, new_script_tag, content, count=1)

    # 2. Specific negative transformation fragment (user screenshot)
    p_neg = re.compile(
        r'<p>\s*For an image with:\s*</p>\s*'
        r'<p>\s*\$\$\s*L\s*\$\$\s*</p>\s*'
        r'<p>\s*possible intensity levels, the standard image-negative transformation is:\s*</p>\s*'
        r'<p>\s*\$\$\s*s=\(?L-1\)?-r\s*\$\$\s*</p>\s*'
        r'<p>\s*For an 8-bit image:\s*</p>\s*'
        r'<p>\s*\$\$\s*L=256\s*\$\$\s*</p>\s*'
        r'<p>\s*so:\s*</p>\s*'
        r'<p>\s*\$\$\s*s=255-r\s*\$\$\s*</p>',
        re.IGNORECASE
    )
    def repl_neg(m):
        return (
            '<p>For an image with $L$ possible intensity levels, the standard image-negative transformation is:</p>\n'
            '<div class="math-display">\n'
            '  $$s = (L - 1) - r$$\n'
            '</div>\n'
            '<p>For an 8-bit image (where $L = 256$):</p>\n'
            '<div class="math-display">\n'
            '  $$s = 255 - r$$\n'
            '</div>'
        )
    content = p_neg.sub(repl_neg, content)

    # 3. "For an 8-bit image: $$ L=256 $$ so/therefore: $$ s=... $$"
    p_8bit = re.compile(
        r'<p>\s*For an 8-bit image:\s*</p>\s*'
        r'<p>\s*\$\$\s*L=256\s*\$\$\s*</p>\s*'
        r'<p>\s*(?:so|therefore):\s*</p>\s*'
        r'<p>\s*\$\$\s*([^\$]+?)\s*\$\$\s*</p>',
        re.IGNORECASE
    )
    def repl_8bit(m):
        eq = m.group(1).strip()
        return (
            '<p>For an 8-bit image (where $L = 256$):</p>\n'
            '<div class="math-display">\n'
            f'  $${eq}$$\n'
            '</div>'
        )
    content = p_8bit.sub(repl_8bit, content)

    # 4. Suppose: $$ M1 $$ and: $$ M2 $$ then/Then: $$ M3 $$
    p_chain3 = re.compile(
        r'<p>\s*(Suppose|If):\s*</p>\s*'
        r'<p>\s*\$\$\s*([^\$\n]+?)\s*\$\$\s*</p>\s*'
        r'<p>\s*and:\s*</p>\s*'
        r'<p>\s*\$\$\s*([^\$\n]+?)\s*\$\$\s*</p>\s*'
        r'<p>\s*(?:then|Then|so|So):\s*</p>\s*'
        r'<p>\s*\$\$\s*([^\$\n]+?)\s*\$\$\s*</p>',
        re.IGNORECASE
    )
    def repl_chain3(m):
        lead = m.group(1).capitalize()
        m1 = m.group(2).strip()
        m2 = m.group(3).strip()
        m3 = m.group(4).strip()
        return (
            f'<p>{lead} ${m1}$ and ${m2}$. Then:</p>\n'
            '<div class="math-display">\n'
            f'  $${m3}$$\n'
            '</div>'
        )
    content = p_chain3.sub(repl_chain3, content)

    # 5. Suppose/If: $$ M1 $$ then/Then/so: $$ M2 $$
    p_chain2 = re.compile(
        r'<p>\s*(Suppose|If):\s*</p>\s*'
        r'<p>\s*\$\$\s*([^\$\n]+?)\s*\$\$\s*</p>\s*'
        r'<p>\s*(then|Then|so|So):\s*</p>\s*'
        r'<p>\s*\$\$\s*([^\$\n]+?)\s*\$\$\s*</p>',
        re.IGNORECASE
    )
    def repl_chain2(m):
        lead = m.group(1).capitalize()
        m1 = m.group(2).strip()
        m2 = m.group(4).strip()
        return (
            f'<p>{lead} ${m1}$, then:</p>\n'
            '<div class="math-display">\n'
            f'  $${m2}$$\n'
            '</div>'
        )
    content = p_chain2.sub(repl_chain2, content)

    # 6. Consecutive $$ M1 $$ and $$ \boxed{...} $$
    p_boxed = re.compile(
        r'<p>\s*\$\$\s*([a-zA-Z0-9_\(\)\-\+\*\/\s\.]+?)\s*\$\$\s*</p>\s*'
        r'<p>\s*\$\$\s*(\\boxed\{[^\$\n]+?\})\s*\$\$\s*</p>'
    )
    def repl_boxed(m):
        m1 = m.group(1).strip()
        m2 = m.group(2).strip()
        return (
            '<div class="math-display">\n'
            f'  $${m1} = {m2}$$\n'
            '</div>'
        )
    content = p_boxed.sub(repl_boxed, content)

    # 7. Merge short variables interrupting sentences
    def repl_inline_merge(m):
        p1 = m.group(1).strip()
        math = m.group(2).strip()
        p2 = m.group(3).strip()

        # Math must be short variable/expression, not a complex multiline block
        if len(math) > 28 or any(x in math for x in ['\\sum', '\\int', '\\begin', '\\cases', '\\frac', '\\prod', '\\matrix']):
            return m.group(0)

        # Do not merge if p1 or p2 has html tags inside
        if '<' in p1 or '<' in p2:
            return m.group(0)

        continuation_words = ['and', 'or', 'then', 'where', 'with', 'for', 'to', 'possible', 'therefore', 'so', 'denotes', 'describes', 'which', 'is', 'gives', 'representing', 'representing:']
        p2_words = p2.split()
        p2_first_word = p2_words[0].lower() if p2_words else ''
        p2_is_cont = (p2[0].islower() or p2_first_word in continuation_words)

        if not p2_is_cont:
            return m.group(0)

        # Clean trailing colon if it was mid-sentence
        colon_clean_ends = ['with:', 'is:', 'dimensions:', 'for example:', 'ways:', 'Conceptually:', 'pointwise:', 'local:', 'has:', 'levels:', 'gives:', 'Take:', 'If:']
        for end in colon_clean_ends:
            if p1.lower().endswith(end.lower()):
                p1 = p1[:-1]
                break

        if p1.endswith(':') and p2.startswith('where'):
            p1 = p1[:-1]

        if p2.startswith('where') or p2.startswith('and') or p2.startswith('or') or p2.startswith('which'):
            return f'<p>{p1} ${math}$, {p2}</p>'
        else:
            return f'<p>{p1} ${math}$ {p2}</p>'

    content = re.sub(
        r'<p>([^<\n]+?)</p>\s*<p>\s*\$\$\s*([^\$\n]+?)\s*\$\$\s*</p>\s*<p>([^<\n]+?)</p>',
        repl_inline_merge,
        content
    )

    # 8. Wrap remaining standalone <p>\s*\$\$\s*([^\$]+?)\s*\$\$\s*</p> in <div class="math-display">
    def repl_display_wrap(m):
        math_body = m.group(1).strip()
        return f'<div class="math-display">\n  $${math_body}$$\n</div>'

    content = re.sub(
        r'<p>\s*\$\$\s*([\s\S]*?)\s*\$\$\s*</p>',
        repl_display_wrap,
        content
    )

    return content

if __name__ == '__main__':
    chapters = sorted(glob.glob('chapters/ch*.html'))
    print(f'Processing {len(chapters)} chapters...')
    for ch in chapters:
        with open(ch, 'r', encoding='utf-8') as f:
            content = f.read()
        cleaned = clean_html_formulas(content, is_root=False)
        with open(ch, 'w', encoding='utf-8') as f:
            f.write(cleaned)
    print('All chapters cleaned successfully!')

    # Also clean exams and root pages
    exams = sorted(glob.glob('exams/*.html'))
    for ex in exams:
        with open(ex, 'r', encoding='utf-8') as f:
            content = f.read()
        cleaned = clean_html_formulas(content, is_root=False)
        with open(ex, 'w', encoding='utf-8') as f:
            f.write(cleaned)
    print('Exams cleaned successfully!')

    for root_page in ['index.html', 'progress.html']:
        if os.path.exists(root_page):
            with open(root_page, 'r', encoding='utf-8') as f:
                content = f.read()
            cleaned = clean_html_formulas(content, is_root=True)
            with open(root_page, 'w', encoding='utf-8') as f:
                f.write(cleaned)
    print('Root pages cleaned successfully!')
