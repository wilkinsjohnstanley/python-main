import time


n = int(input("Enter the size : "))


for input in range(n):
   
    if input%3==0:
     time.sleep(1) #sleep for one second
     print("fizz") 
    if input%5==0:
      time.sleep(1) #sleep for one second
      print("buzz")
    if input%5==0 and input%3==0:
        time.sleep(1) #sleep for one second
        print("fizzbuzz")
    if input%5!=0 and input%3!=0:
         time.sleep(1) #sleep for one second
         print(input)
     

    