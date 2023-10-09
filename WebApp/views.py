from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, RedirectView, View
from django.contrib.auth.mixins import LoginRequiredMixin  
from django.views.generic.edit import UpdateView, DeleteView  
from .models import Articulo, Categoria, Perfil
from .forms import ArticuloForm, PerfilForm, RegistroUsuarioForm


class PaginaPrincipalView(View):
    def get(self, request):
        return render(request, 'index.html')
# Vista para registrar un nuevo usuario
class RegistroUsuarioView(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'registrar_usuario.html'
    success_url = reverse_lazy('pagina-principal')

    def form_valid(self, form):
        messages.success(self.request, f'¡La cuenta de {form.cleaned_data["username"]} ha sido creada! Ahora puedes iniciar sesión.')
        return super().form_valid(form)

# Vista para el inicio de sesión
class InicioSesionView(FormView):
    form_class = AuthenticationForm
    template_name = 'inicio_sesion.html'
    success_url = 'pagina-principal'

    def form_valid(self, form):
        login(self.request, form.get_user())
        user = self.request.user  # Obtener el usuario que ha iniciado sesión
        messages.success(self.request, f'¡Bienvenido de nuevo, {user.username}!')
        return super().form_valid(form)
# Vista para el cierre de sesión
class CierreSesionView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, 'Has cerrado sesión con éxito.')
        return redirect(reverse_lazy('pagina-principal'))

# Vista para crear un nuevo artículo
class CrearArticuloView(LoginRequiredMixin, CreateView):
    model = Articulo
    template_name = 'crear_articulo.html'
    form_class = ArticuloForm

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

# Vista para editar un artículo existente
class EditarArticuloView(LoginRequiredMixin, UpdateView):
    model = Articulo
    template_name = 'editar_articulo.html'
    form_class = ArticuloForm

# Vista para eliminar un artículo existente
class EliminarArticuloView(LoginRequiredMixin, DeleteView):
    model = Articulo
    template_name = 'eliminar_articulo.html'
    success_url = '/'  # Redirigir a la página de inicio después de eliminar un artículo


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
