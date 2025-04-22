from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, help_text='Required.', required=True,widget=forms.TextInput(attrs={
        'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300 placeholder-gray-400',
        'placeholder': 'Username',
        'autofocus': True,
        }))
    password = forms.CharField(max_length=128, help_text='Required.',required=True, widget=forms.PasswordInput(attrs={
        'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300 placeholder-gray-400',}))
