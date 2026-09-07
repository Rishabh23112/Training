"""Class test cases"""

import unittest

from core.task import Task
from core.task_dataclass import TaskDataclass
from core.task_manager import TaskManager


class TestTask(unittest.TestCase):
    """Test task for empty title, task creation, status transition"""

    def test_task_creation(self):
        """task creattion test"""
        task = TaskDataclass("Test", "Description")
        self.assertEqual(task.status, "todo")

    def test_empty_title_raises_error(self):
        """empty title test"""
        with self.assertRaises(ValueError):
            Task("", "Description")

    def test_status_transition(self):
        """status transition test"""
        task = TaskDataclass("Test", "Desc")
        task.transition_to("in_progress")
        self.assertEqual(task.status, "in_progress")

    def test_invalid_transition_raises_error(self):
        """error handling for invalid transition"""
        task = TaskDataclass("Test", "Desc")
        with self.assertRaises(ValueError):
            task.transition_to("done")  # Can't go from todo to done directly


class TestTaskManager(unittest.TestCase):
    """tests for task manager"""

    def setUp(self):
        """adding tasks"""
        self.manager = TaskManager()
        self.task1 = Task("Task 1", "First task")
        self.task2 = Task("Task 2", "Second task")

    def test_add_task(self):
        """testing added task"""
        self.manager.add_task(self.task1)
        self.assertEqual(len(self.manager), 1)

    # Add more tests...


if __name__ == "__main__":
    unittest.main()
