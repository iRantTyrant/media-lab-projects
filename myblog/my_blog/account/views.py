from django.shortcuts import render
from django.urls import path 
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm

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
                return redirect('home')  # Redirect after login
            else:
                form.add_error(None, 'Invalid username/email or password')

    else:
        form = CustomAuthenticationForm()

    return render(request, 'account/templates/login.html', {'form': form})
