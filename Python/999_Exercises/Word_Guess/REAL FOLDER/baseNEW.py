list_words = []

with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        list_words.append(l)

num = random.randrange(12972)
answer = list_words[num]
print(answer)

for i in range(0,6):
    guess = input("Give me a word! ")
    if guess == answer:
        print("You guesssed it!")
        break
    else:
        for words in list_words:
            if guess == words:
                a = 1
        if a == 1
        print("Wrong word!")
        else:
            print("invalid entry, guess again!")
            w = w +1 
        a = 0
    
f.close()
