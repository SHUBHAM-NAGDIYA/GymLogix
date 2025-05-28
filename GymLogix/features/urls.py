
from django.urls import path
from . import views 


from . import views

urlpatterns = [
    path('exercise_library/',views.exerciseLibrary,name='exercise_library'),
    path('exercises_add/',views.ExercisesAdd,name='exercises_add'),
    path('gym_finder/',views.GymFinder,name='gym_finder'),
    path('nutrition_plans/',views.NutritionPlans,name='nutrition_plans'),
    path('trainer_connect/',views.TrainerConnect,name='trainer_connect'),
    
] 
