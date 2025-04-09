from django.shortcuts import render
from .models import Instructor, YogaClass

def home(request):
    return render(request, 'yoga/home.html')

def instructors(request):
    instructors = Instructor.objects.all()
    return render(request, 'yoga/instructors.html', {'instructors': instructors})

def yoga_classes(request):
    classes = YogaClass.objects.all().order_by('schedule')
    return render(request, 'yoga/classes.html', {'classes': classes})
