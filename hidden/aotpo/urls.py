from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('home', views.home),
    path('login', views.login),
    path('register', views.register),
    path('register_user', views.register_user),
    path('user', views.user),
    path('artwork', views.artwork),
    path('arena', views.arena),
    path('gallery', views.gallery),
    path('hall_of_fame', views.hall_of_fame),
    path('create_art', views.create_art)
]