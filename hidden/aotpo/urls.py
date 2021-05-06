from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('home', views.home),
    path('login', views.login),
    path('register', views.register),
    path('user', views.user),
    path('artwork', views.artwork),
    path('arena', views.arena),
    path('gallery', views.gallery)
]