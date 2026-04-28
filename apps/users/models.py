from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model): # Full profle attribute list
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null = True, blank= True, upload_to="profile_pics/", default="profile_pics/profile.png")
    forename = models.CharField(max_length=50, null=True, blank=True)
    surname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username
    