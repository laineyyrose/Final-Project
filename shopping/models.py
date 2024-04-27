from django.db import models
from users import models #this is so we can assign a user to a post
from django.urls import reverse #ummm idk

# Create your models here.
class Item(models.Model):
    """
    Models for the items in the database that will display on listings page.
    Should have capability to display image, name, and price, and a short description.
    """    
    image = models.ImageField(max_length=100) #limits file names
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2) 
    #allows listings up to a million dollars... idk where we should cap this
    description = models.CharField(max_length=250, null=True)

    """
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    """

    def __str__(self):
        return self.name
    
    def get_absolute_url(self): #todo - this actually
        return reverse("item_detail", kwargs={"pk": self.pk})