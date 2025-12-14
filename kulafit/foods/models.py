from django.db import models

class Food(models.Model):
    FOOD_TYPES = [
        ('starch', 'Starch'),
        ('protein', 'Protein'),
        ('vegetable', 'Vegetable'),
        ('beverage', 'Beverage'),
        ('snack', 'Snack'),
    ]

    name = models.CharField(max_length=100)
    food_type = models.CharField(max_length=20, choices=FOOD_TYPES)
    calories_per_unit = models.PositiveIntegerField()
    protein_per_unit = models.FloatField()
    carbs_per_unit = models.FloatField()
    fats_per_unit = models.FloatField()
    measurement_unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name
