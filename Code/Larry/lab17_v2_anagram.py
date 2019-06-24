# filename: lab17_v2_anagram.py
'''
Lab 17: Anagram

Let's write an anagram - This version uses sorted(list) to split the words to letters AND do the sorting

Two words are anagrams of each other if the letters of one can be rearranged to fit the other.
e.g. anagram and nag a ram.

Write another function check_anagram that takes two strings as parameters and
returns True if they're anagrams of each other,
returns False if they're not.

The procedure for comparing the two strings is as follow:
Convert each word to lower case (lower)
Remove all the spaces from each word (replace)
Sort the letters of each word (sorted)
Check if the two are equal
>>> enter the first word: anagram
>>> enter the second word: nag a ram
>>> 'anagram' and 'nag a ram' are anagrams
'''

import string

def check_anagram(user_word1, user_word2):

    # Sanitize user_words
    user_words = [user_word1, user_word2]
    clean_words = []
    for i in range(len(user_words)):
        user_words[i] = user_words[i].replace(" ", "").lower()    # remove spaces and convert to lowercase
        for letter in user_words[i]:
            if letter not in string.ascii_lowercase:       # if any letter no in ascii_lowercase string ...
                user_words[i] = user_words[i].replace(letter, "") # ... remove it (replace with nothing)
        clean_words.append(user_words[i])                         # add the cleaned word to clean_words list

    if len(clean_words[0]) != len(clean_words[1]): # check_anagram fails if the words aren't the same length
        return False

    # Compare the list using the sorted() function
    if sorted(clean_words[0]) == sorted(clean_words[1]): # if both lists of letters are equal, ...
        return True                                      # ... return True
    return False                                         # else return False

# ''' *** uncomment this line to run the unit tests ***
# Get user input
while True:                                 # stay on this input prompt, ...
    user_word1 = input("\n[Anagram] Enter a word: ")
    if len(user_word1) > 0: #               # ... unless the user submits at least one character
        break
while True:                                 # stay on this input prompt, ...
    user_word2 = input("[Anagram] Enter another word: ")
    if len(user_word2) > 0:                 # ... unless the user submits at least one character
        break

# Print the result of the comparsion
result = check_anagram(user_word1, user_word2)
if result:
    print(f"\n{result}: '{user_word1}' is an anagram of '{user_word2}'\n")
else:
    print(f"\n{result}: '{user_word1}' is NOT an anagram of '{user_word2}'\n")
# '''

###########################################################
### UNIT TESTS ###
###########################################################

# [PASS] N/A: "" == ""          # Empty values are disallowed
# [PASS] N/A: "anagram" != ""   # Empty values are disallowed
# [PASS] N/A: "" != "anagram"   # Empty values are disallowed
# [FAIL] N/A: "a1a" != "a2a"    # Characters not in ascii_lowercase are removed, including integers

# Check a variety of comparison (with spaces, Capital letters, punctuation)
if __name__ == '__main__':

    test_data = [
        (1, 'anagram', 'nag a ram', True),
        (2, 'Nude Dragons', 'Soundgarden', True),
        (3, 'Tar', 'Rat', True),
        (4, 'Arc', 'Car', True),
        (5, 'Elbow', 'Below', True),
        (6, 'State', 'Taste', True),
        (7, 'Cider', 'Cried', True),
        (8, 'Dusty', 'Study', True),
        (9, 'Night', 'Thing', True),
        (10, 'Inch', 'Chin', True),
        (11, 'Brag', 'Grab!', True),
        (12, 'Cat', 'Act', True),
        (13, 'Bored', 'Robed', True),
        (14, 'Save', 'Vase', True),
        (15, 'Angel', 'Glean', True),
        (16, 'Stressed', 'Desserts', True),
        (17, 'debit card', 'bad credit', True),
        (18, 'Dormitory', 'Dirty room', True),
        (19, 'School master', 'The classroom', True),
        (20, 'Conversation', 'Voices rant on', True),
        (21, 'Listen', 'Silent', True),
        (22, 'Astronomer', 'Moon starer', True),
        (23, 'The eyes', 'They see', True),
        (24, 'A gentleman', 'Elegant man', True),
        (25, 'Funeral', 'Real fun', True),
        (26, 'The Morse Codes', 'Here comes dots', True),
        (27, 'Eleven, plus two', 'Twelve, plus one', True),
        (28, 'Slot machines', 'Cash lost in me', True),
        (29, 'Fourth of July', 'Joyful Fourth', True),
        (30, 'The Morse Code', 'Here comes dots', False),
        (31, 'tacocat', 'tacacat', False),
        (32, 'School master', 'The glassroom', False),
        (33, 'Angel', 'Gleam', False),
        (34, 'Astronomer', 'Moon starts', False),
        (35, 'Fourth of June', 'Joyful Fourth', False),
        (36, 'asdf', '(fdda)', False)
    ]

    from lab_functions import run_tests_2

    # print(run_tests_2(test_data, check_anagram)) # *** uncomment this line to run the unit tests ***
