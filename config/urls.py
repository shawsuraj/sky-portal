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
    path("mails/",mailview.mails, name="mails"),
    path("mails/inbox/", mailview.inbox, name="inbox"),
    path("mails/sent_message/", mailview.sent_message, name="sent_message"),
    path("mails/compose_message/", mailview.compose_message, name="compose_message"),
    path("mails/view_draft/", mailview.view_draft, name="view_draft"),
    path('users/login/', userview.login_view, name='login'),
    path('logout/', userview.logout_view, name='logout'),
    path('users/signup/', userview.signup_view, name='signup'),
    path('schedule/', include('apps.schedule.urls')),

]
