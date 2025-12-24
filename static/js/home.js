document.addEventListener('DOMContentLoaded', function() {
    // Элементы модального окна
    const modal = document.getElementById('quickBookModal');
    const closeModal = document.querySelector('.close-modal');
    const quickBookButtons = document.querySelectorAll('.quick-book');
    const quickBookForm = document.getElementById('quickBookForm');
    
    // Открытие модального окна
    quickBookButtons.forEach(button => {
        button.addEventListener('click', function() {
            const tourId = this.getAttribute('data-tour-id');
            document.getElementById('tourId').value = tourId;
            
            // Анимация открытия
            modal.style.display = 'block';
            setTimeout(() => {
                modal.querySelector('.modal-content').style.opacity = '1';
                modal.querySelector('.modal-content').style.transform = 'translateY(0)';
            }, 10);
        });
    });
    
    // Закрытие модального окна
    closeModal.addEventListener('click', closeModalWindow);
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            closeModalWindow();
        }
    });
    
    function closeModalWindow() {
        const modalContent = modal.querySelector('.modal-content');
        modalContent.style.opacity = '0';
        modalContent.style.transform = 'translateY(-50px)';
        
        setTimeout(() => {
            modal.style.display = 'none';
        }, 300);
    }
    
    // Отправка формы быстрого бронирования
    if (quickBookForm) {
        quickBookForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const submitButton = this.querySelector('.submit-button');
            const originalText = submitButton.textContent;
            
            // Показываем загрузку
            submitButton.textContent = 'Отправка...';
            submitButton.disabled = true;
            
            // Отправляем данные через AJAX
            fetch('/quick-book/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': getCookie('csrftoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Показываем успех
                    submitButton.textContent = '✓ Успешно!';
                    submitButton.style.background = '#4CAF50';
                    
                    // Закрываем модальное окно через 2 секунды
                    setTimeout(() => {
                        closeModalWindow();
                        showNotification('Заявка успешно отправлена! Мы вам перезвоним.', 'success');
                        
                        // Восстанавливаем кнопку
                        setTimeout(() => {
                            submitButton.textContent = originalText;
                            submitButton.style.background = '';
                            submitButton.disabled = false;
                            quickBookForm.reset();
                        }, 500);
                    }, 2000);
                } else {
                    // Показываем ошибку
                    submitButton.textContent = '✗ Ошибка';
                    submitButton.style.background = '#f44336';
                    
                    setTimeout(() => {
                        submitButton.textContent = originalText;
                        submitButton.style.background = '';
                        submitButton.disabled = false;
                        showNotification(data.message || 'Ошибка отправки', 'error');
                    }, 2000);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                submitButton.textContent = originalText;
                submitButton.disabled = false;
                showNotification('Ошибка соединения', 'error');
            });
        });
    }
    
    // Анимация статистики
    function animateStats() {
        const statNumbers = document.querySelectorAll('.stat-number');
        statNumbers.forEach(stat => {
            const finalValue = parseInt(stat.textContent);
            let currentValue = 0;
            const increment = finalValue / 100;
            const timer = setInterval(() => {
                currentValue += increment;
                if (currentValue >= finalValue) {
                    stat.textContent = finalValue;
                    clearInterval(timer);
                } else {
                    stat.textContent = Math.floor(currentValue);
                }
            }, 20);
        });
    }
    
    // Запуск анимации статистики при скролле
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateStats();
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    const statsSection = document.querySelector('.stats-section');
    if (statsSection) {
        observer.observe(statsSection);
    }
    
    // Параллакс эффект для героя
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const hero = document.querySelector('.hero-section');
        if (hero) {
            hero.style.backgroundPositionY = scrolled * 0.5 + 'px';
        }
    });
    
    // Плавная прокрутка к якорям
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            if (this.getAttribute('href') !== '#') {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                const targetElement = document.querySelector(targetId);
                
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 80,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
    
    // Обработка формы подписки на новости
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;
            
            fetch('/subscribe/', {
                method: 'POST',
                body: JSON.stringify({ email: email }),
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showNotification('Вы успешно подписались!', 'success');
                    this.reset();
                } else {
                    showNotification(data.message || 'Ошибка подписки', 'error');
                }
            })
            .catch(error => {
                showNotification('Ошибка соединения', 'error');
            });
        });
    }
    
    // Всплывающие уведомления
    function showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.classList.add('show');
        }, 10);
        
        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => {
                document.body.removeChild(notification);
            }, 300);
        }, 3000);
    }
    
    // Стили для уведомлений
    const style = document.createElement('style');
    style.textContent = `
        .notification {
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px 25px;
            border-radius: 5px;
            color: white;
            font-weight: 500;
            transform: translateX(400px);
            transition: transform 0.3s ease;
            z-index: 10000;
        }
        
        .notification.show {
            transform: translateX(0);
        }
        
        .notification.success {
            background: #4CAF50;
        }
        
        .notification.error {
            background: #f44336;
        }
        
        .notification.info {
            background: #2196F3;
        }
    `;
    document.head.appendChild(style);
    
    // Вспомогательная функция для получения CSRF токена
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    // Инициализация карусели (если будет добавлена)
    function initCarousel() {
        const carousels = document.querySelectorAll('.carousel');
        carousels.forEach(carousel => {
            let currentSlide = 0;
            const slides = carousel.querySelectorAll('.carousel-slide');
            const totalSlides = slides.length;
            
            function showSlide(n) {
                slides.forEach(slide => slide.style.display = 'none');
                slides[n].style.display = 'block';
            }
            
            function nextSlide() {
                currentSlide = (currentSlide + 1) % totalSlides;
                showSlide(currentSlide);
            }
            
            // Автопрокрутка каждые 5 секунд
            setInterval(nextSlide, 5000);
            showSlide(currentSlide);
        });
    }
    
    // Вызываем инициализацию карусели
    initCarousel();
});