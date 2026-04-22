from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Meeting
from apps.teams.models import Team


def schedule(request):
    # load teams from database instead of hardcoded list
    teams = Team.objects.all().order_by('team_name')

    # when the popup form is submitted
    if request.method == 'POST':
        title = request.POST.get('title')
        meeting_date = request.POST.get('meeting_date')
        meeting_time = request.POST.get('meeting_time')
        platform = request.POST.get('platform')
        agenda_message = request.POST.get('agenda_message')
        team_id = request.POST.get('team_id')
        created_by_name = request.POST.get('created_by_name')

        # only save if required values exist
        if title and meeting_date and meeting_time and team_id:
            meeting_datetime = datetime.strptime(
                f"{meeting_date} {meeting_time}",
                "%Y-%m-%d %H:%M"
            )

            # get selected team from DB
            selected_team = get_object_or_404(Team, id=team_id)

            Meeting.objects.create(
                title=title,
                meeting_datetime=meeting_datetime,
                platform=platform or '',
                agenda_message=agenda_message or '',
                team_name=selected_team.team_name,
                created_by_name=created_by_name or '',
            )

        return redirect('schedule')

    # load all meetings
    meetings = Meeting.objects.all().order_by('meeting_datetime')

    return render(request, 'schedule/index.html', {
        'meetings': meetings,
        'teams': teams,
    })


def delete_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)

    if request.method == 'POST':
        meeting.delete()

    return redirect('schedule')