// Hacker-themed JavaScript effects
document.addEventListener('DOMContentLoaded', function() {
    createBinaryRain();
    addGlitchEffects();
    addTerminalCursors();
    addLinkHoverEffects();
});

// ── Binary rain background ────────────────────────────────────
function createBinaryRain() {
    const container = document.createElement('div');
    container.id = 'binary-rain-bg';
    Object.assign(container.style, {
        position:      'fixed',
        top:           '0',
        left:          '0',
        width:         '100%',
        height:        '100%',
        pointerEvents: 'none',
        zIndex:        '-1',
        overflow:      'hidden',
    });
    document.body.insertBefore(container, document.body.firstChild);

    const COL_W   = 18;   // px between columns
    const cols    = Math.ceil(window.innerWidth / COL_W);

    for (let i = 0; i < cols; i++) {
        // stagger start times so columns don't all drop together
        setTimeout(() => spawnColumn(container, i * COL_W), Math.random() * 6000);
    }

    // Respawn columns forever
    setInterval(() => {
        const i = Math.floor(Math.random() * cols);
        spawnColumn(container, i * COL_W);
    }, 800);
}

function spawnColumn(container, x) {
    const LENGTH   = 6 + Math.floor(Math.random() * 10);  // chars per column
    const SPEED    = 60 + Math.random() * 80;              // px/s
    const BASE_Y   = -LENGTH * 18;
    const TARGET_Y = window.innerHeight + 40;
    const DURATION = ((TARGET_Y - BASE_Y) / SPEED) * 1000; // ms

    for (let row = 0; row < LENGTH; row++) {
        const span = document.createElement('span');
        span.textContent = Math.random() < 0.5 ? '0' : '1';

        const brightness = row === 0 ? 1 : (1 - row / LENGTH) * 0.6 + 0.05;
        const startY     = BASE_Y + row * 18;

        Object.assign(span.style, {
            position:   'absolute',
            left:       x + 'px',
            top:        startY + 'px',
            color:      '#00ff00',
            opacity:    (brightness * 0.35).toFixed(2),
            fontSize:   '14px',
            fontFamily: "'Share Tech Mono', 'Courier New', monospace",
            lineHeight: '1',
            willChange: 'transform',
        });

        container.appendChild(span);

        // Fall animation
        const anim = span.animate(
            [{ transform: 'translateY(0)' }, { transform: `translateY(${TARGET_Y - startY}px)` }],
            { duration: DURATION, delay: 0, easing: 'linear', fill: 'forwards' }
        );

        // Glitch: random flicker + char swap during fall
        scheduleGlitch(span, DURATION);

        anim.onfinish = () => span.remove();
    }
}

function scheduleGlitch(span, totalDuration) {
    const glitchCount = 2 + Math.floor(Math.random() * 4);
    for (let g = 0; g < glitchCount; g++) {
        const delay = Math.random() * totalDuration;

        // Flicker opacity + maybe shift char + optional horizontal jitter
        setTimeout(() => {
            if (!span.isConnected) return;

            // Swap char
            span.textContent = Math.random() < 0.5 ? '0' : '1';

            // Brief brightness spike
            const origOpacity = span.style.opacity;
            span.style.opacity   = (0.5 + Math.random() * 0.4).toFixed(2);
            span.style.textShadow = '0 0 6px #00ff00, 0 0 12px #00ff00';

            // Occasional horizontal jitter
            const jitter = (Math.random() < 0.3)
                ? `translateX(${(Math.random() * 6 - 3).toFixed(1)}px)`
                : '';
            if (jitter) span.style.transform = jitter;

            // Restore after a short flash
            const flashDur = 60 + Math.random() * 120;
            setTimeout(() => {
                if (!span.isConnected) return;
                span.style.opacity    = origOpacity;
                span.style.textShadow = '';
                span.style.transform  = '';
            }, flashDur);
        }, delay);
    }
}

// ── Terminal cursor ───────────────────────────────────────────
function addTerminalCursors() {
    const els = document.querySelectorAll('.site-title');
    els.forEach(el => {
        const cursor = document.createElement('span');
        cursor.className = 'terminal-cursor';
        cursor.setAttribute('aria-hidden', 'true');
        el.appendChild(cursor);
    });
}

// ── CSS glitch on headings ────────────────────────────────────
function addGlitchEffects() {
    const headings = document.querySelectorAll('.site-title, .section-title, .breach-title');
    headings.forEach(h => {
        h.setAttribute('data-text', h.textContent.trim());
        h.classList.add('glitch');
    });
}

// ── Link hover glow ───────────────────────────────────────────
function addLinkHoverEffects() {
    document.querySelectorAll('a').forEach(link => {
        link.addEventListener('mouseenter', function() {
            this.style.textShadow = '0 0 5px #00ff00, 0 0 10px #00ff00';
        });
        link.addEventListener('mouseleave', function() {
            this.style.textShadow = '';
        });
    });
}
