/**
 * Breach Notes — Terminal Search
 * Pure client-side, Hugo JSON index, no dependencies.
 * Supports filter prefixes: malware: category: domain: cve:
 * Falls back to full-text across title + notes + vector + vendor.
 */
(function () {
  'use strict';

  /* ── Config ─────────────────────────────────────────── */
  const INDEX_URL   = '/index.json';
  const MIN_CHARS   = 2;          // characters before we start searching
  const MAX_RESULTS = 40;
  const DEBOUNCE_MS = 160;

  /* ── DOM refs ────────────────────────────────────────── */
  const input    = document.getElementById('breach-search-input');
  const overlay  = document.getElementById('search-results-overlay');
  const list     = document.getElementById('search-results-list');
  const status   = document.getElementById('search-results-status');
  const closeBtn = document.getElementById('search-results-close');
  const hints    = document.querySelectorAll('.hint-tag');

  if (!input || !overlay || !list) return; // guard for pages missing the partial

  /* ── State ───────────────────────────────────────────── */
  let index    = null;   // loaded once
  let pending  = null;   // debounce timer

  /* ── Load index ─────────────────────────────────────── */
  function loadIndex() {
    if (index !== null) return Promise.resolve(index);
    return fetch(INDEX_URL)
      .then(r => { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(data => {
        index = Array.isArray(data) ? data : [];
        return index;
      });
  }

  /* ── Query parsing ───────────────────────────────────── */
  // Extracts typed filter prefixes and remainder free text
  // e.g. "malware:WannaCry ransomware" → { malware:"wannacry", free:"ransomware" }
  const PREFIXES = ['malware', 'category', 'domain', 'cve', 'type', 'vendor'];

  function parseQuery(raw) {
    const filters = {};
    let remainder = raw.trim().toLowerCase();

    // Extract each prefix token
    PREFIXES.forEach(pfx => {
      const re = new RegExp(`(?:^|\\s)${pfx}:([^\\s]+)`, 'i');
      const m = remainder.match(re);
      if (m) {
        filters[pfx] = m[1].toLowerCase();
        remainder = remainder.replace(m[0], ' ').trim();
      }
    });

    filters.free = remainder.replace(/\s+/g, ' ').trim();
    return filters;
  }

  /* ── Scoring & matching ──────────────────────────────── */
  function scoreRecord(rec, filters) {
    let score = 0;

    // Helper: substring match gives points
    const has = (field, val) => field && field.toLowerCase().includes(val);
    const exact = (field, val) => field && field.toLowerCase() === val;

    // Typed filter checks — must ALL match if present
    if (filters.malware) {
      if (!has(rec.malware, filters.malware)) return -1;
      score += exact(rec.malware, filters.malware) ? 20 : 10;
    }
    if (filters.category) {
      if (!has(rec.category, filters.category)) return -1;
      score += 15;
    }
    if (filters.type) {
      // alias for category
      if (!has(rec.category, filters.type)) return -1;
      score += 15;
    }
    if (filters.domain) {
      if (!has(rec.domain, filters.domain)) return -1;
      score += 15;
    }
    if (filters.cve) {
      const cveStr = Array.isArray(rec.cve) ? rec.cve.join(' ').toLowerCase() : '';
      if (!cveStr.includes(filters.cve)) return -1;
      score += 15;
    }
    if (filters.vendor) {
      if (!has(rec.vendor, filters.vendor)) return -1;
      score += 10;
    }

    // Free text — searched across title + notes + vector + vendor
    if (filters.free) {
      const terms = filters.free.split(' ').filter(Boolean);
      const haystack = [rec.title, rec.notes, rec.vector, rec.vendor, rec.domain, rec.malware]
        .filter(Boolean)
        .join(' ')
        .toLowerCase();

      for (const term of terms) {
        if (!haystack.includes(term)) return -1;  // all terms must match
      }

      // Bonus for title matches
      const titleLow = (rec.title || '').toLowerCase();
      for (const term of terms) {
        if (titleLow.includes(term)) score += 8;
        score += 2; // base for notes match
      }
    }

    // Date recency bonus (tiny, for tie-breaking)
    if (rec.date) {
      const yr = parseInt(rec.date.slice(0, 4), 10);
      if (!isNaN(yr)) score += Math.max(0, (yr - 1990) * 0.05);
    }

    return score;
  }

  /* ── Highlight matched terms in text ────────────────── */
  function highlight(text, terms) {
    if (!text) return '';
    let safe = text.replace(/</g, '&lt;').replace(/>/g, '&gt;');
    if (!terms || !terms.length) return safe;
    const re = new RegExp(`(${terms.map(t =>
      t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|')})`, 'gi');
    return safe.replace(re, '<mark>$1</mark>');
  }

  /* ── Excerpt ─────────────────────────────────────────── */
  function excerpt(text, terms, maxLen = 180) {
    if (!text) return '';
    const lower = text.toLowerCase();
    let best = 0;
    if (terms && terms.length) {
      let earliest = text.length;
      terms.forEach(t => {
        const i = lower.indexOf(t.toLowerCase());
        if (i !== -1 && i < earliest) earliest = i;
      });
      best = Math.max(0, earliest - 40);
    }
    const slice = text.slice(best, best + maxLen);
    const trimmed = (best > 0 ? '…' : '') + slice + (best + maxLen < text.length ? '…' : '');
    return highlight(trimmed, terms);
  }

  /* ── Render results ──────────────────────────────────── */
  function renderResults(results, filters) {
    const terms = filters.free ? filters.free.split(' ').filter(Boolean) : [];

    list.innerHTML = '';

    if (!results.length) {
      status.textContent = '0 RECORDS FOUND — QUERY RETURNED NULL';
      return;
    }

    status.textContent = `${results.length} RECORD${results.length !== 1 ? 'S' : ''} MATCHED`;

    results.slice(0, MAX_RESULTS).forEach((rec, i) => {
      const li = document.createElement('li');
      li.className = 'search-result-item';

      // Determine display domain
      const domainDisplay = rec.domain ? `<span class="sr-domain">${highlight(rec.domain, terms)}</span>` : '';
      const malwareDisplay = rec.malware ? `<span class="sr-tag sr-malware">${highlight(rec.malware, terms)}</span>` : '';
      const catDisplay = `<span class="sr-tag sr-category">${rec.category}</span>`;
      const dateDisplay = rec.date ? `<span class="sr-date">${rec.date.slice(0, 7)}</span>` : '';

      li.innerHTML = `
        <a href="${rec.url}" class="sr-link">
          <div class="sr-header">
            <span class="sr-index">[${String(i + 1).padStart(2, '0')}]</span>
            <span class="sr-title">${highlight(rec.title, terms)}</span>
          </div>
          <div class="sr-meta">
            ${dateDisplay}${catDisplay}${malwareDisplay}${domainDisplay}
          </div>
          <div class="sr-excerpt">${excerpt(rec.notes || rec.vector, terms)}</div>
        </a>
      `;
      list.appendChild(li);
    });

    if (results.length > MAX_RESULTS) {
      const more = document.createElement('li');
      more.className = 'search-result-more';
      more.textContent = `… and ${results.length - MAX_RESULTS} more — refine your query`;
      list.appendChild(more);
    }
  }

  /* ── Run search ─────────────────────────────────────── */
  function runSearch(raw) {
    if (!raw || raw.trim().length < MIN_CHARS) {
      closeResults();
      return;
    }

    const filters = parseQuery(raw);
    const hasFilters = Object.values(filters).some(v =>
      v && (typeof v === 'string' ? v.length >= MIN_CHARS : v.length > 0)
    );
    if (!hasFilters) { closeResults(); return; }

    loadIndex().then(idx => {
      const scored = idx
        .map(rec => ({ rec, score: scoreRecord(rec, filters) }))
        .filter(x => x.score > 0)
        .sort((a, b) => b.score - a.score);

      showOverlay();
      renderResults(scored.map(x => x.rec), filters);
    }).catch(() => {
      status.textContent = 'ERROR: FAILED TO LOAD BREACH INDEX';
      showOverlay();
    });
  }

  /* ── Overlay show/hide ───────────────────────────────── */
  function showOverlay() {
    overlay.hidden = false;
    input.setAttribute('aria-expanded', 'true');
  }

  function closeResults() {
    overlay.hidden = true;
    input.setAttribute('aria-expanded', 'false');
    list.innerHTML = '';
    status.textContent = '';
  }

  /* ── Hint-tag click shortcuts ───────────────────────── */
  hints.forEach(tag => {
    tag.addEventListener('click', () => {
      const type = tag.dataset.filterType;
      if (!type) return;
      // Insert or replace the prefix in the input
      const current = input.value;
      const re = new RegExp(`(?:^|\\s)${type}:[^\\s]*`, 'i');
      const insert = `${type}:`;
      input.value = re.test(current)
        ? current.replace(re, (m) => m.startsWith(' ') ? ' ' + insert : insert).trimStart()
        : (current.trim() ? current.trimEnd() + ' ' + insert : insert);
      input.focus();
      // Place cursor at end
      const len = input.value.length;
      input.setSelectionRange(len, len);
    });
  });

  /* ── Event wiring ────────────────────────────────────── */
  input.addEventListener('input', () => {
    clearTimeout(pending);
    pending = setTimeout(() => runSearch(input.value), DEBOUNCE_MS);
  });

  input.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      if (!overlay.hidden) {
        closeResults();
        input.value = '';
      }
      input.blur();
    }
    if (e.key === 'Enter') {
      clearTimeout(pending);
      runSearch(input.value);
    }
  });

  closeBtn.addEventListener('click', () => {
    closeResults();
    input.value = '';
    input.focus();
  });

  // Click outside overlay to close
  document.addEventListener('click', e => {
    if (!overlay.hidden &&
        !overlay.contains(e.target) &&
        !document.getElementById('terminal-search-bar').contains(e.target)) {
      closeResults();
    }
  });

  // Keyboard shortcut: / to focus search
  document.addEventListener('keydown', e => {
    if (e.key === '/' && document.activeElement !== input &&
        !['INPUT','TEXTAREA','SELECT'].includes(document.activeElement.tagName)) {
      e.preventDefault();
      input.focus();
      input.select();
    }
  });

  // Prefetch the index on hover/focus of the search bar so it's instant
  document.getElementById('terminal-search-bar').addEventListener('mouseenter', () => {
    loadIndex().catch(() => {});
  }, { once: true });
  input.addEventListener('focus', () => {
    loadIndex().catch(() => {});
  }, { once: true });

})();
