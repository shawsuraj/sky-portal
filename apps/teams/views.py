from django.shortcuts import render

from apps.teams.models import Department
from apps.teams.models import Organisation
from apps.teams.models import TeamType
from apps.teams.models import Team

def views_list(request):
    teams = Team.objects.select_related('department', 'team_type', 'manager_user') \
            .prefetch_related(
                'upstream_dependencies__upstream_team',
                'downstream_dependencies__downstream_team'
            ).all()
    context = {
        'teams': teams,
    }
    return render(request, 'teams/teams.html', context)

def department_list(request):

    departments = Department.objects.select_related('organisation', 'dept_leader_user').all()

    context = {
        'departments': departments,
    }

    return render(request, 'teams/departments.html', context)

def organisation_list(request):
    organisations = Organisation.objects.prefetch_related('departments').all()

    context = {
        'organisations': organisations,
    }

    return render(request, 'teams/organisations.html', context)

def team_type_list(request):
    # Grabs all the team categories from the database
    team_types = TeamType.objects.all()

    context = {
        'team_types': team_types,
    }

    return render(request, 'teams/team_types.html', context)

