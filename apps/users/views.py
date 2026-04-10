from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group

@unauthenticated_user # Sign up
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            group, created = Group.objects.get_or_create(name='User')
            user.groups.add(group)

            Profile.objects.create(
                user=user,
                email=user.email,
                name=user.username
            )

            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created for ' + username)
            return redirect('login')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'users/signup.html', context)

@unauthenticated_user # Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect.')

    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request, "home")