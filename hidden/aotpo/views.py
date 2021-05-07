from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.

# <----------GET---------->
#LANDING PAGE(FIRST PAGE USERS SEE)
def landing(request):
    context = {
        'links': {
            'Home': '/home',
            'Arena': '/arena',
            'Hall of Fame': '/hall_of_fame',
            'Logout': '/logout'
        }
    }
    return render(request, 'landing.html', context)

def login(request):
    return render(request,'login.html')

def home(request):
    context = {
        'links': {
            'Home': '/home',
            'Arena': '/arena',
            'Hall of Fame': '/hall_of_fame',
            'Logout': '/logout',
    
        'user': {
            'session' : User.objects.get(id=request.session['user_id'])
            }
        }  
    }  
    return render(request,'home.html', context)

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

def user(request):
    return render(request, 'user_profile.html')

def artwork(request):
    return render(request, 'artwork.html')

def register(request):
    return render(request, 'register.html')

def arena(request):
    context = {
        'links': {
            'Home': '/home',
            'Arena': '/arena',
            'Hall of Fame': '/hall_of_fame',
            'Logout': '/logout'
        }
    }
    return render(request, 'arena.html', context)

def gallery(request):
    context = {
        'links': {
            'Home': '/home',
            'Arena': '/arena',
            'Hall of Fame': '/hall_of_fame',
            'Logout': '/logout'
        }
    }
    return render(request, 'gallery.html', context)

# <---------POST ---------->

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

def create_art(request):
    Art.objects.create(
    caption = request.POST['caption'],
    art_image = request.FILES['art_image'],
    artist = User.objects.get(id=request.session['user_id'])
    )
    print('Art Has Been Made')
    return redirect('/home')