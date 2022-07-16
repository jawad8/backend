from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class customUser(AbstractUser):
    types = (('admin','Admin'),('user','User'))
    user_type = models.CharField(max_length=100, choices=types)