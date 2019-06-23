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
import string

def check_palindrome(user_word):

    # Sanitize user_word
    user_word = user_word.replace(" ", "").lower() # remove spaces and convert to lowercase letters
    for letter in user_word:
        if letter not in string.ascii_lowercase:        # if any characters are not lowercase letters
            user_word = user_word.replace(letter, "")   # replace them with nothing

    # Loop through each letter in the user_word
    for i in range(len(user_word)):
        # Check if 1st letter=last letter, 2nd letter=2nd to last, etc
        if user_word[i] != user_word[(-1-i)]:
            return False # if any mismatches are found, break out of for loop (return False)
    return True          # otherwise, return True

''' *** uncomment this line to run the unit tests ***
# Get user input
user_word = input("[Palindrome] Enter a word: ")

# Print the result of the comparsion
if check_palindrome(user_word):                  # if check_palindrome()
    print(f"'{user_word}' is a palindrome.")     # evals to True, print "it's a palindrome"
else:
    print(f"'{user_word}' is a not palindrome.") # evals to False, print "it's not a palindrome"
# '''

###########################################################
### UNIT TESTS ###
###########################################################

# Check a variety of comparison (with spaces, Capital letters, punctuation)
if __name__ == '__main__':

    # Source: https://www.grammarly.com/blog/16-surprisingly-funny-palindromes/
    test_data = [
        (True, 'racecar'),
        (True, 'Race car'),
        (True, 'Race car!'),
        (True, 'Taco cat'),
        (True, 'Yo, banana boy!'),
        (True, 'Ed, I saw Harpo Marx ram Oprah W. aside.'),
        (True, 'Do geese see God?'),
        (True, 'A man, a plan, a canal: Panama.'),
        (True, 'Straw? No, too stupid a fad; I put soot on warts'),
        (True, 'A nut for a jar of tuna.'),
        (True, 'Al lets Della call Ed "Stella."'),
        (True, 'Al lets Della call Ed “Stella.”'),
        (True, 'Are we not pure? "No, sir!" Panama\'s moody Noriega brags. "It is garbage!" Irony dooms a man—a prisoner up to new era.'),
        (True, 'Are we not pure? “No, sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man—a prisoner up to new era.'),
        (False, 'tacacot'),
        (False, 'afghha'),
        (False, 'racecars'),
    ]
    from lab17_functions import run_tests_p

    print(run_tests_p(test_data, check_palindrome)) # *** uncomment this line to run the unit tests ***
