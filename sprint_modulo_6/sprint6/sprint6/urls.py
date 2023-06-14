
from django.contrib import admin
from django.urls import path
from aplicacion1.views import perfil_beneficiado
from aplicacion1.views import (
    home, 
    login_aportador,login_beneficiado,login_gestor_finanzas,
    lista_de_aportadores, lista_de_beneficiados,
    registro_aportadores,registro_beneficiados,registro_gestor_finanzas,
    perfil_aportador,perfil_gestor_finanzas,perfil_beneficiado,
    agregar_monto, logout_view,
    agregar_monto_animo,aporte_anonimo
    )
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #INICIO Y ADMIN
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    #LOGIN
    path('login_aportador/', login_aportador, name='login_socio'),
    path('login_beneficiado/', login_beneficiado, name='login_socio'),
    path('login_gestor_finanzas/', login_gestor_finanzas, name='login_socio'),
    #LISTAS
    path('aportadores/',lista_de_aportadores,name="aportadores" ),
    path('beneficiados/',lista_de_beneficiados,name="beneficiados"),
    #REGISTRO    
    path('registro_aportadores/',registro_aportadores,name="reg_aportadores"),
    path('registro_beneficiados/', registro_beneficiados, name="reg_beneficiados"),
    path('registro_gestor_finanzas/', registro_gestor_finanzas, name="reg_beneficiados"),
    #PERFILES
    path('perfil_gestion_finanzas/',perfil_gestor_finanzas,name='perfil_gestor_finanzas'),
    path('perfil_aportador/', login_required(perfil_aportador),name='perfil_aportador'),
    path('perfil_beneficiado/',perfil_beneficiado,name='perfil_benefiado'),
    #AGREGAR APORTE
    path('agregar_monto/', agregar_monto, name='agregar_monto'),
    path('agregar_monto_anonimo/', agregar_monto_animo, name='agregar_monto_anonimo'),
    #LOGOUT
    path('logout/', logout_view, name='logout_view'),
    path('aporte_anonimo/',aporte_anonimo,name="aporte_anonimo")
  

    ]
    
    
