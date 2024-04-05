import time 
import csv

class Organization:
    def __init__(self, index, org_id, name, website, country, description, founded, industry, number_of_employees):
        self.index = index
        self.org_id = org_id
        self.name = name.title()
        self.website = website.title()
        self.country = country.title()
        self.description = description.title()
        self.founded = founded
        self.industry = industry.title()
        self.number_of_employees = number_of_employees

    @classmethod
    def from_csv_line(cls, line: list) -> "Organization":
        index = line[0]
        org_id = line[1]
        name = line[2]
        website = line[3]
        country = line[4]
        description = line[5]
        try:
            founded = int(line[6])
        except ValueError:
            founded = None  # or some default value
        industry = line[7]
        number_of_employees = int(line[8])
        return cls(index, org_id, name, website, country, description, founded, industry, number_of_employees)
        
class Algorithm:
    def __init__(self, nameOfAlgorithm, timeComplexity, computationTime):
        self.nameOfAlgorithm=nameOfAlgorithm
        self.timeComplexity=timeComplexity
        self.computationTime=computationTime
        #display method for use by the leaderboard
    def display_info(self):
        print(f"{self.nameOfAlgorithm}\n Time complexity: {self.timeComplexity}\n Time needed to Compute: {self.computationTime}\n")




# Read data from CSV file
org_list = []
with open("organizations-100000.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        org_list.append(Organization.from_csv_line(row))

# start_timer = time.perf_counter()
# end_timer = time.perf_counter()
# print('Execution time: ', round(end_timer-start_timer, 5))

# Test how fast the algorithm is! Program
# Main menu is a list of algorithms like linear search, binary, etc. And it clearly check
# s the speed for how long it took. And stores the speeds and names of the algorithms in a table that you can choose to display to you from the main menu 

def show_algorithms():
    print('**** Choose one to test! ****')
    print('\t Menu')
    print('\t Select an option: ')
    print('\t 1. Constant Time Complexity')
    print('\t 2. Linear Time Complexity')
    print('\t 3. Logarithmic Time Complexity')
    print('\t 4. Polynomial Time Complexity')
    print('\t 5. Factorial Time Complexity')
    print('\t 6. Return to Main Menu')
    print()
#menu option for main menu
constant=1
linear=2
logarithmic=3
polynomial=4
factorial=5
returnToMain=6

def show_menu():
    print('**** Test how fast the algorithm is!  ****')
    print('Explanation: The algorithms will sort 100,000 companies by the number of employees they have.')
    print('The results will be added to the leader board after each test!')
    print('\t Menu')
    print('\t Select an option: ')
    print('\t 1. Display the algorithm leader board!')
    print('\t 2. Test an algorithm')
    print('\t 3. Exit the program')
    print()
#menu option for main menu
leaderBoard = 1
testAlg = 2
exit_program = 3

def main():


# Creating a list to store algorithm objects
    algorithms = []


    show_menu()
#control variable
    option = 0
    

    while option != exit_program:

        #display the menu
        show_menu()

        option = int(input('Enter your choice: '))

       
        if option == leaderBoard:
            for alg in algorithms:
                algorithms.sort(key=lambda alg: alg.computationTime, reverse=True)
                alg.display_info()
               
        elif option == testAlg:
            show_algorithms()
            testChoice = 0
'''
constant=1
linear=2
logarithmic=3
polynomial=4
factorial=5
returnToMain=6
'''

            while testChoice != returnToMain:
                if testChoice == 1:
                elif testChoice == 2:
                elif testChoice == 3:
                elif testChoice == 4:
                elif testChoice == 5:
                else:
                    print("Option unavailable: you have been returned to the main menu. ")

        elif option == exit_program:
            print('Program closed successfully!')
        else:
            print('Option not available. Select another option.')




main()