import json
from django.shortcuts import render
from django.http import JsonResponse

# fake data for now - will swap to DB once we agree on models
# just enough to test the vis.js chart is working

FAKE_DEPARTMENTS = [
    {"name": "Frontend",   "colour": "#3498db"},
    {"name": "Backend",    "colour": "#2ecc71"},
    {"name": "DevOps",     "colour": "#9b59b6"},
    {"name": "Mobile",     "colour": "#f39c12"},
]

FAKE_TEAMS = [
    {"id": 1, "name": "Core Team",      "dept": "Backend",   "leader": "Alice Brown",  "skills": "Python, Django"},
    {"id": 2, "name": "Frontend Team",  "dept": "Frontend",  "leader": "James Carter", "skills": "React, TypeScript"},
    {"id": 3, "name": "API Squad",      "dept": "Backend",   "leader": "Sara Lee",     "skills": "REST, GraphQL"},
    {"id": 4, "name": "DevOps Crew",    "dept": "DevOps",    "leader": "Tom Hughes",   "skills": "Kubernetes, Docker"},
    {"id": 5, "name": "iOS Team",       "dept": "Mobile",    "leader": "Priya Patel",  "skills": "Swift, Xcode"},
    {"id": 6, "name": "Android Team",   "dept": "Mobile",    "leader": "Dan Kim",      "skills": "Kotlin, Jetpack"},
    {"id": 7, "name": "Security Team",  "dept": "DevOps",    "leader": "Emma Walsh",   "skills": "Pen Testing, SSL"},
    {"id": 8, "name": "Data Pipeline",  "dept": "Backend",   "leader": "Chris Yin",    "skills": "Spark, Airflow"},
]

FAKE_DEPS = [
    {"from": 2, "to": 3,  "type": "API Integration"},
    {"from": 1, "to": 3,  "type": "Core Services"},
    {"from": 3, "to": 4,  "type": "CI/CD"},
    {"from": 5, "to": 3,  "type": "API Integration"},
    {"from": 6, "to": 3,  "type": "API Integration"},
    {"from": 4, "to": 7,  "type": "Security Checks"},
    {"from": 1, "to": 8,  "type": "Data Processing"},
    {"from": 8, "to": 4,  "type": "Infra Support"},
]

# colours map sent to the template for the legend
DEPT_COLOURS = {d["name"]: d["colour"] for d in FAKE_DEPARTMENTS}


def organisation_portal(request):
    context = {
        "dept_summaries":    FAKE_DEPARTMENTS,
        "teams":             FAKE_TEAMS,
        "team_count":        len(FAKE_TEAMS),
        "dep_count":         len(FAKE_DEPS),
        "dept_colours_json": json.dumps(DEPT_COLOURS),
        # dropdown options for the dept filter
        "departments":       FAKE_DEPARTMENTS,
    }
    return render(request, "organisation/index.html", context)


def org_graph_data(request):
    # filter by dept if the dropdown was used
    dept_filter    = request.GET.get("dept", "")
    dep_type_filter = request.GET.get("dep_type", "")

    teams = FAKE_TEAMS
    if dept_filter:
        teams = [t for t in teams if t["dept"] == dept_filter]

    team_ids = {t["id"] for t in teams}

    nodes = []
    for t in teams:
        colour = DEPT_COLOURS.get(t["dept"], "#6c757d")
        nodes.append({
            "id":    t["id"],
            "label": t["name"],
            "title": f"<b>{t['name']}</b><br>Leader: {t['leader']}<br>Dept: {t['dept']}<br>Skills: {t['skills']}",
            "color": {"background": colour, "border": colour},
            "font":  {"color": "#fff", "size": 13},
            "shape": "dot",
            "size":  22,
            "dept":  t["dept"],
        })

    deps = FAKE_DEPS
    if dep_type_filter:
        deps = [d for d in deps if d["type"] == dep_type_filter]

    edges = []
    for d in deps:
        if d["from"] in team_ids and d["to"] in team_ids:
            edges.append({
                "from":   d["from"],
                "to":     d["to"],
                "label":  d["type"],
                "title":  d["type"],
                "arrows": "to",
                "color":  {"color": "#adb5bd"},
                "font":   {"size": 10, "color": "#6c757d"},
                "smooth": {"type": "curvedCW", "roundness": 0.2},
            })

    return JsonResponse({"nodes": nodes, "edges": edges})
