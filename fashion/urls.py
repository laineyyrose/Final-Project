from django.urls import path
from . import views
from users import views as userviews

urlpatterns = [
    path('', userviews.home, name='home'),
    path('weather/', views.weather, name='weather'),
]