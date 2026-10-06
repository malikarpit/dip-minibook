#!/usr/bin/env python3
import os
from syllabus_data import UNITS_INFO, CHAPTERS_MAPPING

DIP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def generate_index_html():
    index_file = os.path.join(DIP_DIR, 'index.html')
    
    # Read head and sidebar up to main content
    with open(index_file, 'r', encoding='utf-8') as f:
        orig = f.read()
    
    head_and_sidebar = orig.split('<div class="section-header">')[0]
    
    # Build 4 Units Grid (Syllabus Order)
    syllabus_cards_html = []
    for u_id, u_info in UNITS_INFO.items():
        ch_items_html = []
        u_cls = "unit-badge-u1" if u_id == "unit-1" else "unit-badge-u2" if u_id == "unit-2" else "unit-badge-u3" if u_id == "unit-3" else "unit-badge-u4"
        card_cls = "part-i" if u_id == "unit-1" else "part-ii" if u_id == "unit-2" else "part-iii" if u_id == "unit-3" else "part-iv"
        
        for ch_key in u_info['chapters_syllabus_order']:
            ch = CHAPTERS_MAPPING[ch_key]
            tag_type = "CORE" if ch['num'] in [1, 6, 12, 15, 20, 23, 26, 31] else "MATH" if ch['num'] in [2, 3, 7, 9, 10, 13, 14, 16, 18, 19, 21, 24, 25, 29] else "LAB" if ch['num'] in [5, 30] else "ALGO"
            ch_items_html.append(f'''              <li class="part-chapter-item" data-chapter="{ch['id']}" data-unit="{ch['unit_id']}" data-search="{ch['num_str']} {ch['title'].lower()} {ch['topic_title'].lower()} {ch['unit_num'].lower()}">
                <div class="part-chapter-top">
                  <a href="{ch['file']}"><strong>{ch['num_str']}.</strong> {ch['title']}</a>
                  <span class="ch-tag">{tag_type} · READY</span>
                </div>
                <div class="part-chapter-bottom">
                  <span class="syllabus-topic-pill">🎓 Topic: {ch['topic_title']}</span>
                </div>
              </li>''')
            
        first_ch_file = CHAPTERS_MAPPING[u_info['chapters_syllabus_order'][0]]['file']
        syllabus_cards_html.append(f'''        <!-- {u_info['num']} -->
        <div class="part-card {card_cls} unit-card-item" id="{u_id}" data-unit="{u_id}">
          <div>
            <div class="part-card-header">
              <span class="unit-badge {u_cls}">🎓 {u_info['num']} · Syllabus Order</span>
              <span class="tag-badge tag-core">{len(u_info['chapters_syllabus_order'])} Chapters</span>
            </div>
            <h3 class="part-card-title">{u_info['num']} — {u_info['title']}</h3>
            <p class="part-card-desc">
              <strong>Syllabus Scope:</strong> {u_info['syllabus_line']}
            </p>
            <ul class="part-chapters-list">
{chr(10).join(ch_items_html)}
            </ul>
          </div>
          <a href="{first_ch_file}" class="portal-btn portal-btn-secondary" style="width: 100%; justify-content: center;">
            Start {u_info['num']} →
          </a>
        </div>''')

    # Build 5 Parts Grid (Book Order)
    parts_data = [
        ('part-1', 'part-i', 'Part I · Active', 'Part I — The Image', 'Foundational photon physics, illumination-reflectance models, 2D sampling lattice, Shannon-Nyquist theorems, amplitude quantization, and spatial coordinate conventions.', ['ch01', 'ch02', 'ch03', 'ch04', 'ch05']),
        ('part-2', 'part-ii', 'Part II · Active', 'Part II — Improving the Image', 'Point transformations, histogram equalization, spatial convolution, linear/nonlinear smoothing, Laplacian/Sobel edge detection, 2D Fourier transforms, and restoration deblurring.', ['ch06', 'ch07', 'ch08', 'ch09', 'ch10', 'ch11', 'ch12', 'ch13', 'ch14']),
        ('part-3', 'part-iii', 'Part III · Active', 'Part III — Understanding Image Content', 'Segmentation fundamentals, Otsu global thresholding, split-and-merge region growing, binary morphology (erosion/dilation), texture descriptors, and SIFT/SURF/HOG detectors.', ['ch15', 'ch16', 'ch17', 'ch18', 'ch19', 'ch20']),
        ('part-4', 'part-iv', 'Part IV · Active', 'Part IV — Compressing Images', 'Information entropy, Run-Length Encoding, Huffman variable-length coding, Discrete Cosine Transform (DCT), JPEG pipeline quantization, and multiresolution wavelet compression.', ['ch21', 'ch22', 'ch23', 'ch24']),
        ('part-5', 'part-v', 'Part V · Active', 'Part V — Intelligent Vision', 'Classical image classification, convolutional neural networks (CNNs), VGG/ResNet deep architectures, YOLO real-time object detection, denoising autoencoders, video optical flow, and responsible AI.', ['ch25', 'ch26', 'ch27', 'ch28', 'ch29', 'ch30', 'ch31'])
    ]

    parts_cards_html = []
    for pid, pcls, pbadge, ptitle, pdesc, ch_keys in parts_data:
        ch_items_html = []
        for ch_key in ch_keys:
            ch = CHAPTERS_MAPPING[ch_key]
            tag_type = "CORE" if ch['num'] in [1, 6, 12, 15, 20, 23, 26, 31] else "MATH" if ch['num'] in [2, 3, 7, 9, 10, 13, 14, 16, 18, 19, 21, 24, 25, 29] else "LAB" if ch['num'] in [5, 30] else "ALGO"
            u_cls = "unit-badge-u1" if ch['unit_id'] == "unit-1" else "unit-badge-u2" if ch['unit_id'] == "unit-2" else "unit-badge-u3" if ch['unit_id'] == "unit-3" else "unit-badge-u4"
            ch_items_html.append(f'''              <li class="part-chapter-item" data-chapter="{ch['id']}" data-unit="{ch['unit_id']}" data-search="{ch['num_str']} {ch['title'].lower()} {ch['topic_title'].lower()} {ch['unit_num'].lower()}">
                <div class="part-chapter-top">
                  <a href="{ch['file']}"><strong>{ch['num_str']}.</strong> {ch['title']}</a>
                  <span class="ch-tag">{tag_type} · READY</span>
                </div>
                <div class="part-chapter-bottom">
                  <span class="unit-badge {u_cls}" style="font-size:0.68rem; padding:1px 6px;">{ch['unit_num']}</span>
                  <span class="syllabus-topic-pill" style="font-size:0.72rem;">🎓 {ch['topic_title']}</span>
                </div>
              </li>''')
            
        first_ch_file = CHAPTERS_MAPPING[ch_keys[0]]['file']
        parts_cards_html.append(f'''        <!-- {ptitle} -->
        <div class="part-card {pcls} part-card-item" id="{pid}">
          <div>
            <div class="part-card-header">
              <span class="part-badge">{pbadge}</span>
              <span class="tag-badge tag-core">{len(ch_keys)} Chapters</span>
            </div>
            <h3 class="part-card-title">{ptitle}</h3>
            <p class="part-card-desc">
              {pdesc}
            </p>
            <ul class="part-chapters-list">
{chr(10).join(ch_items_html)}
            </ul>
          </div>
          <a href="{first_ch_file}" class="portal-btn portal-btn-secondary" style="width: 100%; justify-content: center;">
            Explore {ptitle.split('—')[0].strip()} →
          </a>
        </div>''')

    new_section_html = f'''      <!-- Curriculum Overview -->
      <div class="section-header">
        <span class="section-num">MAP</span>
        <h2>Curriculum Explorer &amp; Master Syllabus Map</h2>
      </div>

      <!-- Syllabus & Order Filter Control Hub -->
      <div class="syllabus-filter-wrapper">
        <div class="filter-row-top">
          <div>
            <div style="font-size: 0.74rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--em-accent-text); margin-bottom: 6px;">Curriculum Arrangement</div>
            <div class="view-mode-toggle" id="view-mode-toggle">
              <button class="view-mode-btn active" id="btn-view-syllabus" data-mode="syllabus" title="Arrange chapters in the exact 4-Unit sequence of the university syllabus">
                <span>📋</span> University Syllabus Order (4 Units)
              </button>
              <button class="view-mode-btn" id="btn-view-parts" data-mode="parts" title="Arrange chapters by book parts (Chapters 01 to 31)">
                <span>📚</span> Book Architecture (5 Parts)
              </button>
            </div>
          </div>

          <div class="search-filter-box">
            <span class="search-filter-icon">🔍</span>
            <input type="text" id="topic-search-input" class="search-filter-input" placeholder="Search syllabus topics (e.g. Otsu, SIFT, JPEG, Autoencoders, CNNs, YUV)..." autocomplete="off">
          </div>
        </div>

        <div class="filter-row-bottom">
          <div class="unit-filter-pills" id="unit-filter-pills">
            <span style="font-size: 0.76rem; font-weight: 700; color: var(--em-text-muted); margin-right: 4px;">FILTER BY UNIT:</span>
            <button class="unit-pill-btn active" data-unit="all">All Units (31 Chapters)</button>
            <button class="unit-pill-btn" data-unit="unit-1">Unit I: Introduction (5)</button>
            <button class="unit-pill-btn" data-unit="unit-2">Unit II: Enhancement &amp; Restoration (9)</button>
            <button class="unit-pill-btn" data-unit="unit-3">Unit III: Analysis &amp; Compression (10)</button>
            <button class="unit-pill-btn" data-unit="unit-4">Unit IV: Advanced Topics (7)</button>
          </div>
        </div>
      </div>

      <!-- 1. SYLLABUS ORDER CONTAINER (Default: Arranged in exact 4-Unit Syllabus Order) -->
      <div id="view-syllabus-container" class="parts-grid">
{chr(10).join(syllabus_cards_html)}
      </div>

      <!-- 2. BOOK PARTS CONTAINER (Toggleable: Arranged by 5 Book Parts) -->
      <div id="view-parts-container" class="parts-grid" style="display: none;">
{chr(10).join(parts_cards_html)}
      </div>
    </main>
  </div>

  <script src="assets/js/state.js"></script>
  <script src="assets/js/core.js"></script>
  <script src="assets/js/tts.js"></script>
  <script>
    // Dual-View and Syllabus Unit Filter Engine
    document.addEventListener('DOMContentLoaded', () => {{
      const btnViewSyllabus = document.getElementById('btn-view-syllabus');
      const btnViewParts = document.getElementById('btn-view-parts');
      const syllabusContainer = document.getElementById('view-syllabus-container');
      const partsContainer = document.getElementById('view-parts-container');
      const unitPills = document.querySelectorAll('.unit-pill-btn');
      const searchInput = document.getElementById('topic-search-input');

      let currentMode = localStorage.getItem('dip_curriculum_view') || 'syllabus';
      let currentUnitFilter = 'all';
      let searchQuery = '';

      function setViewMode(mode) {{
        currentMode = mode;
        localStorage.setItem('dip_curriculum_view', mode);
        if (mode === 'syllabus') {{
          btnViewSyllabus.classList.add('active');
          btnViewParts.classList.remove('active');
          syllabusContainer.style.display = 'grid';
          partsContainer.style.display = 'none';
        }} else {{
          btnViewParts.classList.add('active');
          btnViewSyllabus.classList.remove('active');
          partsContainer.style.display = 'grid';
          syllabusContainer.style.display = 'none';
        }}
        applyFilters();
      }}

      function applyFilters() {{
        const activeContainer = currentMode === 'syllabus' ? syllabusContainer : partsContainer;
        const allCards = activeContainer.querySelectorAll('.part-card');

        allCards.forEach(card => {{
          const cardUnit = card.getAttribute('data-unit');
          const chapterItems = card.querySelectorAll('.part-chapter-item');
          let visibleChaptersInCard = 0;

          chapterItems.forEach(item => {{
            const itemUnit = item.getAttribute('data-unit');
            const searchData = item.getAttribute('data-search') || '';
            const matchesUnit = (currentUnitFilter === 'all') || (itemUnit === currentUnitFilter);
            const matchesQuery = (!searchQuery) || searchData.includes(searchQuery);

            if (matchesUnit && matchesQuery) {{
              item.style.display = 'flex';
              visibleChaptersInCard++;
            }} else {{
              item.style.display = 'none';
            }}
          }});

          // In syllabus mode, card matches unit directly
          if (currentMode === 'syllabus') {{
            if ((currentUnitFilter === 'all' || cardUnit === currentUnitFilter) && visibleChaptersInCard > 0) {{
              card.style.display = 'flex';
            }} else {{
              card.style.display = 'none';
            }}
          }} else {{
            // In parts mode, hide card if 0 visible chapters
            if (visibleChaptersInCard > 0) {{
              card.style.display = 'flex';
            }} else {{
              card.style.display = 'none';
            }}
          }}
        }});
      }}

      btnViewSyllabus.addEventListener('click', () => setViewMode('syllabus'));
      btnViewParts.addEventListener('click', () => setViewMode('parts'));

      unitPills.forEach(pill => {{
        pill.addEventListener('click', () => {{
          unitPills.forEach(p => p.classList.remove('active'));
          pill.classList.add('active');
          currentUnitFilter = pill.getAttribute('data-unit');
          applyFilters();
        }});
      }});

      if (searchInput) {{
        searchInput.addEventListener('input', (e) => {{
          searchQuery = e.target.value.toLowerCase().trim();
          applyFilters();
        }});
      }}

      // Initialize
      setViewMode(currentMode);
    }});
  </script>
</body>
</html>
'''

    final_content = head_and_sidebar + new_section_html
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("Successfully regenerated index.html with interactive Syllabus & Parts dual-view filter!")

