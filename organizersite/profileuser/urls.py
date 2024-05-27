from django.urls import path
from . import views
urlpatterns = [
    path('main', views.main, name='main'),
    path('', views.home, name='home'),
    path('registration', views.register_view, name='registration'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    ]