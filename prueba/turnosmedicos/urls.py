from django.urls import path
from . import views
urlpatterns =[
   
    path('index', views.index, name ='index'),
    path('turnos', views.turnosmedicos, name='turnosmedicos'),
    path('iniciosesion', views.iniciosesion, name='iniciosesion'),
    
    path('form_modif/<pk>', views.PacienteUpdateView.as_view(), name="form_modif"),
    path('modifturno/<pk>', views.TurnoUpdateView.as_view(), name="modifturno"),
  
    path('quienes_somos',views.quienes_somos, name='quienes_somos'),
    path('profesionales',views.profesionales, name='profesionales'),
    path('apipage',views.apipage, name='apipage'),
    path('contacto',views.contacto, name='contacto'),
    path('faq',views.faq, name='faq'),
    path('empleo',views.empleo, name='empleo'),
    path('terminos',views.terminos, name='terminos'),
    path('ubicacion',views.ubicacion, name='ubicacion'),
    path('prueba',views.prueba, name='prueba'),

    path('form',views.PacienteCreateView.as_view(), name='form'),
    path('form_profesional',views.ProfesionalCreateView.as_view(), name='form_profesional'),
    path('form_especialidad',views.EspecialidadCreateView.as_view(), name='form_especialidad'),
    path('form_horario',views.HorarioCreateView.as_view(), name='form_horario'),
    path('form_turno',views.TurnoCreateView.as_view(), name='form_turno'),
   path('iniciosesion anterior/<pk>', views.PacienteDetailView.as_view(), name='iniciosesion anterior'),
  
  
    # path('listadoprofesional',views.ProfesionalListView.as_view(), name='nuevoprofesional'),
    path('listadopaciente',views.PacienteListView.as_view(), name='paciente_listado'),
    path('listadoprofesional',views.ProfesionalListView.as_view(), name='listadoprofesional'),
    path('listadoHorario',views.HorarioListView.as_view(), name='listadoHorario'),
    path('listadoespecialidad',views.EspecialidadListView.as_view(), name='listadoespecialidad'),
    path('listadoTurno',views.TurnoListView.as_view(), name='listadoTurno'),

    path('form_borrar/<pk>', views.PacienteDeleteView.as_view(), name="form_borrar"),   
    path('borrarTurno/<pk>', views.PacienteDeleteView.as_view(), name="borrarturno"),   
]