import math
#menu
area_circle_choice=1
circumference_choice=2
exit_program=3
#define functions
#function for the area of a circle
def area_circle():
    radius = float(input('Enter the radius of the circle: '))
    # use ** like an ^, for example radius^2 or radius^3 
    area = math.pi*radius**2
    return area
#function circumference of a circle
def circumference():
    radius = float(input('Enter the radius of the circle: '))
    circumference_circle=2*math.pi*radius
    return circumference_circle
def show_menu():
    print('***Welcome to our Trig Program***')
    #backslash t adds a tab space
    print('\t Menu')
    print('\t Select an option: ')
    print('\t 1. Area of a circle')
    print('\t 2. Circumference of a circle')
    print('\t 3. Exit the program')
    #blank line
    print()

def main():
    
   

    #control variable
    option = 0
    

    while option !=exit_program:
        show_menu()
        option = int(input('Enter your choice: '))     
    #option #1 => area of the circle
        if option == area_circle_choice:
            print('The area of the circle is ', area_circle())
        if option == circumference_choice:
            print('The circumference of the circle is ', circumference())
        elif option == exit_program:
            print('The program is closed.') 
        #need an else as the end of the elif structure
        

        #call the main function
main()