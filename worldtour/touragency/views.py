from django.shortcuts import render
from. models import Tour


# Create your views here.
def index(response):
    return render(response,'index.html',)
def destination(response):
    tours = Tour.objects.all()
    context = {'tours': tours}
    return render(response,'destination.html',context)