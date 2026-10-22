# Python Project Management Tool

A command-line project management application built with Python. It allows users to manage projects, assign tasks, track task progress, and store information in a JSON database.

The project uses realistic Kenyan examples, including a tea farmers' cooperative, an M-Pesa shop, and a fresh produce delivery service.

## Features

- Add and list users.
- Create, view, search, and update projects.
- Assign projects to users.
- Create and list tasks.
- Assign tasks to users.
- Update task details and status.
- Mark tasks as completed.
- Store project data in a JSON file.
- Display information using Rich tables.
- Validate user input and test functionality with pytest.

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- argparse for command-line arguments
- Rich for formatted terminal output
- JSON for data storage
- pytest for automated testing

## Project Structure

```text
python_project_management_tool/
├── data/
│   └── database.json
├── models/
├── tests/
├── utils/
├── main.py
├── Pipfile
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/RozelineGitau/python_project_management_tool.git
```

### 2. Navigate to the project directory

```bash
cd python_project_management_tool
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

On Linux or macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the application from the project root directory.

### View available commands

```bash
python3 main.py --help
```

### Manage users

List users:

```bash
python3 main.py list-users
```

Add a user:

```bash
python3 main.py add-user --name "Wanjiku Mwangi" --email "wanjiku.mwangi@example.com"
```

### Manage projects

List projects:

```bash
python3 main.py list-projects
```

Search for projects:

```bash
python3 main.py search-projects --keyword Kericho
```

List projects associated with a user:

```bash
python3 main.py list-projects --user 1
```

### Manage tasks

List all tasks:

```bash
python3 main.py list-tasks
```

List tasks for a project:

```bash
python3 main.py list-tasks --project 1
```

Use the help command to see the required arguments and optional fields for creating projects, adding tasks, updating records, and completing tasks.

```bash
python3 main.py --help
```

## Sample Use Cases

The application includes sample data representing practical local projects:

- **Tea Farmers' Cooperative:** Record farmer information, track tea deliveries, and prepare payment reports.
- **M-Pesa Shop:** Track daily sales, cash transactions, and stock levels.
- **Fresh Produce Delivery Service:** Manage orders, coordinate deliveries, and update customer records.

The sample names and email addresses are fictional and intended for demonstration.

## Data Storage

Project information is stored in `data/database.json`. The application uses JSON to save and retrieve user, project, and task records.

## Running Tests

Run the automated tests from the project root:

#
pytest -q


The current local test run passed all 7 tests.

## Future Improvements

- Generate project and task summary reports.
- Add deadline reminders.
- Improve search and filtering options.
- Expand automated test coverage.
- Add CSV export functionality.
- Develop a graphical or web-based interface.

## Author

Rozeline Gitau
