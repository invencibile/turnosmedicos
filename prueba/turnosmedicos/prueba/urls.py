"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path( " ", views.home, name= "home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from turnosmedicos import views
# from . import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include ('turnosmedicos.urls') ),
    # path('index/', views.index, name ="index"),
    # path('turnosmedicos/', views.turnosmedicos, name ="turnosmedicos"),
    # path('form_modif/<pk>', views.PacienteUpdateView.as_view(), name="form_modif"),
    # path('form_borrar/<pk>', views.PacienteUpdateView.as_view(), name="form_borrar"),
    # path('iniciosesion/<pk>', views.PacienteDetailView.as_view(), name="iniciosesion"),
    # path('form/',views.PacienteCreateView.as_view(), name= "form"),
    # path('nuevoprofesional/',views.nuevoprofesional, name= "nuevoprofesional"),
    # path('quienes_somos/',views.quienes_somos, name= "quienes_somos"),
    # path('profesionales/',views.profesionales, name="profesionales"),
    # path('apipage/',views.apipage, name="apipage"),
    # path('contacto/',views.contacto, name="contacto"),
    # path('faq/',views.faq, name="faq"),
    # path('empleo/',views.empleo, name="empleo"),
    # path('terminos/',views.terminos, name="terminos"),
    # path('ubicacion/',views.ubicacion, name="ubicacion"),
    # path('prueba/',views.prueba, name="prueba"),
   
    # path('form_profesional',views.ProfesionalCreateView.as_view(), name='form_profesional'),
    # path('form_especialidad',views.EspecialidadCreateView.as_view(), name='form_especialidad'),
    # path('form_horario',views.HorarioCreateView.as_view(), name='form_horario'),
    # path('form_turno',views.TurnoCreateView.as_view(), name='form_turno'),
    # # path('listadooprofesional',views.ProfesionalListView.as_view(), name='nuevoprofesional'),
    # path('listadopaciente',views.PacienteListView.as_view(), name='paciente_listado'),
    # path('listadoprofesional',views.ProfesionalListView.as_view(), name='listadoprofesional'),
    # path('listadoHorario',views.HorarioListView.as_view(), name='listadoHorario'),
    # path('listadoespecialidad',views.EspecialidadListView.as_view(), name='listadoespecialidad'),
    # path('listadoTurno',views.TurnoListView.as_view(), name='listadoTurno'),
    
]
