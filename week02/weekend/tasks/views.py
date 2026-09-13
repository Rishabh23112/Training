from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import TaskForm
from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"
    paginate_by = 10

    def get_queryset(self):
        queryset = Task.objects.all()

        query = self.request.GET.get("q", "").strip()
        due_before = self.request.GET.get("due_before", "").strip()

        if query:
            queryset = queryset.filter(title__icontains=query)

        if due_before:
            queryset = queryset.filter(due_date__lt=due_before)

        return queryset


class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = "task"


class TaskCreateView(SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task-list")
    success_message = "Task created successfully."


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task-list")
    success_message = "Task updated successfully."


class TaskDeleteView(SuccessMessageMixin, DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("task-list")
    success_message = "Task deleted successfully."


# Create your views here.
