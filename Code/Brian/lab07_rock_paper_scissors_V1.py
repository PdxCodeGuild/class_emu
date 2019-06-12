# lab07_rock_paper_scissors_V1.py
import random #imports the random module for random number/word generation
rock_paper_scissors_list = ['Rock', 'Paper', 'Scissors'] #creates list to choose from
user_choice = input("Do you want (Rock), (Paper) or (Scissors)? ") #asks user for input
user_choice = user_choice.lower() #converts user input to lowercase
Computer_Pick = random.choice(rock_paper_scissors_list) #uses the random module to randomly choose from the list
print(f"Computer picks: {Computer_Pick} ") #prints the string plus random pick to show the computers choice
if Computer_Pick == 'Rock': #compares the computers random pick against the users pick.  Same for all below
    if user_choice == 'rock':
        print('Its a tie, try again!')
    if user_choice == 'paper':
        print('You Win!')
    if user_choice == 'scissors':
        print('You Lose!')
if Computer_Pick == 'Paper':
    if user_choice == 'rock':
        print('You Lose!')
    if user_choice == 'paper':
        print('Its a tie, try again!')
    if user_choice == 'scissors':
        print('You Win!')
if Computer_Pick == 'Scissors':
    if user_choice == 'rock':
        print('You Win!')
    if user_choice == 'paper':
        print('You Lose!')
    if user_choice == 'scissors':
        print('Its a tie, try again!')
