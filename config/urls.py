from django.contrib import admin
from django.urls import path, include

from apps.core import views
from apps.users import views as userview

urlpatterns = [
    path('admin/', admin.site.urls),

    # dashboard
    path('', views.home, name='home'),

    # auth
    path('users/login/', userview.login_view, name='login'),
    path('users/signup/', userview.signup_view, name='signup'),
    path('users/update_profile/', userview.update_profile, name='update_profile'),
    path('users/view_profile/', userview.view_profile, name='view_profile'),
    path('logout/', userview.logout_view, name='logout'),

    # app sections - each app handles its own urls.py
    path('teams/', include('apps.teams.urls')),
    path('mails/', include('apps.mails.urls')),
    path('schedule/', include('apps.schedule.urls')),
    path('organisation/', include('apps.organisation.urls')),
]
