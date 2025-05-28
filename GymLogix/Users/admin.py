from django.contrib import admin

# Register your models here.
from .models import FitnessEnthusiast,FitnessEnthusiatSignup,GymOwnerSignup,GymOwner,Trainer,TrainerSignup

admin.site.register(FitnessEnthusiast)
admin.site.register(FitnessEnthusiatSignup)
admin.site.register(GymOwner)
admin.site.register(GymOwnerSignup)
admin.site.register(Trainer)
admin.site.register(TrainerSignup)
# Register your models here.