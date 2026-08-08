import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_goal_problem_evidence_trace_and_tenant_isolation():
    User = get_user_model()
    owner = User.objects.create_user(username="owner", password="strong-test-password")
    other = User.objects.create_user(username="other", password="strong-test-password")

    owner_client = APIClient()
    owner_client.force_authenticate(owner)

    other_client = APIClient()
    other_client.force_authenticate(other)

    project_response = owner_client.post(
        "/api/v1/projects/",
        {"name": "Trace Demo", "description": "Goal to evidence trace"},
        format="json",
    )
    assert project_response.status_code == 201
    project_id = project_response.data["id"]

    goal_response = owner_client.post(
        "/api/v1/goals/",
        {
            "project": project_id,
            "title": "Improve decision quality",
            "target_metric": "validated_decision_ratio",
            "target_value": ">=0.90",
        },
        format="json",
    )
    assert goal_response.status_code == 201
    goal_id = goal_response.data["id"]

    problem_response = owner_client.post(
        "/api/v1/problems/",
        {
            "project": project_id,
            "title": "Decisions lack traceable evidence",
            "goals": [goal_id],
            "severity": "HIGH",
        },
        format="json",
    )
    assert problem_response.status_code == 201
    problem_id = problem_response.data["id"]

    source_response = owner_client.post(
        "/api/v1/sources/",
        {
            "project": project_id,
            "title": "Legacy Sokrat repository",
            "source_type": "GITHUB_REPOSITORY",
            "uri": "https://github.com/VictorKVS/Sokrat",
            "classification": "PUBLIC",
        },
        format="json",
    )
    assert source_response.status_code == 201
    source_id = source_response.data["id"]

    evidence_response = owner_client.post(
        "/api/v1/evidence/",
        {
            "project": project_id,
            "source": source_id,
            "problems": [problem_id],
            "summary": "Legacy implementation stores expert review rounds and decision history.",
            "locator": "legacy code review",
            "confidence": "0.900",
        },
        format="json",
    )
    assert evidence_response.status_code == 201

    # A different authenticated user must not see or attach data to the owner's project.
    assert other_client.get(f"/api/v1/projects/{project_id}/").status_code == 404
    forbidden_goal = other_client.post(
        "/api/v1/goals/",
        {"project": project_id, "title": "Cross-tenant write attempt"},
        format="json",
    )
    assert forbidden_goal.status_code == 400
