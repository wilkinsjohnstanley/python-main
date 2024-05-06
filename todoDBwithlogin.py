import sqlite3
import time
# class Person:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

# class Customer(Person):
#     def __init__(self, username, password):
#         super().__init__(username, password)
# Main Menu
def login_menu():
    print("\nLogin Menu:")
    print("1. Login")
    print("2. Register")

def show_menu():
    print("\nTo-do List Menu:")
    print("1. Add task")
    print("2. Remove task")
    print("3. Show tasks")
    print("4. Save list to database")
    print("5. Load list from database")
    print("6. Exit")
# Append a task to a list. Prompt the user and give feedback.
def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added successfully!")
    time.sleep(1)
# If no tasks to remove, tell the user.
# If there are tasks, give the user an enumerated list to select from.
# Remove the corresponding task and give feedback.
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
# Show the to-do list as an enumerated list.
def show_tasks(todo_list):
    if len(todo_list) == 0:
        print("No tasks to show.")
        time.sleep(1)
        return
    print("Tasks:")
    for index, task in enumerate(todo_list):
        print(f"{index + 1}. {task}")
    time.sleep(1)
# Save tasks to a database
def save_tasks(todo_list):
    if len(todo_list) == 0:
        print("No tasks to save.")
        time.sleep(1)
        return

    answer = input("Are you sure you want to save these tasks to the database? (Y/N): ")
    if answer.lower() == "y":
        dbname = input("Enter file name of database (must end with .db): ")

        try:
            conn = sqlite3.connect(dbname)
            cur = conn.cursor()

            cur.execute('''CREATE TABLE IF NOT EXISTS Todo (
                                TaskIndex INTEGER PRIMARY KEY NOT NULL,
                                Task TEXT)''')

            for index, task in enumerate(todo_list, 1):
                cur.execute('INSERT INTO Todo (TaskIndex, Task) VALUES (?, ?)', (index, task))

            conn.commit()
            print("Tasks saved to database successfully!")
        except sqlite3.Error as e:
            print("Error saving tasks to the database:", e)
        finally:
            if conn:
                conn.close()
    else:
        print("Tasks were not saved.")
#upload tasks from the database and add them to the current to do list
def load_tasks():
    dbname = input("Enter file name of database to load from (must end with .db): ")
    loaded_tasks = []
    try:
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()

        cur.execute('SELECT * FROM Todo')
        todo_list = cur.fetchall()
        if not todo_list:
            print("No tasks found in the database.")
        else:
            print("These tasks have been imported from the database:")
            for row in todo_list:
                print(row[1])  # Assuming Task is the second column
                loaded_tasks.append(row[1])
                time.sleep(1)
    except sqlite3.Error as e:
        print("Error loading tasks from the database:", e)
    finally:
        if conn:
            conn.close()
    return loaded_tasks

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
            save_tasks(todo_list)
        elif choice == "5":
            loaded_tasks = load_tasks()
            todo_list.extend(loaded_tasks)  # Append loaded tasks to the current list
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

main()
