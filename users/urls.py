from django.urls import path
from . import views
from django.urls import path, include
from django.contrib.auth import logout
from .views import UserEditView, RegisterView

urlpatterns = [
    path('', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('home/', views.home, name='home'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.UserEditView.as_view(), name='edit_profile')

]