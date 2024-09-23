from django.shortcuts import render
from .templates import *

def principal(request):
    return render(request, 'home.html')


