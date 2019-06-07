# filename: lab02_v1_mad_libs.py
'''
Lab 2: Mad Libs
Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result.

Instructions:
Search the interwebs for an example Mad Lib
Ask the user for each word you'll put in your Mad Lib
Use string concatenation to put each word into the Mad Lib

Story source: https://mobileapps4teachers.wordpress.com/2012/01/18/mad-libs-lite/
'''

# Ask the user for each word you'll put in your Mad Lib
adj1 = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
animal = input("Enter an animal (plural): ")
game = input("Enter a game: ")

# Use string concatenation to put each word into the Mad Lib
print(f"VACATIONS: A vacation is when you take a trip to some {adj1} place with your {adj2} family. Usually you go to some place that is near a/an {noun1} or up on a/an {noun2}. A good vacation place is one where you can ride {animal} or play {game}.")

'''
Example:
VACATIONS: A vacation is when you take a trip to some bright place with your loud family. Usually you go to some place that is near a/an beach or up on a/an finger. A good vacation place is one where you can ride kittens or play Cards Against Humanity.
'''
