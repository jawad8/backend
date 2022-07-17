from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models, serializers

from logs import models

# Create your views here.
# create user API
@api_view(['POST'])
def createUser(request):
    try:
        reqData = {
            "Username":test,
            "password":jquury123,
            "user_type":"user"
        }
        reqData = request.data
        user_obj = models.customUser()
    
    except Exception as e:
        print(e)
        return Response(False,status=400)