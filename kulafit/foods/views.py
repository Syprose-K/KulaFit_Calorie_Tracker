from django.shortcuts import render
from .models import Food
from django.db.models import Q

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'foods/food_list.html', {'foods': foods})


def food_list(request):
    query = request.GET.get('q')
    food_type = request.GET.get('type')

    foods = Food.objects.all()

    if query:
        foods = foods.filter(name__icontains=query)

    if food_type:
        foods = foods.filter(food_type=food_type)

    return render(request, 'foods/food_list.html', {
        'foods': foods
    })
