from django.db import models
from django.contrib.auth.models import User

class Post (models.Model):
    titulo = models.TextField(max_length=75)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_publicados')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Titulo: {self.titulo} - Contenido: {self.contenido} - Autor: {self.autor}"
