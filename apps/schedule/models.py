# Placeholder: models for schedule
# imports for the models
from django.db import models


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

    # stores the team name
    team_name = models.CharField(max_length=100, blank=True)

    # stores the name of the person who created the meeting
    created_by_name = models.CharField(max_length=100, blank=True)

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

    # stores the attendee name
    attendee_name = models.CharField(max_length=100)

    # stores response (Pending, Accepted, Declined)
    attendee_status = models.CharField(max_length=50, default='Pending')

    # stores when the attendee responded
    response_at = models.DateTimeField(null=True, blank=True)

    # controls how the attendee records are shown in admin
    def __str__(self):
        return self.attendee_name + " - " + self.meeting.title