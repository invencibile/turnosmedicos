# Generated by Django 5.0 on 2023-12-09 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnosmedicos', '0003_horario_matricula_profesional_especialidad_listado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='hora_desde',
            field=models.TimeField(verbose_name='Horario del turno'),
        ),
    ]
