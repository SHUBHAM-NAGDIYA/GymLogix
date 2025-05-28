from django.http import HttpResponse
from django.shortcuts import render
from features import models

def Home(request):
    return render(request, 'index.html')

def FitnessEnthusiast(request):
    return render(request, '')

def GymOwner(request):
    return render(request, 'GymOwners.html')

def PersonalTrainer(request):
    return render(request, 'trainers.html')

def CollegeStudent(request):
    return render(request, 'students.html')

def WorkingProfessions(request):
    return render(request, 'workingProfessions.html')