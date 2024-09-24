from django.urls import path
from .views import *

urlpatterns = [
    path('', principal, name='home'),
    path('crearpost', CrearPost.as_view(), name='crear_post'),
    path('verposteos/<str:autor>', VerPosteos.as_view(), name='ver_posteos'),
    path('misposteos', VerPosteosCreados.as_view(), name='mis_posteos'),
    path('post/<int:id>', ver_detalle, name='ver_post'),
    path('post/eliminar/<int:pk>', EliminarPost.as_view(), name='eliminar_post')
]