from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import MealLog, WeightLog
from foods.models import Food
from datetime import date
from django.db.models import Sum
import json
