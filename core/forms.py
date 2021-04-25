from django import forms
from .models import Usuario, Reserva, Producto, Region, Ciudad, Comuna, Cliente, Empleado, TipoMarca, Proveedor, TipoEmpleado, TipoPago, TipoUsuario, PagoServicio, Servicio, PedidoOrden, PedidoOrdenProducto


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['user_nombre', 'user_contrasena']

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ["res_hora_reservada", "res_fecha_pedido_reserva", "res_desc_reserva", "cli_rut"]

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"

class RegionForm(forms.ModelForm):

    class Meta:
        model = Region
        fields = "__all__"


class CiudadForm(forms.ModelForm):

    class Meta:
        model = Ciudad
        fields = "__all__"

class ComunaForm(forms.ModelForm):

    class Meta: 
        model = Comuna
        fields = "__all__"

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = "__all__"

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = "__all__"

class TipoMarcaForm(forms.ModelForm):

    class Meta:
        model = TipoMarca
        fields = "__all__"

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = "__all__"

class TipoEmpleadoForm(forms.ModelForm):

    class Meta:
        model = TipoEmpleado
        fields = "__all__"

class TipoPagoForm(forms.ModelForm):

    class Meta:
        model = TipoPago
        fields = "__all__"

class TipoUsuarioForm(forms.ModelForm):

    class Meta:
        model = TipoUsuario
        fields = "__all__"

class PagoServicioForm(forms.ModelForm):

    class Meta:
        model = PagoServicio
        fields = "__all__"

class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = "__all__"

class PedidoOrdenForm(forms.ModelForm):

    class Meta:
        model = PedidoOrden
        fields = "__all__"

class PedidoOrdenProductoForm(forms.ModelForm):

    class Meta:
        model = PedidoOrdenProducto
        fields = "__all__"
