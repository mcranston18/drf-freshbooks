from rest_framework.viewsets import ModelViewSet

from projects.filters import ProjectFilter
from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    # filter_fields = ('status', 'budget')
    filter_class = ProjectFilter
    def get_queryset(self):
        queryset = Project.objects.filter(
            client__user__id=self.request.user.id
        )

        return queryset

