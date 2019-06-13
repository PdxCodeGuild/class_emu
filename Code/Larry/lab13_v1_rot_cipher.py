# filename: lab13_v1_rot_cipher.py
'''
Lab 13: ROT Cipher

Write a program that prompts the user for a string, and encodes it with ROT13.
For each character, find the corresponding character, add it to an output string.
Notice that there are 26 letters in the English language,
so encryption is the same as decryption.

Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m
'''
import string
# Create base_alphabet from string library
base_alphabet = string.ascii_lowercase
# Generate rot13_alphabet based on base_alphabet # rot13_alphabet = 'nopqrstuvwxyzabcdefghijklm'
rot13_alphabet_list = []
for letter in base_alphabet:
    rot13_alphabet_list.append(chr((ord(letter) - ord('a') + 13) % 26 + ord('a')))
    rot13_alphabet = ''.join(rot13_alphabet_list)

# prompt the user for a string
user_string = input("Enter a string to ROT13 encrypt: ")

# for each character, find the corresponding character
rot13_letters = []
for letter in user_string:
    id_for_letter = base_alphabet.find(letter)
    # add corresponding character to an output string
    rot13_letters.append(rot13_alphabet[id_for_letter])
    # convert list to string
    rot13_string = ''.join(rot13_letters)

# print
print(f"ROT13: '{rot13_string}'")
