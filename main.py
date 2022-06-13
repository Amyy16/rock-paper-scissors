import random

choices = ["R", "P", "S"]
computer = random.choice(choices)

is_valid_choice = False
while is_valid_choice == False:

    player = input("What is your choice: R for Rock, P for paper, S for Scissors \n").upper()

    if player not in choices:
        print("YOU HAVE SELECTED AN INVALID OPTION TRY AGAIN..   ")
        
    elif player == computer:
        print("player {} : computer {} ".format(player, computer))
        print("It is a tie.... Play again")

    else:
        is_valid_choice = True
        

if player == "R":
    if computer == "P":
        print("player {} : computer {} ".format(player, computer))
        print("You lose")
    if computer == "S":
        print("player {} : computer {} ".format(player, computer))
        print("You Win!!")

elif player == "S":
    if computer == "R":
        print("player {} : computer {} ".format(player, computer))
        print("You lose")
    if computer == "P":
        print("player {} : computer {} ".format(player, computer))
        print("You Win!!")

elif player == "P":
    if computer == "S":
        print("player {} : computer {} ".format(player, computer))
        print("You lose")
    if computer == "R":
        print("player {} : computer {} ".format(player, computer))
        print("You Win!!")






