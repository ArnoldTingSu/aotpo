from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.http import HttpResponseRedirect
from .models import *
from django.contrib import messages
import json
import requests


# Create your views here.

def register_user(request):
    #pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(
    first_name = request.POST['first_name'], 
    last_name = request.POST['last_name'], 
    username = request.POST['username'], 
    email = request.POST['email'], 
    password = request.POST['password'],
    profile_pic = request.FILES['profile_pic']
    )
    request.session['user_id']  = user.id
    request.session['username'] = user.username
    messages.success(request, "You have Successfully Logged In")
    print('*'*50)
    print('user made')
    return redirect('/home')
        # print('*'*50)
        # print('user not made')
        # return redirect('/')
    # if request.method == "POST":
    #     errors = User.objects.user_validator(request.POST)
    #     if len(errors) > 0 :
    #         for key, value in errors.items():
    #             messages.error(request, value)
    #     else:
    #         password = request.POST['password']
    

def login_post(request):
    if request.method == "POST":
        user = User.objects.filter(username=request.POST['username'])
        if user:
            logged_user = user[0]
            if (request.POST['password'] == logged_user.password):
                request.session['user_id'] = logged_user.id
                return redirect('/home')
            messages.error(request, 'Password Does Not Match')
        else:
            messages.error(request, "Username Does Not Exist")
    return redirect('/login')


# <----------GET---------->

#LANDING PAGE(FIRST PAGE USERS SEE)
def landing(request):
    context = {
        'links': {
            'Home': '/home',
            'Arena': '/arena',
            'Hall of Fame': '/hall_of_fame',
        }
    }
    return render(request, 'landing.html', context)

def login(request):
    return render(request,'login.html')

def logout(request):
    request.session.flush()
    return redirect('/')

def home(request):
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
        "users" : User.objects.all(),
        "artworks": Art.objects.all(),
        "logged_user": User.objects.get(id = request.session['user_id']),
        "logged_user_art" : User.objects.get(id = request.session['user_id']).artworks.all(),
        "recent": Art.objects.order_by('-created_at')
    }
    return render(request, "home.html", context)

def hall_of_fame(request):
    context = {
        'links': {
            'Home': '/home',
            'Arena': '/arena',
            'Hall of Fame': '/hall_of_fame',
            'Logout': '/logout'
        }
    }
    return render(request, 'hall_of_fame.html', context)

def artist(request, id):
    context = {
        'artist': User.objects.get(id=id),
        "artworks": User.objects.get(id=id).artworks.all(),
        "logged_user": User.objects.get(id = request.session['user_id']),
        "logged_user_art" : User.objects.get(id = request.session['user_id']).artworks.all(),
        "recent": Art.objects.order_by('-created_at')
    }
    return render(request, 'user_profile.html', context)

def artwork(request, id):
    context = {
        'comments': Comment.objects.filter(artwork=id),
        'artwork': Art.objects.get(id=id),
        'artist': Art.objects.get(id=id).artist,
        'other_works': Art.objects.get(id=id).artist.artworks.all()
    }
    return render(request, 'artwork.html', context)

def register(request):
    return render(request, 'register.html')

def arena(request):
    context = {
        'left': Art.objects.order_by('?').first(),
        'right': Art.objects.order_by('?').first()
    }
    return render(request, 'arena.html', context)

def gallery(request, id):
    context = {
        'artist': User.objects.get(id=id),
        "artworks": User.objects.get(id=id).artworks.all(),
        }
    return render(request, 'gallery.html', context)

# <---------POST ---------->

#implementing art from The Met
def test(request):
    json_response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects")
    
    context = {
        'json': json_response
    }
    return render(request, 'test.html', context)

def vote(request):
    return ('arena')

def create_art(request):
    Art.objects.create(
    caption = request.POST['caption'],
    art_image = request.FILES['art_image'],
    artist = User.objects.get(id=request.session['user_id'])
    )
    print('Art Has Been Made')
    return redirect('/home')

def add_comment(request, id):
    if request.method == "POST":
       Comment.objects.create(
    comment = request.POST['comment'],
    artwork= Art.objects.get(id=id),
    user = User.objects.get(id=request.session['user_id'])
    )
    print('Comment Has Been Made')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
