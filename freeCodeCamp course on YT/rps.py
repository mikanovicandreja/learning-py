import sys
import random
from enum import Enum

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input("Enter: \n1 for Rock,\n2 for Paper or,\n3 for Scissors: ")
    if playerchoice not in ["1", "2", "3"]:
        print("You must choose 1, 2, or 3.")
        return play_rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.','') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.','') + ".")

    # Control flow
    if player == 1 and computer == 2:
        print("You win!\n")
    elif player == 2 and computer == 1:
        print("You win!\n")
    elif player == 3 and computer == 2:
        print("You win!\n")
    elif player == computer:
        print("Tie game!\n")
    else:
        print("Python wins!\n")

    while True:
        playagain = input("\nPlay again?\nY for Yes or\nQ to quit: ")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("Thank you for playing!")
        playagain = False       # break would also work here

play_rps()