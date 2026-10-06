/**
 * DIGITAL IMAGE PROCESSING (DIP) MINIBOOK
 * core.js — Shell Controller & Navigation Engine
 *
 * Implements:
 *   - Theme Manager (Auto, Light Archival Paper, Dark Pitch Black, Paper Sepia)
 *   - Sidebar Drawer with Desktop Collapse & Mobile Overlay
 *   - Reading Progress Bar & Scroll-Spy
 *   - Keyboard Shortcuts (T: Theme, S: Sidebar, F: Reading Focus, ?: Help)
 *   - Code Block Copy Buttons
 *   - Zero-clipping layout coordination
 */
'use strict';

/* ── UTILITIES ──────────────────────────────────────────────────────── */
const Utils = (() => {
  const debounce = (func, wait = 150) => {
    let timeout;
    return (...args) => {
      clearTimeout(timeout);
      timeout = setTimeout(() => func(...args), wait);
    };
  };
  const isReducedMotion = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const safeScrollTo = (top) => window.scrollTo({ top, behavior: isReducedMotion() ? 'auto' : 'smooth' });
  return { debounce, isReducedMotion, safeScrollTo };
})();

/* ── THEME MANAGER ──────────────────────────────────────────────────── */
const ThemeManager = (() => {
  const root = document.documentElement;
  const THEMES = ['auto', 'light', 'dark', 'paper'];

  function actualTheme(mode) {
    if (mode === 'auto') {
      return window.matchMedia?.('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    return ['light', 'dark', 'paper'].includes(mode) ? mode : 'light';
  }

  function icon(theme) {
    const paths = {
      light: '<circle cx="12" cy="12" r="4.5"/><path d="M12 2v2M12 20v2M4.93 4.93l1.42 1.42M17.65 17.65l1.42 1.42M2 12h2M20 12h2M4.93 19.07l1.42-1.42M17.65 6.35l1.42-1.42"/>',
      dark: '<path d="M21 12.8A8.5 8.5 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/>',
      paper: '<path d="M6 3.5h10.5A1.5 1.5 0 0 1 18 5v14.5H7.5A1.5 1.5 0 0 1 6 18V3.5Z"/><path d="M8.5 7h6M8.5 10h6M8.5 13h4"/>'
    };
    return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${paths[theme] || paths.light}</svg>`;
  }

  function apply(mode, options = {}) {
    const normalized = THEMES.includes(mode) ? mode : 'auto';
    const active = actualTheme(normalized);
    root.setAttribute('data-theme', active);
    root.dataset.themePreference = normalized;
    if (!options.skipPersist && window.StateManager) {
      StateManager.set('theme', normalized);
    }

    const btn = document.getElementById('theme-toggle');
    if (btn) {
      btn.innerHTML = icon(active);
      btn.dataset.theme = active;
      btn.dataset.themePreference = normalized;
      btn.setAttribute('aria-label', `Theme: ${normalized}. Appearance: ${active}. Press T to cycle.`);
      btn.title = `Theme: ${normalized} (Press T)`;
    }
    return active;
  }

  function toggle() {
    const current = (window.StateManager && StateManager.get('theme')) || 'auto';
    const next = THEMES[(THEMES.indexOf(current) + 1) % THEMES.length];
    return apply(next);
  }

  function init() {
    const saved = (window.StateManager && StateManager.get('theme')) || 'auto';
    apply(saved, { skipPersist: true });
    const media = window.matchMedia?.('(prefers-color-scheme: dark)');
    if (media) {
      const handler = () => {
        if ((window.StateManager && StateManager.get('theme')) === 'auto') {
          apply('auto', { skipPersist: true });
        }
      };
      if (media.addEventListener) media.addEventListener('change', handler);
      else if (media.addListener) media.addListener(handler);
    }
  }

  return { init, toggle, apply };
})();

/* ── SIDEBAR MANAGER ────────────────────────────────────────────────── */
const SidebarManager = (() => {
  function apply() {
    const isOpen = window.StateManager ? StateManager.get('sidebarOpen') : true;
    const sidebar = document.getElementById('sidebar');
    const content = document.getElementById('main-content');
    const overlay = document.getElementById('sidebar-overlay');
    const isMobile = window.innerWidth <= 1024;

    if (!sidebar) return;
    sidebar.setAttribute('aria-expanded', String(isOpen));

    if (isMobile) {
      if (isOpen) {
        sidebar.classList.add('open');
        sidebar.classList.remove('collapsed');
        if (overlay) overlay.classList.add('show');
        document.body.style.overflow = 'hidden';
      } else {
        sidebar.classList.remove('open');
        if (overlay) overlay.classList.remove('show');
        document.body.style.overflow = '';
      }
    } else {
      if (overlay) overlay.classList.remove('show');
      document.body.style.overflow = '';
      if (isOpen) {
        sidebar.classList.remove('collapsed');
        if (content) content.classList.remove('sidebar-collapsed');
      } else {
        sidebar.classList.add('collapsed');
        if (content) content.classList.add('sidebar-collapsed');
      }
    }

    const toggleBtn = document.getElementById('sidebar-toggle');
    if (toggleBtn) {
      toggleBtn.setAttribute('aria-expanded', String(isOpen));
      toggleBtn.title = isOpen ? 'Hide sidebar (S)' : 'Show sidebar (S)';
    }
  }

  function toggle() {
    const current = window.StateManager ? StateManager.get('sidebarOpen') : true;
    if (window.StateManager) StateManager.set('sidebarOpen', !current);
    apply();
  }

  function closeMobile() {
    if (window.innerWidth <= 1024) {
      if (window.StateManager) StateManager.set('sidebarOpen', false);
      apply();
    }
  }

  function init() {
    const toggleBtn = document.getElementById('sidebar-toggle');
    const overlay = document.getElementById('sidebar-overlay');
    if (toggleBtn) toggleBtn.addEventListener('click', toggle);
    if (overlay) overlay.addEventListener('click', closeMobile);

    window.addEventListener('resize', Utils.debounce(() => {
      apply();
    }, 200));

    apply();
  }

  return { init, toggle, closeMobile };
})();

/* ── PROGRESS & SCROLL SPY ──────────────────────────────────────────── */
const ReadingProgress = (() => {
  const progressBar = document.getElementById('progress-bar');
  const chapterTitleHeader = document.querySelector('.header-chapter-title');
  const chapterHero = document.querySelector('.chapter-hero');
  const headings = Array.from(document.querySelectorAll('.chapter-content h2[id], .content-inner h2[id]'));
  const currentChapterId = document.body.dataset.chapterId || '';

  function onScroll() {
    const docH = document.documentElement.scrollHeight - window.innerHeight;
    const scrolled = window.scrollY;
    const pct = docH > 0 ? Math.min(100, Math.max(0, (scrolled / docH) * 100)) : 0;

    if (progressBar) {
      progressBar.style.width = `${pct}%`;
    }

    if (currentChapterId && window.StateManager) {
      StateManager.setReadProgress(currentChapterId, pct);
    }

    // Header title visibility
    if (chapterTitleHeader && chapterHero) {
      const heroBottom = chapterHero.getBoundingClientRect().bottom;
      if (heroBottom < 60) {
        chapterTitleHeader.classList.add('visible');
      } else {
        chapterTitleHeader.classList.remove('visible');
      }
    }

    // Scroll spy for sidebar links
    if (headings.length > 0) {
      const scrollPos = window.scrollY + 120;
      let activeId = headings[0].id;
      for (let i = 0; i < headings.length; i++) {
        if (headings[i].offsetTop <= scrollPos) {
          activeId = headings[i].id;
        }
      }
      document.querySelectorAll('.sidebar-sub .sidebar-link').forEach(link => {
        if (link.getAttribute('href') === `#${activeId}`) {
          link.classList.add('active');
        } else {
          link.classList.remove('active');
        }
      });
    }
  }

  function init() {
    window.addEventListener('scroll', Utils.debounce(onScroll, 20), { passive: true });
    onScroll();
  }

  return { init };
})();

