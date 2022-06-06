numItems = int(input("How many items? "))
total = 0
for i in range(0,numItems):
    item = input("whats the item? ")
    price = float(input("whats the price? "))
    print("thanks for buying " + item)
    total = total + price
print("your total is: " + str(total))


x = int(input("How many items are you purchasing? "))
y = input("What item are you purchasing? ")
z = input("how much is the item? ")
print("Thank you for purchasing " + y)
total = 0
for i in range(0,x):
    y = input("What item are you purchasing? ")
    z = input("how much is the item? ")
    print("Thank you for purchasing " + y)
    total = total + z
print("for " + x + " items, your total is: " + str(total)
print("Have a nice day!")

    

