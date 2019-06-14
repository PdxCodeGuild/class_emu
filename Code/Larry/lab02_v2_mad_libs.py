# filename: lab02_v2a_mad_libs.py
'''
Lab 2: Mad Libs
Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result.

Story source: https://mobileapps4teachers.wordpress.com/2012/01/18/mad-libs-lite/

Version 2 (optional)
Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, separated by commas, then use the .split() function to store each adjective and later use it in your story.
Add randomness! Use the random module, rather than selecting which adjective goes where in the story.
'''
import random

# Ask the user for 3 adjectives
three_adj = [] # base case, list
for num in range(3):
    user_adj = input("Enter an adjective: ")
    # create a list of adjectives
    three_adj.append(user_adj)


# Add randomness! Use the random module, rather than selecting which adjective goes where in the story.
random.shuffle(three_adj)

# Use string concatenation to put each word into the Mad Lib using the items in the list
print(f"VACATIONS: A vacation is when you take a trip to some {three_adj[0]} place with your {three_adj[1]} family. Usually you go to some place that is near a/an {three_adj[2]} beach or up on a mountain. A good vacation place is one where you can ride donkeys or play Scrabble.")

'''
Example:
INPUT:
Enter an adjective: cool
Enter an adjective: noisy
Enter an adjective: bright

OUTPUT:
VACATIONS: A vacation is when you take a trip to some noisy place with your bright family. Usually you go to some place that is near a/an cool beach or up on a mountain. A good vacation place is one where you can ride donkeys or play Scrabble.
'''
