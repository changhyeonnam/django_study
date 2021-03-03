from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('<h1>Blog Home<h1>') # home view function

def about(request):
	return HttpResponse('<h1>Blog About<h1>') # about view function
# Create your views here.

# Create your views here.
