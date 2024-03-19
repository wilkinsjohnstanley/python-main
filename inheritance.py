#superclass
class Automobile:
    #init==initilize variables
    def __init__(self, make, year, price):
        self.auto_make=make
        self.auto_year=year
        self.auto_price=price






class Car(Automobile):
    Automobile.__init(self, make, year, price)
    self.auto_drive_type=drive_type

    def set_drive_type(self, drive_type):
        self.auto_drive_type=drive_type
    def get_drive_type(self):
        return self.auto_drive_type
#subclass: SUV
    def __init__(self, make, year, price, pass_cap):
        Automobile.__init__(self,make,year,price)
        self.auto_pass_cap
