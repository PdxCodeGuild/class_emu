# lab04.py


# imports the random module to use later in the code
import random
# user_question is made up VARIABLE so I know waht it is.  input() asks the user for input
user_question = input("Hello, What question do you have?: ")
# answer_list is another VARIABLE.  [] make a list.
answer_list = ['Yes', 'No', 'maybe']
# print, prints to the screen.  f" allows curly braces to run code.
print(f"Answer: {random.choice(answer_list)}")




#v2




#import random# imports random module

#while True:
    # asks user a question
#    user_question = input("Hello, What question do you have?: ")
    # list that program will choose from
#    answer_list = ['Yes', 'No', 'Maybe']
    # displays the random choice from the list
#    print(f"Answer: {random.choice(answer_list)}")
#    user_question2 = input("Keep playing? Yes or Done:  ")
#    if user_question2.lower() == 'done':
#        break
