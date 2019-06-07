# lab12.py

# imports "random" module
import random
# computer makes a choice
random_choice = random.randint(1,5)
# sets a counter
counter = 0

while True:
# asks user for guess
    user_input = int(input("What's your choice? "))
# adds 1 to the counter during each iteration of the loop
    counter += 1;
# if user_input does not equal random_choice
    if user_input != random_choice:
        print("Try again")
# if user_input does equal random_choice
    else:
        print("Correct")
        break



# lab12v2

#import random # imports "random" module

#random_choice = random.randint(1,5) # computer makes a choice

#counter = 0 # starts couner at 0

#while True:

#    user_input = int(input("What's your choice? ")) # asks user for guess

#    counter = counter + 1; # the counter adds 1 after each try

#    if user_input != random_choice: # if user_input does not equal random_choice

#        print("Try again")

#    else: # if user_input does equal random_choice


#        print(f"Correct! It took you {counter} tries.") # prints text and runs code
#        break



# lab12v3

#import random # imports "random" module

#random_choice = random.randint(1,5) # computer makes a choice

#ounter = 0 # starts couner at 0

#hile True:

#    user_input = int(input("What's your choice? ")) # asks user for guess

#    counter = counter + 1; # the counter adds 1 after each try

#    if user_input > random_choice:
#        print("Too High.  Try Again")

#    if user_input < random_choice:
#        print("Too Low.  Try Again")

#    else: # if user_input does equal random_choice

#        print(f"Correct! It took you {counter} tries.") # prints text and runs code
#        break
