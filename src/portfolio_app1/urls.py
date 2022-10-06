from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("projects/", views.projects, name="projects"),
    path("project/<slug:slug>", views.project, name="project"),
    path("profile/", views.profile, name="profile"),
    # CRUD PATHS
    path("create_project/", views.create_project, name="create_project"),
    path("update_project/<slug:slug>", views.update_project, name="update_project"),
    path("delete_project/<slug:slug>", views.delete_project, name="delete_project"),
    path("send_email/", views.send_email, name="send_email"),
    path("contact/", views.contact_page, name="contact_page"),
]
