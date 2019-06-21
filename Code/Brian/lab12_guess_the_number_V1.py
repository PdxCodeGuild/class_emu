# lab12_guess_the_number_V1.py
'''
Lab 12: Guess the Number
Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10.
The user will then try to guess the number, and the program will tell them whether they're right or wrong.

Concepts Covered
random.randint
REPL: read-evaluate-print loop
input, print

** Version 1 **
Using a while loop, allow the user to guess 10 times.
If they fail to guess the number after 10 tries, the user is told they've lost.
If the user guesses the number, the user is told they've won and the game exits.
You can get a random number using random.randint:

import random
x = random.randint(1,10)
print(x)
Below is an example run of the game:

guess the number: 5
try again!
guess the number: 2
try again!
guess the number: 3
correct! you guessed 3 times
NOTE: ** you guessed 3 times ** Nowhere in Version 1 does it say to report the number of user guesses to the user.
'''

import random # imports the random module for random generation
print("Hello.  Let's play 'Guess the Number'.  The computer will choose a number between 0 and 10.  Can you guess it? ") # prints the statement
computer_number = random.randint(0, 10) # defines the variable computer_number and generates a random number between 0 and 10
user_tries = 0 # defines the variable user_tries and gives it a value of 0
while True: # starts a while loop
    user_guess = int(input("What do you think the number between 0 and 10 will be? ")) # defines the variable user_guess and prompts user for input and converts that input to an integer
    user_tries += 1 # user_tries increments by 1 for every iteration of the while loop
    if user_guess == computer_number: # if statment inside the while loop to determine if user_guess equals computer_number
        print(f"You are Correct, You win!") # if the above statement is true, this code runs and F string makes the code inside curly brackets run as code {}
        break # if the above if statement is true, will break out of the loop after the print statement runs
    else: # if the above if statment is false, the below code runs
        print("Sorry, that is incorrect. ") # prints this statement if the above if statement is false
    if user_tries == 10: # establishes that if the user_tries is equal to 10, the below code will run
        print("You took too many guesses, You lose. ") # if the above is true, prints this statement
        break # if the above is true, breaks out of the loop
