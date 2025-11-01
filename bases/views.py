from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *

# Create your views here.

def primer_vista(request):
    return HttpResponse("<h1>¡Hola, esta es la primera vista!</h1>")

class HomeView(TemplateView):
    template_name = "bases/home.html"


