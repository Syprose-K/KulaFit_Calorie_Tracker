from django import forms
from .models import MealLog, WeightLog

class MealLogForm(forms.ModelForm):
    class Meta:
        model = MealLog
        fields = ['food', 'quantity', 'meal_type']

class WeightLogForm(forms.ModelForm):
    class Meta:
        model = WeightLog
        fields = ['weight']

    def clean_weight(self):
        weight = self.cleaned_data['weight']
        if weight <= 0:
            raise forms.ValidationError("Weight must be greater than zero.")
        return weight
