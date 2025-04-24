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

#Importing the UserCreationForm class for user registration
from django.contrib.auth.forms import UserCreationForm

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

def logged_out_view(request):
    return render(request, 'account/logged_out.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')  # or wherever you want
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})