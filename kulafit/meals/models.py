from django.db import models
from django.conf import settings
from foods.models import Food
from django.core.exceptions import ValidationError


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


    def clean(self):
        if self.quantity <= 0:
            raise ValidationError("Quantity must be greater than zero.")

    def total_calories(self):
        return self.quantity * self.food.calories_per_unit

    def total_macros(self):
        return {
            "protein": self.quantity * self.food.protein_per_unit,
            "carbs": self.quantity * self.food.carbs_per_unit,
            "fats": self.quantity * self.food.fats_per_unit,
        }

class WeightLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    weight = models.FloatField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
