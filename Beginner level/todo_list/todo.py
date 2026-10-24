# To-Do List (CLI)
# A command-line program for managing a list of tasks.
# Each task is a dictionary holding its text and its status (pending, completed or cancelled).
# All tasks live in one list, and the list is saved to tasks.json so it survives between runs.
# A menu lets the user add, complete, cancel, delete, edit and view tasks, see a completion percentage and quit.
# Task numbers shown to the user start at 1, while the list itself starts counting at 0.
# Invalid input is handled with messages and does not crash the program.

import json


#step 2
def add_task(tasks, text):
    user_tasks = {"text": text,
        "status": "pending"}
    tasks.append(user_tasks)

def show_tasks(tasks):
    if not tasks:
        print("No tasks exist yet")
        return
    else:
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task['text']} - {task['status']}")

#phase 3
def save_task(tasks):

    file_path = "tasks.json"
    with open(file=file_path, mode="w") as file:
        json.dump(tasks, file)

def load_task(file_path):
    try:
        with open(file=file_path, mode="r") as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []

def ask_task_number(tasks):
    if not tasks:
        print("No tasks exist yet")
        return None
    number = input("Enter the task number or c to cancel: ").strip()
    if number.lower() == "c":
        return "cancel"
    try:
        number = int(number)
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")
        return None

    if number < 1 or number > len(tasks):
        print("That number is not on the list")
        return None
    else:
        return number - 1

def set_status(tasks,index,new_status):
    tasks[index]["status"] = new_status

def delete_task(tasks, index):
    tasks.pop(index)

def edit_task(tasks, index, new_text):
    tasks[index]["text"] = new_text

def completion_percentage(tasks):
    if not tasks:
        print("No tasks exist yet")
        return 0
    total = 0
    completed = 0

    for task in tasks:
        if task["status"]!= "cancelled":
            total += 1
        if task["status"] == "completed":
            completed += 1

    if total == 0:
        return 0
    else:
        return completed / total * 100



def main():
    tasks = load_task("tasks.json")

    while True:

        print("**********MENU OPTIONS**********")
        menu = {1: "Add a new task",
                2: "Complete an existing task",
                3: "Cancel an existing task",
                4: "Delete an existing task",
                5: "Edit an existing task",
                6: "View all existing tasks",
                7: "See how many percent of tasks you were able to complete today",
                0: "Quit"}


        for key, value in menu.items():
            print(f"{key}. {value}")

        print("********************************")

        user_input = input("Select one(0 to 7): ")


        if user_input == "1":
            while True:
                task = input("Please enter the name of the task(or c to cancel): ").strip()
                if task:
                    break
                print("Task name cannot be empty")

            if task.lower() == "c":
                print("Task not added")
                continue

            add_task(tasks, task)
            save_task(tasks)
            print("Task added!")

        elif user_input == "2":
            if not tasks:
                print("No tasks exist yet")
                continue
            while True:
                print("***********ALL TASKS************")
                show_tasks(tasks)
                print("********************************")

                index = ask_task_number(tasks)
                if index is not None:
                    break
            if index == "cancel":
                print("Cancelled")
                continue
            set_status(tasks,index,"completed")
            save_task(tasks)
            print("********************************")
            print(f"Task {index + 1} completed")


        elif user_input == "3":
            if not tasks:
                print("No tasks exist yet")
                continue
            while True:
                print("***********ALL TASKS************")
                show_tasks(tasks)
                print("********************************")

                index = ask_task_number(tasks)
                if index is not None:
                    break
            if index == "cancel":
                print("Cancelled")
                continue
            set_status(tasks,index,"cancelled")
            save_task(tasks)
            print("********************************")
            print(f"Task {index + 1} cancelled")

        elif user_input == "4":
            if not tasks:
                print("No tasks exist yet")
                continue
            while True:
                print("***********ALL TASKS************")
                show_tasks(tasks)
                print("********************************")

                index = ask_task_number(tasks)
                if index is not None:
                    break
            if index == "cancel":
                print("Cancelled")
                continue

            confirmation = input("Are you sure y/n?: ").strip()
            if confirmation.lower() == "y":
                delete_task(tasks, index)
                save_task(tasks)
                print("Task deleted")
            else:
                print("Task not deleted")
            print("********************************")

        elif user_input == "5":
            if not tasks:
                print("No tasks exist yet")
                continue
            while True:
                print("***********ALL TASKS************")
                show_tasks(tasks)
                print("********************************")

                index = ask_task_number(tasks)
                if index is not None:
                    break
            if index == "cancel":
                print("Cancelled")
                continue
            confirmation = input("Are you sure y/n?: ").strip()
            if confirmation.lower() == "y":
                print(f"Current task: {tasks[index]["text"]}")
                new_text = input("Enter the new task: ").strip()
                if not new_text:
                    print("Text can't be empty")
                    continue
                edit_task(tasks, index, new_text)
                save_task(tasks)
                print(f"Task {index + 1} edited")
            else:
                print(f"Task {index + 1} not edited")
            print("********************************")


        elif user_input == "6":
            print("***********ALL TASKS************")
            show_tasks(tasks)
            print("********************************")

        elif user_input == "7":
            percentage = round(completion_percentage(tasks))
            print(f"You completed {percentage}% of your tasks.")
        elif user_input == "0":
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()