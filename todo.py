import time

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Setters
    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    # Getters
    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

class John(User):
    def __init__(self, username, password, loggedIn):
        super().__init__(username, password)
        self.loggedIn = loggedIn

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
    time.sleep(3)

def remove_task(todo_list):
    if len(todo_list) == 0:
        print("No tasks to remove.")
        time.sleep(3)
        return

    print("Current tasks:")
    for index, task in enumerate(todo_list):
        print(f"{index + 1}. {task}")

    task_index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_index < len(todo_list):
        removed_task = todo_list.pop(task_index)
        print(f"Task '{removed_task}' removed successfully!")
        time.sleep(3)
    else:
        print("Invalid task number.")
        time.sleep(3)

def show_tasks(todo_list):
    if len(todo_list) == 0:
        print("No tasks.")
        time.sleep(3)
        return

    print("Tasks:")
    for index, task in enumerate(todo_list):
        print(f"{index + 1}. {task}")
    time.sleep(3)

def main():
    loggedIn = False

    # Initialize John
    john = John("John", "abc123", False)

    while not loggedIn:
        name = input("Enter username: ")
        word = input("Enter password: ")

        if name == john.get_username() and word == john.get_password():
            loggedIn = True
        else:
            print("Forgot your password?")
            new_password = input("Enter your new password: ")
            john.set_password(new_password)
            print("Password changed successfully!")

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
            time.sleep(3)
            break
        else:
            print("Invalid choice. Please choose again.")
            time.sleep(3)

main()
