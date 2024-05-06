import time
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    #setters
    def set_username(self, username):
        self.username=username
    def set_password(self, password):
        self.password=password
    #getters
    
    def get_make(self, username):
        return self.username
    def get_make(self, password):
        return self.password

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
    time.sleep(1)

def remove_task(todo_list):
    if len(todo_list) == 0:
        print("No tasks to remove.")
        time.sleep(1)

        return
    print("Current tasks:")
    for index, task in enumerate(todo_list):
        print(f"{index + 1}. {task}")
    task_index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_index < len(todo_list):
        removed_task = todo_list.pop(task_index)
        print(f"Task '{removed_task}' removed successfully!")
        time.sleep(1)

    else:
        print("Invalid task number.")
        time.sleep(1)


def show_tasks(todo_list):
    if len(todo_list) == 0:
        print("No tasks.")
        time.sleep(1)

        return
    print("Tasks:")
    for index, task in enumerate(todo_list):
        print(f"{index + 1}. {task}")
        time.sleep(1)

def main():

    while(loggedIn=True):
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
                time.sleep(1)

                break
            else:
                print("Invalid choice. Please choose again.")
                time.sleep(1)


main()
