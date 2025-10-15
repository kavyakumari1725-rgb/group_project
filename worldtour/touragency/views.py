from django.shortcuts import render

# Create your views here.
def index(response):
    return render(response,'index.html')
def about_us(response):
    return render(response,'about_us.html')