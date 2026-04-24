# Placeholder: models for schedule
# imports for the models
from django.db import models
from django.contrib.auth.models import User
from apps.teams.models import Team


# Creating a meeting table to store data about it
class Meeting(models.Model):
    # creating columns within the table to store data

    # title is used to store data such as the title of the meeting
    title = models.CharField(max_length=200)

    # stores the date and time of the meeting
    meeting_datetime = models.DateTimeField()

    # stores the platform where the meeting will take place
    platform = models.CharField(max_length=100, blank=True)

    # stores the message/details about the meeting
    agenda_message = models.TextField(blank=True)

    # links the meeting to an actual Team record
    # this replaces the old team_name text field
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="meetings",
        null=True,
        blank=True
    )

    # stores the logged-in user who created the meeting
    # this replaces the old created_by_name text field
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_meetings",
        null=True,
        blank=True
    )

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # controls how meeting is displayed in admin
    def __str__(self):
        return self.title


# creating a meeting attendee table to store data about it
class MeetingAttendee(models.Model):
    # links the attendee to a meeting
    meeting = models.ForeignKey(
        Meeting,
        on_delete=models.CASCADE,
        related_name='attendees'
    )

    # links attendee to a real Django user instead of storing their name as text
    # this replaces the old attendee_name text field
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="meeting_attendances",
        null=True,
        blank=True
    )

    # stores response (Pending, Accepted, Declined)
    attendee_status = models.CharField(max_length=50, default='Pending')

    # stores when the attendee responded
    response_at = models.DateTimeField(null=True, blank=True)

    # controls how the attendee records are shown in admin
    def __str__(self):
        if self.user:
            return self.user.username + " - " + self.meeting.title
        return "Unknown attendee - " + self.meeting.title