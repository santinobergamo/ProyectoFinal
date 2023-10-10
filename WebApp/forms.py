from django.contrib.auth.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
    # Agrega un campo de selección para el rol
    ROLES_CHOICES = (
        ('user', 'Usuario Normal'),
        ('admin', 'Administrador'),
    )
    rol = forms.ChoiceField(choices=ROLES_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'rol']

class CustomAuthenticationForm(AuthenticationForm):
    pass
