from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Meeting


def schedule(request):
    # temporary team list until the real teams models are finished
    teams = [
        "Code Warriors",
        "The Debuggers",
        "Bit Masters",
        "Agile Avengers",
        "Syntax Squad",
        "The Codebreakers",
        "DevOps Dynasty",
        "Byte Force",
        "The Cloud Architects",
        "Full Stack Ninjas",
        "Cache Me Outside",
        "The Scrum Lords",
        "The 404 Not Found",
        "The Version Controllers",
        "DevNull Pioneers",
        "Kernel Crushers",
    ]

    # when the popup form is submitted
    if request.method == 'POST':
        title = request.POST.get('title')
        meeting_date = request.POST.get('meeting_date')
        meeting_time = request.POST.get('meeting_time')
        platform = request.POST.get('platform')
        agenda_message = request.POST.get('agenda_message')
        team_name = request.POST.get('team_name')
        created_by_name = request.POST.get('created_by_name')

        # only save if required values exist
        if title and meeting_date and meeting_time:
            # combine date and time into one datetime value
            meeting_datetime = datetime.strptime(
                f"{meeting_date} {meeting_time}",
                "%Y-%m-%d %H:%M"
            )

            Meeting.objects.create(
                title=title,
                meeting_datetime=meeting_datetime,
                platform=platform or '',
                agenda_message=agenda_message or '',
                team_name=team_name or '',
                created_by_name=created_by_name or '',
            )

        # reload the page so the saved meeting appears
        return redirect('schedule')

    # load all meetings from the database
    meetings = Meeting.objects.all().order_by('meeting_datetime')

    return render(request, 'schedule/index.html', {
        'meetings': meetings,
        'teams': teams,
    })


def delete_meeting(request, meeting_id):
    # find the selected meeting or return 404 if not found
    meeting = get_object_or_404(Meeting, id=meeting_id)

    # only allow delete through POST for safety
    if request.method == 'POST':
        meeting.delete()

    return redirect('schedule')