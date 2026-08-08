import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DecisionSession",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("status", models.CharField(default="OPEN", max_length=32)),
                ("token_cost", models.PositiveBigIntegerField(default=0)),
                ("monetary_cost", models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ("latency_ms", models.PositiveBigIntegerField(default=0)),
                ("initiated_by", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="decision_sessions", to=settings.AUTH_USER_MODEL)),
                ("problem", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="decision_sessions", to="core.problem")),
                ("project", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="decision_sessions", to="core.project")),
            ],
        ),
        migrations.CreateModel(
            name="Alternative",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("estimated_cost", models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ("estimated_time_hours", models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ("risk_score", models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ("benefit_score", models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ("status", models.CharField(default="CONSIDERED", max_length=32)),
                ("rejection_reason", models.TextField(blank=True)),
                ("session", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="alternatives", to="decisions.decisionsession")),
            ],
        ),
        migrations.CreateModel(
            name="ExpertReview",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("expert_role", models.CharField(max_length=128)),
                ("methodology", models.CharField(blank=True, max_length=128)),
                ("recommendation", models.TextField()),
                ("confidence", models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ("risks", models.JSONField(blank=True, default=list)),
                ("assumptions", models.JSONField(blank=True, default=list)),
                ("model_provider", models.CharField(blank=True, max_length=64)),
                ("model_name", models.CharField(blank=True, max_length=128)),
                ("tokens", models.PositiveIntegerField(default=0)),
                ("monetary_cost", models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ("evidence", models.ManyToManyField(blank=True, related_name="expert_reviews", to="core.evidence")),
                ("session", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="expert_reviews", to="decisions.decisionsession")),
            ],
        ),
        migrations.CreateModel(
            name="Decision",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("rationale", models.TextField()),
                ("status", models.CharField(choices=[("PROPOSED", "Proposed"), ("ACCEPTED", "Accepted"), ("IMPLEMENTED", "Implemented"), ("VALIDATED", "Validated"), ("REVISED", "Revised"), ("REJECTED", "Rejected"), ("DEPRECATED", "Deprecated")], default="PROPOSED", max_length=16)),
                ("confidence", models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ("expected_effects", models.JSONField(blank=True, default=list)),
                ("validation_plan", models.JSONField(blank=True, default=dict)),
                ("evidence", models.ManyToManyField(blank=True, related_name="decisions", to="core.evidence")),
                ("goals", models.ManyToManyField(blank=True, related_name="decisions", to="core.goal")),
                ("selected_alternative", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="selected_by_decisions", to="decisions.alternative")),
                ("session", models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name="decision", to="decisions.decisionsession")),
            ],
        ),
        migrations.CreateModel(
            name="HumanGate",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("required", models.BooleanField(default=True)),
                ("result", models.CharField(blank=True, max_length=32)),
                ("comment", models.TextField(blank=True)),
                ("decided_at", models.DateTimeField(blank=True, null=True)),
                ("approver", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name="decision_approvals", to=settings.AUTH_USER_MODEL)),
                ("decision", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="human_gate", to="decisions.decision")),
            ],
        ),
    ]
