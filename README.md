# Todo CLI App (Python)

Simple command-line Todo application written in Python.  
The project was created to practice working with data structures, file handling, and building a small CLI tool.

---

## Features

- Add new tasks
- Edit existing tasks
- Delete tasks
- Mark tasks as completed
- Filter tasks (all / completed / pending)
- Search tasks by keyword
- Sort tasks by ID or priority
- Data persistence using JSON file

---

## How it works

Tasks are stored as a list of dictionaries in memory and saved into a JSON file (`tasks.json`).  
When the program starts, data is loaded from the file if it exists.

All changes are automatically saved after each operation.

---

## Project structure

- `main.py` – application flow and menu
- `tasks.py` – logic for task operations
- `storage.py` – loading and saving data to JSON

---

## How to run

```bash
python main.py
