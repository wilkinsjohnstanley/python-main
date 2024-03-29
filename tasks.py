import csv

class Task:
    def __init__(self, task_id, description, priority):
        self.task_id = task_id
        self.description = description
        self.priority = priority

def create_tasks_from_csv(file_path):
    tasks = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            task_id = int(row['Task ID'])
            description = row['Task Description']
            priority = row['Priority']
            task = Task(task_id, description, priority)
            tasks.append(task)
    return tasks

def main():
    file_path = 'tasks.csv'
    tasks = create_tasks_from_csv(file_path)
    for task in tasks:
        print(f"Task ID: {task.task_id}, Description: {task.description}, Priority: {task.priority}")


main()
