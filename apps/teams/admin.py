from django.contrib import admin
from .models import Organisation, Department, Team, Repository, TeamDependency

admin.site.register(Organisation)
admin.site.register(Department)
admin.site.register(Team)
admin.site.register(Repository)
admin.site.register(TeamDependency)