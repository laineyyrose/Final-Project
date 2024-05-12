from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse
from .models import Item, Comment
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import AddItem, EditItem, AddComment

# Create your tests here.

class ItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username='testuser')
        Item.objects.create(
            image='itemimages/test_image.jpg',
            name='Test Item',
            price=9.99,
            description='This is a test item',
            date_posted=timezone.now(),
            user=user
        )

    def test_name_label(self):
        item = Item.objects.get(id=1)
        field_label = item._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_price_max_digits(self):
        item = Item.objects.get(id=1)
        max_digits = item._meta.get_field('price').max_digits
        self.assertEqual(max_digits, 9)

    def test_description_null(self):
        item = Item.objects.get(id=1)
        null = item._meta.get_field('description').null
        self.assertEqual(null, True)

    def test_get_absolute_url(self):
        item = Item.objects.get(id=1)
        url = item.get_absolute_url()
        self.assertEqual(url, '/item/1')

class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create an item
        item = Item.objects.create(name='Test Item', price=10.99)
        
        # Create a comment
        Comment.objects.create(comment='Test comment', user=user, item=item, date_posted=timezone.now())
    
    def test_comment_str_representation(self):
        comment = Comment.objects.get(id=1)
        expected_str = f"{comment.user} on {comment.item} at {comment.date_posted}"
        self.assertEqual(str(comment), expected_str)
    
    def test_comment_delete_text(self):
        comment = Comment.objects.get(id=1)
        comment.delete_text()
        self.assertEqual(comment.comment, "This comment has been deleted.")
    
    def test_comment_absolute_url(self):
        comment = Comment.objects.get(id=1)
        expected_url = f"/comment/{comment.pk}/"
        self.assertEqual(comment.get_absolute_url(), expected_url)


# VIEWS TESTS

#TODO - go back and make sure this is a proper test lol
class ListingsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create some test items
        Item.objects.create(name='Item 1', price=10)
        Item.objects.create(name='Item 2', price=20)
        Item.objects.create(name='Item 3', price=30)

    def test_listings_get(self):
        response = self.client.get(reverse('listings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopping/listings.html')
        self.assertQuerysetEqual(response.context['item_display'], ['<Item: Item 1>', '<Item: Item 2>', '<Item: Item 3>'])

    def test_listings_filter_by_min_price(self):
        response = self.client.get(reverse('listings'), {'min_price': 15})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopping/listings.html')
        self.assertQuerysetEqual(response.context['item_display'], ['<Item: Item 2>', '<Item: Item 3>'])

    def test_listings_filter_by_max_price(self):
        response = self.client.get(reverse('listings'), {'max_price': 25})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopping/listings.html')
        self.assertQuerysetEqual(response.context['item_display'], ['<Item: Item 1>', '<Item: Item 2>'])

    def test_listings_filter_by_min_and_max_price(self):
        response = self.client.get(reverse('listings'), {'min_price': 15, 'max_price': 25})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopping/listings.html')
        self.assertQuerysetEqual(response.context['item_display'], ['<Item: Item 2>'])

    def test_listings_post(self):
        response = self.client.post(reverse('listings'))
        self.assertEqual(response.status_code, 405)  # Method Not Allowed

    def test_listings_unauthenticated(self):
        self.client.logout()
        response = self.client.get(reverse('listings'))
        self.assertEqual(response.status_code, 302)  # Redirect to login page
        self.assertRedirects(response, '/accounts/login/?next=/listings/')

class ItemViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create an item
        item = Item.objects.create(name='Test Item', price=10.99)
        
        # Create comments
        Comment.objects.create(comment='Test comment 1', user=user, item=item, date_posted=timezone.now())
        Comment.objects.create(comment='Test comment 2', user=user, item=item, date_posted=timezone.now())
    
    def test_item_view(self):
        client = Client()
        item = Item.objects.get(id=1)
        url = reverse('item', args=[item.pk])
        response = client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopping/item.html')
        self.assertEqual(response.context['item'], item)
        self.assertEqual(len(response.context['comments']), 2)
        self.assertEqual(response.context['editform'].instance, item)