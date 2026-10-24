# To-Do List (CLI)

A command-line program for managing a list of tasks. Tasks are saved to a file, so they are still there the next time you run it.

## Features

- Add a new task
- Mark a task as completed
- Mark a task as cancelled
- Delete a task (with confirmation)
- Edit a task's text (with confirmation)
- View all tasks with their status
- See what percentage of your tasks are completed (cancelled tasks are not counted)
- Type `c` at any task prompt to go back to the menu without changing anything
- Invalid input shows a message instead of crashing

## Requirements

- Python 3.12 or newer
- No external libraries (only the built-in `json` module)

## How to run

1. Download or clone this repository.
2. Open a terminal in the `todo_list` folder.
3. Run:

```
python todo.py
```

## How to use

The program shows a menu. Type a number and press Enter:

| Option | What it does |
|---|---|
| 1 | Add a new task |
| 2 | Complete an existing task |
| 3 | Cancel an existing task |
| 4 | Delete an existing task |
| 5 | Edit an existing task |
| 6 | View all existing tasks |
| 7 | See your completion percentage |
| 0 | Quit |

Options 2 to 5 show your tasks first, then ask for a task number. Type `c` instead to cancel and return to the menu.

## How data is stored

Tasks are kept in a list of dictionaries, each with a `text` and a `status` (`pending`, `completed` or `cancelled`). The list is saved to `tasks.json` in the folder you run the program from. If the file does not exist, the program starts with an empty list and creates it on the first save.

## What I learned

- Functions, parameters and return values
- Lists and dictionaries, and how they combine
- Reading and writing JSON files
- Handling bad input with `try` / `except` and input checks
- Looping until valid input, and using `break` and `continue` correctly
- Using Git and GitHub for version control