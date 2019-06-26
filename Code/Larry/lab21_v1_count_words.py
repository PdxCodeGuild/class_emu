# filename: lab21_v1_counts_words.py
"""
Lab 21: Count Words

Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and
display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to
identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

Find a book on Project Gutenberg. Download it as a UTF-8 text file.

1. Open the file.
2. Make everything lowercase, strip punctuation, split into a list of words.
3. Your dictionary will have words as keys and counts as values.
    If a word isn't in your dictionary yet, add it with a count of 1.
    If it is, increment its count.
4. Print the most frequent top 10 out with their counts. You can do that with the code below.
# # word_dict is a dictionary where the key is the word and the value is the count
# words = list(word_dict.items()) # .items() returns a list of tuples
# words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#   print(words[i])
"""

import requests
import string

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
    words_list[i] = words_list[i].lower()                     # convert to lowercase
    for letter in words_list[i]:
        if letter not in string.ascii_lowercase:       # if any letter no in ascii_lowercase string ...
            words_list[i] = words_list[i].replace(letter, "") # ... remove it (replace with nothing)
    clean_words.append(words_list[i])                         # add the cleaned word to clean_words list

for word in clean_words:
    if word == 'wwwgutenbergorg':
        clean_words.remove('wwwgutenbergorg') # maybe unnecessary since count is low
    # Add checks for a host of unwanted words(strings), e.g. 'youll', 'th' (from 18TH), etc.

# * If a word isn't in your dictionary yet, add it with a count of 1.
# * If it is, increment its count.
# based on snippet of code from lab10_v4_average_numbers.py
words_dict = {} # set base case (dictionary)
for clean_word in clean_words:
    if len(clean_word) > 2: #skips words < 3 chars long, e.g. '',  like 'a', 'an'
        if clean_word in words_dict:
            # if the user enters a number that already exists, increment the count by 1
            words_dict[clean_word] += 1
        else:
            # if word does not yet exist, set count = 1
            words_dict[clean_word] = 1

# Print the most frequent top 10 out with their counts. You can do that with the code below.
# word_dict is a dictionary where the key is the word and the value is the count
words = list(words_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
