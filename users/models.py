from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models
from .manager import CustomUserManager
# Create your models here.

class User(AbstractUser, PermissionsMixin):
    email = models.EmailField( unique=True)
    username = models.CharField(_('username'), max_length=150, unique=True)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_superuser = models.BooleanField(_('superuser status'), default=False)

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return self.email
 