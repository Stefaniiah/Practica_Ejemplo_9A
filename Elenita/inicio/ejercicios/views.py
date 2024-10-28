from django.shortcuts import render
from .servicios import solicitar
from .servicios import obtener_mensaje

def principal(request):
    return render(request,"ejercicios/principal.html",{'datos':solicitar()})

def mensaje(request):
    return render(request, "ejercicios/mensaje.html", {'datos': obtener_mensaje()})