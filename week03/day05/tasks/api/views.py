from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Task
from .pagination import TaskPagination
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = TaskPagination

    def get_queryset(self):
        return (
            Task.objects.filter(owner=self.request.user)
            .select_related("owner")
            .order_by("-created_at")
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
