from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
# Create your views here.

class RegisterUserView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')  # Redirect to login page after successful registration
    template_name = 'users/register.html'