def square(num) :
    sum = 0
    for i in range (1, num+1) :
        sum= sum + (i * i)
    return sum
num = 6
print("Sum of square is:", square(num))
