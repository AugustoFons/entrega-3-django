from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from ventas.models import Cliente, Venta

#obtener clientes
def clients(request):
    clientes= Cliente.objects.all()

    return render(request, 'clientes.html', {'clientes': clientes})

#crear cliente via formulario
def crear_cliente(request):
    if request.method == "POST":
        nuevo_cliente = Cliente(
            nombre = request.POST["name"],    #entre comillas va el name del form
            documento = request.POST["dni"],
            email = request.POST["email"]
        )
        nuevo_cliente.save()
        return redirect('/clientes/')

    return render(request, 'crear_cliente.html')

#obtener ventas
def ventas(request):
    ventas= Venta.objects.all()

    return render(request, 'ventas.html', {'ventas': ventas})

#crear ventas via formulario
def crear_venta(request):
    clientes= Cliente.objects.all()
    if request.method == "POST":
        nueva_venta = Venta(
            nro_venta = request.POST["nro"],
            producto = request.POST["prod"],
            cantidad = request.POST["cant"],
            fecha_de_venta = request.POST["date"],
            cliente_id=request.POST["client"]
        )
        nueva_venta.save()
        return redirect('/ventas/')
    
    return render(request, 'crear_venta.html', {'clientes': clientes})