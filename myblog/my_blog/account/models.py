#We import the User model from django.contrib.auth.models so we can create a one-to-one relationship with our profile model
from django.contrib.auth.models import User
#We import the models module from django.db so we can create our profile model
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'

