from django.urls import path
from ventas.views import clients, crear_cliente, ventas, crear_venta

# En tu app de ventas
urlpatterns = [
    path('clientes/', clients, name="clients"),
    path('clientes/crear/', crear_cliente, name="crear cliente"),
    path('ventas/', ventas, name="ventas"),
    path('ventas/crear/', crear_venta, name="crear venta")
]
