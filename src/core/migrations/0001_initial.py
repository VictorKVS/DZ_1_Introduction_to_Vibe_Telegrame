# Generated for the FATHER MVP baseline.

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("status", models.CharField(choices=[("IDEA", "Idea"), ("ACTIVE", "Active"), ("PAUSED", "Paused"), ("COMPLETED", "Completed"), ("ARCHIVED", "Archived")], default="IDEA", max_length=16)),
                ("owner", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="father_projects", to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Goal",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("target_metric", models.CharField(blank=True, max_length=255)),
                ("target_value", models.CharField(blank=True, max_length=255)),
                ("status", models.CharField(default="ACTIVE", max_length=32)),
                ("project", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="goals", to="core.project")),
            ],
        ),
        migrations.CreateModel(
            name="Problem",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("severity", models.CharField(default="MEDIUM", max_length=16)),
                ("status", models.CharField(default="OPEN", max_length=32)),
                ("goals", models.ManyToManyField(blank=True, related_name="problems", to="core.goal")),
                ("project", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="problems", to="core.project")),
            ],
        ),
        migrations.CreateModel(
            name="Source",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("source_type", models.CharField(max_length=64)),
                ("uri", models.TextField(blank=True)),
                ("content_hash", models.CharField(blank=True, db_index=True, max_length=128)),
                ("acquired_at", models.DateTimeField(blank=True, null=True)),
                ("trust_score", models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ("classification", models.CharField(default="INTERNAL", max_length=64)),
                ("project", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="sources", to="core.project")),
            ],
        ),
        migrations.CreateModel(
            name="Evidence",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("summary", models.TextField()),
                ("locator", models.CharField(blank=True, help_text="Page, line range, section, symbol or other source locator", max_length=512)),
                ("confidence", models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ("status", models.CharField(default="CANDIDATE", max_length=32)),
                ("problems", models.ManyToManyField(blank=True, related_name="evidence_items", to="core.problem")),
                ("project", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="evidence", to="core.project")),
                ("source", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="evidence_items", to="core.source")),
            ],
        ),
    ]
