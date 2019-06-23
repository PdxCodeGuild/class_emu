# lab07_rock_paper_scissors_V3.py
'''
** Version 3 (optional) **

Rock, paper, scissors, lizard, Spock!
https://www.instructables.com/id/How-to-Play-Rock-Paper-Scissors-Lizard-Spock/
'''
import random #imports the random module for random number/word generation
rpsclsp_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock'] #creates list to choose from
user_choice = input("Do you want (Rock), (Paper), (Scissors), (Lizard) or (Spock)? ") #asks user for input
user_choice = user_choice.lower() #converts user input to lowercase
Computer_Pick = random.choice(rpsclsp_list) #uses the random module to randomly choose from the list
print(f"Computer picks: {Computer_Pick} ") #prints the string plus random pick to show the computers choice
if Computer_Pick == 'Rock': #compares the computers random pick against the users pick.  Same for all below
    if user_choice == 'rock':
        print('Its a tie, try again!')
    elif user_choice == 'paper':
        print('You Win!')
    elif user_choice == 'scissors':
        print('You Lose!')
    elif user_choice == 'lizard':
        print('You Lose!')
    elif user_choice == 'spock':
        print('You Win!')
if Computer_Pick == 'Paper':
    if user_choice == 'rock':
        print('You Lose!')
    elif user_choice == 'paper':
        print('Its a tie, try again!')
    elif user_choice == 'scissors':
        print('You Win!')
    elif user_choice == 'lizard':
        print('You Win!')
    elif user_choice == 'spock':
        print('You Lose')
if Computer_Pick == 'Scissors':
    if user_choice == 'rock':
        print('You Win!')
    elif user_choice == 'paper':
        print('You Lose!')
    elif user_choice == 'scissors':
        print('Its a tie, try again!')
    elif user_choice == 'lizard':
        print('You Lose!')
    elif user_choice == 'spock':
        print('You Win!')
if Computer_Pick == 'Lizard':
    if user_choice == 'rock':
        print('You Win!')
    elif user_choice == 'paper':
        print('You Lose!')
    elif user_choice == 'scissors':
        print('You Win')
    elif user_choice == 'lizard':
        print('Its a tie, try again!')
    elif user_choice == 'spock':
        print('You Lose!')
if Computer_Pick == 'Spock':
    if user_choice == 'rock':
        print('You Lose!')
    elif user_choice == 'paper':
        print('You Win!')
    elif user_choice == 'scissors':
        print('You Lose')
    elif user_choice == 'lizard':
        print('You Win!')
    elif user_choice == 'spock':
        print('Its a tie, try again!')
