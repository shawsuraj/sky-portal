from django.contrib import admin
from .models import Organisation, Department, TeamType, Team, TeamDependency

admin.site.register(Organisation)
admin.site.register(Department)
admin.site.register(TeamType)
admin.site.register(Team)
admin.site.register(TeamDependency)