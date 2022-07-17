from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from . import models
import json

class GetLogsSerializer(serializers.ModelSerializer):
    # log_type = 
    class Meta:
        model = models.LogTable
        fields = '__all__'
