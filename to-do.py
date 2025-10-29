tasks = []

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
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            show_tasks()
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num-1)
                print("Task removed!")
        elif choice == '4':
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!")

todo_app()
