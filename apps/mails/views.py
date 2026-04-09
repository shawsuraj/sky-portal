from django.shortcuts import render

# Create your views here.

# Export base.html
def mails(request) :
    return render(request, "mails/index.html")

def inbox(request) :
    return render(request, "mails/inbox.html")