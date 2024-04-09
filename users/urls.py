from django.urls import path
from . import views
from django.urls import path, include
from django.contrib.auth import logout

urlpatterns = [
    path('', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('logout', views.user_logout, name='logout'),
    
]