from asyncio.log import logger
from distutils.log import Log
from trace import Trace
from django.shortcuts import render
from . import models, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
import logging
logger = logging.getLogger('db',)

# api for creating logs
@api_view(['GET'])
def getLogs(request):
    logger.info("this is info log")
    logger.debug("this is debug log")
    logger.warning("this is warning log")
    logger.critical("this is critical log")
    logger.error("this is error log")
    return Response(True)

# api for fetching all the log records
@api_view(['GET'])
def fetchLogs(request):
    try:
        res_obj = models.LogTable.objects.all()
        serializer_obj = serializers.GetLogsSerializer(res_obj, many=True)
        return Response(serializer_obj.data, status=200)
    except Exception as e:
        print(e)
        return Response(False, status=400)
# filter api for logs
@api_view(['POST'])
def filterLogs(request):
    try:
        filteredList = []
        reqData = request.data
        if 'info' in reqData:
            res_obj = models.LogTable.objects.filter(log_type=reqData['info'])
            serializer_obj = serializers.GetLogsSerializer(res_obj,many=True)
            print(serializer_obj)
            filteredList.append(serializer_obj.data)
        if 'error' in reqData:
            res_obj = models.LogTable.objects.filter(log_type=reqData['error'])
            serializer_obj = serializers.GetLogsSerializer(res_obj,many=True)
            print(serializer_obj)
            filteredList.append(serializer_obj.data)

        if 'debug' in reqData:
            res_obj = models.LogTable.objects.filter(log_type=reqData['debug'])
            serializer_obj = serializers.GetLogsSerializer(res_obj,many=True)
            print(serializer_obj)
            filteredList.append(serializer_obj.data)

        if 'critical' in reqData:
            res_obj = models.LogTable.objects.filter(log_type=reqData['critical'])
            serializer_obj = serializers.GetLogsSerializer(res_obj,many=True)
            print(serializer_obj)     
            filteredList.append(serializer_obj.data)

        if 'warning' in reqData:
            res_obj = models.LogTable.objects.filter(log_type=reqData['warning'])
            serializer_obj = serializers.GetLogsSerializer(res_obj,many=True)
            print(serializer_obj)     
            filteredList.append(serializer_obj.data)

    
    except Exception as e:
        print(e)
        return Response()
