
# imports 
from django.contrib import admin
from .models import Meeting, MeetingAttendee


# Register Meeting model in admin
@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):

    # shows the columns within the admin list
    list_display = [
        'id',
        'title',
        'team_name',
        'platform',
        'meeting_datetime',
        'created_by_name'
    ]

    # filters on the right side
    list_filter = ['platform', 'meeting_datetime']

    # search bar
    search_fields = ['title', 'agenda_message', 'team_name', 'created_by_name']


# Register MeetingAttendee model 
@admin.register(MeetingAttendee)
class MeetingAttendeeAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'meeting',
        'attendee_name',
        'attendee_status',
        'response_at'
    ]

    list_filter = ['attendee_status']

    search_fields = ['meeting__title', 'attendee_name']
