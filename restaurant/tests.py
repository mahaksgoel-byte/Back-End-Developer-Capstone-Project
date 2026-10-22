from datetime import date, time, timedelta
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from .models import Booking, MenuItem


class CapstoneApiTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="reviewer", password="A-Strong-Test-Password-42!")
        self.token = Token.objects.create(user=self.user)

    def test_home_page_is_served(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Little Lemon")

    def test_menu_read_is_public_and_writes_require_authentication(self):
        MenuItem.objects.create(title="Bruschetta", price="8.50", category="Starters")
        self.assertEqual(self.client.get("/api/menu/").status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.post("/api/menu/", {}).status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_menu_crud(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        response = self.client.post("/api/menu/", {"title": "Pasta", "price": "14.00", "category": "Mains"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        item_id = response.data["id"]
        self.assertEqual(self.client.patch(f"/api/menu/{item_id}/", {"price": "15.00"}).status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.delete(f"/api/menu/{item_id}/").status_code, status.HTTP_204_NO_CONTENT)

    def test_registration_and_token_login(self):
        response = self.client.post("/api/registration/", {"username": "newuser", "password": "A-Strong-Test-Password-43!"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotIn("password", response.data)
        response = self.client.post("/api/token/login/", {"username": "newuser", "password": "A-Strong-Test-Password-43!"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)

    def test_booking_auth_validation_and_owner_scope(self):
        self.assertEqual(self.client.get("/api/bookings/").status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        path = "/api/bookings/"
        payload = {"name": "Ada", "no_of_guests": 2, "booking_date": (date.today() + timedelta(days=1)).isoformat(), "booking_time": "18:30:00"}
        response = self.client.post(path, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(self.client.post(path, payload).status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.client.post(path, {**payload, "no_of_guests": 0, "booking_time": "19:30:00"}).status_code, status.HTTP_400_BAD_REQUEST)
