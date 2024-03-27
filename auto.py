class Automobile:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")


class Car(Automobile):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors


class SUV(Automobile):
    def __init__(self, make, model, year, all_wheel_drive):
        super().__init__(make, model, year)
        self.all_wheel_drive = all_wheel_drive


class Truck(Automobile):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity


def main():
    # Example usage:
    car1 = Car("Toyota", "Corolla", 2020, 4)
    suv1 = SUV("Honda", "CR-V", 2021, True)
    truck1 = Truck("Ford", "F-150", 2019, "10,000 lbs")

    # Creating a list to store Automobile objects
    automobiles = []

    # Adding Automobile objects to the list
    automobiles.append(car1)
    automobiles.append(suv1)
    automobiles.append(truck1)

    # Displaying information about each automobile in the list
    for auto in automobiles:
        auto.display_info()


if __name__ == "__main__":
    main()
