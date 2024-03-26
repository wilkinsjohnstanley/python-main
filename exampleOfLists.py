even_numbers = [2, 4, 6, 8, 10]
#item based traversal
for element in even_numbers:
    print(element, end=', ')
#range-based
for element in range(len(even_numbers)):
    print(even_numbers[element], end=', ')
    












#len is for length
print(len(even_numbers)) #returns 5

odd_numbers = [1, 3, 5, 7, 9]
#example of concatenation
new_list=even_numbers+odd_numbers
print(new_list)
#finding elements in a list
#look_for=int(input("What do you search for?"))
#if look_for in even_numbers:
if 2 in even_numbers:
    print("Found it!")
else:
    print("Uh oh")

#append adds to the end of the list
names = ['Bobby', 'Billy','Joe',"Tommy"]
print(f"The names are: {names}")
new_name = input('Enter a new name: ')
names.append(new_name)
print(f"New list: {names}")
name = input('Enter name to delete: ')
if name in names:
    index=names.index(name)
    del names[index]
print(f"Updated list: {names}")
answer=input('Do you want to sort?')
if answer=="yes":
    names.sort()
print(f"Your list: {names}")



