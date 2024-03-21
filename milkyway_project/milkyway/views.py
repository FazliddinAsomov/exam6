from django.shortcuts import render
from .models import Galaxy

def home(request):
    galaxies = Galaxy.objects.all()
    return render(request, 'milkyway/home.html', {'galaxies': galaxies})

def about(request):
    return render(request, 'milkyway/about.html')
