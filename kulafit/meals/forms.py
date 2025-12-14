from django import forms
from .models import MealLog

class MealLogForm(forms.ModelForm):
    class Meta:
        model = MealLog
        fields = ['food', 'quantity', 'meal_type']

    def clean_quantity(self):
        qty = self.cleaned_data['quantity']
        if qty <= 0:
            raise forms.ValidationError("Quantity must be greater than zero.")
        return qty
