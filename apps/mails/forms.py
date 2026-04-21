from django import forms
from django.contrib.auth.models import User
from .models import Message


class MessageForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = Message
        fields = ["receiver", "subject", "content"]
        widgets = {
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 6}),
        }