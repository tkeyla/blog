from django.urls import path
from .views import *

urlpatterns = [
    path('', principal, name='home'),
    path('crearpost', CrearPost.as_view(), name='crear_post')
]