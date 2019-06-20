# filename: lab17_palindrome.py
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
    user_word = user_word.replace(" ", "").lower()
    # for letter in user_word:
    #     if letter in string.punctuation:
    #         user_word = user_word.replace(letter, "")
    for letter in user_word:
        if letter not in string.ascii_lowercase:
            user_word = user_word.replace(letter, "")

    # Loop through each letter in the user_word
    letter_not_matched = 0
    for i in range(len(user_word)):

        # Check if 1st letter=last letter, 2nd letter=2nd to last, etc
        if user_word[i] != user_word[(-1-i)]:
            letter_not_matched += 1

    # If any of letters don't match, return False, else return True
    if letter_not_matched == 0:
        return True
    return False

# Get user input
user_word = input("[Palindrome] Enter a word: ")

if check_palindrome(user_word) == True:
    print(f"'{user_word}' is a palindrome.")
else:
    print(f"'{user_word}' is a not palindrome.")


### UNIT TESTS ###
'''
Source: https://www.grammarly.com/blog/16-surprisingly-funny-palindromes/
Pass: True <= racecar
Pass: False <= racecars
Pass: True <= Race car
Pass: True <= Race car!
Pass: True <= Taco cat
Pass: True <= Yo, banana boy!
Pass: True <= Ed, I saw Harpo Marx ram Oprah W. aside.
Pass: True <= Do geese see God?
Pass: True <= A man, a plan, a canal: Panama.
Pass: True <= Straw? No, too stupid a fad; I put soot on warts.
Pass: True <= A nut for a jar of tuna.
Pass: True <= Al lets Della call Ed "Stella."
Pass: True <= Al lets Della call Ed “Stella.”
Pass: True <= Are we not pure? "No, sir!" Panama's moody Noriega brags. "It is garbage!" Irony dooms a man—a prisoner up to new era.
Pass: True <= Are we not pure? “No, sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man—a prisoner up to new era.
'''
