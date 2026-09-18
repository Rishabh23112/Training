from rest_framework.routers import DefaultRouter

from .views import TaskViewSet

router = DefaultRouter()

router.register("tasks", TaskViewSet, basename="api-task")

urlpatterns = router.urls
