# Importing path from django.urls to define URL patterns
from django.urls import path 

# Importing views for login, logout, and signup
from .views import login_view 

# Importing auth views for authentication password change , reset password , and login logout built in django views
from django.contrib.auth import views as auth_views 

 # Importing reverse_lazy for URL redirection
from django.urls import reverse_lazy

# Importing TemplateView for rendering templates
from django.views.generic import TemplateView 


app_name = 'account' # Setting the app name for namespacing URLs 
# URL patterns for the account app
urlpatterns = [
    path('login/', login_view, name='login'), # URL for login view
    path('logout/',auth_views.LogoutView.as_view(next_page=reverse_lazy('account:logged_out')),name='logout'), # URL for django based logout view
    path('logged-out/', TemplateView.as_view(template_name='logout.html'), name='logged_out'),# URL for custom logged out view
    path('password-change/',auth_views.PasswordChangeView.as_view(template_name='account/password_change_form.html'),name='password_change'),# URL for password change view
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),#

]