from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
import datetime

from django.db.models.fields import CharField
# Create your models here.
class Departamento(models.Model):
    id_dep = models.CharField(max_length=20, primary_key=True)
    nombre_dep = models.CharField(max_length=100)
    desc_dep = models.CharField(max_length=150)

class Puestos(models.Model):
    id_puesto = models.CharField(max_length=20, primary_key=True)
    nombre_puesto = models.CharField(max_length=40)
    descr_p = models.CharField(max_length=255)
    id_dep = models.ForeignKey(Departamento, on_delete=RESTRICT)

    def __str__(self):
        return u'{0}'.format(self.nombre_puesto)

class Privilegios(models.Model):
    id_priv = models.CharField(max_length=20, primary_key=True)
    tipo_privilegio = models.CharField(max_length=40)

    def __str__(self) -> str:
        return u'{0}'.format(self.tipo_privilegio)

class Imagenes(models.Model):
    id_img = models.IntegerField(primary_key=True)
    nombre_arch = models.CharField(max_length=50)
    archivo = models.FileField(max_length=255, upload_to=None)
    fecha_subida = models.DateField()

class Empleados(models.Model):
    id_empleado = models.CharField(max_length=20, primary_key=True)
    id_img = models.ForeignKey(Imagenes, on_delete=RESTRICT)
    nombre = models.CharField(max_length=50)
    ap_paterno = models.CharField(max_length=30)
    ap_materno = models.CharField(max_length=30)
    puesto = models.ForeignKey(Puestos, on_delete=RESTRICT)
    fecha_registro = models.DateField()

class Usuarios(models.Model):
    email = models.CharField(max_length=50, primary_key=True)
    pass_word = models.CharField(max_length=50)
    privilegio = models.ForeignKey(Privilegios, on_delete=RESTRICT)
    empleado = models.ForeignKey(Empleados, on_delete=RESTRICT)

class Inventario(models.Model):
    id_producto = models.CharField(max_length=20, primary_key=True)
    id_img = models.ForeignKey(Imagenes,  on_delete=RESTRICT)
    nombre_producto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    cantidad = models.FloatField()
    medida = models.CharField(max_length=15)
    id_dep = models.ForeignKey(Departamento, on_delete=RESTRICT)

class Movimientos_almacen(models.Model):
    id_MovAlm = models.CharField(max_length=20, primary_key=True)
    tipo_mov = models.CharField(max_length=10)
    origen_destino = models.CharField(max_length=50)
    motivo = models.CharField(max_length=150)
    fecha_mov = models.DateField()

class Clientes(models.Model):
    id_cliente = models.CharField(max_length=20, primary_key=True)
    nombre_cliente = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=200)

class Compras(models.Model):
    id_compra = models.CharField(max_length=20, primary_key=True)
    id_MovAlm = models.CharField(max_length=20)
    valor_total = models.DecimalField(max_digits=19, decimal_places=4)
    fecha_compra = models.DateField()
    email = models.ForeignKey(Usuarios, on_delete=RESTRICT)

class Ventas(models.Model):
    id_venta = models.CharField(max_length=20, primary_key=True)
    id_MovAlm = models.ForeignKey(Movimientos_almacen, on_delete=RESTRICT)
    valor_total = models.DecimalField(max_digits=19, decimal_places=4)
    email = models.ForeignKey(Usuarios, on_delete=RESTRICT)
    fecha_venta = models.DateField()

class Mov_Ind(models.Model):
    id_MovInd = models.CharField(max_length=20, primary_key=True)
    id_MovAlm = models.ForeignKey(Movimientos_almacen, on_delete=RESTRICT)
    id_producto = models.ForeignKey(Inventario, on_delete=RESTRICT)
    cant_prod = models.FloatField()
    email = models.ForeignKey(Usuarios, on_delete=RESTRICT)

class Proveedor(models.Model):
    id_provee = models.CharField(max_length=20, primary_key=True)
    nombre_provee = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=200)

class PRECIO_INV_VENTA(models.Model):
    ID_PRODUCTO = models.ForeignKey(Inventario, on_delete=RESTRICT)
    PRECIO_UNIT_VENTA = models.DecimalField(max_digits=19, decimal_places=4)

class Est_Prod(models.Model):
    id_producto = models.ForeignKey(Inventario, on_delete=RESTRICT)
    estado = models.CharField(max_length=20)

class detalles_compras(models.Model):
    id_detalle = models.CharField(max_length=20, primary_key=True)
    id_compra = models.ForeignKey(Compras, on_delete=RESTRICT)
    id_producto = models.ForeignKey(Inventario, on_delete=RESTRICT)
    precio_unitario = models.DecimalField(max_digits=19, decimal_places=4)
    cant_xprod = models.DecimalField(max_digits=19, decimal_places=4)
    id_provee = models.ForeignKey(Proveedor, on_delete=RESTRICT)

class detalles_ventas(models.Model):
    id_detalle = models.CharField(max_length=20, primary_key=True)
    id_venta = models.ForeignKey(Ventas, on_delete=RESTRICT)
    id_producto = models.ForeignKey(Inventario, on_delete=RESTRICT)
    precio_unitario = models.DecimalField(max_digits=19, decimal_places=4)
    cant_xprod = models.DecimalField(max_digits=19, decimal_places=4)
    id_cliente = models.ForeignKey(Clientes, on_delete=RESTRICT)

class cuentas_por_cobrar(models.Model):
    id_cpc = models.CharField(max_length=20, primary_key=True)
    status = models.CharField(max_length=50)
    fecha_de_pago_fact = models.CharField(max_length=20)
    contrarecibo = models.CharField(max_length=25)
    fecha_rec_pago = models.CharField(max_length=20)
    sp = models.CharField(max_length=35)
    oc = models.CharField(max_length=35)
    fecha = models.DateField()
    id_producto = models.ForeignKey(Inventario, on_delete=RESTRICT)
    email = models.ForeignKey(Usuarios, on_delete=RESTRICT, null=True)
    pozo = models.CharField(max_length=100)
    total_servicios = models.FloatField()
    subtotal_usd = models.DecimalField(decimal_places=4, max_digits=19)
    iva = models.DecimalField(decimal_places=4, max_digits=19)
    total_usd_xservicio = models.DecimalField(decimal_places=4, max_digits=19)
    monto_total = models.DecimalField(decimal_places=4, max_digits=19)
    fact_no = models.CharField(max_length=35)
    fecha_de_fac = models.CharField(max_length=20)
    recibo_pag_fac_mcgreen = models.CharField(max_length=20)
    fecha_de_rec_pago = models.CharField(max_length=20)
    dllr = models.CharField(max_length=20)
    monto_mxp = models.DecimalField(decimal_places=4, max_digits=19)
    monto_mxp_pagado = models.DecimalField(decimal_places=4, max_digits=19)

class auditoria(models.Model):
    id_audit = models.AutoField(primary_key=True)
    email = models.ForeignKey(Usuarios, on_delete=RESTRICT)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
