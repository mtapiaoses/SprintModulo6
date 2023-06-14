from django.db import models
from django.contrib.auth.models import User
#PERFILES

class PerfilAportador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)


class Meta:
    permissions = [
        ("permiso_aportador", "Puede acceder a las interfaces de aportador")
    ]
    def __str__(self):
        return f"{self.user.first_name} | {self.user.last_name} | {self.edad} | {self.ciudad} "


class PerfilBeneficiado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.first_name} | {self.user.last_name} | {self.edad} | {self.ciudad} "


class Meta:
    permissions = [
        ("permiso_beneficiado", "Puede acceder a las interfaces de beneficiado")
    ]

class PerfilGestorFinanzas(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.first_name} | {self.user.last_name} | {self.edad} | {self.ciudad} "


class Meta:
    permissions = [
        ("permiso_finanzas", "Puede acceder a las interfaces de finanzas")
    ]


#FINANZAS
class Beneficio(models.Model):
    total = models.IntegerField()
    beneficiado = models.ForeignKey(PerfilBeneficiado, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)


class Aporte(models.Model):
    total = models.IntegerField()
    aportador = models.ForeignKey(PerfilAportador, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)

class Finanzas(models.Model):

    beneficios = models.ForeignKey(Beneficio, on_delete=models.CASCADE)
    aportes = models.ForeignKey(Aporte, on_delete=models.CASCADE)
    total_beneficios_entregados = models.IntegerField()
    total_aportes_entregados = models.IntegerField()
    

