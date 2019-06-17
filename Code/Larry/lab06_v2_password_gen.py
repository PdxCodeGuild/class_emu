# lab06_v2_password_gen.py
'''
Lab 6: Password Generator
Let's generate a 10-character password using a while loop and random.choice, this will be a string of random characters.

Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

Version 2
Allow the user to enter the value of n, remember to convert its type, as input returns a string.
'''
# import the string variable and random function
import string
import random

# get the characters to choose from from string()
letters = string.ascii_letters      # UPPER and lower case letters, a-Z
digits = str(string.digits)         # integers, 0-9
punctuation = string.punctuation   # punctuation, !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
letters_digits_punctuation = letters + digits + punctuation

while True:
    # Get the password length from the user
    user_input = input("How many characters in the password? (1 or greater): ")
    # validate user input
    if user_input.isdigit():                # check if input is an integer
        if int(user_input) >= 1:            # check if input is a positive integer < 0
            user_input = int(user_input)    # if so, convert string to integer
            counter = 0                     # set base value for counter integer
            your_password = ''              # set base value for your_password string
            while counter < user_input:     # Loop through n times to create an n-character password
                your_password += random.choice(letters_digits_punctuation) # pick a random character
                counter = counter + 1       # increment the counter
            break                           # break out of the outer while loop and print

# Print the n-character password
print(your_password)
