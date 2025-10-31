from django.shortcuts import render
from django.views.generic import *

# Create your views here.
class AboutView(TemplateView):
    template_name = "pages/about.html"

