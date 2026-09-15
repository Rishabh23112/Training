"""Url routes for tasks app"""
from django.urls import path

from .views import TaskCreateView, TaskDeleteView, TaskListView, TaskUpdateView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("edit/<int:pk>", TaskUpdateView.as_view(), name="task-edit"),
    path("delete/<int:pk>", TaskDeleteView.as_view(), name="task-delete"),
]
