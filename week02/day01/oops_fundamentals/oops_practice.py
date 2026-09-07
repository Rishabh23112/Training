"""Oops Fundamentals"""

from dataclasses import dataclass
from datetime import date
from typing import Any, Literal


class Person:
    """Person class for learning encapsulation , dunder methods"""

    species: str = "Homo Sapiens"  # class attribute

    def __init__(self) -> None:
        """constructor"""
        self.name = "Abc"  # instance attribute
        self.age = 21
        self.name1 = "Abc"
        self.__aadhar = 1234567890  # Private
        self.__phone = 111111

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """Bypasses __str__ and __repr__"""
        return f"My name is {self.name} and I am {self.age}."

    def __str__(self) -> Any:
        """Shows the human readable string."""
        return f"hello using __str__ to print :{self.name}"

    def __repr__(self) -> Any:
        """Show the data (mainly used for logs)"""
        return f"using __repr__ to print : {self.age}"

    def __eq__(self, value: object) -> bool:
        """For comparision, == implements the same."""
        if isinstance(value, Person):
            return value.name1 == self.name
        return False

    # Encapsulation

    def get_aadhar(self) -> int:
        """To access the private attribute. getter"""
        return self.__aadhar

    def set_aadhar(self) -> None:
        """To change the private attribute. setter"""
        self.__aadhar = 12345

    @property
    def phone(self) -> int:
        """same work using property decorator . getter"""
        return self.__phone

    @phone.setter
    def phone(self, new_number: int) -> None:
        """same work using property decorator . setter"""
        self.__phone = new_number


p = Person()
p1 = Person()
print(p)
print([p])
print(p())
print(p == p1)
print(p.set_aadhar())
print(p.get_aadhar())
print(p.phone)
NEW = 22222
p.phone = NEW
print(p.phone)


# Inheritance


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
