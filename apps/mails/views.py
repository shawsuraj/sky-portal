from django.shortcuts import render

# Create your views here.

# Export base.html
def mails(request) :
    return render(request, "mails/index.html")

def inbox(request) :
    return render(request, "mails/inbox.html")

def compose_message(request) :
    return render(request, "mails/compose_message.html")

def view_draft(request) :
    return render(request, "mails/view_draft.html")

def sent_message(request) :
    return render(request, "mails/sent_message.html")