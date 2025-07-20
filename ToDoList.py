# Simple To-Do List

tasks = []

while True:
    print("\n--- Simple To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        if not tasks:
            print("No tasks yet.")
        else:
            print("Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == '2':
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == '3':
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Enter a valid number.")

    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
