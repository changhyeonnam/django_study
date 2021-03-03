from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name='blog-name'),
	path('about/', views.about, name='blog-about'),
	#don't need to add path for project urls.py for adding about.
]