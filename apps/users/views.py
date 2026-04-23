from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group

@unauthenticated_user # Sign up
def signup_view(request):
    if request.method == 'POST': # If submitted
        form = SignUpForm(request.POST)
        if form.is_valid(): # If valid
            user = form.save() # Save details as user

            group, created = Group.objects.get_or_create(name='User') # Add to user
            user.groups.add(group)

            Profile.objects.create( # Profile = user + extra details/attributes
                user=user,
                email=user.email,
                name=user.username
            ) 

            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created for ' + username) # Message
            return redirect('login') # Redirect user to login page
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'users/signup.html', context)

@unauthenticated_user # Login
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


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request, "home")

@login_required(login_url="login")
def update_profile(request):
    profile, created = Profile.objects.get_or_create(
        user=request.user,
        defaults={
            "email": request.user.email,
            "name": request.user.username,
        }
    )

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("base")
    else:
        form = ProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'users/update_profile.html', context)

# shows the logged-in user's profile page

@login_required(login_url="login")

def view_profile(request):

    profile = Profile.objects.get(user=request.user)

    context = {

        "profile": profile

    }

    return render(request, "users/view_profile.html", context)
