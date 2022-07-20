from django.db import models
from django.conf import settings

# Table for storing the logs
class LogTable(models.Model):
    types_log = (('0', 'not_set'), ('20', 'info'), ('40', 'error'),
                 ('10', 'debug'), ('50', 'critical'), ('30', 'warning'))
    log_type = models.CharField(max_length=100, choices=types_log)
    log_time = models.DateTimeField(auto_now_add=True)
    log_error_Message = models.TextField(default='')

    def __str__(self):
        return self.log_error_Message
