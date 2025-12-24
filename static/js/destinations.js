document.addEventListener('DOMContentLoaded', function() {
    // Animate destination cards on scroll
    const destinationCards = document.querySelectorAll('.destination-card');
    
    destinationCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(50px)';
        card.style.transition = `all 0.6s ease ${index * 0.1}s`;
    });
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    destinationCards.forEach(card => observer.observe(card));
    
    // Destination card click handler
    destinationCards.forEach(card => {
        card.addEventListener('click', function(e) {
            if (!e.target.classList.contains('btn') && !e.target.closest('.btn')) {
                const link = this.querySelector('.btn');
                if (link) {
                    link.click();
                }
            }
        });
    });
    
    // Search form enhancement
    const searchInput = document.querySelector('.search-input');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            if (this.value.length > 0) {
                this.style.borderColor = 'var(--primary-color)';
            } else {
                this.style.borderColor = 'var(--border-color)';
            }
        });
    }
});
