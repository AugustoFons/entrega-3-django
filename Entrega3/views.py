from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from productos.models import Producto

#obtener productos
def home(request):

    productos = Producto.objects.all()

    return render(request, 'index.html', {'productos': productos})
