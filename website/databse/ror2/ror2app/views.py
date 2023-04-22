from django.shortcuts import render
from .models import Items

# Create your views here.
def index(request):
    data= Items.objects.all()
    return render(request, "index.html", {'data' : data} )

