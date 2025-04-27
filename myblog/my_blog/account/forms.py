#Importing the necessary form class
from django import forms

#Importing the built in Authentication Form (for the login form)
from django.contrib.auth.forms import AuthenticationForm

#Imporing the built in UserCreationForm (for the registration form)
from django.contrib.auth.forms import UserCreationForm 

#Importing the User model from django.contrib.auth.models
from django.contrib.auth.models import User

#Import the Profile model from the models module in the same directory
from .models import Profile

#Login form for the login page with Tailwind CSS classes 
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, help_text='Required.', required=True,widget=forms.TextInput(attrs={
        'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300 placeholder-gray-400',
        'placeholder': 'Username',
        'autofocus': True,
        }))
    password = forms.CharField(max_length=128, help_text='Required.',required=True, widget=forms.PasswordInput(attrs={
        'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300 placeholder-gray-400',
        'placeholder': 'Password',
        }))

#Registration form 

class CustomUserCreationForm(UserCreationForm):
    bio = forms.CharField(required=False, widget=forms.Textarea())
    location = forms.CharField(required=False, widget=forms.TextInput())
    birthdate = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        
        # Save the user, including email
        if commit:
            user.email = self.cleaned_data['email']
            user.save()
        
        # Create or update the Profile object
        profile, created = Profile.objects.get_or_create(user=user)
        # Update the profile fields, whether it was created or already exists
        profile.bio = self.cleaned_data.get('bio', '')
        profile.location = self.cleaned_data.get('location', '')
        profile.birth_date = self.cleaned_data.get('birthdate', None)
        
        # Save the profile object
        profile.save()
        
        return user
#We are gonna reuse some of the fields from the CustomUserCreationForm in the profile view to update the user profile. 
#This is one way to customize a form but keep the default functionality of the AuthenticationForm form Django . The other way is shown in the regisetr.html where we connect the logic from django to html and just use regular Tailwind CSS classes to style the form.

