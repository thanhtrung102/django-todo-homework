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
