// Document Ready
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initPreloader();
    initMobileMenu();
    initSearch();
    initScrollEffects();
    initMessages();
    initDropdowns();
    initAnimations();
    initNewsletter();
});

// ===== PRELOADER =====
function initPreloader() {
    const preloader = document.querySelector('.preloader');
    if (preloader) {
        window.addEventListener('load', function() {
            setTimeout(() => {
                preloader.classList.add('loaded');
                setTimeout(() => {
                    preloader.style.display = 'none';
                }, 500);
            }, 1000);
        });
    }
}

// ===== MOBILE MENU =====
function initMobileMenu() {
    const menuToggle = document.getElementById('menuToggle');
    const menuClose = document.getElementById('menuClose');
    const mobileMenu = document.getElementById('mobileMenu');

    if (menuToggle && mobileMenu) {
        menuToggle.addEventListener('click', function() {
            menuToggle.classList.toggle('active');
            mobileMenu.classList.toggle('active');
            document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
        });
    }

    if (menuClose && mobileMenu) {
        menuClose.addEventListener('click', function() {
            menuToggle.classList.remove('active');
            mobileMenu.classList.remove('active');
            document.body.style.overflow = '';
        });
    }

    // Close menu on link click
    document.querySelectorAll('.mobile-nav-link').forEach(link => {
        link.addEventListener('click', function() {
            menuToggle.classList.remove('active');
            mobileMenu.classList.remove('active');
            document.body.style.overflow = '';
        });
    });

    // Close menu on outside click
    document.addEventListener('click', function(e) {
        if (mobileMenu && mobileMenu.classList.contains('active')) {
            if (!mobileMenu.contains(e.target) && !menuToggle.contains(e.target)) {
                menuToggle.classList.remove('active');
                mobileMenu.classList.remove('active');
                document.body.style.overflow = '';
            }
        }
    });
}

// ===== SEARCH FUNCTIONALITY =====
function initSearch() {
    const searchBtn = document.querySelector('.btn-search');
    const searchClose = document.getElementById('searchClose');
    const searchOverlay = document.getElementById('searchOverlay');
    const searchInput = document.querySelector('.search-input');

    // Open search
    if (searchBtn && searchOverlay) {
        searchBtn.addEventListener('click', function() {
            searchOverlay.classList.add('active');
            document.body.style.overflow = 'hidden';
            setTimeout(() => {
                searchInput.focus();
            }, 300);
        });
    }

    // Close search
    if (searchClose && searchOverlay) {
        searchClose.addEventListener('click', function() {
            searchOverlay.classList.remove('active');
            document.body.style.overflow = '';
        });
    }

    // Close on escape
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && searchOverlay.classList.contains('active')) {
            searchOverlay.classList.remove('active');
            document.body.style.overflow = '';
        }
    });

    // Search functionality
    const searchActionBtn = document.querySelector('.btn-search-action');
    if (searchActionBtn && searchInput) {
        searchActionBtn.addEventListener('click', function() {
            performSearch(searchInput.value);
        });

        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                performSearch(this.value);
            }
        });
    }

    // Trending search clicks
    document.querySelectorAll('.search-trending a').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const term = this.textContent;
            searchInput.value = term;
            performSearch(term);
        });
    });
}

function performSearch(term) {
    if (term.trim()) {
        // Here you would normally make an API call
        console.log('Searching for:', term);
        // For demo, just show alert
        alert(`Поиск: ${term}\n\nВ реальном проекте здесь будет интеграция с поиском туров.`);
    }
}

