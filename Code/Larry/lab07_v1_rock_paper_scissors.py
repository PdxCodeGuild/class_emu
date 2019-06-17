# filename: lab07_v1_rock_paper_scissors.py
'''
Lab 7: Rock Paper Scissors
Let's play rock-paper-scissors with the computer.

The computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user

Let's list all the cases:
rock vs rock (tie)
rock vs paper
rock vs scissors
paper vs rock
paper vs paper (tie)
paper vs scissors
scissors vs rock
scissors vs paper
scissors vs scissors (tie)
'''
import random

# create list of choices
choices = ['rock', 'paper', 'scissors']

while True:
# The computer will ask the user for their choice (rock, paper, scissors)
    user_choice = input("Type your choice, (rock)(paper)(scissors): ")
    # validate user input, start over if user_choice is not one of three options in list
    if user_choice not in choices:
        print("Try again")
        continue

    # The computer will randomly choose rock, paper or scissors
    computer_choice = random.choice(choices)

    # "It's a tie!" print statement
    tie = f"Computer picked {computer_choice}. It's a tie!"
    # "You win" print statement
    you_win = f"Computer picked {computer_choice}. You win!"
    # "You lose" print statement
    you_lose = f"Computer picked {computer_choice}. You lose!"

    # Determine who won and tell the user
    if computer_choice == user_choice: # Tie: computer_choice is same as user_choice
        print(tie)
    elif computer_choice == "rock" and user_choice == "paper":
        print(you_win)
    elif computer_choice == "paper" and user_choice == "scissors":
        print(you_win)
    elif computer_choice == "scissors" and user_choice == "rock":
        print(you_win)
    elif computer_choice == "rock" and user_choice == "scissors":
        print(you_lose)
    elif computer_choice == "paper" and user_choice == "rock":
        print(you_lose)
    elif computer_choice == "scissors" and user_choice == "paper":
        print(you_lose)

    break # get out of the while loop
