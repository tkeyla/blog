from django.shortcuts import render, redirect
from .templates import *
from django.contrib.auth.models import User
from .forms import *

def principal(request):
    return render(request, 'home.html')

def crear_usuario(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username, email, password)
            return redirect('login')
    else:
        form = SignUp()
        return render(request, 'registration/registro.html', {'form':form})



