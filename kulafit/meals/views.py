from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MealLogForm

@login_required
def log_meal(request):
    if request.method == 'POST':
        form = MealLogForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            return redirect('food-list')
    else:
        form = MealLogForm()
    return render(request, 'meals/log_meal.html', {'form': form})
