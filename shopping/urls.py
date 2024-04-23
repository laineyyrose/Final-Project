from django.urls import path
from . import views
from users import views

urlpatterns = [
    path('', views.home, name='home')
]