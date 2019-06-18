# filename: lab04_v1_magic_8_ball.py
'''
Lab 4: Magic 8-Ball

Let's write a program to simulate the classic "Magic Eight Ball"

Print a welcome screen to the user.
Use the random module's random.choice() to choose a prediction.
Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
Display the result of the 8-ball.
Below are some example 'predictions': see "answer" list below
'''

import random

# create a list of 20 predictions
predictions = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

# Print a welcome screen to the user.
print("Welcome to the Virtual Magic 8 Ball\n")

# Prompt the user to ask the 8-ball a question e.g. "will I win the lottery tomorrow?"
question = input("Enter your question: ")

# Use the random module's random.choice() to choose a prediction.
prediction = random.choice(predictions)

# Display the result of the 8-ball.
print(prediction)
