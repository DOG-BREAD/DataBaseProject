from django.shortcuts import render

from .models import *
# Create your views here.
def index(request):
    data= Items.objects.all()
    return render(request, "index.html", {'data' : data} )

def enemies(request):
    data = Enemies.objects.all()
    return render(request, "enemies.html", {'data': data})

def environment(request):
    data = Environment.objects.all()
    return render(request, "enviroment.html", {'data': data})

def home(request):

    return render(request, "home.html" )