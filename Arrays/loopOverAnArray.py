cars=["Toyota", "Honda", "Toyota", "Nissan", "Toyota"]
numberofToyotas=0
print(cars)
for items in cars:
    if items=="Toyota":
        numberofToyotas+=1
print(f"There are {numberofToyotas} Toyotas in inventory.")
        