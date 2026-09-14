from django.urls import path

from .views import TaskCreateView, TaskDeleteView, TaskListView, TaskUpdateView

urlpatterns = [
    path(
        "",
        TaskListView.as_view(),
        name="task-list",
    ),
    path(
        "create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path(
        "<int:pk>/edit/",
        TaskUpdateView.as_view(),
        name="task-edit",
    ),
    path(
        "<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
]
