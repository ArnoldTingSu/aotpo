from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('home', views.home),
    path('login', views.login),
    path('register', views.register),
    path('register_user', views.register_user),
    path('artist/<int:id>', views.artist),
    path('artwork/<int:id>', views.artwork),
    path('arena', views.arena),
    path('artwork/<int:id>/add_comment', views.add_comment),
    path('artist/<int:id>/gallery', views.gallery),
    path('hall_of_fame', views.hall_of_fame),
    path('create_art', views.create_art),
    path('logout', views.logout),
    path('login-post', views.login_post),
    path('vote', views.vote)
]