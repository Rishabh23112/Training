from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import TaskForm
from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = super().get_queryset()

        if not queryset.exists():
            messages.info(self.request, "No task found!")

        return queryset


class TaskCreateView(
    CreateView,
):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        messages.success(self.request, "Task created successfully")
        return super().form_valid(form)


# Create your views here.
