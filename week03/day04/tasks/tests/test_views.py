from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from tasks.models import Task


class TaskViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="1234567890")
        self.task = Task.objects.create(owner=self.user, title="TaskView test")

    def test_task_list_view_requires_login(self):
        response = self.client.get(reverse("task-list"))
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

    def test_task_list_view_authenticated(self):
        self.client.login(username="user", password="1234567890")
        response = self.client.get(reverse("task-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "TaskView test")
