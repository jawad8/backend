from django.contrib import admin
from . models import LogTable
# Register your models here.


class logTableadmin(admin.ModelAdmin):
    readonly_fields = ('log_time',)

admin.site.register(LogTable, logTableadmin)
