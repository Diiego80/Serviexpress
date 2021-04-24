from django.shortcuts import render, redirect
from .forms import UsuarioForm

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def ingreso(request):
    return render(request,'core/ingreso.html')

def nosotros(request):
    return render (request,'core/nosotros.html')

def servicio (request):
    return render(request, 'core/servicio.html')

def ubicacion (request):
    return render(request, 'core/ubicacion.html')

def reserva (request):
    return render(request, 'core/reserva.html')