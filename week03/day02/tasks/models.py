
"""Schema of the app"""

from django.db import models


class Task(models.Model):
    """Schema"""
    class Status(models.TextChoices):
        """Status"""
        TODO = "todo", "Todo"
        IN_PROGRESS = "in_progress", "In-Progress"
        DONE = "done", "Done"

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.TODO
    )
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Metadata"""
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return str(self.title)


# Create your models here.
