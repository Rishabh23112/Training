from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from .forms import TaskForm
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"
    paginate_by = 10

    def get_queryset(self):
        queryset = (
            Task.objects
            .filter(owner=self.request.user)
            .order_by("-created_at")
        )

        search = self.request.GET.get("search", "").strip()
        status_filter = self.request.GET.get("status", "").strip()
        due_date = self.request.GET.get("due_date", "").strip()

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search)
                | Q(description__icontains=search)
            )

        if status_filter:
            queryset = queryset.filter(
                status=status_filter
            )

        if due_date:
            queryset = queryset.filter(
                due_date=due_date
            )

        return queryset


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user

        response = super().form_valid(form)

        messages.success(
            self.request,
            "Task created successfully.",
        )

        return response


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task-list")

    def get_queryset(self):
        return Task.objects.filter(
            owner=self.request.user
        )

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(
            self.request,
            "Task updated successfully.",
        )

        return response


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/task_delete.html"
    success_url = reverse_lazy("task-list")

    def get_queryset(self):
        return Task.objects.filter(
            owner=self.request.user
        )

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(
            self.request,
            "Task deleted successfully.",
        )

        return response