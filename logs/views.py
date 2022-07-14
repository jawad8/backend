from django.shortcuts import render
from . import models, serializers
from users import models as userModels
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def getLogs(request):
    try:
        res_obj = models.LogTable.objects.all()
        serializer_obj = serializers.GetLogsSerializer(res_obj, many=True)
        return Response(serializer_obj.data,status=200)
    except Exception as e:
        print(e)
        return Response(False,status=400)

