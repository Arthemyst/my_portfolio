from django.shortcuts import render
from portfolio_app1.models import Project


def home(request):
    return render(request, 'portfolio_app1/home.html')

def projects(request):
    Projects = Project.objects.all()

    context = {'projects': projects}
    return render(request, 'portfolio_app1/projects.html', context)

def project(request):
    return render(request, 'portfolio_app1/project.html')

def profile(request):
    return render(request, 'portfolio_app1/profile.html')





