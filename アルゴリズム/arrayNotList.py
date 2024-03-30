from array import *

#how to declare
#arrayName = array(typecode, [Initializers])
myArray = array('i', [10,20,30,40,50])
#traverse the array
for x in myArray:
    print(x)
#access a single element
print(myArray[0])
#insertion 60 at index 1, shifts the other elements right
myArray.insert(1, 60)
print(myArray)
#remove
myArray.remove(10)
print(myArray)
#search for an index
print(myArray.index(40)) #index of 40 turns out to be 3
#update
myArray[4] = 80
print(myArray)