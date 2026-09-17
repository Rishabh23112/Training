from datetime import date, timedelta

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from tasks.models import Task


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@gmail.com",
            username="testuser",
            password="testpassword",
        )

    def test_task_creation(self):
        task = Task.objects.create(
            owner=self.user,
            title="testTask",
            description="Test task description",
        )
        self.assertEqual(task.title, "testTask")
        self.assertEqual(task.owner, self.user)

    def test_default_status(self):
        task = Task.objects.create(owner=self.user, title="testStatus")
        self.assertEqual(task.status, Task.Status.TODO)

    def test_str(self):
        task = Task.objects.create(owner=self.user, title="django")
        self.assertEqual(str(task), "django")

    def test_due_date(self):
        task = Task.objects.create(
            owner=self.user,
            title="past date test",
            due_date=date.today() - timedelta(days=1),
        )
        with self.assertRaises(ValidationError):
            task.full_clean()
