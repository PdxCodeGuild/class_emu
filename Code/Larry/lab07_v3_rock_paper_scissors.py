# filename: lab07_v3_rock_paper_scissors.py
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
rock vs lizard
rock vs Spock
paper vs rock
paper vs paper (tie)
paper vs scissors
paper vs lizard
paper vs Spock
scissors vs rock
scissors vs paper
scissors vs scissors (tie)
scissors vs lizard
scissors vs Spock
lizard vs rock
lizard vs paper
lizard vs scissors
lizard vs lizard (tie)
lizard vs Spock
Spock vs rock
Spock vs paper
Spock vs scissors
Spock vs lizard
Spock vs Spock (tie)

Version 2 (optional)
After playing, ask them if they'd like to play again. If they say yes, restart the game, otherwise exit.

Version 3 (optional)
Rock, paper, scissors, lizard, Spock!
https://www.instructables.com/id/How-to-Play-Rock-Paper-Scissors-Lizard-Spock/
'''
import random

# create list of choices
choices = ['rock', 'paper', 'scissors', 'lizard', 'Spock']

while True:
# The computer will ask the user for their choice (rock, paper, scissors)
    user_choice = input("Type your choice, (rock)(paper)(scissors)(lizard)(Spock): ")
    # validate user input, start over if user_choice is not one of three options in list
    if user_choice not in choices:
        print("That's not one of the choices. Try again.")
        continue

    # The computer will randomly choose rock, paper or scissors
    computer_choice = random.choice(choices)

    # Determine who won and tell the user
    if computer_choice == user_choice: # Tie: computer_choice is same as user_choice
        print(f"Computer picked {computer_choice}. It's a tie!")
    elif computer_choice == "rock" and user_choice == "paper":
        print(f"Computer picked {computer_choice}.\nYou win!  Paper covers rock.")
    elif computer_choice == "rock" and user_choice == "scissors":
        print(f"Computer picked {computer_choice}.\nYou lose! Rock crushes scissors.")
    elif computer_choice == "rock" and user_choice == "lizard":
        print(f"Computer picked {computer_choice}.\nYou lose! Rock crushes lizard.")
    elif computer_choice == "rock" and user_choice == "Spock":
        print(f"Computer picked {computer_choice}.\nYou win! Spock vaporizes rock.")
    elif computer_choice == "paper" and user_choice == "rock":
        print(f"Computer picked {computer_choice}.\nYou lose! Paper covers rock.")
    elif computer_choice == "paper" and user_choice == "scissors":
        print(f"Computer picked {computer_choice}.\nYou win! Scissors cut paper.")
    elif computer_choice == "paper" and user_choice == "lizard":
        print(f"Computer picked {computer_choice}.\nYou win! Lizard eats paper.")
    elif computer_choice == "paper" and user_choice == "Spock":
        print(f"Computer picked {computer_choice}.\nYou lose! Paper disproves Spock.")
    elif computer_choice == "scissors" and user_choice == "rock":
        print(f"Computer picked {computer_choice}.\nYou win! Rock crushes scissors.")
    elif computer_choice == "scissors" and user_choice == "paper":
        print(f"Computer picked {computer_choice}.\nYou lose! Scissors cut paper.")
    elif computer_choice == "scissors" and user_choice == "lizard":
        print(f"Computer picked {computer_choice}.\nYou lose! Scissors decapitate lizard.")
    elif computer_choice == "scissors" and user_choice == "Spock":
        print(f"Computer picked {computer_choice}.\nYou win! Spock smashes scissors.")
    elif computer_choice == "lizard" and user_choice == "rock":
        print(f"Computer picked {computer_choice}.\nYou win! Rock crushes lizard.")
    elif computer_choice == "lizard" and user_choice == "paper":
        print(f"Computer picked {computer_choice}.\nYou lose! Lizard eats paper.")
    elif computer_choice == "lizard" and user_choice == "scissors":
        print(f"Computer picked {computer_choice}.\nYou win! Scissors decapitate lizard.")
    elif computer_choice == "lizard" and user_choice == "Spock":
        print(f"Computer picked {computer_choice}.\nYou lose! Lizard poisons Spock.")
    elif computer_choice == "Spock" and user_choice == "rock":
        print(f"Computer picked {computer_choice}.\nYou lose! Spock vaporizes rock.")
    elif computer_choice == "Spock" and user_choice == "paper":
        print(f"Computer picked {computer_choice}.\nYou win! Paper disproves Spock.")
    elif computer_choice == "Spock" and user_choice == "scissors":
        print(f"Computer picked {computer_choice}.\nYou lose! Spock smashes scissors.")
    elif computer_choice == "Spock" and user_choice == "lizard":
        print(f"Computer picked {computer_choice}.\nYou win! Lizard poisons Spock.")

    # After playing, ask them if they'd like to play again.
    start_again = input("Do you want to play again?: (yes)(no) ")
    # If they say yes, restart the game, otherwise exit.
    if start_again == "yes":
        continue
    else:
        break
