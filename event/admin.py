from django.contrib import admin
from event.models import Category, Event,Participant
# from django.contrib.auth.models import User
# from django.contrib.auth.models import User

# admin.site.register(User)  
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Participant)