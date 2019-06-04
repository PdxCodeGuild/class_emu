# password_gen.py

'''
Lab 7: Password Generator
Let's generate a password ten characters long using a loop (while loop or for loop) and random.choice,
this will be a string of random characters.

Allow the user to choose how many letters, numbers, and punctuation characters they want in their password.
Mix everything up using list(), random.shuffle(), and ''.join().

>>> list('asfd')
['a', 's', 'f', 'd']
>>> random.shuffle()
>>> ''.join()
'''
# import the string variable and random function
import string
import random

# get the characters to choose from from string()
letters_list = string.ascii_letters
# Ask the user to choose how many ascii_letters will be included in the password.
length1 = input("How many ASCII_LETTERS do you want in the password. Enter a number between 1 - 52: ")
out_string1 = ''
for num in range(int(length1)):
    out_string1 += random.choice(letters_list)
    my_ascii = list(out_string1)

digits_list = str(string.digits)
# Ask the user to choose how many digits will be included in the password.
length2 = input("How many DIGITS do you want in the password. Enter a number between 1 - 10: ")
out_string2 = ''
for num in range(int(length2)):
    out_string2 += random.choice(digits_list)
    my_digits = list(out_string2)

punctutation_list = string.punctuation
# Ask the user to choose how many punctuation will be included in the password.
length3 = input("How many PUNCTUATION do you want in the password. Enter a number between 1 - 32: ")
out_string3 = ''
for num in range(int(length3)):
    out_string3 += random.choice(punctutation_list)
    my_punctuation = list(out_string3)

# Generate a password based on the number of characters specified by the user
# It starts letters, then numbers, then punctuation
list_concatenate = my_ascii + my_digits + my_punctuation

# shuffle the letters, numbers, and punctuation
random.shuffle(list_concatenate)

# print the result
print("".join(list_concatenate))

# QUESTION: how do I make sure there aren't duplicates in any of the lists?
# pop() would work but I need to know the index of the item that was selected in the random.choice.
