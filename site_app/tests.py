from django.test import TestCase
from .models import Destination, Tour, Booking, BlogPost, ContactMessage
from decimal import Decimal


class DestinationModelTest(TestCase):
    def test_string_representation(self):
        destination = Destination(name="Иссык-Куль", country="Кыргызстан")
        self.assertEqual(str(destination), "Иссык-Куль, Кыргызстан")


class TourModelTest(TestCase):
    def setUp(self):
        self.destination = Destination.objects.create(
            name="Иссык-Куль",
            country="Кыргызстан",
            description="Красивое озеро"
        )
    
    def test_string_representation(self):
        tour = Tour(title="Тур на Иссык-Куль", destination=self.destination)
        self.assertEqual(str(tour), "Тур на Иссык-Куль")


class BookingModelTest(TestCase):
    def setUp(self):
        self.destination = Destination.objects.create(
            name="Иссык-Куль",
            country="Кыргызстан",
            description="Красивое озеро"
        )
        self.tour = Tour.objects.create(
            title="Тур на Иссык-Куль",
            destination=self.destination,
            description="Отличный тур",
            duration_days=5,
            price=Decimal('500.00'),
            max_group_size=10
        )
    
    def test_total_price_calculation(self):
        booking = Booking.objects.create(
            tour=self.tour,
            first_name="Иван",
            last_name="Иванов",
            email="ivan@test.com",
            phone="+996700123456",
            number_of_people=2,
            travel_date="2024-06-01"
        )
        self.assertEqual(booking.total_price, Decimal('1000.00'))
