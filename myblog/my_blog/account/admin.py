#We import admin from django.contrib so we can register our models
from django.contrib import admin
#We import our profile model from models.py so we can register it in the admin panel
from .models import Profile
# Register your models here.

#We register our profile model in the admin panel
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'location', 'birth_date']  # Display user (username from the User model) and the extra fields in the admin panel
    search_fields = ['user__username']  # Allow search by username (through user) and email
    list_filter = ['user__username']  # Allow filtering by username (through user) and email
    ordering = ['user__username']  # Order by username (through user) and email

admin.site.register(Profile, ProfileAdmin)