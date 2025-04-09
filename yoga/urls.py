from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('instructors/', views.instructors, name='instructors'),
    path('classes/', views.yoga_classes, name='yoga_classes'),
]
