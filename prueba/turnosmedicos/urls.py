from django.urls import path
from . import views
urlpatterns =[
    path('', views.index, name ='index'),
    path('', views.turnosmedicos, name='turnosmedicos'),
    path('',views.iniciosesion, name='iniciosesion'),
    # path('',views.form, name='form'),
    # path('',views.quienes_somos, name='quienes_somos'),
    # path('',views.profesionales, name='profesionales'),
    # path('',views.apipage, name='apipage'),
    # path('',views.contacto, name='contacto'),
    # path('',views.faq, name='faq'),
    # path('',views.empleo, name='empleo'),
    # path('',views.terminos, name='terminos'),
    # path('',views.ubicacion, name='ubicacion'),
]