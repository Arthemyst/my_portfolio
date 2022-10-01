from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("projects/", views.projects, name="projects"),
    path("project/<int:pk>", views.project, name="project"),
    path("profile/", views.profile, name="profile"),
    # CRUD PATHS
    path("create_project/", views.create_project, name="create_project"),
]
