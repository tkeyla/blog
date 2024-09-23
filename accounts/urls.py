from django.urls import path
from .views import *

urlpatterns = [
    path('signup', crear_usuario, name='registro'),
]

