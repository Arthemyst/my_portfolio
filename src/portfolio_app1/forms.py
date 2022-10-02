from django import forms
from django.forms import ModelForm

from portfolio_app1.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
        }
