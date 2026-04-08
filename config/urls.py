# Placeholder: project URL configuration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schedule/', include('apps.schedule.urls')),
]