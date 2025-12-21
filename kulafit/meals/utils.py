from django.db.models import Sum, F
from .models import MealLog

def daily_summary(user, date):
    meals = MealLog.objects.filter(user=user, date=date)

    summary = meals.aggregate(
        calories=Sum(F('quantity') * F('food__calories_per_unit')),
        protein=Sum(F('quantity') * F('food__protein_per_unit')),
        carbs=Sum(F('quantity') * F('food__carbs_per_unit')),
        fats=Sum(F('quantity') * F('food__fats_per_unit')),
    )

    return {k: v or 0 for k, v in summary.items()}
