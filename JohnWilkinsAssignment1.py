

F = float(input("Enter the future value that you want in the account: \n"))
r = float(input("Enter the annual interest rate: \n"))
n = float(input("Enter the number of years that you plan to let money sit in the account: \n"))

P = F / (1+r)**n

print("The amount you need to deposit today is: ", round(P, 2))

'''
Output:
Enter the future value that you want in the account:
10000
Enter the annual interest rate:
.01
Enter the number of years that you plan to let money sit in the account: 
10
The amount you need to deposit today is:  9052.87





'''