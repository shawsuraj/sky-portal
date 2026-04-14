from django.shortcuts import render

from apps.teams.models import Department

def views_list(request):
    return render(request, 'teams/teams.html')

def department_list(request):

    departments = Department.objects.select_related('organisation', 'dept_leader_user').all()

    context = {
        'departments': departments,
    }

    return render(request, 'teams/departments.html', context)