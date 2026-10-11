import json
from pathlib import Path


DEFAULT_DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "database.json"


def empty_data():
    """Return the empty database structure."""
    return {"users": [], "projects": [], "tasks": []}


def load_data(file_path=DEFAULT_DATA_FILE):
    """Load JSON data and handle missing or malformed files."""
    path = Path(file_path)

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            return empty_data()

        data.setdefault("users", [])
        data.setdefault("projects", [])
        data.setdefault("tasks", [])
        return data

    except FileNotFoundError:
        return empty_data()
    except (json.JSONDecodeError, OSError):
        return empty_data()


def save_data(data, file_path=DEFAULT_DATA_FILE):
    """Save application data to a JSON file."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
