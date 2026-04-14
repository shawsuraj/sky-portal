from django.urls import path
from . import views

app_name = 'teams' # This fixes the "namespace" error!

urlpatterns = [
    # This says: when someone goes to /teams/, run the 'teams_list' view
    path('', views.views_list, name='teams_list'), 
]

app_name = 'teams'
urlpatterns = [
    path('', views.views_list, name='teams_list'),
    path('departments/', views.department_list, name='department_list'),
]