from django.urls import path
from . import views


urlpatterns = [
    path('createlog/', views.createLogs),
    path('fetchLogs/', views.fetchLogs),
    path('filterLogs/', views.filterLogs),

]