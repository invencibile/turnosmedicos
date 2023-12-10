# Generated by Django 5.0 on 2023-12-10 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnosmedicos', '0003_horario_matricula_profesional_especialidad_listado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='especialidad',
            name='id_espe',
            field=models.IntegerField(null=True, verbose_name='código especialidad'),
        ),
        migrations.AddField(
            model_name='horario',
            name='duracion',
            field=models.IntegerField(default=20, verbose_name='duración de consulta'),
        ),
        migrations.AddField(
            model_name='horario',
            name='hora_desde',
            field=models.TimeField(default='2023-12-11 12:00', verbose_name='Horario del turno'),
        ),
        migrations.AddField(
            model_name='horario',
            name='hora_hasta',
            field=models.TimeField(default='2023-12-11 12:00', verbose_name='hora de fin de consulta'),
        ),
        migrations.AddField(
            model_name='obrasocial',
            name='id_obrasoc',
            field=models.IntegerField(default='1', verbose_name='codigo obra social'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='obra_social_listado',
            field=models.IntegerField(default=1, verbose_name='obra/s social/es'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesional',
            name='obra_social',
            field=models.IntegerField(default=0, verbose_name='Obra Social'),
        ),
        migrations.AlterField(
            model_name='turno',
            name='hora_desde',
            field=models.TimeField(default='2023-12-11 12:00', verbose_name='Horario del turno'),
        ),
    ]
