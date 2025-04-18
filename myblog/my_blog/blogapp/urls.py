from django.urls import path
from . import views
app_name = 'blogapp'
urlpatterns = [
	# post views
	path('', views.post_list, name='post_list'),#The path for the post list view
	path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),#The path for the post detail view
	path('<int:post_id>/share/', views.post_share, name='post_share'),#The path for the share post view
	]