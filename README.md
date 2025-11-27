# AI-Assisted Django TODO Application
This repository contains a simple TODO application built using Django. The development process was guided entirely by an AI assistant, demonstrating an iterative workflow from environment setup to test-driven debugging.

## 📋 Project Overview
The application allows users to:

- View a list of tasks.
- Create new tasks with due dates.
- Mark tasks as "Done" or "Undo" them.
- Delete tasks.

## 🛠️ Prerequisites
- Python 3.13+ (Official installer recommended over Microsoft Store version).
- Git (Optional, for version control).

## 🚀 Development Workflow (The Journey)
This project was built following a strict AI-Assisted workflow. Below is the step-by-step process used to generate the code, handle errors, and finalize the application.

### Phase 1: Environment & Installation
We encountered issues with the Windows Store version of Python. The fix involved a "Clean Slate" approach:

- **Cleanup**: Uninstalled broken Python versions and disabled "App Execution Aliases".
- **Installation**: Installed official Python from python.org (ensuring "Add to PATH" was checked).
- **Virtual Environment**: Created an isolated environment to manage dependencies.

```bash
# Commands used
python -m venv .venv
.venv\Scripts\activate
pip install django

# AI-Assisted Django TODO Application

This project is a simple Task Management application built using **Django**. It was developed as part of a homework assignment to demonstrate an **AI-Assisted Development Workflow**, going from environmental troubleshooting to a fully tested application.

## 📋 Project Overview

The application allows users to:
* **Create** new tasks with a title and due date.
* **Read** a list of pending and completed tasks.
* **Update** tasks by toggling their status (Resolved/Unresolved).
* **Delete** unwanted tasks.

## 🛠️ Prerequisites

* **Python 3.13+** (Official Installer)
    * *Note:* The Microsoft Store version of Python is **not** recommended due to permission issues with `pip`.
* **Django 5.x**

---

## 🚀 Development Workflow & Journey

This project was built iteratively using an AI assistant. Below is the step-by-step workflow, including the challenges faced and how they were resolved.

### Phase 1: Environment Setup & Troubleshooting
**Goal:** Install Django and set up a Virtual Environment.

1.  **Challenge:** Initial attempts to use `ensurepip` failed with `Access Denied` and `Unable to create process` errors.
2.  **Diagnosis:** The issue was caused by the Windows Store version of Python and "App Execution Aliases."
3.  **Solution:** * Disabled Python "App Execution Aliases" in Windows Settings.
    * Installed the official Python installer from python.org.
    * **Crucial Step:** Checked "Add Python to PATH" during installation.
4.  **Final Setup Commands:**
    ```powershell
    # Create virtual environment
    python -m venv .venv
    
    # Activate environment
    .venv\Scripts\activate
    
    # Install Django
    pip install django
    ```

### Phase 2: Project Scaffolding
**Goal:** Create the project structure.

1.  Created the project: `django-admin startproject todo_project`
2.  Created the app: `python manage.py startapp todo_app`
3.  **Configuration:** Registered `'todo_app'` in `settings.py` under `INSTALLED_APPS`.

### Phase 3: Data Modeling
**Goal:** Define the database structure.

* Modified `todo_app/models.py` to include `title`, `description`, `due_date`, and `is_resolved`.
* Ran migrations to initialize the SQLite database:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

### Phase 4: Logic & Routing (Iterative Debugging)
**Goal:** Implement Views and URLs.

* **Logic:** Implemented `todo_list`, `todo_create`, `delete`, and `toggle` views in `views.py`.
* **Challenge (NoReverseMatch):** When running tests early, we encountered `django.urls.exceptions.NoReverseMatch`.
* **Fix:** We created `todo_app/urls.py` and defined `name='todo_list'`, `name='todo_create'`, etc., so Django could find the routes.

### Phase 5: The Frontend (Templates)
**Goal:** Create the HTML interface.

* **Challenge (TemplateDoesNotExist):** The views tried to load HTML files that didn't exist yet.
* **Fix:**
    1.  Created a root `templates/` folder.
    2.  Registered this folder in `settings.py` under `TEMPLATES['DIRS']`.
    3.  Created `base.html` (layout) and `todo_list.html` (content).

### Phase 6: Testing
**Goal:** Verify functionality.

We used a Test-Driven approach where the AI wrote tests before the features were fully connected.
* **Command:** `python manage.py test`
* **Coverage:**
    * Model creation.
    * URL accessibility.
    * Form submission (POST requests).
    * Database updates (Delete/Toggle).

---

## 📂 Project Structure

```text
todo_project/
├── manage.py              # Django task runner
├── .venv/                 # Virtual Environment
├── templates/             # HTML Templates
│   ├── base.html          # Main layout (Bootstrap)
│   ├── todo_list.html     # Homepage
│   └── todo_create.html   # Form page
├── todo_app/              # App Logic
│   ├── models.py          # Database Schema
│   ├── views.py           # Logic/Controllers
│   ├── urls.py            # App Routing
│   └── tests.py           # Unit Tests
└── todo_project/          # Global Settings
    ├── settings.py
    └── urls.py

## 🏃‍♀️ How to Run the App

1.  **Activate the Environment:**
    ```powershell
    .venv\Scripts\activate
    ```

2.  **Run the Server:**
    ```powershell
    python manage.py runserver
    ```

3.  **Access the App:**
    Open your browser and navigate to: `http://127.0.0.1:8000/`

## 🧪 How to Run Tests

To run the automated test suite designed during the workflow:

```powershell
python manage.py test
