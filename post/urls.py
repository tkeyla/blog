from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='home'),
    path('accounts/signup', views.crear_usuario, name='registro')
]