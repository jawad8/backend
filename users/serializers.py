from pyexpat import model
from . import models
from rest_framework import serializers


class createUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.customUser
        fields = ['username', 'password']

