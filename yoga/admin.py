from django.contrib import admin
from .models import Instructor, YogaClass, Participant

admin.site.register(Instructor)
admin.site.register(YogaClass)
admin.site.register(Participant)

