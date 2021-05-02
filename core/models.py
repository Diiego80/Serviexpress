# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from sequences import get_next_value
import datetime
from django.db import models
import functools
"""
def set_sql_for_field(field, sql):
    
    Decorator for Model.save() to set SQL for field if empty.

    Example:

    class LegacyModel(models.Model):
        col1 = models.IntegerField(primary_key=True)
        col2 = models.IntegerField()

        @set_sql_for_field('col1', 'select col1_seq.nextval from dual')
        @set_sql_for_field('col2', 'select 1+max(col2) from legacy_model')
        def save(self, *args, **kwargs):
            super().save(*args, **kwargs)

    When this model is saved col1 and col2 will be set (if empty) to the output
    of the provided SQL within the schema/database of the model's app.
    ""
    def decorator(model_save_func):
        @functools.wraps(model_save_func)
        def wrapper(obj, *args, **kwargs):
            assert hasattr(obj, field), (
                'set_sql_for_field was given a field that does not exist on '
                'the model. Double-check model fields and decorators for '
                f'{obj.__class__}.{field} and SQL {sql}'
            )

            if getattr(obj, field) is None:
                # Multi-DB safe! Get DB for class from default manager.
                database = obj.__class__._default_manager.db

                from django.db import connections
                with connections[database].cursor() as cursor:
                    cursor.execute(f'{sql}')
                    setattr(obj, field, cursor.fetchone()[0])

            return model_save_func(obj, *args, **kwargs)
        return wrapper
    return decorator """


class BoletaFactura(models.Model):
    bol_fac_id = models.AutoField(primary_key=True)
    serv = models.ForeignKey('Servicio', models.DO_NOTHING)
    bol_fac_total = models.BigIntegerField()
    bol_fac_fecha_emision = models.DateField()
    desc_bol_fac = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'boleta_factura'


class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True, blank=True)
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
    cli_email = models.EmailField(max_length=50)
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
    emp_email = models.EmailField(max_length=30)
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
        
    def __str__(self):
        return self.desc_region

opciones_hora_reservada = [
    ["08:00","08:00"],
    ["09:00","09:00"],
    ["10:00","10:00"],
    ["11:00","11:00"],
    ["12:00","12:00"],
    ["13:00","13:00"],
    ["14:00","14:00"],
    ["15:00","15:00"],
    ["16:00","16:00"],
    ["17:00","17:00"],
    ["18:00","18:00"],
    ["19:00","19:00"],
    ["20:00","20:00"]

]



class Reserva(models.Model):
    res_id_reserva = models.BigIntegerField(primary_key=True)
    res_hora_reservada = models.DateField(max_length=5, choices=opciones_hora_reservada)
    res_fecha_pedido_reserva = models.DateField(default=datetime.date.today)
    res_desc_reserva = models.CharField(max_length=200)
    cli_rut = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cli_rut')

    class Meta:
        managed = False
        db_table = 'reserva'


class Servicio(models.Model):
    serv_id = models.BigIntegerField(primary_key=True) 
    serv_descripcion = models.CharField(max_length=150)
    serv_costo = models.BigIntegerField()
    serv_titulo = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'servicio'

    def __str__(self):
        return self.serv_descripcion


class TipoEmpleado(models.Model):
    id_tipo_empleado = models.AutoField(primary_key=True)
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
    user_id = models.AutoField(primary_key=True)
    user_nombre = models.CharField(max_length=20)
    user_contrasena = models.CharField(max_length=20)
    tipo_user = models.ForeignKey(TipoUsuario, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuario'
        
    def __str__(self):
        return self.user_nombre 