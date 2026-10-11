# Python Project Management CLI Tool

A beginner-friendly Python command-line application for managing users, projects, and tasks.

## Features

- Create and list users.
- Create, list, search, and update projects.
- Create, list, update, and complete tasks.
- Assign projects to users.
- Assign tasks to users.
- Persist data locally using JSON.
- Use `argparse` for CLI commands.
- Use `rich` for readable terminal output.
- Use classes, inheritance, properties, class attributes, and relationships.
- Include unit tests with pytest.

## Project Structure

```text
project-management-cli/
├── main.py
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── user.py
│   ├── project.py
│   └── task.py
├── utils/
│   ├── __init__.py
│   └── storage.py
├── data/
│   └── database.json
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   └── test_cli.py
├── requirements.txt
├── Pipfile
└── README.md
```

## Setup

Create and activate a virtual environment:

```bash
python -m venv venv
```

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the CLI

Show help:

```bash
python main.py --help
```

### Add a user

```bash
python main.py add-user --name "Alex" --email "alex@example.com"
```

### List users

```bash
python main.py list-users
```

### Add a project

```bash
python main.py add-project --user "Alex" --title "CLI Tool" --description "Build a project tracker" --due-date "2026-12-01"
```

### List projects

```bash
python main.py list-projects
```

### List projects for one user

```bash
python main.py list-projects --user "Alex"
```

### Search projects

```bash
python main.py search-projects --keyword "CLI"
```

### Add a task

```bash
python main.py add-task --project "CLI Tool" --title "Implement add-task" --assigned-to "Alex"
```

### List tasks

```bash
python main.py list-tasks
```

### Complete a task

```bash
python main.py complete-task --task "Implement add-task"
```

### Update a project

```bash
python main.py update-project --project "CLI Tool" --description "Updated description"
```

### Update a task

```bash
python main.py update-task --task "Implement add-task" --status "in-progress"
```

## Run Tests

```bash
pytest
```

## Persistence

Application data is stored in:

```text
data/database.json
```

The application handles missing or malformed JSON files without crashing.

## Known Issues

- User and project names are used as simple CLI lookup keys.
- This is a local learning project and does not include authentication.
- Data is stored in one local JSON file.
