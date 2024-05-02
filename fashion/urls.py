from django.urls import path, include
from . import views
from users import views as userviews

urlpatterns = [
    path('', userviews.home, name='home'),
    path('weather/', views.weather, name='weather'),
    path('thrift_map/', views.thrift_map, name='thrift_map'),
]