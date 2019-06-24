# filename: lab02_v3_mad_libs.py
'''
Lab 2: Mad Libs

Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result.

Version 3 (optional)
Make it a repeatable game. Once you're done prompting the user for words, prompt them for whether they'd like to hear the story. Use a while loop to keep asking if they'd like to hear the story again until the answer is 'no'. You could then ask them if they'd like to make another story, and so on.

Story source: https://mobileapps4teachers.wordpress.com/2012/01/18/mad-libs-lite/
'''

play_again = ''
while True:
    if play_again == "no":
        break
    # Ask the user for each word you'll put in your Mad Lib
    adj1 = input("Enter an adjective: ")
    adj2 = input("Enter another adjective: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    animal = input("Enter an animal (plural): ")
    game = input("Enter a game: ")
    while True:
        hear_story = input("Do you want to hear the story? (yes)(no): ")
        if hear_story == "yes":
            # Use string concatenation to put each word into the Mad Lib using the items in the list
            print(f"VACATIONS: A vacation is when you take a trip to some {adj1} place with your {adj2} family. Usually you go to some place that is near a/an {noun1} or up on a/an {noun2}. A good vacation place is one where you can ride {animal} or play {game}.")
        else:
            play_again = input("Do you want to play again? (yes)(no): ")
            break
