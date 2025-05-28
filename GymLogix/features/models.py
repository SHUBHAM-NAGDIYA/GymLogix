from django.db import models



# Create your models here.
class ExerciseLibrary(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='exercise_image/')
    video = models.FileField(upload_to='exercise_video/')
    equipment = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.description}'

class NutritionPlan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    calories = models.PositiveIntegerField(help_text="Total calories per day")
    protein = models.FloatField(help_text="Protein in grams per day")
    carbs = models.FloatField(help_text="Carbohydrates in grams per day")
    fats = models.FloatField(help_text="Fats in grams per day")
    duration_days = models.PositiveIntegerField(help_text="Duration of the plan in days")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Optionally, you can add a field for an image or PDF file
    # plan_file = models.FileField(upload_to='nutrition_plans/', blank=True, null=True)

    def __str__(self):
      return f'{self.title} - {self.description}'

