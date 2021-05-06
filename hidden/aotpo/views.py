from django.shortcuts import render, HttpResponse

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
            'Logout': '/logout'
        }
    }
    return render(request,'home.html', context)

def user(request):
    return render(request, 'user_profile.html')

def artwork(request):
    return render(request, 'artwork.html')

def register(request):
    return render(request, 'register.html')

def arena(request):
    return render(request, 'arena.html')

def gallery(request):
    return render(request, 'gallery.html')
