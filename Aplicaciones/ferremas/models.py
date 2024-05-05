from django.db import models
from .admin import Producto
# Create your models here.

class Producto(models.Model):
    codigoProducto=models.CharField(primary_key=True,max_length=10)
    marca=models.CharField(max_length=10)
    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=50)
    precio=models.CharField(max_length=10)
    fecha=models.CharField(max_length=100)
