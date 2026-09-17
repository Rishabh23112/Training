from django.test import TestCase

from tasks.forms import TaskForm
from tasks.models import Task


class TaskFormTest(TestCase):
    def test_empty_title(self):
        form = TaskForm(
            data={
                "title": "",
                "description": "Empty title description",
                "status": Task.Status.TODO,
                "due_date": "",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)

    def test_blank_space_title(self):
        form = TaskForm(
            data={
                "title": "   ",
                "description": "Empty title description",
                "status": Task.Status.TODO,
                "due_date": "",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)

    def test_valid_form(self):
        form = TaskForm(
            data={
                "title": "valid form",
                "description": "valid form test",
                "status": Task.Status.TODO,
                "due_date": "",
            }
        )
        self.assertTrue(form.is_valid())
