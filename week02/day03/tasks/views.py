"""Django View """
from django.shortcuts import render


def home_view(request):
    """Renders home page"""
    return render(request, "home.html")


def api_tasks_list(request):
    """Renders tasks page along with the tasks."""
    sample_tasks = [
        {"id": 1, "title": "Setup Django Project", "status": "done"},
        {
            "id": 2,
            "title": "Configure Templates & Static Files",
            "status": "in_progress",
        },
        {"id": 3, "title": "Implementation", "status": "todo"},
    ]

    return render(request, "tasks/task_list.html", {"tasks": sample_tasks})


# Create your views here.
