from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, help_text='Required.')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, help_text='Required.')
