print("this is a random joke generator! ")
one = "Did you hear they arrested the devil?.....Yeah, they got him on possession."
two = "Did you hear about the shepherd who drove his sheep through town?.....He was given a ticket for making a ewe turn."
three = "Scientists have recently discovered a food that greatly reduces sex drive?....It’s called wedding cake."
four = "What do you call a bear with no teeth?....A gummy bear."
five = "What do you call a steak that’s been knighted by the queen?...Sir Loin."
list1 = [one,two,three,four,five]
import random
x = (random.randrange(0,4))
print(list1[x])