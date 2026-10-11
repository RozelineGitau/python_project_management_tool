from models.user import User
from models.project import Project
from models.task import Task


def test_user_can_add_project():
    user = User("Alex", "alex@example.com")
    user.add_project(1)

    assert 1 in user.project_ids


def test_project_can_add_task():
    project = Project("CLI Tool", "Test project", "2026-12-01", 1)
    project.add_task(1)

    assert 1 in project.task_ids


def test_task_can_be_completed():
    task = Task("Write tests")

    task.complete()

    assert task.status == "completed"


def test_task_rejects_invalid_status():
    try:
        Task("Bad task", status="unknown")
        assert False
    except ValueError:
        assert True


def test_user_properties():
    user = User("Alex", "alex@example.com")

    assert user.name == "Alex"
    assert user.email == "alex@example.com"
