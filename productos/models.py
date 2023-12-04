from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    stock = models.IntegerField()
    
    def __str__(self):
        return self.nombre