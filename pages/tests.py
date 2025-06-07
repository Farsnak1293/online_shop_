from django.test import TestCase
from django.urls import reverse

class PagesTests(TestCase):

    def test_homepage_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_aboutus_status_code(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_aboutus_template(self):
        response = self.client.get(reverse('aboutus'))
        self.assertTemplateUsed(response, 'pages/aboutus.html')

    def test_aboutus_content(self):
        response = self.client.get(reverse('aboutus'))
        self.assertContains(response, "about us")

    def test_homepage_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "home page")  # این رو به محتوای واقعی صفحه تغییر بده



