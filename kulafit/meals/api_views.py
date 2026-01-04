from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import MealLog, WeightLog
from foods.models import Food
from datetime import date
from django.db.models import Sum
import json

@require_http_methods(["POST"])
@login_required
def meals_api(request):
    data = json.loads(request.body)

    food = Food.objects.get(id=data["food_id"])

    meal = MealLog.objects.create(
        user=request.user,
        food=food,
        quantity=data["quantity"],
        meal_type=data["meal_type"]
    )

    return JsonResponse(
        {"message": "Meal created", "id": meal.id},
        status=201
    )

@require_http_methods(["GET", "POST"])
@login_required
def meals_api(request):
    if request.method == "GET":
        meals = MealLog.objects.filter(user=request.user).select_related('food')

        data = [
            {
                "id": m.id,
                "food": m.food.name,
                "quantity": m.quantity,
                "meal_type": m.meal_type,
                "calories": m.total_calories(),
                "date": m.date
            }
            for m in meals
        ]

        return JsonResponse(data, safe=False, status=200)

@require_http_methods(["GET", "POST"])
@login_required
def weights_api(request):
    if request.method == "POST":
        data = json.loads(request.body)

        weight = WeightLog.objects.create(
            user=request.user,
            weight=data["weight"]
        )

        return JsonResponse(
            {"message": "Weight logged", "id": weight.id},
            status=201
        )

    weights = WeightLog.objects.filter(user=request.user)

    data = [
        {"weight": w.weight, "date": w.date}
        for w in weights
    ]

    return JsonResponse(data, safe=False, status=200)
