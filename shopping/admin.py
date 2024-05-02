from django.apps import apps
from django.contrib import admin
from .models import Post, Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)

app = apps.get_app_config('shopping')

# Auto register all models using for loop
for model_name, model in app.models.items():
    admin.site.register(model)