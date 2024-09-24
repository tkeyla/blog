from django import forms
from django.contrib.auth.models import User

class SeleccionarAutor(forms.Form):
    autor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Seleccionar Autor",
        empty_label="Todos los autores", 
        required=False  
    )
