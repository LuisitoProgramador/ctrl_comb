from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path("primer-vista/", primer_vista, name="primer_vista"),
    path("", HomeView.as_view(), name="home"),
]