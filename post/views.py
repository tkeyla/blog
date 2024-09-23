from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .templates import *
from .forms import *
from .models import *

def principal(request):
    return render(request, 'home.html')

class CrearPost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titulo', 'contenido']
    template_name = 'crear_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


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



