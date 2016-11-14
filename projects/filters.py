import django_filters
from projects.models import Project
from projects.serializers import ProjectSerializer
from rest_framework import generics

class ProjectFilter(django_filters.rest_framework.FilterSet):
    min_budget = django_filters.NumberFilter(name="budget", lookup_expr='gte')
    max_budget = django_filters.NumberFilter(name="budget", lookup_expr='lte')

    class Meta:
        model = Project
        fields = [
            'client',
            'status'
        ]
