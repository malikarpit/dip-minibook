#!/usr/bin/env python3
import os
import re
from syllabus_data import UNITS_INFO, CHAPTERS_MAPPING

DIP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS_DIR = os.path.join(DIP_DIR, 'chapters')

def get_unit_class(unit_id):
    if unit_id == 'unit-1': return 'unit-badge-u1'
    if unit_id == 'unit-2': return 'unit-badge-u2'
    if unit_id == 'unit-3': return 'unit-badge-u3'
    if unit_id == 'unit-4': return 'unit-badge-u4'
    return 'unit-badge-u1'

def update_chapter_file(ch_key, meta):
    file_path = os.path.join(DIP_DIR, meta['file'])
    if not os.path.exists(file_path):
        print(f"Warning: {file_path} not found!")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    unit_cls = get_unit_class(meta['unit_id'])
    unit_badge_html = f'<span class="unit-badge {unit_cls}">🎓 {meta["unit_num"]}</span>'

    # 1. Update Hero Meta if unit badge not present
    if 'unit-badge' not in content:
        # Insert after <div class="hero-meta">
        content = re.sub(
            r'(<div class="hero-meta">\s*)',
            r'\1' + unit_badge_html + '\n          ',
            content,
            count=1
        )

    # 2. Update .syllabus-anchor
    new_syllabus_anchor = f'''<div class="syllabus-anchor">
          <div class="syllabus-anchor-header">
            <span class="syllabus-anchor-label">🎓 DU DSE-3 Syllabus Alignment</span>
            <span class="unit-badge {unit_cls}">{meta["unit_num"]}: {meta["unit_title"]}</span>
          </div>
          <div class="syllabus-topic-name">
            <span class="label">Syllabus Topic</span>
            <span>{meta["topic_title"]}</span>
          </div>
          <div class="syllabus-topic-detail">
            {meta["syllabus_mention"]}
          </div>
        </div>'''

    content = re.sub(
        r'<div class="syllabus-anchor">.*?</div>\s*</div>',
        new_syllabus_anchor + '\n      </div>',
        content,
        flags=re.DOTALL,
        count=1
    )

    # 3. Update sidebar part headers to show Unit association
    content = content.replace(
        '<div class="sidebar-section-label part-label part-i">Part I — The Image</div>',
        '<div class="sidebar-section-label part-label part-i">Unit I · Part I — The Image</div>'
    )
    content = content.replace(
        '<div class="sidebar-section-label part-label part-ii">Part II — Improving the Image</div>',
        '<div class="sidebar-section-label part-label part-ii">Unit II · Part II — Improving the Image</div>'
    )
    content = content.replace(
        '<div class="sidebar-section-label part-label part-iii">Part III — Understanding Content</div>',
        '<div class="sidebar-section-label part-label part-iii">Unit III · Part III — Understanding Content</div>'
    )
    content = content.replace(
        '<div class="sidebar-section-label part-label part-iv">Part IV — Compressing Images</div>',
        '<div class="sidebar-section-label part-label part-iv">Unit III · Part IV — Compressing Images</div>'
    )
    content = content.replace(
        '<div class="sidebar-section-label part-label part-v">Part V — Intelligent Vision</div>',
        '<div class="sidebar-section-label part-label part-v">Unit IV · Part V — Intelligent Vision</div>'
    )

    # 4. Insert exam suite links into sidebar if not already present
    if 'unit-quiz.html' not in content:
        content = content.replace(
            '''        <a href="../progress.html" class="sidebar-link">
          <span class="link-icon">📊</span>
          <span>Study Dashboard</span>
        </a>''',
            '''        <a href="../progress.html" class="sidebar-link">
          <span class="link-icon">📊</span>
          <span>Study Dashboard</span>
        </a>
        <a href="../exams/unit-quiz.html" class="sidebar-link">
          <span class="link-icon">⚡</span>
          <span>100 MCQ Unit Quiz</span>
        </a>
        <a href="../exams/formula-sheet.html" class="sidebar-link">
          <span class="link-icon">📐</span>
          <span>Formula &amp; Revision Deck</span>
        </a>'''
        )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {meta['file']}")

def run():
    for ch_key, meta in CHAPTERS_MAPPING.items():
        update_chapter_file(ch_key, meta)

if __name__ == '__main__':
    run()
