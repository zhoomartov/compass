document.addEventListener('DOMContentLoaded', function() {
    // Animate tour cards
    const tourCards = document.querySelectorAll('.tour-card');
    tourCards.forEach((card, index) => {
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
    }, { threshold: 0.1 });
    
    tourCards.forEach(card => observer.observe(card));
    
    // Modal handling
    const bookingBtn = document.getElementById('bookingBtn');
    const bookingModal = document.getElementById('bookingModal');
    const modalClose = document.getElementById('modalClose');
    const modalOverlay = document.getElementById('modalOverlay');
    
    if (bookingBtn && bookingModal) {
        bookingBtn.addEventListener('click', function() {
            bookingModal.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
        
        function closeModal() {
            bookingModal.classList.remove('active');
            document.body.style.overflow = '';
        }
        
        if (modalClose) {
            modalClose.addEventListener('click', closeModal);
        }
        
        if (modalOverlay) {
            modalOverlay.addEventListener('click', closeModal);
        }
        
        // Close on Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && bookingModal.classList.contains('active')) {
                closeModal();
            }
        });
    }
    
    // Calculate total price
    const numberOfPeopleInput = document.getElementById('id_number_of_people');
    const totalAmountElement = document.getElementById('totalAmount');
    
    if (numberOfPeopleInput && totalAmountElement && typeof tourPrice !== 'undefined') {
        numberOfPeopleInput.addEventListener('input', function() {
            const people = parseInt(this.value) || 1;
            const total = tourPrice * people;
            totalAmountElement.textContent = '$' + total.toFixed(2);
        });
    }
    
    // Form validation
    const bookingForm = document.getElementById('bookingFormSubmit');
    if (bookingForm) {
        bookingForm.addEventListener('submit', function(e) {
            const inputs = this.querySelectorAll('input[required], textarea[required]');
            let isValid = true;
            
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.style.borderColor = '#ef4444';
                } else {
                    input.style.borderColor = 'var(--border-color)';
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                alert('Пожалуйста, заполните все обязательные поля');
            }
        });
    }
    
    // Filters auto-submit on change
    const filterSelects = document.querySelectorAll('.filter-select');
    filterSelects.forEach(select => {
        select.addEventListener('change', function() {
            const form = this.closest('form');
            if (form) {
                form.submit();
            }
        });
    });
});
