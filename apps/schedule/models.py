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
    # blank=True means it is optional
    platform = models.CharField(max_length=100, blank=True)

    # stores the message/details about the meeting
    # TextField is used for longer text input
    agenda_message = models.TextField(blank=True)

    # links the meeting to an actual Team record
    # this replaces the old team_name text field
    # ForeignKey creates a relationship (many meetings -> one team)
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,        # delete meetings if team is deleted
        related_name="meetings",         # allows team.meetings access
        null=True,
        blank=True
    )

    # stores the logged-in user who created the meeting
    # this replaces the old created_by_name text field
    # ForeignKey linking to Django's built-in User model
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,        # delete meetings if user is deleted
        related_name="created_meetings", # allows user.created_meetings
        null=True,
        blank=True
    )

    # timestamps
    # auto_now_add = set once when created
    created_at = models.DateTimeField(auto_now_add=True)

    # auto_now = updates every time the object is saved
    updated_at = models.DateTimeField(auto_now=True)

    # controls how meeting is displayed in admin
    def __str__(self):
        # shows meeting title instead of "Meeting object (1)"
        return self.title


# creating a meeting attendee table to store data about it
class MeetingAttendee(models.Model):
    # links the attendee to a meeting
    # one meeting can have many attendees
    meeting = models.ForeignKey(
        Meeting,
        on_delete=models.CASCADE,        # delete attendees if meeting is deleted
        related_name='attendees'         # allows meeting.attendees access
    )

    # links attendee to a real Django user instead of storing their name as text
    # this replaces the old attendee_name text field
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,        # delete attendee if user is deleted
        related_name="meeting_attendances",
        null=True,
        blank=True
    )

    # stores response (Pending, Accepted, Declined)
    # default = Pending when first created
    attendee_status = models.CharField(max_length=50, default='Pending')

    # stores when the attendee responded
    # null=True means it can be empty in database
    # blank=True means optional in forms
    response_at = models.DateTimeField(null=True, blank=True)

    # controls how the attendee records are shown in admin
    def __str__(self):
        # if user exists, show username + meeting title
        if self.user:
            return self.user.username + " - " + self.meeting.title

        # fallback if user is missing
        return "Unknown attendee - " + self.meeting.title