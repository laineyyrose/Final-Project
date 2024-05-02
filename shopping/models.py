from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')
    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=50, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/userprofiles/')
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)
    venmo_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    