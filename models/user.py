from .person import Person


class User(Person):
    """Represents a project tracker user."""

    _id_counter = 1

    def __init__(self, name, email, user_id=None, project_ids=None):
        super().__init__(name, email)

        if user_id is None:
            self.id = User._id_counter
            User._id_counter += 1
        else:
            self.id = int(user_id)
            User._id_counter = max(User._id_counter, self.id + 1)

        self.project_ids = project_ids or []

    def add_project(self, project_id):
        """Add a project ID to this user's project list."""
        if project_id not in self.project_ids:
            self.project_ids.append(project_id)

    def to_dict(self):
        """Convert the user to JSON-compatible data."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "project_ids": self.project_ids,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a User object from a dictionary."""
        return cls(
            data["name"],
            data["email"],
            data["id"],
            data.get("project_ids", []),
        )

    @classmethod
    def get_all(cls, data):
        """Create User objects from stored user dictionaries."""
        return [cls.from_dict(item) for item in data.get("users", [])]

    def __repr__(self):
        return f"User(id={self.id}, name={self.name!r})"

    def __str__(self):
        return f"{self.id}: {self.name} ({self.email})"
