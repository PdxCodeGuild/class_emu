# filename: lab12_v3_guess_the_number.py
'''
Lab 12: Guess the Number

Version 3
Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.
'''

# Computer will guess a random int between 1 and 10.
import random
computer_number = random.randint(1,10)
# Using a while loop, allow the user to guess infinite times.
# Keep track of how many guesses the user has made, and tell them at the end.
counter = 0
while True:
    user_guess = input("Guess the number, or 'done': ")
    # if user guesses the wrong number, try again, up to 10 attempts
    if user_guess == 'done':
        print("Adios. Sayonara, buh-bye!")
        break
    user_guess = int(user_guess)
    # if user guesses the correct number, exit the while loop
    if computer_number == user_guess:
        counter = counter + 1
        print(f"Correct! You guessed {user_guess} and it only took {counter} tries.")
        break
    else:
        # if user_guess is higher than the computer_number, say it's "too high"
        if user_guess < computer_number:
            print("That's too low! Try again!")
        else:
        # if user_guess is higher than the computer_number, say it's "too high"
            print("That's too high! Try again!")
    counter = counter + 1
