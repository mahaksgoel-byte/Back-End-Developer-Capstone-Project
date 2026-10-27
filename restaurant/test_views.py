from django.test import TestCase
from django.urls import reverse


class MenuViewTest(TestCase):

    def test_menu_api_get(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, 200)


class HomePageTest(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)