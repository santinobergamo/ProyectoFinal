from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=255)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='articulos_images', blank=True, null=True)
    

    def __str__(self):
        return self.titulo

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.TextField()
    avatar = models.ImageField(default='default.jpg', upload_to='perfil_images', blank=True, null=True)

    def __str__(self):
        return self.usuario.username
    
class InfoExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    es_admin = models.BooleanField(default=False)
    link = models.URLField(null=True)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)

