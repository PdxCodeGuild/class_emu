# lab17_palindrome_and_anagram.py
'''
Lab 17: Palindrome and Anagram
Let's write a palindrome and anagram checker.

Palindrome
A palindrome is a word that's the same forwards or backwards, e.g. racecar.
Another way to think of it is as a word that's equal to its own reverse.

Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.

>>> enter a word: racecar
>>> 'racecar' is a palindrome

>>> enter a word: palindrome
>>> 'palindrome' is not a palindrome
'''

print("Lets check a word to see if it's a palindrome! ") # prints a statement
user_word = input("Enter the word to check if it is a palindrome: ").lower() # prompts user for input and converts it to lowercase
user_word_rev = reversed(user_word) # defines variable as the reverse of the other variable
if list(user_word) == list(user_word_rev): # if statement to check if user_word equals the reversed version of user_word
    print("Yes!  This is a palindrome! ") # if the above is True, prints this message.
else:
    print("Sorry, this is not a palindrome. Please try again if you want. ") # if the above is False, prints this message.

'''
Anagram
Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.

Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:

Convert each word to lower case (lower)
Remove all the spaces from each word (replace)
Sort the letters of each word (sorted)
Check if the two are equal
>>> enter the first word: anagram
>>> enter the second word: nag a ram
>>> 'anagram' and 'nag a ram' are anagrams
'''

print("Lets check 2 words to see if they are anagrams! ") # prints a statement
user_word_1 = input("Enter the first word to be checked: ").lower().replace(" ", "") # prompts user for input, converts to lowercase, replaces any spaces to account for user entering spaces.
user_word_2 = input("Enter the second word to be checked against the first word: ").lower().replace(" ", "")
if(sorted(user_word_1) == sorted(user_word_2)): # if statement to check if the sorted word 1 equals the sorted word 2 (*Note: sorted puts the string into a list automatically)
    print("Yes!  This is a anagram! ") # if the above is True, prints message.
else:
    print("Sorry, this is not a anagram. Please try again if you want to find a anagram. ") # if the above is False, prints this message.
