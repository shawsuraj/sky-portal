# Placeholder: URLs for schedule
from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_home, name='schedule_home'),
]