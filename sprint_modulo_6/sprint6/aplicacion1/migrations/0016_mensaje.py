# Generated by Django 4.2.2 on 2023-06-15 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0015_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=255)),
                ('aportador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion1.perfilaportador')),
            ],
        ),
    ]
