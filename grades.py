grades=[]
average=0
size=int(input("How many grades do you have?"))
#get grades
for grade in range(size):
    grade=float(input("Enter a grade: "))
    grades.append(grade)
for grade in grades:
    average = round(average+grade/size, 2)
print(f'The average of all your grades is {average}')
print('The highest grade is ', max(grades))
print('The lowest grade is ', min(grades))


#high grade

#low grade

