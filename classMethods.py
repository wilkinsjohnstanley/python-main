class Rectangle:
    #function inside of a class is a method
    #every class has a function that sets it up
    #an init sets up the object when you create it
    #the parameter is a placeholder for the object name
    #for example: def __init__(robert)
    #besides self, the first parameter, and other params
    def __init__(self, color, length, width):
    #python uses "self" instead of "this" keyword
        self.color=color
        self.length=length
        self.width=width

#creating the object
robert=Rectangle('red', 2, 4)
print(f"Robert is {robert.color}")
#a new object that is also a rectangle
richard=Rectangle('blue', 1, 8)
print(f"Richard is {richard.color}")
