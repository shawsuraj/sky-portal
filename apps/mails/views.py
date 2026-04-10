from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# Export base.html
@login_required(login_url='login')  # Restricts access to page, only logged in users can view
def mails(request) :
    return render(request, "mails/index.html")

@login_required(login_url='login')
def inbox(request) :
    return render(request, "mails/inbox.html")

@login_required(login_url='login')
def compose_message(request) :
    return render(request, "mails/compose_message.html")

@login_required(login_url='login')
def view_draft(request) :
    return render(request, "mails/view_draft.html")

@login_required(login_url='login') 
def sent_message(request) :
    return render(request, "mails/sent_message.html")