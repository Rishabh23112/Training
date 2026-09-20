from rest_framework import serializers
from django.utils import timezone

from ..models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=[
            "id",
            "title",
            "description",
            "status",
            "due_date",
            "created_at",
            "updated_at"
        ]

        read_only_fields=["id", "owner", "created_at", "updated_at"]

    def validate_title(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Title cannot be empty")
        return value.strip()

    def validate_due_date(self, value):
        if value and value < timezone.localdate():
            raise serializers.ValidationError("Due date shouldn't be in the past")

    def validate_status(self, value):
        valid_status={
            Task.Status.TODO,
            Task.Status.IN_PROGRESS,
            Task.Status.DONE
        }

        if value not in valid_status:
            raise serializers.ValidationError("Invalid status")
        return value