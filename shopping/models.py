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
    
    def get_absolute_url(self): #todo - this actually
        return reverse("item_detail", kwargs={"pk": self.pk})