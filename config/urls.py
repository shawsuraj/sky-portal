"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include

from apps.core import views
from apps.mails import views as mailview
from apps.users import views as userview



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home, name="home"),
    path("mails/", include("apps.mails.urls")),
    path('users/login/', userview.login_view, name='login'),
    path('logout/', userview.logout_view, name='logout'),
    path('users/signup/', userview.signup_view, name='signup'),
    path('users/update_profile/', userview.update_profile, name='update_profile'),
    path('users/view_profile/', userview.view_profile, name='view_profile'),
    path('schedule/', include('apps.schedule.urls')),
    path('organisation/', include('apps.organisation.urls')),
    path('teams/', include('apps.teams.urls')),
    path('users/', include('apps.users.urls')),
]
