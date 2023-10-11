from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, RedirectView, View
from django.contrib.auth.mixins import LoginRequiredMixin  
from django.views.generic.edit import UpdateView, DeleteView  
from .models import Articulo, Categoria, Perfil
from .forms import ArticuloForm, PerfilForm, RegistroUsuarioForm
from django.http import Http404

class PaginaPrincipalView(View):
    def get(self, request):
        es_administrador = is_admin(request.user)  
        context = {
            'es_administrador': es_administrador,
        }
        return render(request, 'index.html', context)


class RegistroUsuarioView(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'registrar_usuario.html'
    success_url = reverse_lazy('pagina-principal')

    def form_valid(self, form):
        messages.success(self.request, '¡Registro completado con éxito! Ahora puedes iniciar sesión.')
        return super().form_valid(form)


class InicioSesionView(FormView):
    form_class = AuthenticationForm
    template_name = 'inicio_sesion.html'
    success_url = reverse_lazy('pagina-principal')

    def form_valid(self, form):
        login(self.request, form.get_user())
        user = self.request.user
        messages.success(self.request, f'¡Bienvenido de nuevo, {user.username}!')
        return super().form_valid(form)


class CierreSesionView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, 'Has cerrado sesión con éxito.')
        return redirect(reverse_lazy('pagina-principal'))


class CrearArticuloView(LoginRequiredMixin, CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'crear_articulo.html'
    success_url = reverse_lazy('pagina-principal')

    def form_valid(self, form):
        # Set the author of the article to the currently logged-in user
        form.instance.autor = self.request.user
        # Rest of your existing code
        categoria_nombre = form.cleaned_data['categoria'].nombre
        categoria = get_object_or_404(Categoria, nombre=categoria_nombre)
        form.instance.categoria = categoria
        return super().form_valid(form)


class EditarArticuloView(LoginRequiredMixin, UpdateView):
    model = Articulo
    template_name = 'editar_articulo.html'
    form_class = ArticuloForm


class EliminarArticuloView(LoginRequiredMixin, DeleteView):
    model = Articulo
    template_name = 'eliminar_articulo.html'
    success_url = '/'  

def noticia_1 (req):

    return render(req, 'notica_1_futbol_argentino.html')

def noticia_2(req):

    return render(req, 'noticia_2_futbol_argentino.html')

def futbol_argentino(req):

    return render(req, 'futbol-argentino.html')

def seleccion_arg(req):
    return render(req, 'seleccion-arg.html')

def about(req):

    return render(req, 'about.html')

def editar_usuario(req):
    
    return render(req, 'editar-usuario.html')

def cambiar_contraseña(req):
    return render(req, 'cambiar-contraseña.html')

def is_admin(user):
    return user.is_staff

def noticia_detalle (req):
    return render(req, 'noticia_detalle.html')



def detalle_articulo(request, articulo_id):
    # Recuperar el artículo de la base de datos o mostrar un error si no existe
    articulo = Articulo.objects.get(pk=articulo_id)
    
    # Renderizar el template y pasar el artículo como contexto
    return render(request, 'noticia_detalle.html', {'articulo': articulo})


