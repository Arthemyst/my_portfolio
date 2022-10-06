from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .filters import ProjectFilter
from .forms import ProjectForm
from .models import Project
import environ
from pathlib import Path

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(BASE_DIR / ".env")


def home(request):
    return render(request, "portfolio_app1/home.html")


def projects(request):
    projects = Project.objects.filter(active=True)
    my_filter = ProjectFilter(request.GET, queryset=projects)
    projects = my_filter.qs
    project = request.GET.get("page")

    paginator = Paginator(projects.order_by("id"), 6)
    try:
        projects = paginator.page(project)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

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


def contact_page(request):
    return render(request, "portfolio_app1/contact.html")


def send_email(request):

    if request.method == "POST":

        template = render_to_string(
            "portfolio_app1/email_template.html",
            {
                "name": request.POST["name"],
                "email": request.POST["email"],
                "message": request.POST["message"],
            },
        )

        email = EmailMessage(
            request.POST["subject"],
            template,
            settings.EMAIL_HOST_USER,
            [env("EMAIL_HOST_USER")],
        )

        email.fail_silently = False
        email.send()

    return render(request, "portfolio_app1/email_sent.html")
