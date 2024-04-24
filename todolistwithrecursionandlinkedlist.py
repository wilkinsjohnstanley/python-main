class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class TodoList:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_task = Node(task)
        if not self.head:
            self.head = new_task
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_task
        print(f"Task '{task}' added successfully.")

    def remove_task(self, task):
        current = self.head
        prev = None
        while current:
            if current.data == task:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"Task '{task}' removed successfully.")
                return
            prev = current
            current = current.next
        print(f"Task '{task}' not found.")

    def view_tasks(self):
        current = self.head
        if not current:
            print("Your to-do list is empty.")
            return
        print("Your to-do list:")
        while current:
            print(current.data)
            current = current.next

    def recursive_sort(self, head):
        if not head or not head.next:
            return head
        mid = self.find_middle(head)
        left_head = head
        right_head = mid.next
        mid.next = None
        left_sorted = self.recursive_sort(left_head)
        right_sorted = self.recursive_sort(right_head)
        return self.merge(left_sorted, right_sorted)

    def find_middle(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        dummy = Node(0)
        current = dummy
        while left and right:
            if left.data < right.data:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        current.next = left or right
        return dummy.next

    def sort_tasks(self):
        if not self.head:
            print("Your to-do list is empty.")
            return
        self.head = self.recursive_sort(self.head)
        print("Tasks sorted successfully.")


def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Sort Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            todo_list.sort_tasks()
        elif choice == '5':
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
