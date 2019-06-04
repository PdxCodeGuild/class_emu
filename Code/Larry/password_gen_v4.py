# password_gen_v4.py
# Generate a password based on the number of characters of each "type" as specified by the user

'''
Intro Class > Lab 7: Password Generator
Let's generate a password ten characters long using a loop (while loop or for loop) and random.choice,
this will be a string of random characters.

Allow the user to choose how many letters, numbers, and punctuation characters they want in their password.
Mix everything up using list(), random.shuffle(), and ''.join().

v4: I'm using list.pop() instead of random.choice()
'''

# Import the string variable and the random functions
import string
import random

### LETTERS ###
# Ask the user to choose how many ascii_letters will be included in the password.
# While loop: Ensure the user input is within range. (Error handling)
while True:
    input_length1 = int(input("How many ASCII_LETTERS do you want in the password. Enter a value from 1 - 52: "))
    if input_length1 > 0:
        if input_length1 < 53:
            break
        else:
            print(f"Try Again! You entered {input_length1}. The value must be between 1 and 52.")
    else:
        print(f"Try Again! You entered {input_length1}. The value must be between 1 and 52.")
# Create a list from string.ascii_letters
string_ascii_letters = list(string.ascii_letters)
# For loop: Create a list of letters randomly chosen from the string_ascii_letters list and quantity from user input.
out_string1 = ''
for num in range(input_length1):
    out_string1 += string_ascii_letters.pop()
letters_list = list(out_string1)

### NUMBERS ###
# Ask the user to choose how many numbers will be included in the password.
# While loop: Ensure the user input is within range. (Error handling)
while True:
    input_length2 = int(input("How many NUMBERS do you want in the password. Enter a value from 1 - 10: "))
    if input_length2 > 0:
        if input_length2 < 11:
            break
        else:
            print(f"Try Again! You entered {input_length2}. The value must be between 1 and 10.")
    else:
        print(f"Try Again! You entered {input_length2}. The value must be between 1 and 10.")
# Create a list from string.digits
string_digits = list(string.digits)
# For loop: Create a list of numbers randomly chosen from the string_digits list and quantity from user input.
out_string2 = ''
for num in range(input_length2):
    out_string2 += string_digits.pop()
numbers_list = list(out_string2)

### PUNCTUATION ###
# Ask the user to choose how many punctuation marks will be included in the password.
# While loop: Ensure the user input is within range. (Error handling)
while True:
    input_length3 = int(input("How many PUNCTUATION MARKS do you want in the password. Enter a value from 1 - 32: "))
    if input_length3 > 0:
        if input_length3 < 33:
            break
        else:
            print(f"Try Again! You entered {input_length3}. The value must be between 1 and 32.")
    else:
        print(f"Try Again! You entered {input_length3}. The value must be between 1 and 32.")
# Create a list from string.punctuation
string_punctuation = list(string.punctuation)
# For loop: Create a list of punctuation marks randomly chosen from the string_punctuation list and quantity from user input.
out_string3 = ''
for num in range(input_length3):
    out_string3 += string_punctuation.pop()
punctuation_list = list(out_string3)

### COMBINE, SHUFFLE, PRINT ###
# Combine the list in order: letters, numbers, punctuation marks
lists_concatenate = letters_list + numbers_list + punctuation_list

# Shuffle the letters, numbers, and punctuation marks
random.shuffle(lists_concatenate)

# Convert from list back to a string and print the result
print("".join(lists_concatenate))
