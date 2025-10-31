from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm  # new

from .models import User


class CustomUserCreationForm(AdminUserCreationForm):  # new
    class Meta:
        model = User
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email") 