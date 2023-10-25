from django.contrib import admin
from .models import Articulo, Categoria, InfoExtra
from .forms import ArticuloFormulario, Categoria

    # Registro del modelo Articulo con el formulario ArticuloForm
@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria')

# Registro del modelo Perfil con el formulario PerfilForm
@admin.register(InfoExtra)
class InfoExtraAdmin(admin.ModelAdmin):
    search_fields = ('user', 'es_admin', 'link')
    list_display = ('user', 'es_admin', 'link', 'avatar')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin): 
    list_display = ('nombre',)
