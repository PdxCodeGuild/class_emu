# modules

import requests
import random
import string





hangman_ascii_art = [
"""
_________
|/
|
|
|
|
|
|___
""",

"""
_________
|/   |
|
|
|
|
|
|___
H""",

"""
_________
|/   |
|   (_)
|
|
|
|
|___
HA""",

"""
________
|/   |
|   (_)
|    |
|    |
|
|
|___
HAN""",


"""
_________
|/   |
|   (_)
|   /|
|    |
|
|
|___
HANG""",


"""
_________
|/   |
|   (_)
|   /|\\
|    |
|
|
|___
HANGM""",



"""
________
|/   |
|   (_)
|   /|\\
|    |
|   /
|
|___
HANGMA""",


"""
________
|/   |
|   (_)
|   /|\\
|    |
|   / \\
|
|___
HANGMAN"""]




# todo
# show the user "you found 5 a's"


# file loading ===================================

# load text file

# get word from text file


def random_word():

    response = requests.get('https://raw.githubusercontent.com/PdxCodeGuild/class_sheep/master/1%20Python/data/english.txt')
    text = response.text

    # split
    text=text.split()
    # only take words > 5 characters
    big_words = []
    for word in text:
        if len(word) > 5:
            big_words.append(word)

    return random.choice(big_words)

word = random_word()

# initialization =================================

underscores = []
for num in range(len(word)):
    underscores.append('_')

guess_counter = len(hangman_ascii_art)

previous_guesses = []


# loop =======================================
while True:
    print(hangman_ascii_art[len(hangman_ascii_art)-guess_counter])
    print("Number of guesses remaining: " + str(guess_counter))
    print(' '.join(underscores))

    print("Previous guesses: " + ', '.join(previous_guesses))

    user_guess = input("Please select a letter: ").lower()
    if user_guess == word:
        print("Congratulations!")
        break
    if len(user_guess) == len(word):
        guess_counter -= 1
        print("Wrong. Nice try. -_-")
        continue
    if len(user_guess) != 1 or user_guess not in string.ascii_lowercase:
        print("That is not a valid guess. Dummy.")
        continue
    if user_guess in previous_guesses: # check if letter has already been guessed
        print("You already guessed that, Sherlock.")
        continue
    previous_guesses.append(user_guess)

    # check if letter is found within the word
    # change corresponding underscore to letter
    letter_found = 0
    for i in range(len(word)):
        if word[i] == user_guess:
            underscores[i] = word[i]
            letter_found += 1
    if letter_found == 0:
        guess_counter -= 1 # if there's no match, reduce guess counter
        print("Letter not found, archfool.")
    if letter_found > 0:
        print("You found " + str(letter_found) + " " + user_guess + ("'s" if letter_found > 1 else ''))

    # lose condition
    # if the # of guesses is 0, insult them and quit
    if guess_counter == 0:
        print("you are forever the archfool! The word was " + word)
        break
    if '_' not in underscores:
        print("You win, murderer! The word was " + word)
        break
