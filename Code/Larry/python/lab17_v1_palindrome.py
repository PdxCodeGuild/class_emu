# filename: lab17_v1_palindrome.py
'''
Lab 17: Palindrome

Let's write a palindrome.

Palindrome
A palindrome is a word that's the same forwards or backwards, e.g. racecar.
Another way to think of it is as a word that's equal to its own reverse.

Write a function check_palindrome which takes a string, and
returns True if the string's a palindrome, or
returns False if it's not.

>>> enter a word: racecar
>>> 'racecar' is a palindrome
>>> enter a word: palindrome
>>> 'palindrome' is not a palindrome
'''

from string import ascii_lowercase # for utilizing the ascii_lowercase set
from sys    import argv            # for using sys.argv e.g. $python filename.py run_tests

def check_palindrome(user_word):

    # Sanitize user_word
    user_word = user_word.replace(" ", "").lower() # remove spaces and convert to lowercase letters
    for letter in user_word:
        if letter not in ascii_lowercase:        # if any characters are not lowercase letters
            user_word = user_word.replace(letter, "")   # replace them with nothing

    # Loop through each letter in the user_word
    for i in range(len(user_word)):
        # Check if 1st letter=last letter, 2nd letter=2nd to last, etc
        if user_word[i] != user_word[(-1-i)]:
            return False # if any mismatches are found, break out of for loop (return False)
    return True          # otherwise, return True

if len(argv) == 1: # only execute these lines 'run_tests' is passed

    # Get user input
    user_word = input("\n[Palindrome] Enter a word: ")

    # Print the result of the comparsion
    result = check_palindrome(user_word)
    if result:
        print(f"\n{result}: '{user_word}' is a palindrome.\n")     # evals to True, print "it's a palindrome"
    else:
        print(f"\n{result}: '{user_word}' is a not palindrome.\n") # evals to False, print "it's not a palindrome"

###########################################################
### UNIT TESTS ###
###########################################################

# Check a variety of comparison (with spaces, Capital letters, punctuation)
if len(argv) > 1:
    if argv[1] == 'run_tests':  # argv[1] = first argument after the program name, e.g. py filename.py run_tests

        # Source: https://www.grammarly.com/blog/16-surprisingly-funny-palindromes/
        test_data = [
            (1, 'racecar', True),
            (2, 'Race car', True),
            (3, 'Race car!', True),
            (4, 'Taco cat', True),
            (5, 'Yo, banana boy!', True),
            (6, 'Ed, I saw Harpo Marx ram Oprah W. aside.', True),
            (7, 'Do geese see God?', True),
            (8, 'A man, a plan, a canal: Panama.', True),
            (9, 'Straw? No, too stupid a fad; I put soot on warts', True),
            (10, 'A nut for a jar of tuna.', True),
            (11, 'Al lets Della call Ed "Stella."', True),
            (12, 'Al lets Della call Ed “Stella.”', True),
            (13, 'Are we not pure? "No, sir!" Panama\'s moody Noriega brags. "It is garbage!" Irony dooms a man—a prisoner up to new era.', True),
            (14, 'Are we not pure? “No, sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man—a prisoner up to new era.', True),
            (15, 'tacacot', False),
            (16, 'afghha', False),
            (17, 'racecars', False)
        ]

        from lab_functions import unit_tester_1

        print(unit_tester_1(test_data, check_palindrome))
