# filename: lab12_v1_guess_the_number.py
'''
Lab 12: Guess the Number

Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10.
The user will then try to guess the number, and the program will tell them whether they're right or wrong.

Using a while loop, allow the user to guess 10 times.
If they fail to guess the number after 10 tries, the user is told they've lost.
If the user guesses the number, the user is told they've won and the game exits.

You can get a random number using random.randint:
import random
x = random.randint(1,10)
print(x)
'''

import random

# Computer will guess a random int between 1 and 10.
computer_number = random.randint(1,10)

# Using a while loop, allow the user to guess 10 times.
counter = 0
while counter < 10:
    user_guess = int(input("Guess the number: "))
    # if user guesses the correct number, exit the while loop
    if computer_number == user_guess:
        print(f"Correct! You guessed {user_guess}.")
        break
    # if user guesses the wrong number, try again, up to 10 attempts
    if counter < 9:
        print(f"That's not it. Try again!")
    counter = counter + 1
print(f"Sorry Charlie. You only get 10 guesses.")
