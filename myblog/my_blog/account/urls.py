# Importing path from django.urls to define URL patterns
from django.urls import path 

# Importing views for login, logout, and signup
from .views import login_view , register_view

# Importing auth views for authentication password change , reset password , and login logout built in django views
from django.contrib.auth import views as auth_views 

 # Importing reverse_lazy for URL redirection
from django.urls import reverse_lazy

# Importing TemplateView for rendering templates
from django.views.generic import TemplateView 


app_name = 'account' # Setting the app name for namespacing URLs 
# URL patterns for the account app
urlpatterns = [
    # This will include the default auth URLs provided by Django
    # path('accounts/', include('django.contrib.auth.urls')), # This line is commented out because we are defining our own URLs below 
    
    # URL for login view
    path('login/', login_view, name='login'), 

    #URL for Logged out view (We use the built in django logout view but redirect to our own template using our next_page parameter)
    path('logout/',
        auth_views.LogoutView.as_view(next_page=reverse_lazy('account:logged_out')),
        name='logout'),
    
    # URL for logged out view (This is the template that will be shown after logging out)
    path('logged-out/', 
        TemplateView.as_view(template_name='logout.html'), 
        name='logged_out'),
    
    #URL for password change view (We use the built in django password change view but redirect to our own template using our success_url parameter)
    path('password-change/',
        auth_views.PasswordChangeView.as_view(template_name='account/password_change_form.html',
        success_url=reverse_lazy('account:password_change_done')),
        name='password_change'),
    
    #URL for password change done view (This is the template that will be shown after changing the password)
    path('password-change/done/', 
        auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), 
        name='password_change_done'),#Success URL for password change done view

    #URL for password reset view (We use the built in django password reset view but redirect to our own template using template_name parameter)
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset_form.html',
    email_template_name='account/password_reset_email.html',
    success_url=reverse_lazy('account:password_reset_done')) ,
    name='password_reset'),

    #URL for password reset done view (This is the template that will be shown after requesting a password reset) It's a confirmation page
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), 
    name='password_reset_done'),
    
    #URL for password reset confirm view (This is the template that will be shown after clicking the link in the email)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html',
    success_url=reverse_lazy('account:password_reset_complete')), 
    name='password_reset_confirm'),
    
    #URL for password reset complete view (This is the template that will be shown after resetting the password)
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),

    #URL for signup view (This is the template that will be shown after successfully signing up)
    path('register/', register_view, name='register'),
]