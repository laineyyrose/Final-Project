from django.urls import path
from . import views
from users import views as userviews #this is to avoid conflicts, it fucks w the other views if not

urlpatterns = [
    path('', userviews.home, name='home'),
    path('listings/', views.listings, name='listings'),
]