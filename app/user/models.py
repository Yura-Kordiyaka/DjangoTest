from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import CustomUserManager


# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    objects = CustomUserManager()
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    first_name = models.CharField(max_length=255, null=True)
