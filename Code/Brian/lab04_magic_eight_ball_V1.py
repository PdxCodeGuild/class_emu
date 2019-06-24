# lab04_magic_eight_ball_V1
'''
Lab 4: Magic 8-Ball

** Version 1 **

Let's write a program to simulate the classic "Magic Eight Ball"

Concepts Covered
input, print
import
random.choice
Instructions
Print a welcome screen to the user.
Use the random module's random.choice() to choose a prediction.
Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
Display the result of the 8-ball.
Below are some example 'predictions':

It is certain
It is decidedly so
Without a doubt
Yes definitely
You may rely on it
As I see it, yes
Most likely
Outlook good
Yes
Signs point to yes
Reply hazy try again
Ask again later
Better not tell you now
Cannot predict now
Concentrate and ask again
Don't count on it
My reply is no
My sources say no
Outlook not so good
Very doubtful
'''
print("Welcome") #The print function in Python is a function that outputs to your console window whatever you say you want to print out.
import random #import random imports the random module, which contains a variety of things to do with random number generation.
user_question = input("Ask the 8 ball a question: ") #variable pointing to a string.  input always outputs a string.  asks the user to type a # QUESTION: .  It's important to use quotes (single or double) inside of ()
random_result = ['Outlook does not look good', 'no', 'You bet', 'Absolutely'] #variable pointing to a list. Lists use brackets [] and must be in quotes (singler or double) and seperated by a comma.  This list will provide the random choice.
print(f"And the 8 ball says:  {random.choice(random_result)}")  #In Python source code, an f-string is a literal string, prefixed with 'f', which contains expressions inside curly braces which will run as code inside the string.
