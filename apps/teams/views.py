from django.shortcuts import render

from apps.teams.models import Department
from apps.teams.models import Organisation
from apps.teams.models import TeamType
from apps.teams.models import Team
from django.db.models import Q

from django.shortcuts import render
from .models import Department, Organisation, TeamType, Team
from django.db.models import Q 

def views_list(request): 
    # 1. Base Query 
    teams = Team.objects.select_related('department', 'team_type', 'manager_user') \
                        .prefetch_related(
                            'upstream_dependencies__upstream_team',
                            'downstream_dependencies__downstream_team'
                        )

    # 2. Grab the search variables from the URL
    search_query = request.GET.get('search', '')
    dept_filter = request.GET.get('department', '')

    # 3. Apply the Search Filter
    if search_query:
        teams = teams.filter(team_name__icontains=search_query)

    # 4. Apply the Department Filter
    if dept_filter:
        teams = teams.filter(department_id=dept_filter)

    # 5. Grab all departments
    all_departments = Department.objects.all()

    context = {
        'teams': teams,
        'all_departments': all_departments, 
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

