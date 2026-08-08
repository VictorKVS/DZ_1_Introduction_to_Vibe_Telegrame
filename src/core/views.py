from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Evidence, Goal, Problem, Project, Source
from .serializers import EvidenceSerializer, GoalSerializer, ProblemSerializer, ProjectSerializer, SourceSerializer


class OwnedProjectQuerysetMixin:
    permission_classes = [IsAuthenticated]

    def get_project_filter(self):
        return {"project__owner": self.request.user}


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GoalViewSet(OwnedProjectQuerysetMixin, viewsets.ModelViewSet):
    serializer_class = GoalSerializer

    def get_queryset(self):
        return Goal.objects.filter(**self.get_project_filter()).order_by("-created_at")


class ProblemViewSet(OwnedProjectQuerysetMixin, viewsets.ModelViewSet):
    serializer_class = ProblemSerializer

    def get_queryset(self):
        return Problem.objects.filter(**self.get_project_filter()).order_by("-created_at")


class SourceViewSet(OwnedProjectQuerysetMixin, viewsets.ModelViewSet):
    serializer_class = SourceSerializer

    def get_queryset(self):
        return Source.objects.filter(**self.get_project_filter()).order_by("-created_at")


class EvidenceViewSet(OwnedProjectQuerysetMixin, viewsets.ModelViewSet):
    serializer_class = EvidenceSerializer

    def get_queryset(self):
        return Evidence.objects.filter(**self.get_project_filter()).order_by("-created_at")
