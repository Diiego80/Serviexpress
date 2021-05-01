from django.contrib import admin
from django.urls import path

from .views import index, ingreso, nosotros, servicio, ubicacion, registro, registro_clientes, registro_productos, formulario_productos, formulario_empleados, formulario_clientes, formulario_reserva

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
    path('registro_clientes/', registro_clientes, name="registro_clientes"),
    path('registro_productos/', registro_productos, name="registro_productos"),
    #Formularios
    path('formulario_productos/', formulario_productos, name="formulario_productos"),
    path('formulario_empleados/', formulario_empleados, name="formulario_empleados"),
    path('formulario_clientes/', formulario_clientes, name="formulario_clientes"),
    path ('formulario_reserva/', formulario_reserva, name="formulario_reserva"),
]


