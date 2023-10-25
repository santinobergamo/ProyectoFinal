from django.contrib.auth import login as django_login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, RedirectView, View
from django.contrib.auth.mixins import LoginRequiredMixin  
from django.views.generic.edit import UpdateView, DeleteView  
from .models import Articulo, Categoria, Perfil
from .forms import *
from django.http import Http404
from django.contrib.auth.views import PasswordChangeView

class PaginaPrincipalView(View):
    def get(self, request):
        es_administrador = is_admin(request.user)  
        context = {
            'es_administrador': es_administrador,
        }
        return render(request, 'index.html', context)

# Create your views here.
def login(request):
    error_message = None
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            
            usuario = authenticate(username=username, password=password)

            if usuario is not None:
                django_login(request, usuario)
            
                InfoExtra.objects.get_or_create(user=usuario)
            
                return redirect('pagina-principal')
        
        else:
            error_message = "Credenciales incorrectas. Por favor, inténtalo de nuevo."
    else:
        formulario = AuthenticationForm()
        
    return render(request, 'inicio_sesion.html', {'formulario': formulario, 'error_message': error_message})

def register(request):
    error_message = None
    if request.method == 'POST':
        formulario = FormularioDeRegistro(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()  

            info_extra = InfoExtra(user=usuario, es_admin=False, link='', avatar=None)
            info_extra.save()

            return redirect('login')
        else:
            error_message = "Datos incorrectos. Por favor, inténtalo de nuevo."
    else:
        formulario = FormularioDeRegistro()
        
    return render(request, 'register.html', {'formulario': formulario, 'error_message': error_message})

@login_required
def editar_perfil(request):
    try:
        info_extra = request.user.infoextra
    except InfoExtra.DoesNotExist:
        info_extra = InfoExtra(user=request.user, es_admin=False, link='', avatar=None)
        info_extra.save()

    if request.method == 'POST':
        formulario = FormularioDeEditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            info_extra.link = formulario.cleaned_data.get('link')
            if formulario.cleaned_data.get('avatar'):
                info_extra.avatar = formulario.cleaned_data.get('avatar')
            info_extra.save()
            
            formulario.save()
            return redirect('pagina-principal')
    else:
        formulario = FormularioDeEditarPerfil(initial={'link': info_extra.link, 'avatar': info_extra.avatar}, instance=request.user)
    return render(request, 'editar_perfil.html', {'formulario': formulario})

class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'editar_pass.html'
    form_class = CambiarPasswordForm
    success_url = reverse_lazy('editar_perfil')

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})


class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    template_name = 'crear_articulo.html'
    form_class = ArticuloFormulario
    success_url = reverse_lazy('pagina-principal')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)



class EditarArticuloView(LoginRequiredMixin, UpdateView):
    model = Articulo
    template_name = 'editar_articulo.html'
    form_class = ArticuloFormulario


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



def is_admin(user):
    return user.is_staff

def noticia_detalle (req):
    return render(req, 'noticia_detalle.html')



def detalle_categoria(request, categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    articulos = Articulo.objects.filter(categoria=categoria)
    return render(request, 'detalle_categoria.html', {'categoria': categoria, 'articulos': articulos})





