"""Routing URLs"""
from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("api/tasks/", views.api_tasks_list, name="task_list"),
]
