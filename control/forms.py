from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib import messages

class gastoDiarioForm(forms.ModelForm):
    
    class Meta:
        model = Gastosdiarios
        fields = '__all__'
        labels = {
            'descripcion' : 'Descripción',
            'gasto' : 'Gasto',
        }

class marcaForm(forms.ModelForm):
    
    class Meta:
        model = Marcas
        fields = '__all__'
        labels = {
            'nommarca' : 'Nombre de la marca',
        }

class mercanciaForm(forms.ModelForm):
    
    class Meta:
        model = Mercancia
        fields = '__all__'
        labels = {
            'idreferencia' : 'Nombre de la referencia',
        }

class radiadorForm(forms.ModelForm):
    
    class Meta:
        model = Radiadores
        fields = '__all__'
        labels = {
            'referencia' : 'Nombre de referencia',
            'preciocosto' : 'Precio de costo',
            'precioventa' : 'Precio de venta',
        }

class referenciaForm(forms.ModelForm):
    
    class Meta:
        model = Referencia
        fields = '__all__'
        labels = {
            'nomreferencia' : 'Nombre de referencia',
            'idmarcas' : 'Marca',
            'numreferencia' : 'Numero de referencia',
            'posicion' : 'Posición',
            'preciocosto' : 'Precio de costo',
            'idubicacion' : 'Ubicacion de la referencia',
            'idposicion' : 'Lugar posicionado',
            'idempresa' : 'Empresa',
        }

class UsuarioForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo electronico',
        }
        widgets = {
            'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
            'apellido': forms.TextInput(attrs = {'class': 'form-control'}),
            'correo': forms.EmailInput(attrs = {'class': 'form-control'}),
            'telefono': forms.TextInput(attrs = {'class': 'form-control'}),
            'is_active': forms.CheckboxInput(),
        }
    password2 = forms.CharField(label = 'Contraseña de confirmacion', widget = forms.PasswordInput())

class ventaDiariaForm(forms.ModelForm):
    class Meta:
        model = Ventadiaria
        fields = '__all__'
        labels = {
            'descripcion' : 'Descripción',
            'precioventa' : 'Precio de Venta',
            'ventatanque' : 'Venta de Tanque',
        }