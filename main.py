import argparse

from rich.console import Console
from rich.table import Table

from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import load_data, save_data


console = Console()


def build_parser():
    """Build and return the argparse command-line parser."""
    parser = argparse.ArgumentParser(
        description="Manage users, projects, and tasks."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_user = subparsers.add_parser("add-user", help="Create a user.")
    add_user.add_argument("--name", required=True)
    add_user.add_argument("--email", required=True)

    subparsers.add_parser("list-users", help="List all users.")

    add_project = subparsers.add_parser("add-project", help="Create a project.")
    add_project.add_argument("--user", required=True, help="User name.")
    add_project.add_argument("--title", required=True)
    add_project.add_argument("--description", default="")
    add_project.add_argument("--due-date", default="")

    list_projects = subparsers.add_parser(
        "list-projects", help="List projects."
    )
    list_projects.add_argument("--user", help="Filter by user name.")

    search_projects = subparsers.add_parser(
        "search-projects", help="Search projects by title."
    )
    search_projects.add_argument("--keyword", required=True)

    update_project = subparsers.add_parser(
        "update-project", help="Update a project."
    )
    update_project.add_argument("--project", required=True)
    update_project.add_argument("--title")
    update_project.add_argument("--description")
    update_project.add_argument("--due-date")

    add_task = subparsers.add_parser("add-task", help="Create a task.")
    add_task.add_argument("--project", required=True, help="Project title.")
    add_task.add_argument("--title", required=True)
    add_task.add_argument("--assigned-to", help="User name.")

    list_tasks = subparsers.add_parser("list-tasks", help="List tasks.")
    list_tasks.add_argument("--project", help="Project title.")

    complete_task = subparsers.add_parser(
        "complete-task", help="Complete a task."
    )
    complete_task.add_argument("--task", required=True, help="Task title.")

    update_task = subparsers.add_parser("update-task", help="Update a task.")
    update_task.add_argument("--task", required=True)
    update_task.add_argument("--title")
    update_task.add_argument("--status")
    update_task.add_argument("--assigned-to")

    return parser


def find_user(users, name):
    """Find a user by name."""
    return next((user for user in users if user.name.lower() == name.lower()), None)


def find_project(projects, title):
    """Find a project by title."""
    return next(
        (project for project in projects if project.title.lower() == title.lower()),
        None,
    )


def find_task(tasks, title):
    """Find a task by title."""
    return next(
        (task for task in tasks if task.title.lower() == title.lower()),
        None,
    )


def save_objects(users, projects, tasks):
    """Save model objects to JSON storage."""
    save_data(
        {
            "users": [user.to_dict() for user in users],
            "projects": [project.to_dict() for project in projects],
            "tasks": [task.to_dict() for task in tasks],
        }
    )


def load_objects():
    """Load JSON data and convert it into model objects."""
    data = load_data()
    return (
        User.get_all(data),
        Project.get_all(data),
        Task.get_all(data),
    )


def add_user(args):
    """Create and save a new user."""
    users, projects, tasks = load_objects()

    if find_user(users, args.name):
        console.print("[red]A user with that name already exists.[/red]")
        return

    try:
        user = User(args.name, args.email)
        users.append(user)
        save_objects(users, projects, tasks)
        console.print(f"[green]User created:[/green] {user}")
    except ValueError as error:
        console.print(f"[red]{error}[/red]")


def list_users():
    """Display all users."""
    users, _, _ = load_objects()

    if not users:
        console.print("No users found.")
        return

    table = Table(title="Users")
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Email")

    for user in users:
        table.add_row(str(user.id), user.name, user.email)

    console.print(table)


def add_project(args):
    """Create and save a project for a user."""
    users, projects, tasks = load_objects()
    user = find_user(users, args.user)

    if not user:
        console.print("[red]User not found.[/red]")
        return

    if find_project(projects, args.title):
        console.print("[red]A project with that title already exists.[/red]")
        return

    try:
        project = Project(
            args.title,
            args.description,
            args.due_date,
            user.id,
        )
        projects.append(project)
        user.add_project(project.id)
        save_objects(users, projects, tasks)

        console.print(
            f"[green]Project created:[/green] {project} "
            f"for {user.name}"
        )
    except ValueError as error:
        console.print(f"[red]{error}[/red]")


def list_projects(args):
    """Display all projects, optionally filtered by user."""
    users, projects, _ = load_objects()

    if args.user:
        user = find_user(users, args.user)
        if not user:
            console.print("[red]User not found.[/red]")
            return
        projects = [project for project in projects if project.user_id == user.id]

    if not projects:
        console.print("No projects found.")
        return

    table = Table(title="Projects")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Owner")
    table.add_column("Due Date")

    for project in projects:
        owner = next(
            (user.name for user in users if user.id == project.user_id),
            "Unknown",
        )
        table.add_row(
            str(project.id),
            project.title,
            owner,
            project.due_date or "No date",
        )

    console.print(table)


def search_projects(args):
    """Search projects by a keyword in the title."""
    _, projects, _ = load_objects()
    keyword = args.keyword.lower()

    matches = [
        project for project in projects
        if keyword in project.title.lower()
    ]

    if not matches:
        console.print("No matching projects found.")
        return

    for project in matches:
        console.print(project)


def update_project(args):
    """Update a project and save the changes."""
    users, projects, tasks = load_objects()
    project = find_project(projects, args.project)

    if not project:
        console.print("[red]Project not found.[/red]")
        return

    try:
        project.update(args.title, args.description, args.due_date)
        save_objects(users, projects, tasks)
        console.print(f"[green]Project updated:[/green] {project}")
    except ValueError as error:
        console.print(f"[red]{error}[/red]")


def add_task(args):
    """Create and save a task inside a project."""
    users, projects, tasks = load_objects()
    project = find_project(projects, args.project)

    if not project:
        console.print("[red]Project not found.[/red]")
        return

    assigned_to = None

    if args.assigned_to:
        user = find_user(users, args.assigned_to)
        if not user:
            console.print("[red]Assigned user not found.[/red]")
            return
        assigned_to = user.id

    try:
        task = Task(
            args.title,
            assigned_to=assigned_to,
            project_id=project.id,
        )
        tasks.append(task)
        project.add_task(task.id)
        save_objects(users, projects, tasks)

        console.print(f"[green]Task created:[/green] {task}")
    except ValueError as error:
        console.print(f"[red]{error}[/red]")


def list_tasks(args):
    """Display tasks, optionally filtered by project."""
    users, projects, tasks = load_objects()

    if args.project:
        project = find_project(projects, args.project)
        if not project:
            console.print("[red]Project not found.[/red]")
            return
        tasks = [task for task in tasks if task.project_id == project.id]

    if not tasks:
        console.print("No tasks found.")
        return

    table = Table(title="Tasks")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Status")
    table.add_column("Assigned To")

    for task in tasks:
        assigned = next(
            (user.name for user in users if user.id == task.assigned_to),
            "Unassigned",
        )
        table.add_row(
            str(task.id),
            task.title,
            task.status,
            assigned,
        )

    console.print(table)


def complete_task(args):
    """Mark a task as completed."""
    users, projects, tasks = load_objects()
    task = find_task(tasks, args.task)

    if not task:
        console.print("[red]Task not found.[/red]")
        return

    task.complete()
    save_objects(users, projects, tasks)
    console.print(f"[green]Task completed:[/green] {task}")


def update_task(args):
    """Update a task and save the changes."""
    users, projects, tasks = load_objects()
    task = find_task(tasks, args.task)

    if not task:
        console.print("[red]Task not found.[/red]")
        return

    assigned_to = task.assigned_to

    if args.assigned_to:
        user = find_user(users, args.assigned_to)
        if not user:
            console.print("[red]Assigned user not found.[/red]")
            return
        assigned_to = user.id

    try:
        task.update(args.title, args.status, assigned_to)
        save_objects(users, projects, tasks)
        console.print(f"[green]Task updated:[/green] {task}")
    except ValueError as error:
        console.print(f"[red]{error}[/red]")


def main():
    """Run the CLI application."""
    parser = build_parser()
    args = parser.parse_args()

    commands = {
        "add-user": lambda: add_user(args),
        "list-users": list_users,
        "add-project": lambda: add_project(args),
        "list-projects": lambda: list_projects(args),
        "search-projects": lambda: search_projects(args),
        "update-project": lambda: update_project(args),
        "add-task": lambda: add_task(args),
        "list-tasks": lambda: list_tasks(args),
        "complete-task": lambda: complete_task(args),
        "update-task": lambda: update_task(args),
    }

    try:
        commands[args.command]()
    except Exception as error:
        console.print(f"[red]Error:[/red] {error}")


if __name__ == "__main__":
    main()
