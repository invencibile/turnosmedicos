from django.shortcuts import render
from django.http import HttpResponse
# from django.http import views
# Create your views here.
def index(request):
    return HttpResponse("turnos o no médicos")

def turnosmedicos(request):
    return HttpResponse("turnos médicos segunda edicion")
def iniciosesion (request):
    return HttpResponse('aca va el inicio de sesion , usuario y contraseña')
