#Calculate the gross pay for employees
#3 employees
num_employees=3
#Create a list to hold employee hours
#initilize the list in 0 -> initilizes the list with "num of employees" items.
hours = [0]*num_employees #positions created is the number of employees! Can change the variable at the top at any time
for index in range(num_employees):
    hours[index]=float(input(f'Enter the number of hours worked by the employee: {index+1}: '))
    
#hourly pay rate
pay_rate=float(input('Enter hourly pay rate: $'))
#display each employee's gross pay.
for index in range(num_employees):
    gross_pay=hours[index]*pay_rate
    # colon point two f formats it to two decimal places
    print(f'Gross pay for exmployee {index+1}: ${gross_pay:.2f}')