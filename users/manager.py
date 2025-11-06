from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    """
    Custom user manager where email is the unique identifier
    for authentication instead of usernames.
    """

    def _create_user(self, email, username, first_name, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError(_('The Email must be set'))
        if not first_name:
            raise ValueError(_('The First Name must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, 
                          username=username, 
                          first_name=first_name,
                          last_login=now, 
                          **extra_fields
                          )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, username, first_name, password, **extra_fields):
        return self._create_user(email, username, first_name, password, **extra_fields)

    def create_superuser(self, email, username, first_name, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(email, username, first_name, password, **extra_fields)


