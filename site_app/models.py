from django.db import models
from django.utils import timezone


class Destination(models.Model):
    """Направления путешествий"""
    name = models.CharField(max_length=200, verbose_name='Название')
    country = models.CharField(max_length=100, verbose_name='Страна')
    description = models.TextField(verbose_name='Описание')
    image_url = models.URLField(blank=True, verbose_name='URL изображения')
    featured = models.BooleanField(default=False, verbose_name='Избранное')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'
        ordering = ['-featured', 'name']

    def __str__(self):
        return f"{self.name}, {self.country}"


class Tour(models.Model):
    """Туры"""
    DIFFICULTY_CHOICES = [
        ('easy', 'Легкий'),
        ('moderate', 'Средний'),
        ('hard', 'Сложный'),
    ]

    title = models.CharField(max_length=200, verbose_name='Название тура')
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name='tours',
        verbose_name='Направление'
    )
    description = models.TextField(verbose_name='Описание')
    duration_days = models.IntegerField(verbose_name='Продолжительность (дни)')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена (USD)')
    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default='moderate',
        verbose_name='Сложность'
    )
    max_group_size = models.IntegerField(verbose_name='Максимальный размер группы')
    image_url = models.URLField(blank=True, verbose_name='URL изображения')
    includes = models.TextField(blank=True, verbose_name='Что включено')
    itinerary = models.TextField(blank=True, verbose_name='Маршрут')
    available = models.BooleanField(default=True, verbose_name='Доступен')
    featured = models.BooleanField(default=False, verbose_name='Рекомендуемый')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'
        ordering = ['-featured', '-created_at']

    def __str__(self):
        return self.title


class Booking(models.Model):
    """Бронирования"""
    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('confirmed', 'Подтверждено'),
        ('cancelled', 'Отменено'),
    ]

    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='bookings',
        verbose_name='Тур'
    )
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    number_of_people = models.IntegerField(verbose_name='Количество человек')
    travel_date = models.DateField(verbose_name='Дата путешествия')
    message = models.TextField(blank=True, verbose_name='Сообщение')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Статус'
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Общая стоимость'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата бронирования')

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.tour.title}"

    def save(self, *args, **kwargs):
        if not self.total_price:
            self.total_price = self.tour.price * self.number_of_people
        super().save(*args, **kwargs)


class BlogPost(models.Model):
    """Блог"""
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL slug')
    content = models.TextField(verbose_name='Содержание')
    excerpt = models.TextField(max_length=300, verbose_name='Краткое описание')
    image_url = models.URLField(blank=True, verbose_name='URL изображения')
    author = models.CharField(max_length=100, default='Compass Travel', verbose_name='Автор')
    published = models.BooleanField(default=True, verbose_name='Опубликовано')
    featured = models.BooleanField(default=False, verbose_name='Избранное')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Статья блога'
        verbose_name_plural = 'Статьи блога'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    """Контактные сообщения"""
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=200, verbose_name='Тема')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    read = models.BooleanField(default=False, verbose_name='Прочитано')

    class Meta:
        verbose_name = 'Контактное сообщение'
        verbose_name_plural = 'Контактные сообщения'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"
