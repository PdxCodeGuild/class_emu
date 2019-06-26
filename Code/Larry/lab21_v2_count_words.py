# filename: lab21_v2_counts_words.py
"""
Lab 21: Count Words

Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and
display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to
identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

Version 2
Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.
USE list of tuples
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
book_words_list = contents.split() # split on whitespace

# Clean words: Make everything lowercase, strip punctuation
# (Based on snippet of code from lab17_v2_anagram.py)
clean_words = []
for i in range(len(book_words_list)):
    book_words_list[i] = book_words_list[i].lower()    # convert to lowercase
    for letter in book_words_list[i]:
        if letter not in string.ascii_lowercase:       # if any letter no in ascii_lowercase string ...
            book_words_list[i] = book_words_list[i].replace(letter, "") # ... remove it (replace with nothing)
    clean_words.append(book_words_list[i])             # add the cleaned word to clean_words list

# Remove weird concatenations caused when stripping integers and punctuation, e.g. URLs
# No handling for contractions, English ordinal numbers, etc.
for word in clean_words:
    if word == 'wwwgutenbergorg':
        clean_words.remove('wwwgutenbergorg') # example (maybe unnecessary since count is low)
    # Add checks for a host of unwanted words(strings), e.g. 'youll', 'th' (from 18TH), etc.

# Create a list of word pairs (tuples)
pairs_list = []
for i in range(len(clean_words)-1): # 'len(clean_words)-1' => prevent IndexError: list index out of range
    pairs_list.append((clean_words[i], clean_words[i+1])) # list of tuples: word and word-next-to-it

# If a pair isn't in your dictionary yet, add it with a count of 1.
# If it is, increment its count.
# (Based on snippet of code from lab10_v4_average_numbers.py)
pairs_dict = {} # set base case (dictionary)
for pair in pairs_list:
    if len(pair[0]) > 2 and len(pair[1]) > 2: #skip pair if len of both words < 3, e.g. '', 'a', 'an'
    # if len(pair[0]) > 2 or len(pair[1]) > 2: #skip pair if len of either word < 3, e.g. '', 'a', 'an'
        if pair in pairs_dict:
            # if word pair already exists in pairs_dict, increment the count by 1
            pairs_dict[pair] += 1
        else:
            # if word pair does not exist in pairs_dict, add word & set count = 1
            pairs_dict[pair] = 1

# Print the most frequent top 10 out with their counts. You can do that with the code below.
# pairs_dict is a dictionary where the key is the word pair and the value is the count
pairs = list(pairs_dict.items()) # .items() returns a list of tuples
pairs.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(pairs))):  # print the top 10 pairs, or all of them, whichever is smaller
    print(pairs[i])
