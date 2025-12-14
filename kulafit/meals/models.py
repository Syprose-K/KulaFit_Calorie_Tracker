from django.db import models
from django.conf import settings
from foods.models import Food

class MealLog(models.Model):
    MEAL_TYPES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.FloatField()
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    date = models.DateField(auto_now_add=True)

    def total_calories(self):
        return self.quantity * self.food.calories_per_unit
