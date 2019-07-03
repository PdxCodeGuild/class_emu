'''

Group Exercise: Hangman

Let's write a program to play a game of hangman. In the data folder, you'll find english.txt which contains a list of several thousand english words. Write a function load_words(path) which reads the text from this file and return a list of strings which are greater than 5 letters. Randomly pick a word from that list and begin the game. Allow the user 10 tries to guess the letters of the word. Keep track of the letters the user has already guessed.

Show them a list of 'blanks' and ask them for a letter. If they guess a letter which is in the word, show the blanks with the letters filled in. If they guess a letter which is not in the word, tell them and subtract 1 from their remaining guesses. If they guess a letter they've guessed before, tell them and do not subtract 1 from their guesses.

Be kind, if the user can't guess the word in the number of allotted guesses, print the word and ask them if they'd like to play again.

Feel free to customize the user interface, but provide these minimum features. Below is an example run of the program.

_ _ _ _ _ _ _ _ _
# of guesses remaining: 10
already guessed:

Guess a letter: a
_ a _ _ _ _ a _ _
# of guesses remaining: 10
already guessed: a

Guess a letter: a
You've already guessed that
_ a _ _ _ _ a _ _
# of guesses remaining: 10
already guessed: a

Guess a letter: k
_ a _ _ _ _ a _ _
# of guesses remaining: 9
already guessed: a, k
Guess a letter:

'''



import random

def load_words(path):
    #read file and return list of strings > than 5 letters
    with open(path, 'r') as f:
        contents = f.read()
    #print(contents)
    #create a list of words 5 characters or more
    word_list = contents.split('\n')
    #print(word_list)
    hangman_words = []
    for word in word_list:
        if len(word) > 5:
            hangman_words.append(word)
    #print(hangman_words)
    return hangman_words

#randomly pick a word
word_file_path = r'C:\Users\flux\programs\class_emu\1 Python\data\english.txt'
word_bank = load_words(word_file_path)
game_word = random.choice(word_bank)
#print(game_word)

underscores = []
for i in range(len(game_word)):
    underscores.append("_")
#print(underscores)
user_tries = 10

guessed = []
while True:
    print(' '.join(underscores))
    print(f'Guesses remaining: {user_tries}')
    guessed.sort()
    print('Guessed letters: ' + ' '.join(guessed))
    user_guess = input("Guess a letter or the whole word: ")
    if len(user_guess) > 1:
        if user_guess == game_word:
            print('YOU WIN!')
        else:
            print('YOU LOST!')
            print(game_word)
        break
    if user_guess in guessed:
        print("Sorry, you've already guessed that")
    elif user_guess not in game_word:
        guessed.append(user_guess)
        print('sorry, try again')
        user_tries -= 1
    else:
        guessed.append(user_guess)
        for i in range(len(game_word)):
            if user_guess == game_word[i]:
                underscores[i] = game_word[i]
    
    # lost condition
    if user_tries == 0:
        print("Sorry, you've tried too many times. Goodbye")
        print(game_word)
        break
    
    # win condition
    if "_" not in underscores:
        print("YOU WIN!")  
        break                              
    
    
    
    
    
