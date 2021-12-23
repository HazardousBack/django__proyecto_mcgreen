from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Puestos, Privilegios

ELEGIR_ROL = {
    ('ADM-IN1', 'Administrador'),
    ('JEFE', 'Jefe'),
    ('EMPLEADO', 'Empleado'),
}
ELEGIR_EXT_EMAIL = {
    ('@sigssmac.com.mx', '@sigssmac.com.mx'),
    ('@fluidosmcgreen.com.mx', '@fluidosmcgreen.com.mx')
}

class formulario_proveedor(forms.Form):
    Identificador = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Identificador'
    }))
    proveedor = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control mt-3',
        'placeholder': 'Nombre'
    }))
    telefono = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'class': 'form-control mt-3',
        'placeholder': 'Teléfono'
    }))
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control mt-3',
        'placeholder': 'Email'
    }))

class formulario_cliente(forms.Form):
    Identificador = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Identificador'
    }))
    cliente = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control mt-3',
        'placeholder': 'Nombre'
    }))
    direccion = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control mt-3',
        'placeholder': 'Dirección'
    }))
    telefono = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'class': 'form-control mt-3',
        'placeholder': 'Teléfono'
    }))
    email = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control mt-3',
        'placeholder': 'Email'
    }))

class Formulario_registro(forms.Form):
    matricula = forms.CharField(max_length=20, label="Matricula", widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    nombre_usuario = forms.CharField(max_length=50, label="Nombre", widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    ap_p = forms.CharField(label="Apellido paterno", widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    ap_m = forms.CharField(label="Apellido materno", widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    sl_puestos = forms.ModelChoiceField(label="Puestos", queryset=Puestos.objects.all(), widget=forms.Select(attrs={
        'class': 'form-select',
    }))
    email = forms.CharField(label="Email", widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    slemail = forms.ChoiceField(choices=ELEGIR_EXT_EMAIL, widget=forms.Select(attrs={
        'class': 'form-select'
    }))
    contra = forms.CharField(label="Contraseña", widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    rol = forms.ChoiceField(label="Rol", choices=ELEGIR_ROL, widget=forms.RadioSelect(attrs={
        'class': 'form-check-input'
    }))
