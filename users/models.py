import uuid
from venv import create
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# import uuid
# Create your models here.

class customUser(AbstractUser):
    # uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    types = (('admin','Admin'),('user','User'))
    user_type = models.CharField(max_length=100, choices=types)
    # created_At = models.DateField(auto_now=True)