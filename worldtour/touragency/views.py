from django.shortcuts import render

# Create your views here.
def index(response):
    return render(response,'index.html')
def packages(response):
    return render(response,'packages.html')
def destination(response):
    return render(response,'destination.html')