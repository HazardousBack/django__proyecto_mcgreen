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