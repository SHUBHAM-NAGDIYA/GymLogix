from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ... your other URLs ...
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    #path('signup/', views.fitnessenthusiastSignup, name='fitnessenthusiast_signup'),
    path('fitnessenthusiast_login/', views.fitnessenthusiastLogin, name='fitnessenthusiast_login'),
    #path('gym_owner_signup/', views.gymOwnerSignup, name='gym_owner_signup'),
    path('gym_owner_login/', views.gymOwnerLogin, name='gym_owner_login'),
    path('gym_finder/', views.gymFinder, name='gym_finder'),
    #path('trainer_signup/', views.trainerSignup, name='trainer_signup'),
    path('trainer/', views.trainers, name='trainer'),
    path('trainer_login/', views.trainerLogin, name='trainer_login'),
    #path('signup/', views.signup, name='signup'),
     path('signup/', views.unified_signup, name='signup'),
]
