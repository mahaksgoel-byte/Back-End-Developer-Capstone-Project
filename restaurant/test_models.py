from django.test import TestCase

from .models import Menu, Booking


class MenuModelTest(TestCase):

    def test_menu_model_exists(self):
        self.assertTrue(Menu)


class BookingModelTest(TestCase):

    def test_booking_model_exists(self):
        self.assertTrue(Booking)