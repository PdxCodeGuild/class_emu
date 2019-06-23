# lab13_ROT13_V1.py
'''
Lab 13: ROT Cipher
** Version 1 **
Write a program that prompts the user for a string, and encodes it with ROT13.
For each character, find the corresponding character, add it to an output string.
Notice that there are 26 letters in the English language, so encryption is the same as decryption.

Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m
'''
# def rot13(text):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     rot13_alphabet = 'nopqrstuvwxyzabcdefghijklm'
#     output = ''
#     for char in text:
#         index = alphabet.find(char)
#         output += rot13_alphabet[index]
#     return output
# user_input = input('What text would you like scrambled using rot13? ')
# print('Here you go, use the rot13 text below! ')
# print(rot13(user_input))

# NOTE: The above and below are just 2 different ways to write the code to accomplish the task

def rot13(text): # defines a funtion called rot13.  Note: Functions can be called upon even outside of this file
    alphabet = 'abcdefghijklmnopqrstuvwxyz' # defines variable alphabet as a string containing the alphabet
    output = '' # defines variable ouput as an empty string
    for char in text: # for each character in the text, it runs the following code
       output += alphabet[(alphabet.find(char)+13)%26] # finds/checks the character in the alphabet, adds 13 then adds it to the output
       # (%26 makes sure it doesn't go past 26 characters and starts back at the beginning of the alphabet)
    return output
user_input = input('What text would you like scrambled using rot13? ')
print('Here you go, use the rot13 text below! ')
print(rot13(user_input)) # takes the user input and applies the above defined function on it, then prints the result
