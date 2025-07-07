# Test Todo App

This repository contains a simple Todo web application built with Python's
built-in `http.server` module. The application script is `todo_app.py` and lives
in the repository root, so after cloning make sure you are on the `main` branch
or pull the latest changes to see it.

## Usage

1. Run the server:
   ```bash
   python3 todo_app.py
   ```
2. Open `http://localhost:8000/` in your browser.
3. Add a task with `http://localhost:8000/add?task=My%20task`.
4. View tasks at `http://localhost:8000/list`.
