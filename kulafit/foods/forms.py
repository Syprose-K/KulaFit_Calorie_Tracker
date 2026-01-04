from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = [
            'name',
            'food_type',
            'calories_per_unit',
            'protein_per_unit',
            'carbs_per_unit',
            'fats_per_unit',
            'measurement_unit'
        ]
