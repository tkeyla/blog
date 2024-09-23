from django.urls import path
from .views import *

urlpatterns = [
    path('', principal, name='home'),
    path('accounts/signup', crear_usuario, name='registro'),
    path('crearpost', CrearPost.as_view(), name='crear_post')
]