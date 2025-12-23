from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MealLogForm, WeightLogForm
from datetime import date
from .utils import daily_summary
from django.db.models import Sum
from .models import WeightLog


@login_required
def dashboard(request):
    today = date.today()
    summary = daily_summary(request.user, today)

    weights = WeightLog.objects.filter(user=request.user).order_by('date')
    weight_dates = [w.date.strftime('%Y-%m-%d') for w in weights]
    weight_values = [w.weight for w in weights]


    return render(request, 'meals/dashboard.html', {
        'summary': summary,
        'date': today,
        'weight_dates': weight_dates,
        'weight_values': weight_values,

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


@login_required
def log_weight(request):
    if request.method == 'POST':
        form = WeightLogForm(request.POST)
        if form.is_valid():
            weight_log = form.save(commit=False)
            weight_log.user = request.user
            weight_log.save()
            return redirect('dashboard')
    else:
        form = WeightLogForm()

    weights = WeightLog.objects.filter(user=request.user)

    return render(request, 'meals/log_weight.html', {
        'form': form,
        'weights': weights,
    })
