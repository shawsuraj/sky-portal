from django.shortcuts import render

from .models import Report

# Create your views here.

def org_report(request):
    return render(request, 'organisation/org_report.html', {
        'organisation': Report.objects.all(),
    })
