from django.contrib.auth.models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'categoria', 'imagen']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['descripcion', 'avatar']

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
