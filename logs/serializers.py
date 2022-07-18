from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from . import models
import json

class GetLogsSerializer(serializers.ModelSerializer):
    log_type = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.LogTable
        fields = '__all__'
        
    def get_log_type(self,obj):
        return obj.get_log_type_display()