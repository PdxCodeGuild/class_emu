# filename: lab17_v1_anagram.py
'''
Lab 17: Anagram

Let's write an anagram - This version uses 'for' loop to split the words AND list.sort()

Two words are anagrams of each other if the letters of one can be rearranged to fit the other.
e.g. anagram and nag a ram.

Write another function check_anagram that takes two strings as parameters and
returns True if they're anagrams of eachother,
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
        user_words[i] = user_words[i].replace(" ", "").lower() # remove spaces and convert to lowercase
        for letter in user_words[i]:
            if letter not in string.ascii_lowercase:    # if any letter no in ascii_lowercase string ...
                user_words[i] = user_words[i].replace(letter, "") # ... remove it (replace with nothing)
        clean_words.append(user_words[i])                         # add the cleaned word to clean_words list

    if len(clean_words[0]) != len(clean_words[1]): # check_anagram fails if the words aren't the same length
        return False

    # # Split each list element in string to its own list of letters
    for i in range(len(clean_words)):
        letters_list1 = list(clean_words[0]) # split words into a list of letters
        letters_list2 = list(clean_words[1]) # split words into a list of letters

    # Sort the list
    letters_list1.sort()
    letters_list2.sort()

    # Compare the list
    if letters_list1 == letters_list2:  # if both lists of letters are equal, ...
        return True                     # ... return True
    return False                        # else return False

# ''' *** uncomment this line to run the unit tests ***
# Get user input
while True:                                 # stay on this input prompt, ...
    user_word1 = input("[Anagram] Enter a word: ")
    if len(user_word1) > 0: #               # ... unless the user submits at least one character
        break
while True:                                 # stay on this input prompt, ...
    user_word2 = input("Enter another word: ")
    if len(user_word2) > 0:                 # ... unless the user submits at least one character
        break

# print(check_anagram(user_word1, user_word2)) #DEBUG
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
        (True, 'anagram', 'nag a ram'),
        (True, 'Nude Dragons', 'Soundgarden'),
        (True, 'Tar', 'Rat'),
        (True, 'Arc', 'Car'),
        (True, 'Elbow', 'Below'),
        (True, 'State', 'Taste'),
        (True, 'Cider', 'Cried'),
        (True, 'Dusty', 'Study'),
        (True, 'Night', 'Thing'),
        (True, 'Inch', 'Chin'),
        (True, 'Brag', 'Grab!'),
        (True, 'Cat', 'Act'),
        (True, 'Bored', 'Robed'),
        (True, 'Save', 'Vase'),
        (True, 'Angel', 'Glean'),
        (True, 'Stressed', 'Desserts'),
        (True, 'debit card', 'bad credit'),
        (True, 'Dormitory', 'Dirty room'),
        (True, 'School master', 'The classroom'),
        (True, 'Conversation', 'Voices rant on'),
        (True, 'Listen', 'Silent'),
        (True, 'Astronomer', 'Moon starer'),
        (True, 'The eyes', 'They see'),
        (True, 'A gentleman', 'Elegant man'),
        (True, 'Funeral', 'Real fun'),
        (True, 'The Morse Codes', 'Here comes dots'),
        (True, 'Eleven, plus two', 'Twelve, plus one'),
        (True, 'Slot machines', 'Cash lost in me'),
        (True, 'Fourth of July', 'Joyful Fourth'),
        (False, 'The Morse Code', 'Here comes dots'),
        (False, 'tacocat', 'tacacat'),
        (False, 'School master', 'The glassroom'),
        (False, 'Angel', 'Gleam'),
        (False, 'Astronomer', 'Moon starts'),
        (False, 'Fourth of June', 'Joyful Fourth'),
        (False, 'asdf', '(fdda)')
    ]

### RUN TESTS ###
def run_tests(input_output, function_name):
    failed_test_count = 0
    for i in range(len(input_output)):
        function_output = function_name(input_output[i][1], input_output[i][2])
        expected_output = input_output[i][0]
        if function_output != expected_output:
            return f"Input: {input_output[i][1], input_output[i][2]}\nFail. Expected Result: {expected_output} ==> Actual result: {function_output}"
            failed_test_count += 1
    if failed_test_count == 0:
            return "All tests passed."

# print(run_tests(test_data, check_anagram)) # *** uncomment this line to run the unit tests ***