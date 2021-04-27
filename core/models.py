# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BoletaFactura(models.Model):
    bol_fac_id = models.BigIntegerField(primary_key=True)
    serv = models.ForeignKey('Servicio', models.DO_NOTHING)
    bol_fac_total = models.BigIntegerField()
    bol_fac_fecha_emision = models.DateField()
    desc_bol_fac = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'boleta_factura'


class Ciudad(models.Model):
    id_ciudad = models.BigIntegerField(primary_key=True)
    desc_ciudad = models.CharField(max_length=100)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')

    class Meta:
        managed = False
        db_table = 'ciudad'

    def __str__(self):
        return self.desc_ciudad


class Cliente(models.Model):
    cli_rut = models.IntegerField(primary_key=True)
    cli_pnombre = models.CharField(max_length=30)
    cli_apellidopat = models.CharField(max_length=50)
    cli_apellidomat = models.CharField(max_length=50)
    cli_email = models.CharField(max_length=50)
    cli_telefono = models.BigIntegerField()
    id_comuna = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='id_comuna', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'

    def __int__(self):
        return self.cli_rut


class Comuna(models.Model):
    id_comuna = models.BigIntegerField(primary_key=True)
    desc_comuna = models.CharField(max_length=100)
    id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciudad')

    class Meta:
        managed = False
        db_table = 'comuna'
    
    def __str__(self):
        return self.desc_comuna


class DetalleServicio(models.Model):
    id_det_serv = models.BigIntegerField(primary_key=True)
    fecha_serv_realizado = models.DateField()
    hora_servicio_realizado = models.CharField(max_length=5)
    servicios_realizados = models.CharField(max_length=150)
    serv = models.ForeignKey('Servicio', models.DO_NOTHING)
    costo_total_servicios = models.BigIntegerField()
    cli_rut = models.IntegerField()
    pago = models.ForeignKey('PagoServicio', models.DO_NOTHING)
    res_id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='res_id_reserva')

    class Meta:
        managed = False
        db_table = 'detalle_servicio'
    
    def __str__(self):
        return self.id_det_serv


class Empleado(models.Model):
    emp_rut = models.IntegerField(primary_key=True)
    emp_id = models.BigIntegerField()
    emp_pnombre = models.CharField(max_length=50)
    emp_apellidopat = models.CharField(max_length=50)
    emp_apellidomat = models.CharField(max_length=50)
    emp_sueldo = models.BigIntegerField()
    emp_telefono = models.IntegerField()
    emp_email = models.CharField(max_length=30)
    id_tipo_empleado = models.ForeignKey('TipoEmpleado', models.DO_NOTHING, db_column='id_tipo_empleado')
    user = models.ForeignKey('Usuario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'empleado'
    
    def __str__(self):
        return self.emp_pnombre


class EmpleadoServicio(models.Model):
    id_empleado_servicio = models.BigIntegerField(primary_key=True)
    cant_utilizada_prod = models.BigIntegerField()
    res_id_reserva = models.BigIntegerField()
    serv = models.ForeignKey('Servicio', models.DO_NOTHING)
    prod = models.ForeignKey('Producto', models.DO_NOTHING)
    emp_rut = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='emp_rut')

    class Meta:
        managed = False
        db_table = 'empleado_servicio'


class PagoServicio(models.Model):
    pago_id = models.BigIntegerField(primary_key=True)
    desc_serv = models.CharField(max_length=50)
    medio_pago = models.ForeignKey('TipoPago', models.DO_NOTHING)
    bol_fac = models.ForeignKey(BoletaFactura, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pago_servicio'


class PedidoOrden(models.Model):
    ped_id_emision = models.BigIntegerField(primary_key=True)
    ped_desc_emision = models.CharField(max_length=100)
    emp_rut = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='emp_rut')
    ped_fecha_emision = models.DateField()

    class Meta:
        managed = False
        db_table = 'pedido_orden'


class PedidoOrdenProducto(models.Model):
    id_pedido_orden_prod = models.BigIntegerField(primary_key=True)
    id_pedido_producto = models.BigIntegerField()
    prod_cantidad = models.BigIntegerField()
    costo_pedido = models.BigIntegerField()
    prod = models.ForeignKey('Producto', models.DO_NOTHING)
    ped_id_emision = models.ForeignKey(PedidoOrden, models.DO_NOTHING, db_column='ped_id_emision')

    class Meta:
        managed = False
        db_table = 'pedido_orden_producto'


class Producto(models.Model):
    prod_id = models.BigIntegerField(primary_key=True)
    prod_nombre = models.CharField(max_length=100)
    prod_stock = models.BigIntegerField()
    prov = models.ForeignKey('Proveedor', models.DO_NOTHING)
    id_marca = models.ForeignKey('TipoMarca', models.DO_NOTHING, db_column='id_marca')

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    prov_id = models.BigIntegerField(primary_key=True)
    prov_nombre = models.CharField(max_length=100)
    prov_rut_empresa = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'proveedor'


class RecepcionPedido(models.Model):
    id_recepcion = models.BigIntegerField(primary_key=True)
    fecha_recepcion = models.DateField()
    desc_recepcion = models.CharField(max_length=150)
    emp_rut = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='emp_rut')

    class Meta:
        managed = False
        db_table = 'recepcion_pedido'


class RecepcionPedidoProducto(models.Model):
    id_pedido_prod = models.BigIntegerField(primary_key=True)
    prod_cantidad = models.BigIntegerField()
    fecha_recepcion = models.DateField()
    costo_recepcion = models.BigIntegerField(blank=True, null=True)
    prod = models.ForeignKey(Producto, models.DO_NOTHING)
    id_recepcion = models.ForeignKey(RecepcionPedido, models.DO_NOTHING, db_column='id_recepcion')

    class Meta:
        managed = False
        db_table = 'recepcion_pedido_producto'


class Region(models.Model):
    id_region = models.BigIntegerField(primary_key=True)
    desc_region = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'region'


class Reserva(models.Model):
    res_id_reserva = models.BigIntegerField(primary_key=True)
    res_hora_reservada = models.DateField(max_length=5)
    res_fecha_pedido_reserva = models.DateField()
    res_desc_reserva = models.CharField(max_length=200)
    cli_rut = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cli_rut')

    class Meta:
        managed = False
        db_table = 'reserva'


class Servicio(models.Model):
    serv_id = models.BigIntegerField(primary_key=True)
    serv_descripcion = models.CharField(max_length=150)
    serv_costo = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'servicio'


class TipoEmpleado(models.Model):
    id_tipo_empleado = models.BigIntegerField(primary_key=True)
    desc_empleado = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_empleado'


class TipoMarca(models.Model):
    id_marca = models.BigIntegerField(primary_key=True)
    desc_marca = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_marca'


class TipoPago(models.Model):
    medio_pago_id = models.BigIntegerField(primary_key=True)
    desc_medio_pago = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_pago'


class TipoUsuario(models.Model):
    tipo_user_id = models.BigIntegerField(primary_key=True)
    user_desc = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuario(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    user_nombre = models.CharField(max_length=20)
    user_contrasena = models.CharField(max_length=20)
    tipo_user = models.ForeignKey(TipoUsuario, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuario'
        
    def __str__(self):
        return self.user_nombre 