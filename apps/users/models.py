from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )

    email = models.EmailField(unique=True)

    name = models.CharField('Nombre', max_length=100)

    job = models.CharField(
        'Trabajo',
        max_length=30, 
        blank=True
    )

    gender = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES, 
        blank=True
    )

    birthdate = models.DateField(
        'Fecha de nacimiento', 
        blank=True,
        null=True
    )

    is_staff = models.BooleanField(default=False)

    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def get_short_name(self):
        return self.email
    
    def get_full_name(self):
        return self.name
