# Generated by Django 5.0 on 2023-12-09 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnosmedicos', '0006_alter_horario_hora_desde_alter_horario_hora_hasta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='hora_desde',
            field=models.TimeField(default='2023-12-11 12:00', verbose_name='Horario del turno'),
        ),
    ]
