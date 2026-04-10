from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func): # Restricts view for unathenticated users
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]): # Selected user roles are eligible to view
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            return HttpResponse('You are not authorised to view this page.')
        return wrapper_func
    return decorator


def admin_only(view_func): #Admin only restriction
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'User':
            return redirect('user-page')
        if group == 'Admin':
            return view_func(request, *args, **kwargs)

        return HttpResponse('You are not authorised to view this page.')
    return wrapper_function