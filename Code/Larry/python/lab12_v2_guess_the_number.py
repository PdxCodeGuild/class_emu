# filename: lab12_v2_guess_the_number.py
'''
Lab 12: Guess the Number

Version 2

Allow the user to make an unlimited number of guesses using a while True and break.
Keep track of how many guesses the user has made, and tell them at the end.
'''

import random

# Computer will guess a random int between 1 and 10.
computer_number = random.randint(1,10)

# Using a while loop, allow the user to guess infinite times.
# Keep track of how many guesses the user has made, and tell them at the end.
counter = 0
while True:
    user_guess = input("Guess the number, or 'done': ")
    # if user guesses the correct number, exit the while loop
    if user_guess.isdigit() and computer_number == int(user_guess):
        counter = counter + 1
        print(f"Correct! You guessed {user_guess} and it only took {counter} tries.")
        break
    # if user guesses the wrong number, try again, up to 10 attempts
    elif user_guess == "done":
        print("Adios. Sayonara, buh-bye!")
        break
    print(f"That's not it. Try again!")
    counter = counter + 1
