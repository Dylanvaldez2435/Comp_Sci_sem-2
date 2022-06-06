x = int(input("Please enter line length: "))
y = str(input("Do you want a horizontal or vertical Line? "))

if y == "h":
    for i in range(0,x):
        print("P")
elif y == "v":
    for i in range(0,x):
        print("P", end="")

else:
    print("Please input a valid character")