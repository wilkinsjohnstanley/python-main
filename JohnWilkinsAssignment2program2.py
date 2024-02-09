#control variable
user_menu = 'y'
#while loop
while user_menu == 'y':

    propertyList={}
  
    for property in range(3):
        propertyValue = int(input("Enter the property value: "))
        propertyTax = propertyValue*.0065
        print(f"The property tax is {propertyTax} for property#{property}")
    user_menu = input('Do you want to calculate the property tax for a new list of lots?\n Enter y to continue, n to stop calculating property taxes: \n')