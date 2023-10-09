from django.urls import path
from .views import  *

urlpatterns = [
    path('', PaginaPrincipalView.as_view(), name='pagina-principal'),  # URL principal
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('inicio-sesion/', InicioSesionView.as_view(), name='inicio-sesion'),
    path('cierre-sesion/', CierreSesionView.as_view(), name='cierre-sesion'),
    path('crear-articulo/', CrearArticuloView.as_view(), name='crear-articulo'),
    path('editar-articulo/<int:pk>/', EditarArticuloView.as_view(), name='editar-articulo'),
    path('eliminar-articulo/<int:pk>/', EliminarArticuloView.as_view(), name='eliminar-articulo'),
    path('noticia_1/', noticia_1, name='noticia_1'),
    path('noticia_2/', noticia_2, name='noticia_2'),
    path('futbol-argentino/', futbol_argentino, name='futbol-argentino' ),
    path('seleccion-arg/', seleccion_arg, name='seleccion-arg'),
    path('about/', about, name='about'),
]