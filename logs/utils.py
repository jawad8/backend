from . import models, serializers
from datetime import date
from datetime import timedelta
from asyncio.log import logger
from django.shortcuts import render

# handles filtering mechanism for logs
def filterHandler(val):
    today = date.today()
    yesterday = today - timedelta(days = 1)

    if val == 'today':
        res_obj = models.LogTable.objects.filter(log_time__gte= yesterday )
        serializer_obj = serializers.GetLogsSerializer(res_obj, many=True)
        return serializer_obj.data
    elif val == 'yesterday':
        res_obj = models.LogTable.objects.filter(log_time__gte=(yesterday - timedelta(days = 1)),log_time__lte = yesterday)
        serializer_obj = serializers.GetLogsSerializer(res_obj, many=True)
        return serializer_obj.data
    else:
        res_obj = models.LogTable.objects.filter(log_type=val)
        serializer_obj = serializers.GetLogsSerializer(res_obj, many=True)
        return serializer_obj.data
