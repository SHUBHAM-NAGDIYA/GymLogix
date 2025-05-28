"""
URL configuration for GymLogix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='home'),
    #path('exercise_library/',views.ExerciseLibrary,name='exercise_library'),
    path('features/', include('features.urls')),
    path('Users/', include('Users.urls')),
    path('fitness_enthusiast/',views.FitnessEnthusiast,name='fitness_enthusiast'),
    path('gym_owner/',views.GymOwner,name='gym_owner'),
    path('personal_trainer/',views.PersonalTrainer,name='personal_trainer'),
    path('college_student/',views.CollegeStudent,name='college_student'),
    path('working_professions/',views.WorkingProfessions,name='working_professions'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
