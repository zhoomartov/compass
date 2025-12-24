from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('destinations/', views.destinations, name='destinations'),
    path('tours/', views.tours_list, name='tours'),
    path('tours/<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('offers/', views.special_offers, name='offers'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_post, name='blog_post'),
    path('contacts/', views.contacts, name='contacts'),
]
