from __future__ import annotations

import uuid

from django.conf import settings
from django.db import models

from core.models import Evidence, Goal, Problem, Project, TimeStampedModel


class DecisionSession(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="decision_sessions")
    problem = models.ForeignKey(Problem, on_delete=models.PROTECT, related_name="decision_sessions")
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=32, default="OPEN")
    initiated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="decision_sessions")
    token_cost = models.PositiveBigIntegerField(default=0)
    monetary_cost = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    latency_ms = models.PositiveBigIntegerField(default=0)


class Alternative(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session = models.ForeignKey(DecisionSession, on_delete=models.CASCADE, related_name="alternatives")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    estimated_cost = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    estimated_time_hours = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    risk_score = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)
    benefit_score = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)
    status = models.CharField(max_length=32, default="CONSIDERED")
    rejection_reason = models.TextField(blank=True)


class ExpertReview(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session = models.ForeignKey(DecisionSession, on_delete=models.CASCADE, related_name="expert_reviews")
    expert_role = models.CharField(max_length=128)
    methodology = models.CharField(max_length=128, blank=True)
    recommendation = models.TextField()
    confidence = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)
    evidence = models.ManyToManyField(Evidence, related_name="expert_reviews", blank=True)
    risks = models.JSONField(default=list, blank=True)
    assumptions = models.JSONField(default=list, blank=True)
    model_provider = models.CharField(max_length=64, blank=True)
    model_name = models.CharField(max_length=128, blank=True)
    tokens = models.PositiveIntegerField(default=0)
    monetary_cost = models.DecimalField(max_digits=12, decimal_places=4, default=0)


class Decision(TimeStampedModel):
    class Status(models.TextChoices):
        PROPOSED = "PROPOSED", "Proposed"
        ACCEPTED = "ACCEPTED", "Accepted"
        IMPLEMENTED = "IMPLEMENTED", "Implemented"
        VALIDATED = "VALIDATED", "Validated"
        REVISED = "REVISED", "Revised"
        REJECTED = "REJECTED", "Rejected"
        DEPRECATED = "DEPRECATED", "Deprecated"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session = models.OneToOneField(DecisionSession, on_delete=models.PROTECT, related_name="decision")
    selected_alternative = models.ForeignKey(Alternative, on_delete=models.PROTECT, related_name="selected_by_decisions")
    title = models.CharField(max_length=255)
    rationale = models.TextField()
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.PROPOSED)
    confidence = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)
    evidence = models.ManyToManyField(Evidence, related_name="decisions", blank=True)
    goals = models.ManyToManyField(Goal, related_name="decisions", blank=True)
    expected_effects = models.JSONField(default=list, blank=True)
    validation_plan = models.JSONField(default=dict, blank=True)


class HumanGate(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    decision = models.OneToOneField(Decision, on_delete=models.CASCADE, related_name="human_gate")
    required = models.BooleanField(default=True)
    approver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="decision_approvals", null=True, blank=True)
    result = models.CharField(max_length=32, blank=True)
    comment = models.TextField(blank=True)
    decided_at = models.DateTimeField(null=True, blank=True)
