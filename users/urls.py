from django.urls import path
from .views import UserRegisterView, UserEditView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from . import views
#from django.urls import path, include
#from django.contrib.auth import logout
#from .views import UserEditView, RegisterView, ShowProfilePageView, EditProfilePageView

#app_name = 'users'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
    #path('', views.home, name='home'),
    #path('', include('django.contrib.auth.urls')),
    #path('home/', views.home, name='home'),
    #path('sign-up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout_view, name='logout')
    #path('register/', views.RegisterView.as_view(), name='register'),
    #path('profile/', views.profile, name='profile'),
    #path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    #path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    #path('edit-profile/', views.UserEditView.as_view(), name='edit_profile'),
    #path('fashion/', include('fashion.urls'))
]