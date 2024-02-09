'''
John Wilkins
Fundamentals of Computer Programming
Dr. Jose Martinez
Assignment 2 Program 2
February 8th, 2024


'''

#control variable
user_menu = 'y'
#while loop
while user_menu == 'y':


    totalTax=0
    for property in range(1, 4):
        propertyValue = int(input("Enter the property value: "))
        propertyTax = propertyValue*.0065
        print(f"The property tax is {propertyTax} for property #{property}")
        totalTax+=propertyTax
    print("The property tax to be collected for the all the entire list in question is: ", totalTax)
    user_menu = input('Do you want to calculate the property tax for a new list of lots?\n Enter y to continue, n to stop calculating property taxes: \n')