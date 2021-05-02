from django.shortcuts import render, redirect
from .models import BoletaFactura, Ciudad, Cliente, Comuna, DetalleServicio, Empleado, EmpleadoServicio, PagoServicio, PedidoOrden, PedidoOrdenProducto, Producto, Proveedor, RecepcionPedido, RecepcionPedidoProducto, Region, Reserva, Servicio, TipoEmpleado, TipoMarca, TipoPago, TipoUsuario, Usuario
from .forms import UsuarioForm, ReservaForm, ProductoForm, RegionForm, CiudadForm, ComunaForm, ClienteForm, EmpleadoForm, TipoMarcaForm, ProveedorForm, TipoEmpleadoForm, TipoPagoForm, TipoUsuarioForm, PagoServicioForm, ServicioForm, PedidoOrdenForm, PedidoOrdenProductoForm, RecepcionPedidoForm, RecepcionPedidoProductoForm, DetalleServicioForm, EmpleadoServicioForm, BoletaFacturaPedidoForm
# Extra
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from rest_framework import viewsets

# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def ingreso(request):
    return render(request, 'core/ingreso.html')


def nosotros(request):
    return render(request, 'core/nosotros.html')


def servicio(request):
    servicio = Servicio.objects.all()
    dataServicio = {
        'servicio': servicio
    }
    return render(request, 'core/servicio.html', dataServicio)


def ubicacion(request):
    return render(request, 'core/ubicacion.html')


def registro(request):
    dataRegistro = {
        'form': UsuarioForm()
    }
    if request.method == 'POST':
        formularioContacto = UsuarioForm(data=request.POST)
        if formularioContacto.is_valid():
            formularioContacto.save()
            dataRegistro["mensaje"] = "Usuario Guardado Correctamente"
        else:
            dataRegistro["form"] = formularioContacto

    return render(request, 'registration/registro.html', dataRegistro)


def registro_clientes(request):
    return render(request, 'core/registro_clientes.html')


def registro_productos(request):
    return render(request, 'core/registro_productos.html')


def formulario_productos(request):
    return render(request, 'core/formularios/formulario_productos.html')


def formulario_empleados(request):
    return render(request, 'core/producto/formulario_empleados.html')


def formulario_clientes(request):
    return render(request, 'core/cliente/formulario_clientes.html')


def formulario_reserva(request):
    data = {
        'formReserva': ReservaForm()
    }

    if request.method == 'POST':
        formulario = ReservaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Reserva Guardada Con Exito"
        else:
            data["form"] = formulario
    return render(request, 'core/reserva/formulario_reserva.html', data)


def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Producto Guardado Correctamente"
        else:
            data["form"] = formulario

    return render(request, 'core/producto/agregar_producto.html', data)

def listado_productos (request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }
    return render(request, 'core/producto/listado_productos.html', data)
