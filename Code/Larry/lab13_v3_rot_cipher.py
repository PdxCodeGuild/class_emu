# filename: lab13_v3_rot_cipher.py
'''
Lab 13: ROT Cipher

Write a program that prompts the user for a string, and encodes it with ROT13.
For each character, find the corresponding character, add it to an output string.
Notice that there are 26 letters in the English language,
so encryption is the same as decryption.

Version 2 (optional)
Allow the user to input the amount of rotation used in the encryption / decryption.

Bonus Version by Larry
Allow users to input UPPER + lowercase letters, numbers, punctuation
'''
# import the string libraries
import string

# Set variables
# Create base_char_set (UPPER + lowercase letters, numbers, punctuation) from string library
base_char_set = string.ascii_letters + string.digits + string.punctuation
len_base_char_set = len(base_char_set)

# prompt the user for a string
user_string = input("Enter a string to ROT encrypt: ")
while True:
    amount_of_rotation = int(input("Enter the amount (1 - 94): "))
    if amount_of_rotation < 1 or amount_of_rotation > len_base_char_set:
        print("Invalid amount. Try again!")
    else:
        break

# Generate rotN_chars based on base_char_set
rotN_chars_list = []
for char in base_char_set:
    rotN_chars_list.append(chr((ord(char) - ord('!') + amount_of_rotation) % len_base_char_set + ord('!')))
    rotN_chars = ''.join(rotN_chars_list)

# for each character, find the corresponding character
rotN_characters = []
for char in user_string:
    id_for_char = base_char_set.find(char)
    # add corresponding character to an output string
    rotN_characters.append(rotN_chars_list[id_for_char])
    # convert list to string
    rotN_string = ''.join(rotN_characters)

# print
print(f"ROT{amount_of_rotation}: {rotN_string}")
