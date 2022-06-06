import random

list1 = [3,6,1,7,2,5,9,4,8,10]

x = int(input("how many random numbers would you like? "))

for i in range (0,x):
    print(list1[random.randrange(10)])
    
