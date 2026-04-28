from django.urls import path
from . import views

urlpatterns = [
    path("", views.organisation_portal, name="organisation"),
    path("graph-data/", views.org_graph_data, name="org_graph_data"),
]
