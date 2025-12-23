from django.urls import path
from .views import log_meal, log_weight, dashboard

urlpatterns = [
    path('log/', log_meal, name='log-meal'),
    path('weight/', log_weight, name='log-weight'),
    path('dashboard/', dashboard, name='dashboard'),
]
