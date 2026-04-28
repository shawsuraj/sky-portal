# Placeholder: URLs for schedule
from django.urls import path
from . import views


# URL patterns define what URL calls which view
urlpatterns = [

    # when user goes to /schedule/ → load schedule page
    path('', views.schedule, name='schedule'),

    # when user clicks cancel/delete → calls delete_meeting view
    # <int:meeting_id> means it passes the meeting ID from URL
    path('delete/<int:meeting_id>/', views.delete_meeting, name='delete_meeting'),

]