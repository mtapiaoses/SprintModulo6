from django.contrib import admin
from aplicacion1.models import PerfilAportador, PerfilBeneficiado,PerfilGestorFinanzas, Finanzas, Aporte,Beneficio
# Register your models here.
admin.site.register(PerfilBeneficiado)
admin.site.register(PerfilAportador)
admin.site.register(PerfilGestorFinanzas)
admin.site.register(Finanzas)
admin.site.register(Aporte)
admin.site.register(Beneficio)
