from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone

from tasks.models import Task


class Command(BaseCommand):
    help = "Create demo user and sample tasks"

    def handle(self, *args, **options):
        User = get_user_model()

        user, created = User.objects.get_or_create(
            username="demo",
            defaults={
                "is_staff": True,
                "is_superuser": True,
            },
        )

        if created:
            user.set_password("demo123")
            user.save()

            self.stdout.write(self.style.SUCCESS("Demo user created successfully."))
        else:
            self.stdout.write(self.style.WARNING("Demo user already exists."))

        Task.objects.all().delete()

        today = timezone.localdate()

        tasks = [
            {
                "title": "Learn Django",
                "description": "Learn Django daily.",
                "status": Task.Status.TODO,
                "due_date": today + timedelta(days=2),
            },
            {
                "title": "Review Documentation",
                "description": "Review project documentation.",
                "status": Task.Status.TODO,
                "due_date": today + timedelta(days=3),
            },
            {
                "title": "Fix Bug",
                "description": "Fix bugs",
                "status": Task.Status.IN_PROGRESS,
                "due_date": today + timedelta(days=4),
            },
            {
                "title": "Write Unit Tests",
                "description": "Add tests for task.",
                "status": Task.Status.IN_PROGRESS,
                "due_date": today + timedelta(days=5),
            },
            {
                "title": "Update README",
                "description": "Document project setup.",
                "status": Task.Status.DONE,
                "due_date": today + timedelta(days=6),
            },
            {
                "title": "Database schema Review",
                "description": "Review database schema.",
                "status": Task.Status.DONE,
                "due_date": today + timedelta(days=7),
            },
            {
                "title": "Prepare ",
                "description": "Prepare for .",
                "status": Task.Status.TODO,
                "due_date": today + timedelta(days=8),
            },
            {
                "title": "Code Review",
                "description": "Review refactor, pylint, black, isort.",
                "status": Task.Status.IN_PROGRESS,
                "due_date": today + timedelta(days=9),
            },
            {
                "title": " Application",
                "description": "Task app.",
                "status": Task.Status.TODO,
                "due_date": today + timedelta(days=10),
            },
            {
                "title": "Project Cleanup",
                "description": "Remove unused files and code.",
                "status": Task.Status.DONE,
                "due_date": today + timedelta(days=11),
            },
        ]

        Task.objects.bulk_create([Task(**task) for task in tasks])

        self.stdout.write(self.style.SUCCESS("10 sample tasks created successfully."))
