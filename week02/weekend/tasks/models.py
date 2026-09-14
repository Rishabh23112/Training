
from django.utils import timezone

from django.db import models
from django.core.exceptions import ValidationError



class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "todo", "To-do"
        IN_PROGRESS = "in-progress", "In Progress"
        DONE = "done", "Done"

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.TODO
    )
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return str(self.title)

    def clean(self):
        errors = {}
        if self.due_date and not self.pk:
            if self.due_date <= timezone.localdate():
                errors["due_date"] = "Due date must be upcoming dates."

        if self.pk:
            old_task = Task.objects.get(pk=self.pk)

            allowed_transitions = {
                self.Status.TODO.value: [self.Status.TODO, self.Status.IN_PROGRESS],
                self.Status.IN_PROGRESS.value: [
                    self.Status.IN_PROGRESS,
                    self.Status.DONE,
                ],
                self.Status.DONE.value: [self.Status.DONE],
            }

            allowed_status = allowed_transitions[old_task.status]

            if self.status not in allowed_status:
                errors["status"] = f"Invalid status transition"

        if errors:
            raise ValidationError(errors)


# Create your models here.
