from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Message
from .forms import MessageForm


@login_required(login_url="login")
def mails(request):
    return render(request, "mails/index.html")


@login_required(login_url="login")
def inbox(request):
    messages = Message.objects.filter(
        receiver=request.user,
        is_draft=False
    ).order_by("-timestamp")

    return render(request, "mails/inbox.html", {"messages": messages})


@login_required(login_url="login")
def compose_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user

            if "save_draft" in request.POST:
                message.is_draft = True
                message.save()
                return redirect("view_draft")

            if "send_message" in request.POST:
                message.is_draft = False
                message.save()
                return redirect("sent_message")
    else:
        form = MessageForm()

    return render(request, "mails/compose_message.html", {"form": form})


@login_required(login_url="login")
def view_draft(request):
    messages = Message.objects.filter(
        sender=request.user,
        is_draft=True
    ).order_by("-timestamp")

    if request.method == "POST" and "delete_draft" in request.POST:
        draft_id = request.POST.get("draft_id")
        draft = get_object_or_404(
            Message,
            id=draft_id,
            sender=request.user,
            is_draft=True
        )
        draft.delete()
        return redirect("view_draft")

    return render(request, "mails/view_draft.html", {"messages": messages})


@login_required(login_url="login")
def edit_draft(request, draft_id):
    draft = get_object_or_404(
        Message,
        id=draft_id,
        sender=request.user,
        is_draft=True
    )

    if request.method == "POST":
        form = MessageForm(request.POST, instance=draft)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user

            if "save_draft" in request.POST:
                message.is_draft = True
                message.save()
                return redirect("view_draft")

            if "send_message" in request.POST:
                message.is_draft = False
                message.save()
                return redirect("sent_message")
    else:
        form = MessageForm(instance=draft)

    return render(request, "mails/edit_draft.html", {"form": form, "draft": draft})


@login_required(login_url="login")
def sent_message(request):
    messages = Message.objects.filter(
        sender=request.user,
        is_draft=False
    ).order_by("-timestamp")

    return render(request, "mails/sent_message.html", {"messages": messages})