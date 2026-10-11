class Task:
    """Represents a task belonging to a project."""

    _id_counter = 1
    VALID_STATUSES = {"pending", "in-progress", "completed"}

    def __init__(
        self,
        title,
        status="pending",
        assigned_to=None,
        project_id=None,
        task_id=None,
    ):
        self.title = title.strip()
        if not self.title:
            raise ValueError("Task title cannot be empty.")

        self.status = status
        self.assigned_to = assigned_to
        self.project_id = int(project_id) if project_id is not None else None

        if task_id is None:
            self.id = Task._id_counter
            Task._id_counter += 1
        else:
            self.id = int(task_id)
            Task._id_counter = max(Task._id_counter, self.id + 1)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        value = value.strip().lower()
        if value not in self.VALID_STATUSES:
            raise ValueError(
                "Status must be pending, in-progress, or completed."
            )
        self._status = value

    def complete(self):
        """Mark the task as completed."""
        self.status = "completed"

    def update(self, title=None, status=None, assigned_to=None):
        """Update the task's editable fields."""
        if title is not None:
            title = title.strip()
            if not title:
                raise ValueError("Task title cannot be empty.")
            self.title = title
        if status is not None:
            self.status = status
        if assigned_to is not None:
            self.assigned_to = assigned_to

    def to_dict(self):
        """Convert the task to JSON-compatible data."""
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to,
            "project_id": self.project_id,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Task object from a dictionary."""
        return cls(
            data["title"],
            data.get("status", "pending"),
            data.get("assigned_to"),
            data.get("project_id"),
            data["id"],
        )

    @classmethod
    def get_all(cls, data):
        """Create Task objects from stored task dictionaries."""
        return [cls.from_dict(item) for item in data.get("tasks", [])]

    def __repr__(self):
        return f"Task(id={self.id}, title={self.title!r}, status={self.status!r})"

    def __str__(self):
        return f"{self.id}: {self.title} [{self.status}]"
