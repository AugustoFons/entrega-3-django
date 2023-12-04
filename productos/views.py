from django.shortcuts import render, redirect
from productos.models import Producto
from django.template import loader
from django.http import HttpResponse

#crear producto via formulario
def crear_producto(request):
    if request.method == "POST":
        nuevo_producto = Producto(
            nombre = request.POST["name"],    #entre comillas va el name del form
            descripcion = request.POST["description"],
            stock = request.POST["stock"]
        )
        nuevo_producto.save()
        return redirect('/')

    return render(request, 'crear_producto.html')