from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    forename = forms.CharField(required=True)
    surname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("forename", "surname", "username", "email", "phone", "password1", "password2")


class ProfileForm(forms.ModelForm): # Extra details for the user
    class Meta:
        model = Profile
        fields = ["forename", "surname", "phone", "profile_pic"]
