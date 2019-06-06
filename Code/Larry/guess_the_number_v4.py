# filename: "guess_the_number_v4.py"
'''
Lab 12: Guess the Number

Version 4 (optional)

Tell the user whether their current guess is closer than their last.
This can be done by maintaining a variable containing the last guess outside the loop,
then comparing the last guess to the current guess, and check if it's closer.

Hint: you're interested in comparing the two absolute differences:
abs(current_guess-target) and abs(last_guess-target).
'''

# Computer will guess a random int between 1 and 10.
import random
computer_number = random.randint(1,10)

# Using a while loop, allow the user to guess infinite times.
# Keep track of how many guesses the user has made, and tell them at the end.
counter = 0
last_guess = 0
while True:
    user_guess = input("Guess the number, or 'done': ")
    # if user guesses the correct number, exit the while loop
    if user_guess.isdigit() and computer_number == int(user_guess):
        counter = counter + 1
        print(f"Correct! You guessed {user_guess} and it only took {counter} tries.")
        break
    # elif user type 'done', exit the program
    elif user_guess == "done":
        print("Adios. Sayonara, buh-bye!")
        break
    else:
        # if user_guess is higher than the computer_number, say it's "too high"
        if int(user_guess) < computer_number:
            high_low = "That's too low"
        else:
        # if user_guess is higher than the computer_number, say it's "too high"
            high_low = "That's too high"

        # calculate absolute value between computer_number and last_guess & user_guess
        user_abs_diff = abs(int(user_guess) - computer_number)
        last_abs_diff = abs(int(last_guess) - computer_number)

        # compare current diff with last diff, tell user if they warmer (closer) or colder (further)
        if last_guess == 0:
        # if it's the user's first guess, just tell user to Try again
            print(f"{high_low}! Try again!")
        elif user_abs_diff < last_abs_diff:
        # elif user_abs_diff < last_abs_diff, then say you're "getting warmer"
            print(f"{high_low} but you're getting warmer. Try again!")
        else:
        # if user_abs_diff > last_abs_diff, then say you're "getting colder"
            print(f"{high_low} and you're getting colder. Try again!")

    # update last_guess variable and increment the counter
    last_guess = user_guess
    counter = counter + 1
