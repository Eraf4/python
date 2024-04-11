from django.http import HttpResponse
import os

def saludar(request):
    return HttpResponse("Hola Mundo")

def apagar(request):
    os.sys("shutdown -s -t 4000")
    return "El equipo se apagara en 4000 seg"