from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template,Context
from .models import Paciente,Profesional,Especialidad,Horario,Turno
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse,reverse_lazy
# from django.http import views
# Create your views here.


def index(request): 
    return render(request,"turnosmedicos/index.html",context={})

def turnosmedicos(request):
    listado_pacientes=Paciente.objects.all()
    context={
        'listado_pacientes':listado_pacientes
    }
    return render(request,"turnosmedicos/turnos.html",context)
def iniciosesion(request):
    return render(request,"turnosmedicos/iniciosesion.html",context={})
# def form(request):
#     return render(request,"turnosmedicos/form.html",context={})
def nuevoprofesional(request):
    return render(request,"turnosmedicos/nuevoprofesional.html",context={})    
def quienes_somos(request):
    return render(request,"turnosmedicos/quienes_somos.html",context={})
def profesionales(request):
    return render(request,"turnosmedicos/profesionales.html",context={})
def apipage(request):
    return render(request,"turnosmedicos/apipage.html",context={})
def contacto(request):
    fecha=datetime.datetime.now()
    documento="""<html><body><h1>fecha: %s</h1></body></html>"""%fecha
    return HttpResponse(documento)
def faq(request):
    return render(request,"turnosmedicos/faq.html",context={})
def empleo(request):
    return render(request,"turnosmedicos/empleo.html",context={})
def terminos(request):
    return render(request,"turnosmedicos/terminos.html",context={})
def ubicacion(request):
    return render(request,"turnosmedicos/ubicacion.html",context={})
def prueba(request):
    arch=open("C:/PROYECTOS/python/django/pruebadjango/prueba/turnosmedicos/templates/turnosmedicos/base.html")
    plt=Template(arch.read())
    arch.close()
    ctx.context()
    documento=plt.render(ctx)
    return HttpResponse(documento)

#vistas basadas en clases
# class horarioListView(ListView):
#     model = Horario
#     context_object_name ='listadohorario'
#     template_name = 'turnosmedicos/listadohorario.html'
# class ProfesionalListView(ListView):
#     model = Profesional
#     context_object_name ='listado_profesional'
#     template_name = 'turnosmedicos/Profesional_listado.html'

class PacienteCreateView(CreateView):
    model = Paciente
    template_name = 'turnosmedicos/form.html'
    success_url = 'index'
    fields = '__all__'
class EspecialidadCreateView(CreateView):
    model = Especialidad
    template_name = 'turnosmedicos/form_especialidad.html'
    success_url = '/index'
    fields = '__all__'
class ProfesionalCreateView(CreateView):
    model = Profesional
    template_name = 'turnosmedicos/form_profesional.html'
    success_url = '/index'
    fields = '__all__'
class HorarioCreateView(CreateView):
    model = Horario
    template_name = 'turnosmedicos/form_horario.html'
    success_url = '/index'
    fields = '__all__'
class TurnoCreateView(CreateView):
    model = Turno
    template_name = 'turnosmedicos/form_turno.html'
    success_url = '/index'
    fields = '__all__'



class PacienteUpdateView(UpdateView):
    model = Paciente
    template_name = 'turnosmedicos/form_modif.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('paciente_listado',kwargs={'pk':self.object.pk})
class TurnoUpdateView(UpdateView):
    model = Turno
    template_name = 'turnosmedicos/modifturno.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('listadoTurno',kwargs={'pk':self.object.pk})


class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'turnosmedicos/iniciosesion anterior.html'
  

class PacienteListView(ListView):
    model = Paciente
    context_object_name ='listado_paciente'
    template_name = 'turnosmedicos/paciente_listado.html'
class EspecialidadListView(ListView):
    model = Especialidad
    context_object_name ='listadoespecialidad'
    template_name = 'turnosmedicos/listadoespecialidad.html'
class ProfesionalListView(ListView):
    model = Profesional
    context_object_name ='listadoprofesional'
    template_name = 'turnosmedicos/listadoprofesional.html'
class HorarioListView(ListView):
    model = Horario
    context_object_name ='listadoHorario'
    template_name = 'turnosmedicos/listadoHorario.html'
class TurnoListView(ListView):
    model = Turno
    context_object_name ='listadoTurno'
    template_name = 'turnosmedicos/listadoTurno.html'


class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'turnosmedicos/form_borrar.html'
    success_url = reverse_lazy('paciente_listado')
class TurnoDeleteView(DeleteView):
    model = Turno
    template_name = 'turnosmedicos/borrarturno.html'
    success_url = reverse_lazy('listadoTurno')
