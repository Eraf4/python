from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def carga_localidad(request):
    localidad = loader.get_template('form.html')
    documento = localidad.render()
    return HttpResponse(documento)