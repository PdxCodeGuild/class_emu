# lab12_guess_the_number_V5.py
'''
Lab 12: Guess the Number
Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10.
The user will then try to guess the number, and the program will tell them whether they're right or wrong.

Concepts Covered
random.randint
REPL: read-evaluate-print loop
input, print

Version 5 (optional)
Swap the user with the computer: the user will pick a number, and the computer will make random guesses until they get it right.
'''
import random # imports the random module for random generation
computer_tries = 0 # defines the variable and starts with value 0 to account for the number of computer guesses
print("Hello.  Let's play 'Guess the Number'.  You will choose a number between 0 and 10 and the computer will try and guess it. ") # prints the statement
while True: # creates a while loop just in case the user types a number out of range, the game can continue
    user_number = int(input("Enter your number between 0 and 10: ")) # defines the variable user_number and prompts user for input and converts that input to an integer
    if user_number < 0 or user_number > 10: # if statement to determine if the user inputs a number out of range.
        print("Sorry that is not a valid number, please pick a number between 0 and 10. ") # if the above statement is true, prints message
        continue # continues back at the top of the while loop
    else: # if the above if statement is false, runs the code below
        print(f"Your number is {user_number}") # lets the user know what thier number is that the computer will try and guess. F string makes the code inside curly brackets run as code {}
        break # breaks out of the loop
while True: # starts a while loop
    computer_guess = random.randint(0, 10) # defines the variable computer_guess and generates a random number between 0 and 10
    computer_tries += 1 # increments computer_tries by 1 for every iteration of the loop
    if computer_guess == user_number: # if statment inside the while loop to determine if computer_guess equals user_number
        print(f"The computer was Correct! The computer took {computer_tries} tries to find the right answer. ") # if the above statement is true, this code runs and F string makes the code inside curly brackets run as code {}
        break # if the above if statement is true, will break out of the loop after the print statement runs
