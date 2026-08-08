from rest_framework.routers import DefaultRouter

from .views import EvidenceViewSet, GoalViewSet, ProblemViewSet, ProjectViewSet, SourceViewSet

router = DefaultRouter()
router.register("projects", ProjectViewSet, basename="project")
router.register("goals", GoalViewSet, basename="goal")
router.register("problems", ProblemViewSet, basename="problem")
router.register("sources", SourceViewSet, basename="source")
router.register("evidence", EvidenceViewSet, basename="evidence")

urlpatterns = router.urls
