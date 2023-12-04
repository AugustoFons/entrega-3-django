from django.urls import path
from productos.views import crear_producto

urlpatterns = [
    path('crear/', crear_producto, name='crear producto'),
]