
# Placeholder: views for schedule
from django.shortcuts import render
from .models import Meeting


def schedule_home(request):
    meetings = Meeting.objects.all().order_by('meeting_datetime')
    return render(request, 'schedule/index.html', {'meetings': meetings})

from django.shortcuts import render


