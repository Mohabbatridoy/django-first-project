from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1> This is homepage</h1> <a href='contact/'>Contact Page</a> <a href='about/'>About</a>")

def contact(request):
    return HttpResponse("this is contact page <a href='/'>Homepage</a> <a href='/about/'>about</a>")
def about(request):
    return HttpResponse("this is about page <a href='/'>Homepage</a> <a href='/contact/'>contact</a>")