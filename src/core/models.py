from __future__ import annotations

import uuid

from django.conf import settings
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(TimeStampedModel):
    class Status(models.TextChoices):
        IDEA = "IDEA", "Idea"
        ACTIVE = "ACTIVE", "Active"
        PAUSED = "PAUSED", "Paused"
        COMPLETED = "COMPLETED", "Completed"
        ARCHIVED = "ARCHIVED", "Archived"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.IDEA)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="father_projects")

    def __str__(self) -> str:
        return self.name


class Goal(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="goals")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    target_metric = models.CharField(max_length=255, blank=True)
    target_value = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=32, default="ACTIVE")

    def __str__(self) -> str:
        return self.title


class Problem(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="problems")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    goals = models.ManyToManyField(Goal, related_name="problems", blank=True)
    severity = models.CharField(max_length=16, default="MEDIUM")
    status = models.CharField(max_length=32, default="OPEN")

    def __str__(self) -> str:
        return self.title


class Source(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="sources")
    title = models.CharField(max_length=255)
    source_type = models.CharField(max_length=64)
    uri = models.TextField(blank=True)
    content_hash = models.CharField(max_length=128, blank=True, db_index=True)
    acquired_at = models.DateTimeField(null=True, blank=True)
    trust_score = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)
    classification = models.CharField(max_length=64, default="INTERNAL")

    def __str__(self) -> str:
        return self.title


class Evidence(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="evidence")
    source = models.ForeignKey(Source, on_delete=models.PROTECT, related_name="evidence_items")
    problems = models.ManyToManyField(Problem, related_name="evidence_items", blank=True)
    summary = models.TextField()
    locator = models.CharField(max_length=512, blank=True, help_text="Page, line range, section, symbol or other source locator")
    confidence = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)
    status = models.CharField(max_length=32, default="CANDIDATE")

    def __str__(self) -> str:
        return f"Evidence {self.id}"
