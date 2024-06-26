from django.urls import path
from . import views

urlpatterns = [
    path('gallery', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add', views.addPhoto, name='add'),
]