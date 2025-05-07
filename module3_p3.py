print("1. Add task")
print("2. Remove Task")
print("3. View Tasks")
print("4. Exit")

tasks = []

while True:
    try:
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            new_task = input("Add Task: ")
            tasks.append(new_task)
            print(f"Task '{new_task}' added!")
        elif choice == 2:
            if not tasks:
                print("No tasks to remove.")
            else:
                print("Current tasks:")
                for i, task in enumerate(tasks):
                    print(f"{i + 1}. {task}")
                try:
                    remove_index = int(input("Enter the number of the task to remove: ")) - 1
                    if 0 <= remove_index < len(tasks):
                        removed_task = tasks.pop(remove_index)
                        print(f"Task '{removed_task}' removed!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == 3:
            if not tasks:
                print("No tasks to display.")
            else:
                print("Current tasks:")
                for i, task in enumerate(tasks):
                    print(f"{i + 1}. {task}")
        elif choice == 4:
            print("Goodbye...")
            exit()
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input! Please enter a number.")