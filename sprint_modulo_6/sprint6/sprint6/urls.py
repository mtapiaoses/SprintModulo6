
from django.contrib import admin
from django.urls import path
from aplicacion1.views import perfil_beneficiado
from aplicacion1.views import (
    home, 
    login_beneficiado,
    lista_de_aportadores, lista_de_beneficiados,
    registro_aportadores,
    perfil_aportador,perfil_gestor_finanzas,perfil_beneficiado,
    agregar_monto, logout_view,
    agregar_monto_animo,aporte_anonimo,
    entregar_beneficios,
    aporte_total
    )
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
    #INICIO Y ADMIN
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    #LOGIN
    path('login/', login_beneficiado, name='login'),
    # #LISTAS
    path('aportadores/',lista_de_aportadores,name="aportadores" ),
    path('beneficiados/',lista_de_beneficiados,name="beneficiados"),
    #REGISTRO    
    path('registro_aportadores/',registro_aportadores,name="reg_aportadores"),

    #PERFILES
    path('perfil_gestor_finanzas/',perfil_gestor_finanzas,name='perfil_gestor_finanzas'),
    path('perfil_aportador/', login_required(perfil_aportador),name='perfil_aportador'),
    path('perfil_beneficiado/',perfil_beneficiado,name='perfil_benefiado'),
    #AGREGAR APORTE
    path('agregar_monto/', agregar_monto, name='agregar_monto'),
    path('agregar_monto_anonimo/', agregar_monto_animo, name='agregar_monto_anonimo'),
    #LOGOUT
    path('logout/', logout_view, name='logout_view'),
    path('aporte_anonimo/',aporte_anonimo,name="aporte_anonimo"),
    #ENTREGAR BENEFICIO
    path('entregar_beneficios/', entregar_beneficios, name="entregar_beneficio"),
    path('aporte_total/',aporte_total,name="aporte_total"),
    path('logueate/', TemplateView.as_view(template_name='alogin.html'),
         name='nombre_vista'),
  

    ]
    
    
