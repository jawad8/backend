from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models, serializers

# api for user creation


@api_view(['POST'])
def createUser(request):
    try:
        reqData = request.data
        user_obj = models.customUser(
            username=reqData['Username'], password=reqData['password'], user_type=reqData['user_type'])
        user_obj.save()
        return Response(True)
    except Exception as e:
        print(e)
        return Response(False)

#  api for user authentication


@api_view(['POST'])
def authUser(request):
    try:
        reqData = request.data
        user_obj = models.customUser.objects.filter(
            username=reqData['Username'], password=reqData['password'])
        if user_obj:
            return Response(True)
        else:
            return Response(False)
    except Exception as e:
        print(e)
        return Response(False)
