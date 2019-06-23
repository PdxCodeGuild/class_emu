# lab13_ROT13_V2.py
'''
Lab 13: ROT Cipher

** Version 2 (optional) **
Allow the user to input the amount of rotation used in the encryption / decryption.
'''
def user_rot(text, n): # defines a funtion called user rot with 2 parameters.  Note: Functions can be called upon even outside of this file
    alphabet = 'abcdefghijklmnopqrstuvwxyz' # defines variable alphabet as a string containing the alphabet
    output = '' # defines variable ouput as an empty string
    for char in text: # for each character in the text, it runs the following code
       output += alphabet[(alphabet.find(char)+n)%26]# finds/checks the character in the alphabet, adds the users input to it then adds it to the output
       # (%26 makes sure it doesn't go past 26 characters and starts back at the beginning of the alphabet)
    return output
user_input = int(input('How many characters would you like to scramble by "rot" ? ')) # defines variable, prompts user for input and converts it to integer
user_input2 = input(f'What text would you like scrambled by "rot{user_input}" ? ') # defines variable, prompts user for input text.  F strings runs {} as code.
print(f'Here you go, use the rot{user_input} text below! ') # prints the statement with F string to run {} as code
print(user_rot(user_input2, user_input)) # prints statement using the text from user and rot number from user by using the above defined function
