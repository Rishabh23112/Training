"""Task with validation."""

from dataclasses import dataclass
from datetime import date
from typing import Literal

TaskStatus = Literal["todo", "in_progress", "done"]


@dataclass
class TaskDataclass:
    """Data validation"""

    title: str
    description: str
    status: TaskStatus = "todo"
    due_date: date | None = None

    def __post_init__(self) -> None:
        """Validate after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty")

        if self.due_date and self.due_date < date.today():
            raise ValueError("Due date cannot be in the past")

    def transition_to(self, new_status: TaskStatus) -> None:
        """Change status with validation."""
        valid_transitions: dict[TaskStatus, list[TaskStatus]] = {
            "todo": ["in_progress"],
            "in_progress": ["done", "todo"],
            "done": ["todo"],
        }

        if new_status not in valid_transitions[self.status]:
            raise ValueError(
                f"Cannot transition from " f"{self.status} to {new_status}"
            )

        self.status = new_status


# task = TaskDataclass("Write tests", "Unit tests for utils")
# task.transition_to("in_progress")
# print(task.status)  # "in_progress"

# try:
#     task.transition_to("todo")  # Valid: can go back
# except ValueError as e:
#     print(e)
