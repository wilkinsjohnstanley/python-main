cars=["Honda", "Nissan", "Toyota"]
print(cars)
for items in cars:
    if items=="Toyota":
        cars.remove(items)
        print("You have removed", items)
print(cars)