/**
 * Breach Notes — Browse Controls
 * Load-more pagination and sort controls for the homepage breach grid.
 * Pure vanilla JS, no dependencies.
 */
(function () {
  'use strict';

  /* ── Config ─────────────────────────────────────── */
  var PAGE_SIZE = 12;

  /* ── DOM refs ───────────────────────────────────── */
  var grid       = document.getElementById('breach-grid');
  var loadBtn    = document.getElementById('load-more-btn');
  var loadHint   = document.getElementById('load-more-hint');
  var container  = document.getElementById('load-more-container');
  var sortBtns   = document.querySelectorAll('.sort-btn');

  if (!grid || !loadBtn) return;

  /* ── State ──────────────────────────────────────── */
  var allCards    = Array.from(grid.querySelectorAll('.breach-card-wrapper'));
  var visible     = PAGE_SIZE;
  var currentSort = 'recent';

  /* ── Initial hide ───────────────────────────────── */
  function applyVisibility() {
    allCards.forEach(function (card, i) {
      card.style.display = i < visible ? '' : 'none';
    });

    var remaining = allCards.length - visible;
    if (remaining <= 0) {
      container.style.display = 'none';
    } else {
      container.style.display = '';
      loadHint.textContent = remaining + ' more record' + (remaining !== 1 ? 's' : '');
    }
  }

  /* ── Sort functions ─────────────────────────────── */
  function sortCards(mode) {
    var sorted = allCards.slice();

    switch (mode) {
      case 'recent':
        sorted.sort(function (a, b) {
          return (b.getAttribute('data-date') || '').localeCompare(a.getAttribute('data-date') || '');
        });
        break;
      case 'name-asc':
        sorted.sort(function (a, b) {
          return (a.getAttribute('data-name') || '').toLowerCase()
            .localeCompare((b.getAttribute('data-name') || '').toLowerCase());
        });
        break;
      case 'name-desc':
        sorted.sort(function (a, b) {
          return (b.getAttribute('data-name') || '').toLowerCase()
            .localeCompare((a.getAttribute('data-name') || '').toLowerCase());
        });
        break;
      case 'category':
        sorted.sort(function (a, b) {
          var catCmp = (a.getAttribute('data-category') || '').localeCompare(b.getAttribute('data-category') || '');
          if (catCmp !== 0) return catCmp;
          return (b.getAttribute('data-date') || '').localeCompare(a.getAttribute('data-date') || '');
        });
        break;
    }

    allCards = sorted;

    // Re-order DOM
    sorted.forEach(function (card) {
      grid.appendChild(card);
    });
  }

  /* ── Load more handler ──────────────────────────── */
  loadBtn.addEventListener('click', function () {
    visible = Math.min(visible + PAGE_SIZE, allCards.length);
    applyVisibility();
  });

  /* ── Sort button handlers ───────────────────────── */
  sortBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var mode = btn.getAttribute('data-sort');
      if (mode === currentSort) return;

      currentSort = mode;

      // Update active state
      sortBtns.forEach(function (b) {
        b.classList.remove('sort-btn--active');
        b.setAttribute('aria-pressed', 'false');
      });
      btn.classList.add('sort-btn--active');
      btn.setAttribute('aria-pressed', 'true');

      // Re-sort and reset to first page
      sortCards(mode);
      visible = PAGE_SIZE;
      applyVisibility();

      // Scroll to top of section
      var section = document.getElementById('home-recent');
      if (section) section.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  /* ── Init ────────────────────────────────────────── */
  applyVisibility();

})();
