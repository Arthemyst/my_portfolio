from django.shortcuts import render
from portfolio_app1.models import Project
from django.http import HttpResponse

def home(request):
    return render(request, 'portfolio_app1/home.html')

def projects(request):
    return render(request, 'portfolio_app1/projects.html')

def project(request):
    return render(request, 'portfolio_app1/project.html')

def profile(request):
    return render(request, 'portfolio_app1/profile.html')





