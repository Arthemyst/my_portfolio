from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .filters import ProjectFilter
from .forms import ProjectForm
from .models import Project


def home(request):
    return render(request, "portfolio_app1/home.html")


def projects(request):
    projects = Project.objects.filter(active=True)
    my_filter = ProjectFilter(request.GET, queryset=projects)
    projects = my_filter.qs
    context = {"projects": projects, "my_filter": my_filter}
    return render(request, "portfolio_app1/projects.html", context)


def project(request, pk):
    project = Project.objects.get(id=pk)

    context = {"project": project}
    return render(request, "portfolio_app1/project.html", context)


def profile(request):
    return render(request, "portfolio_app1/profile.html")


# CRUD VIEWS


@login_required(login_url="home")
def create_project(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("projects")

    context = {"form": form}
    return render(request, "portfolio_app1/project_form.html", context)


@login_required(login_url="home")
def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
        return redirect("projects")

    context = {"form": form}
    return render(request, "portfolio_app1/project_form.html", context)


@login_required(login_url="home")
def delete_project(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect("projects")
    context = {"item": project}
    return render(request, "portfolio_app1/delete.html", context)
