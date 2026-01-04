from django.urls import path
from .api_views import meals_api, weights_api, meal_detail_api

urlpatterns = [
    path('meals/', meals_api),
    path('weights/', weights_api),
    path('meals/<int:meal_id>/', meal_detail_api),

]
