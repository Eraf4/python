from django.shortcuts import render
from django.http import HttpResponse
from .models import Cancion

# Create your views here.

def inicio(request):
    lista_cancion = Cancion.objects.all()
    return render(request,'index.html',{"canciones":lista_cancion})