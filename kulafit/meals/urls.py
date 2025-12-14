from django.urls import path
from .views import log_meal

urlpatterns = [
    path('log/', log_meal, name='log-meal'),
]
