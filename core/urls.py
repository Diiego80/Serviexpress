from django.contrib import admin
from django.urls import path
from .views import index, ingreso, nosotros, servicio, ubicacion, reserva, registro

urlpatterns = [
    path('', index, name="index"),
    path('ingreso/', ingreso, name="ingreso"),
    path ('nosotros/', nosotros, name="nosotros"),
    path ('servicio/', servicio, name="servicio"),
    path ('ubicacion/', ubicacion, name="ubicacion"),
    path ('reserva/', reserva, name="reserva"),
    path ('registro/', registro, name="registro"),
]


