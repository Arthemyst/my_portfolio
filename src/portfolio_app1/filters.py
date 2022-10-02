from tkinter import Widget
import django_filters
from django_filters import CharFilter

from .models import *

from django import forms

class ProjectFilter(django_filters.FilterSet):
    headline = CharFilter(field_name="headline", lookup_expr="icontains", label="Headline")
    tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Project
        fields = ['headline', 'tags']