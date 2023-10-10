from django.contrib import admin
from .models import Articulo, Perfil, Categoria
from .forms import ArticuloForm, PerfilForm, Categoria

    # Registro del modelo Articulo con el formulario ArticuloForm
@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    form = ArticuloForm  # Asigna el formulario personalizado ArticuloForm
    list_display = ('titulo', 'autor', 'fecha_publicacion')

# Registro del modelo Perfil con el formulario PerfilForm
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    form = PerfilForm  # Asigna el formulario personalizado PerfilForm

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin): 
    list_display = ('nombre',)
