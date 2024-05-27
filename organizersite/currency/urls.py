from django.urls import path

from currency import views

urlpatterns = [
    path('currency', views.convert_currency, name='convert_currency'),
]