# Placeholder: URLs for schedule
from django.urls import path
from . import views


urlpatterns = [
    path('', views.schedule, name='schedule'),
     path('delete/<int:meeting_id>/', views.delete_meeting, name='delete_meeting'),
    

]