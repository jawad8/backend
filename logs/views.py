from asyncio.log import logger
from django.shortcuts import render
from . import models, serializers, utils
from rest_framework.decorators import api_view
from rest_framework.response import Response
import logging

logger = logging.getLogger('db')

# api for creating logs
@api_view(['GET'])
def createLogs(request):
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
    filteredList = []
    reqData = request.data
    if not reqData:
        res_obj = models.LogTable.objects.all()
        serializer_obj = serializers.GetLogsSerializer(res_obj, many=True)
        return Response(serializer_obj.data)
    for val in reqData:
        filteredList.extend(utils.filterHandler(reqData[val]))
    return Response(filteredList)


