#superclass
class Automobile:
    #init==initilize variables
    def __init__(self, make, year, price):
        self.auto_make=make
        self.auto_year=year
        self.auto_price=price
    #setters
    def set_make(self, make):
        self.auto_make=make

    def set_year(self, year):
        self.auto_year=year

    def set_price(self, price):
        self.auto_price=price

    #getters/accessors return stuff
    def get_make(self):
        return self.auto_make

    def get_year(self):
        return self.auto_year

    def get_price(self):
        return self.auto_price
    


class Car(Automobile):
    #first call init method.
    def __init__(self, make, year, price, doors):
        Automobile.__init__(self, make, year, price)
        self.auto_doors=doors

    def set_doors(self, doors):
        self.auto_doors=doors
    def get_doors(self):
        return self.auto_doors


class Truck(Automobile):
#subclass:Truck
    def __init__(self, make, year, price, drive_type):
        Automobile.__init__(self, make, year, price)
        self.auto_drive_type=drive_type
    def set_drive_type(self, drive_type):
        self.auto_drive_type=drive_type
    def get_drive_type(self):
        return self.auto_drive_type    


class SUV(Automobile):
#subclass: SUV
    def __init__(self, make, year, price, pass_cap):
        Automobile.__init__(self, make, year, price)
        self.auto_pass_cap=pass_cap
    def set_pass_cap(self, pass_cap):
        self.auto_pass_cap=pass_cap
    def get_pass_cap(self):
        return self.auto_pass_cap

#main program
def main():
    car1=Car('BMW', 2020, 20000, 4)
    truck1=Truck('Toyota', 2021, 15000, '4WD')
#user input
    make=input('Enter SUV manufacturer:')
    year=int(input('Enter SUV year: '))
    price=float(input('Enter SUV price: $'))
    cap=int(input('Enter SUV passenger capacity: '))

    suv1=SUV(make, year, price, cap)
    #print data
    print('\nCar Inventory\n')
    print('Make: ', car1.get_make())
    print('Year: ', car1.get_year())
    print('Doors:', car1.get_doors())

    print()

   
    print('Make: ', truck1.get_make())
    print('Year: ', truck1.get_year())
    print('Price:', truck1.get_price())
    print('Drivetrain:', truck1.get_drive_type())

    print()

    print('Make: ', truck1.get_make())
    print('Year: ', truck1.get_year())
    print('Price:', truck1.get_price())
    print('Passenger Capacity:', suv1.get_pass_cap())
main()