/* ── READING FOCUS MODE ─────────────────────────────────────────────── */
const FocusMode = (() => {
  function toggle() {
    const isFocus = document.body.classList.toggle('reading-focus');
    const btn = document.getElementById('reading-mode-btn');
    if (btn) {
      btn.setAttribute('aria-pressed', String(isFocus));
      btn.classList.toggle('active', isFocus);
    }
  }

  function init() {
    const btn = document.getElementById('reading-mode-btn');
    if (btn) btn.addEventListener('click', toggle);
  }

  return { init, toggle };
})();

/* ── CODE COPY BUTTONS ──────────────────────────────────────────────── */
function initCodeCopy() {
  document.querySelectorAll('.code-block').forEach(block => {
    const btn = block.querySelector('.code-copy-btn');
    const pre = block.querySelector('pre');
    if (!btn || !pre) return;

    btn.addEventListener('click', async () => {
      try {
        const text = pre.innerText;
        await navigator.clipboard.writeText(text);
        const originalText = btn.innerHTML;
        btn.innerHTML = '<span>✓ Copied</span>';
        setTimeout(() => { btn.innerHTML = originalText; }, 2000);
      } catch (err) {
        console.warn('Copy failed:', err);
      }
    });
  });
}

/* ── KEYBOARD SHORTCUTS ─────────────────────────────────────────────── */
function initKeyboard() {
  window.addEventListener('keydown', (e) => {
    if (['INPUT', 'TEXTAREA'].includes(e.target.tagName) || e.target.isContentEditable) return;

    // Theme toggle: T
    if (e.key === 't' || e.key === 'T') {
      e.preventDefault();
      ThemeManager.toggle();
    }
    // Sidebar toggle: S
    else if (e.key === 's' || e.key === 'S') {
      e.preventDefault();
      SidebarManager.toggle();
    }
    // Reading Focus: F
    else if (e.key === 'f' || e.key === 'F') {
      e.preventDefault();
      FocusMode.toggle();
    }
  });
}

/* ── BOOTSTRAP ──────────────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  ThemeManager.init();
  SidebarManager.init();
  ReadingProgress.init();
  FocusMode.init();
  initCodeCopy();
  initKeyboard();

  const themeBtn = document.getElementById('theme-toggle');
  if (themeBtn) themeBtn.addEventListener('click', ThemeManager.toggle);
});
