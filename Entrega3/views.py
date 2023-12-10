from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from productos.models import Producto
from django.db.models import Q
from django.http import JsonResponse

#obtener productos
def home(request):

    productos = Producto.objects.all()

    return render(request, 'index.html', {'productos': productos})

def busqueda(request):
    if request.method == "POST":
        data = request.POST.get("nombre", "").lower()  # Obtener el dato y convertirlo a minúsculas

        lista_busq= Producto.objects.filter(Q(nombre__icontains=data))
        return render(request, 'index.html', {'lista': lista_busq})
    
    return render(request, 'index.html')

def realizar_compra(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad'))
        # Lógica para encontrar el producto y actualizar el stock
        producto = Producto.objects.get(id=producto_id)
        if producto.stock >= cantidad:
            producto.stock -= cantidad
            producto.save()

            return render(request, 'realizar_compra.html')
        else:
            return JsonResponse({'mensaje': 'No hay suficiente stock'}, status=400)
