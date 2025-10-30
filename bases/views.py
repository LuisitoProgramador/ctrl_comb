from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def primer_vista(request):
    return HttpResponse("<h1>¡Hola, esta es la primera vista!</h1>")

