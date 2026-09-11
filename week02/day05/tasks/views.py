from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import TaskForm
from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        due_date = self.request.GET.get("due_date")

        if q:
            queryset = queryset.filter(title__icontains=q)
        if due_date:
            queryset = queryset.filter(due_date=due_date)

        return queryset.order_by("due_date")


class TaskCreateView(CreateView, SuccessMessageMixin):
    model = Task
    template_name = "tasks/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("task-list")
    success_message = "Task Created"


class TaskUpdateView(UpdateView, SuccessMessageMixin):
    model = Task
    template_name = "tasks/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("task-list")
    success_message = "Task Updated"


class TaskDeleteView(DeleteView, SuccessMessageMixin):
    model = Task
    template_name = "tasks/task_delete.html"
    success_url = reverse_lazy("task-list")
    success_message = "Task Deleted"


# Create your views here.
