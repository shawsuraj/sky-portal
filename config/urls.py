from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.core import views
from apps.users import views as userview

urlpatterns = [
    path('admin/', admin.site.urls),

    # dashboard
    path('', views.home, name='home'),

    # auth
    path('login/', userview.login_view, name='login'),
    path('signup/', userview.signup_view, name='signup'),
    path('update_profile/', userview.update_profile, name='update_profile'),
    path('view_profile/', userview.view_profile, name='view_profile'),
    path('logout/', userview.logout_view, name='logout'),
    path('profile/', userview.profile, name='profile'),

    # app sections - each app handles its own urls.py
    path('teams/', include('apps.teams.urls')),
    path('mails/', include('apps.mails.urls')),
    path('schedule/', include('apps.schedule.urls')),
    path('organisation/', include('apps.organisation.urls')),
    path('users/', include('apps.users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
