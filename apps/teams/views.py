from django.shortcuts import render

def views_list(request):
    return render(request, 'teams/teams.html')