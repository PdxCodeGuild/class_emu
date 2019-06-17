# filename: lab13_v2_rot_cipher.py
'''
Lab 13: ROT Cipher

Write a program that prompts the user for a string, and encodes it with ROT13.
For each character, find the corresponding character, add it to an output string.
Notice that there are 26 letters in the English language,
so encryption is the same as decryption.

Version 2 (optional)
Allow the user to input the amount of rotation used in the encryption / decryption.
'''
# import the string libraries
import string

# Set variables
# Create base_alphabet from string library
base_alphabet = string.ascii_lowercase
# prompt the user for a string
user_string = input("Enter a lowercase word to ROT encrypt: ")
while True:
    amount_of_rotation = int(input("Enter the amount (1 - 26): "))
    if amount_of_rotation < 1 or amount_of_rotation > 26:
        print("Invalid amount. Try again!")
    else:
        break

# Part of solution 1
# Generate rotN_alphabet based on base_alphabet
rotN_alphabet_list = []
for letter in base_alphabet:
    rotN_alphabet_list.append(base_alphabet[(base_alphabet.find(letter) + amount_of_rotation) % 26]) # uses index for base_alphabet list
    rotN_alphabet = ''.join(rotN_alphabet_list)

# for each character, find the corresponding character
rotN_letters = []
for letter in user_string:
    id_for_letter = base_alphabet.find(letter)                              # part of solution 1
    # orig_id_for_letter = base_alphabet.find(letter)                       # part of solution 2
    # calculate the offset position                                         # part of solution 2
    # new_id_for_letter = (orig_id_for_letter + amount_of_rotation) % 26    # part of solution 2
    # add corresponding character to an output string
    rotN_letters.append(rotN_alphabet[id_for_letter])                       # part of solution 1
    # rotN_letters.append(base_alphabet[new_id_for_letter])                 # part of solution 2
    # convert list to string
    rotN_string = ''.join(rotN_letters)

# print
print(f"ROT{amount_of_rotation}: '{rotN_string}'")
