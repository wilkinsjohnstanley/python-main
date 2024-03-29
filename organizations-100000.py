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

# Read data from CSV file
org_list = []
with open("organizations-100000.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        org_list.append(Organization.from_csv_line(row))

#Main menu
def show_menu():
    print('**** Welcome to the Organization ****')
    print('\t Menu')
    print('\t Select an option: ')
    print('\t 1. Browse all orgs')
    print('\t 2. Add/Remove an org')
    print('\t 3. Filter orgs by year/number of employees')
    print('\t 4. Exit the program')
    print()
#menu option
display_all_orgs = 1
edit_list = 2
filter_results= 3
exit_program = 4

def main():

    show_menu()
#control variable
    option = 0
    

    while option != exit_program:

        #display the menu
        show_menu()

        option = int(input('Enter your choice: '))

       
        if option == display_all_orgs:
            for org in org_list:
                print(
                    f"Business Number: {org.index}.\n Name: {org.name}\n Founded: {org.founded}\n Number of Employees: {org.number_of_employees}\n"
                )
      
        elif option == filter_results:
            answer_about_filter=int(input("Press '1' to filter orgs by year, Press '2' to filter orgs by price: "))
            if(answer_about_filter==1):
                # Sorting automobiles by year
                order=int(input("Press '1' for oldest first, Press '2' for newest first: "))
                if(order==1):
                    org_list.sort(key=lambda org: org.founded)
                    for org in org_list:
                        print(
                            f"Business Number: {org.index}.\n Name: {org.name}\n Founded: {org.founded}\n Number of Employees: {org.number_of_employees}\n"
                        )
                        
                elif(order==2):
                    org_list.sort(key=lambda org: org.founded, reverse=True)
                    for org in org_list:
                        print(
                            f"Business Number: {org.index}.\n Name: {org.name}\n Founded: {org.founded}\n Number of Employees: {org.number_of_employees}\n"
                        )
                else:
                    print("Option unavailable: you have been returned to the main menu. ")

                
            elif(answer_about_filter==2):
                # Sorting automobiles by price
                order=int(input("Press '1' to view prices low to high, Press '2' to to view prices high to low: "))
                if(order==1):
                    automobiles.sort(key=lambda auto: auto.auto_price)
                    for auto in automobiles:
                        auto.display_info()
                elif(order==2):
                    automobiles.sort(key=lambda auto: auto.auto_price, reverse=True)
                    for auto in automobiles:
                        auto.display_info()
                else:
                    print("Option unavailable: you have been returned to the main menu. ")
            else:
                print("Option unavailable: you have been returned to the main menu")
                
    
            
           

        elif option == exit_program:
          
            
            print('Program closed successfully!')
        else:
            print('Option not available. Select another option.')


   

main()

