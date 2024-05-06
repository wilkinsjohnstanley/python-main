import csv

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Customer(Person):
    def __init__(self, username, password):
        super().__init__(username, password)
    
    def order_product(self, inventory):
        print("Available Products:")
        for product in inventory:
            print(f"ID: {product['Product ID']}, Name: {product['Product Name']}, Quantity: {product['Quantity']}")
        product_id = input("Enter the product ID you want to order: ")
        quantity = int(input("Enter the quantity: "))
        for product in inventory:
            if product['Product ID'] == product_id:
                if int(product['Quantity']) >= quantity:
                    product['Quantity'] -= quantity
                    save_inventory(inventory)
                    print("Order placed successfully.")
                else:
                    print("Sorry, the quantity requested is not available.")
                return
        print("Product ID not found.")

class Employee(Person):
    def __init__(self, username, password):
        super().__init__(username, password)

    def view_orders(self, orders):
        if orders:
            print("Orders to be fulfilled:")
            for order in orders:
                print(f"Product ID: {order['Product ID']}, Quantity: {order['Quantity']}")
        else:
            print("No pending orders.")

    def mark_order_fulfilled(self, orders):
        product_id = input("Enter the product ID of the order to mark as fulfilled: ")
        for order in orders:
            if order['Product ID'] == product_id:
                orders.remove(order)
                print("Order marked as fulfilled.")
                return
        print("Product ID not found in orders.")

def load_inventory():
    try:
        with open('inventory.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            inventory = list(reader)
        return inventory
    except FileNotFoundError:
        print("Inventory file not found. Creating a new one...")
        with open('inventory.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Product Name", "Product ID", "Quantity"])
            writer.writeheader()
        return []

def save_inventory(inventory):
    with open('inventory.csv', 'w', newline='') as file:
        fieldnames = ["Product Name", "Product ID", "Quantity"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(inventory)

def load_orders():
    try:
        with open('orders.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            orders = list(reader)
        return orders
    except FileNotFoundError:
        print("Orders file not found. Creating a new one...")
        return []

def save_orders(orders):
    with open('orders.csv', 'w', newline='') as file:
        fieldnames = ["Product ID", "Quantity"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(orders)

def check_low_inventory(inventory):
    low_products = []
    for product in inventory:
        if int(product['Quantity']) <= 5:
            low_products.append(product['Product Name'])
    if low_products:
        print("Low inventory for the following products:", ", ".join(low_products))

def main():
    inventory = load_inventory()
    orders = load_orders()

    while True:
        print("\nMain Menu")
        print("1. Customer Menu")
        print("2. Employee Menu")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            customer_menu(inventory, orders)
        elif choice == '2':
            employee_menu(inventory, orders)
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def customer_menu(inventory, orders):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    customer = Customer(username, password)

    while True:
        print("\nCustomer Menu")
        print("1. Order Product")
        print("2. Return to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            customer.order_product(inventory)
        elif choice == '2':
            print("Returning to Main Menu.")
            break
        else:
            print("Invalid choice. Please try again.")

def employee_menu(inventory, orders):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    employee = Employee(username, password)

    while True:
        print("\nEmployee Menu")
        print("1. View Orders")
        print("2. Mark Order as Fulfilled")
        print("3. Check Low Inventory")
        print("4. Return to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            employee.view_orders(orders)
        elif choice == '2':
            employee.mark_order_fulfilled(orders)
            save_orders(orders)
        elif choice == '3':
            check_low_inventory(inventory)
        elif choice == '4':
            print("Returning to Main Menu.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
