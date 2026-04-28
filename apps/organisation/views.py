import json
from django.shortcuts import render
from django.http import JsonResponse

from apps.teams.models import Team, Department, TeamDependency

# one colour per department - these match the actual dept names loaded from the excel
# picked colours that look decent on the dark vis.js canvas
DEPT_COLOURS = {
    "xTV_Web":          "#e74c3c",
    "Native TVs":       "#3498db",
    "Mobile":           "#f39c12",
    "Reliability_Tool": "#9b59b6",
    "Arch":             "#2ecc71",
    "Programme":        "#f1c40f",
}

# fallback colour if a dept name doesnt match any of the above
DEFAULT_COLOUR = "#6c757d"


def organisation_portal(request):
    # grab all departments and their teams from the db
    departments = Department.objects.prefetch_related("teams").select_related("organisation")
    teams = Team.objects.select_related("department")
    dep_count = TeamDependency.objects.count()

    # build a list of dept summary dicts for the legend and stat cards
    dept_summaries = []
    for dept in departments:
        colour = DEPT_COLOURS.get(dept.department_name, DEFAULT_COLOUR)
        dept_summaries.append({
            "name":       dept.department_name,
            "colour":     colour,
            "team_count": dept.teams.count(),
        })

    context = {
        "departments":       departments,
        "teams":             teams,
        "team_count":        teams.count(),
        "dep_count":         dep_count,
        "dept_summaries":    dept_summaries,
        # send colours as json so the js can read them
        "dept_colours_json": json.dumps(DEPT_COLOURS),
    }
    return render(request, "organisation/index.html", context)


def org_graph_data(request):
    # this is the json endpoint vis.js calls to build the network graph
    # supports filtering by ?dept= and ?dep_type= from the dropdowns

    dept_filter     = request.GET.get("dept", "")
    dep_type_filter = request.GET.get("dep_type", "")

    teams_qs = Team.objects.select_related("department")
    if dept_filter:
        teams_qs = teams_qs.filter(department__department_name=dept_filter)

    nodes = []
    for team in teams_qs:
        dept_name = team.department.department_name
        colour = DEPT_COLOURS.get(dept_name, DEFAULT_COLOUR)

        # build the tooltip that shows when you hover over a node
        tooltip = (
            f"<b>{team.team_name}</b><br>"
            f"Leader: {team.leader_name or '&mdash;'}<br>"
            f"Dept: {dept_name}<br>"
            f"Skills: {team.skills or '&mdash;'}"
        )

        nodes.append({
            "id":    team.id,
            "label": team.team_name,
            "title": tooltip,
            "color": {
                "background": colour,
                "border":     colour,
                "highlight":  {"background": colour, "border": "#000"},
            },
            "font":  {"color": "#ffffff", "size": 13},
            "shape": "dot",
            "size":  22,
            "dept":  dept_name,
        })

    team_ids = {t.id for t in teams_qs}

    # grab all dependencies and filter to only ones where both teams are visible
    deps_qs = TeamDependency.objects.select_related("upstream_team", "downstream_team")
    if dep_type_filter:
        deps_qs = deps_qs.filter(dependency_type=dep_type_filter)

    edges = []
    for dep in deps_qs:
        if dep.upstream_team_id in team_ids and dep.downstream_team_id in team_ids:
            edges.append({
                "from":   dep.upstream_team_id,
                "to":     dep.downstream_team_id,
                "label":  dep.dependency_type,
                "title":  dep.dependency_type,
                "arrows": "to",
                "color":  {"color": "#adb5bd", "highlight": "#495057"},
                "font":   {"size": 10, "color": "#6c757d"},
                "smooth": {"type": "curvedCW", "roundness": 0.2},
            })

    return JsonResponse({"nodes": nodes, "edges": edges})
