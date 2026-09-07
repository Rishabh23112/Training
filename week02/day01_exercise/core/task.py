"""Base task class."""


class Task:
    """Base task class with mark_complete function."""

    def __init__(self, title: str, description: str) -> None:

        if not title or not title.strip():
            raise ValueError("Title can't be empty.")
        self.title = title
        self.description = description
        self.completed = False

    def mark_complete(self) -> None:
        """Mark task as completed."""
        self.completed = True

    def __repr__(self) -> str:
        """Return developer-friendly representation."""
        status = "good" if self.completed else "bad"
        return f"{status} {self.title}"


class UrgentTask(Task):
    """Urgent task with deadline."""

    def __init__(
        self,
        title: str,
        description: str,
        deadline: str,
    ) -> None:
        super().__init__(title, description)
        self.deadline = deadline

    def is_overdue(self, current_date: str) -> bool:
        """Check if task is overdue."""
        return current_date > self.deadline

    def __repr__(self) -> str:
        """Return representation with deadline."""
        base = super().__repr__()
        return f"{base} (Due: {self.deadline})"
