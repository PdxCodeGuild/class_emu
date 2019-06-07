# filename: "guess_the_number_v5.py"
'''
Lab 12: Guess the Number

Version 4 (optional)

Tell the user whether their current guess is closer than their last.
This can be done by maintaining a variable containing the last guess outside the loop,
then comparing the last guess to the current guess, and check if it's closer.

Hint: you're interested in comparing the two absolute differences:
abs(current_guess-target) and abs(last_guess-target).

Version 5 (optional)

Swap the user with the computer: the user will pick a number,
and the computer will make random guesses until they get it right.

### how to make this version more interactive ###
# 1. computer randomly picks are starting (guess) number
# 2. if the computer_guess is greater than human_number, set computer_guess lower by 1
# 3. if the computer_guess is less than human_number, set computer_guess higher by 1
'''

# Computer will guess a random int between 1 and 10.
import random
# computer_number = random.randint(1,10)
human_number = int(input("Enter a number from 1 to 10: "))

# Using a while loop, allow the user to guess infinite times.
# Keep track of how many guesses the user has made, and tell them at the end.
counter = 0
last_guess = 0
# Instead of using random.randint(1,10), create a list and shuffle it.
one_ten = list(range(1,11))
random.shuffle(one_ten)
while True:
    # To prevent duplicates, guesses are pop()ped from the list.
    computer_guess = one_ten.pop()
    random.shuffle(one_ten)
    print(f"computer_guess: {computer_guess}")
    # if user guesses the correct number, exit the while loop
    if human_number == computer_guess:
        counter = counter + 1
        print(f"Correct! The computer guessed {computer_guess} and it only took {counter} tries.")
        break
    else:
        # if computer_guess is higher than the human_number, say it's "too high"
        if int(computer_guess) < human_number:
            high_low = "That's too low"
        else:
        # if computer_guess is higher than the human_number, say it's "too high"
            high_low = "That's too high"

        # calculate absolute value between human_number and last_guess & computer_guess
        computer_abs_diff = abs(int(computer_guess) - human_number)
        last_abs_diff = abs(int(last_guess) - human_number)

        # compare current diff with last diff, tell user if they warmer (closer) or colder (further)
        if last_guess == 0:
        # if it's the computer's first guess, just tell user to Try again
            print(f"{high_low}! Try again!")
        elif computer_abs_diff < last_abs_diff:
        # elif computer_abs_diff < last_abs_diff, then say you're "getting warmer"
            print(f"{high_low} but you're getting warmer. Try again!")
        else:
        # if computer_abs_diff > last_abs_diff, then say you're "getting colder"
            print(f"{high_low} and you're getting colder. Try again!")

    # update last_guess variable and increment the counter
    last_guess = computer_guess
    counter = counter + 1
