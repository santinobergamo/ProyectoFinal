from django.urls import path
from .views import  *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    #PAGINA PRINCIPAL, ABOUT:
    path('', PaginaPrincipalView.as_view(), name='pagina-principal'),  # URL principal
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),  
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('articulo1/', noticia_1, name='noticia_1'),
    path('articulo2/', noticia_2, name='noticia_2'),

    #REGISTER/LOGIN/LOGOUT, EDITAR PERFIL/PASSWORD:
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/editar/password/', CambiarPassword.as_view(), name='editar_pass'),

    #CREAR/EDITAR/ELIMINAR/VER ARTICULO:
    path('crear-post/', crear_post, name='crear_post'),
    path('ver-posts/', ver_posts, name='ver_posts'),
    path('eliminar-post/<int:post_id>/', eliminar_post, name='eliminar_post'),
    path('detalle-articulo/<int:articulo_id>/', detalle_articulo, name='detalle_articulo'),
    path('editar-articulo/<int:articulo_id>/', editar_articulo, name='editar_articulo'),


]


