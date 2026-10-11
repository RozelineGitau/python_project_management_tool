class Project:
    """Represents a project owned by a user."""

    _id_counter = 1

    def __init__(
        self,
        title,
        description,
        due_date,
        user_id,
        project_id=None,
        task_ids=None,
    ):
        self.title = title.strip()
        self.description = description.strip()
        self.due_date = due_date.strip()
        self.user_id = int(user_id)

        if not self.title:
            raise ValueError("Project title cannot be empty.")

        if project_id is None:
            self.id = Project._id_counter
            Project._id_counter += 1
        else:
            self.id = int(project_id)
            Project._id_counter = max(Project._id_counter, self.id + 1)

        self.task_ids = task_ids or []

    def add_task(self, task_id):
        """Add a task ID to this project."""
        if task_id not in self.task_ids:
            self.task_ids.append(task_id)

    def update(self, title=None, description=None, due_date=None):
        """Update the project's editable fields."""
        if title is not None:
            title = title.strip()
            if not title:
                raise ValueError("Project title cannot be empty.")
            self.title = title
        if description is not None:
            self.description = description.strip()
        if due_date is not None:
            self.due_date = due_date.strip()

    def to_dict(self):
        """Convert the project to JSON-compatible data."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "user_id": self.user_id,
            "task_ids": self.task_ids,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Project object from a dictionary."""
        return cls(
            data["title"],
            data.get("description", ""),
            data.get("due_date", ""),
            data["user_id"],
            data["id"],
            data.get("task_ids", []),
        )

    @classmethod
    def get_all(cls, data):
        """Create Project objects from stored project dictionaries."""
        return [cls.from_dict(item) for item in data.get("projects", [])]

    def __repr__(self):
        return f"Project(id={self.id}, title={self.title!r})"

    def __str__(self):
        return f"{self.id}: {self.title} (Due: {self.due_date or 'No date'})"
