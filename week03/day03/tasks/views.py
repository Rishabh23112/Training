from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Restrict retreived tasks to the requesting user"""
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Assigns current authenticated user as the owner of the task"""
        serializer.save(user=self.request.user)


# Create your views here.
