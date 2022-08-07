from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.getRoutes),
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>', views.getRoom),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
