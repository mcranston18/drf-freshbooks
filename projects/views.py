from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    # queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
