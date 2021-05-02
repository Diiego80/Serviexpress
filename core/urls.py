from django.contrib import admin
from django.urls import path

from .views import index, ingreso, nosotros, servicio, ubicacion, registro, registro_clientes, registro_productos, formulario_productos, formulario_empleados, formulario_clientes, formulario_reserva, agregar_producto, listado_productos

urlpatterns = [
    #Navegacion General
    path('', index, name="index"),
    path('ingreso/', ingreso, name="ingreso"),
    path ('nosotros/', nosotros, name="nosotros"),
    path ('servicio/', servicio, name="servicio"),
    path ('ubicacion/', ubicacion, name="ubicacion"),
    
    #Registro
    path('registro/', registro, name="registro"),
    #Administracion Interna
    path('registro-clientes/', registro_clientes, name="registro_clientes"),
    path('registro-productos/', registro_productos, name="registro_productos"),
    #Formularios
    path('formulario-productos/', formulario_productos, name="formulario_productos"),
    path('formulario-empleados/', formulario_empleados, name="formulario_empleados"),
    path('formulario-clientes/', formulario_clientes, name="formulario_clientes"),
    path ('formulario-reserva/', formulario_reserva, name="formulario_reserva"),
    #Agregar
    path ('agregar-producto/', agregar_producto, name="agregar_producto"),
    #Listados
    path ('listado-producto/', listado_productos, name="listado_productos"),
]


