document.addEventListener('DOMContentLoaded', function() {
    // Animate offer cards
    const offerCards = document.querySelectorAll('.offer-card');
    
    offerCards.forEach((card, index) => {
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
    
    offerCards.forEach(card => observer.observe(card));
    
    // Animate benefit cards
    const benefitCards = document.querySelectorAll('.benefit-card');
    benefitCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'scale(0.9)';
        card.style.transition = `all 0.6s ease ${index * 0.1}s`;
    });
    
    benefitCards.forEach(card => observer.observe(card));
    
    // Newsletter form
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const emailInput = this.querySelector('input[type="email"]');
            if (emailInput && emailInput.value) {
                alert('Спасибо за подписку! Мы будем присылать вам лучшие предложения.');
                emailInput.value = '';
            }
        });
    }
    
    // Offer card click handler
    offerCards.forEach(card => {
        card.addEventListener('click', function(e) {
            if (!e.target.classList.contains('btn') && !e.target.closest('.btn')) {
                const link = this.querySelector('.btn');
                if (link) {
                    link.click();
                }
            }
        });
    });
});
