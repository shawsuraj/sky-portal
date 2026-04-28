from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# login_not_required tells the global auth middleware to let these pages through without logging in
from django.contrib.auth.decorators import login_not_required
from .forms import SignUpForm
from .models import Profile
from .forms import ProfileForm
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group


# login/signup/logout are public - exempt them from the global login wall
@login_not_required
@unauthenticated_user
def signup_view(request):
    if request.method == 'POST': # If submitted
        form = SignUpForm(request.POST)
        if form.is_valid(): # If valid
            user = form.save() # Save details as user

            group, _ = Group.objects.get_or_create(name='User') # Add to user
            user.groups.add(group)

            Profile.objects.create( # Profile = user + extra details/attributes
                user=user,
                forename=form.cleaned_data.get("forename"),
                surname=form.cleaned_data.get("surname"),
                email=form.cleaned_data.get("email"),
                phone=form.cleaned_data.get("phone"),
            ) 

            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created for ' + username) # Message
            return redirect('login') # Redirect user to login page
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'users/signup.html', context)


@login_not_required
@unauthenticated_user
def login_view(request):
    if request.method == 'POST': # If submitted
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password) # Authenticate

        if user is not None: # If authenticated, redirect user to home page
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect.') # Else display error message

    return render(request, "users/login.html")


@login_not_required
def logout_view(request):
    logout(request)
    return redirect('login')


def update_profile(request):
    profile, _ = Profile.objects.get_or_create(
        user=request.user,
        defaults={
            "email": request.user.email,
        }
    )

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            # redirect to profile (full page with sidebar) not view_profile which is bare iframe content
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)

    context = {'form': form, "active_page": "profile"}
    return render(request, "users/update_profile.html", context)


def view_profile(request):
    # use get_or_create so it doesnt crash if the profile row doesnt exist yet
    profile, _ = Profile.objects.get_or_create(
        user=request.user,
        defaults={
            "email": request.user.email,
            "name": request.user.username,
        }
    )

    context = {
        "profile": profile,
        "active_page": "profile"
    }

    return render(request, "users/view_profile.html", context)


def settings_view(request):
    return render(request, 'users/settings.html')


def profile(request):
    return render(request, "users/profile.html", {"active_page": "profile"})
