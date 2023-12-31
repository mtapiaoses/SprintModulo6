# Generated by Django 4.2.2 on 2023-06-13 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplicacion1', '0002_delete_finanzas'),
    ]

    operations = [
        migrations.CreateModel(
            name='GestorFinanzas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Finanzas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_beneficios_entregados', models.IntegerField()),
                ('total_aportes_entregados', models.IntegerField()),
                ('aportes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion1.aporte')),
                ('beneficios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion1.beneficio')),
            ],
        ),
    ]
