# lab02_madlibs_V2: use split() function and add randomness to the adjective list
# Using movie quote: “You is kind. You is smart. You is important.” -The Help, 2011
import random # imports the random module, which contains a variety of things to do with random number and/or word generation.
user_adjectives = input("Enter 3 adjectives seperated by commas: ")
# asks user to enter 3 adjectives separated by commas to be able to split them into a list, later used for random generation.
while True: # while True: will run with the code until either something becomes false or it breaks out of the loop (or crashes)
    user_choice_proceed = input("Would you like to hear the story? Type 'yes' or 'no' ").lower()
    # asks the user to choose if they want to hear the story or not by entering yes or no.
    if user_choice_proceed == "no": # if statement checks to see if user types no, if so, breaks out with break statement below
        break
    elif user_choice_proceed == "yes": # if statement checks to see if user types yes, or anything other than "no" and runs the code and asks again in the loop.
        adjective_list = user_adjectives.split() # The split() method splits a string into a list.
        random.shuffle(adjective_list) # randomly shuffles the list, to be able to choose from later
        while adjective_list: # creating a while loop to loop over the list
            adjective_1 = adjective_list.pop() # using the pop() function to select and remove item from list so it can only be used once.
            adjective_2 = adjective_list.pop() # repeating previous step to use the next item randomly
            adjective_3 = adjective_list.pop() # same as last line
            print(f"You is {adjective_1}. You is {adjective_2}. You is {adjective_3}.") # prints the random 3 adjectives, from previous steps, into the madlib
    else:
        print('not a valid answer')
