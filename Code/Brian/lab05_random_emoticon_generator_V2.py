# lab05_random_emoticon_generator_V2.py
import random #import used for random generation/choice of intergers and strings
while True:
    eyes_list = [':', ';'] #defines a list of eyes
    nose_list = ['-', '<'] #defines a list of noses
    mouth_list = ['P', 'D'] #defines a list of mouths
    eyes = random.choice(eyes_list) #chooses randomly from the list of eyes
    nose = random.choice(nose_list) #chooses randomly from the list of noses
    mouth = random.choice(mouth_list) #chooses randomly from the list of mouths
    length = input("Enter how many emoticons you would like: ") #prompts user to enter the desired number of emoticons
    length = int(length) #converts user input to an interger
    out_string = '' #defines as a blank string
    for piece in range(length): #takes the amount entered by user and applies that number of times to generate desired amount of emoticons with below code
        out_string += random.choice(eyes_list) + random.choice(nose_list) + random.choice(mouth_list)
    print(out_string)
    if_done = input("Would you like to try again?  Enter 'yes'.  If not, enter 'done' ").lower()
    if if_done == 'done': #if user enters done, exits the program.
        break
    elif if_done == 'yes': #if user enters yes, it will continue in the loop
        continue
    else:
        print("That is not a valid input, goodbye. ") #if user enters anything other that done or yes, prints statement and exits the program.
        break
