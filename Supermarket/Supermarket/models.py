from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Negocios(models.Model):
    nombre = models.CharField( max_length=200 )
    id_creator_user = models.ForeignKey( User, on_delete=models.CASCADE, related_name='user_creator' )
    coordenadas = models.CharField( max_length=100 )
    direccion = models.CharField( max_length=300 )
    imagen = models.ImageField( upload_to='static/imagen/negocios/' , default='static/imagen/negocios/base_supermarket.jpg' )
    
    def __str__(self):
        return f'{self.id}__{self.nombre}'
class Categorias(models.Model):
    nombre = models.CharField( max_length=200 )
    def __str__(self):
        return f'{self.id}__{self.nombre}'
    
class Producto(models.Model):
    nombre = models.CharField( max_length=200 )
    imagen = models.ImageField( upload_to='static/imagen/productos/' , default='static/imagen/productos/base_productos.jpg' )
    id_negocio = models.ForeignKey( Negocios, on_delete=models.CASCADE, related_name='negocio' )
    id_categoria = models.ForeignKey( Categorias, on_delete=models.CASCADE, related_name='categoria' )
    def __str__(self):
        return f'{self.id}__{self.nombre}'

class Precio_Producto(models.Model):
    precio = models.FloatField()
    fecha_creacion = models.DateTimeField( default=timezone.now )
    id_producto = models.ForeignKey( Producto, on_delete=models.CASCADE, related_name='producto' )