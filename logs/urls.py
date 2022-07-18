from django.urls import path
from . import views


urlpatterns = [
    path('createlog/', views.getLogs),
    path('fetchLogs/', views.fetchLogs),
    path('filterLogs/', views.filterLogs),

]