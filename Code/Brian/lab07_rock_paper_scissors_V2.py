# lab07_rock_paper_scissors_V2.py
import random #imports the random module for random number/word generation
rock_paper_scissors_list = ['Rock', 'Paper', 'Scissors'] #creates list to choose from
while True: #using a while loop to ask the user to choose to continue OR stop playing
    user_choice = input("Do you want (Rock), (Paper) or (Scissors)? ") #asks user for input
    user_choice = user_choice.lower() #converts user input to lowercase
    Computer_Pick = random.choice(rock_paper_scissors_list) #uses the random module to randomly choose from the list
    print(f"Computer picks: {Computer_Pick} ") #prints the string plus random pick to show the computers choice
    if Computer_Pick == 'Rock': #compares the computers random pick against the users pick.  Same for all below
        if user_choice == 'rock':
            print('Its a tie, try again!')
        elif user_choice == 'paper':
            print('You Win!')
        elif user_choice == 'scissors':
            print('You Lose!')
    if Computer_Pick == 'Paper':
        if user_choice == 'rock':
            print('You Lose!')
        elif user_choice == 'paper':
            print('Its a tie, try again!')
        elif user_choice == 'scissors':
            print('You Win!')
    if Computer_Pick == 'Scissors':
        if user_choice == 'rock':
            print('You Win!')
        elif user_choice == 'paper':
            print('You Lose!')
        elif user_choice == 'scissors':
            print('Its a tie, try again!')
    user_choice_proceed = input("Would you like to play again? If no, enter 'done' ").lower() #asks user for input and .lower() converts the user input into all lowercase
    if user_choice_proceed == "done": #if user types done, the program will stop (break out of the loop)
        break
