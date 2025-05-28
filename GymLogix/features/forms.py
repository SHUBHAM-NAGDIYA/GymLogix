from django import forms
from .models import ExerciseLibrary,NutritionPlan
class ExerciseLibraryForm(forms.ModelForm):
    class Meta:
        model = ExerciseLibrary
        fields = ['name', 'description', 'image', 'video', 'equipment']
        
class NutritionPlanForm(forms.ModelForm):
    class Meta:
        model = NutritionPlan
        fields = ['title', 'description', 'calories', 'protein', 'carbs', 'fats', 'duration_days']

class NutritionPlanForm(forms.ModelForm):
    class Meta:
        model = NutritionPlan
        fields = ['title', 'description', 'calories', 'protein', 'carbs', 'fats', 'duration_days']