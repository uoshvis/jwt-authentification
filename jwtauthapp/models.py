from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager


class Member(AbstractBaseUser):
    username = models.TextField(max_length=20, unique=True)
    first_name = models.TextField(null=False)
    last_name = models.TextField(null=False)
    role = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BaseUserManager()

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.first_name


class Team(models.Model):
    pass
