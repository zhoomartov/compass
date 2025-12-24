from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Destination, Tour, BlogPost
from .forms import BookingForm, ContactForm


def home(request):
    """Главная страница"""
    featured_tours = Tour.objects.filter(available=True, featured=True)[:6]
    featured_destinations = Destination.objects.filter(featured=True)[:9]
    recent_posts = BlogPost.objects.filter(published=True)[:6]

    context = {
        'featured_tours': featured_tours,
        'featured_destinations': featured_destinations,
        'recent_posts': recent_posts,
    }
    return render(request, 'site_app/home.html', context)


def about(request):
    """О нас"""
    return render(request, 'site_app/about.html')


def destinations(request):
    """Направления"""
    destinations_list = Destination.objects.all()

    search_query = request.GET.get('search', '')
    if search_query:
        destinations_list = destinations_list.filter(
            Q(name__icontains=search_query) |
            Q(country__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    context = {
        'destinations': destinations_list,
        'search_query': search_query,
    }
    return render(request, 'site_app/destinations.html', context)


def tours_list(request):
    """Список туров"""
    tours = Tour.objects.filter(available=True)

    # Фильтрация
    destination_id = request.GET.get('destination')
    difficulty = request.GET.get('difficulty')
    search_query = request.GET.get('search', '')

    if destination_id:
        tours = tours.filter(destination_id=destination_id)

    if difficulty:
        tours = tours.filter(difficulty=difficulty)

    if search_query:
        tours = tours.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(destination__name__icontains=search_query)
        )

    # Сортировка
    sort_by = request.GET.get('sort', 'featured')
    if sort_by == 'price_asc':
        tours = tours.order_by('price')
    elif sort_by == 'price_desc':
        tours = tours.order_by('-price')
    elif sort_by == 'duration':
        tours = tours.order_by('duration_days')

    destinations_for_filter = Destination.objects.all()

    context = {
        'tours': tours,
        'destinations': destinations_for_filter,
        'selected_destination': destination_id,
        'selected_difficulty': difficulty,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    return render(request, 'site_app/tours.html', context)


def tour_detail(request, tour_id):
    """Детальная страница тура"""
    tour = get_object_or_404(Tour, id=tour_id, available=True)
    related_tours = Tour.objects.filter(
        destination=tour.destination,
        available=True
    ).exclude(id=tour.id)[:3]

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.tour = tour
            booking.total_price = tour.price * booking.number_of_people
            booking.save()
            messages.success(request, 'Ваше бронирование успешно отправлено! Мы свяжемся с вами в ближайшее время.')
            return redirect('tour_detail', tour_id=tour.id)
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = BookingForm()

    context = {
        'tour': tour,
        'related_tours': related_tours,
        'form': form,
    }
    return render(request, 'site_app/tour_detail.html', context)


def special_offers(request):
    """Специальные предложения"""
    featured_tours = Tour.objects.filter(available=True, featured=True)

    context = {
        'featured_tours': featured_tours,
    }
    return render(request, 'site_app/offers.html', context)


def blog(request):
    """Блог"""
    posts = BlogPost.objects.filter(published=True)

    search_query = request.GET.get('search', '')
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(excerpt__icontains=search_query)
        )

    context = {
        'posts': posts,
        'search_query': search_query,
    }
    return render(request, 'site_app/blog.html', context)


def blog_post(request, slug):
    """Статья блога"""
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    recent_posts = BlogPost.objects.filter(published=True).exclude(slug=slug)[:4]

    context = {
        'post': post,
        'recent_posts': recent_posts,
    }
    return render(request, 'site_app/blog_post.html', context)


def contacts(request):
    """Контакты"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение успешно отправлено! Мы ответим вам в ближайшее время.')
            return redirect('contacts')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'site_app/contacts.html', context)
