from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MealLogForm, WeightLogForm
from datetime import date,timedelta
from .utils import daily_summary
from django.db.models import Sum
from .models import MealLog, WeightLog
import json



@login_required
def dashboard(request):
    today = date.today()

    # Daily summary
    daily_meals = MealLog.objects.filter(user=request.user, date=today)
    summary = {
        'calories': daily_meals.aggregate(Sum('calories'))['calories__sum'] or 0,
        'protein': daily_meals.aggregate(Sum('protein'))['protein__sum'] or 0,
        'carbs': daily_meals.aggregate(Sum('carbs'))['carbs__sum'] or 0,
        'fats': daily_meals.aggregate(Sum('fats'))['fats__sum'] or 0,
    }

    # Weight chart
    weights = WeightLog.objects.filter(user=request.user).order_by('date')
    weight_dates = [w.date.strftime('%Y-%m-%d') for w in weights]
    weight_values = [w.weight for w in weights]

    # Macro chart
    macro_labels = ['Protein', 'Carbs', 'Fats']
    macro_values = [summary['protein'], summary['carbs'], summary['fats']]

    # Weekly calories chart
    last_7_days = [today - timedelta(days=i) for i in reversed(range(7))]
    last7_dates = [d.strftime('%Y-%m-%d') for d in last_7_days]
    last7_calories = []
    for d in last_7_days:
        day_total = MealLog.objects.filter(user=request.user, date=d).aggregate(Sum('calories'))['calories__sum'] or 0
        last7_calories.append(day_total)

    return render(request, 'meals/dashboard.html', {
        'summary': summary,
        'weight_dates': json.dumps(weight_dates),
        'weight_values': json.dumps(weight_values),
        'macro_labels': json.dumps(macro_labels),
        'macro_values': json.dumps(macro_values),
        'last7_dates': json.dumps(last7_dates),
        'last7_calories': json.dumps(last7_calories),
        'date': today,
    })


@login_required
def log_meal(request):
    if request.method == 'POST':
        form = MealLogForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            return redirect('meals:dashboard')
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
            return redirect('meals:dashboard')
    else:
        form = WeightLogForm()

    weights = WeightLog.objects.filter(user=request.user)

    return render(request, 'meals/log_weight.html', {
        'form': form,
        'weights': weights,
    })
