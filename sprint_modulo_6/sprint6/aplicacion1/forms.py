from django import forms

#LOGIN FORM
class LoginBeneficiadoForm(forms.Form):
    usuario = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    clave = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))


class LoginAportadorForm(forms.Form):
    usuario = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    clave = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))


class LoginGestorFinanzas(forms.Form):
    usuario = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    clave = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))

# REGISTROS FOTM
class RegistroAportadorForm(forms.Form):
    nombre_usuario = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    apellido = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    clave = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    confirmacion_clave = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))    
    direccion = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    telefono = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    ciudad = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))


class RegistroBeneficiadoForm(forms.Form):
    nombre_usuario = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    apellido = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    clave = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    confirmacion_clave = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    direccion = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    telefono = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    ciudad = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    edad = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'w3-input'}))


class RegistroGestorFinanzasForm(forms.Form):
    nombre_usuario = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'w3-input'}))
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    apellido = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    clave=forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    confirmacion_clave=forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    direccion = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    telefono = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    ciudad = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))

class AgregarAporteForm(forms.Form):
        monto = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'w3-input','placeholder':'Ingresa la cantidad'}))
