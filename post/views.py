from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .templates import *

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




