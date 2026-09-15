"""Views"""

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import TaskForm
from .models import Task


class TaskListView(ListView):
    """Task List"""
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"
    paginate_by = 4


class TaskCreateView(CreateView):
    """Create Tasks"""
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    context_object_name = "tasks"
    success_url = reverse_lazy("task-list")

    def form_valid(self, form):
        """If form passes validation success message will be thrown via form_valid"""
        messages.success(self.request, "Task created successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        """If any error gets triggered then error will be thrown via form_invalid"""
        messages.success(self.request, "Fix the error.")
        return super().form_invalid(form)


class TaskUpdateView(UpdateView):
    """Edit or Update Tasks"""
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    context_object_name = "tasks"
    success_url = reverse_lazy("task-list")

    def form_valid(self, form):
        """If form passes validation success message will be thrown via form_valid"""
        messages.success(self.request, "Task updated successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        """If any error gets triggered then error will be thrown via form_invalid"""
        messages.success(self.request, "Fix the error")
        return super().form_invalid(form)


class TaskDeleteView(SuccessMessageMixin, DeleteView):
    """Task delete"""
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("task-list")
    success_message = "Task deleted successfully."


# Create your views here.
