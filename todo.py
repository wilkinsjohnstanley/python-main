def show_menu():
    print("\nTodo List Menu:")
    print("1. Add task")
    print("2. Remove task")
    print("3. Show tasks")
    print("4. Exit")

def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added successfully!")

def remove_task(todo_list):
    if len(todo_list) == 0:
        print("No tasks to remove.")
        return
    print("Current tasks:")
    for index, task in enumerate(todo_list):
        print(f"{index + 1}. {task}")
    task_index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_index < len(todo_list):
        removed_task = todo_list.pop(task_index)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task number.")

def show_tasks(todo_list):
    if len(todo_list) == 0:
        print("No tasks.")
        return
    print("Tasks:")
    for index, task in enumerate(todo_list):
        print(f"{index + 1}. {task}")

def main():
    todo_list = []
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            remove_task(todo_list)
        elif choice == "3":
            show_tasks(todo_list)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")


main()
