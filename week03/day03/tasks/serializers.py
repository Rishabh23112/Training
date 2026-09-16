from django.utils import timezone
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "user",
            "title",
            "status",
            "description",
            "due_date",
            "created_at",
            "updated_at",
        ]

        read_only_fields = ["id", "created_at", "updated_at", "user"]

    def validate_title(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Enter title")
        return value.strip()

    def validate_due_date(self, value):
        if value and value <= timezone.localdate():
            raise serializers.ValidationError("Due date should be the upcoming date.")
        return value
