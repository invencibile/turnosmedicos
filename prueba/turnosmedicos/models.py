from django.db import models


class Profesional(models.Model):
         matricula = models.IntegerField(verbose_name='Nro. de matrícula')
         nombre = models.CharField(max_length=100, verbose_name='Nombre')
         apellido = models.CharField(max_length=100, verbose_name='Apellido')
         mail_prof=models.EmailField(max_length=100, verbose_name='E-mail')
         telefono_prof=models.IntegerField(verbose_name='Teléfono')
         costo_consulta=models.FloatField(verbose_name='Precio de consulta')
         especialidad_listado = models.IntegerField(verbose_name='Especialidad',default=00000)
         obra_social = models.IntegerField(verbose_name='Obra Social',default=00000)
        #  horario_listado=[]
def __str__(self):
      return f'{self.matricula}{self.nombre}{self.apellido}{self.especialidad}{self.costo_consulta}{self.telefono_prof}{self.mail_prof}{self.obra_social}'
class Paciente(models.Model):
         dni = models.IntegerField(verbose_name='Documento de Identidad')
         nombre = models.CharField(max_length=100, verbose_name='Nombre')
         apellido = models.CharField(max_length=100, verbose_name='Apellido')
         sexo = models.CharField(max_length=20, verbose_name='Sexo')
         nacimiento = models.DateTimeField(verbose_name='Fecha de nacimiento')
         mail_paciente=models.EmailField(max_length=100, verbose_name='E-mail')
         telefono_paciente=models.IntegerField(verbose_name='Teléfono')
         provincia = models.CharField(max_length=100)
         partido = models.CharField(max_length=100)
         ciudad = models.CharField(max_length=100)
         calle = models.CharField(max_length=100)
         contraseña=models.CharField(max_length=50, verbose_name='Contraseña', null=True)
         obra_social_listado = models.IntegerField(verbose_name='obra/s social/es')
        #  turno=[]
def __str__(self):
      return f'{self.dni}{self.nombre}{self.apellido}{self.sexo}{self.nacimiento}{self.telefono_paciente}{self.mail_paciente}{self.provincia}{self.partido}{self.ciudad}{self.calle}{self.obra_social_listado}{self.contraseña}'
class Especialidad(models.Model):
         id_espe= models.IntegerField(verbose_name='código especialidad', null=True)
         nombre_especialidad = models.CharField(max_length=100, verbose_name='Especialidad')
def __str__(self):
        return f'{self.id_espe}{self.nombre_especialidad}'
class ObraSocial(models.Model):
         id_obrasoc =models.IntegerField(verbose_name='codigo obra social',default='1')
         nombre_obrasoc=models.CharField(max_length=100, verbose_name='Obra Social')
         tarifa=models.FloatField(verbose_name='Precio de consulta')
def __str__(self):
        return f'{self.id_obrasoc}{self.nombre_obrasoc}{self.tarifa}'
class Horario(models.Model):
         diasem=models.DateField(verbose_name='Día de la semana')
         hora_desde=models.TimeField(verbose_name='Horario del turno',default='2023-12-11 12:00')
         duracion=models.IntegerField(verbose_name='duración de consulta',default=20)
         hora_hasta=models.TimeField(verbose_name='hora de fin de consulta',default='2023-12-11 12:00')
         matricula= models.IntegerField(verbose_name='Nro. de matrícula',default=00000)
def __str__(self):
        return f'{self.diasem}{self.hora_desde}{self.duracion}{self.hora_hasta}{self.matricula}'
class Turno(models.Model):
         diasem=models.DateField(verbose_name='Día de la semana')
         hora_desde=models.TimeField(verbose_name='Horario del turno',default='2023-12-11 12:00')
         duracion=models.IntegerField(verbose_name='Duración del turno')
         matricula= models.IntegerField(verbose_name='Nro. de matrícula',default=00000)
         dni=models.IntegerField(verbose_name='Documento de Identidad',default=00000)
def __str__(self):
        return f'{self.diasem}{self.hora_desde}{self.duracion}{self.matricula}{self.dni}'
