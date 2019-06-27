# filename: lab22_v1_compute_ari.py
"""
Lab 22: Compute Automated Readability Index

Compute the ARI for a given body of text loaded in from a file.
The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text.
The general formula to compute the ARI is as follows:

=> 4.71(characters/words) + 0.5(words/sentences) - 21.43

The score is computed by multiplying the number of characters divided by the number of words by 4.71,
adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43.
If the result is a decimal, always round up. Scores greater than 14 should be presented as having the
same age and grade level as scores of 14.
"""

import requests
import string
import re

# Get the file
# response = requests.get("http://www.gutenberg.org/cache/epub/31168/pg31168.txt")
# book_title = "Astounding Stories"
response = requests.get("http://www.veryabc.cn/movie/uploads/script/Dialog-TheShawshankRedemption.txt")
book_title = "The Shawshank Redemption"
contents = response.text

# Open the file.
# with open(r'/home/larry/software_dev/Python/class_emu/1 Python/data/apothecary.txt', 'r', encoding='utf-8') as f:
#     contents = f.read()
# book_title = "The Apothecary"
    # print(contents)

# contents = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

# Split into a list of words.
words_list = contents.split() # split on whitespace

clean_words = []
for i in range(len(words_list)):
    words_list[i] = words_list[i].lower()                       # convert to lowercase
    for letter in words_list[i]:
        if letter not in string.ascii_lowercase:                # if any letter no in ascii_lowercase string ...
            words_list[i] = words_list[i].replace(letter, "")   # ... remove it (replace with nothing)
    clean_words.append(words_list[i])                           # add the cleaned word to clean_words list

for word in clean_words:
    if word == '':
        clean_words.remove('') # example
# print(f"clean words: {clean_words}")

# Get number of characters (number_of_characters)
# concatenate to giant string & count the letters
number_of_characters = len(''.join(clean_words))

# Get number of words (number_of_words)
number_of_words = len(clean_words)

# char_word_avg = (number of characters divided by number of words) multiplied by 4.71
char_word_avg = (number_of_characters / number_of_words) * 4.71

# Get number of sentences (number_of_sentences)
number_of_sentences = len(re.split('[\w\s][\.!\?][\w\s]', contents)) # split on . or ? or ! plus space, then get length
# number_of_sentences = len(contents.split(". ")) # split on period+space, then get length

# word_sentences_avg = (number of words divided by number of sentences) multiplied by 0.5
word_sentences_avg = (number_of_words / number_of_sentences) * 0.5

# ari = (characters/words + words/sentences) - 21.43
ari = round((char_word_avg + word_sentences_avg) - 21.43)
if ari > 14:
    ari = 14

# Use the following dictionary to look up the age range and grade level.
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

# The output should look something like the following:
# --------------------------------------------------------
#
# The ARI for gettysburg-address.txt is 12
# This corresponds to a 11th Grade level of difficulty
# that is suitable for an average person 16-17 years old.
#
# --------------------------------------------------------

print(f"""--------------------------------------------------------

The ARI for {book_title} is {ari}.
This corresponds to a {ari_scale[ari]['grade_level']} level of difficulty
that is suitable for an average person {ari_scale[ari]['ages']} years old.

--------------------------------------------------------
""")
