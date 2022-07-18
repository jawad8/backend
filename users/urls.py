from django.urls import path
from . import views

urlpatterns = [
    path('createuser/', views.createUser),
    path('authUser/', views.authUser),
]