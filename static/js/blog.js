document.addEventListener('DOMContentLoaded', function() {
    // Animate blog cards
    const blogCards = document.querySelectorAll('.blog-card');
    
    blogCards.forEach((card, index) => {
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
    
    blogCards.forEach(card => observer.observe(card));
    
    // Animate related posts
    const relatedPosts = document.querySelectorAll('.related-post-card');
    relatedPosts.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateX(-50px)';
        card.style.transition = `all 0.6s ease ${index * 0.1}s`;
    });
    
    relatedPosts.forEach(card => observer.observe(card));
    
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
    
    // Share buttons (simple implementation)
    const shareLinks = document.querySelectorAll('.share-link');
    shareLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const url = window.location.href;
            const title = document.querySelector('.post-title')?.textContent || document.title;
            
            // Simple share simulation
            if (navigator.share) {
                navigator.share({
                    title: title,
                    url: url
                }).catch(err => console.log('Error sharing:', err));
            } else {
                // Fallback: copy to clipboard
                navigator.clipboard.writeText(url).then(() => {
                    alert('Ссылка скопирована в буфер обмена!');
                });
            }
        });
    });
    
    // Animate post content on scroll
    const postContent = document.querySelector('.post-content');
    if (postContent) {
        const paragraphs = postContent.querySelectorAll('p');
        paragraphs.forEach((p, index) => {
            p.style.opacity = '0';
            p.style.transform = 'translateY(20px)';
            p.style.transition = `all 0.5s ease ${index * 0.05}s`;
        });
        
        paragraphs.forEach(p => observer.observe(p));
    }
});
