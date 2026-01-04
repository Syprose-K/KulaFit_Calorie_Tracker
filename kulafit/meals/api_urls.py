from django.urls import path
from .api_views import meals_api, weights_api

urlpatterns = [
    path('meals/', meals_api),
    path('weights/', weights_api),
]
