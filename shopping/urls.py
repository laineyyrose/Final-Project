from django.urls import path, include
from . import views
from users import views as userviews #this is to avoid conflicts, it fucks w the other views if not
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', userviews.home, name='home'),
    path('listings/', views.listings, name='listings'),
    path('listings/new/', views.add_item, name='add-item'),
    path('listings/<int:pk>/delete/', views.delete_item, name='delete-item'),
    path('item/<int:pk>', views.item, name='item'),
    path('item/add-comment', views.add_comment, name='add-comment')
] 
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)