def generate_progress_html():
    progress_file = os.path.join(DIP_DIR, 'progress.html')
    with open(progress_file, 'r', encoding='utf-8') as f:
        orig = f.read()

    # Split before stats grid or dashboard-header
    header_and_stats = orig.split('<!-- Part I Checklist -->')[0]

    # Build syllabus view checklist tables
    syllabus_tables_html = []
    for u_id, u_info in UNITS_INFO.items():
        u_cls = "unit-badge-u1" if u_id == "unit-1" else "unit-badge-u2" if u_id == "unit-2" else "unit-badge-u3" if u_id == "unit-3" else "unit-badge-u4"
        syllabus_tables_html.append(f'''      <!-- {u_info['num']} Checklist -->
      <div class="chapter-checklist-card unit-check-card" data-unit="{u_id}" style="margin-bottom: var(--em-space-6);">
        <div class="checklist-title">
          <div style="display:flex; align-items:center; gap:8px;">
            <span class="unit-badge {u_cls}">🎓 {u_info['num']}</span>
            <span>{u_info['title']}</span>
          </div>
          <span class="tag-badge tag-core" id="badge-{u_id}-status">{len(u_info['chapters_syllabus_order'])} Chapters Ready</span>
        </div>
        <div style="padding: 10px 18px; font-size: 0.84rem; color: var(--em-text-secondary); background: var(--em-surface-2); border-bottom: 1px solid var(--em-border);">
          <strong>Syllabus Scope:</strong> {u_info['syllabus_line']}
        </div>
        <div class="table-wrap">
          <table class="checklist-table">
            <thead>
              <tr>
                <th style="width: 70px;">Chapter</th>
                <th style="min-width: 220px;">Chapter Title</th>
                <th style="min-width: 260px;">Syllabus Topic Alignment</th>
                <th style="width: 120px;">Progress</th>
                <th style="width: 95px;">Status</th>
                <th style="width: 80px;">Action</th>
              </tr>
            </thead>
            <tbody id="{u_id}-table-body">
              <!-- Rendered via JS -->
            </tbody>
          </table>
        </div>
      </div>''')

    # Build parts view checklist tables
    parts_data = [
        ('part1', 'Part I: The Image', 5),
        ('part2', 'Part II: Improving the Image', 9),
        ('part3', 'Part III: Understanding Content', 6),
        ('part4', 'Part IV: Compressing Images', 4),
        ('part5', 'Part V: Intelligent Vision', 7)
    ]
    parts_tables_html = []
    for pid, ptitle, pcount in parts_data:
        parts_tables_html.append(f'''      <!-- {ptitle} Checklist -->
      <div class="chapter-checklist-card" style="margin-bottom: var(--em-space-6);">
        <div class="checklist-title">
          <span>{ptitle} — Chapter Completion Tracker</span>
          <span class="tag-badge tag-core" id="badge-{pid}-status">{pcount} Chapters Ready</span>
        </div>
        <div class="table-wrap">
          <table class="checklist-table">
            <thead>
              <tr>
                <th style="width: 70px;">Chapter</th>
                <th style="min-width: 220px;">Title</th>
                <th style="min-width: 260px;">Syllabus Topic</th>
                <th style="width: 120px;">Progress</th>
                <th style="width: 95px;">Status</th>
                <th style="width: 80px;">Action</th>
              </tr>
            </thead>
            <tbody id="{pid}-table-body">
              <!-- Rendered via JS -->
            </tbody>
          </table>
        </div>
      </div>''')

    new_content = header_and_stats + f'''      <!-- Syllabus & Order Filter Control Hub for Dashboard -->
      <div class="syllabus-filter-wrapper">
        <div class="filter-row-top">
          <div>
            <div style="font-size: 0.74rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--em-accent-text); margin-bottom: 6px;">Curriculum Arrangement</div>
            <div class="view-mode-toggle" id="view-mode-toggle">
              <button class="view-mode-btn active" id="btn-view-syllabus" data-mode="syllabus">
                <span>📋</span> University Syllabus Order (4 Units)
              </button>
              <button class="view-mode-btn" id="btn-view-parts" data-mode="parts">
                <span>📚</span> Book Architecture (5 Parts)
              </button>
            </div>
          </div>
          <div class="unit-filter-pills" id="unit-filter-pills">
            <span style="font-size: 0.76rem; font-weight: 700; color: var(--em-text-muted); margin-right: 4px;">FILTER:</span>
            <button class="unit-pill-btn active" data-unit="all">All Units (31)</button>
            <button class="unit-pill-btn" data-unit="unit-1">Unit I (5)</button>
            <button class="unit-pill-btn" data-unit="unit-2">Unit II (9)</button>
            <button class="unit-pill-btn" data-unit="unit-3">Unit III (10)</button>
            <button class="unit-pill-btn" data-unit="unit-4">Unit IV (7)</button>
          </div>
        </div>
      </div>

      <!-- Syllabus View Container -->
      <div id="view-syllabus-container">
{chr(10).join(syllabus_tables_html)}
      </div>

      <!-- Parts View Container -->
      <div id="view-parts-container" style="display: none;">
{chr(10).join(parts_tables_html)}
      </div>

      <!-- Data Export / Import Actions -->
      <div class="dash-actions-row">
        <button id="btn-export-data" class="btn-outline">
          <span>💾</span> Export Study Backup (JSON)
        </button>
        <button id="btn-import-data" class="btn-outline">
          <span>📥</span> Import Study Backup
        </button>
        <button id="btn-reset-data" class="btn-outline" style="color: var(--danger); border-color: rgba(220, 38, 38, 0.3);">
          <span>⚠️</span> Reset Progress
        </button>
        <input type="file" id="file-import" accept=".json" style="display: none;">
      </div>
    </main>
  </div>

  <script src="assets/js/state.js"></script>
  <script src="assets/js/core.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      const CHAPTERS_ALL = {list(CHAPTERS_MAPPING.values())};
      
      const btnViewSyllabus = document.getElementById('btn-view-syllabus');
      const btnViewParts = document.getElementById('btn-view-parts');
      const syllabusContainer = document.getElementById('view-syllabus-container');
      const partsContainer = document.getElementById('view-parts-container');
      const unitPills = document.querySelectorAll('.unit-pill-btn');

      let currentMode = localStorage.getItem('dip_curriculum_view') || 'syllabus';
      let currentUnit = 'all';

      function renderTable(chapters, tbodyId) {{
        const tbody = document.getElementById(tbodyId);
        if (!tbody) return {{ read: 0, pctSum: 0 }};
        tbody.innerHTML = '';

        let readCount = 0;
        let pctSum = 0;

        chapters.forEach(ch => {{
          const pct = StateManager.getReadProgress(ch.id);
          pctSum += pct;
          const isDone = pct >= 90;
          if (isDone) readCount++;

          const uCls = ch.unit_id === 'unit-1' ? 'unit-badge-u1' : ch.unit_id === 'unit-2' ? 'unit-badge-u2' : ch.unit_id === 'unit-3' ? 'unit-badge-u3' : 'unit-badge-u4';

          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td><strong style="font-family: var(--font-mono); color: var(--em-accent-text);">C${{ch.num_str}}</strong></td>
            <td>
              <strong style="color: var(--em-text); display:block;">${{ch.title}}</strong>
              <span class="unit-badge ${{uCls}}" style="font-size:0.68rem; padding:1px 6px; margin-top:3px;">${{ch.unit_num}}</span>
            </td>
            <td>
              <span class="syllabus-topic-pill" style="font-size:0.75rem;">🎓 ${{ch.topic_title}}</span>
            </td>
            <td>
              <div style="background: var(--em-surface-2); border-radius: 4px; height: 8px; width: 100%; overflow: hidden;">
                <div style="background: var(--em-accent); height: 100%; width: ${{pct}}%;"></div>
              </div>
              <span style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--em-text-muted);">${{pct}}%</span>
            </td>
            <td>
              <span class="tag-badge ${{isDone ? 'tag-lab' : 'tag-core'}}">${{isDone ? 'COMPLETED' : pct > 0 ? 'READING' : 'NOT STARTED'}}</span>
            </td>
            <td>
              <a href="${{ch.file}}" class="btn-outline" style="padding: 4px 10px; font-size: 0.78rem;">Open →</a>
            </td>
          `;
          tbody.appendChild(tr);
        }});

        return {{ read: readCount, pctSum: pctSum }};
      }}

      function renderDashboard() {{
        // Syllabus tables
        const u1Chapters = ['ch01', 'ch02', 'ch03', 'ch04', 'ch05'].map(k => CHAPTERS_ALL.find(c => c.id === k));
        const u2Chapters = ['ch06', 'ch07', 'ch08', 'ch09', 'ch10', 'ch11', 'ch12', 'ch13', 'ch14'].map(k => CHAPTERS_ALL.find(c => c.id === k));
        const u3Chapters = ['ch15', 'ch16', 'ch17', 'ch18', 'ch19', 'ch20', 'ch21', 'ch22', 'ch23', 'ch24'].map(k => CHAPTERS_ALL.find(c => c.id === k));
        // Unit IV in exact syllabus order: 25, 26, 27, 28, 29, 31, 30
        const u4Chapters = ['ch25', 'ch26', 'ch27', 'ch28', 'ch29', 'ch31', 'ch30'].map(k => CHAPTERS_ALL.find(c => c.id === k));

        renderTable(u1Chapters, 'unit-1-table-body');
        renderTable(u2Chapters, 'unit-2-table-body');
        renderTable(u3Chapters, 'unit-3-table-body');
        renderTable(u4Chapters, 'unit-4-table-body');

        // Parts tables
        const p1Chapters = CHAPTERS_ALL.filter(c => c.part_id === 'part-i');
        const p2Chapters = CHAPTERS_ALL.filter(c => c.part_id === 'part-ii');
        const p3Chapters = CHAPTERS_ALL.filter(c => c.part_id === 'part-iii');
        const p4Chapters = CHAPTERS_ALL.filter(c => c.part_id === 'part-iv');
        const p5Chapters = CHAPTERS_ALL.filter(c => c.part_id === 'part-v');

        const r1 = renderTable(p1Chapters, 'part1-table-body');
        const r2 = renderTable(p2Chapters, 'part2-table-body');
        const r3 = renderTable(p3Chapters, 'part3-table-body');
        const r4 = renderTable(p4Chapters, 'part4-table-body');
        const r5 = renderTable(p5Chapters, 'part5-table-body');

        const totalChapters = CHAPTERS_ALL.length;
        const totalRead = r1.read + r2.read + r3.read + r4.read + r5.read;
        const totalPct = Math.round((r1.pctSum + r2.pctSum + r3.pctSum + r4.pctSum + r5.pctSum) / totalChapters);

        document.getElementById('stat-chapters-read').innerText = `${{totalRead}} / ${{totalChapters}}`;
        document.getElementById('stat-overall-pct').innerText = `${{totalPct}}%`;
      }}

      function setViewMode(mode) {{
        currentMode = mode;
        localStorage.setItem('dip_curriculum_view', mode);
        if (mode === 'syllabus') {{
          btnViewSyllabus.classList.add('active');
          btnViewParts.classList.remove('active');
          syllabusContainer.style.display = 'block';
          partsContainer.style.display = 'none';
        }} else {{
          btnViewParts.classList.add('active');
          btnViewSyllabus.classList.remove('active');
          partsContainer.style.display = 'block';
          syllabusContainer.style.display = 'none';
        }}
        filterUnit();
      }}

      function filterUnit() {{
        const cards = document.querySelectorAll('.unit-check-card');
        cards.forEach(card => {{
          const u = card.getAttribute('data-unit');
          if (currentUnit === 'all' || u === currentUnit) {{
            card.style.display = 'block';
          }} else {{
            card.style.display = 'none';
          }}
        }});
      }}

      btnViewSyllabus.addEventListener('click', () => setViewMode('syllabus'));
      btnViewParts.addEventListener('click', () => setViewMode('parts'));

      unitPills.forEach(pill => {{
        pill.addEventListener('click', () => {{
          unitPills.forEach(p => p.classList.remove('active'));
          pill.classList.add('active');
          currentUnit = pill.getAttribute('data-unit');
          filterUnit();
        }});
      }});

      renderDashboard();
      setViewMode(currentMode);

      // Export / Import
      document.getElementById('btn-export-data').addEventListener('click', () => {{
        const data = StateManager.exportState();
        const blob = new Blob([data], {{ type: 'application/json' }});
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'dip-minibook-study-backup.json';
        a.click();
        URL.revokeObjectURL(url);
      }});

      document.getElementById('btn-import-data').addEventListener('click', () => {{
        document.getElementById('file-import').click();
      }});

      document.getElementById('file-import').addEventListener('change', (e) => {{
        const file = e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (evt) => {{
          if (StateManager.importState(evt.target.result)) {{
            alert('Study progress imported successfully!');
            location.reload();
          }} else {{
            alert('Failed to parse backup JSON.');
          }}
        }};
        reader.readAsText(file);
      }});

      document.getElementById('btn-reset-data').addEventListener('click', () => {{
        if (confirm('Are you sure you want to reset all reading progress? This action cannot be undone.')) {{
          localStorage.clear();
          location.reload();
        }}
      }});
    }});
  </script>
</body>
</html>
'''

    with open(progress_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully regenerated progress.html with Syllabus & Parts dual-view filter and syllabus topics!")

if __name__ == '__main__':
    generate_index_html()
    generate_progress_html()
