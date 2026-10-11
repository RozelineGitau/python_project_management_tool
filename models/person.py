class Person:
    """Base class for people in the project tracker."""

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        value = value.strip()
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        value = value.strip()
        if "@" not in value or "." not in value:
            raise ValueError("Please enter a valid email address.")
        self._email = value

    def __str__(self):
        return f"{self.name} <{self.email}>"
