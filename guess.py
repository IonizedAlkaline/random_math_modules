import random

number = random.randint(10, 20)

print("can you guess a number between 10 and 20")
while True:
    guess = int(input("enter a number: "))
    if number == guess:
        print("you won")
        break
    else:
        print("wrong")
