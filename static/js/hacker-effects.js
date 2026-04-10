// Hacker-themed JavaScript effects
document.addEventListener('DOMContentLoaded', function() {
    // Matrix code rain effect
    createMatrixRain();

    // Terminal cursor blinking
    addTerminalCursors();

    // Add glitch effect to certain elements
    addGlitchEffects();

    // Add hover effects to links
    addLinkHoverEffects();
});

function createMatrixRain() {
    const matrixContainer = document.createElement('div');
    matrixContainer.className = 'matrix-code';
    document.body.appendChild(matrixContainer);
}

function addTerminalCursors() {
    // Add cursor to elements with specific classes
    const elements = document.querySelectorAll('.site-title, .section-title, .breach-title');
    elements.forEach(el => {
        const cursor = document.createElement('span');
        cursor.className = 'terminal-cursor';
        cursor.setAttribute('aria-hidden', 'true');
        el.appendChild(cursor);
    });
}

function addGlitchEffects() {
    // Add glitch effect to headings
    const headings = document.querySelectorAll('.home-title, .section-title, .breach-title');
    headings.forEach(heading => {
        heading.setAttribute('data-text', heading.textContent);
        heading.classList.add('glitch');
    });
}

function addLinkHoverEffects() {
    // Add subtle glitch on hover for links
    const links = document.querySelectorAll('a');
    links.forEach(link => {
        link.addEventListener('mouseenter', function() {
            this.style.textShadow = '0 0 5px #00ff00, 0 0 10px #00ff00';
        });
        link.addEventListener('mouseleave', function() {
            this.style.textShadow = 'none';
        });
    });
}

// Add some random binary characters occasionally
function addBinaryChars() {
    setInterval(() => {
        const binaryChars = ['0', '1'];
        const char = binaryChars[Math.floor(Math.random() * binaryChars.length)];

        const span = document.createElement('span');
        span.textContent = char;
        span.style.position = 'fixed';
        span.style.left = Math.random() * 100 + 'vw';
        span.style.top = Math.random() * 100 + 'vh';
        span.style.color = '#00ff00';
        span.style.opacity = '0.7';
        span.style.fontFamily = "'Courier New', monospace";
        span.style.pointerEvents = 'none';
        span.style.zIndex = '9999';

        document.body.appendChild(span);

        // Remove after animation
        setTimeout(() => {
            span.remove();
        }, 3000 + Math.random() * 2000);
    }, 500);
}

// Start adding binary characters
addBinaryChars();