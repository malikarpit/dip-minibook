/*
 * DIGITAL IMAGE PROCESSING (DIP) MINIBOOK
 * state.js — Local-First State Manager
 *
 * Handles:
 *   - Theme preference ('auto', 'light', 'dark', 'paper')
 *   - Sidebar state (open/collapsed)
 *   - Reading progress & completions by chapter
 *   - Bookmarks & Highlights
 *   - MCQ results & quiz scores
 *   - Reading focus mode
 */
'use strict';

(() => {
  const KEY = 'dip-minibook-state';
  const NUDGE_KEY = 'dip-minibook-backup-nudge';
  const DEFAULT_STATE = {
    theme: 'auto',
    sidebarOpen: typeof window !== 'undefined' ? window.innerWidth > 1024 : true,
    checklist: {},
    bookmarks: [],
    highlights: [],
    fontSize: 17,
    mcqResults: {},
    readProgress: {},
    readingMode: false
  };

  let state = clone(DEFAULT_STATE);

  function clone(value) {
    return JSON.parse(JSON.stringify(value));
  }

  function normalizeTheme(value) {
    return ['auto', 'light', 'dark', 'paper'].includes(value) ? value : 'auto';
  }

  function normalizeState(candidate) {
    const next = { ...clone(DEFAULT_STATE), ...(candidate && typeof candidate === 'object' ? candidate : {}) };
    next.theme = normalizeTheme(next.theme);
    next.sidebarOpen = Boolean(next.sidebarOpen);
    next.checklist = next.checklist && typeof next.checklist === 'object' ? next.checklist : {};
    next.bookmarks = Array.isArray(next.bookmarks) ? next.bookmarks : [];
    next.highlights = Array.isArray(next.highlights) ? next.highlights : [];
    next.mcqResults = next.mcqResults && typeof next.mcqResults === 'object' ? next.mcqResults : {};
    next.readProgress = next.readProgress && typeof next.readProgress === 'object' ? next.readProgress : {};
    next.readingMode = Boolean(next.readingMode);
    const numericFont = Number(next.fontSize);
    next.fontSize = Number.isFinite(numericFont) ? Math.min(22, Math.max(14, Math.round(numericFont))) : 17;
    return next;
  }

  function safeGet(key) {
    try { return localStorage.getItem(key); } catch (e) { console.warn('safeGet failed', e); return null; }
  }
  function safeSet(key, value) {
    try { localStorage.setItem(key, value); return true; } catch (e) { console.warn('safeSet failed', e); return false; }
  }

  function init() {
    try {
      const saved = safeGet(KEY);
      if (saved) {
        try { state = normalizeState(JSON.parse(saved)); }
        catch (e) { console.warn('Ignoring invalid saved state:', e); state = clone(DEFAULT_STATE); }
      }
      maybeNudgeBackup();
    } catch (e) {
      console.warn('StateManager.init error:', e);
    }
  }

  function save() {
    safeSet(KEY, JSON.stringify(state));
  }

  function get(key) {
    if (!key) return clone(state);
    return state[key] !== undefined ? clone(state[key]) : undefined;
  }

  function set(key, value) {
    if (!key) return;
    state[key] = clone(value);
    save();
    window.dispatchEvent(new CustomEvent('dip-state-change', { detail: { key, value } }));
  }

  function setReadProgress(chapterId, percent) {
    if (!chapterId) return;
    const progress = Math.min(100, Math.max(0, Math.round(percent)));
    if (!state.readProgress) state.readProgress = {};
    state.readProgress[chapterId] = progress;
    if (progress >= 90) {
      if (!state.checklist) state.checklist = {};
      state.checklist[chapterId] = true;
    }
    save();
  }

  function getReadProgress(chapterId) {
    return (state.readProgress && state.readProgress[chapterId]) || 0;
  }

  function getAllReadProgress() {
    return clone(state.readProgress || {});
  }

  function setMCQResult(quizId, questionIdx, isCorrect) {
    if (!quizId) return;
    if (!state.mcqResults) state.mcqResults = {};
    if (!state.mcqResults[quizId]) state.mcqResults[quizId] = {};
    state.mcqResults[quizId][questionIdx] = Boolean(isCorrect);
    save();
  }

  function getMCQStats(quizId) {
    if (!quizId || !state.mcqResults || !state.mcqResults[quizId]) {
      return { total: 0, correct: 0, pct: 0 };
    }
    const answers = Object.values(state.mcqResults[quizId]);
    const total = answers.length;
    const correct = answers.filter(Boolean).length;
    const pct = total > 0 ? Math.round((correct / total) * 100) : 0;
    return { total, correct, pct };
  }

  function exportData() {
    return JSON.stringify({
      schema: 'dip-minibook-v1',
      exportedAt: new Date().toISOString(),
      state: clone(state)
    }, null, 2);
  }

  function importData(rawJson) {
    try {
      const parsed = JSON.parse(rawJson);
      const incoming = parsed && parsed.state ? parsed.state : parsed;
      state = normalizeState(incoming);
      save();
      return true;
    } catch (e) {
      console.error('importData failed:', e);
      return false;
    }
  }

  function maybeNudgeBackup() {
    const totalActions = Object.keys(state.readProgress || {}).length +
      (state.bookmarks || []).length +
      (state.highlights || []).length;
    if (totalActions < 5) return;
    const lastNudge = Number(safeGet(NUDGE_KEY) || 0);
    const now = Date.now();
    const sevenDays = 7 * 24 * 60 * 60 * 1000;
    if (now - lastNudge > sevenDays) {
      safeSet(NUDGE_KEY, String(now));
      console.info('Tip: You can export your DIP MiniBook notes and progress from the dashboard.');
    }
  }

  window.StateManager = {
    init,
    get,
    set,
    save,
    setReadProgress,
    getReadProgress,
    getAllReadProgress,
    setMCQResult,
    getMCQStats,
    exportData,
    importData
  };

  init();
})();
