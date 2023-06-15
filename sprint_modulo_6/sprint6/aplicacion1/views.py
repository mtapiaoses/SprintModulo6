from django.shortcuts import render, redirect

from aplicacion1.forms import (
    LoginAportadorForm, LoginGestorFinanzas, LoginBeneficiadoForm,
    RegistroAportadorForm,
    AgregarAporteForm, MensajeForm)
from django.contrib.auth.decorators import permission_required
from aplicacion1.models import (
    PerfilAportador, PerfilBeneficiado, PerfilGestorFinanzas,
    Finanzas, Aporte, Beneficio, Mensaje)

from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db.models import Sum, Count

from django.contrib.auth.models import Group
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
            grupo = formulario.cleaned_data['grupo']
            usuario = User(
                username=nombre_usuario,
                first_name=nombre,
                last_name=apellido,
                email=email)
            usuario.password = make_password(clave)
            usuario.save()

            if grupo == 'aportador':
                perfil = PerfilAportador(
                    user=usuario,
                    direccion=direccion,
                    ciudad=ciudad
                )
                perfil.save()
                grupo = Group.objects.get(name='aportadores')
                usuario.groups.add(grupo)

            if grupo == 'beneficiado':
                perfil = PerfilBeneficiado(
                    user=usuario,
                    direccion=direccion,
                    ciudad=ciudad,
                    telefono=telefono)
                perfil.save()
                grupo = Group.objects.get(name='beneficiados')
                usuario.groups.add(grupo)

            if grupo == 'gestor_finanzas':
                perfil = PerfilGestorFinanzas(
                    user=usuario,
                    direccion=direccion,
                    ciudad=ciudad
                )
                perfil.save()
                grupo = Group.objects.get(name='gestor_finanzas')
                usuario.groups.add(grupo)

        return redirect("/logueate/")

    else:
        formulario = RegistroAportadorForm()
        return render(request, 'registro_aportadores.html', context={'formulario': formulario})


# LOGIN


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

                perfil_aportador = PerfilAportador.objects.filter(
                    user_id=user.id).count()
                perfil_beneficiado = PerfilBeneficiado.objects.filter(
                    user_id=user.id).count()
                perfil_gestor_finanzas = PerfilGestorFinanzas.objects.filter(
                    user_id=user.id).count()

                if perfil_aportador==1 and perfil_beneficiado == 0 and perfil_gestor_finanzas == 0:
                    return redirect('/perfil_aportador/')
                if perfil_aportador == 0 and perfil_beneficiado == 1 and perfil_gestor_finanzas == 0:
                    return redirect('/perfil_beneficiado/')
                if perfil_aportador == 0 and perfil_beneficiado == 0 and perfil_gestor_finanzas == 1:
                    return redirect('/perfil_gestor_finanzas/')

               
            else:
                pass
            return redirect('/')
    else:
        formulario = LoginBeneficiadoForm()
        return render(request, 'login_beneficiado.html', {'formulario': formulario})




# LISTAS
@permission_required('aplicacion1.permiso_finanzas')
def lista_de_aportadores(request):
    perfiles = PerfilAportador.objects.all()
    return render(request, 'lista_de_aportadores.html', {'perfiles': perfiles})


@permission_required('aplicacion1.permiso_finanzas')
def lista_de_beneficiados(request):
    perfiles = PerfilBeneficiado.objects.all()
    return render(request, 'lista_de_beneficiados.html', {'perfiles': perfiles})
   # return HttpResponse("HOLA")


# PERFIL
@permission_required('aplicacion1.permiso_aportador')
def perfil_aportador(request):
    print('entre perfil aportador')
    formulario = AgregarAporteForm()
    perfil = PerfilAportador.objects.get(user_id=request.user.id)
    aportes = Aporte.objects.filter(aportador_id=perfil.id)
    print(aportes)
    context = {'perfil': perfil, 'aportes': aportes, 'formulario': formulario}
    return render(request, 'perfil_aportador.html', context)


@permission_required('aplicacion1.permiso_beneficiado')
def perfil_beneficiado(request):
    perfil = PerfilBeneficiado.objects.get(user_id=request.user.id)
    beneficios = Beneficio.objects.filter(beneficiado_id=perfil.id)
    context = {'perfil': perfil, 'beneficios': beneficios}
    return render(request, 'perfil_beneficiado.html', context)


@permission_required('aplicacion1.permiso_finanzas')
def perfil_gestor_finanzas(request):
    formulario_mensaje = MensajeForm()
    aportes = Aporte.objects.all()
    beneficio = Beneficio.objects.all()
    aportadores = PerfilAportador.objects   .all()
    beneficiados = PerfilBeneficiado.objects.all()
    total_aporte = Aporte.objects.aggregate(total=Sum('total'))
    print(total_aporte['total'])
    context = {'aportes': aportes, 'beneficios': beneficio, 'aportadores': aportadores,
               'beneficiados': beneficiados, 'fm': formulario_mensaje, 'total_aporte': total_aporte['total']}
    return render(request, 'perfil_gestor_finanzas.html', context)


def agregar_monto(request):
    if request.method == 'POST':

        formulario = AgregarAporteForm(request.POST)
        monto = formulario['monto'].value()
        perfil = PerfilAportador.objects.get(user_id=request.user.id)
        aporte = Aporte(total=monto, aportador=perfil)
        aporte.save()
        return redirect('/perfil_aportador/')

    else:
        return HttpResponse(" GET")


def logout_view(request):

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
        return redirect('/')

    else:
        return HttpResponse(" GET")


def aporte_anonimo(request):
    formulario = AgregarAporteForm()
    context = {'formulario': formulario}
    return render(request, 'aporte_anonimo.html', context)


@permission_required('aplicacion1.permiso_finanzas')
def entregar_beneficios(request):
    total_aporte = Aporte.objects.aggregate(total=Sum('total'))
    cuenta_de_registros = PerfilBeneficiado.objects.aggregate(
        total=Count('id'))
    beneficiados = PerfilBeneficiado.objects.all()

    if (cuenta_de_registros['total'] > 0):
        beneficio = float(total_aporte['total']/cuenta_de_registros['total'])

        for beneficiado in beneficiados:
            beneficio_perfil = Beneficio(
                beneficiado=beneficiado, total=beneficio)
            beneficio_perfil.save()
            Aporte.objects.filter().delete()
        return redirect('/perfil_gestor_finanzas/')

    else:
        return HttpResponse("AUN NO EXISTE NINGUN REGISTRO")


def aporte_total(request):
    total_aporte = Aporte.objects.aggregate(total=Sum('total'))
    return render(request, 'total.html', {'total': total_aporte['total']})
