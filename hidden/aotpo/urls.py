from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('login', views.login),
    path('register', views.register),
    path('home', views.home),
    path('user_profile', views.user_profile),
    path('artwork_profile', views.artwork_profile)
]