from django.contrib import admin
from .models import Meeting, MeetingAttendee


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    # fields shown in Django admin list page
    list_display = (
        "title",
        "meeting_datetime",
        "team",
        "platform",
        "created_by",
        "created_at",
    )

    # fields that can be searched in admin
    search_fields = (
        "title",
        "agenda_message",
        "team__team_name",
        "created_by__username",
        "created_by__first_name",
        "created_by__last_name",
    )


@admin.register(MeetingAttendee)
class MeetingAttendeeAdmin(admin.ModelAdmin):
    # fields shown in Django admin list page
    list_display = (
        "meeting",
        "user",
        "attendee_status",
        "response_at",
    )

    # fields that can be searched in admin
    search_fields = (
        "meeting__title",
        "user__username",
        "user__first_name",
        "user__last_name",
    )