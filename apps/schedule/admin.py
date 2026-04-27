from django.contrib import admin
from .models import Meeting, MeetingAttendee


# Register the Meeting model in Django admin
@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):

    # Fields displayed in the admin list view (table view)
    list_display = (
        "title",              # Meeting title
        "meeting_datetime",  # Date & time of meeting
        "team",              # Related team
        "platform",          # Meeting platform (Zoom, Teams, etc.)
        "created_by",        # User who created the meeting
        "created_at",        # Timestamp when meeting was created
    )

    # Fields that can be searched using the admin search bar
    search_fields = (
        "title",                         # search by meeting title
        "agenda_message",                # search by message/description
        "team__team_name",               # search by team name (foreign key lookup)
        "created_by__username",          # search by creator username
        "created_by__first_name",        # search by creator first name
        "created_by__last_name",         # search by creator last name
    )


# Register the MeetingAttendee model in Django admin
@admin.register(MeetingAttendee)
class MeetingAttendeeAdmin(admin.ModelAdmin):

    # Fields displayed in the admin list view
    list_display = (
        "meeting",          # Related meeting
        "user",             # User attending the meeting
        "attendee_status",  # Status (Accepted / Pending / Declined)
        "response_at",      # When user responded
    )

    # Fields that can be searched in admin
    search_fields = (
        "meeting__title",       # search by meeting title
        "user__username",       # search by username
        "user__first_name",     # search by first name
        "user__last_name",      # search by last name
    )