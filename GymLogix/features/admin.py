from django.contrib import admin
from .models import ExerciseLibrary,NutritionPlan

# Register your models here.
admin.site.register(ExerciseLibrary)
admin.site.register(NutritionPlan)