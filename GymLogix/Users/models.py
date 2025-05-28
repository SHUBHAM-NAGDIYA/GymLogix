from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
# Create your models here.
class FitnessEnthusiast(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    fitness_goals = models.TextField()
    preferred_workout_time = models.CharField(max_length=50)
    preferred_workout_location = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.email} - {self.phone_number} - {self.fitness_goals} - {self.preferred_workout_time} - {self.preferred_workout_location}'

class FitnessEnthusiatSignup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fitness_enthusiast = models.ForeignKey(FitnessEnthusiast, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.fitness_enthusiast.name}'

def FitnessEnthusiastLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Change 'home' to your desired redirect
        else:
            # Invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

class GymOwner(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    gym_location = models.CharField(max_length=100)
    gym_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.email} - {self.phone_number} - {self.gym_location} - {self.gym_name}'

class GymOwnerSignup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gym_owner = models.ForeignKey(GymOwner, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.gym_owner.name}'
    
class GymOwnerLogin(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.username} - {self.password}'
    

    
class Trainer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)
    experience_years = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.email} - {self.phone_number} - {self.specialization} - {self.experience_years}'
    

class TrainerSignup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.trainer.name}'