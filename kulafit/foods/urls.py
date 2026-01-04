from django.urls import path
from .import views
from .views import food_list

app_name = 'foods'

urlpatterns = [
    path('', food_list, name='food-list'),
    path('add/', views.add_food, name='add-food'),
]
