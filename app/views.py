from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from . import models
from django.db import connection
from .forms import formulario_cliente, formulario_proveedor, Formulario_registro

# Create your views here.
# ?? Sesiones
def iniciar_sesion(request):
    if request.method == 'POST':
        try:
            cursor = connection.cursor()
            cursor.execute("Select privilegio_id from app_usuarios where email = %s",[request.POST["user"]])
            privilegio = cursor.fetchone()
            cursor.callproc("VERIFICAR_USUARIO",[request.POST["user"], request.POST["pass"]])
            mensaje = cursor.fetchone()[0]
            if mensaje == 'EXISTE':
                request.session["email"] = request.POST["user"]
                request.session["privilegio"] = privilegio[0]
                return redirect("/Inventario_general")
            else:
                return HttpResponse("<h1>No existe el usuario</h1>")
        finally:
            cursor.close()
    return render(request, 'login.html')

def registro(request):
    if request.session.get('email'):
        formulario = Formulario_registro()
        return render(request, 'registro.html', {'formulario': formulario, 'privilegio': request.session.get("privilegio")})
    else:
        return redirect("/cerrar_sesion")


def cerrar_sesion(request):
    try:
        del request.session["email"]
        print(request.session)
    except KeyError:
        pass
    return render(request, "Inventario/cerrar_sesion.html")

# ?? Inventario
def Inventario_general(request):
    if request.session.get("email"):
        cursor = connection.cursor()
        if request.session.get("privilegio") != 'ADM-IN1':
            cursor.callproc('MOSTRAR_PRODUCTOS_ACTIVOS')
            nombres = [
                models.Inventario._meta.get_field("id_producto").name,
                models.Inventario._meta.get_field("nombre_producto").name,
                models.Inventario._meta.get_field("descripcion").name,
                models.Inventario._meta.get_field("cantidad").name,
                models.Inventario._meta.get_field("medida").name,
                models.Inventario._meta.get_field("id_dep_id").name,
                "Precio unitario",
                "Subtotal",
                "Precio total",
            ]
            context = {
                'departamentos': models.Departamento.objects.all(),
                'inventario': cursor.fetchall(),
                'campos_inv': nombres,
                'privilegio': request.session.get("privilegio")
            }
            cursor.close()
            return render(request, 'Inventario/index.html', context)
        else:
            cursor.callproc('MOSTRAR_TODOS_LOS_PRODUCTOS')
            nombres = [
                models.Inventario._meta.get_field("id_producto").name,
                models.Inventario._meta.get_field("nombre_producto").name,
                models.Inventario._meta.get_field("descripcion").name,
                models.Inventario._meta.get_field("cantidad").name,
                models.Inventario._meta.get_field("medida").name,
                models.Inventario._meta.get_field("id_dep_id").name,
                "Precio unitario",
                "Subtotal",
                "Precio total",
            ]
            context = {
                'departamentos': models.Departamento.objects.all(),
                'inventario': cursor.fetchall(),
                'campos_inv': nombres,
                'privilegio': request.session.get("privilegio")
            }
            cursor.close()
            return render(request, 'Inventario/index.html', context)
    else:
        return redirect("/cerrar_sesion")

# ?? Compras
def compras(request):
    if request.session.get('email'):
        if request.method != 'POST':
            cursor = connection.cursor()
            cursor.callproc('MOSTRAR_PRODUCTOS_ACTIVOS')
            form = formulario_proveedor()
            context = {
                'productos': cursor.fetchall(),
                'proveedores': models.Proveedor.objects.all(),
                'form': form,
                'sesion': request.session.get("email"),
                'privilegio': request.session.get("privilegio")
            }
            cursor.close()
            return render(request, 'Inventario/compras.html', context)
    else:
        return redirect("/cerrar_sesion")



# ?? Ventas
def ventas(request):
    if request.session.get('email'):
        if request.method != 'POST':
            cursor = connection.cursor()
            cursor.callproc('MOSTRAR_SISTEMAS_ACTIVOS')
            form = formulario_cliente()
            context = {
                'sistemas': cursor.fetchall(),
                'clientes': models.Clientes.objects.all(),
                'sesion': request.session.get("email"),
                'privilegio': request.session.get("privilegio"),
                'form': form,
            }
            cursor.close()
            return render(request, 'Inventario/cuentas_p_c.html', context)
    else:
        return redirect("/cerrar_sesion")

# ?? Otros tipos de movimientos
def otras_e_s(request):
    if request.session.get('email'):
        cursor = connection.cursor()
        cursor.callproc('MOSTRAR_PRODUCTOS_ACTIVOS')
        context = {
            'sesion': request.session.get("email"),
            'privilegio': request.session.get("privilegio"),
            'productos': cursor.fetchall(),
        }
        cursor.close()
        return render(request, 'Inventario/otras_e_s.html', context)
    else:
        return redirect("/cerrar_sesion")


def movimientos(request):
    if request.session.get('email'):
        cursor = connection.cursor()
        cursor.callproc("MOSTRAR_MOV_IND")
        context = {
            'movimientos': cursor.fetchall()
        }
        cursor.close()
        context["privilegio"] = request.session.get("privilegio")
        return render(request, 'Inventario/movimientos.html', context)
    else:
        return redirect("/cerrar_sesion")


# ?? Vistas
def ver_compras(request):
    if request.session.get('email'):
        cursor = connection.cursor()
        cursor.callproc('MOSTRAR_COMPRAS')
        context = {
            'datos_compras': cursor.fetchall()
        }
        cursor.close()
        return render(request, 'Inventario/ver_compras.html', context)
    else:
        return redirect("/cerrar_sesion")

def ver_ventas(request):
    if request.session.get('email'):
        cursor = connection.cursor()
        cursor.callproc("MOSTRAR_MOV_IND")
        context = {
            'movimientos': cursor.fetchall()
        }
        cursor.close()
        return render(request, 'Inventario/ver_ventas.html', context)
    else:
        return redirect("/cerrar_sesion")

def ver_cuentas_p_c(request):
    if request.session.get('email'):
        cursor = connection.cursor()
        cursor.callproc("MOSTRAR_VENTAS_MOD")
        context = {
            'movimientos': cursor.fetchall()
        }
        cursor.close()
        return render(request, 'Inventario/ver_cuentas_pc.html', context)
    else:
        return redirect("/cerrar_sesion")

def ver_otros(request):
    if request.session.get('email'):
        cursor = connection.cursor()
        cursor.callproc("MOSTRAR_MOV_IND")
        context = {
            'movimientos': cursor.fetchall()
        }
        cursor.close()
        return render(request, 'Inventario/ver_otros.html', context)
    else:
        return redirect("/cerrar_sesion")
