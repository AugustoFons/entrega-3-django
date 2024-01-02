from django.urls import path
from ventas.views import clients, crear_cliente, crear_venta, eliminar_cliente, editar_cliente, VentaListView

# En tu app de ventas
urlpatterns = [
    path('clientes/', clients, name="clients"),
    path('clientes/crear/', crear_cliente, name="crear cliente"),
    path('ventas/', VentaListView.as_view(), name="ventas"),
    path('ventas/crear/', crear_venta, name="crear venta"),
    path('eliminar/<nombre_cliente>', eliminar_cliente, name="eliminar"),
    path('editar/<nombre_cliente>', editar_cliente, name="editar")
]
