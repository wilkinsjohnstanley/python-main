'''
Using lists in Python can enhance the functionality 
of your program by allowing you to store 
and manipulate collections of objects more efficiently. 

Instead of handling each object separately, 
we utilize a list called automobiles to store them.

Using a list allows us to iterate over it 
and perform operations on each Automobile object efficiently. 
'''
#superclass
class Automobile:
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
    #display information
    def display_info(self):
        print(f"{self.year} {self.make} {self.price}")    
    
    

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

#Objects to be added to the list
    car1=Car('BMW', 2020, 20000, 4)
    car2=Car('Honda', 2005, 2000, 4)
    car3=Car('Ford', 2012, 5000, 2)
    truck1=Truck('Toyota', 2021, 15000, '4WD')
    truck2=Truck('Ford', 2010, 6000, 'FWD')
    truck3=Truck('Chevrolet', 2021, 15000, 'RWD')
    suv2=SUV('Nissan', 1995, 1500, 5)
    suv3=SUV('Hyundai', 2009, 6500, 5)
#automobiles list
    automobiles = [] 
# Adding Automobile objects to the list
    automobiles.append(car1)
    automobiles.append(car2)
    automobiles.append(car3)
    automobiles.append(truck1)
    automobiles.append(truck2)
    automobiles.append(truck3)
    #automobiles.append(suv1)
    automobiles.append(suv2)
    automobiles.append(suv3)

# Displaying information about each automobile in the list
for auto in automobiles:
    auto.display_info()


#user input
    # make=input('Enter SUV manufacturer:')
    # year=int(input('Enter SUV year: '))
    # price=float(input('Enter SUV price: $'))
    # cap=int(input('Enter SUV passenger capacity: '))

    # suv1=SUV(make, year, price, cap)
    # automobiles.append(suv1)


    #print data
    # print('\nCar automobiles\n')
    # print('The car:')
    # print('Make: ', car1.get_make())
    # print('Year: ', car1.get_year())
    # print('Doors:', car1.get_doors())

    # print()

    # print('The truck: ')
    # print('Make: ', truck1.get_make())
    # print('Year: ', truck1.get_year())
    # print('Price:', truck1.get_price())
    # print('Drivetrain:', truck1.get_drive_type())

    # print()
    # print('The SUV: ')
    # print('Make: ', suv1.get_make())
    # print('Year: ', suv1.get_year())
    # print('Price:', suv1.get_price())
    # print('Passenger Capacity:', suv1.get_pass_cap())
if __name__ == "__main__":
    main()

