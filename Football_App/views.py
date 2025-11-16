from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def arena(request):
    return render(request, 'arena.html')

def booking(request):
    return render(request, 'booking.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def booking(request):
    return render(request, 'booking.html')

def logout(request):
    return render(request, 'logout.html')

def payment(request):
    return render(request, 'payment.html')

def profile(request):
    return render(request, 'profile.html')
  
