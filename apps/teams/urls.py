from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [
    # 1. The main directory with search
    path('teams/', views.views_list, name='teams_list'),
    # 2. The dynamic team hub
    path('<int:team_id>/', views.team_detail, name='team_detail'),
]