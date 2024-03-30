dict = {'Name': 'John', 'Age': 28, 'Money': 25000}
print(f"dict['Name'] {dict['Name']}")
#delete
# del dict['Money']  #remove entry with key'Money'
# dict.clear()       #remove all entries in dict
# del dict           #delete entire dictionary

#update
dict['Money']=50000
print(f"dict['Money'] {dict['Money']}")

myDictionary = {'Array': [1, 2, 3, 4, 5, 6], 'Tuple': (1, 2, 3, 4, 5, 6), 'Integer': 100000}
for i in myDictionary:
    print(f"i is {i}, key is {myDictionary[i]}")
