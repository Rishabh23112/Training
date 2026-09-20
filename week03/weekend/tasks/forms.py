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
                    "placeholder": "Enter task title",
                    "class": "form-control",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Enter description",
                    "class": "form-control",
                    "rows": 5,
                }
            ),
            "status": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "due_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()

        if not title:
            raise forms.ValidationError(
                "Title cannot be empty."
            )

        if len(title) > 200:
            raise forms.ValidationError(
                "Title must be 200 characters or fewer."
            )

        return title

    def clean_description(self):
        description = self.cleaned_data.get("description", "")

        if len(description) > 1000:
            raise forms.ValidationError(
                "Description must be 1000 characters or fewer."
            )

        return description

    def clean_due_date(self):
        due_date = self.cleaned_data.get("due_date")

        if (
            due_date
            and self.instance.pk is None
            and due_date <= timezone.localdate()
        ):
            raise forms.ValidationError(
                "Due date must be in the future."
            )

        return due_date

    def clean(self):
        cleaned_data = super().clean()

        status = cleaned_data.get("status")
        due_date = cleaned_data.get("due_date")

        if status == Task.Status.DONE and not due_date:

            pass

        return cleaned_data