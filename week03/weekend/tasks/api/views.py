from datetime import date

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tasks.models import Task

from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            Task.objects
            .filter(owner=self.request.user)
            .select_related("owner")
            .order_by("-created_at")
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        status_param = request.query_params.get("status")

        if status_param:
            valid_statuses = {
                Task.Status.TODO,
                Task.Status.IN_PROGRESS,
                Task.Status.DONE,
            }

            if status_param not in valid_statuses:
                return Response(
                    {
                        "detail": (
                            "Invalid status. Must be one of: "
                            "todo, in_progress, done"
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            queryset = queryset.filter(
                status=status_param
            )

        due_before = request.query_params.get(
            "due_before"
        )

        due_before_date = None

        if due_before:
            try:
                due_before_date = date.fromisoformat(
                    due_before
                )
            except ValueError:
                return Response(
                    {
                        "detail": (
                            "Invalid due_before date. "
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            queryset = queryset.filter(
                due_date__lte=due_before_date
            )

        due_after = request.query_params.get(
            "due_after"
        )

        due_after_date = None

        if due_after:
            try:
                due_after_date = date.fromisoformat(
                    due_after
                )
            except ValueError:
                return Response(
                    {
                        "detail": (
                            "Invalid due_after date. "
                            "Use YYYY-MM-DD format."
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            queryset = queryset.filter(
                due_date__gte=due_after_date
            )

        if (
            due_before_date
            and due_after_date
            and due_after_date > due_before_date
        ):
            return Response(
                {
                    "detail": (
                        "due_after must be earlier than "
                        "or equal to due_before."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(
                page,
                many=True,
            )

            return self.get_paginated_response(
                serializer.data
            )

        serializer = self.get_serializer(
            queryset,
            many=True,
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user
        )