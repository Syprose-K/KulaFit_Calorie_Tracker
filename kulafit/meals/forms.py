from django import forms
from .models import MealLog

class MealLogForm(forms.ModelForm):
    class Meta:
        model = MealLog
        fields = ['food', 'quantity', 'meal_type']
