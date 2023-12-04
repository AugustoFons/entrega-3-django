from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre= models.CharField(max_length=50) #charfield necesita que se le diga la maxima cantidad de caracteres
    documento= models.IntegerField()         #texfield no define maximo
    email= models.EmailField()

    def __str__(self):
        return self.nombre + ", DNI: " + str(self.documento)

class Venta(models.Model):
    cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="ventas") #relacionar ambas tablas
    nro_venta= models.IntegerField()  #si borro un cliente, cascade borra todas las ventas de ese cliente, hay otras opciones como PROTECTED
    producto= models.CharField(max_length=50)   #related name es para cuando en la db escriba clientes.ventas obtenga las ventas relacionadas
    cantidad= models.IntegerField()
    fecha_de_venta= models.DateField()

    def __str__(self):
        return "Venta nro: " + str(self.nro_venta)
