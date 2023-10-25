from django.contrib.auth.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django import forms
from .models import *


class ArticuloFormulario(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['categoria', 'titulo', 'subtitulo', 'contenido', 'imagen']

        contenido = forms.CharField(widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super(ArticuloFormulario, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'




class FormularioDeRegistro(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {campo: '' for campo in fields}

class FormularioDeEditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(label='Cambiar email')
    first_name = forms.CharField(label='Nombre', max_length=30)
    last_name = forms.CharField(label='Apellido', max_length=50)
    link = forms.URLField(required=False)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'link', 'avatar']
        
    def __init__(self, *args, **kwargs):
        super(FormularioDeEditarPerfil, self).__init__(*args, **kwargs)
        
        # Aplicar clases CSS a los widgets de los campos
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
class CambiarPasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        
    def __init__(self, *args, **kwargs):
        super(CambiarPasswordForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class CustomAuthenticationForm(AuthenticationForm):
    pass
