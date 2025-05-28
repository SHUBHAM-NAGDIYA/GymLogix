from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import FitnessEnthusiastSignupForm, GymOwnerSignupForm, TrainerSignupForm
from .models import FitnessEnthusiatSignup, GymOwnerSignup, TrainerSignup,Trainer



def fitnessenthusiastLogin(request):
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


def gymOwnerLogin(request):
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

def trainers(request):
    trainer = Trainer.objects.all()
    return render(request,'trainer.html', {'trainer': trainer})


def trainerLogin(request):
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


def gymFinder(request):
    return render(request, 'gym_finder.html')




'''
def fitnessenthusiastSignup(request):
    if request.method == 'POST':
        form = FitnessEnthusiastSignupForm(request.POST)
        if form.is_valid():
            # Create the User
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # Create the FitnessEnthusiast profile
            enthusiast = form.save(commit=False)
            enthusiast.email = form.cleaned_data['email']
            enthusiast.save()
            # Link User and FitnessEnthusiast
            FitnessEnthusiatSignup.objects.create(user=user, fitness_enthusiast=enthusiast)
            login(request, user)
            return redirect('home')  # Change 'home' to your desired redirect
    else:
        form = FitnessEnthusiastSignupForm()
    return render(request, 'signup.html', {'form': form})

def fitnessenthusiastLogin(request):
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

def gymOwnerSignup(request):
    if request.method == 'POST':
        form = GymOwnerSignupForm(request.POST)
        if form.is_valid():
            # Create the User
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # Create the GymOwner profile
            gym_owner = form.save(commit=False)
            gym_owner.email = form.cleaned_data['email']
            gym_owner.save()
            # Link User and GymOwner
            GymOwnerSignup.objects.create(user=user, gym_owner=gym_owner)
            login(request, user)
            return redirect('home')  # Change 'home' to your desired redirect
    else:
        form = GymOwnerSignupForm()
    return render(request, 'gym_owner_signup.html', {'form': form})

def gymOwnerLogin(request):
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

def trainers(request):
    trainer = Trainer.objects.all()
    return render(request,'trainer.html', {'trainer': trainer})



def trainerLogin(request):
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



def trainerSignup(request):
    if request.method == 'POST':
        form = TrainerSignupForm(request.POST)
        if form.is_valid():
            # Create the User
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # Create the Trainer profile
            trainer = form.save(commit=False)
            trainer.email = form.cleaned_data['email']
            trainer.save()
            # Link User and Trainer
            TrainerSignup.objects.create(user=user, trainer=trainer)
            login(request, user)
            return redirect('home')  # Change 'home' to your desired redirect
    else:
        form = TrainerSignupForm()
    return render(request, 'trainer_signup.html', {'form': form})

def gymFinder(request):
    return render(request, 'gym_finder.html')

def signup(request):
    return render(request, 'signup.html')'''





def unified_signup(request):
    user_type = request.GET.get('user_type')
    form = None

    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        if user_type == 'enthusiast':
            form = FitnessEnthusiastSignupForm(request.POST)
        elif user_type == 'owner':
            form = GymOwnerSignupForm(request.POST)
        elif user_type == 'trainer':
            form = TrainerSignupForm(request.POST)
        else:
            form = None

        if form and form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            profile = form.save(commit=False)
            profile.email = form.cleaned_data['email']
            profile.save()
            # Link user and profile
            if user_type == 'enthusiast':
                FitnessEnthusiatSignup.objects.create(user=user, fitness_enthusiast=profile)
            elif user_type == 'owner':
                GymOwnerSignup.objects.create(user=user, gym_owner=profile)
            elif user_type == 'trainer':
                TrainerSignup.objects.create(user=user, trainer=profile)
            login(request, user)
            return redirect('home')
    else:
        if user_type == 'enthusiast':
            form = FitnessEnthusiastSignupForm()
        elif user_type == 'owner':
            form = GymOwnerSignupForm()
        elif user_type == 'trainer':
            form = TrainerSignupForm()

    return render(request, 'signup.html', {'form': form, 'user_type': user_type})