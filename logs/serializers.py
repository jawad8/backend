from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from . import models
from datetime import datetime
import json

class GetLogsSerializer(serializers.ModelSerializer):
    log_type = serializers.SerializerMethodField(read_only=True)
    log_time = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = models.LogTable
        fields = '__all__'
        
    def get_log_type(self,obj):
        return obj.get_log_type_display()

    def get_log_time(self,obj):
        return obj.log_time.strftime("%m/%d/%Y, %H:%M:%S")