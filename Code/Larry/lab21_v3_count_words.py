# filename: lab21_v2_counts_words.py
"""
Lab 21: Count Words

Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and
display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to
identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

Version 3 (optional)
Let the user enter a word, then show the words which most frequently follow it.

NOTHING IMPLEMENTED YET
"""

import requests
import string

# Get user input
user_word = input("Enter a word, e.g. 'strange': ")

# Get the file
response = requests.get("http://www.gutenberg.org/cache/epub/31168/pg31168.txt")
contents = response.text

# # Open the file.
# with open(r'/users/larrymoiola/Desktop/class_emu/1 Python/data/apothecary.txt', 'r', encoding='utf-8') as f:
#     contents = f.read()

# Split into a list of words.
words_list = contents.split() # split on whitespace

# Make everything lowercase, strip punctuation
# based on snippet of code from lab17_v2_anagram.py
clean_words = []
for i in range(len(words_list)):
    words_list[i] = words_list[i].lower()              # convert to lowercase
    for letter in words_list[i]:
        if letter not in string.ascii_lowercase:       # if any letter no in ascii_lowercase string ...
            words_list[i] = words_list[i].replace(letter, "") # ... remove it (replace with nothing)
    clean_words.append(words_list[i])                  # add the cleaned word to clean_words list

# Create a list of word pairs (tuples)
pairs_list = []
for i in range(len(clean_words)-1):
    pairs_list.append((clean_words[i], clean_words[i+1]))

# If a word isn't in your dictionary yet, add it with a count of 1.
# If it is, increment its count.
# (Based on snippet of code from lab10_v4_average_numbers.py)
word_follows_myword = {} # set base case (dictionary)
for i in range(len(pairs_list)):
    if user_word == pairs_list[i][0]:
        # print(pairs_list[i][1])
        if pairs_list[i][1] in word_follows_myword:
            # if the user enters a number that already exists, increment the count by 1
            word_follows_myword[pairs_list[i][1]] += 1
        else:
            # if word does not yet exist, set count = 1
            word_follows_myword[pairs_list[i][1]] = 1

# Print the most frequent top 10 out with their counts. You can do that with the code below.
# word_follows_myword is a dictionary where the key is the word and the value is the count
word_follows_myword = list(word_follows_myword.items()) # .items() returns a list of tuples
word_follows_myword.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(word_follows_myword))):  # print the top 10 words that come after my word, or all of them, whichever is smaller
    print(word_follows_myword[i])
