from django.contrib import admin
from .models import Destination, Tour, Booking, BlogPost, ContactMessage


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'featured', 'created_at']
    list_filter = ['featured', 'country', 'created_at']
    search_fields = ['name', 'country', 'description']
    list_editable = ['featured']


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['title', 'destination', 'price', 'duration_days', 'difficulty', 'available', 'featured', 'created_at']
    list_filter = ['difficulty', 'available', 'featured', 'destination', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['available', 'featured']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['tour', 'first_name', 'last_name', 'email', 'number_of_people', 'travel_date', 'status', 'total_price', 'created_at']
    list_filter = ['status', 'travel_date', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'tour__title']
    list_editable = ['status']
    readonly_fields = ['total_price', 'created_at']
    date_hierarchy = 'travel_date'


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published', 'featured', 'created_at']
    list_filter = ['published', 'featured', 'created_at']
    search_fields = ['title', 'content', 'author']
    list_editable = ['published', 'featured']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'read']
    list_filter = ['read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    list_editable = ['read']
    readonly_fields = ['created_at']
