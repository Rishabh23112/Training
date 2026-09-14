from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task

        fields = ["title", "description", "status", "due_date"]

        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter task title"}),
            "description": forms.Textarea(
                attrs={"placeholder": "Enter task description", "rows": 5}
            ),
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }
