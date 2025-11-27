Here is a comprehensive README documentation documenting the development lifecycle of this project.

AI-Assisted Django TODO Application
This repository contains a simple TODO application built using Django. The development process was guided entirely by an AI assistant, demonstrating an iterative workflow from environment setup to test-driven debugging.

📋 Project Overview
The application allows users to:

View a list of tasks.

Create new tasks with due dates.

Mark tasks as "Done" or "Undo" them.

Delete tasks.

🛠️ Prerequisites
Python 3.13+ (Official installer recommended over Microsoft Store version).

Git (Optional, for version control).

🚀 Development Workflow (The Journey)
This project was built following a strict AI-Assisted workflow. Below is the step-by-step process used to generate the code, handle errors, and finalize the application.

Shutterstock

Phase 1: Environment & Installation
We encountered issues with the Windows Store version of Python. The fix involved a "Clean Slate" approach:

Cleanup: Uninstalled broken Python versions and disabled "App Execution Aliases".

Installation: Installed official Python from python.org (ensuring "Add to PATH" was checked).

Virtual Environment: Created an isolated environment to manage dependencies.

PowerShell

# Commands used
python -m venv .venv
.venv\Scripts\activate
pip install django
Phase 2: Project Initialization
We generated the standard Django scaffolding using the CLI.

Created the project: django-admin startproject todo_project

Created the app: python manage.py startapp todo_app

Configuration: Registered 'todo_app' in settings.py under INSTALLED_APPS.

Phase 3: Data Modeling
We asked the AI to define a model representing a Task.

File: todo_app/models.py

Fields: title (Char), due_date (DateTime), is_resolved (Boolean).

Action: Ran makemigrations and migrate to create the SQLite database.

Phase 4: Logic & Routing (Iterative Debugging)
We implemented the business logic in views.py and connected them in urls.py.

Views: Implemented functions for todo_list, todo_create, todo_delete, and todo_toggle_status.

Routing:

Created todo_app/urls.py to map views to URL names.

Included these URLs in the main project's urls.py using include().

🐞 Challenge Encountered: NoReverseMatch

Issue: Tests failed because URL names (e.g., 'todo_list') were referenced before urls.py was fully configured.

Fix: We explicitly defined urlpatterns with name='...' parameters.

Phase 5: Templating (The Frontend)
We separated the HTML structure into a base layout and specific page content.

Configuration: Updated TEMPLATES['DIRS'] in settings.py to point to a root templates/ folder.

Files:

base.html: Contains Bootstrap CDN links and the main container.

todo_list.html: Loops through tasks and provides "Done" and "Delete" buttons.

Challenge Encountered: TemplateDoesNotExist. This was fixed by creating the missing HTML files in the correct directory.

Phase 6: Testing
We used Django's built-in unittest framework.

Shutterstock
Explore

Command: python manage.py test

Scenarios Covered:

Model integrity (checking fields).

Homepage HTTP 200 response.

Creation of tasks via POST request.

Deletion of tasks.

Toggling completion status.

📂 Project Structure
Plaintext

todo_project/
│
├── manage.py              # Django task runner
├── .venv/                 # Virtual Environment (Dependencies)
│
├── templates/             # HTML Files
│   ├── base.html          # Main layout (Bootstrap)
│   ├── todo_list.html     # Homepage
│   └── todo_create.html   # Add Task Form
│
├── todo_app/              # The Django App
│   ├── migrations/        # Database history
│   ├── admin.py           # Admin panel config
│   ├── models.py          # Database Schema (Todo Class)
│   ├── tests.py           # Unit Tests
│   ├── urls.py            # App-specific routing
│   └── views.py           # Business Logic
│
└── todo_project/          # Project Settings
    ├── settings.py        # Global config (Apps, Templates, DB)
    └── urls.py            # Global routing
🏃‍♀️ How to Run the App
Activate the Environment:

PowerShell

.venv\Scripts\activate
Apply Migrations (if not done):

PowerShell

python manage.py migrate
Run the Server:

PowerShell

python manage.py runserver
Access the App: Open your browser and go to http://127.0.0.1:8000/

🧪 How to Run Tests
To verify that all features work as expected:

PowerShell

python manage.py test
Expected Output: Ran 5 tests in 0.xxx s ... OK
