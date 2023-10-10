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


def CrearArticuloView(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.instance.autor = request.user
            form.save()
            
            # Obtén la categoría seleccionada por el usuario
            categoria_seleccionada = form.cleaned_data['categoria']
            
            # Redirige a la página de categoría correspondiente
            if categoria_seleccionada.nombre == "Futbol Argentino":
                return redirect('futbol-argentino')  # Reemplaza 'categoria-futbol-argentino' con tu URL real
            elif categoria_seleccionada.nombre == "Seleccion Argentina":
                return redirect('seleccion-arg')  # Reemplaza 'categoria-seleccion-argentina' con tu URL real

    else:
        form = ArticuloForm()

    context = {
        'form': form
    }

    return render(request, 'crear_articulo.html', context)

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



def categoria(request, categoria_url):
    categoria = Categoria.objects.get(nombre__iexact=categoria_url.replace('-', ' '))
    articulos = Articulo.objects.filter(categoria=categoria)

    return render(request, 'tu_template_de_categoria.html', {'categoria': categoria, 'articulos': articulos})

def noticia_nueva(request):
    # Lógica para determinar la categoría seleccionada por el usuario,
    # supongamos que se almacena en una variable llamada 'categoria_elegida'
    categoria_elegida = request.GET.get('categoria')

    # Recupera el artículo más reciente de la categoría seleccionada
    nuevo_articulo = Articulo.objects.filter(categoria=categoria_elegida).latest('fecha_publicacion')

    # Recupera otros artículos de la misma categoría
    articulos = Articulo.objects.filter(categoria=categoria_elegida).exclude(id=nuevo_articulo.id)

    context = {
        'nuevo_articulo': nuevo_articulo,
        'articulos': articulos,
    }

    # Determina qué plantilla HTML renderizar en función de la categoría seleccionada
    if categoria_elegida == 'Futbol Argentino':
        template = 'futbol-argentino.html'
    elif categoria_elegida == 'Seleccion Argentina':
        template = 'seleccion_arg.html'
    else:
        # Manejo de caso de categoría no válida o por defecto
        template = 'WebApp/index.html'  # Puedes crear una plantilla de error personalizada

    return render(request, template, context)