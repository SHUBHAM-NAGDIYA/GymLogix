from django.shortcuts import render,redirect,get_object_or_404
from .models import ExerciseLibrary,NutritionPlan
from .forms import ExerciseLibraryForm,NutritionPlanForm


# Create your views heredef Home(request):


def exerciseLibrary(request):
    exercises = ExerciseLibrary.objects.all()
    return render(request, 'exercise_library.html', {'exercises': exercises})

def ExercisesAdd(request):
    if request.method == 'POST':
        form = ExerciseLibraryForm(request.POST, request.FILES)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.user = request.user
            form.save()
            return redirect('exercise_library')
    else:
        form = ExerciseLibraryForm()
    return render(request, 'add_exercise.html', {'form': form})

def GymFinder(request):
    return render(request, 'GymFinder')
    
def NutritionPlans(request):
    # Fetch all nutrition plans from the database
    nutrition_plans = NutritionPlan.objects.all()
    return render(request, 'nutrition_plans.html', {'nutrition_plans': nutrition_plans})


def AddNutritionPlan(request):
    if request.method == 'POST':
        form = NutritionPlanForm(request.POST)
        if form.is_valid():
            nutritions = form.save(commit=False)
            nutritions.user = request.user
            form.save()
            return redirect('nutrition_plans')  # Make sure this matches your nutrition plans list URL name
    else:
        form = NutritionPlanForm()
    return render(request, 'add_nutrition_plan.html', {'form': form})


def TrainerConnect(request):
    return render(request, 'TrainerConnect')