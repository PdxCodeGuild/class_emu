# lab06_v3_password_gen.py
'''
Lab 6: Password Generator

Let's generate a 10-character password using a while loop and random.choice,
this will be a string of random characters.

Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

Version 2
Allow the user to enter the value of n, remember to convert its type, as input returns a string.

Version 3 (optional)
Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters they'd like
in their password. Generate a password accordingly.
'''

# import the string variable and random function
import string
import random

# get the characters to choose from from string()
letters_upper = string.ascii_uppercase      # UPPERCASE letters, A-Z
letters_lower = string.ascii_lowercase      # lowercase letters, a-z
digits = string.digits                      # integers, 0-9
special_chars = string.punctuation          # punctuation, !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~

# get input and validate that (1) is an integer and (2) greater than 1
def get_integer(prompt_text):
    error_msg = "Try again. You must enter an integer >= 1."
    while True:
        try:
            num = int(input(prompt_text))
            if num < 1:
                print(error_msg)
            else:
                return num
        except ValueError:
            print(error_msg)

# use get_integer function, pass the prompt_text
user_upper = get_integer("How many uppercase letters in the password? (1 - 26): ")
user_lower = get_integer("How many lowercase letters in the password? (1 - 26): ")
user_digits = get_integer("How many integers in the password? (1 - 10): ")
user_special_chars = get_integer("How many special characters in the password? (1 - 32): ")

# loop through each character type the number of times specified in the user input (num)
your_password = []                          # set base value for your_password list
for i in range(user_upper):                 # Loop through n times to create an n-character password
    your_password.append(random.choice(letters_upper)) # pick a uppercase letter
for i in range(user_lower):                 # Loop through n times to create an n-character password
    your_password.append(random.choice(letters_lower)) # pick a random lowercase letter
for i in range(user_digits):                # Loop through n times to create an n-character password
    your_password.append(random.choice(digits)) # pick a random number
for i in range(user_special_chars):         # Loop through n times to create an n-character password
    your_password.append(random.choice(special_chars)) # pick a random special character

# Shuffle the letters, numbers, and punctuation marks
random.shuffle(your_password)

# Convert from list back to a string and print the result
your_password = "".join(your_password)
print(f"Your password is: {your_password}")
