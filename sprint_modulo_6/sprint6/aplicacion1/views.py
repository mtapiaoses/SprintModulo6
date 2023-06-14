from django.shortcuts import render, redirect

from aplicacion1.forms import (
    LoginAportadorForm, LoginGestorFinanzas, LoginBeneficiadoForm,
    RegistroAportadorForm, RegistroBeneficiadoForm, RegistroGestorFinanzasForm,
    AgregarAporteForm)

from aplicacion1.models import (
    PerfilAportador, PerfilBeneficiado, PerfilGestorFinanzas,
    Finanzas, Aporte, Beneficio)

from django.http import HttpResponse

from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# HOME


def home(request):
    context = {'clave': 'valor'}
    return render(request, 'home.html', context)


# REGISTROS
def registro_aportadores(request):
    if request.method == 'POST':

        formulario = RegistroAportadorForm(request.POST)

        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data['nombre_usuario']
            nombre = formulario.cleaned_data['nombre']
            apellido = formulario.cleaned_data['apellido']
            email = formulario.cleaned_data['email']
            clave = formulario.cleaned_data['clave']
            direccion = formulario.cleaned_data['direccion']
            telefono = formulario.cleaned_data['telefono']
            ciudad = formulario.cleaned_data['ciudad']
            
            usuario = User(
                username=nombre_usuario,
                first_name=nombre,
                last_name=apellido,
                email=email)
            usuario.password = make_password(clave)
            usuario.save()

            perfil = PerfilAportador(
                user=usuario,
                direccion=direccion,
                ciudad=ciudad,
                telefono=telefono)
            perfil.save()

        return HttpResponse(f"{nombre} {apellido} {email} {direccion} {telefono} {ciudad}",)

    else:
        formulario = RegistroAportadorForm()
        return render(request, 'registro_aportadores.html', context={'formulario': formulario})


def registro_beneficiados(request):
    if request.method == 'POST':
        print("REGISTRO BENEFICIADOS")

        formulario = RegistroBeneficiadoForm(request.POST)

        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data['nombre_usuario']
            nombre = formulario.cleaned_data['nombre']
            apellido = formulario.cleaned_data['apellido']
            email = formulario.cleaned_data['email']
            edad = formulario.cleaned_data['edad']
            clave = formulario.cleaned_data['clave']
            direccion = formulario.cleaned_data['direccion']
            telefono = formulario.cleaned_data['telefono']
            ciudad = formulario.cleaned_data['ciudad']

            usuario = User(
                username=nombre_usuario,
                first_name=nombre,
                last_name=apellido,
                email=email)
            usuario.password = make_password(clave)
       
       
            usuario.save()

            perfil = PerfilBeneficiado(
                user=usuario,
                direccion=direccion,
                ciudad=ciudad,
                telefono=telefono,
                edad=edad)
            perfil.save()

        return HttpResponse(f"{nombre} {apellido} {email} {direccion} {telefono} {ciudad}",)

    else:
        formulario = RegistroBeneficiadoForm()
        return render(request, 'registro_beneficiados.html', context={'formulario': formulario})


def registro_gestor_finanzas(request):
    if request.method == 'POST':

        formulario = RegistroGestorFinanzasForm(request.POST)

        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data['nombre_usuario']
            nombre = formulario.cleaned_data['nombre']
            apellido = formulario.cleaned_data['apellido']
            email = formulario.cleaned_data['email']
            clave = formulario.cleaned_data['clave']
            direccion = formulario.cleaned_data['direccion']
            telefono = formulario.cleaned_data['telefono']
            ciudad = formulario.cleaned_data['ciudad']

            usuario = User(
                username=nombre_usuario,
                first_name=nombre,
                last_name=apellido,
                email=email)
            usuario.save()

            perfil = PerfilGestorFinanzas(
                user=usuario,
                direccion=direccion,
                ciudad=ciudad,
                telefono=telefono)
            perfil.save()

        return HttpResponse(f"{nombre} {apellido} {email} {direccion} {telefono} {ciudad}",)

    else:
        formulario = RegistroGestorFinanzasForm()
        return render(request, 'registro_gestor_finanzas.html', context={'formulario': formulario})

