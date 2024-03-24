def swapPositions(cars, pos1, pos2):
    #popping both elements from the list
    first_element=cars.pop(pos1)
    second_element=cars.pop(pos2-1)
    #inserting in each others positions
    cars.insert(pos1, second_element)
    cars.insert(pos2, first_element)
    return cars

#driver function
cars=["Accord", "BMW", "Cayenne", "Dump truck", "Cayenne"]
pos1, pos2=3, 4
print(swapPositions(cars, pos1-1, pos2-1))