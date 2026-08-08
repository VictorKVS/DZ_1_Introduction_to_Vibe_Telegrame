from rest_framework import serializers

from .models import Evidence, Goal, Problem, Project, Source


class ProjectOwnedSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.none())

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.user.is_authenticated and "project" in fields:
            fields["project"].queryset = Project.objects.filter(owner=request.user)
        return fields


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "description", "status", "owner", "created_at", "updated_at"]
        read_only_fields = ["id", "owner", "created_at", "updated_at"]


class GoalSerializer(ProjectOwnedSerializer):
    class Meta:
        model = Goal
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]


class ProblemSerializer(ProjectOwnedSerializer):
    goals = serializers.PrimaryKeyRelatedField(queryset=Goal.objects.none(), many=True, required=False)

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            fields["goals"].child_relation.queryset = Goal.objects.filter(project__owner=request.user)
        return fields

    def validate(self, attrs):
        attrs = super().validate(attrs)
        project = attrs.get("project") or getattr(self.instance, "project", None)
        for goal in attrs.get("goals", []):
            if project and goal.project_id != project.id:
                raise serializers.ValidationError({"goals": "All goals must belong to the selected project."})
        return attrs

    class Meta:
        model = Problem
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]


class SourceSerializer(ProjectOwnedSerializer):
    class Meta:
        model = Source
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]


class EvidenceSerializer(ProjectOwnedSerializer):
    source = serializers.PrimaryKeyRelatedField(queryset=Source.objects.none())
    problems = serializers.PrimaryKeyRelatedField(queryset=Problem.objects.none(), many=True, required=False)

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            fields["source"].queryset = Source.objects.filter(project__owner=request.user)
            fields["problems"].child_relation.queryset = Problem.objects.filter(project__owner=request.user)
        return fields

    def validate(self, attrs):
        attrs = super().validate(attrs)
        project = attrs.get("project") or getattr(self.instance, "project", None)
        source = attrs.get("source") or getattr(self.instance, "source", None)
        if project and source and source.project_id != project.id:
            raise serializers.ValidationError({"source": "Source must belong to the selected project."})
        for problem in attrs.get("problems", []):
            if project and problem.project_id != project.id:
                raise serializers.ValidationError({"problems": "All problems must belong to the selected project."})
        return attrs

    class Meta:
        model = Evidence
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
