import time 
import csv
import threading
import random

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
        self.nameOfAlgorithm = nameOfAlgorithm
        self.timeComplexity = timeComplexity
        self.computationTime = computationTime

    # Display method for use by the leaderboard
    def display_info(self):
        print(f"{self.nameOfAlgorithm}\n Time complexity: {self.timeComplexity}\n Time needed to Compute: {self.computationTime}\n")
# Define timeComplexity globally
# timeComplexity = ""
# Counting Sort
def counting_sort(arr, stop_event):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    sorted_arr = []
    timeComplexity = "Linear"  # Define timeComplexity locally

    for num in arr:
        count[num] += 1

    for i in range(max_val + 1):
        if stop_event.is_set():
            return  # If stop event is set, return without completing the sort
        if count[i] > 0:
            sorted_arr.extend([i] * count[i])

    return sorted_arr

# Merge Sort
def merge_sort(arr, stop_event):
    timeComplexity = "Logarithmic"  # Define timeComplexity locally


    n = len(arr)
    width = 1
    while width < n:
        left = 0
        while left < n:
            mid = left + width
            right = min(left + 2 * width, n)
            if mid < right:
                arr[left:right] = merge_sort(arr[left:mid], arr[mid:right])
            left += 2 * width
        width *= 2

    return arr




# Bubble Sort
def bubble_sort(arr, stop_event):
    timeComplexity = "Polynomial"  # Define timeComplexity locally
    if stop_event.is_set():
        return
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# Bogo Sort
def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
def bogo_sort(arr, stop_event):
    timeComplexity = "Factorial"  # Define timeComplexity locally
    while not is_sorted(arr):
        if stop_event.is_set():
            return
        random.shuffle(arr)
    return arr



# Read data from CSV file
org_list = []
with open("organizations-100000.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        org_list.append(Organization.from_csv_line(row))

# Test how fast the algorithm is!
def test_algorithm(sort_function, name):
    stop_event = threading.Event()
    stopwatch_thread = threading.Thread(target=stopwatch, args=(stop_event,))
    stopwatch_thread.start()
    start_time = time.perf_counter()
    sorted_org_list = sort_function([org.number_of_employees for org in org_list], stop_event)
    end_time = time.perf_counter()
    stop_event.set()  # Signal the stopwatch thread to stop
    computation_time = end_time - start_time
    print(f"{name} - Computation Time: {computation_time:.4f} seconds")
    return Algorithm(name, timeComplexity, computation_time)

# Stopwatch function
def stopwatch(stop_event):
    start_time = time.perf_counter()
    while not stop_event.is_set():
        current_time = time.perf_counter()
        elapsed_time = current_time - start_time
        print(f"\rElapsed Time: {elapsed_time:.2f} seconds", end="")
        time.sleep(0.1)

def main():
    # Create a list to store algorithm objects
    algorithms = []

    option = 0
    while option != 3:
        print('**** Test how fast the algorithm is!  ****')
        print('Explanation: The algorithms will sort 100,000 companies by the number of employees they have.')
        print('\t Menu')
        print('\t Select an option: ')
        print('\t 1. Display the algorithm leaderboard')
        print('\t 2. Test an algorithm')
        print('\t 3. Exit the program')

        option = int(input('Enter your choice: '))
        if option == 1:
            if algorithms:
                print("*************Algorithm Leader Board!!!*************")
                algorithms.sort(key=lambda alg: alg.computationTime)
                for alg in algorithms:
                    alg.display_info()
            else:
                print("No algorithms have been tested yet.")
                time.sleep(1)
        elif option == 2:
            print('**** Choose an algorithm to test! ****')
            print('\t 1. Counting Sort')
            print('\t 2. Merge Sort')
            print('\t 3. Bubble Sort')
            print('\t 4. Bogo Sort')
            test_choice = int(input('Enter your choice: '))

            if test_choice == 1:
                algorithms.append(test_algorithm(counting_sort, "Counting Sort"))
                time.sleep(3)
            elif test_choice == 2:
                algorithms.append(test_algorithm(merge_sort, "Merge Sort"))
                time.sleep(3)
            elif test_choice == 3:
                algorithms.append(test_algorithm(bubble_sort, "Bubble Sort"))
                time.sleep(3)
            elif test_choice == 4:
                algorithms.append(test_algorithm(bogo_sort, "Bogo Sort"))
                time.sleep(3)
            else:
                print("Invalid choice")
        elif option == 3:
            print('Program closed successfully!')
        else:
            print('Option not available. Select another option.')

if __name__ == "__main__":
    main()
