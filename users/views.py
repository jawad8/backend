from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models, serializers

# Create your views here.
# create user API
@api_view(['POST'])
def createUser(request):
    try:
        reqData = request.data
        print(reqData)
        user_obj = models.customUser(username=reqData['Username'],password=reqData['password'], user_type=reqData['user_type'])
        print(user_obj)
        user_obj.save()
        return Response(True)
    except Exception as e:
        print(e)
        return Response(False)