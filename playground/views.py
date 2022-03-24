from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    x = 1
    y = 4
    
    return render(request, 'index.html')

