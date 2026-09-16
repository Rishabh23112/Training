from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "todo", "Todo"
        IN_PROGRESS = "in-progress", "In-Progress"
        DONE = "done", "Done"

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.TODO
    )
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return str(self.title)


# Create your models here.
