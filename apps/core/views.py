from django.shortcuts import render
from apps.teams.models import Team, Department
from apps.mails.models import Message


def home(request):
    # count all teams and departments for the stat cards
    total_teams = Team.objects.count()
    total_depts = Department.objects.count()

    # unread messages only makes sense if the user is logged in
    unread_msgs = 0
    recent_activity = []
    if request.user.is_authenticated:
        unread_msgs = Message.objects.filter(
            receiver=request.user, is_read=False, is_draft=False
        ).count()
        # show the 5 most recent messages the user received
        recent_activity = Message.objects.filter(
            receiver=request.user, is_draft=False
        ).select_related('sender').order_by('-timestamp')[:5]

    # no visit-tracking yet so just grab 3 teams as "recently visited"
    # select_related department so the template doesn't fire extra queries
    recent_teams = Team.objects.select_related('department', 'manager_user').order_by('id')[:3]

    context = {
        'total_teams':     total_teams,
        'total_depts':     total_depts,
        'unread_msgs':     unread_msgs,
        'recent_teams':    recent_teams,
        'recent_activity': recent_activity,
    }
    return render(request, 'dashboard.html', context)
