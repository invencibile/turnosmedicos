# Generated by Django 4.2.7 on 2023-12-07 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnosmedicos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='contraseña',
            field=models.CharField(max_length=50, null=True, verbose_name='Contraseña'),
        ),
    ]
