from django.shortcuts import render
from django.http import JsonResponse
from .models import Meeting


def schedule(request):
    # gets all meeting objects from the DB and orders them by date/time
    meetings = Meeting.objects.all().order_by('meeting_datetime')

    # renders it to the index.html page and passes meetings to be displayed
    return render(request, 'schedule/index.html', {'meetings': meetings})

# sending data to the full calander
def meeting_event(request):
    # gets all meeting objects
    meetings = Meeting.objects.all()
    # empty list/array to store the events
    events = []
    # looping through the meetings and adding data into the events list/array
    for meeting in meetings:
        events.append({
            'id': meeting.id,
            'title': meeting.title,
            'start': meeting.meeting_datetime.isoformat(),
        })

    return JsonResponse(events, safe=False)