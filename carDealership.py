class Automobile:
    def __init__(self, make, year, price):
        self.auto_make=make
        self.auto_year=year
        self.auto_price=price

    
    def set_make(self, make):
        self.auto_make=make

    def set_year(self, year):
        self.auto_year=year

    def set_price(self, price):
        self.auto_price=price
    def get_make(self):
        return self.auto_make

    def get_year(self):
        return self.auto_year

    def get_price(self):
        return self.auto_price


class Car(Automobile):
    def __init__(self, make, year, price, doors):
        Automobile.__init__(self, make, year, price)
        self.auto_doors=doors
    def set_doors(self, doors):
        self.auto_doors=doors
    def get_doors(self):
        return self.auto_doors
 
    def display_info(self):
        print(f"{self.auto_make}\n Year: {self.auto_year}\n Price: {self.auto_price}\n Doors: {self.auto_doors}\n")


class Truck(Automobile):
    def __init__(self, make, year, price, drive_type):
        Automobile.__init__(self, make, year, price)
        self.auto_drive_type=drive_type
    def set_drive_type(self, drive_type):
        self.auto_drive_type=drive_type
    def get_drive_type(self):
        return self.auto_drive_type
    def display_info(self):
        print(f"{self.auto_make}\n Year: {self.auto_year}\n Price: {self.auto_price}\n Drivetrain: {self.auto_drive_type}\n")

class SUV(Automobile):
    def __init__(self, make, year, price, pass_cap):
        Automobile.__init__(self, make, year, price)
        self.auto_pass_cap=pass_cap
    def set_pass_cap(self, pass_cap):
        self.auto_pass_cap=pass_cap
    def get_pass_cap(self):
        return self.auto_pass_cap
    def display_info(self):
        print(f"{self.auto_make}\n Year: {self.auto_year}\n Price: {self.auto_price}\n Capacity: {self.auto_pass_cap}\n")

#Main menu
def show_menu():
    print('**** Welcome to the Car Dealership ****')
    print('\t Menu')
    print('\t Select an option: ')
    print('\t 1. Browse all cars')
    print('\t 2. Add/Remove a car')
    print('\t 3. Filter results')
    print('\t 4. Exit the program')
    print()
#menu option
display_all_cars = 1
edit_list = 2
filter_results= 3
exit_program = 4

def main():
        # Example usage:
    car1=Car('BMW', 2020, 20000, 4)
    car2=Car('Honda', 2005, 2000, 4)
    car3=Car('Ford', 2012, 5000, 2)
    truck1=Truck('Toyota', 2021, 15000, '4WD')
    truck2=Truck('Ford', 2010, 6000, 'FWD')
    truck3=Truck('Chevrolet', 2021, 15000, 'RWD')
    suv1=SUV('Tesla', 2024, 30000, 5)
    suv2=SUV('Nissan', 1995, 1500, 5)
    suv3=SUV('Hyundai', 2009, 6500, 5)
    

    # Creating a list to store Automobile objects
    automobiles = []

    # Adding Automobile objects to the list
    automobiles.append(car1)
    automobiles.append(car2)
    automobiles.append(car3)
    automobiles.append(suv1)
    automobiles.append(suv2)
    automobiles.append(suv3)
    automobiles.append(truck1)
    automobiles.append(truck2)
    automobiles.append(truck3)
    #since we are using a menu, we need
    #some repetion structure with control
    #best option: while loop

    #control variable
    option = 0
    

    while option != exit_program:

        #display the menu
        show_menu()

        option = int(input('Enter your choice: '))

       
        if option == display_all_cars:
            # Displaying everything as it is
            for auto in automobiles:
                auto.display_info()

        elif option == edit_list:
            answer=int(input("Press '1' to add, Press '2' to remove: "))
            if(answer==1):
                answer2=int(input("Press '1' to add a Car, Press '2' to add a Truck, or Press '3' to add a SUV: "))
                if(answer2==1):
                    make=input('Enter the manufacturer: ')
                    year=int(input('Enter the year: '))
                    price=int(input('Enter the price: $'))
                    doors=int(input('Enter the number of doors: '))

                    car=Car(make, year, price, doors)
                    automobiles.append(car)
                  
                    print(f"New car successfully added to the inventory.")

                elif(answer2==2):
                    make=input('Enter the manufacturer: ')
                    year=int(input('Enter the year: '))
                    price=int(input('Enter the price: $'))
                    drive_type=input('Enter the drive type(4WD, FWD, RWD): ')

                    truck=Truck(make, year, price, drive_type)
                    automobiles.append(truck)
                    
                    print(f"New truck successfully added to the inventory.")

                elif(answer2==3):
                    make=input('Enter the manufacturer: ')
                    year=int(input('Enter the year: '))
                    price=int(input('Enter the price: $'))
                    cap=int(input('Enter the passenger capacity: '))

                    suv=SUV(make, year, price, cap)
                    automobiles.append(suv)
                    
                    print(f"New SUV successfully added to the inventory.")
                    for auto in automobiles:
                        auto.display_info()
                else:
                    print("Option unavailable: you have been returned to the main menu. ")
                    
            elif(answer==2):
                if automobiles:
                    print("Current cars:")
                for i, auto in enumerate(automobiles):
                    print(f"{i + 1}. {auto.auto_year} {auto.auto_make} {auto.auto_price}")

                index = int(input("Enter the index of the car to remove: ")) - 1
                if 0 <= index < len(automobiles):
                    del automobiles[index]
                 
                    print("Car removed successfully!")
                    for auto in automobiles:
                        auto.display_info()
                else:
                    print("Invalid index!")
            else:
                print("Option unavailable: you have been returned to the main menu. ")
                        

                        
        elif option == filter_results:
            answer_about_filter=int(input("Press '1' to filter cars by year, Press '2' to filter cars by price: "))
            if(answer_about_filter==1):
                # Sorting automobiles by year
                order=int(input("Press '1' for oldest first, Press '2' for newest first: "))
                if(order==1):
                    automobiles.sort(key=lambda auto: auto.auto_year)
                    for auto in automobiles:
                        auto.display_info()
                        
                elif(order==2):
                    automobiles.sort(key=lambda auto: auto.auto_year, reverse=True)
                    for auto in automobiles:
                        auto.display_info()
                else:
                    print("Option unavailable: you have been returned to the main menu. ")

                
            elif(answer_about_filter==2):
                # Sorting automobiles by price
                order=int(input("Press '1' to view prices low to high, Press '2' to to view prices high to low: "))
                if(order==1):
                    automobiles.sort(key=lambda auto: auto.auto_price)
                    for auto in automobiles:
                        auto.display_info()
                elif(order==2):
                    automobiles.sort(key=lambda auto: auto.auto_price, reverse=True)
                    for auto in automobiles:
                        auto.display_info()
                else:
                    print("Option unavailable: you have been returned to the main menu. ")
            else:
                print("Option unavailable: you have been returned to the main menu")
                
    
            
           

        elif option == exit_program:
          
            
            print('Program closed successfully!')
        else:
            print('Option not available. Select another option.')





        


if __name__ == "__main__":
    main()
