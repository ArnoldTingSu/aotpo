from django.shortcuts import render, HttpResponse

# Create your views here.

# <----------GET---------->
#LANDING PAGE(FIRST PAGE USERS SEE)
def landing(request):
    return render(request, 'landing.html')

def login(request):
    return render(request,'register.html')

def home(request):
    return render(request,'home.html')

def user_profile(request):
    return render(request, 'user_profile.html')

def artwork_profile(request):
    return render(request, 'artwork_profile.html')

def register(request):
    return render(request, 'register.html')