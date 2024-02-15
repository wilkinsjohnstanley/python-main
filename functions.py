import math
#menu
area_circle_choice=1
circumference_choice=2
exit_program=3
#define functions

#function for the area of a circle
def area_circle():
    radius = float(input('Enter the radius of the circle: '))
    area = math.pi*radius**2