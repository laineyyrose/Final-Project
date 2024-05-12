from django.urls import path, include
from . import views
from users import views as userviews #this is to avoid conflicts, it fucks w the other views if not
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView

urlpatterns = [
    path('listings/', views.listings, name='listings'),
    path('listings/new/', views.add_item, name='add-item'),
    path('listings/<int:pk>/delete/', views.delete_item, name='delete-item'),
    path('item/<int:pk>', views.item, name='item'),
    path('item/<int:pk>/edit', views.edit_item, name='edit-item'),
    path('item/comment/add/<int:pk>/', views.add_comment, name='add-comment'),
    path('item/comment/delete/<int:pk>/', views.delete_comment, name='delete-comment'),
    path('home/', HomeView.as_view(), name="home_page")
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)