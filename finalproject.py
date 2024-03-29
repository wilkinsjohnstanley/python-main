'''
Buddy says: Woof!
Whiskers says: Meow!
Enter your pet's name: Spots
Enter your pet's type (dog/cat): dog
Hello, Spots! You have a dog
Factorial of 5 is 120
Dictionary: {'name': 'John', 'age': 30, 'city': 'New York'}
'''

# Implementation of inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# User Input
def get_user_input():
    name = input("Enter your pet's name: ")
    animal_type = input("Enter your pet's type (dog/cat): ").lower()
    return name, animal_type

# Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Data structures
def demonstrate_data_structure():
    # Using a dictionary as an advanced data structure
    my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
    print("Dictionary:", my_dict)

if __name__ == "__main__":
    # Implementation of inheritance
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    print(dog.name, "says:", dog.speak())
    print(cat.name, "says:", cat.speak())

    # User Input
    name, animal_type = get_user_input()
    print("Hello,", name + "! You have a", animal_type)

    # Recursion
    num = 5
    print("Factorial of", num, "is", factorial(num))

    # Data structures
    demonstrate_data_structure()
