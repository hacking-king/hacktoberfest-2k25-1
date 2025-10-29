import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "todo_data.json")

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except (json.JSONDecodeError, OSError):
        pass
    return []

def save_tasks(tasks):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2)
    except OSError:
        print("Warning: Failed to save tasks to disk.")

tasks = load_tasks()

def show_tasks():
    print("\n📋 To-Do List:")
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def todo_app():
    print("Welcome to To-Do List Manager ✅")
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            show_tasks()
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num-1)
                save_tasks(tasks)
                print("Task removed!")
        elif choice == '4':
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!")

todo_app()
