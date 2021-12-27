from django.shortcuts import redirect, render
from django.db import connection

def usuarios(request):
    if request.session.get("email"):
        if request.session.get("privilegio") == 'ADM-IN1':
            context = {
                'privilegio': request.session.get("privilegio")
            }
            try:
                cursor = connection.cursor()
                cursor.callproc("MOSTRAR_USUARIOS")
                context["usuarios"] = cursor.fetchall()
            finally:
                cursor.close()
            return render(request, "permisos_admin/ver_usuarios.html", context)
        else:
            return redirect("/Inventario_general")
    else:
        return redirect("/cerrar_sesion")

def auditoria(request):
    if request.session.get('email'):
        if request.session.get("privilegio") == 'ADM-IN1' or request.session.get("privilegio") == 'JEFE':
            cursor = connection.cursor()
            cursor.callproc("Mostrar_AUDITORIA")
            context = {
                'datos_audi': cursor.fetchall(),
            }
            return render(request, 'auditoria.html', context)
    return redirect("/cerrar_sesion")