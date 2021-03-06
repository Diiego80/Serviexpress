from django.contrib import admin
from .models import BoletaFactura, Ciudad, Cliente, Comuna, DetalleServicio, Empleado, EmpleadoServicio, PagoServicio, PedidoOrden, PedidoOrdenProducto, Producto, Proveedor, RecepcionPedido, RecepcionPedidoProducto, Region, Reserva, Servicio, TipoEmpleado, TipoMarca, TipoPago, TipoUsuario, Usuario
# Register your models here.

admin.site.register(BoletaFactura)
admin.site.register(Ciudad)
admin.site.register(Cliente)
admin.site.register(Comuna)
admin.site.register(DetalleServicio)
admin.site.register(Empleado)
admin.site.register(EmpleadoServicio)
admin.site.register(PagoServicio)
admin.site.register(PedidoOrden)
admin.site.register(PedidoOrdenProducto)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(RecepcionPedido)
admin.site.register(RecepcionPedidoProducto)
admin.site.register(Region)
admin.site.register(Reserva)
admin.site.register(Servicio)
admin.site.register(TipoEmpleado)
admin.site.register(TipoMarca)
admin.site.register(TipoPago)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)