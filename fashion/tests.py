from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class WeatherTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/weather/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("weather"))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse("weather"))
        self.assertTemplateUsed(response, "weather.html")