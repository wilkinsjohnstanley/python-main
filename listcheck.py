list = [420, 69, 666]
check = int(input("Guess the number I'm thinking of!: "))

if(check not in list):
    print("not found")
else:
    print("it's there")