from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from .views import home


class HomePageTester(TestCase):
    def test_home_view_status(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)