from django import forms

#LOGIN FORM
class LoginBeneficiadoForm(forms.Form):
    usuario = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    clave = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'w3-input'}))


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

    CHOICES = (
        ('aportador', 'Aportador'),
        ('beneficiado', 'Beneficiado'),
        ('gestor_finanzas', 'Gestor Finanzas')
    )

    grupo = forms.ChoiceField(
        choices=CHOICES, widget=forms.Select(attrs={'class': 'w3-input'}))

    nombre_usuario = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    apellido = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    clave = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'w3-input'}))
    direccion = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    telefono = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    ciudad = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))



class AgregarAporteForm(forms.Form):
        monto = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'w3-input','placeholder':'Ingresa la cantidad'}))


class MensajeForm(forms.Form):
    mensaje= forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
