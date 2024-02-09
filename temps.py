
'''
John Wilkins
Fundamentals of Computer Programming
Dr. Jose Martinez
Assignment 2 Program 1
February 8th, 2024


'''
#control variable
user_menu = 'y'
#while loop
while user_menu == 'y':
    print("Temperature Table")
#ask the user to enter a starting and ending temp.
    start = int(input("Enter the starting temperature in Fahrenheits: "))
    end = int(input("Enter the ending temperature in Fahrenheit: "))
    '''
    Add one to the temp to account
    for the range of the loop
    '''
    end += 1 #counter or accumulator
    print('------------------------------------------------------------------')

    for fahrenheit in range (start, end): #fahrenheit is local, only works in this for loop. Fahrenheit is the counter.
        celsius = (fahrenheit - 32)*(5/9)
        if celsius<= 0:
             print(f"{fahrenheit:0.2f}*F --------->  {celsius:0.2f}*C --------> Freezing conditions. Take caution.")
        else:
            print(f"{fahrenheit:0.2f}*F--------->    {celsius:0.2f}*C")
    print('------------------------------------------------------------------')
    user_menu = input('Do you want to continue making temperature tables?\n Enter y to continue, n to stop: \n')