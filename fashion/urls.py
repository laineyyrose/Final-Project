from django.urls import path, include
from . import views

urlpatterns = [
    path('thrift_map/', views.thrift_map, name='thrift_map'),
]