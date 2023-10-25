from django.urls import path
from .views import  *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', PaginaPrincipalView.as_view(), name='pagina-principal'),  # URL principal
    path('articulos/crear', ArticuloCreateView.as_view(), name="crear_articulo"),
    path('editar-articulo/<int:pk>/', EditarArticuloView.as_view(), name='editar-articulo'),
    path('eliminar-articulo/<int:pk>/', EliminarArticuloView.as_view(), name='eliminar-articulo'),
    path('articulo1/', noticia_1, name='noticia_1'),
    path('articulo2/', noticia_2, name='noticia_2'),
    path('futbol-argentino/', futbol_argentino, name='futbol-argentino' ),
    path('seleccion-arg/', seleccion_arg, name='seleccion-arg'),
    path('about/', about, name='about'),
    path('noticia-detalle/', noticia_detalle, name='noticia-detalle'),
    path('categoria/<int:categoria_id>/', detalle_categoria, name='detalle-articulos'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),  
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/editar/password/', CambiarPassword.as_view(), name='editar_pass'),

]


