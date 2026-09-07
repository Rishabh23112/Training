"""Task Manager"""

from dataclasses import dataclass
from datetime import date
from typing import Literal

StatusType = Literal["todo", "in_progress", "done"]


@dataclass
class Task:
    """Task manager"""

    title: str
    description: str
    status: StatusType = "todo"
    due_date: date | None = None

    def __post_init__(self) -> None:
        """what should happen after dataclass."""
        if not self.title.strip():
            raise ValueError("Title cannot be empty.")
        if self.due_date and self.due_date < date.today():
            raise ValueError("Due date cannot be in the past.")

    def transition_to(self, new_status: StatusType) -> None:
        """transition to in_progress, done , or todo"""
        valid_transitions: dict[StatusType, list[StatusType]] = {
            "todo": ["in_progress"],
            "in_progress": ["done", "todo"],
            "done": ["in_progress"],
        }
        if new_status not in valid_transitions[self.status]:
            raise ValueError(f"Invalid transition from {self.status} to {new_status}")
        self.status = new_status


class TaskManager:
    """Uses composition to manage a collection of tasks."""

    def __init__(self) -> None:
        """constructor"""
        self._tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        """function to add tasks"""
        self._tasks.append(task)

    def list_pending(self) -> list[Task]:
        """List of pending tasks"""
        return [t for t in self._tasks if t.status != "done"]
