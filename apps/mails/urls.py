from django.urls import path
from . import views

urlpatterns = [
    path("", views.mails, name="mails"),
    path("inbox/", views.inbox, name="inbox"),
    path("compose_message/", views.compose_message, name="compose_message"),
    path("sent_message/", views.sent_message, name="sent_message"),
    path("view_draft/", views.view_draft, name="view_draft"),
    path("edit_draft/<int:draft_id>/", views.edit_draft, name="edit_draft"),
]