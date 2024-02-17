#Write a program that will allow
#the user to choose form the menu:
#Option 1: calculate the area of a circle
#Option 2: calculate the circumference
#Option 3: Exit the program

#import a module (import a library)
import math

#menu option
area_circle_choice = 1
circumference_choice = 2
rectangle_choice= 3
exit_program = 4

#define functions

#function fro area of the circle
def area_circle(radius):
    area = round(math.pi * radius**2, 3)
    return area

#function for circumference of the circle
def circumference(radius):
    circumference_circle = round(2 * math.pi * radius,3)
    return circumference_circle

#function for area and perimeter of a rectangle
def rectangle(length, width):

    perimeter=round(length*2+width*2, 3)
    area = round(length*width,3)
    print(f'The perimeter is: {perimeter} and the area is: {area}')




def show_menu():
    print('**** Welcome to Trigonometry ****')
    print('\t Menu')
    print('\t Select an option: ')
    print('\t 1. Area of a circle')
    print('\t 2. Circumeference of a circle')
    print('\t 3. Area and Perimeter of a Rectangle')
    print('\t 4. Exit the program')
    print()

def main():

    

    #since we are using a menu, we need
    #some repetion structure with control
    #best option: while loop

    #control variable
    option = 0
    

    while option != exit_program:

        #display the menu
        show_menu()

        option = int(input('Enter your choice: '))

        #option #1 => area of the circle
        if option == area_circle_choice:
            #area_returned = area_circle()
            radius = float(input('Enter the radius of the circle: '))
            print('The area of the circle is: ', area_circle(radius))
        elif option == circumference_choice:
            radius = float(input('Enter the radius of the circle: '))
            print('The circumference of the circle is: ', circumference(radius))
        elif option == rectangle_choice:
            length = float(input('Enter the length of the rectangle: '))
            width = float(input('Enter the width of the rectangle: '))
            rectangle(length,width)
           

        elif option == exit_program:
            print('Program is closing.')
        else:
            print('Option not available. Select another option.')

main()