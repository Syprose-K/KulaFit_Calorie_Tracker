from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MealLogForm
from datetime import date
from .utils import daily_summary
from django.db.models import Sum
from .models import WeightLog


@login_required
def dashboard(request):
    today = date.today()
    summary = daily_summary(request.user, today)

    return render(request, 'meals/dashboard.html', {
        'summary': summary,
        'date': today
    })


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


@login_required
def weight_chart(request):
    weights = WeightLog.objects.filter(user=request.user).order_by('date')

    dates = [w.date.strftime('%Y-%m-%d') for w in weights]
    values = [w.weight for w in weights]

    return render(request, 'meals/weight_chart.html', {
        'dates': dates,
        'weights': values
    })
