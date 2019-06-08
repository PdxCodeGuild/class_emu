# guess_number.py

import random

comp_number = random.randint(1, 10)
print("The Computer Chose A Number...")

while True:
    user_answer = input ("What is your guess? ")
    user_answer = int(user_answer)
    if user_answer == comp_number:
        print("Way to go, champ!")
        break
    else:
        print("All your base are belong to us.")
    if user_answer > comp_number:
        print("Too High")
    if user_answer < comp_number:
        print("Too Low")
