from django import forms
from . import models

class FitnessEnthusiastForm(forms.ModelForm):
    class Meta:
        model = models.FitnessEnthusiast
        fields = ['name', 'email', 'phone_number', 'fitness_goals', 'preferred_workout_time', 'preferred_workout_location']
        widgets = {
            'fitness_goals': forms.Textarea(attrs={'rows': 4}),
            'preferred_workout_time': forms.TextInput(attrs={'placeholder': 'e.g., Morning, Evening'}),
            'preferred_workout_location': forms.TextInput(attrs={'placeholder': 'e.g., Gym, Home'}),
        }

class FitnessEnthusiastSignupForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = models.FitnessEnthusiast
        fields = ['name', 'phone_number', 'fitness_goals', 'preferred_workout_time', 'preferred_workout_location']

class GymOwnerForm(forms.ModelForm):
    class Meta:
        model = models.GymOwner
        fields = ['name', 'email', 'phone_number', 'gym_location', 'gym_name']
        widgets = {
            'gym_location': forms.TextInput(attrs={'placeholder': 'e.g., Downtown, Suburb'}),
            'gym_name': forms.TextInput(attrs={'placeholder': 'e.g., Fitness Hub, Power Gym'}),
        }


class GymOwnerSignupForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = models.GymOwner
        fields = ['name', 'phone_number', 'gym_location', 'gym_name']

class GymOwnerLoginForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.GymOwner
        fields = ['username', 'password']
class TrainerForm(forms.ModelForm):
    class Meta:
        model = models.Trainer
        fields = ['name', 'email', 'phone_number', 'specialization', 'experience_years']
        widgets = {
            'specialization': forms.TextInput(attrs={'placeholder': 'e.g., Weightlifting, Cardio'}),
            'experience_years': forms.NumberInput(attrs={'min': 0}),
        }

class TrainerSignupForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = models.Trainer
        fields = ['name', 'phone_number', 'specialization', 'experience_years']