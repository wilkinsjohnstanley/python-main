from numpy import *

cars=["Toyota", "Honda", "Toyota", "Nissan", "Toyota"]
vehicles=[]
print(f"This is the original array: {cars}")
for items in cars:
    if items =="Toyota":
        vehicles.append(items)
        cars.remove(items)

print(f"This is the new one: {vehicles}")
print(f"This is the old one now: {cars}")
