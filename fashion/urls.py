from django.urls import path, include
from . import views
from users import views as userviews #this is to avoid conflicts

urlpatterns = [
    path('weather/', views.weather, name='weather'),
    path('thrift_map/', views.thrift_map, name='thrift_map'),
    path('color_picker/', views.color_picker, name='color_picker'),
]