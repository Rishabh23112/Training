from django.utils import timezone
from rest_framework import serializers

from ..models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "owner",
            "title",
            "description",
            "due_date",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "owner", "created_at", "updated_at"]

    def due_date_validation(self, value):
        if value and value < timezone.localdate():
            raise serializers.ValidationError("Due date should be an upcoming date.")
        return value
