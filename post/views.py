from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
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
    success_url = reverse_lazy('mis_posteos')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class VerPosteos(ListView):
    model = Post
    template_name = 'listar_todos.html'
    context_object_name = 'posteos'

    def get_queryset(self):
        autor = self.request.GET.get('autor')
        if autor:
            return Post.objects.filter(autor__id=autor)
        else:
            return Post.objects.all()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SeleccionarAutor(self.request.GET or None)  
        return context
        

class VerPosteosCreados(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'listar_post_creados.html'
    context_object_name = 'posteos'

    def get_queryset(self):
        return Post.objects.filter(autor=self.request.user)
    
def ver_detalle(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'ver_post.html', {'post':post})

class EliminarPost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'confirmar_eliminacion.html'
    success_url = reverse_lazy('mis_posteos')

class EditarPost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['titulo', 'contenido']
    template_name = 'editar_post.html'
    success_url = reverse_lazy('mis_posteos')