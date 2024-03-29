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

# Print organization details
for org in org_list:
    print(
        f"Index: {org.index}, Name: {org.name}, Founded: {org.founded}, Number of Employees: {org.number_of_employees}"
    )
