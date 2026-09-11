from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ("TODO", "To-do"),
        ("IN_PROGRESS", "In-progress "),
        ("DONE", "Done"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="TODO")
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)


# Create your models here.
