"""Form"""
from django import forms
from django.utils import timezone

from .models import Task


class TaskForm(forms.ModelForm):
    """Clean the inputs for validation."""
    class Meta:
        """Metadata of the form"""
        model = Task

        fields = ["title", "description", "status", "due_date"]

        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter task title"}),
            "description": forms.Textarea(
                attrs={"placeholder": "Enter task description", "rows": 5}
            ),
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_title(self):
        """Clean title"""
        title = self.cleaned_data["title"].strip()

        if len(title) < 3:
            raise forms.ValidationError("Title should be greater than 3 characters.")
        return title

    def clean_due_date(self):
        """Clean due date"""
        due_date = self.cleaned_data.get("due_date")

        if due_date and due_date < timezone.localdate():
            raise forms.ValidationError("Due date should be an upcoming date.")
        return due_date

    def clean(self):
        """Cross field validation"""
        cleaned_data = super().clean()

        status = cleaned_data.get("status")
        due_date = cleaned_data.get("due_date")

        if status == Task.Status.DONE and not due_date:
            raise forms.ValidationError("Completed task must have due date.")

        return self.cleaned_data
