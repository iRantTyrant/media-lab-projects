#Importing the render function to render templates
from django.shortcuts import render

#Importing the path function to define URL patterns
from django.urls import path 

#Importing authentication views from Django's built-in auth module and login function
from django.contrib.auth import authenticate, login

#Importing the redirect function to redirect users after login and logout
from django.shortcuts import redirect

#Importing the CustomAuthenticationForm class for custom authentication
from .forms import CustomAuthenticationForm

#Importing the UserCreationForm class for user registration and its custom form
from .forms import CustomUserCreationForm

#Login required decorator to restrict access to certain views (profile view in this case)
from django.contrib.auth.decorators import login_required

from .models import Profile  # Importing the Profile model to handle user profiles

#Login view to handle user login
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Check if the input is an email or username
            if '@' in username_or_email:  # If it's an email
                user = authenticate(request, username=User.objects.get(email=username_or_email).username, password=password)
            else:  # If it's a username
                user = authenticate(request, username=username_or_email, password=password)

            if user is not None:
                login(request, user)
                return redirect('/blogapp/')  # Redirect after login
            else:
                form.add_error(None, 'Invalid username/email or password')

    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})

#Registration view to handle user registration
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the user and the profile

            return redirect('account:login')  # Redirect to login after registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'account/register.html', {'form': form})

# View to handle viewing and editing the user profile
@login_required
def profile_edit_view(request):
    # Get the logged-in user
    user = request.user
    profile = Profile.objects.get(user=user)  # Get the profile for the logged-in user
    
    # If the form is submitted with updated data
    if request.method == 'POST':
        # Create a form for updating profile information
        form = CustomUserCreationForm(request.POST)  # Using the same form or create a new one for profile
        if form.is_valid():
            # Update the user's profile fields
            profile.bio = form.cleaned_data.get('bio', profile.bio)
            profile.location = form.cleaned_data.get('location', profile.location)
            profile.birth_date = form.cleaned_data.get('birthdate', profile.birth_date)
            profile.save()  # Save the updated profile

            return redirect('profile')  # Redirect to the profile view after saving
    else:
        # Initialize the form with current profile data
        form = CustomUserCreationForm(initial={
            'bio': profile.bio,
            'location': profile.location,
            'birthdate': profile.birth_date,
        })

    return render(request, 'account/profile_edit.html', {'form': form})


#View to handle displaying the user profile
@login_required
def profile_view(request):
    user = request.user
    # Get the user's profile or create one if it doesn't exist
    profile, created = Profile.objects.get_or_create(user=user)

    # Pass the profile to the template for display
    return render(request, 'account/profile.html', {'profile': profile})