from django.shortcuts import render, redirect, get_object_or_404
from .models import Food
from .forms import FoodForm
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_superuser 

@login_required
@user_passes_test(is_admin)
def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food-list')  
    else:
        form = FoodForm()
    return render(request, 'foods/add_food.html', {'form': form})


@login_required
def food_list(request):
    query = request.GET.get('q')
    food_type = request.GET.get('type')

    foods = Food.objects.all()

    if query:
        foods = foods.filter(name__icontains=query)

    if food_type:
        foods = foods.filter(food_type=food_type)

    return render(request, 'foods/food_list.html', {
        'foods': foods,
        'query': query,
        'food_type': food_type,
    })
