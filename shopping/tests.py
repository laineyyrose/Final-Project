from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from .models import Item


# Create your tests here.

class ListingsViewTest(TestCase):
    def test_listings_view(self):
        # Create some test items
        item1 = Item.objects.create(title='Item 1', description='Description 1')
        item2 = Item.objects.create(title='Item 2', description='Description 2')

        # Make a GET request to the listings view
        response = self.client.get(reverse('listings'))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the items' titles
        self.assertContains(response, item1.title)
        self.assertContains(response, item2.title)

        # Check that the items are displayed in descending order of date posted
        items_display = response.context['items_display']
        self.assertEqual(items_display[0], item2)
        self.assertEqual(items_display[1], item1)

    def test_listings_view_no_items(self):
        # Make a GET request to the listings view when there are no items
        response = self.client.get(reverse('listings'))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the message for no postings
        self.assertContains(response, "No postings right now. Why not add something of your own?")