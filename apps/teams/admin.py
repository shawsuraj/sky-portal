from django.contrib import admin
from .models import Department, Team, Repository

admin.site.register(Department)
admin.site.register(Team)
admin.site.register(Repository)