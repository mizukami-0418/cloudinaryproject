# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('album/new/', views.create_album, name='create_album'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
]