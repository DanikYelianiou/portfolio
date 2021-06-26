from rest_framework import generics

from .serializers import ProjectListSerializer, ProjectDetailSerializer
from .models import Project
from .service import PaginationProjects


class ProjectView(generics.ListAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    pagination_class = PaginationProjects


class ProjectDetailView(generics.RetrieveAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
