from django.db import models
from django.urls import reverse #ummm idk
from django.contrib.auth.models import User #this is how you use users, not import from users, my mistake
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    """
    Models for the items in the database that will display on listings page.
    Should have capability to display image, name, and price, and a short description.
    """    
    image = models.ImageField(max_length=100, upload_to='itemimages/', null=False) #limits file names
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2) 
    #allows listings up to a million dollars... idk where we should cap this
    description = models.CharField(max_length=250, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    user = models.ForeignKey(User,on_delete=models.CASCADE,)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('item', kwargs={'pk': self.pk})
    
class Comment(models.Model):
    """
    Models for the comments on the items in the database that will display on the item page.
    Should have capability to display the comment, the user who posted it, and the item it is posted on.
    """    
    comment = models.CharField(max_length=250) #might be bad naming practice
    user = models.ForeignKey(User,on_delete=models.PROTECT,) #when the user is deleted, the comment is protected
    item = models.ForeignKey(Item,on_delete=models.CASCADE,)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user} on {self.item} at {self.date_posted}"
    
    def delete_text(self):
        self.comment = "This comment has been deleted."
        self.save()

    def get_absolute_url(self):
        return reverse('comment', kwargs={'pk': self.pk})
