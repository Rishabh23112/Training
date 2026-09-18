from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import TaskForm
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task/task_list.html"
    paginate_by = 6
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = (
            Task.objects.filter(owner=self.request.user)
            .select_related("owner")
            .order_by("-created_at")
        )

        search = self.request.GET.get("search")
        due_date = self.request.GET.get("due_date")

        if search:
            queryset = queryset.filter(title__icontains=search)

        if due_date:
            queryset = queryset.filter(due_date=due_date)

        return queryset


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task/task_form.html"
    success_url = reverse_lazy("task-list")

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        form.instance.owner = self.request.user

        messages.success(self.request, "Task created successfully.")

        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task/task_form.html"
    success_url = reverse_lazy("task-list")

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Task updated successfully.")

        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView, SuccessMessageMixin):
    model = Task
    template_name = "task/task_delete.html"
    success_url = reverse_lazy("task-list")
    success_message = "Task deleted successfully."

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


# Create your views here.
