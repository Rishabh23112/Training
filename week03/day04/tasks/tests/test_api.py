from datetime import date, timedelta

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


from typing import cast
from rest_framework.response import Response


from tasks.models import Task


class APITest(APITestCase):
    client: APIClient

    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@gmail.com",
            username="testuser",
            password="testpassword",
        )

        self.second_user = User.objects.create_user(
            email="testuser1@gmail.com",
            username="testuser1",
            password="testpassword",
        )

        self.user_task = Task.objects.create(owner=self.user, title="API Task test")

        self.second_user_task = Task.objects.create(
            owner=self.second_user, title="test title 1"
        )

    def test_api_list_requires_authentication(self):
        response = cast(Response,self.client.get(reverse("api_task-list")))
        self.assertIn(
            response.status_code,
            [
                status.HTTP_401_UNAUTHORIZED,
                status.HTTP_403_FORBIDDEN,
            ],
        )

    def test_api_list_returns_only_current_users_tasks(self):
        self.client.force_authenticate(user=self.user)

        response = cast(Response,self.client.get(reverse("api_task-list")))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = (
            response.data.get("results", response.data) or []
            if isinstance(response.data, dict)
            else response.data or []
        )
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "API Task test")

    def test_api_create_task_success(self):
        self.client.force_authenticate(user=self.user)

        response = cast(Response,self.client.post(
            reverse("api_task-list"),
            {
                "title": "API Created Task test",
                "description": "Created through API.",
                "status": Task.Status.TODO,
                "due_date": None,
            },
            format="json",
        ))

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        task = Task.objects.get(title="API Created Task test")
        self.assertEqual(task.owner, self.user)

    def test_api_create_task_without_title(self):
        self.client.force_authenticate(user=self.user)

        response = cast(Response,self.client.post(
            reverse("api_task-list"),
            {
                "title": "",
                "description": "Missing title.",
                "status": Task.Status.TODO,
                "due_date": None,
            },
            format="json",
        ))

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data or {})

    def test_api_due_date(self):
        self.client.force_authenticate(user=self.user)

        past_date = (date.today() - timedelta(days=1)).isoformat()

        response = cast(Response,self.client.post(
            reverse("api_task-list"),
            {
                "title": "Past Task",
                "description": "Invalid due date.",
                "status": Task.Status.TODO,
                "due_date": past_date,
            },
            format="json",
        ))

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("due_date", response.data or {})

    def test_user_cannot_access_other_users_task(self):
        self.client.force_authenticate(user=self.user)

        response = cast(Response,self.client.get(
            reverse(
                "api_task-detail",
                kwargs={"pk": self.second_user_task.pk},
            )
        ))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_access_own_task(self):
        self.client.force_authenticate(user=self.user)

        response = cast(Response,self.client.get(
            reverse(
                "api_task-detail",
                kwargs={"pk": self.user_task.pk},
            )
        ))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual((response.data or {})["title"], "API Task test")

    def test_api_delete_own_task(self):
        self.client.force_authenticate(user=self.user)

        response = cast(Response,self.client.delete(
            reverse(
                "api_task-detail",
                kwargs={"pk": self.user_task.pk},
            )
        ))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(pk=self.user_task.pk).exists())
