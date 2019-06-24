# lab12_guess_the_number_V3.py
'''
Lab 12: Guess the Number
Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10.
The user will then try to guess the number, and the program will tell them whether they're right or wrong.

Concepts Covered
random.randint
REPL: read-evaluate-print loop
input, print

** Version 3 **
Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.
'''
import random # imports the random module for random generation
print("Hello.  Let's play 'Guess the Number'.  The computer will choose a number between 0 and 10.  Can you guess it? ") # prints the statement
computer_number = random.randint(0, 10) # defines the variable computer_number and generates a random number between 0 and 10
while True: # starts a while loop
    user_guess = int(input("What do you think the number between 0 and 10 will be? ")) # defines the variable user_guess and prompts user for input and converts that input to an integer
    if user_guess == computer_number: # if statment inside the while loop to determine if user_guess equals computer_number
        print(f"You are Correct! The answer was {computer_number}. ") # if the above statement is true, this code runs and F string makes the code inside curly brackets run as code {}
        break # if the above if statement is true, will break out of the loop after the print statement runs
    else: # if the above if statment is false, the below code runs
        print("Sorry, that is incorrect.") # prints this statement if the above if statement is false
    if user_guess < computer_number: # if statement to determine if the user_guess is less than the computer_number
        print("You're guess was Too Low!") # if the above is true, prints this statement
    elif user_guess > computer_number: # if the above if statements are false, this will will check if the user_guess is greater than the computer_number
        print("You're guess was Too High!") # if the above is true, will print this statement
