from django.contrib import admin # We import admin from django.contrib so we can register our models
from django.urls import include, path # Importing include and path from django.urls to define URL patterns

urlpatterns = [
	path('admin/', admin.site.urls),# Admin panel URL
	path('blogapp/', include('blogapp.urls', namespace='blogapp')),# URL for blogapp
	path('account/', include('account.urls', namespace='account')),# URL for account app
	]