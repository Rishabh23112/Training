from django import forms
from django.utils import timezone

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "status",
            "due_date",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Enter the title",
                }
            ),
            "description": forms.Textarea(
                attrs={"placeholder": "Enter the task description", "rows": 5}
            ),
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()

        if not title:
            raise forms.ValidationError("Enter title")
        return title

    def clean_due_date(self):
        due_date = self.cleaned_data.get("due_date")

        if due_date and due_date < timezone.localdate():
            raise forms.ValidationError("Due date cannot be in the past.")
        return due_date

    def clean_status(self):
        status = self.cleaned_data["status"]

        valid_status = [Task.Status.TODO, Task.Status.IN_PROGRESS, Task.Status.DONE]

        if status not in valid_status:
            raise forms.ValidationError("Invalid Status.")
        return status
