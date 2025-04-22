from django.urls import path # Importing path from django.urls to define URL patterns
from .views import login_view # Importing views for login, logout, and signup
from django.contrib.auth import views as auth_views # Importing auth views for authentication
from django.urls import reverse_lazy # Importing reverse_lazy for URL redirection
from django.views.generic import TemplateView # Importing TemplateView for rendering templates

app_name = 'account' # Setting the app name for namespacing URLs 
# URL patterns for the account app
urlpatterns = [
    path('login/', login_view, name='login'), # URL for login view
    path('logout/',auth_views.LogoutView.as_view(next_page=reverse_lazy('account:logged_out')),name='logout'), # URL for django based logout view
    path('logged-out/', TemplateView.as_view(template_name='logout.html'), name='logged_out'),# URL for custom logged out view
    # path('signup/', signup_view, name='signup'), # URL for signup view (commented out)
]