from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import datetime

from .models import Meeting, MeetingAttendee
# FIXED: imported TeamMember so we can loop through the new membership table instead of the old M2M
from apps.teams.models import Team, TeamMember


# FIXED: added login_url="login" to match the rest of the project
@login_required(login_url="login")
def schedule(request):
    # Load all teams from the database for the dropdown
    # This lets any logged-in user select a team when scheduling a meeting
    # order_by ensures teams show alphabetically in dropdown
    teams = Team.objects.all().order_by('team_name')

    # When the popup form is submitted (form POST request)
    if request.method == 'POST':

        # Get form data from request
        title = request.POST.get('title')
        meeting_date = request.POST.get('meeting_date')
        meeting_time = request.POST.get('meeting_time')
        platform = request.POST.get('platform')
        agenda_message = request.POST.get('agenda_message')
        team_id = request.POST.get('team_id')

        # Only save if required values exist
        # prevents empty/invalid meetings being created
        if title and meeting_date and meeting_time and team_id:

            # Combine date + time into one datetime object
            meeting_datetime = datetime.strptime(
                f"{meeting_date} {meeting_time}",
                "%Y-%m-%d %H:%M"
            )

            # Get selected team from the database
            # if team doesn't exist → returns 404 instead of crashing
            selected_team = get_object_or_404(Team, id=team_id)

            # Create meeting
            # created_by is automatically the logged-in user
            meeting = Meeting.objects.create(
                title=title,
                meeting_datetime=meeting_datetime,
                platform=platform or '',        # fallback if empty
                agenda_message=agenda_message or '',
                team=selected_team,
                created_by=request.user,        # important for ownership tracking
            )

            # Add creator as accepted attendee
            # ensures creator sees meeting immediately
            MeetingAttendee.objects.get_or_create(
                meeting=meeting,
                user=request.user,
                defaults={"attendee_status": "Accepted"}
            )

            # Add all team members as attendees
            # This means team members can also see the meeting
            # FIXED: was selected_team.members.all() - members M2M is gone, loop through TeamMember now
            for membership in selected_team.team_members.all():
                MeetingAttendee.objects.get_or_create(
                    meeting=meeting,
                    user=membership.user,
                    defaults={"attendee_status": "Pending"}
                )

        # After creating meeting → reload page
        return redirect('schedule')

    # Only show meetings where the logged-in user is still an attendee
    # If the user cancels the meeting, it only disappears from their own schedule
    meetings = Meeting.objects.filter(
        attendees__user=request.user   # only meetings linked to this user
    ).distinct().order_by('meeting_datetime')

    # Render schedule page and pass data to template
    return render(request, 'schedule/index.html', {
        'meetings': meetings,
        'teams': teams,
    })


# FIXED: added login_url="login" to match the rest of the project
@login_required(login_url="login")
def delete_meeting(request, meeting_id):
    # Cancel only removes the meeting from the logged-in user's own schedule
    # It does NOT delete the meeting from database entirely

    # Get meeting object safely
    meeting = get_object_or_404(Meeting, id=meeting_id)

    # Only cancel/remove it when the form sends a POST request
    # just removes the current user from the attendee list, doesnt delete the whole meeting
    if request.method == 'POST':
        MeetingAttendee.objects.filter(meeting=meeting, user=request.user).delete()

    return redirect('schedule')
