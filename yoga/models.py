from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class YogaClass(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    schedule = models.DateTimeField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='classes')

    def __str__(self):
        return self.title
    
from django.contrib.auth.models import User

class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    yoga_class = models.ForeignKey(YogaClass, on_delete=models.CASCADE, related_name='participants')
    enrolled_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=(
        ('Enrolled', 'Enrolled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ), default='Enrolled')

    def __str__(self):
        return f"{self.user.username} - {self.yoga_class.title}"

