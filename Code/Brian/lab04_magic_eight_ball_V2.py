# lab04_magic_eight_ball_V2
import random #import random imports the random module, which contains a variety of things to do with random number generation.
print("Welcome") #The print function in Python is a function that outputs to your console window whatever you say you want to print out.
while True:
    user_question = input("Ask the 8 ball a question: ") #variable pointing to a string.  input always outputs a string.  asks the user to type a # QUESTION: .  It's important to use quotes (single or double) inside of ()
    random_result = ['Outlook does not look good', 'no', 'You bet', 'Absolutely'] #variable pointing to a list. Lists use brackets [] and must be in quotes (singler or double) and seperated by a comma.  This list will provide the random choice.
    print(f"And the 8 ball says:  {random.choice(random_result)}")  #In Python source code, an f-string is a literal string, prefixed with 'f', which contains expressions inside curly braces which will run as code inside the string.
    user_choice_proceed = input("If you would like to Ask another question enter 'yes'. If not, enter 'no' or 'done' ").lower() #asks user for input and .lower() converts the user input into all lowercase
    if user_choice_proceed == "done" or user_choice_proceed == "no": #if user types either, the program will stop (break out of the loop)
        break
    elif user_choice_proceed == "yes": #if user types yes, will continue in the loop
        continue
    else:
        print("Sorry, that is not a valid input. Please ask the 8 ball another question. ") #if user types anything other than yes, done or no: the use will see this message and be prompted to ask the 8 ball another question.
