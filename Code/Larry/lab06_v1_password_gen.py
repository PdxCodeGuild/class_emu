# lab06_v1_password_gen.py
'''
Lab 6: Password Generator
Let's generate a 10-character password using a while loop and random.choice, this will be a string of random characters.

Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.
'''
# import the string variable and random function
import string
import random

# get the characters to choose from from string()
letters = string.ascii_letters      # UPPER and lower case letters, a-Z
digits = str(string.digits)         # integers, 0-9
punctuation = string.punctuation    # punctuation, !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
letters_digits_punctuation = letters + digits + punctuation # combine letters, digits, punctuation into one string

counter = 0
your_password = ''
while counter < 10:
    your_password += random.choice(letters_digits_punctuation)
    counter = counter + 1
# Print the 10-character password
print(your_password)
