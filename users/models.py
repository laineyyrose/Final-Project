from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    def user_directory_path(instance, filename):
        return f'media/userprofiles/{instance.user.username}/{filename}'
    
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=50, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to=user_directory_path, default='userprofiles/default.jpg')
    venmo_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)