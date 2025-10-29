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
        for i, item in enumerate(tasks, 1):
            if isinstance(item, dict):
                status = "✅" if item.get("done") else "⬜"
                print(f"{i}. {status} {item.get('title')}")
            else:
                print(f"{i}. ⬜ {item}")

def todo_app():
    print("Welcome to To-Do List Manager ✅")
    while True:
        try:
            print("\n1. Add Task\n2. View Tasks\n3. Toggle Done\n4. Remove Task\n5. Exit")
            choice = input("Enter choice: ").strip()

            if choice == '1':
                title = input("Enter new task: ").strip()
                if title:
                    tasks.append({"title": title, "done": False})
                    save_tasks(tasks)
                    print("Task added!")
                else:
                    print("Task title cannot be empty.")
            elif choice == '2':
                show_tasks()
            elif choice == '3':
                show_tasks()
                if not tasks:
                    continue
                try:
                    num = int(input("Enter task number to toggle: "))
                except ValueError:
                    print("Invalid number.")
                    continue
                if 1 <= num <= len(tasks):
                    if isinstance(tasks[num - 1], dict):
                        tasks[num - 1]["done"] = not tasks[num - 1]["done"]
                    else:
                        # Convert old format to new format
                        tasks[num - 1] = {"title": tasks[num - 1], "done": True}
                    save_tasks(tasks)
                    print("Task updated!")
                else:
                    print("Invalid task number.")
            elif choice == '4':
                show_tasks()
                if not tasks:
                    continue
                try:
                    num = int(input("Enter task number to remove: "))
                except ValueError:
                    print("Invalid number.")
                    continue
                if 1 <= num <= len(tasks):
                    tasks.pop(num - 1)
                    save_tasks(tasks)
                    print("Task removed!")
                else:
                    print("Invalid task number.")
            elif choice == '5':
                print("Goodbye 👋")
                break
            else:
                print("Invalid choice!")
        except KeyboardInterrupt:
            print("\nGoodbye 👋")
            break

todo_app()
