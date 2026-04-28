from django.shortcuts import render, get_object_or_404
from .models import Team, Department

# no @login_required needed here - the global LoginRequiredMiddleware in settings covers all views

# 1. TEAM DIRECTORY & SEARCH (Wireframe Page 7)
def views_list(request): 
    # Grab all teams and pre-load everything needed for the directory cards
    # FIXED: members M2M is gone, now prefetch team_members (the new TeamMember table) and their users
    teams = Team.objects.select_related('department', 'manager_user') \
                        .prefetch_related('team_members__user', 'repositories')

    # Grab the search variables from the URL
    search_query = request.GET.get('search', '')
    dept_filter = request.GET.get('department', '')

    # Apply the Search Filter (matches team names)
    if search_query:
        teams = teams.filter(team_name__icontains=search_query)

    # Apply the Department Filter (dropdown selection)
    if dept_filter:
        teams = teams.filter(department_id=dept_filter)

    # Grab departments to populate the search dropdown menu
    all_departments = Department.objects.all()

    context = {
        'teams': teams,
        'all_departments': all_departments, 
    }
    return render(request, 'teams/teams.html', context)


# 2. THE TEAM PROFILE HUB (Wireframe Page 8)
def team_detail(request, team_id):
    # Grabs the specific team and pre-loads ALL tab data at once:
    # 1. Department/Manager (Header)
    # 2. Dependencies (Dependency Tab)
    # 3. Members & Repositories (The other tabs)
    # FIXED: members M2M is gone, prefetch team_members__user instead
    team = get_object_or_404(
        Team.objects.select_related('department', 'manager_user')
        .prefetch_related(
            'team_members__user',
            'repositories',
            'upstream_dependencies__upstream_team',
            'downstream_dependencies__downstream_team'
        ),
        id=team_id
    )

    context = {
        'team': team,
    }

    return render(request, 'teams/team_detail.html', context)