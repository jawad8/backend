from django.db import models
from django.conf import settings
# Create your models here.


class LogTable(models.Model):
    log_type = models.CharField(max_length=100)
    log_time = models.DateTimeField(auto_now_add = True)
    log_error = models.CharField(max_length=100)