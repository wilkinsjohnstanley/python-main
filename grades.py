grades=[]
size=int(input("How many grades do you have?"))
#get grades
for grade in range(size):
    grade=int(input("Enter a grade: "))
    grades.append(grade)
for grade in grades:
    print(grade)


#tell the grades back 