from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import UserProfileManager
# Create your models here.

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model For Users in the System"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrive Full Name Of User """
        return self.name

    def get_short_name(self):
        """Retrive short Name Of User """
        return self.name

    def __str__(self):
        """Return String Representation of our user """
        return self.email
