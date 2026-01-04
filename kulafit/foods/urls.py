from django.urls import path
from .views import food_list

app_name = 'foods'

urlpatterns = [
    path('', food_list, name='food-list'),
]
