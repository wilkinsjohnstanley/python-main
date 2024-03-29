import csv

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

def add_product(inventory):
    name = input("Enter product name: ")
    product_id = input("Enter product ID: ")
    quantity = int(input("Enter quantity: "))
    inventory.append({"Product Name": name, "Product ID": product_id, "Quantity": quantity})
    save_inventory(inventory)
    print("Product added successfully.")

def update_quantity(inventory):
    product_id = input("Enter product ID to update quantity: ")
    for product in inventory:
        if product["Product ID"] == product_id:
            new_quantity = int(input("Enter new quantity: "))
            product["Quantity"] = new_quantity
            save_inventory(inventory)
            print("Quantity updated successfully.")
            return
    print("Product ID not found.")

def generate_report(inventory):
    print("Current Inventory:")
    for product in inventory:
        print(f"Name: {product['Product Name']}, ID: {product['Product ID']}, Quantity: {product['Quantity']}")

def main():
    inventory = load_inventory()
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Quantity")
        print("3. Generate Report")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_product(inventory)
        elif choice == '2':
            update_quantity(inventory)
        elif choice == '3':
            generate_report(inventory)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
