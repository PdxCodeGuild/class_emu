# guess_number.py


#imports random module to be used here
import random
#assigns comp_number to a number between 1 and 10
comp_number = random.randint(1, 10)
#asks the suer to pick a number
print("The Computer Chose A Number...")
#a while loop that only stops if the user picks the right answer
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
