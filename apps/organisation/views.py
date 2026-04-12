from django.shortcuts import render


def organisation_portal(request):
    return render(request, "organisation/index.html")
