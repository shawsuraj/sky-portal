from django.shortcuts import render

# Create your views here.

# Export base.html
def home(request) :
    return render(request, "base.html")