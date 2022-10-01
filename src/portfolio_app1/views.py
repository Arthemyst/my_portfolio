from django.shortcuts import render, redirect

from .models import Project
from .forms import ProjectForm

def home(request):
    return render(request, "portfolio_app1/home.html")


def projects(request):
    projects = Project.objects.filter(active=True)

    context = {"projects": projects}
    return render(request, "portfolio_app1/projects.html", context)


def project(request, pk):
    project = Project.objects.get(id=pk)

    context = {"project": project}
    return render(request, "portfolio_app1/project.html", context)


def profile(request):
    return render(request, "portfolio_app1/profile.html")


# CRUD VIEWS


def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('projects')

    context = {'form': form}
    return render(request, "portfolio_app1/project_form.html", context)
