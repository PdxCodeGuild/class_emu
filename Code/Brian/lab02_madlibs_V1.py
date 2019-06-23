#lab02_madlibs_V1
'''
Lab 2: Mad Libs

** Version 1 **

Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result.

Instructions
Search the interwebs for an example Mad Lib
Ask the user for each word you'll put in your Mad Lib
Use string concatenation to put each word into the Mad Lib
Example:
>>> Give me an antonym for 'data': nonmaterial
>>> Tell me an adjective: Bearded
>>> Give me a sciency buzzword: half-stack
>>> A type of animal (plural): parrots
>>> Some Sciency thing: warp drive
>>> Another sciency thing: Trilithium crystals
>>> Sciency adjective: biochemical
...
>>> Nonmaterial Scientist Job Description:
>>> Seeking a bearded engineer, able to work on half-stack projects with a team of parrots.
>>> Key responsibilities:
>>> - Extract patterns from non-material
>>> - Optimize warp drive
>>> - Transform trilithium crystals into biochemical material.
'''
madlib_color1 = input("Name a color you like: ") # asks the user to input some data
madlib_color2 = input("Name another color you like: ")
madlib_noun1 = input("Name a place you like to be: ")
madlib_noun2 = input("Name another place you like to be: ")
print(f"Morpheus says: You take the {madlib_color1} pill - the story ends, you wake up in your {madlib_noun1} and believe whatever you want to believe. You take the {madlib_color2} pill - you stay in {madlib_noun2} and I show you how deep the rabbit-hole goes.")
# after asking the user to input the data you need, print and f string.  An f string allows the data inside curly braces to run as code.
