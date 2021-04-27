from django.shortcuts import render, redirect
from .forms import UsuarioForm, ReservaForm, ProductoForm, RegionForm, CiudadForm, ComunaForm, ClienteForm, EmpleadoForm, TipoMarcaForm, ProveedorForm, TipoEmpleadoForm, TipoPagoForm, TipoUsuarioForm, PagoServicioForm, ServicioForm, PedidoOrdenForm, PedidoOrdenProductoForm, RecepcionPedidoForm, RecepcionPedidoProductoForm, DetalleServicioForm, EmpleadoServicioForm, BoletaFacturaPedidoForm 

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
    data = {
        'formReserva': ReservaForm()
    }
    return render(request, 'core/reserva.html', data)


def registro (request):
    return render(request, 'registration/registro.html')