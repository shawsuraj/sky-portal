from django.urls import path
from . import views

app_name = 'teams' 

urlpatterns = [
    path('', views.views_list, name='teams_list'), 
    path('departments/', views.department_list, name='department_list'), 
    path('organisations/', views.organisation_list, name='organisation_list'), 
    path('team-types/', views.team_type_list, name='team_type_list'),
]