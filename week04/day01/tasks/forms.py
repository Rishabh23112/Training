from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "due_date", "priority"]

        widgets = {
            "title": forms.TextInput(
                attrs={"placeholer": "Enter task title", "class": "form-input"}
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Enter task description",
                    "rows": 5,
                    "class": "form-input",
                }
            ),
            "status": forms.Select(attrs={"class": "form-input"}),
            "due_date": forms.DateInput(attrs={"type": "date", "class": "form-input"}),
            "priority": forms.Select(attrs={"class": "form-input"}),
        }
