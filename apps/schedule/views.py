from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import datetime

from .models import Meeting, MeetingAttendee
from apps.teams.models import Team


@login_required
def schedule(request):
    # Load all teams from the database for the dropdown
    # This lets any logged-in user select a team when scheduling a meeting
    teams = Team.objects.all().order_by('team_name')

    # When the popup form is submitted
    if request.method == 'POST':
        title = request.POST.get('title')
        meeting_date = request.POST.get('meeting_date')
        meeting_time = request.POST.get('meeting_time')
        platform = request.POST.get('platform')
        agenda_message = request.POST.get('agenda_message')
        team_id = request.POST.get('team_id')

        # Only save if required values exist
        if title and meeting_date and meeting_time and team_id:
            meeting_datetime = datetime.strptime(
                f"{meeting_date} {meeting_time}",
                "%Y-%m-%d %H:%M"
            )

            # Get selected team from the database
            selected_team = get_object_or_404(Team, id=team_id)

            # Create meeting
            # created_by is automatically the logged-in user
            meeting = Meeting.objects.create(
                title=title,
                meeting_datetime=meeting_datetime,
                platform=platform or '',
                agenda_message=agenda_message or '',
                team=selected_team,
                created_by=request.user,
            )

            # Add creator as accepted attendee
            MeetingAttendee.objects.get_or_create(
                meeting=meeting,
                user=request.user,
                defaults={"attendee_status": "Accepted"}
            )

            # Add all team members as attendees
            # This means team members can also see the meeting
            for member in selected_team.members.all():
                MeetingAttendee.objects.get_or_create(
                    meeting=meeting,
                    user=member,
                    defaults={"attendee_status": "Pending"}
                )

        return redirect('schedule')

    # Only show meetings where the logged-in user is still an attendee
    # If the user cancels the meeting, it only disappears from their own schedule
    meetings = Meeting.objects.filter(
        attendees__user=request.user
    ).distinct().order_by('meeting_datetime')

    return render(request, 'schedule/index.html', {
        'meetings': meetings,
        'teams': teams,
    })


@login_required
def delete_meeting(request, meeting_id):
    # Cancel only removes the meeting from the logged-in user's own schedule
    # It does not delete the meeting for everyone else
    meeting = get_object_or_404(Meeting, id=meeting_id)

    # Only cancel/remove it when the form sends a POST request
    if request.method == 'POST':
        MeetingAttendee.objects.filter(
            meeting=meeting,
            user=request.user
        ).delete()

    return redirect('schedule')