// ===== SCROLL EFFECTS =====
function initScrollEffects() {
    // Sticky header
    const header = document.getElementById('header');
    if (header) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }

    // Scroll to top button
    const scrollTopBtn = document.getElementById('scrollTop');
    if (scrollTopBtn) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 500) {
                scrollTopBtn.classList.add('visible');
            } else {
                scrollTopBtn.classList.remove('visible');
            }
        });

        scrollTopBtn.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            // Skip if it's just "#"
            if (href === '#') return;

            // Skip for dropdown links
            if (this.classList.contains('nav-link') && this.querySelector('.fa-chevron-down')) {
                return;
            }

            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const headerHeight = header ? header.offsetHeight : 0;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset;

                window.scrollTo({
                    top: targetPosition - headerHeight - 20,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// ===== MESSAGES =====
function initMessages() {
    const messages = document.querySelectorAll('.message');

    messages.forEach(function(message) {
        // Auto dismiss after 5 seconds
        const autoDismiss = setTimeout(function() {
            dismissMessage(message);
        }, 5000);

        // Close button
        const closeBtn = message.querySelector('.message-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', function() {
                clearTimeout(autoDismiss);
                dismissMessage(message);
            });
        }
    });
}

function dismissMessage(message) {
    message.style.animation = 'slideOutRight 0.3s ease-out forwards';
    setTimeout(function() {
        message.remove();
    }, 300);
}

// Add slideOutRight animation
const style = document.createElement('style');
style.textContent = `
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// ===== DROPDOWNS =====
function initDropdowns() {
    const dropdowns = document.querySelectorAll('.nav-dropdown');

    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('mouseenter', function() {
            this.classList.add('open');
        });

        dropdown.addEventListener('mouseleave', function() {
            this.classList.remove('open');
        });

        // Touch devices
        dropdown.addEventListener('touchstart', function(e) {
            e.preventDefault();
            this.classList.toggle('open');
        });
    });
}

// ===== ANIMATIONS =====
function initAnimations() {
    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
            }
        });
    }, observerOptions);

    // Observe elements that should animate
    document.querySelectorAll('.hover-lift, .card, .btn-primary').forEach(el => {
        observer.observe(el);
    });

    // Parallax effect for hero sections
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const parallaxElements = document.querySelectorAll('[data-parallax]');

        parallaxElements.forEach(el => {
            const speed = el.dataset.parallaxSpeed || 0.5;
            const yPos = -(scrolled * speed);
            el.style.transform = `translateY(${yPos}px)`;
        });
    });
}

// ===== NEWSLETTER FORM =====
function initNewsletter() {
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;

            // Here you would normally send to your backend
            console.log('Newsletter subscription:', email);

            // Show success message
            showMessage('success', 'Спасибо! Вы подписались на наши обновления.');

            // Reset form
            this.reset();
        });
    }
}

// ===== UTILITY FUNCTIONS =====
function showMessage(type, text) {
    const messagesContainer = document.querySelector('.messages-container');
    if (!messagesContainer) return;

    const message = document.createElement('div');
    message.className = `message message-${type}`;
    message.innerHTML = `
        <div class="message-icon">
            ${type === 'success' ? '<i class="fas fa-check-circle"></i>' :
              type === 'error' ? '<i class="fas fa-exclamation-circle"></i>' :
              type === 'warning' ? '<i class="fas fa-exclamation-triangle"></i>' :
              '<i class="fas fa-info-circle"></i>'}
        </div>
        <div class="message-content">
            <strong>${type === 'success' ? 'Успешно' : 
                     type === 'error' ? 'Ошибка' : 
                     type === 'warning' ? 'Внимание' : 'Информация'}</strong>
            <p>${text}</p>
        </div>
        <button class="message-close">&times;</button>
    `;

    messagesContainer.appendChild(message);
    initMessages(); // Re-initialize messages for new one
}

// ===== CURRENT YEAR =====
document.addEventListener('DOMContentLoaded', function() {
    const yearElement = document.querySelector('.footer-copyright');
    if (yearElement) {
        const currentYear = new Date().getFullYear();
        yearElement.innerHTML = yearElement.innerHTML.replace('2024', currentYear);
    }
});

// ===== TOUCH DEVICE DETECTION =====
function isTouchDevice() {
    return ('ontouchstart' in window) || (navigator.maxTouchPoints > 0);
}

if (isTouchDevice()) {
    document.body.classList.add('touch-device');
}

// ===== RESIZE HANDLER =====
let resizeTimer;
window.addEventListener('resize', function() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function() {
        // Close mobile menu on resize to desktop
        if (window.innerWidth >= 1024) {
            const menuToggle = document.getElementById('menuToggle');
            const mobileMenu = document.getElementById('mobileMenu');
            if (menuToggle && mobileMenu) {
                menuToggle.classList.remove('active');
                mobileMenu.classList.remove('active');
                document.body.style.overflow = '';
            }
        }
    }, 250);
});