import random

while True:
    user_input = input("enter your choice: rock , paper or scissor: ")
    action = ["rock", "paper", "scissor"]
    computer_action = random.choice(action)
    if user_input == computer_action:
        print("its a tie")
    elif user_input == "rock":
        if computer_action == "scissor":
            print("you won")
        else:
            print("you lost")
    elif user_input == "paper":
        if computer_action == "rock":
            print("you won")
        else:
            print("you lost")
    elif user_input == "scissor":
        if computer_action == "paper":
            print("you won")
        else:
            print("you lost")
    player = input("Want to try again? Y or N: ")
    if player == "N":
        break
