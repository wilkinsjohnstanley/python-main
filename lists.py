list1 = ['become programmer', 'live in Japan', 1995, 2025]
print("list1[0]:", list1[0])
print("list1[0:]: ", list1[0:]) #prints everything from zero onward
#change a value from A to B
list1[0] = 'become a software engineer'
print(f"The new list is now as follows : {list1}")
del list1[3]
print(f"del list1[3]: {list1}")

#length
len([1, 2, 3]) #result: 3
#concatenation
[1, 2, 3] + [4, 5, 6] #result: [1, 2, 3, 4, 5, 6]
#repetition
print(['Hi!']*4) #Result:['Hi!', 'Hi!', 'Hi!', 'Hi!']
#Membership
3 in [1, 2, 3] #Result: True
#iteration
for x in [1, 2, 3]: print x #1, 2, 3