# LOGIN

def login_aportador(request):
    if request.method == 'POST':

        formulario = LoginAportadorForm(request.POST)

        print(formulario['clave'].value())

        if formulario.is_valid():
            username = formulario.cleaned_data['usuario']
            password = formulario.cleaned_data['clave']

            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:

                login(request, user)
                return redirect('/perfil_aportador/')
            else:
                pass
            return redirect('/')
    else:
        formulario = LoginAportadorForm()
        return render(request, 'login_aportador.html', {'formulario': formulario})


def login_beneficiado(request):
    if request.method == 'POST':

        formulario = LoginBeneficiadoForm(request.POST)

        print(formulario['clave'].value())

        if formulario.is_valid():
            username = formulario.cleaned_data['usuario']
            password = formulario.cleaned_data['clave']

            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:

                login(request, user)
                return redirect('/perfil_beneficiado/')
            else:
                pass
            return redirect('/')
    else:
        formulario = LoginBeneficiadoForm()
        return render(request, 'login_beneficiado.html', {'formulario': formulario})


def login_gestor_finanzas(request):
    if request.method == 'POST':

        formulario = LoginGestorFinanzas(request.POST)

        print(formulario['clave'].value())

        if formulario.is_valid():
            username = formulario.cleaned_data['usuario']
            password = formulario.cleaned_data['clave']

            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:

                login(request, user)
                return redirect('')
            else:
                pass
            return redirect('/')
    else:
        formulario = LoginGestorFinanzas()
        return render(request, 'login_gestor_finanzas.html', {'formulario': formulario})


# LISTAS

def lista_de_aportadores(request):
    perfiles = PerfilAportador.objects.all()
    return render(request, 'lista_de_aportadores.html', {'perfiles': perfiles})


def lista_de_beneficiados(request):
    perfiles = PerfilBeneficiado.objects.all()
    return render(request, 'lista_de_beneficiados.html', {'perfiles': perfiles})
   # return HttpResponse("HOLA")


# PERFIL
def perfil_aportador(request):
    print('entre perfil aportador')
    formulario = AgregarAporteForm()
    perfil = PerfilAportador.objects.get(user_id=request.user.id)
    aportes = Aporte.objects.filter(aportador_id=perfil.id)
    print(aportes)
    context = {'perfil': perfil,'aportes':aportes,'formulario':formulario}
    return render(request, 'perfil_aportador.html', context)


def perfil_beneficiado(request):
    perfil = PerfilBeneficiado.objects.get(user_id=request.user.id)
    beneficios = Beneficio.objects.filter(beneficiado_id=perfil.id)
    context = {'perfil': perfil,'beneficios':beneficios}
    return render(request, 'perfil_beneficiado.html', context)


def perfil_gestor_finanzas(request):
    perfil = PerfilGestorFinanzas.objects.get(user_id=request.user.id)
    context = {'perfil': perfil}
    return render(request, 'perfil_gestor_finanzas.html', context)

def agregar_monto(request):
        if request.method == 'POST':

            formulario = AgregarAporteForm(request.POST)
            monto = formulario['monto'].value()    
            perfil = PerfilAportador.objects.get(user_id=request.user.id)
            aporte = Aporte( total=monto, aportador=perfil  )
            aporte.save()
            return redirect('/perfil_aportador/')
            
        

        else:    
            return HttpResponse(" GET")


def logout_view(request):
    print(request.user)
    print('logout')
    logout(request)
    return redirect('/')



def agregar_monto_animo(request):
        if request.method == 'POST':

            formulario = AgregarAporteForm(request.POST)
            monto = formulario['monto'].value()
            perfil = PerfilAportador.objects.get(id=3)
            aporte = Aporte(total=monto, aportador=perfil)
            aporte.save()
            return redirect('/anonimo')

        else:
            return HttpResponse(" GET")
def aporte_anonimo(request):
    formulario = AgregarAporteForm()
    context = { 'formulario': formulario}
    return render(request, 'aporte_anonimo.html', context)
